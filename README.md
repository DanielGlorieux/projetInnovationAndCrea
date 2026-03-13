# Projet IVF - Extraction et Présentation

## Description

Ce projet extrait les informations clés du tutoriel vidéo **"Inverted File Index (IVF) Explained"** de la chaîne TensorTeach (Mastering Vector Databases), puis génère automatiquement une présentation explicative sur l'algorithme IVF.

## Contenu du tutoriel extrait

L'algorithme **Inverted File Index (IVF)** est une méthode d'indexation pour les bases de données vectorielles. Voici les concepts clés extraits :

### Phase d'Indexation
1. **Clustering K-means** : Tous les vecteurs sont regroupés en `nlist` clusters via l'algorithme K-means
2. **Centroïdes & Posting Lists** : Chaque cluster possède un centroïde et une posting list contenant les IDs des vecteurs du cluster
3. **Ajout de vecteurs** : Pour un nouveau vecteur, on trouve le centroïde le plus proche et on l'ajoute à sa posting list

### Phase de Recherche (Retrieval)
1. **Trouver les centroïdes proches** : Pour une requête, on trouve les `nprobe` centroïdes les plus proches
2. **Explorer les clusters** : On cherche les voisins uniquement dans les `nprobe` clusters sélectionnés
3. **Retourner les résultats** : On retourne les top-k résultats combinés de tous les clusters explorés

### Paramètres Clés
- **`nlist`** : Nombre de clusters (plus de clusters = posting lists plus petites par cluster)
- **`nprobe`** : Nombre de clusters à explorer (plus élevé = meilleur recall mais latence plus haute)

## Scripts

### 1. `extract_video_info.py` - Extraction de la vidéo

Extrait les informations (texte via OCR et images clés) de la vidéo tutoriel.

```bash
pip install -r requirements.txt
sudo apt install tesseract-ocr tesseract-ocr-eng
python3 extract_video_info.py
```

**Sorties :**
- `output/extracted_info.json` : Données structurées en JSON
- `output/extracted_text.txt` : Résumé textuel lisible
- `output/key_frames/` : Frames clés extraites de la vidéo

### 2. `create_presentation.py` - Création de la présentation

Génère une présentation PowerPoint (10 slides) expliquant l'algorithme IVF, basée sur les informations extraites du tutoriel.

```bash
python3 create_presentation.py
```

**Sortie :**
- `output/presentation_ivf.pptx` : Présentation PowerPoint importable dans Canva

### Importer dans Canva

1. Aller sur [https://www.canva.com/](https://www.canva.com/)
2. Cliquer sur **"Créer un design"** → **"Importer"**
3. Sélectionner le fichier `output/presentation_ivf.pptx`
4. Canva convertira automatiquement le fichier en design éditable

## Structure de la présentation

| Slide | Titre | Contenu |
|-------|-------|---------|
| 1 | Inverted File Index (IVF) | Page de titre |
| 2 | Pourquoi l'IVF ? | Problème et solution |
| 3 | IVF - Phase d'Indexation | Vue d'ensemble en 3 étapes |
| 4 | Clustering K-means | Détail du partitionnement |
| 5 | Centroïdes & Posting Lists | Structure de données |
| 6 | Ajout d'un Nouveau Vecteur | Processus d'insertion |
| 7 | Phase de Recherche | Vue d'ensemble de la recherche |
| 8 | Le Paramètre nprobe | Compromis vitesse/précision |
| 9 | Paramètres Clés | nlist, nprobe, k |
| 10 | Récapitulatif | Synthèse, avantages et limites |

## Prérequis

- Python 3.8+
- Tesseract OCR (`apt install tesseract-ocr`)
- Dépendances Python : voir `requirements.txt`

## Source

Tutoriel vidéo : *"Inverted File Index (IVF) Explained"* - TensorTeach (Mastering Vector Databases)
