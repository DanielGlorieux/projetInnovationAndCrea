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

query = "Queles sont les implications éthiques de l'intelligence artificielle ?"
vecteur_query = modEmb(query)