"""
Exercice 1 - Nettoyage de texte
================================
Fonctions de prétraitement d'un fichier TXT :
  - Lecture du fichier
  - Remplacement des adresses email par « MAIL »
  - Remplacement des numéros de téléphone par « TEL »
  - Suppression des espaces en trop et des caractères spéciaux (sauf les points)
  - Conversion en minuscules
"""

import re


# ---------------------------------------------------------------------------
# 1. Lecture du fichier TXT
# ---------------------------------------------------------------------------

def lire_fichier(chemin_fichier: str) -> str:
    """Lit un fichier texte et retourne son contenu sous forme de chaîne.

    Args:
        chemin_fichier: Chemin vers le fichier TXT à lire.

    Returns:
        Contenu brut du fichier.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        OSError: En cas d'erreur de lecture.
    """
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# 2. Remplacement des emails
# ---------------------------------------------------------------------------

def remplacer_emails(texte: str) -> str:
    """Remplace toutes les adresses email par le mot « MAIL ».

    Pattern reconnu : caractères alphanumériques/._+- @ domaine . extension
    Exemple : jean.dupont@example.com → MAIL

    Args:
        texte: Texte brut à traiter.

    Returns:
        Texte avec les emails remplacés.
    """
    pattern_email = r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"
    return re.sub(pattern_email, "MAIL", texte)


# ---------------------------------------------------------------------------
# 3. Remplacement des numéros de téléphone
# ---------------------------------------------------------------------------

def remplacer_telephones(texte: str) -> str:
    """Remplace les numéros de téléphone par le mot « TEL ».

    Formats reconnus (numéros français) :
      - 06 12 34 56 78
      - 06-12-34-56-78
      - 0612345678
      - +33 6 12 34 56 78
      - +33612345678
      - 0033 6 12 34 56 78

    Args:
        texte: Texte brut à traiter.

    Returns:
        Texte avec les numéros de téléphone remplacés.
    """
    pattern_tel = (
        r"(?:"
        r"\+33\s?|"          # préfixe international +33 optionnel
        r"0033\s?|"          # préfixe international 0033 optionnel
        r"0"                 # ou indicatif national 0
        r")"
        r"[1-9]"             # premier chiffre significatif (1-9)
        r"(?:[\s.\-/]?\d{2}){4}"  # 4 groupes de 2 chiffres séparés optionnellement
    )
    return re.sub(pattern_tel, "TEL", texte)


# ---------------------------------------------------------------------------
# 4. Suppression des caractères spéciaux et espaces en trop
# ---------------------------------------------------------------------------

def nettoyer_texte(texte: str) -> str:
    """Supprime les caractères spéciaux (sauf les points) et les espaces en trop.

    Étapes :
      1. Suppression des caractères non alphanumériques sauf espaces et points.
      2. Remplacement des séquences d'espaces blancs multiples par un seul espace.
      3. Suppression des espaces en début et fin de chaîne.

    Args:
        texte: Texte à nettoyer.

    Returns:
        Texte nettoyé.
    """
    # Garder uniquement lettres, chiffres, espaces et points
    texte = re.sub(r"[^\w\s.]", " ", texte)
    # Réduire les espaces multiples à un seul
    texte = re.sub(r"\s+", " ", texte)
    return texte.strip()


# ---------------------------------------------------------------------------
# 5. Conversion en minuscules
# ---------------------------------------------------------------------------

def mettre_en_minuscules(texte: str) -> str:
    """Convertit l'intégralité du texte en minuscules.

    Args:
        texte: Texte à convertir.

    Returns:
        Texte en minuscules.
    """
    return texte.lower()


# ---------------------------------------------------------------------------
# 6. Pipeline complet
# ---------------------------------------------------------------------------

def traiter_fichier(chemin_fichier: str) -> str:
    """Pipeline complet de nettoyage d'un fichier TXT.

    Enchaîne dans l'ordre :
      1. Lecture du fichier
      2. Remplacement des emails par MAIL
      3. Remplacement des numéros de téléphone par TEL
      4. Conversion en minuscules
      5. Nettoyage des caractères spéciaux et espaces en trop

    Args:
        chemin_fichier: Chemin vers le fichier TXT.

    Returns:
        Texte entièrement nettoyé, ou None si le fichier est introuvable.
    """
    try:
        texte = lire_fichier(chemin_fichier)
        texte = remplacer_emails(texte)
        texte = remplacer_telephones(texte)
        texte = mettre_en_minuscules(texte)
        texte = nettoyer_texte(texte)
        return texte
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable → {chemin_fichier}")
        return None
    except Exception as e:
        print(f"Erreur lors du traitement : {e}")
        return None


# ---------------------------------------------------------------------------
# Démonstration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os

    chemin = os.path.join(os.path.dirname(__file__), "sample_data.txt")
    resultat = traiter_fichier(chemin)

    if resultat:
        print("=== Texte nettoyé ===")
        print(resultat)
