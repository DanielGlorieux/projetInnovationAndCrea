"""
Exercice 3 - Métriques de similarité vectorielle
=================================================
Fonctions de calcul de :
  - Similarité cosinus
  - Distance euclidienne
  - Produit scalaire

Et discussion sur l'adéquation de chaque métrique selon le type de recherche.
"""

import math
from typing import List


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

Vector = List[float]


# ---------------------------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------------------------

def _verifier_dimensions(v1: Vector, v2: Vector) -> None:
    """Vérifie que deux vecteurs ont la même dimension.

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur.

    Raises:
        ValueError: Si les vecteurs n'ont pas la même longueur ou sont vides.
    """
    if len(v1) == 0 or len(v2) == 0:
        raise ValueError("Les vecteurs ne doivent pas être vides.")
    if len(v1) != len(v2):
        raise ValueError(
            f"Les vecteurs doivent avoir la même dimension "
            f"({len(v1)} ≠ {len(v2)})."
        )


def norme(v: Vector) -> float:
    """Calcule la norme euclidienne (L2) d'un vecteur.

    Args:
        v: Vecteur numérique.

    Returns:
        Norme L2 du vecteur.
    """
    return math.sqrt(sum(x ** 2 for x in v))


# ---------------------------------------------------------------------------
# 1. Produit scalaire (dot product)
# ---------------------------------------------------------------------------

def produit_scalaire(v1: Vector, v2: Vector) -> float:
    """Calcule le produit scalaire de deux vecteurs.

    Formule : v1 · v2 = Σ (v1[i] × v2[i])

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur (même dimension que v1).

    Returns:
        Valeur scalaire du produit.

    Raises:
        ValueError: Si les vecteurs ont des dimensions différentes ou sont vides.

    Exemple:
        >>> produit_scalaire([1, 2, 3], [4, 5, 6])
        32
    """
    _verifier_dimensions(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))


# ---------------------------------------------------------------------------
# 2. Similarité cosinus
# ---------------------------------------------------------------------------

def similarite_cosinus(v1: Vector, v2: Vector) -> float:
    """Calcule la similarité cosinus entre deux vecteurs.

    Formule : cos(θ) = (v1 · v2) / (‖v1‖ × ‖v2‖)

    La valeur est comprise entre -1 et 1 :
      - 1  : vecteurs parfaitement similaires (même direction)
      - 0  : vecteurs orthogonaux (aucune similarité)
      - -1 : vecteurs opposés

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur (même dimension que v1).

    Returns:
        Valeur de similarité cosinus.  Mathématiquement bornée à [-1, 1] ;
        des erreurs d'arrondi en virgule flottante peuvent légèrement dépasser
        ces bornes.

    Raises:
        ValueError: Si l'un des vecteurs est nul (norme = 0) ou si les
                    dimensions diffèrent.

    Exemple:
        >>> similarite_cosinus([1, 0, 0], [1, 0, 0])
        1.0
        >>> similarite_cosinus([1, 0, 0], [0, 1, 0])
        0.0
    """
    _verifier_dimensions(v1, v2)
    norme_v1 = norme(v1)
    norme_v2 = norme(v2)
    if norme_v1 == 0 or norme_v2 == 0:
        raise ValueError("La similarité cosinus n'est pas définie pour un vecteur nul.")
    return produit_scalaire(v1, v2) / (norme_v1 * norme_v2)


# ---------------------------------------------------------------------------
# 3. Distance euclidienne
# ---------------------------------------------------------------------------

def distance_euclidienne(v1: Vector, v2: Vector) -> float:
    """Calcule la distance euclidienne (L2) entre deux vecteurs.

    Formule : d(v1, v2) = √ Σ (v1[i] - v2[i])²

    La valeur est toujours positive ou nulle :
      - 0 : vecteurs identiques
      - Plus la valeur est grande, plus les vecteurs sont éloignés.

    Args:
        v1: Premier vecteur.
        v2: Deuxième vecteur (même dimension que v1).

    Returns:
        Distance euclidienne.  Mathématiquement toujours ≥ 0 ; en pratique
        une valeur de 0.0 indique des vecteurs identiques.

    Raises:
        ValueError: Si les dimensions diffèrent ou si les vecteurs sont vides.

    Exemple:
        >>> distance_euclidienne([0, 0], [3, 4])
        5.0
    """
    _verifier_dimensions(v1, v2)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))


# ---------------------------------------------------------------------------
# Discussion : quelle métrique pour quel type de recherche ?
# ---------------------------------------------------------------------------

DISCUSSION_METRIQUES = """
=============================================================
  MÉTRIQUES DE SIMILARITÉ — GUIDE DE CHOIX
=============================================================

1. SIMILARITÉ COSINUS
   ──────────────────
   Mesure l'angle entre deux vecteurs, indépendamment de leur magnitude.

   ✅ Cas d'usage recommandés :
     • Recherche sémantique dans des corpus de textes (NLP/RAG).
     • Comparaison de documents dont la longueur varie (un court résumé
       vs un long article traitent du même sujet).
     • Moteurs de recommandation où l'orientation du vecteur importe
       plus que son amplitude.
     • Embeddings issus de modèles de langage (Word2Vec, BERT, etc.)
       car ces représentations encodent le sens dans la direction.

   ⚠️  Limites :
     • Insensible à la magnitude ; deux vecteurs d'intensités très
       différentes peuvent avoir une similarité cosinus élevée.

2. DISTANCE EUCLIDIENNE
   ─────────────────────
   Mesure la distance géométrique entre deux points dans l'espace.

   ✅ Cas d'usage recommandés :
     • Données métriques continues (coordonnées GPS, données capteurs).
     • Clustering (K-Means) où la distance absolue a un sens physique.
     • Recherche d'images ou de sons lorsque les vecteurs sont normalisés
       et que la magnitude est significative.
     • Modèles d'embedding où les vecteurs sont normalisés à l'avance
       (la distance euclidienne est alors équivalente à la cosinus).

   ⚠️  Limites :
     • Sensible à la magnitude ; peut pénaliser des vecteurs longs même
       s'ils pointent dans la même direction.
     • Moins efficace en haute dimension (malédiction de la dimension).

3. PRODUIT SCALAIRE (DOT PRODUCT)
   ────────────────────────────────
   Combine à la fois la direction et la magnitude des vecteurs.

   ✅ Cas d'usage recommandés :
     • Systèmes de recommandation collaboratifs (factorisation matricielle)
       où la magnitude encode la popularité ou la confiance.
     • Modèles de recherche où la pertinence dépend à la fois de la
       direction et de l'amplitude (ex. : modèles bi-encodeurs).
     • Calculs rapides lorsque les vecteurs sont déjà normalisés
       (le produit scalaire devient alors équivalent à la cosinus).

   ⚠️  Limites :
     • Pas borné : difficile à interpréter sans normalisation préalable.
     • Des vecteurs très longs peuvent dominer le score même si leur
       direction n'est pas idéale.

─────────────────────────────────────────────────────────────
RÉSUMÉ RAPIDE
─────────────────────────────────────────────────────────────
 Similarité cosinus  → recherche sémantique, NLP, RAG
 Distance euclidienne → clustering, données métriques physiques
 Produit scalaire    → recommandation, modèles bi-encodeurs
=============================================================
"""


# ---------------------------------------------------------------------------
# Démonstration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    v3 = [1.0, 2.0, 3.0]  # identique à v1

    print("=== Vecteurs de test ===")
    print(f"  v1 = {v1}")
    print(f"  v2 = {v2}")
    print(f"  v3 = {v3} (identique à v1)")

    print("\n=== Produit scalaire ===")
    print(f"  v1 · v2 = {produit_scalaire(v1, v2)}")
    print(f"  v1 · v3 = {produit_scalaire(v1, v3)}")

    print("\n=== Similarité cosinus ===")
    print(f"  cos(v1, v2) = {similarite_cosinus(v1, v2):.6f}")
    print(f"  cos(v1, v3) = {similarite_cosinus(v1, v3):.6f}")

    print("\n=== Distance euclidienne ===")
    print(f"  d(v1, v2) = {distance_euclidienne(v1, v2):.6f}")
    print(f"  d(v1, v3) = {distance_euclidienne(v1, v3):.6f}")

    print(DISCUSSION_METRIQUES)
