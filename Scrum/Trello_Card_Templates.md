# 📋 Templates de Cartes Trello - Textes Prêts à Copier

## 🔵 EPIC 1 - Analyse et Détection d'Erreurs

### Titre
```
[EPIC] Analyse et Détection d'Erreurs
```

### Description
```
Vision: 
Permettre au système d'analyser automatiquement le code source et de détecter les erreurs courantes (syntaxe, logique, style).

Objectif Principal:
Fournir un moteur d'analyse robuste capable d'identifier rapidement les problèmes dans le code des étudiants.

Features Associées:
- Feature 1: Analyse Syntaxique
- Feature 2: Détection d'Erreurs Logiques

Valeur Métier:
Gagner du temps pour les enseignants en automatisant la première phase de correction.

Hypothèses:
- Le système supporte Python 3.8+
- Les fichiers font moins de 1000 lignes
- Temps de traitement < 5 secondes

Risques:
- Complexité des AST
- Faux positifs
- Performance sur gros fichiers
```

### Champs
- **Type**: Epic
- **Priorité**: Haute
- **Story Points**: 34
- **Étiquette**: 🔵 Bleu

---

## 🔵 EPIC 2 - Correction Automatique

### Titre
```
[EPIC] Correction Automatique
```

### Description
```
Vision:
Fournir des suggestions de correction automatique intelligentes pour les erreurs détectées.

Objectif Principal:
Permettre aux étudiants de corriger rapidement leur code avec des suggestions contextuelles.

Features Associées:
- Feature 3: Correction de Syntaxe
- Feature 4: Suggestions d'Amélioration

Valeur Métier:
Accélérer l'apprentissage en fournissant un feedback immédiat et actionnable.

Hypothèses:
- Les corrections proposées sont valides à 95%
- L'étudiant peut accepter/refuser les suggestions
- Prévisualisation avant application

Risques:
- Corrections incorrectes
- Complexité des refactorings
- Régression de code fonctionnel
```

### Champs
- **Type**: Epic
- **Priorité**: Haute
- **Story Points**: 21
- **Étiquette**: 🔵 Bleu

---

## 🔵 EPIC 3 - Feedback Pédagogique

### Titre
```
[EPIC] Feedback Pédagogique
```

### Description
```
Vision:
Générer des retours personnalisés et pédagogiques pour aider les étudiants à progresser.

Objectif Principal:
Créer un système de feedback intelligent qui s'adapte au niveau de l'étudiant.

Features Associées:
- Feature 5: Rapport de Progression

Valeur Métier:
Améliorer l'engagement des étudiants et mesurer leur évolution dans le temps.

Hypothèses:
- Les données de progression sont stockées
- Les étudiants consultent régulièrement leur dashboard
- Les métriques sont motivantes

Risques:
- Surcharge d'informations
- Comparaisons démotivantes
- Protection des données personnelles
```

### Champs
- **Type**: Epic
- **Priorité**: Moyenne
- **Story Points**: 21
- **Étiquette**: 🔵 Bleu

---

## 🟢 FEATURE 1 - Analyse Syntaxique

### Titre
```
[FEATURE] Analyse Syntaxique
```

### Description
```
En tant qu'enseignant
Je veux que le système détecte automatiquement les erreurs de syntaxe
Afin d'identifier rapidement les problèmes basiques et fournir un feedback immédiat

Epic Parent: 
[EPIC] Analyse et Détection d'Erreurs

User Stories Associées:
- US1: Parser le Code Source
- US2: Détecter les Erreurs de Syntaxe

Bénéfices:
- Gain de temps de correction: ~60%
- Feedback immédiat pour l'étudiant
- Standardisation des messages d'erreur

Critères de Succès:
- 95% des erreurs de syntaxe détectées
- Temps de traitement < 2 secondes
- Messages d'erreur clairs et pédagogiques

Dépendances:
- Bibliothèque AST Python
- Module de parsing
```

### Champs
- **Type**: Feature
- **Priorité**: Haute
- **Story Points**: 13
- **Sprint**: Sprint 1
- **Étiquette**: 🟢 Vert

---

## 🟢 FEATURE 2 - Détection d'Erreurs Logiques

### Titre
```
[FEATURE] Détection d'Erreurs Logiques
```

### Description
```
En tant qu'enseignant
Je veux que le système identifie les erreurs de logique courantes
Afin d'améliorer la qualité du code et enseigner les bonnes pratiques

Epic Parent:
[EPIC] Analyse et Détection d'Erreurs

User Stories Associées:
- US3: Identifier les Variables Non Définies
- US4: Détecter les Imports Inutilisés

Bénéfices:
- Prévention des bugs à l'exécution
- Amélioration de la qualité du code
- Apprentissage des conventions

Critères de Succès:
- Détection des variables non définies: 100%
- Taux de faux positifs < 5%
- Couverture des erreurs courantes: 80%

Dépendances:
- Analyse de scope
- Table des symboles
```

### Champs
- **Type**: Feature
- **Priorité**: Haute
- **Story Points**: 13
- **Sprint**: Sprint 1
- **Étiquette**: 🟢 Vert

---

## 🟢 FEATURE 3 - Correction de Syntaxe

### Titre
```
[FEATURE] Correction de Syntaxe
```

### Description
```
En tant qu'étudiant
Je veux recevoir des corrections automatiques pour mes erreurs de syntaxe
Afin de gagner du temps et apprendre la syntaxe correcte

Epic Parent:
[EPIC] Correction Automatique

User Stories Associées:
- US5: Corriger les Indentations
- US6: Corriger les Noms de Variables

Bénéfices:
- Gain de temps pour l'étudiant
- Apprentissage par l'exemple
- Code conforme PEP8

Critères de Succès:
- Corrections valides: 98%
- Prévisualisation avant application
- Possibilité d'annuler

Dépendances:
- Module de refactoring
- Parser AST
```

### Champs
- **Type**: Feature
- **Priorité**: Haute
- **Story Points**: 8
- **Sprint**: Sprint 1
- **Étiquette**: 🟢 Vert

---

## 🟢 FEATURE 4 - Suggestions d'Amélioration

### Titre
```
[FEATURE] Suggestions d'Amélioration
```

### Description
```
En tant qu'étudiant
Je veux recevoir des suggestions pour améliorer mon code
Afin d'apprendre les bonnes pratiques et écrire du code pythonique

Epic Parent:
[EPIC] Correction Automatique

User Stories Associées:
- US7: Suggérer l'Utilisation de Compréhensions de Liste
- US8: Générer un Score de Qualité

Bénéfices:
- Amélioration continue
- Apprentissage des idiomes Python
- Motivation par le score

Critères de Succès:
- Suggestions pertinentes: 90%
- Explications pédagogiques claires
- Score objectif et reproductible

Dépendances:
- Moteur de règles qualité
- Base de patterns
```

### Champs
- **Type**: Feature
- **Priorité**: Moyenne
- **Story Points**: 13
- **Sprint**: Sprint 2
- **Étiquette**: 🟢 Vert

---

## 🟢 FEATURE 5 - Rapport de Progression

### Titre
```
[FEATURE] Rapport de Progression
```

### Description
```
En tant qu'étudiant
Je veux voir mon évolution dans le temps
Afin de mesurer mes progrès et rester motivé

Epic Parent:
[EPIC] Feedback Pédagogique

User Stories Associées:
- US9: Afficher l'Historique des Corrections
- US10: Générer des Graphiques de Progression

Bénéfices:
- Motivation accrue
- Visibilité sur les progrès
- Identification des points faibles

Critères de Succès:
- Données historiques complètes
- Graphiques lisibles et pertinents
- Comparaison temporelle

Dépendances:
- Base de données
- Bibliothèque graphiques
```

### Champs
- **Type**: Feature
- **Priorité**: Basse
- **Story Points**: 8
- **Sprint**: Sprint 3
- **Étiquette**: 🟢 Vert

---

## 🟡 USER STORY 1 - Parser le Code Source

### Titre
```
[US] Parser le Code Source
```

### Description
```
En tant que système
Je veux parser le code source Python
Afin de créer un AST (Abstract Syntax Tree) exploitable

Feature Parent:
[FEATURE] Analyse Syntaxique

Contexte:
Le parsing est la première étape de l'analyse. Il doit être robuste et gérer les erreurs gracieusement.

Critères d'Acceptation:
☐ Le système peut lire un fichier .py depuis le système de fichiers
☐ Un AST est généré avec succès pour du code valide
☐ Les erreurs de parsing sont capturées et reportées clairement
☐ Supporte Python 3.8, 3.9, 3.10, 3.11
☐ Gestion des encodages (UTF-8, ASCII, Latin-1)
☐ Temps de parsing < 1 seconde pour 500 lignes

Notes Techniques:
- Utiliser le module 'ast' de Python
- Gérer les exceptions SyntaxError
- Encoder les positions des erreurs (ligne, colonne)
- Logger les fichiers problématiques

Tests:
- Fichier valide simple
- Fichier avec erreur de syntaxe
- Fichier avec caractères spéciaux
- Fichier de 1000+ lignes

Définition of Done:
☐ Code implémenté et commenté
☐ Tests unitaires passent (couverture > 80%)
☐ Documentation API complète
☐ Revue de code validée
☐ Démo fonctionnelle au client
```

### Champs
- **Type**: User Story
- **Priorité**: Haute
- **Story Points**: 5
- **Sprint**: Sprint 1
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 2 - Détecter les Erreurs de Syntaxe

### Titre
```
[US] Détecter les Erreurs de Syntaxe
```

### Description
```
En tant qu'enseignant
Je veux que les erreurs de syntaxe soient détectées
Afin de les signaler clairement aux étudiants

Feature Parent:
[FEATURE] Analyse Syntaxique

Contexte:
Les étudiants font souvent des erreurs simples (parenthèses, indentation). Le système doit les identifier avec des messages pédagogiques.

Critères d'Acceptation:
☐ Les parenthèses/crochets/accolades non fermés sont détectés
☐ Les indentations incorrectes sont identifiées
☐ La position exacte de l'erreur est fournie (ligne, colonne)
☐ Un message d'erreur clair et pédagogique est généré
☐ Détection des deux-points manquants (if, for, def, etc.)
☐ Identification des quotes non fermées

Notes Techniques:
- Parser le code et capturer les SyntaxError
- Créer des messages d'erreur personnalisés
- Stocker les erreurs dans une structure de données
- Formater la sortie en JSON

Exemples d'Erreurs:
1. "Parenthèse ouvrante '(' à la ligne 5 n'est pas fermée"
2. "Indentation incorrecte ligne 12: attendu 4 espaces, trouvé 2"
3. "Deux-points manquants après 'if' ligne 8"

Tests:
- Parenthèses non fermées
- Indentation mixte (tabs/espaces)
- Quotes non fermées
- Deux-points manquants

Définition of Done:
☐ Code implémenté avec gestion d'erreurs
☐ Tests unitaires > 85% couverture
☐ Messages testés par un enseignant
☐ Documentation utilisateur
☐ Démo validée
```

### Champs
- **Type**: User Story
- **Priorité**: Haute
- **Story Points**: 3
- **Sprint**: Sprint 1
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 3 - Identifier les Variables Non Définies

### Titre
```
[US] Identifier les Variables Non Définies
```

### Description
```
En tant que système
Je veux détecter les variables utilisées mais non définies
Afin d'éviter les erreurs NameError à l'exécution

Feature Parent:
[FEATURE] Détection d'Erreurs Logiques

Contexte:
Les étudiants oublient souvent de définir leurs variables avant de les utiliser. Cette US prévient ces bugs.

Critères d'Acceptation:
☐ Les variables utilisées mais non définies sont listées
☐ Le numéro de ligne exact est précisé
☐ Les faux positifs sont minimisés (<5%)
☐ Gestion correcte du scope des variables (local, global, nonlocal)
☐ Détection dans les fonctions et classes
☐ Gestion des imports et variables built-in

Notes Techniques:
- Parcourir l'AST et construire une table des symboles
- Tracker les définitions (assignments, imports, params)
- Tracker les utilisations (Load context)
- Vérifier scope par scope
- Exclure les built-ins Python

Cas Limites:
- Variables définies dans if/else
- Variables de boucle
- Compréhensions de liste
- Variables globales
- Attributs de classe

Tests:
- Variable simple non définie
- Variable dans une fonction
- Variable conditionnelle
- Variable de boucle
- Import vs variable

Définition of Done:
☐ Implémentation complète avec scopes
☐ Tests unitaires détaillés
☐ Taux de faux positifs < 5%
☐ Performance testée (fichiers 500+ lignes)
☐ Validation client
```

### Champs
- **Type**: User Story
- **Priorité**: Haute
- **Story Points**: 5
- **Sprint**: Sprint 1
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 4 - Détecter les Imports Inutilisés

### Titre
```
[US] Détecter les Imports Inutilisés
```

### Description
```
En tant qu'enseignant
Je veux identifier les imports non utilisés
Afin d'encourager un code propre et maintenable

Feature Parent:
[FEATURE] Détection d'Erreurs Logiques

Contexte:
Les imports inutiles alourdissent le code et créent de la confusion. C'est une bonne pratique de les supprimer.

Critères d'Acceptation:
☐ Tous les imports (import, from...import) sont analysés
☐ Les imports non référencés dans le code sont identifiés
☐ Liste claire avec ligne de chaque import inutilisé
☐ Distinction import module vs import fonction/classe
☐ Gestion des imports avec alias (as)
☐ Suggestion de suppression automatique

Notes Techniques:
- Parser les instructions import
- Vérifier chaque nom importé dans le code
- Gérer les cas: import module, from module import name
- Tracker l'utilisation avec visitor pattern
- Formater le rapport

Exemples:
```python
import os  # Ligne 1 - Inutilisé
import sys  # Ligne 2 - Utilisé ligne 10
from math import pi, sqrt  # Ligne 3 - pi inutilisé, sqrt utilisé

print(sys.version)  # Ligne 10
result = sqrt(16)  # Ligne 11
```

Rapport:
- Ligne 1: import 'os' non utilisé → Supprimer
- Ligne 3: 'pi' de math non utilisé → Remplacer par 'from math import sqrt'

Tests:
- Import module complet inutilisé
- Import sélectif partiellement utilisé
- Import avec alias
- Import utilisé dans docstring

Définition of Done:
☐ Détection précise des imports
☐ Rapport formaté lisible
☐ Tests de non-régression
☐ Documentation
☐ Validation enseignant
```

### Champs
- **Type**: User Story
- **Priorité**: Moyenne
- **Story Points**: 2
- **Sprint**: Sprint 1
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 5 - Corriger les Indentations

### Titre
```
[US] Corriger les Indentations
```

### Description
```
En tant qu'étudiant
Je veux que mes erreurs d'indentation soient corrigées automatiquement
Afin de respecter PEP8 et éviter les erreurs de syntaxe

Feature Parent:
[FEATURE] Correction de Syntaxe

Contexte:
L'indentation est cruciale en Python. Les étudiants mélangent souvent tabs et espaces.

Critères d'Acceptation:
☐ Indentation à 4 espaces appliquée partout (PEP8)
☐ Conversion automatique des tabs en 4 espaces
☐ Cohérence dans tout le fichier
☐ Option pour prévisualiser avant application
☐ Préservation de la logique du code
☐ Gestion des lignes vides et commentaires

Notes Techniques:
- Tokenizer Python pour analyser l'indentation
- Détecter le style actuel (tabs, 2 espaces, 4 espaces, mixte)
- Reconstruire le fichier avec indentation uniforme
- Mode preview (diff) avant application
- Backup automatique du fichier original

Règles d'Indentation PEP8:
- 4 espaces par niveau
- Pas de tabs
- Continuation sur plusieurs lignes: +4 espaces
- Fermeture de structures: alignée ou indentée

Exemples de Correction:
```python
# Avant
def hello():
  print("world")  # 2 espaces
    print("!")    # 4 espaces

# Après
def hello():
    print("world")  # 4 espaces
    print("!")      # 4 espaces
```

Tests:
- Fichier avec tabs
- Fichier avec 2 espaces
- Fichier mixte (tabs + espaces)
- Lignes de continuation
- Structures imbriquées

Définition of Done:
☐ Correction fonctionnelle
☐ Mode preview implémenté
☐ Tests avec différents styles
☐ Aucune perte de code
☐ Validation sur vrais fichiers étudiants
```

### Champs
- **Type**: User Story
- **Priorité**: Haute
- **Story Points**: 3
- **Sprint**: Sprint 1
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 6 - Corriger les Noms de Variables

### Titre
```
[US] Corriger les Noms de Variables
```

### Description
```
En tant qu'étudiant
Je veux recevoir des suggestions pour renommer mes variables
Afin de respecter les conventions Python (PEP8)

Feature Parent:
[FEATURE] Correction de Syntaxe

Contexte:
Les noms de variables doivent être descriptifs et suivre snake_case en Python.

Critères d'Acceptation:
☐ Détection des noms non conformes (camelCase, PascalCase, SCREAMING)
☐ Suggestions de noms plus descriptifs (si noms trop courts)
☐ Refactoring automatique possible (renommer partout)
☐ Respect de PEP8 (snake_case pour variables/fonctions)
☐ Conservation des constantes en MAJUSCULES
☐ Détection des noms réservés ou ambigus

Notes Techniques:
- Parser l'AST pour trouver toutes les variables
- Vérifier le style de nommage avec regex
- Suggérer des alternatives
- Refactorer avec ast.NodeTransformer
- Préserver les références

Règles de Nommage PEP8:
- Variables/fonctions: snake_case (mon_compteur)
- Classes: PascalCase (MaClasse)
- Constantes: SCREAMING_SNAKE_CASE (MAX_SIZE)
- Noms descriptifs (pas 'x', 'temp', 'var1')

Exemples de Suggestions:
```python
# Avant → Après
myVariable → my_variable
firstName → first_name
c → counter (avec contexte)
MAX_value → MAX_VALUE
TempVar → temp_var
```

Niveaux de Suggestion:
1. Erreur: Nom réservé (list, dict, str)
2. Warning: Mauvaise convention (camelCase)
3. Info: Nom peu descriptif (x, tmp)

Tests:
- camelCase vers snake_case
- Variable d'une lettre
- Nom réservé
- Refactoring complet

Définition of Done:
☐ Détection des styles
☐ Suggestions pertinentes
☐ Refactoring sans casser le code
☐ Tests de régression
☐ Interface preview
```

### Champs
- **Type**: User Story
- **Priorité**: Moyenne
- **Story Points**: 5
- **Sprint**: Sprint 2
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 7 - Suggérer Compréhensions de Liste

### Titre
```
[US] Suggérer l'Utilisation de Compréhensions de Liste
```

### Description
```
En tant qu'étudiant
Je veux recevoir des suggestions pour utiliser les compréhensions de liste
Afin d'écrire du code plus pythonique et performant

Feature Parent:
[FEATURE] Suggestions d'Amélioration

Contexte:
Les list comprehensions sont idiomatiques en Python et souvent plus rapides que les boucles.

Critères d'Acceptation:
☐ Détection des boucles for convertibles en compréhension
☐ Affichage de la version optimisée
☐ Explication pédagogique de l'amélioration
☐ Comparaison de performance (si significative)
☐ Gestion des conditions (if)
☐ Détection des compréhensions imbriquées (warning si trop complexe)

Notes Techniques:
- Identifier pattern: for + append
- Vérifier simplicité (pas d'effets de bord)
- Transformer en compréhension
- Estimer gain de performance
- Formater la suggestion

Patterns Détectables:
```python
# Pattern 1: Simple loop
result = []
for item in items:
    result.append(item * 2)
# → [item * 2 for item in items]

# Pattern 2: With condition
result = []
for item in items:
    if item > 0:
        result.append(item)
# → [item for item in items if item > 0]

# Pattern 3: Transformation
names = []
for user in users:
    names.append(user.name)
# → [user.name for user in users]
```

Ne PAS Suggérer Si:
- Corps de boucle complexe (>2 lignes)
- Effets de bord (print, I/O)
- Compréhension imbriquée trop profonde

Tests:
- Boucle simple avec append
- Boucle avec condition
- Boucle avec transformation
- Boucle non éligible

Définition of Done:
☐ Détection précise des patterns
☐ Suggestions valides
☐ Explications pédagogiques
☐ Tests de performance
☐ Validation enseignant
```

### Champs
- **Type**: User Story
- **Priorité**: Basse
- **Story Points**: 5
- **Sprint**: Sprint 2
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 8 - Générer un Score de Qualité

### Titre
```
[US] Générer un Score de Qualité
```

### Description
```
En tant qu'enseignant
Je veux attribuer un score de qualité au code
Afin d'évaluer objectivement le travail des étudiants

Feature Parent:
[FEATURE] Suggestions d'Amélioration

Contexte:
Un score objectif aide à évaluer et comparer le code des étudiants de manière standardisée.

Critères d'Acceptation:
☐ Score sur 100 points
☐ Critères clairs: syntaxe (25%), style (25%), logique (25%), complexité (25%)
☐ Pondération configurable par l'enseignant
☐ Détail par catégorie avec justification
☐ Évolution du score visible dans le temps
☐ Seuils: Excellent (>85), Bon (70-85), Moyen (50-70), Faible (<50)

Notes Techniques:
- Calculer métriques pour chaque catégorie
- Appliquer pondération
- Agréger en score total
- Générer rapport détaillé JSON/PDF
- Stocker historique

Catégories de Score:

1. **Syntaxe (25 points)**
   - Pas d'erreurs de syntaxe: 25
   - Erreurs mineures: 15
   - Erreurs majeures: 0

2. **Style (25 points)**
   - PEP8 parfait: 25
   - Quelques violations: 15-20
   - Nombreuses violations: 0-10

3. **Logique (25 points)**
   - Pas d'erreurs logiques: 25
   - Variables non définies: -5 chacune
   - Imports inutilisés: -2 chacun
   - Dead code: -3

4. **Complexité (25 points)**
   - Complexité cyclomatique < 10: 25
   - Complexité 10-15: 15
   - Complexité > 15: 0-10

Formule:
```
Score = (Syntaxe × W1 + Style × W2 + Logique × W3 + Complexité × W4)
Avec W1 + W2 + W3 + W4 = 1
```

Exemple de Rapport:
```
Score Total: 78/100 (Bon)

Syntaxe: 25/25 ✓
Style: 18/25 ⚠
  - 3 violations PEP8 (indentation)
  - Noms de variables non conformes
  
Logique: 20/25 ⚠
  - 1 import inutilisé
  - 2 variables peu descriptives

Complexité: 15/25 ⚠
  - Fonction main() trop complexe (CC=12)
```

Tests:
- Code parfait → 100
- Code avec erreurs syntaxe
- Code avec mauvais style
- Code complexe

Définition of Done:
☐ Calcul de score fonctionnel
☐ Pondération configurable
☐ Rapport détaillé
☐ Tests sur vrais codes
☐ Validation barème enseignant
```

### Champs
- **Type**: User Story
- **Priorité**: Moyenne
- **Story Points**: 8
- **Sprint**: Sprint 2
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 9 - Afficher l'Historique des Corrections

### Titre
```
[US] Afficher l'Historique des Corrections
```

### Description
```
En tant qu'étudiant
Je veux voir l'historique de mes corrections
Afin de ne pas répéter les mêmes erreurs

Feature Parent:
[FEATURE] Rapport de Progression

Contexte:
L'historique permet aux étudiants de suivre leur évolution et d'identifier leurs erreurs récurrentes.

Critères d'Acceptation:
☐ Liste chronologique des soumissions (plus récent d'abord)
☐ Comparaison avant/après pour chaque correction
☐ Statistiques d'amélioration (score, erreurs résolues)
☐ Filtrage par date, type d'erreur
☐ Export en PDF pour portfolio
☐ Limite à 50 dernières soumissions (pagination)

Notes Techniques:
- Base de données SQLite/PostgreSQL
- Table: submissions (id, student_id, code_before, code_after, timestamp, score, errors)
- API REST: GET /history?student_id=X&limit=50
- Frontend: liste avec diff viewer
- Export PDF avec jinja2 ou reportlab

Structure de Données:
```json
{
  "submission_id": "sub_123",
  "timestamp": "2026-03-26T09:00:00Z",
  "filename": "tp1_exercice2.py",
  "score_before": 45,
  "score_after": 78,
  "errors_fixed": [
    "Indentation ligne 12",
    "Variable 'result' non définie",
    "Import 'os' inutilisé"
  ],
  "diff_url": "/diff/sub_123"
}
```

Interface Utilisateur:
- Timeline verticale avec cards
- Chaque card: date, fichier, score, amélioration
- Clic → voir détails et diff
- Bouton export PDF
- Filtres: date, fichier, type erreur

Diff Viewer:
- Vue côte à côte (before/after)
- Highlighting des changements
- Annotations des corrections

Tests:
- Récupération historique
- Filtres
- Pagination
- Export PDF
- Performance (50+ soumissions)

Définition of Done:
☐ Base de données configurée
☐ API fonctionnelle
☐ Interface utilisateur intuitive
☐ Export PDF
☐ Tests E2E
```

### Champs
- **Type**: User Story
- **Priorité**: Basse
- **Story Points**: 5
- **Sprint**: Sprint 3
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🟡 USER STORY 10 - Générer des Graphiques de Progression

### Titre
```
[US] Générer des Graphiques de Progression
```

### Description
```
En tant qu'étudiant
Je veux visualiser ma progression avec des graphiques
Afin de me motiver et identifier mes axes d'amélioration

Feature Parent:
[FEATURE] Rapport de Progression

Contexte:
Les visualisations rendent les progrès tangibles et motivent les étudiants à s'améliorer.

Critères d'Acceptation:
☐ Graphique d'évolution du score dans le temps (line chart)
☐ Répartition des types d'erreurs (pie chart)
☐ Comparaison avec la moyenne de la classe (bar chart)
☐ Évolution du nombre d'erreurs (area chart)
☐ Interface interactive (zoom, hover tooltips)
☐ Export des graphiques en PNG/SVG

Notes Techniques:
- Frontend: Chart.js ou D3.js
- Backend: générer données agrégées
- API: GET /stats?student_id=X&period=30days
- Calcul moyenne classe (anonymisée)
- Caching des stats (Redis)

Graphiques à Implémenter:

1. **Évolution du Score** (Line Chart)
   - X: Dates des soumissions
   - Y: Score (0-100)
   - Ligne de tendance
   - Moyenne mobile (7 jours)

2. **Types d'Erreurs** (Pie Chart)
   - Syntaxe: 30%
   - Style: 25%
   - Logique: 35%
   - Complexité: 10%

3. **Comparaison Classe** (Bar Chart)
   - Moi: 78
   - Moyenne classe: 72
   - Top 25%: 85
   - Médiane: 70

4. **Erreurs dans le Temps** (Area Chart)
   - Empilé: syntaxe, style, logique
   - Tendance décroissante = progrès

Exemple de Données:
```json
{
  "score_evolution": [
    {"date": "2026-03-01", "score": 45},
    {"date": "2026-03-08", "score": 62},
    {"date": "2026-03-15", "score": 78},
    {"date": "2026-03-22", "score": 85}
  ],
  "error_distribution": {
    "syntax": 12,
    "style": 18,
    "logic": 15,
    "complexity": 5
  },
  "class_comparison": {
    "my_score": 78,
    "class_average": 72,
    "class_median": 70,
    "top_25_percent": 85
  }
}
```

Fonctionnalités Interactives:
- Hover: afficher valeur exacte
- Clic: détails de la soumission
- Filtrer par période (7j, 30j, tout)
- Zoom sur timeline

Tests:
- Génération graphiques
- Données correctes
- Performance (100+ points)
- Responsive design
- Export image

Définition of Done:
☐ 4 graphiques implémentés
☐ Interactivité fonctionnelle
☐ Design responsive
☐ Export PNG/SVG
☐ Tests visuels validés
```

### Champs
- **Type**: User Story
- **Priorité**: Basse
- **Story Points**: 3
- **Sprint**: Sprint 3
- **Assigné à**: [Nom du développeur]
- **Étiquette**: 🟡 Jaune

---

## 🔴 TEMPLATE BUG

### Titre
```
[BUG] [Titre court du bug]
```

### Description
```
Environnement:
- OS: [Windows/Linux/Mac]
- Python: [Version]
- Navigateur: [Chrome/Firefox/Safari] [Version]

Comportement Attendu:
[Décrire ce qui devrait se passer]

Comportement Observé:
[Décrire ce qui se passe réellement]

Étapes pour Reproduire:
1. [Première étape]
2. [Deuxième étape]
3. [Troisième étape]

Logs/Erreurs:
```
[Coller les messages d'erreur ou logs]
```

Impact:
☐ Bloquant (empêche l'utilisation)
☐ Majeur (fonctionnalité importante cassée)
☐ Mineur (workaround possible)
☐ Cosmétique (UI/UX)

Workaround:
[Si un workaround existe, le décrire]

User Story Liée:
[US correspondante si applicable]
```

### Champs
- **Type**: Bug
- **Priorité**: [Haute/Moyenne/Basse selon impact]
- **Story Points**: [Estimation]
- **Sprint**: [À planifier]
- **Assigné à**: [Nom]
- **Étiquette**: 🔴 Rouge

---

## 🟣 TEMPLATE TECHNICAL DEBT

### Titre
```
[TECH DEBT] [Description de la dette]
```

### Description
```
Origine:
[Pourquoi cette dette existe? Sprint rapide, manque de temps, hack temporaire?]

Dette Actuelle:
[Décrire l'état actuel du code/architecture]

Impact:
☐ Performance dégradée
☐ Maintenabilité difficile
☐ Tests incomplets
☐ Documentation manquante
☐ Couplage élevé
☐ Duplication de code

État Souhaité:
[Décrire comment ça devrait être]

Bénéfices du Refactoring:
- [Bénéfice 1]
- [Bénéfice 2]
- [Bénéfice 3]

Coût Estimé:
[Story points ou temps estimé]

Priorité:
☐ Urgent (bloque nouvelles features)
☐ Important (ralentit le développement)
☐ Peut attendre (amélioration continue)

Notes:
[Contexte supplémentaire, liens vers code, etc.]
```

### Champs
- **Type**: Technical Debt
- **Priorité**: [Haute/Moyenne/Basse]
- **Story Points**: [Estimation]
- **Sprint**: [À planifier]
- **Assigné à**: [Nom]
- **Étiquette**: 🟣 Violet

---

## 📝 TEMPLATE TÂCHE TECHNIQUE

### Titre
```
[TASK] [Titre de la tâche]
```

### Description
```
Objectif:
[But de cette tâche technique]

User Story Parent:
[US à laquelle cette tâche contribue]

Description Détaillée:
[Expliquer ce qui doit être fait]

Étapes:
1. [Première étape]
2. [Deuxième étape]
3. [Troisième étape]

Critères de Complétion:
☐ [Critère 1]
☐ [Critère 2]
☐ [Critère 3]

Dépendances:
- [Tâche ou US qui doit être faite avant]

Ressources:
- [Liens vers documentation, tutoriels, etc.]

Risques:
[Risques identifiés et mitigation]

Estimation:
[Temps estimé en heures]
```

### Champs
- **Type**: Task
- **Priorité**: [Selon US parent]
- **Estimation**: [Heures]
- **Sprint**: [Courant]
- **Assigné à**: [Nom]
- **Étiquette**: Selon contexte

---

## 📊 TEMPLATE SPIKE (Investigation)

### Titre
```
[SPIKE] [Sujet de l'investigation]
```

### Description
```
Question à Répondre:
[Quelle décision technique dépend de ce spike?]

Contexte:
[Pourquoi cette investigation est nécessaire?]

Objectifs:
☐ [Objectif 1]
☐ [Objectif 2]
☐ [Objectif 3]

Approches à Explorer:
1. [Approche 1] - Pros: [X] / Cons: [Y]
2. [Approche 2] - Pros: [X] / Cons: [Y]
3. [Approche 3] - Pros: [X] / Cons: [Y]

Livrables:
☐ Document de décision (ADR)
☐ Prototype fonctionnel
☐ Comparaison performance
☐ Recommandation avec justification

Time-box:
[Durée maximale du spike, ex: 4 heures]

Critères de Succès:
[Comment saurons-nous que le spike est réussi?]

Décision Attendue:
[Quelle décision sera prise après le spike?]
```

### Champs
- **Type**: Spike
- **Priorité**: Haute (bloquant)
- **Time-box**: [Heures]
- **Sprint**: [Courant]
- **Assigné à**: [Nom]
- **Étiquette**: Selon contexte
