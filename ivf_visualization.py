"""
Visualisation interactive et simulateur de l'algorithme Inverted File Index (IVF).

Ce script crée une interface interactive avec matplotlib pour illustrer
le fonctionnement de l'algorithme IVF utilisé dans les bases de données vectorielles.

Fonctionnalités :
    - Génération de vecteurs 2D aléatoires
    - Clustering K-means avec régions de Voronoi
    - Sliders interactifs pour ajuster nlist, nprobe, top-k et le nombre de vecteurs
    - Clic pour placer un vecteur requête et voir la recherche en action
    - Boutons pour les phases d'indexation et de recherche pas-à-pas
    - Affichage des posting lists et des résultats de recherche

Usage :
    python3 ivf_visualization.py

Prérequis :
    pip install matplotlib numpy scipy scikit-learn
"""

import numpy as np
import matplotlib
import importlib

# Select a GUI backend when running standalone.
# If a backend was explicitly set before import (e.g. Agg for headless/testing),
# we skip the selection to avoid overriding it.
_current = matplotlib.get_backend()
if _current.lower() in ("agg", ""):
    for _backend in ("TkAgg", "QtAgg", "Qt5Agg"):
        try:
            # Verify the backend module can actually be imported before selecting it
            mod_name = f"matplotlib.backends.backend_{_backend.lower()}"
            importlib.import_module(mod_name)
            matplotlib.use(_backend)
            break
        except (ImportError, ModuleNotFoundError):
            continue
    # If none worked, Agg remains (headless — no interactive widgets)

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.collections import PatchCollection
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


# ---------------------------------------------------------------------------
# Couleurs du thème (palette cohérente)
# ---------------------------------------------------------------------------
COLORS = [
    "#e6194b",
    "#3cb44b",
    "#4363d8",
    "#f58231",
    "#911eb4",
    "#42d4f4",
    "#f032e6",
    "#bfef45",
    "#fabed4",
    "#469990",
    "#dcbeff",
    "#9A6324",
    "#fffac8",
    "#800000",
    "#aaffc3",
    "#808000",
    "#ffd8b1",
    "#000075",
    "#a9a9a9",
    "#e6beff",
]

CLUSTER_ALPHA = 0.15
POINT_SIZE = 30
CENTROID_SIZE = 150
QUERY_SIZE = 200
RESULT_SIZE = 80


class IVFSimulator:
    """Simulateur interactif de l'algorithme IVF."""

    def __init__(self, n_vectors=200, nlist=5, nprobe=2, top_k=5, seed=42):
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.n_vectors = n_vectors
        self.nlist = nlist
        self.nprobe = nprobe
        self.top_k = top_k

        # Données
        self.vectors = None
        self.labels = None
        self.centroids = None
        self.posting_lists = None
        self.kmeans = None

        # État de la recherche
        self.query_point = None
        self.searched_clusters = []
        self.candidate_ids = []
        self.top_k_ids = []
        self.phase = "idle"  # idle, indexed, querying, results

        # Générer les données et indexer
        self._generate_data()
        self._build_index()

        # Interface matplotlib
        self._setup_figure()
        self._draw()

    # ------------------------------------------------------------------
    # Génération et indexation
    # ------------------------------------------------------------------
    def _generate_data(self):
        """Génère des vecteurs 2D aléatoires avec des groupes naturels."""
        n_groups = max(3, self.nlist)
        centers = self.rng.uniform(1, 9, size=(n_groups, 2))
        points_per_group = self.n_vectors // n_groups
        remainder = self.n_vectors - points_per_group * n_groups

        all_points = []
        for i in range(n_groups):
            n_pts = points_per_group + (1 if i < remainder else 0)
            spread = self.rng.uniform(0.3, 0.8)
            pts = self.rng.normal(loc=centers[i], scale=spread, size=(n_pts, 2))
            all_points.append(pts)

        self.vectors = np.vstack(all_points)
        # Clamp to [0, 10]
        self.vectors = np.clip(self.vectors, 0, 10)

    def _build_index(self):
        """Construit l'index IVF via K-means clustering."""
        actual_nlist = min(self.nlist, len(self.vectors))
        self.kmeans = KMeans(
            n_clusters=actual_nlist, random_state=self.seed, n_init=10
        )
        self.labels = self.kmeans.fit_predict(self.vectors)
        self.centroids = self.kmeans.cluster_centers_

        # Construire les posting lists
        self.posting_lists = {}
        for cluster_id in range(actual_nlist):
            ids = np.where(self.labels == cluster_id)[0].tolist()
            self.posting_lists[cluster_id] = ids

    def _search(self, query):
        """Effectue une recherche IVF pour le vecteur requête."""
        # Étape 1 : Trouver les nprobe centroïdes les plus proches
        dists_to_centroids = cdist([query], self.centroids, metric="euclidean")[0]
        actual_nprobe = min(self.nprobe, len(self.centroids))
        self.searched_clusters = np.argsort(dists_to_centroids)[:actual_nprobe].tolist()

        # Étape 2 : Collecter les candidats des clusters sélectionnés
        self.candidate_ids = []
        for cluster_id in self.searched_clusters:
            self.candidate_ids.extend(self.posting_lists[cluster_id])

        # Étape 3 : Trouver les top-k plus proches voisins parmi les candidats
        if self.candidate_ids:
            candidate_vectors = self.vectors[self.candidate_ids]
            dists = cdist([query], candidate_vectors, metric="euclidean")[0]
            actual_k = min(self.top_k, len(self.candidate_ids))
            top_k_local = np.argsort(dists)[:actual_k]
            self.top_k_ids = [self.candidate_ids[i] for i in top_k_local]
        else:
            self.top_k_ids = []

    # ------------------------------------------------------------------
    # Interface graphique
    # ------------------------------------------------------------------
    def _setup_figure(self):
        """Configure la figure matplotlib et tous les widgets."""
        self.fig = plt.figure(figsize=(16, 10), facecolor="#1a1a2e")
        self.fig.canvas.manager.set_window_title(
            "IVF - Visualisation Interactive | Inverted File Index Simulator"
        )

        # Zone principale (visualisation)
        self.ax_main = self.fig.add_axes([0.05, 0.22, 0.55, 0.72])
        self.ax_main.set_facecolor("#16213e")

        # Zone d'information (panneau droit)
        self.ax_info = self.fig.add_axes([0.65, 0.22, 0.32, 0.72])
        self.ax_info.set_facecolor("#1a1a2e")
        self.ax_info.axis("off")

        # --- Sliders ---
        slider_color = "#0f3460"
        slider_kwargs = dict(
            valfmt="%d",
            color="#e94560",
            initcolor="none",
        )

        ax_nlist = self.fig.add_axes([0.08, 0.12, 0.40, 0.03])
        self.slider_nlist = Slider(
            ax_nlist,
            "nlist (clusters)",
            2,
            20,
            valinit=self.nlist,
            valstep=1,
            **slider_kwargs,
        )
        self.slider_nlist.on_changed(self._on_nlist_changed)

        ax_nprobe = self.fig.add_axes([0.08, 0.08, 0.40, 0.03])
        self.slider_nprobe = Slider(
            ax_nprobe,
            "nprobe (search)",
            1,
            20,
            valinit=self.nprobe,
            valstep=1,
            **slider_kwargs,
        )
        self.slider_nprobe.on_changed(self._on_nprobe_changed)

        ax_topk = self.fig.add_axes([0.08, 0.04, 0.40, 0.03])
        self.slider_topk = Slider(
            ax_topk,
            "top-k (results)",
            1,
            20,
            valinit=self.top_k,
            valstep=1,
            **slider_kwargs,
        )
        self.slider_topk.on_changed(self._on_topk_changed)

        # --- Boutons ---
        ax_regen = self.fig.add_axes([0.55, 0.12, 0.12, 0.04])
        self.btn_regenerate = Button(
            ax_regen, "Régénérer", color="#0f3460", hovercolor="#e94560"
        )
        self.btn_regenerate.on_clicked(self._on_regenerate)
        self.btn_regenerate.label.set_color("white")
        self.btn_regenerate.label.set_fontsize(10)

        ax_reset = self.fig.add_axes([0.55, 0.07, 0.12, 0.04])
        self.btn_reset_query = Button(
            ax_reset, "Reset Requête", color="#0f3460", hovercolor="#e94560"
        )
        self.btn_reset_query.on_clicked(self._on_reset_query)
        self.btn_reset_query.label.set_color("white")
        self.btn_reset_query.label.set_fontsize(10)

        ax_brute = self.fig.add_axes([0.55, 0.02, 0.12, 0.04])
        self.btn_brute_force = Button(
            ax_brute, "Brute Force", color="#0f3460", hovercolor="#e94560"
        )
        self.btn_brute_force.on_clicked(self._on_brute_force)
        self.btn_brute_force.label.set_color("white")
        self.btn_brute_force.label.set_fontsize(10)

        # --- Titre global ---
        self.fig.text(
            0.32,
            0.96,
            "Inverted File Index (IVF) - Simulateur Interactif",
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color="white",
        )
        self.fig.text(
            0.32,
            0.935,
            "Cliquez dans la zone pour placer un vecteur requête",
            ha="center",
            va="center",
            fontsize=10,
            color="#aaaaaa",
            style="italic",
        )

        # Connecter le clic
        self.fig.canvas.mpl_connect("button_press_event", self._on_click)

    # ------------------------------------------------------------------
    # Dessin
    # ------------------------------------------------------------------
    def _draw(self):
        """Redessine toute la visualisation."""
        self._draw_main()
        self._draw_info_panel()
        self.fig.canvas.draw_idle()

    def _draw_main(self):
        """Dessine la vue principale avec les vecteurs et clusters."""
        ax = self.ax_main
        ax.clear()
        ax.set_facecolor("#16213e")
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-0.5, 10.5)
        ax.set_aspect("equal")
        ax.tick_params(colors="#666666", labelsize=8)
        for spine in ax.spines.values():
            spine.set_color("#333333")
        ax.grid(True, alpha=0.1, color="white")

        n_clusters = len(self.centroids)

        # Dessiner les régions de Voronoi
        self._draw_voronoi(ax, n_clusters)

        # Dessiner les vecteurs colorés par cluster
        for cluster_id in range(n_clusters):
            mask = self.labels == cluster_id
            color = COLORS[cluster_id % len(COLORS)]

            is_searched = cluster_id in self.searched_clusters
            alpha = 0.9 if is_searched or not self.searched_clusters else 0.2
            size = POINT_SIZE if not is_searched else POINT_SIZE * 1.3

            ax.scatter(
                self.vectors[mask, 0],
                self.vectors[mask, 1],
                c=color,
                s=size,
                alpha=alpha,
                edgecolors="white" if is_searched else "none",
                linewidth=0.5 if is_searched else 0,
                zorder=2,
                label=f"Cluster {cluster_id} ({len(self.posting_lists[cluster_id])} pts)"
                if cluster_id < 8
                else None,
            )

        # Dessiner les centroïdes
        for cluster_id in range(n_clusters):
            color = COLORS[cluster_id % len(COLORS)]
            is_searched = cluster_id in self.searched_clusters

            marker = "*"
            size = CENTROID_SIZE * 1.5 if is_searched else CENTROID_SIZE
            edge_color = "white" if is_searched else "#333333"
            edge_width = 2 if is_searched else 1

            ax.scatter(
                self.centroids[cluster_id, 0],
                self.centroids[cluster_id, 1],
                c=color,
                s=size,
                marker=marker,
                edgecolors=edge_color,
                linewidth=edge_width,
                zorder=4,
            )

            # Étiquette du centroïde
            ax.annotate(
                f"C{cluster_id}",
                (self.centroids[cluster_id, 0], self.centroids[cluster_id, 1]),
                textcoords="offset points",
                xytext=(8, 8),
                fontsize=8,
                color=color,
                fontweight="bold",
                zorder=5,
            )

        # Marquer les clusters recherchés
        if self.searched_clusters:
            for cluster_id in self.searched_clusters:
                circle = plt.Circle(
                    (self.centroids[cluster_id, 0], self.centroids[cluster_id, 1]),
                    radius=0.3,
                    fill=False,
                    color="yellow",
                    linewidth=2,
                    linestyle="--",
                    zorder=3,
                )
                ax.add_patch(circle)

        # Marquer les candidats
        if self.candidate_ids and self.query_point is not None:
            candidate_set = set(self.candidate_ids)
            topk_set = set(self.top_k_ids)
            only_candidates = candidate_set - topk_set

            if only_candidates:
                cand_array = np.array(
                    [self.vectors[i] for i in only_candidates]
                )
                ax.scatter(
                    cand_array[:, 0],
                    cand_array[:, 1],
                    facecolors="none",
                    edgecolors="cyan",
                    s=RESULT_SIZE,
                    linewidth=1.5,
                    zorder=5,
                    label=f"Candidats ({len(self.candidate_ids)})",
                )

        # Marquer les top-k résultats
        if self.top_k_ids and self.query_point is not None:
            topk_array = np.array([self.vectors[i] for i in self.top_k_ids])
            ax.scatter(
                topk_array[:, 0],
                topk_array[:, 1],
                facecolors="none",
                edgecolors="#00ff00",
                s=RESULT_SIZE * 1.5,
                linewidth=2.5,
                zorder=6,
                marker="D",
                label=f"Top-{len(self.top_k_ids)} resultats",
            )
            # Lignes vers le point de requête
            for vid in self.top_k_ids:
                ax.plot(
                    [self.query_point[0], self.vectors[vid, 0]],
                    [self.query_point[1], self.vectors[vid, 1]],
                    color="#00ff00",
                    alpha=0.4,
                    linewidth=1,
                    linestyle="--",
                    zorder=3,
                )

        # Dessiner le point de requête
        if self.query_point is not None:
            ax.scatter(
                self.query_point[0],
                self.query_point[1],
                c="red",
                s=QUERY_SIZE,
                marker="X",
                edgecolors="white",
                linewidth=2,
                zorder=7,
                label="Requete",
            )

            # Lignes vers les centroïdes recherchés
            for cluster_id in self.searched_clusters:
                ax.plot(
                    [self.query_point[0], self.centroids[cluster_id, 0]],
                    [self.query_point[1], self.centroids[cluster_id, 1]],
                    color="yellow",
                    alpha=0.6,
                    linewidth=1.5,
                    linestyle="-.",
                    zorder=3,
                )

        # Légende
        ax.legend(
            loc="upper left",
            fontsize=7,
            facecolor="#1a1a2e",
            edgecolor="#333333",
            labelcolor="white",
            framealpha=0.9,
        )

        # Titre de la zone
        status_text = "INDEX PRET"
        status_color = "#3cb44b"
        if self.query_point is not None:
            status_text = (
                f"RECHERCHE : nprobe={self.nprobe}, "
                f"top-{self.top_k} | "
                f"{len(self.candidate_ids)} candidats explores"
            )
            status_color = "#e94560"

        ax.set_title(
            status_text,
            color=status_color,
            fontsize=11,
            fontweight="bold",
            pad=10,
        )

    def _draw_voronoi(self, ax, n_clusters):
        """Dessine les régions de Voronoi pour les clusters."""
        if n_clusters < 3:
            return

        # Ajouter des points miroirs pour que le Voronoi couvre la zone
        mirror_points = np.array(
            [
                [-20, -20],
                [-20, 30],
                [30, -20],
                [30, 30],
            ]
        )
        extended_points = np.vstack([self.centroids, mirror_points])

        try:
            vor = Voronoi(extended_points)
            for region_idx, region in enumerate(vor.regions):
                if not region or -1 in region:
                    continue
                # Trouver à quel centroïde appartient cette région
                point_idx = None
                for pi, ri in enumerate(vor.point_region):
                    if ri == vor.regions.index(region) and pi < n_clusters:
                        point_idx = pi
                        break

                if point_idx is not None and point_idx < n_clusters:
                    polygon = [vor.vertices[i] for i in region]
                    color = COLORS[point_idx % len(COLORS)]
                    is_searched = point_idx in self.searched_clusters
                    alpha = 0.25 if is_searched else CLUSTER_ALPHA

                    ax.fill(
                        *zip(*polygon),
                        color=color,
                        alpha=alpha,
                        zorder=0,
                    )
        except Exception:
            pass

    def _draw_info_panel(self):
        """Dessine le panneau d'information à droite."""
        ax = self.ax_info
        ax.clear()
        ax.set_facecolor("#1a1a2e")
        ax.axis("off")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 22)

        y = 21.5

        # Titre
        ax.text(
            5,
            y,
            "ALGORITHME IVF",
            ha="center",
            fontsize=13,
            fontweight="bold",
            color="#e94560",
        )
        y -= 0.8
        ax.axhline(y=y, xmin=0.05, xmax=0.95, color="#333333", linewidth=1)
        y -= 0.6

        # Paramètres actuels
        ax.text(
            0.3,
            y,
            "Parametres actuels :",
            fontsize=10,
            fontweight="bold",
            color="#42d4f4",
        )
        y -= 0.6
        params = [
            f"  Vecteurs : {self.n_vectors}",
            f"  nlist (clusters) : {self.nlist}",
            f"  nprobe (recherche) : {self.nprobe}",
            f"  top-k : {self.top_k}",
        ]
        for p in params:
            ax.text(0.5, y, p, fontsize=9, color="white")
            y -= 0.5
        y -= 0.3

        # Posting lists
        ax.axhline(y=y, xmin=0.05, xmax=0.95, color="#333333", linewidth=1)
        y -= 0.6
        ax.text(
            0.3,
            y,
            "Posting Lists :",
            fontsize=10,
            fontweight="bold",
            color="#42d4f4",
        )
        y -= 0.6

        n_display = min(len(self.posting_lists), 12)
        for cluster_id in range(n_display):
            ids = self.posting_lists[cluster_id]
            color = COLORS[cluster_id % len(COLORS)]
            is_searched = cluster_id in self.searched_clusters
            prefix = ">> " if is_searched else "   "
            weight = "bold" if is_searched else "normal"

            id_preview = ids[:6]
            suffix = f"... +{len(ids) - 6}" if len(ids) > 6 else ""
            ids_str = ", ".join(str(i) for i in id_preview)

            ax.text(
                0.5,
                y,
                f"{prefix}C{cluster_id}: [{ids_str}{suffix}]",
                fontsize=7,
                color=color,
                fontweight=weight,
                family="monospace",
            )
            y -= 0.45

        if len(self.posting_lists) > n_display:
            ax.text(
                0.5,
                y,
                f"   ... +{len(self.posting_lists) - n_display} clusters",
                fontsize=7,
                color="#666666",
            )
            y -= 0.45

        y -= 0.3

        # Résultats de recherche
        ax.axhline(y=y, xmin=0.05, xmax=0.95, color="#333333", linewidth=1)
        y -= 0.6

        if self.query_point is not None:
            ax.text(
                0.3,
                y,
                "Resultats de recherche :",
                fontsize=10,
                fontweight="bold",
                color="#00ff00",
            )
            y -= 0.6

            ax.text(
                0.5,
                y,
                f"  Requete : ({self.query_point[0]:.2f}, {self.query_point[1]:.2f})",
                fontsize=9,
                color="red",
            )
            y -= 0.5

            clusters_str = ", ".join(f"C{c}" for c in self.searched_clusters)
            ax.text(
                0.5,
                y,
                f"  Clusters explores : {clusters_str}",
                fontsize=9,
                color="yellow",
            )
            y -= 0.5

            ax.text(
                0.5,
                y,
                f"  Candidats : {len(self.candidate_ids)} vecteurs",
                fontsize=9,
                color="cyan",
            )
            y -= 0.5

            ax.text(
                0.5,
                y,
                f"  Top-{len(self.top_k_ids)} resultats :",
                fontsize=9,
                color="#00ff00",
                fontweight="bold",
            )
            y -= 0.5

            for rank, vid in enumerate(self.top_k_ids):
                dist = np.linalg.norm(self.query_point - self.vectors[vid])
                cluster_id = self.labels[vid]
                ax.text(
                    0.7,
                    y,
                    f"#{rank + 1}  ID={vid}  C{cluster_id}  d={dist:.3f}",
                    fontsize=8,
                    color="#00ff00",
                    family="monospace",
                )
                y -= 0.45

            # Statistiques
            y -= 0.3
            total_vecs = len(self.vectors)
            explored_pct = (
                len(self.candidate_ids) / total_vecs * 100 if total_vecs > 0 else 0
            )
            ax.text(
                0.3,
                y,
                "Statistiques :",
                fontsize=10,
                fontweight="bold",
                color="#42d4f4",
            )
            y -= 0.5
            ax.text(
                0.5,
                y,
                f"  Vecteurs explores : {len(self.candidate_ids)}/{total_vecs} "
                f"({explored_pct:.1f}%)",
                fontsize=9,
                color="white",
            )
            y -= 0.5
            # Brute force comparison
            if self.top_k_ids:
                bf_dists = cdist(
                    [self.query_point], self.vectors, metric="euclidean"
                )[0]
                bf_topk = np.argsort(bf_dists)[: self.top_k].tolist()
                recall = (
                    len(set(self.top_k_ids) & set(bf_topk)) / len(bf_topk) * 100
                )
                ax.text(
                    0.5,
                    y,
                    f"  Recall vs brute force : {recall:.0f}%",
                    fontsize=9,
                    color="#ffcc00" if recall < 100 else "#00ff00",
                    fontweight="bold",
                )
                y -= 0.5
                ax.text(
                    0.5,
                    y,
                    f"  Économies : {100 - explored_pct:.1f}% des comparaisons évitées",
                    fontsize=9,
                    color="white",
                )
        else:
            ax.text(
                0.3,
                y,
                "Mode :",
                fontsize=10,
                fontweight="bold",
                color="#42d4f4",
            )
            y -= 0.6
            ax.text(
                0.5,
                y,
                "  Cliquez dans la zone de",
                fontsize=9,
                color="#aaaaaa",
            )
            y -= 0.5
            ax.text(
                0.5,
                y,
                "  visualisation pour placer",
                fontsize=9,
                color="#aaaaaa",
            )
            y -= 0.5
            ax.text(
                0.5,
                y,
                "  un vecteur requête.",
                fontsize=9,
                color="#aaaaaa",
            )
            y -= 1.0

            # Instructions
            ax.text(
                0.3,
                y,
                "Comment utiliser :",
                fontsize=10,
                fontweight="bold",
                color="#42d4f4",
            )
            y -= 0.6
            instructions = [
                "1. Ajustez nlist pour le clustering",
                "2. Cliquez pour placer une requête",
                "3. Modifiez nprobe pour explorer",
                "   plus ou moins de clusters",
                "4. Observez le recall et les",
                "   economies de calcul",
                "",
                "Regenerer : nouvelles donnees",
                "Reset : effacer la requête",
                "Brute Force : nprobe = nlist",
            ]
            for inst in instructions:
                ax.text(0.5, y, inst, fontsize=8, color="#888888")
                y -= 0.45

    # ------------------------------------------------------------------
    # Callbacks des événements
    # ------------------------------------------------------------------
    def _on_click(self, event):
        """Gère le clic pour placer un vecteur requête."""
        if event.inaxes != self.ax_main:
            return
        if event.button != 1:  # Clic gauche uniquement
            return

        self.query_point = np.array([event.xdata, event.ydata])
        self._search(self.query_point)
        self._draw()

    def _on_nlist_changed(self, val):
        """Met à jour le nombre de clusters."""
        new_nlist = int(val)
        if new_nlist != self.nlist:
            self.nlist = new_nlist
            self.slider_nprobe.valmax = max(new_nlist, 1)
            if self.nprobe > new_nlist:
                self.nprobe = new_nlist
                self.slider_nprobe.set_val(self.nprobe)
            self._build_index()
            if self.query_point is not None:
                self._search(self.query_point)
            self._draw()

    def _on_nprobe_changed(self, val):
        """Met à jour le nombre de clusters à explorer."""
        new_nprobe = int(val)
        new_nprobe = min(new_nprobe, self.nlist)
        if new_nprobe != self.nprobe:
            self.nprobe = new_nprobe
            if self.query_point is not None:
                self._search(self.query_point)
            self._draw()

    def _on_topk_changed(self, val):
        """Met à jour le nombre de résultats à retourner."""
        self.top_k = int(val)
        if self.query_point is not None:
            self._search(self.query_point)
        self._draw()

    def _on_regenerate(self, event):
        """Régénère les données et reconstruit l'index."""
        self.seed += 1
        self.rng = np.random.RandomState(self.seed)
        self.query_point = None
        self.searched_clusters = []
        self.candidate_ids = []
        self.top_k_ids = []
        self._generate_data()
        self._build_index()
        self._draw()

    def _on_reset_query(self, event):
        """Réinitialise la requête."""
        self.query_point = None
        self.searched_clusters = []
        self.candidate_ids = []
        self.top_k_ids = []
        self._draw()

    def _on_brute_force(self, event):
        """Simule une recherche brute force (nprobe = nlist)."""
        if self.query_point is None:
            return
        old_nprobe = self.nprobe
        self.nprobe = self.nlist
        self.slider_nprobe.set_val(self.nlist)
        self._search(self.query_point)
        self._draw()

    # ------------------------------------------------------------------
    # Lancement
    # ------------------------------------------------------------------
    def show(self):
        """Affiche la visualisation interactive."""
        plt.show()


def main():
    """Point d'entrée principal."""
    print("=" * 60)
    print("  IVF - Visualisation Interactive")
    print("  Inverted File Index Simulator")
    print("=" * 60)
    print()
    print("Instructions :")
    print("  - Cliquez dans la zone pour placer un vecteur requête")
    print("  - Ajustez les sliders (nlist, nprobe, top-k)")
    print("  - Observez le fonctionnement de l'algorithme IVF")
    print()

    sim = IVFSimulator(n_vectors=200, nlist=5, nprobe=2, top_k=5)
    sim.show()


if __name__ == "__main__":
    main()
