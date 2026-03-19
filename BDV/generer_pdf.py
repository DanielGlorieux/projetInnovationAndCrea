from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Créer le PDF
pdf_file = r"C:\Users\danie\Desktop\ProjetInno\BDV\Examen_BDV_Complet.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4, topMargin=2*cm, bottomMargin=2*cm)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Title1', fontSize=18, textColor=colors.HexColor('#1a1a1a'), 
                          spaceAfter=12, alignment=TA_CENTER, bold=True))
styles.add(ParagraphStyle(name='Title2', fontSize=16, textColor=colors.HexColor('#2c3e50'), 
                          spaceAfter=10, bold=True))
styles.add(ParagraphStyle(name='Title3', fontSize=14, textColor=colors.HexColor('#34495e'), 
                          spaceAfter=8, bold=True))
styles.add(ParagraphStyle(name='Title4', fontSize=12, textColor=colors.HexColor('#7f8c8d'), 
                          spaceAfter=6, bold=True))
styles.add(ParagraphStyle(name='CodeStyle', fontSize=9, fontName='Courier', 
                          leftIndent=20, spaceBefore=6, spaceAfter=6,
                          textColor=colors.HexColor('#2c3e50')))
styles.add(ParagraphStyle(name='Normal2', fontSize=11, spaceAfter=6, alignment=TA_JUSTIFY))

story = []

# PAGE DE GARDE
story.append(Spacer(1, 4*cm))
story.append(Paragraph("EXAMEN DE CONTRÔLE DES CONNAISSANCES", styles['Title1']))
story.append(Paragraph("BASES DE DONNÉES VECTORIELLES", styles['Title1']))
story.append(Spacer(1, 2*cm))

# Informations
info_data = [
    ['Durée :', '2 heures'],
    ['Documents :', 'Non autorisés'],
    ['Matériel :', 'Python autorisé (bibliothèques standard)']
]
info_table = Table(info_data, colWidths=[4*cm, 10*cm])
info_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 12),
    ('TEXTCOLOR', (0,0), (0,-1), colors.HexColor('#2c3e50')),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(info_table)
story.append(PageBreak())

# SUJET D'EXAMEN
story.append(Paragraph("PARTIE 1 : QUESTIONS DE COURS (8 points)", styles['Title2']))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("Question 1 (2 points)", styles['Title3']))
story.append(Paragraph("Expliquez le principe de la recherche vectorielle et en quoi elle diffère de la recherche traditionnelle par mots-clés dans les bases de données relationnelles.", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 2 (2 points)", styles['Title3']))
story.append(Paragraph("Décrivez les 4 étapes principales du processus de recherche vectorielle, de la transformation des données jusqu'à l'affichage des résultats.", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 3 (2 points)", styles['Title3']))
story.append(Paragraph("Qu'est-ce que l'indexation ANN (Approximate Nearest Neighbors) ? Citez et expliquez brièvement deux algorithmes d'indexation utilisés dans les bases de données vectorielles.", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 4 (2 points)", styles['Title3']))
story.append(Paragraph("Expliquez le \"trilemme de la performance\" dans les bases de données vectorielles. Quels sont les trois facteurs en jeu et pourquoi est-il difficile d'optimiser les trois simultanément ?", styles['Normal2']))
story.append(Spacer(1, 0.5*cm))

# PARTIE 2
story.append(PageBreak())
story.append(Paragraph("PARTIE 2 : EXERCICES PRATIQUES (12 points)", styles['Title2']))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("EXERCICE 1 : Prétraitement de données (3 points)", styles['Title3']))
story.append(Paragraph("Écrivez une fonction Python <b>nettoyer_texte(fichier_txt)</b> qui permet de :", styles['Normal2']))
story.append(Paragraph("• Lire des données issues d'un fichier au format TXT", styles['Normal2']))
story.append(Paragraph("• Remplacer les adresses mails par « MAIL » et les numéros de téléphone par « TEL »", styles['Normal2']))
story.append(Paragraph("• Supprimer les espaces en trop et les caractères spéciaux (sauf les points)", styles['Normal2']))
story.append(Paragraph("• Passer toutes les données en minuscules", styles['Normal2']))
story.append(Paragraph("• Retourner le texte nettoyé", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Exemple d'entrée :</b>", styles['Normal2']))
story.append(Paragraph("Contactez Jean Dupont au 06.12.34.56.78 ou par email : jean.dupont@example.com pour plus d'informations!!!", styles['CodeStyle']))
story.append(Paragraph("<b>Exemple de sortie attendue :</b>", styles['Normal2']))
story.append(Paragraph("contactez jean dupont au tel ou par email mail pour plus dinformations.", styles['CodeStyle']))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("EXERCICE 2 : Découpage de texte (Chunking) (4 points)", styles['Title3']))
story.append(Paragraph("<b>2.1 Découpage par blocs (1.5 points)</b>", styles['Title4']))
story.append(Paragraph("Écrivez une fonction Python <b>decouper_blocs(texte, n)</b> qui découpe un texte en blocs de n tokens (mots).", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>2.2 Découpage par phrases (1 point)</b>", styles['Title4']))
story.append(Paragraph("Écrivez une fonction Python <b>decouper_phrases(texte)</b> qui découpe un texte en phrases.", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>2.3 Découpage avec chevauchement (1.5 points)</b>", styles['Title4']))
story.append(Paragraph("Ajoutez à la fonction decouper_blocs un paramètre de chevauchement m qui permet de créer un overlap de m mots entre les blocs consécutifs.", styles['Normal2']))
story.append(Spacer(1, 0.5*cm))

story.append(PageBreak())
story.append(Paragraph("EXERCICE 3 : Métriques de similarité (5 points)", styles['Title3']))
story.append(Paragraph("<b>3.1 Implémentation (3 points)</b>", styles['Title4']))
story.append(Paragraph("Écrivez trois fonctions Python simples (sans utiliser de bibliothèques externes comme numpy) pour calculer :", styles['Normal2']))
story.append(Paragraph("a) Le produit scalaire <b>produit_scalaire(v1, v2)</b>", styles['Normal2']))
story.append(Paragraph("b) La similarité cosinus <b>similarite_cosinus(v1, v2)</b>", styles['Normal2']))
story.append(Paragraph("c) La distance euclidienne <b>distance_euclidienne(v1, v2)</b>", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>Rappels mathématiques :</b>", styles['Normal2']))
story.append(Paragraph("• Produit scalaire : v1 · v2 = Σ(v1[i] * v2[i])", styles['CodeStyle']))
story.append(Paragraph("• Similarité cosinus : cos(θ) = (v1 · v2) / (||v1|| * ||v2||)", styles['CodeStyle']))
story.append(Paragraph("• Distance euclidienne : d = √(Σ(v1[i] - v2[i])²)", styles['CodeStyle']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>3.2 Question théorique (2 points)</b>", styles['Title4']))
story.append(Paragraph("Pour chacune des trois métriques ci-dessus, expliquez dans quel type de recherche elle est la plus adaptée et pourquoi. Donnez un exemple concret d'utilisation pour chaque métrique.", styles['Normal2']))
story.append(Spacer(1, 0.5*cm))

# PARTIE 3
story.append(Paragraph("PARTIE 3 : CAS PRATIQUE (Bonus : 2 points)", styles['Title2']))
story.append(Paragraph("Sécurité et anonymisation", styles['Title3']))
story.append(Paragraph("Soit la phrase suivante contenant des données personnelles :", styles['Normal2']))
story.append(Paragraph("\"Le client Marc Traoré, né le 15/03/1985, ayant comme email marc.traore@gmail.com et numéro +226 70 12 34 56 a réservé le vol AF456.\"", styles['CodeStyle']))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("En vous basant sur vos connaissances du cours et l'exercice 1, écrivez une fonction Python <b>anonymiser_donnees(texte)</b> qui anonymise cette phrase.", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

# BARÈME
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("BARÈME RÉCAPITULATIF", styles['Title3']))
bareme_data = [
    ['Partie', 'Points'],
    ['Partie 1 : Questions de cours', '8'],
    ['Exercice 1 : Prétraitement', '3'],
    ['Exercice 2 : Chunking', '4'],
    ['Exercice 3 : Métriques', '5'],
    ['Total', '20'],
    ['Bonus', '+2']
]
bareme_table = Table(bareme_data, colWidths=[12*cm, 3*cm])
bareme_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND', (0,-2), (-1,-1), colors.HexColor('#ecf0f1')),
    ('GRID', (0,0), (-1,-1), 1, colors.grey),
]))
story.append(bareme_table)

# SÉPARATEUR AVANT CORRIGÉ
story.append(PageBreak())
story.append(Spacer(1, 3*cm))
story.append(Paragraph("═" * 80, styles['Title1']))
story.append(Spacer(1, 1*cm))
story.append(Paragraph("CORRIGÉ", styles['Title1']))
story.append(Spacer(1, 1*cm))
story.append(Paragraph("═" * 80, styles['Title1']))
story.append(PageBreak())

# CORRIGÉ PARTIE 1
story.append(Paragraph("PARTIE 1 : QUESTIONS DE COURS (8 points)", styles['Title2']))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("Question 1 (2 points)", styles['Title3']))
story.append(Paragraph("<b>Réponse :</b>", styles['Normal2']))
story.append(Paragraph("La recherche vectorielle change de paradigme en recherchant le <b>sens</b> plutôt que des mots-clés exacts. Dans une base de données relationnelle traditionnelle, on cherche des correspondances exactes (ex: \"animaux de compagnie\" nécessite de définir la catégorie et d'écrire une requête SQL spécifique). Avec la recherche vectorielle, les données sont transformées en vecteurs numériques (embeddings) dans un espace multidimensionnel, ce qui permet de trouver des résultats similaires sémantiquement (ex: \"animaux domestiques\" trouvera aussi \"chien\", \"chat\" sans requête exacte).", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 2 (2 points)", styles['Title3']))
story.append(Paragraph("<b>Réponse - Les 4 étapes :</b>", styles['Normal2']))
story.append(Paragraph("1. <b>L'Embedding</b> : Transformation des données en vecteurs numériques dans un espace vectoriel à n dimensions (n ≥ 300)", styles['Normal2']))
story.append(Paragraph("2. <b>Calcul des métriques de similarité</b> : Mesure de la proximité entre vecteurs via produit scalaire, similarité cosinus ou distance euclidienne", styles['Normal2']))
story.append(Paragraph("3. <b>Indexation ANN</b> : Utilisation d'algorithmes (HNSW, IVF) pour rechercher efficacement les vecteurs similaires", styles['Normal2']))
story.append(Paragraph("4. <b>Affichage des résultats</b> : Retour des k résultats les plus proches avec leurs données associées", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 3 (2 points)", styles['Title3']))
story.append(Paragraph("<b>Réponse :</b>", styles['Normal2']))
story.append(Paragraph("L'indexation ANN (Approximate Nearest Neighbors) utilise des algorithmes pour rechercher rapidement les vecteurs les plus similaires sans parcourir toute la base.", styles['Normal2']))
story.append(Paragraph("• <b>HNSW (Hierarchical Navigable Small World)</b> : Recherche à travers un réseau de chemins hiérarchiques, comme un graphe navigable", styles['Normal2']))
story.append(Paragraph("• <b>IVF (Inverted File Index)</b> : Divise l'espace vectoriel en zones (clusters) et ne cherche que dans la zone où se trouve la requête", styles['Normal2']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Question 4 (2 points)", styles['Title3']))
story.append(Paragraph("<b>Réponse :</b>", styles['Normal2']))
story.append(Paragraph("Le trilemme de la performance implique trois facteurs : <b>Vitesse des requêtes</b>, <b>Pertinence des résultats</b>, <b>Utilisation de la mémoire</b>. Améliorer l'un dégrade les deux autres. Ex: augmenter les paramètres HNSW (ef, M) améliore la pertinence mais réduit la vitesse et augmente la mémoire utilisée.", styles['Normal2']))

# CORRIGÉ EXERCICE 1
story.append(PageBreak())
story.append(Paragraph("EXERCICE 1 : Prétraitement de données (3 points)", styles['Title3']))
story.append(Paragraph("import re", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("def nettoyer_texte(fichier_txt):", styles['CodeStyle']))
story.append(Paragraph("    with open(fichier_txt, 'r', encoding='utf-8') as f:", styles['CodeStyle']))
story.append(Paragraph("        texte = f.read()", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer emails par MAIL", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', 'MAIL', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer téléphones par TEL", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\+?\\d{1,3}[\\s.-]?\\d{1,2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}', 'TEL', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Supprimer caractères spéciaux sauf points", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'[^\\w\\s.]', '', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Supprimer espaces multiples", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\s+', ' ', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Passer en minuscules", styles['CodeStyle']))
story.append(Paragraph("    return texte.lower().strip()", styles['CodeStyle']))

# CORRIGÉ EXERCICE 2
story.append(PageBreak())
story.append(Paragraph("EXERCICE 2 : Découpage de texte (4 points)", styles['Title3']))
story.append(Paragraph("<b>2.1 Découpage par blocs</b>", styles['Title4']))
story.append(Paragraph("def decouper_blocs(texte, n):", styles['CodeStyle']))
story.append(Paragraph("    mots = texte.split()", styles['CodeStyle']))
story.append(Paragraph("    blocs = []", styles['CodeStyle']))
story.append(Paragraph("    for i in range(0, len(mots), n):", styles['CodeStyle']))
story.append(Paragraph("        bloc = ' '.join(mots[i:i+n])", styles['CodeStyle']))
story.append(Paragraph("        blocs.append(bloc)", styles['CodeStyle']))
story.append(Paragraph("    return blocs", styles['CodeStyle']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>2.2 Découpage par phrases</b>", styles['Title4']))
story.append(Paragraph("def decouper_phrases(texte):", styles['CodeStyle']))
story.append(Paragraph("    phrases = texte.split('.')", styles['CodeStyle']))
story.append(Paragraph("    return [p.strip() for p in phrases if p.strip()]", styles['CodeStyle']))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("<b>2.3 Découpage avec chevauchement</b>", styles['Title4']))
story.append(Paragraph("def decouper_blocs_avec_overlap(texte, n, m):", styles['CodeStyle']))
story.append(Paragraph("    mots = texte.split()", styles['CodeStyle']))
story.append(Paragraph("    blocs = []", styles['CodeStyle']))
story.append(Paragraph("    i = 0", styles['CodeStyle']))
story.append(Paragraph("    while i < len(mots):", styles['CodeStyle']))
story.append(Paragraph("        bloc = ' '.join(mots[i:i+n])", styles['CodeStyle']))
story.append(Paragraph("        blocs.append(bloc)", styles['CodeStyle']))
story.append(Paragraph("        i += (n - m)  # Chevauchement de m mots", styles['CodeStyle']))
story.append(Paragraph("        if m >= n:", styles['CodeStyle']))
story.append(Paragraph("            i += 1", styles['CodeStyle']))
story.append(Paragraph("    return blocs", styles['CodeStyle']))

# CORRIGÉ EXERCICE 3
story.append(PageBreak())
story.append(Paragraph("EXERCICE 3 : Métriques de similarité (5 points)", styles['Title3']))
story.append(Paragraph("<b>3.1 Implémentation</b>", styles['Title4']))
story.append(Paragraph("import math", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("def produit_scalaire(v1, v2):", styles['CodeStyle']))
story.append(Paragraph("    return sum(v1[i] * v2[i] for i in range(len(v1)))", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("def similarite_cosinus(v1, v2):", styles['CodeStyle']))
story.append(Paragraph("    dot_product = produit_scalaire(v1, v2)", styles['CodeStyle']))
story.append(Paragraph("    norme_v1 = math.sqrt(sum(x**2 for x in v1))", styles['CodeStyle']))
story.append(Paragraph("    norme_v2 = math.sqrt(sum(x**2 for x in v2))", styles['CodeStyle']))
story.append(Paragraph("    if norme_v1 == 0 or norme_v2 == 0:", styles['CodeStyle']))
story.append(Paragraph("        return 0", styles['CodeStyle']))
story.append(Paragraph("    return dot_product / (norme_v1 * norme_v2)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("def distance_euclidienne(v1, v2):", styles['CodeStyle']))
story.append(Paragraph("    return math.sqrt(sum((v1[i] - v2[i])**2 for i in range(len(v1))))", styles['CodeStyle']))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("<b>3.2 Question théorique</b>", styles['Title4']))
story.append(Paragraph("<b>Produit scalaire</b> : Mesure direction ET magnitude. Adapté pour systèmes de recommandation où l'intensité compte.", styles['Normal2']))
story.append(Paragraph("<b>Similarité cosinus</b> : Mesure l'angle (direction uniquement). Adapté pour recherche sémantique de documents de tailles différentes.", styles['Normal2']))
story.append(Paragraph("<b>Distance euclidienne</b> : Mesure la distance physique. Adapté pour reconnaissance d'images et classification.", styles['Normal2']))

# CORRIGÉ BONUS
story.append(PageBreak())
story.append(Paragraph("PARTIE 3 : CAS PRATIQUE (Bonus)", styles['Title3']))
story.append(Paragraph("def anonymiser_donnees(texte):", styles['CodeStyle']))
story.append(Paragraph("    import re", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer dates JJ/MM/AAAA", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\b\\d{2}/\\d{2}/\\d{4}\\b', 'DATE', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer emails", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', 'MAIL', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer téléphones", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\+?\\d{1,3}[\\s.-]?\\d{1,2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}[\\s.-]?\\d{2}', 'TEL', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    # Remplacer noms de personnes (Prénom Nom)", styles['CodeStyle']))
story.append(Paragraph("    texte = re.sub(r'\\b[A-Z][a-z]+\\s+[A-Z][a-zé]+\\b', 'CLIENT', texte)", styles['CodeStyle']))
story.append(Paragraph("", styles['CodeStyle']))
story.append(Paragraph("    return texte", styles['CodeStyle']))

# Construction du PDF
doc.build(story)
print(f"PDF créé avec succès : {pdf_file}")
