"""
Système RAG avec vectorisation et stockage Chroma
Utilise BGE-M3 pour le multilingue (français) et Chroma pour la persistance
"""

import re
import chroma
import chromadb
from chromadb import Client
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Any

# ============================================================================
# PARTIE 1 : NETTOYAGE DU TEXTE (Fonction précédente)
# ============================================================================


def process_text_file(file_path):
    """
    Traite un fichier TXT en remplaçant les emails et numéros de téléphone,
    supprimant les caractères spéciaux et espaces en trop, et convertissant en minuscules.
   
    Args:
        file_path (str): Chemin vers le fichier TXT à traiter
       
    Returns:
        str: Texte traité
    """
   
    try:
        # 1. Lire le fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
       
        # 2. Remplacer les adresses emails
        # Pattern: xxx@xxx.xxx
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'mail', text)
       
        # 3. Remplacer les numéros de téléphone français
        # Formats supportés:
        # - 0X XX XX XX XX (format français standard)
        # - +33 X XX XX XX XX (format international)
        # - +33X XX XX XX XX (format international sans espace)
        # - 06/07/08/09 XX XX XX XX (format avec slashes)
        # - 06 98 76 54 32, +33 9 87 65 43 21, 0033144276891, 07 11 22 33 44, etc.
       
        # Pattern pour numéros français avec différents formats
        phone_pattern = r'(?:\+33\s?|0)[1-9](?:\s|\.|-|/)?(?:\d{2}(?:\s|\.|-)?)(?:\d{2}(?:\s|\.|-)?)(?:\d{2}(?:\s|\.|-)?)?(?:\d{2})?'
        text = re.sub(phone_pattern, 'tel', text, flags=re.IGNORECASE)
       
        # 4. Passer en minuscules
        text = text.lower()
       
        # 5. Supprimer les caractères spéciaux (sauf les points)
        # Garder: lettres, chiffres, espaces, points
        text = re.sub(r'[^\w\s.\']', ' ', text)
       
        # 6. Supprimer les espaces en trop (remplacer les espaces multiples par un seul)
        text = re.sub(r'\s+', ' ', text)
       
        # 7. Supprimer les espaces au début et à la fin
        text = text.strip()
       
        return text
       
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {str(e)}")
        return None

def decoupePhrase(fichier, m) :
    data = fichier.split(".")
    chunks = []
    chunks.append(data[0])
    for i in range (len(data)-1) :
        phrase = data[i].split(" ")
        chunks.append(" ".join(phrase[-m : ]) + "." + data[i+1])
    return chunks


# Creation d'un client chroma / base de données en mémoire

client = chromadb.Client()

# Création de la fonction d'embedding

modEmb = embedding_functions.SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")

# Creation d'une collection - table SQL

collection = client.get_or_create_collection("name", modEmb)

texte = process_text_file("doc1_intelligence_artificielle.txt")

data = decoupePhrase(texte, 6)

data_vect = modEmb(data)

id = [str(i) for i in range(1, len(data)+1)]

# collection.add(ids = id, documents = data)

query = "Quelles sont les implications éthiques de l'intelligence artificielle ?"
vecteur_query = modEmb([query])


# ============================================================================
# PARTIE 2 : FONCTIONS DE CALCUL DE SIMILARITÉ / DISTANCE
# ============================================================================


def cosinus(vec1, vec2):
    """
    Calcule la similarité cosinus entre deux vecteurs.

    La similarité cosinus mesure l'angle entre deux vecteurs, indépendamment
    de leur magnitude. Elle retourne une valeur entre -1 et 1 :
      - 1  = vecteurs identiques en direction
      - 0  = vecteurs orthogonaux
      - -1 = vecteurs opposés

    Métrique la plus adaptée pour :
        La recherche sémantique / textuelle, où l'on compare le sens
        (direction) des vecteurs d'embeddings plutôt que leur amplitude.
        Très utilisée en NLP et en systèmes de recommandation.

    Args:
        vec1 (np.ndarray): Premier vecteur
        vec2 (np.ndarray): Deuxième vecteur

    Returns:
        float: Similarité cosinus entre les deux vecteurs
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot = np.dot(vec1, vec2)
    norme1 = np.linalg.norm(vec1)
    norme2 = np.linalg.norm(vec2)
    if norme1 == 0 or norme2 == 0:
        return 0.0
    return dot / (norme1 * norme2)


def distance_euclidienne(vec1, vec2):
    """
    Calcule la distance euclidienne entre deux vecteurs.

    La distance euclidienne mesure la distance « en ligne droite » entre deux
    points dans l'espace vectoriel. Plus la valeur est faible, plus les
    vecteurs sont proches.

    Métrique la plus adaptée pour :
        La recherche par similarité géométrique / spatiale, par exemple la
        classification d'images, le clustering (k-means), ou toute tâche où
        la magnitude des vecteurs a un sens (données normalisées, coordonnées
        géographiques, etc.).

    Args:
        vec1 (np.ndarray): Premier vecteur
        vec2 (np.ndarray): Deuxième vecteur

    Returns:
        float: Distance euclidienne entre les deux vecteurs
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.linalg.norm(vec1 - vec2)


def produit_scalaire(vec1, vec2):
    """
    Calcule le produit scalaire (dot product) entre deux vecteurs.

    Le produit scalaire mesure à la fois la similarité de direction ET la
    magnitude des vecteurs. Une valeur élevée indique des vecteurs de grande
    norme pointant dans la même direction.

    Métrique la plus adaptée pour :
        La recherche où la magnitude compte autant que la direction, par
        exemple le classement par pertinence dans les moteurs de recherche
        (TF-IDF, BM25), la détection d'anomalies, ou les systèmes de
        recommandation où la « force » du signal est importante.

    Args:
        vec1 (np.ndarray): Premier vecteur
        vec2 (np.ndarray): Deuxième vecteur

    Returns:
        float: Produit scalaire des deux vecteurs
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2)


# ============================================================================
# PARTIE 3 : RECHERCHE DES 3 RÉSULTATS LES PLUS PROCHES
# ============================================================================


def top_k_resultats(vecteur_requete, vecteurs_data, textes, fonction_metrique, k=3, plus_grand_est_mieux=True):
    """
    Retourne les k résultats les plus proches de la requête selon la métrique donnée.

    Args:
        vecteur_requete (np.ndarray): Vecteur de la requête
        vecteurs_data (list): Liste des vecteurs de la base de données
        textes (list): Liste des textes correspondant aux vecteurs
        fonction_metrique (callable): Fonction de calcul de la métrique
        k (int): Nombre de résultats à retourner
        plus_grand_est_mieux (bool): True si un score plus élevé = plus proche
                                     (cosinus, produit scalaire).
                                     False si un score plus bas = plus proche
                                     (distance euclidienne).

    Returns:
        list: Liste de tuples (score, texte) des k meilleurs résultats
    """
    scores = []
    for i, vec in enumerate(vecteurs_data):
        score = fonction_metrique(vecteur_requete, vec)
        scores.append((score, textes[i]))

    scores.sort(key=lambda x: x[0], reverse=plus_grand_est_mieux)
    return scores[:k]


def afficher_resultats(nom_metrique, resultats, description_usage):
    """
    Affiche les résultats d'une recherche pour une métrique donnée.
    """
    print("=" * 80)
    print(f"  MÉTRIQUE : {nom_metrique}")
    print(f"  Type de recherche le plus adapté : {description_usage}")
    print("=" * 80)
    for rang, (score, texte) in enumerate(resultats, 1):
        print(f"\n  #{rang} — Score : {score:.6f}")
        print(f"     Texte : {texte[:150]}{'...' if len(texte) > 150 else ''}")
    print()


# --- Exécution de la recherche pour chaque métrique ---

print(f"\nQuestion de recherche : \"{query}\"\n")

# 1. Similarité Cosinus (plus grand = plus proche → plus_grand_est_mieux=True)
resultats_cosinus = top_k_resultats(
    vecteur_query[0], data_vect, data, cosinus, k=3, plus_grand_est_mieux=True
)
afficher_resultats(
    "Similarité Cosinus",
    resultats_cosinus,
    "Recherche sémantique / textuelle — compare la direction des vecteurs "
    "(le sens), indépendamment de leur amplitude. Idéale pour le NLP et les "
    "systèmes de recommandation basés sur le contenu."
)

# 2. Distance Euclidienne (plus petit = plus proche → plus_grand_est_mieux=False)
resultats_euclidienne = top_k_resultats(
    vecteur_query[0], data_vect, data, distance_euclidienne, k=3, plus_grand_est_mieux=False
)
afficher_resultats(
    "Distance Euclidienne",
    resultats_euclidienne,
    "Recherche spatiale / géométrique — mesure la distance absolue entre deux "
    "points. Idéale pour le clustering (k-means), la classification d'images, "
    "et les données normalisées où la magnitude est significative."
)

# 3. Produit Scalaire (plus grand = plus proche → plus_grand_est_mieux=True)
resultats_scalaire = top_k_resultats(
    vecteur_query[0], data_vect, data, produit_scalaire, k=3, plus_grand_est_mieux=True
)
afficher_resultats(
    "Produit Scalaire (Dot Product)",
    resultats_scalaire,
    "Recherche par pertinence pondérée — tient compte à la fois de la direction "
    "et de la magnitude des vecteurs. Idéal pour le classement par pertinence "
    "(TF-IDF, BM25), la détection d'anomalies et les recommandations pondérées."
)