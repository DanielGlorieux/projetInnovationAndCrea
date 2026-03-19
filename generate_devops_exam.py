import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def extract_pdf_text(pdf_path):
    """Extrait le texte d'un fichier PDF"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Erreur lors de l'extraction du PDF {pdf_path}: {e}")
    return text

def create_devops_exam():
    """Crée un examen de DevOps basé sur le cours"""
    
    # Extraction du contenu des PDFs
    print("Extraction du contenu des cours...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cours_path = os.path.join(base_dir, "DevOps", "Cours_DevOps.pdf")
    ppt_path = os.path.join(base_dir, "DevOps", "PPT_DevOps.pdf")

    cours_text = extract_pdf_text(cours_path)
    ppt_text = extract_pdf_text(ppt_path)

    print(f"Cours extrait: {len(cours_text)} caractères")
    print(f"PPT extrait: {len(ppt_text)} caractères")

    # Création du document PDF d'examen
    output_path = os.path.join(base_dir, "Examen_DevOps.pdf")
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                           rightMargin=2*cm, leftMargin=2*cm,
                           topMargin=2*cm, bottomMargin=2*cm)
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='navy',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='darkblue',
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    # Contenu de l'examen
    story = []
    
    # En-tête
    story.append(Paragraph("EXAMEN DE CONTRÔLE DE CONNAISSANCES", title_style))
    story.append(Paragraph("DevOps - Développement et Opérations", heading_style))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("<b>Durée:</b> 2 heures", normal_style))
    story.append(Paragraph("<b>Documents autorisés:</b> Aucun", normal_style))
    story.append(Paragraph("<b>Notation:</b> 20 points au total", normal_style))
    story.append(Spacer(1, 1*cm))
    
    # Section 1: Questions de cours (QCM)
    story.append(Paragraph("PARTIE 1 : Questions à Choix Multiples (8 points)", heading_style))
    story.append(Paragraph("Choisissez la ou les bonnes réponses (1 point par question)", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    qcm_questions = [
        {
            "q": "1. Qu'est-ce que DevOps ?",
            "options": [
                "a) Un outil de développement logiciel",
                "b) Une culture favorisant la collaboration entre Dev et Ops",
                "c) Un langage de programmation",
                "d) Un système d'exploitation"
            ],
            "answer": "b"
        },
        {
            "q": "2. Quel est l'objectif principal de l'intégration continue (CI) ?",
            "options": [
                "a) Déployer automatiquement en production",
                "b) Intégrer régulièrement le code et détecter les erreurs rapidement",
                "c) Remplacer les développeurs",
                "d) Créer des environnements de test"
            ],
            "answer": "b"
        },
        {
            "q": "3. Parmi ces outils, lesquels sont utilisés pour le CI/CD ?",
            "options": [
                "a) Jenkins",
                "b) Microsoft Word",
                "c) GitLab CI",
                "d) Docker"
            ],
            "answer": "a, c, d"
        },
        {
            "q": "4. Qu'est-ce que Docker ?",
            "options": [
                "a) Une plateforme de conteneurisation",
                "b) Un système de gestion de base de données",
                "c) Un éditeur de code",
                "d) Un outil de virtualisation léger"
            ],
            "answer": "a, d"
        },
        {
            "q": "5. Kubernetes est utilisé pour :",
            "options": [
                "a) L'orchestration de conteneurs",
                "b) L'édition de code",
                "c) La gestion et le déploiement automatique de conteneurs",
                "d) La compilation de code"
            ],
            "answer": "a, c"
        },
        {
            "q": "6. Qu'est-ce que l'Infrastructure as Code (IaC) ?",
            "options": [
                "a) Gérer l'infrastructure via du code",
                "b) Écrire du code d'infrastructure manuelle",
                "c) Utiliser des fichiers de configuration versionnés",
                "d) Un langage de programmation"
            ],
            "answer": "a, c"
        },
        {
            "q": "7. Quels sont les avantages du DevOps ?",
            "options": [
                "a) Déploiements plus rapides",
                "b) Meilleure collaboration entre équipes",
                "c) Réduction des coûts",
                "d) Augmentation de la taille du code"
            ],
            "answer": "a, b, c"
        },
        {
            "q": "8. Quel outil est utilisé pour la gestion de versions ?",
            "options": [
                "a) Git",
                "b) Ansible",
                "c) GitHub",
                "d) Photoshop"
            ],
            "answer": "a, c"
        }
    ]
    
    for item in qcm_questions:
        story.append(Paragraph(item["q"], question_style))
        for opt in item["options"]:
            story.append(Paragraph(opt, normal_style))
        story.append(Spacer(1, 0.3*cm))
    
    # Section 2: Questions courtes
    story.append(PageBreak())
    story.append(Paragraph("PARTIE 2 : Questions Courtes (6 points)", heading_style))
    story.append(Paragraph("Répondez de manière concise (2 points par question)", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    short_questions = [
        "9. Expliquez la différence entre l'intégration continue (CI) et le déploiement continu (CD).",
        "10. Quels sont les principaux composants d'un pipeline CI/CD ?",
        "11. Pourquoi utilise-t-on des conteneurs plutôt que des machines virtuelles traditionnelles ?"
    ]
    
    for q in short_questions:
        story.append(Paragraph(q, question_style))
        story.append(Spacer(1, 2*cm))
    
    # Section 3: Question de synthèse
    story.append(PageBreak())
    story.append(Paragraph("PARTIE 3 : Question de Synthèse (6 points)", heading_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("12. Vous êtes responsable DevOps dans une entreprise qui souhaite moderniser son processus de développement. Actuellement, les déploiements sont manuels et prennent plusieurs jours. Proposez une architecture DevOps complète incluant :", question_style))
    story.append(Paragraph("- Les outils à utiliser (CI/CD, conteneurisation, orchestration)", normal_style))
    story.append(Paragraph("- Le workflow de développement à la production", normal_style))
    story.append(Paragraph("- Les bénéfices attendus", normal_style))
    story.append(Spacer(1, 4*cm))
    
    # CORRECTION
    story.append(PageBreak())
    story.append(Paragraph("CORRECTION DE L'EXAMEN", title_style))
    story.append(Spacer(1, 1*cm))
    
    # Correction Partie 1
    story.append(Paragraph("PARTIE 1 : Correction des QCM (8 points)", heading_style))
    story.append(Spacer(1, 0.3*cm))
    
    for i, item in enumerate(qcm_questions, 1):
        story.append(Paragraph(f"<b>Question {i}:</b> Réponse correcte: <b>{item['answer']}</b>", normal_style))
        story.append(Spacer(1, 0.2*cm))
    
    story.append(Spacer(1, 0.5*cm))
    
    # Correction Partie 2
    story.append(Paragraph("PARTIE 2 : Correction des Questions Courtes (6 points)", heading_style))
    story.append(Spacer(1, 0.3*cm))
    
    corrections_short = [
        {
            "q": "9. Différence entre CI et CD:",
            "r": "<b>CI (Intégration Continue):</b> Processus qui consiste à intégrer régulièrement le code des développeurs dans un dépôt partagé, suivi de builds et tests automatiques pour détecter rapidement les erreurs.<br/><br/><b>CD (Déploiement Continu):</b> Extension de CI qui automatise le déploiement du code validé vers les environnements de test et/ou production. Chaque modification validée peut être déployée automatiquement."
        },
        {
            "q": "10. Composants principaux d'un pipeline CI/CD:",
            "r": "- <b>Source Control:</b> Gestion du code (Git)<br/>- <b>Build:</b> Compilation et packaging<br/>- <b>Test:</b> Tests automatisés (unitaires, intégration, fonctionnels)<br/>- <b>Deploy:</b> Déploiement automatique<br/>- <b>Monitor:</b> Surveillance et feedback<br/>- <b>Outils:</b> Jenkins, GitLab CI, GitHub Actions, etc."
        },
        {
            "q": "11. Avantages des conteneurs vs VMs:",
            "r": "- <b>Légèreté:</b> Les conteneurs partagent le noyau de l'OS, consommant moins de ressources<br/>- <b>Rapidité:</b> Démarrage en secondes vs minutes pour les VMs<br/>- <b>Portabilité:</b> 'Build once, run anywhere' - même environnement partout<br/>- <b>Efficacité:</b> Meilleure densité d'applications sur le même hardware<br/>- <b>Isolation:</b> Isolation des processus sans la surcharge d'un OS complet"
        }
    ]
    
    for item in corrections_short:
        story.append(Paragraph(item["q"], question_style))
        story.append(Paragraph(item["r"], normal_style))
        story.append(Spacer(1, 0.5*cm))
    
    # Correction Partie 3
    story.append(PageBreak())
    story.append(Paragraph("PARTIE 3 : Correction Question de Synthèse (6 points)", heading_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>12. Architecture DevOps complète - Éléments de réponse:</b>", question_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>A. Outils recommandés (2 points):</b>", normal_style))
    story.append(Paragraph("- <b>Gestion de version:</b> Git + GitHub/GitLab", normal_style))
    story.append(Paragraph("- <b>CI/CD:</b> Jenkins, GitLab CI, ou GitHub Actions", normal_style))
    story.append(Paragraph("- <b>Conteneurisation:</b> Docker", normal_style))
    story.append(Paragraph("- <b>Orchestration:</b> Kubernetes (ou Docker Swarm pour plus simple)", normal_style))
    story.append(Paragraph("- <b>IaC:</b> Terraform ou Ansible", normal_style))
    story.append(Paragraph("- <b>Monitoring:</b> Prometheus + Grafana", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>B. Workflow Dev → Production (2 points):</b>", normal_style))
    story.append(Paragraph("1. <b>Développement:</b> Code poussé sur branche Git", normal_style))
    story.append(Paragraph("2. <b>CI:</b> Déclenchement automatique du pipeline", normal_style))
    story.append(Paragraph("   - Build de l'application", normal_style))
    story.append(Paragraph("   - Exécution des tests unitaires", normal_style))
    story.append(Paragraph("   - Construction de l'image Docker", normal_style))
    story.append(Paragraph("3. <b>Tests:</b> Déploiement en environnement de test", normal_style))
    story.append(Paragraph("   - Tests d'intégration et fonctionnels", normal_style))
    story.append(Paragraph("4. <b>Staging:</b> Validation en pré-production", normal_style))
    story.append(Paragraph("5. <b>Production:</b> Déploiement automatique ou manuel", normal_style))
    story.append(Paragraph("   - Rolling update via Kubernetes", normal_style))
    story.append(Paragraph("6. <b>Monitoring:</b> Surveillance continue", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("<b>C. Bénéfices attendus (2 points):</b>", normal_style))
    story.append(Paragraph("- <b>Rapidité:</b> Déploiements de plusieurs jours → minutes/heures", normal_style))
    story.append(Paragraph("- <b>Qualité:</b> Détection précoce des bugs via tests automatisés", normal_style))
    story.append(Paragraph("- <b>Fiabilité:</b> Réduction des erreurs humaines (automatisation)", normal_style))
    story.append(Paragraph("- <b>Scalabilité:</b> Kubernetes permet mise à l'échelle automatique", normal_style))
    story.append(Paragraph("- <b>Collaboration:</b> Meilleure communication Dev/Ops", normal_style))
    story.append(Paragraph("- <b>Coûts:</b> Optimisation des ressources et réduction du time-to-market", normal_style))
    story.append(Paragraph("- <b>Réversibilité:</b> Rollback rapide en cas de problème", normal_style))
    
    # Génération du PDF
    print("\nGénération du PDF d'examen...")
    doc.build(story)
    print(f"\n✅ Examen créé avec succès: {output_path}")
    print(f"\n📋 L'examen contient:")
    print(f"   - Partie 1: 8 QCM (8 points)")
    print(f"   - Partie 2: 3 questions courtes (6 points)")
    print(f"   - Partie 3: 1 question de synthèse (6 points)")
    print(f"   - Correction complète incluse à la fin")

if __name__ == "__main__":
    create_devops_exam()
