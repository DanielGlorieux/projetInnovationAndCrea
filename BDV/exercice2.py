"""
Exercice 2 – Découpage de texte (chunking)
==========================================
Fonctions permettant de :
  1. Découper un texte en blocs de n tokens (mots).
  2. Découper un texte par phrases.
  3. Découper par phrases avec un chevauchement de m mots entre blocs consécutifs.
"""

import re
from typing import List


# ---------------------------------------------------------------------------
# 1. Découpage en blocs de n tokens
# ---------------------------------------------------------------------------

def decouper_en_blocs(texte: str, n: int) -> List[str]:
    """Découpe un texte en blocs de n tokens (mots).

    Args:
        texte: Texte à découper.
        n: Nombre de tokens par bloc.

    Returns:
        Liste de blocs, chaque bloc contenant au plus n tokens.

    Raises:
        ValueError: Si n est inférieur ou égal à zéro.
    """
    if n <= 0:
        raise ValueError("Le nombre de tokens par bloc doit être supérieur à zéro.")

    tokens = texte.split()
    blocs = []
    for i in range(0, len(tokens), n):
        bloc = " ".join(tokens[i : i + n])
        blocs.append(bloc)
    return blocs


# ---------------------------------------------------------------------------
# 2. Découpage par phrases
# ---------------------------------------------------------------------------

def decouper_par_phrases(texte: str) -> List[str]:
    """Découpe un texte en phrases.

    La séparation s'effectue sur les signes de ponctuation terminaux
    (`.`, `!`, `?`) éventuellement suivis d'espaces.

    Args:
        texte: Texte à découper.

    Returns:
        Liste de phrases non vides.
    """
    # Sépare sur '.', '!' ou '?' (signe conservé grâce au lookahead)
    phrases = re.split(r"(?<=[.!?])\s+", texte.strip())
    return [p.strip() for p in phrases if p.strip()]


# ---------------------------------------------------------------------------
# 3. Découpage par phrases avec chevauchement de m mots
# ---------------------------------------------------------------------------

def decouper_par_phrases_avec_chevauchement(texte: str, m: int) -> List[str]:
    """Découpe un texte par phrases en ajoutant un chevauchement de m mots.

    Chaque bloc contient une phrase à laquelle sont préfixés les m derniers
    mots de la phrase précédente.

    Args:
        texte: Texte à découper.
        m: Nombre de mots de chevauchement provenant de la phrase précédente.

    Returns:
        Liste de blocs avec chevauchement.

    Raises:
        ValueError: Si m est négatif.
    """
    if m < 0:
        raise ValueError("Le chevauchement doit être un entier positif ou nul.")

    phrases = decouper_par_phrases(texte)
    if not phrases:
        return []

    blocs = [phrases[0]]  # premier bloc : pas de contexte précédent
    for i in range(1, len(phrases)):
        mots_precedents = phrases[i - 1].split()
        chevauchement = " ".join(mots_precedents[-m:]) if m > 0 else ""
        if chevauchement:
            blocs.append(chevauchement + " " + phrases[i])
        else:
            blocs.append(phrases[i])
    return blocs


# ---------------------------------------------------------------------------
# Démonstration rapide
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    texte_exemple = (
        "L'intelligence artificielle transforme de nombreux secteurs. "
        "Les bases de données vectorielles jouent un rôle clé dans la recherche sémantique. "
        "Elles permettent de comparer des représentations numériques de textes. "
        "Les modèles de langage génèrent ces représentations appelées embeddings."
    )

    print("=== Texte original ===")
    print(texte_exemple)
    print()

    # 1. Découpage en blocs de 10 tokens
    blocs = decouper_en_blocs(texte_exemple, 10)
    print(f"=== Découpage en blocs de 10 tokens ({len(blocs)} blocs) ===")
    for i, b in enumerate(blocs, 1):
        print(f"  Bloc {i}: {b}")
    print()

    # 2. Découpage par phrases
    phrases = decouper_par_phrases(texte_exemple)
    print(f"=== Découpage par phrases ({len(phrases)} phrases) ===")
    for i, p in enumerate(phrases, 1):
        print(f"  Phrase {i}: {p}")
    print()

    # 3. Découpage par phrases avec chevauchement de 3 mots
    blocs_chev = decouper_par_phrases_avec_chevauchement(texte_exemple, 3)
    print(f"=== Découpage par phrases avec chevauchement de 3 mots ({len(blocs_chev)} blocs) ===")
    for i, b in enumerate(blocs_chev, 1):
        print(f"  Bloc {i}: {b}")
