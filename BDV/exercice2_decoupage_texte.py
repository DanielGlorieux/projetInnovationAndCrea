"""
Exercice 2 - Découpage de texte (chunking)
==========================================
Fonctions de découpage de texte :
  - Découpage en blocs de n tokens
  - Découpage par phrases
  - Découpage par phrases avec chevauchement de m mots
"""

import re
from typing import List


# ---------------------------------------------------------------------------
# 1. Découpage en blocs de n tokens
# ---------------------------------------------------------------------------

def decouper_en_blocs(texte: str, n: int) -> List[str]:
    """Découpe un texte en blocs de n tokens (mots).

    La tokenisation est naïve : les tokens sont les séquences de caractères
    séparées par des espaces.  Le dernier bloc peut contenir moins de n tokens
    si le nombre total de tokens n'est pas un multiple de n.

    Args:
        texte: Texte brut à découper.
        n: Nombre de tokens par bloc (doit être > 0).

    Returns:
        Liste de chaînes, chacune contenant au plus n tokens.

    Raises:
        ValueError: Si n est inférieur ou égal à zéro.

    Exemple:
        >>> decouper_en_blocs("un deux trois quatre cinq", 2)
        ['un deux', 'trois quatre', 'cinq']
    """
    if n <= 0:
        raise ValueError("n doit être strictement positif.")

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
    """Découpe un texte en phrases individuelles.

    Une phrase est définie comme un segment terminé par un point (`.`),
    un point d'exclamation (`!`) ou un point d'interrogation (`?`).
    Les phrases vides résultant du découpage sont ignorées.

    Args:
        texte: Texte à découper.

    Returns:
        Liste de phrases, chacune nettoyée des espaces de début/fin.

    Exemple:
        >>> decouper_par_phrases("Bonjour le monde. Comment allez-vous ? Très bien.")
        ['Bonjour le monde', 'Comment allez-vous', 'Très bien']
    """
    # Séparation sur . ! ?
    phrases = re.split(r"[.!?]+", texte)
    # Nettoyer et filtrer les segments vides
    phrases = [p.strip() for p in phrases if p.strip()]
    return phrases


# ---------------------------------------------------------------------------
# 3. Découpage par phrases avec chevauchement de m mots
# ---------------------------------------------------------------------------

def decouper_phrases_avec_chevauchement(texte: str, m: int) -> List[str]:
    """Découpe un texte par phrases en ajoutant un chevauchement de m mots.

    Chaque phrase (à partir de la deuxième) est précédée des m derniers mots
    de la phrase précédente.  Cela permet de conserver le contexte entre blocs
    lors d'une ingestion dans une base de données vectorielle.

    Args:
        texte: Texte à découper.
        m: Nombre de mots de chevauchement issus de la phrase précédente
           (doit être >= 0).

    Returns:
        Liste de chaînes où chaque élément correspond à une phrase,
        éventuellement préfixée par les m derniers mots de la phrase précédente.

    Raises:
        ValueError: Si m est négatif.

    Exemple:
        >>> decouper_phrases_avec_chevauchement("un deux trois. quatre cinq six. sept huit.", 2)
        ['un deux trois', 'deux trois quatre cinq six', 'cinq six sept huit']
    """
    if m < 0:
        raise ValueError("m doit être positif ou nul.")

    phrases = decouper_par_phrases(texte)
    if not phrases:
        return []

    chunks = [phrases[0]]
    for i in range(1, len(phrases)):
        phrase_precedente = phrases[i - 1]
        mots_precedents = phrase_precedente.split()
        # Prendre les m derniers mots de la phrase précédente
        chevauchement = " ".join(mots_precedents[-m:]) if m > 0 else ""
        if chevauchement:
            chunk = chevauchement + " " + phrases[i]
        else:
            chunk = phrases[i]
        chunks.append(chunk)

    return chunks


# ---------------------------------------------------------------------------
# Démonstration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    texte_exemple = (
        "Les bases de données vectorielles stockent des embeddings. "
        "Elles permettent une recherche par similarité sémantique. "
        "Chroma et Pinecone sont deux exemples populaires. "
        "La distance cosinus est souvent utilisée pour comparer des vecteurs."
    )

    print("=== Texte original ===")
    print(texte_exemple)

    print("\n=== Blocs de 5 tokens ===")
    blocs = decouper_en_blocs(texte_exemple, 5)
    for i, b in enumerate(blocs, 1):
        print(f"  Bloc {i}: {b}")

    print("\n=== Découpage par phrases ===")
    phrases = decouper_par_phrases(texte_exemple)
    for i, p in enumerate(phrases, 1):
        print(f"  Phrase {i}: {p}")

    print("\n=== Phrases avec chevauchement de 3 mots ===")
    chunks = decouper_phrases_avec_chevauchement(texte_exemple, 3)
    for i, c in enumerate(chunks, 1):
        print(f"  Chunk {i}: {c}")
