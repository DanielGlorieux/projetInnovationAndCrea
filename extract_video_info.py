"""
Script d'extraction d'informations du tutoriel vidéo sur l'algorithme IVF.
Source : "Inverted File Index (IVF) Explained - Mastering Vector Databases - TensorTeach"

Ce script :
1. Extrait des frames à intervalles réguliers depuis la vidéo
2. Effectue de l'OCR (reconnaissance optique de caractères) sur chaque frame
3. Déduplique les textes similaires pour ne garder que les sections uniques
4. Sauvegarde les frames clés en images et le texte extrait en JSON/texte

Prérequis :
    pip install opencv-python-headless pytesseract Pillow
    apt install tesseract-ocr tesseract-ocr-eng
"""

import cv2
import pytesseract
import os
import json
import numpy as np
from PIL import Image

# Configuration
VIDEO_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Inverted File Index (IVF) Explained _ Mastering Vector Databases _ TensorTeach.mp4",
)
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
KEY_FRAMES_DIR = os.path.join(OUTPUT_DIR, "key_frames")
EXTRACTION_INTERVAL_SEC = 5
# Jaccard similarity threshold: texts with > 80% word overlap are considered duplicates.
# Lower values = more sections retained; higher values = more aggressive deduplication.
DUPLICATE_TEXT_THRESHOLD = 0.80
# Minimum number of characters for a text block to be considered meaningful (filters OCR noise)
MIN_TEXT_LENGTH = 15


def ensure_dirs():
    """Crée les répertoires de sortie s'ils n'existent pas."""
    os.makedirs(KEY_FRAMES_DIR, exist_ok=True)


def extract_text_from_frame(frame):
    """Extrait le texte d'une frame vidéo via OCR Tesseract."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    text = pytesseract.image_to_string(pil_img, lang="eng", config="--psm 6")
    return text.strip()


def text_similarity(text1, text2):
    """Calcule la similarité entre deux textes (Jaccard sur les mots)."""
    if not text1 or not text2:
        return 0.0
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)


def extract_frames_and_ocr(video_path):
    """
    Extrait des frames à intervalles réguliers et effectue l'OCR.
    Retourne une liste de sections uniques avec texte et métadonnées.
    """
    print(f"Ouverture de la vidéo : {video_path}")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir la vidéo : {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"  FPS : {fps}")
    print(f"  Frames totales : {total_frames}")
    print(f"  Durée : {duration:.1f}s ({duration / 60:.1f} min)")
    print(f"  Intervalle d'extraction : {EXTRACTION_INTERVAL_SEC}s")

    all_frames = []
    for sec in range(0, int(duration) + 1, EXTRACTION_INTERVAL_SEC):
        frame_pos = int(sec * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
        ret, frame = cap.read()
        if not ret:
            break

        # Sauvegarder la frame
        fname = f"frame_{sec:04d}s.png"
        fpath = os.path.join(KEY_FRAMES_DIR, fname)
        cv2.imwrite(fpath, frame)

        # OCR
        text = extract_text_from_frame(frame)

        all_frames.append(
            {
                "timestamp_sec": sec,
                "timestamp_str": f"{sec // 60}:{sec % 60:02d}",
                "filename": fname,
                "path": fpath,
                "text": text,
            }
        )
        print(f"  t={sec // 60}:{sec % 60:02d} - {len(text)} caractères extraits")

    cap.release()
    print(f"\n{len(all_frames)} frames extraites au total")

    # Déduplication par similarité textuelle
    unique_sections = []
    prev_text = ""
    for frame_info in all_frames:
        if frame_info["text"] and len(frame_info["text"]) > MIN_TEXT_LENGTH:
            sim = text_similarity(frame_info["text"], prev_text)
            if sim < DUPLICATE_TEXT_THRESHOLD:
                unique_sections.append(frame_info)
                prev_text = frame_info["text"]

    print(f"{len(unique_sections)} sections uniques identifiées\n")
    return all_frames, unique_sections


def save_key_representative_frames(video_path):
    """
    Sauvegarde des frames représentatives aux timestamps clés
    identifiés manuellement à partir de l'analyse du tutoriel.
    """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    key_timestamps = {
        "01_titre_ivf": 0,
        "02_indexation_intro": 20,
        "03_clusters_kmeans": 40,
        "04_centroid_posting_list": 50,
        "05_ajout_vecteur": 105,
        "06_indexation_complete": 160,
        "07_titre_retrieval": 165,
        "08_recherche_nprobe": 175,
        "09_exploration_clusters": 210,
        "10_retrieval_complet_params": 245,
    }

    saved = []
    for name, sec in key_timestamps.items():
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
        ret, frame = cap.read()
        if ret:
            fpath = os.path.join(KEY_FRAMES_DIR, f"{name}.png")
            cv2.imwrite(fpath, frame)
            saved.append({"name": name, "timestamp_sec": sec, "path": fpath})
            print(f"  Frame clé sauvegardée : {name} (t={sec // 60}:{sec % 60:02d})")

    cap.release()
    return saved


def save_results(all_frames, unique_sections, key_frames_info):
    """Sauvegarde les résultats en JSON et en texte lisible."""
    # JSON structuré
    json_path = os.path.join(OUTPUT_DIR, "extracted_info.json")
    json_data = {
        "video": os.path.basename(VIDEO_PATH),
        "total_frames_extracted": len(all_frames),
        "unique_sections_count": len(unique_sections),
        "key_representative_frames": key_frames_info,
        "unique_sections": [
            {
                "timestamp": s["timestamp_str"],
                "timestamp_sec": s["timestamp_sec"],
                "text": s["text"],
                "frame_file": s["filename"],
            }
            for s in unique_sections
        ],
        "ivf_algorithm_summary": {
            "title": "Inverted File Index (IVF)",
            "source": "TensorTeach - Mastering Vector Databases",
            "indexing": [
                "Indexing works by first clustering all of the vectors you want to store into 'nlist' clusters using k-means.",
                "Each cluster has a centroid, and you keep a posting list of the IDs of vectors in that cluster.",
                "When adding a new vector, you find the closest centroid and store it in that centroid's posting list.",
            ],
            "retrieval": [
                "When querying results for a new vector, you find the closest 'nprobe' cluster centroids.",
                "From there you only explore the closest 'nprobe' clusters for nearest neighbors.",
                "You then return the top k results across all 'nprobe' clusters.",
            ],
            "key_parameters": {
                "nlist": "Number of clusters (more clusters = smaller posting lists per cluster)",
                "nprobe": "Number of clusters to search (higher nprobe = better recall but higher latency)",
            },
        },
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print(f"Données structurées sauvegardées : {json_path}")

    # Texte lisible
    txt_path = os.path.join(OUTPUT_DIR, "extracted_text.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("TEXTE EXTRAIT DU TUTORIEL : Inverted File Index (IVF)\n")
        f.write("Source : TensorTeach - Mastering Vector Databases\n")
        f.write("=" * 80 + "\n\n")

        for i, section in enumerate(unique_sections):
            f.write(
                f"--- Section {i + 1} (Timestamp: {section['timestamp_str']}) ---\n"
            )
            f.write(f"Frame: {section['filename']}\n")
            f.write(section["text"])
            f.write("\n\n")

        f.write("=" * 80 + "\n")
        f.write("RÉSUMÉ DE L'ALGORITHME IVF\n")
        f.write("=" * 80 + "\n\n")
        f.write("INDEXATION :\n")
        for step in json_data["ivf_algorithm_summary"]["indexing"]:
            f.write(f"  • {step}\n")
        f.write("\nRECHERCHE (RETRIEVAL) :\n")
        for step in json_data["ivf_algorithm_summary"]["retrieval"]:
            f.write(f"  • {step}\n")
        f.write("\nPARAMÈTRES CLÉS :\n")
        for param, desc in json_data["ivf_algorithm_summary"][
            "key_parameters"
        ].items():
            f.write(f"  • {param}: {desc}\n")

    print(f"Résumé textuel sauvegardé : {txt_path}")
    return json_path, txt_path


def main():
    """Point d'entrée principal du script d'extraction."""
    print("=" * 60)
    print("Extraction d'informations du tutoriel IVF")
    print("=" * 60 + "\n")

    ensure_dirs()

    # Étape 1 : Extraction des frames et OCR
    print("Étape 1 : Extraction des frames et OCR...")
    all_frames, unique_sections = extract_frames_and_ocr(VIDEO_PATH)

    # Étape 2 : Sauvegarde des frames représentatives
    print("Étape 2 : Sauvegarde des frames clés représentatives...")
    key_frames_info = save_key_representative_frames(VIDEO_PATH)

    # Étape 3 : Sauvegarde des résultats
    print("\nÉtape 3 : Sauvegarde des résultats...")
    json_path, txt_path = save_results(all_frames, unique_sections, key_frames_info)

    print(f"\n{'=' * 60}")
    print("Extraction terminée !")
    print(f"  Frames clés : {KEY_FRAMES_DIR}")
    print(f"  Données JSON : {json_path}")
    print(f"  Résumé texte : {txt_path}")
    print(f"{'=' * 60}")

    return unique_sections


if __name__ == "__main__":
    sections = main()
