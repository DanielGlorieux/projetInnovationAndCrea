"""
Exercice 3 – Métriques de similarité / distance
=================================================
Fonctions de calcul de :
  1. La similarité cosinus.
  2. La distance euclidienne.
  3. Le produit scalaire.

Chaque fonction accepte deux vecteurs représentés par des listes ou tout
objet itérable de nombres, et ne dépend que de la bibliothèque standard Python
(+ math).

Analyse de l'usage recommandé
------------------------------
Similarité cosinus
    Mesure l'angle entre deux vecteurs indépendamment de leur norme.
    → Idéale pour la **recherche sémantique** (embeddings de texte) où la
      direction du vecteur encode le sens et où les longueurs des documents
      peuvent varier fortement.

Distance euclidienne
    Mesure la distance géométrique entre deux points dans l'espace.
    → Adaptée aux espaces où la **magnitude compte** : comparaison d'images,
      clustering (k-means), recommandations basées sur des features normalisées.
      Moins robuste pour les embeddings de haute dimension (curse of
      dimensionality).

Produit scalaire (dot product)
    Combine la direction et la magnitude des vecteurs.
    → Utile lorsque les vecteurs sont déjà normalisés (dans ce cas il est
      équivalent à la similarité cosinus) ou pour des **systèmes de
      recommandation** où la popularité (magnitude) doit influencer le score.
      Souvent utilisé dans les indexes de recherche approximative (ANN) comme
      FAISS avec l'index IP (Inner Product).
"""

import math
from typing import List, Union

Vector = List[Union[int, float]]


# ---------------------------------------------------------------------------
# Fonctions utilitaires internes
# ---------------------------------------------------------------------------

def _norme(vecteur: Vector) -> float:
    """Calcule la norme (longueur) euclidienne d'un vecteur."""
    return math.sqrt(sum(x ** 2 for x in vecteur))


def _verifier_dimensions(v1: Vector, v2: Vector) -> None:
    """Vérifie que deux vecteurs ont la même dimension."""
    if len(v1) != len(v2):
        raise ValueError(
            f"Les vecteurs doivent avoir la même dimension : "
            f"{len(v1)} ≠ {len(v2)}."
        )


# ---------------------------------------------------------------------------
# 1. Similarité cosinus
# ---------------------------------------------------------------------------

def similarite_cosinus(v1: Vector, v2: Vector) -> float:
    """Calcule la similarité cosinus entre deux vecteurs.

    La similarité cosinus est définie par :
        cos(θ) = (v1 · v2) / (||v1|| × ||v2||)

    Elle vaut 1 si les vecteurs sont identiques (même direction), 0 s'ils
    sont orthogonaux, et -1 s'ils sont opposés.

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur.

    Returns:
        Valeur de similarité cosinus dans [-1, 1].

    Raises:
        ValueError: Si les vecteurs n'ont pas la même dimension ou si l'un
                    d'eux est le vecteur nul.
    """
    _verifier_dimensions(v1, v2)
    norme_v1 = _norme(v1)
    norme_v2 = _norme(v2)
    if norme_v1 == 0 or norme_v2 == 0:
        raise ValueError("La similarité cosinus n'est pas définie pour un vecteur nul.")
    produit = sum(a * b for a, b in zip(v1, v2))
    return produit / (norme_v1 * norme_v2)


# ---------------------------------------------------------------------------
# 2. Distance euclidienne
# ---------------------------------------------------------------------------

def distance_euclidienne(v1: Vector, v2: Vector) -> float:
    """Calcule la distance euclidienne entre deux vecteurs.

    La distance euclidienne est définie par :
        d(v1, v2) = sqrt(Σ (v1_i - v2_i)²)

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur.

    Returns:
        Distance euclidienne (valeur positive ou nulle).

    Raises:
        ValueError: Si les vecteurs n'ont pas la même dimension.
    """
    _verifier_dimensions(v1, v2)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))


# ---------------------------------------------------------------------------
# 3. Produit scalaire
# ---------------------------------------------------------------------------

def produit_scalaire(v1: Vector, v2: Vector) -> float:
    """Calcule le produit scalaire (dot product) de deux vecteurs.

    Le produit scalaire est défini par :
        v1 · v2 = Σ (v1_i × v2_i)

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur.

    Returns:
        Valeur du produit scalaire.

    Raises:
        ValueError: Si les vecteurs n'ont pas la même dimension.
    """
    _verifier_dimensions(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))


# ---------------------------------------------------------------------------
# Démonstration rapide
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    v3 = [1, 2, 3]   # identique à v1
    v4 = [-1, -2, -3]  # opposé à v1

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}  (identique à v1)")
    print(f"v4 = {v4}  (opposé à v1)")
    print()

    print("=== Similarité cosinus ===")
    print(f"  cos(v1, v2) = {similarite_cosinus(v1, v2):.4f}")
    print(f"  cos(v1, v3) = {similarite_cosinus(v1, v3):.4f}  (attendu : 1.0)")
    print(f"  cos(v1, v4) = {similarite_cosinus(v1, v4):.4f}  (attendu : -1.0)")
    print()

    print("=== Distance euclidienne ===")
    print(f"  d(v1, v2) = {distance_euclidienne(v1, v2):.4f}")
    print(f"  d(v1, v3) = {distance_euclidienne(v1, v3):.4f}  (attendu : 0.0)")
    print()

    print("=== Produit scalaire ===")
    print(f"  v1 · v2 = {produit_scalaire(v1, v2):.4f}")
    print(f"  v1 · v3 = {produit_scalaire(v1, v3):.4f}")
    print()

    print("=== Quelle métrique pour quel type de recherche ? ===")
    print(
        "  • Similarité cosinus  → Recherche sémantique sur embeddings de texte\n"
        "    (la direction encode le sens, indépendamment de la longueur du doc).\n"
        "  • Distance euclidienne → Clustering, recherche dans des espaces\n"
        "    basse dimension où la magnitude est significative (ex. images).\n"
        "  • Produit scalaire    → Systèmes de recommandation ou recherche ANN\n"
        "    avec vecteurs déjà normalisés (équivalent cosinus) ou lorsque\n"
        "    la popularité (magnitude) doit influencer le score."
    )
