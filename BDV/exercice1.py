"""
Exercice 1 – Nettoyage de texte
================================
Fonctions permettant de :
  1. Lire des données depuis un fichier TXT.
  2. Remplacer les adresses e-mail par « MAIL » et les numéros de téléphone par « TEL ».
  3. Supprimer les espaces en trop et les caractères spéciaux (sauf les points).
  4. Passer toutes les données en minuscules.
"""

import re


# ---------------------------------------------------------------------------
# 1. Lecture du fichier TXT
# ---------------------------------------------------------------------------

def lire_fichier(chemin: str) -> str:
    """Lit un fichier TXT et retourne son contenu sous forme de chaîne.

    Args:
        chemin: Chemin vers le fichier TXT à lire.

    Returns:
        Contenu brut du fichier.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# 2. Remplacement des e-mails et numéros de téléphone
# ---------------------------------------------------------------------------

# Motif e-mail : xxx@xxx.xxx
_PATTERN_EMAIL = re.compile(
    r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"
)

# Motifs numéros de téléphone (formats français courants)
#   • 06 12 34 56 78       • +33 6 12 34 56 78
#   • 0033612345678        • 06-12-34-56-78
_PATTERN_TELEPHONE = re.compile(
    r"(?:\+33\s?|0033\s?|0)[1-9](?:[\s.\-/]?\d{2}){4}"
)


def remplacer_emails(texte: str) -> str:
    """Remplace toutes les adresses e-mail par le token MAIL."""
    return _PATTERN_EMAIL.sub("MAIL", texte)


def remplacer_telephones(texte: str) -> str:
    """Remplace tous les numéros de téléphone par le token TEL."""
    return _PATTERN_TELEPHONE.sub("TEL", texte)


# ---------------------------------------------------------------------------
# 3. Suppression des espaces en trop et des caractères spéciaux
# ---------------------------------------------------------------------------

def supprimer_caracteres_speciaux(texte: str) -> str:
    """Supprime les caractères spéciaux en conservant les lettres, chiffres,
    espaces et points.

    Args:
        texte: Texte à nettoyer.

    Returns:
        Texte nettoyé.
    """
    # Remplacer tout caractère qui n'est pas une lettre, un chiffre, un espace
    # ou un point par un espace.
    texte = re.sub(r"[^\w\s.]", " ", texte)
    # Normaliser les espaces multiples en un seul espace.
    texte = re.sub(r"\s+", " ", texte)
    return texte.strip()


# ---------------------------------------------------------------------------
# 4. Passage en minuscules
# ---------------------------------------------------------------------------

def mettre_en_minuscules(texte: str) -> str:
    """Convertit tout le texte en minuscules."""
    return texte.lower()


# ---------------------------------------------------------------------------
# Fonction principale combinant toutes les étapes
# ---------------------------------------------------------------------------

def nettoyer_fichier(chemin: str) -> str:
    """Lit un fichier TXT et applique toutes les transformations de nettoyage.

    Étapes :
      1. Lecture du fichier.
      2. Remplacement des e-mails par MAIL.
      3. Remplacement des numéros de téléphone par TEL.
      4. Suppression des caractères spéciaux (sauf points) et des espaces en trop.
      5. Passage en minuscules.

    Args:
        chemin: Chemin vers le fichier TXT à traiter.

    Returns:
        Texte nettoyé.
    """
    texte = lire_fichier(chemin)
    texte = remplacer_emails(texte)
    texte = remplacer_telephones(texte)
    texte = supprimer_caracteres_speciaux(texte)
    texte = mettre_en_minuscules(texte)
    return texte


# ---------------------------------------------------------------------------
# Démonstration rapide
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    exemple = (
        "Bonjour, contactez-moi à john.doe@example.com ou au +33 6 12 34 56 78.\n"
        "Mon autre mail est jane_doe@mail.org  et mon second numéro : 06-98-76-54-32.\n"
        "C'est   très   important !!!\n"
    )

    print("=== Texte original ===")
    print(exemple)

    texte = remplacer_emails(exemple)
    texte = remplacer_telephones(texte)
    texte = supprimer_caracteres_speciaux(texte)
    texte = mettre_en_minuscules(texte)

    print("=== Texte nettoyé ===")
    print(texte)
