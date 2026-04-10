# Exercice 2 : Élaboration des Premières User Stories

## Contexte du Projet
**Projet** : Logiciel de correction automatique de code  
**Client** : Chargé d'enseignement  
**Équipe** : Vous et vos collaborateurs

## Vision Produit
Créer un système automatisé capable d'analyser, corriger et améliorer le code source des étudiants, en fournissant des retours constructifs et pédagogiques.

## Valeur Métier
- Gagner du temps pour les enseignants
- Fournir un feedback immédiat aux étudiants
- Améliorer la qualité du code produit
- Standardiser l'évaluation

## Durée de Sprint Proposée
**2 semaines** (10 jours ouvrables)

---

## 3 Epics

### Epic 1 : [EPIC] Analyse et Détection d'Erreurs
**Vision** : Permettre au système d'analyser automatiquement le code et de détecter les erreurs courantes  
**Priorité** : Haute  
**Story Points** : 34

### Epic 2 : [EPIC] Correction Automatique
**Vision** : Fournir des suggestions de correction automatique pour les erreurs détectées  
**Priorité** : Haute  
**Story Points** : 21

### Epic 3 : [EPIC] Feedback Pédagogique
**Vision** : Générer des retours personnalisés et pédagogiques pour aider les étudiants à progresser  
**Priorité** : Moyenne  
**Story Points** : 21

---

## 5 Features

### Feature 1 : [FEATURE] Analyse Syntaxique
**Epic parent** : Epic 1 - Analyse et Détection d'Erreurs  
**Description** : En tant qu'enseignant, je veux que le système détecte les erreurs de syntaxe afin d'identifier rapidement les problèmes basiques  
**Priorité** : Haute  
**Story Points** : 13

### Feature 2 : [FEATURE] Détection d'Erreurs Logiques
**Epic parent** : Epic 1 - Analyse et Détection d'Erreurs  
**Description** : En tant qu'enseignant, je veux que le système identifie les erreurs de logique courantes afin d'améliorer la qualité du code  
**Priorité** : Haute  
**Story Points** : 13

### Feature 3 : [FEATURE] Correction de Syntaxe
**Epic parent** : Epic 2 - Correction Automatique  
**Description** : En tant qu'étudiant, je veux recevoir des corrections automatiques pour mes erreurs de syntaxe afin de gagner du temps  
**Priorité** : Haute  
**Story Points** : 8

### Feature 4 : [FEATURE] Suggestions d'Amélioration
**Epic parent** : Epic 2 - Correction Automatique  
**Description** : En tant qu'étudiant, je veux recevoir des suggestions pour améliorer mon code afin d'apprendre les bonnes pratiques  
**Priorité** : Moyenne  
**Story Points** : 13

### Feature 5 : [FEATURE] Rapport de Progression
**Epic parent** : Epic 3 - Feedback Pédagogique  
**Description** : En tant qu'étudiant, je veux voir mon évolution dans le temps afin de mesurer mes progrès  
**Priorité** : Basse  
**Story Points** : 8

---

## 10 User Stories

### User Story 1 : [US] Parser le Code Source
**Feature parent** : Feature 1 - Analyse Syntaxique  
**Description** : En tant que système, je veux parser le code source Python afin de créer un AST (Abstract Syntax Tree)  
**Story Points** : 5  
**Priorité** : Haute

**Critères d'acceptation** :
- [ ] Le système peut lire un fichier .py
- [ ] Un AST est généré avec succès
- [ ] Les erreurs de parsing sont capturées et reportées
- [ ] Supporte Python 3.8+

---

### User Story 2 : [US] Détecter les Erreurs de Syntaxe
**Feature parent** : Feature 1 - Analyse Syntaxique  
**Description** : En tant qu'enseignant, je veux que les erreurs de syntaxe soient détectées afin de les signaler aux étudiants  
**Story Points** : 3  
**Priorité** : Haute

**Critères d'acceptation** :
- [ ] Les parenthèses non fermées sont détectées
- [ ] Les indentations incorrectes sont identifiées
- [ ] La position exacte de l'erreur est fournie
- [ ] Un message d'erreur clair est généré

---

### User Story 3 : [US] Identifier les Variables Non Définies
**Feature parent** : Feature 2 - Détection d'Erreurs Logiques  
**Description** : En tant que système, je veux détecter les variables utilisées mais non définies afin d'éviter les erreurs d'exécution  
**Story Points** : 5  
**Priorité** : Haute

**Critères d'acceptation** :
- [ ] Les variables non définies sont listées
- [ ] Le numéro de ligne est précisé
- [ ] Les faux positifs sont minimisés
- [ ] Gestion du scope des variables

---

### User Story 4 : [US] Détecter les Imports Inutilisés
**Feature parent** : Feature 2 - Détection d'Erreurs Logiques  
**Description** : En tant qu'enseignant, je veux identifier les imports non utilisés afin d'encourager un code propre  
**Story Points** : 2  
**Priorité** : Moyenne

**Critères d'acceptation** :
- [ ] Tous les imports sont analysés
- [ ] Les imports non référencés sont identifiés
- [ ] Liste claire des imports à supprimer
- [ ] Exemples de correction fournis

---

### User Story 5 : [US] Corriger les Indentations
**Feature parent** : Feature 3 - Correction de Syntaxe  
**Description** : En tant qu'étudiant, je veux que mes erreurs d'indentation soient corrigées automatiquement afin de respecter PEP8  
**Story Points** : 3  
**Priorité** : Haute

**Critères d'acceptation** :
- [ ] Indentation à 4 espaces appliquée
- [ ] Cohérence dans tout le fichier
- [ ] Option pour prévisualiser avant application
- [ ] Préservation de la logique du code

---

### User Story 6 : [US] Corriger les Noms de Variables
**Feature parent** : Feature 3 - Correction de Syntaxe  
**Description** : En tant qu'étudiant, je veux recevoir des suggestions pour renommer mes variables afin de respecter les conventions  
**Story Points** : 5  
**Priorité** : Moyenne

**Critères d'acceptation** :
- [ ] Détection des noms non conformes (camelCase vs snake_case)
- [ ] Suggestions de noms plus descriptifs
- [ ] Refactoring automatique possible
- [ ] Respect de PEP8

---

### User Story 7 : [US] Suggérer l'Utilisation de Compréhensions de Liste
**Feature parent** : Feature 4 - Suggestions d'Amélioration  
**Description** : En tant qu'étudiant, je veux recevoir des suggestions pour utiliser les compréhensions de liste afin d'écrire du code plus pythonique  
**Story Points** : 5  
**Priorité** : Basse

**Critères d'acceptation** :
- [ ] Détection des boucles for convertibles
- [ ] Affichage de la version optimisée
- [ ] Explication de l'amélioration
- [ ] Comparaison de performance

---

### User Story 8 : [US] Générer un Score de Qualité
**Feature parent** : Feature 4 - Suggestions d'Amélioration  
**Description** : En tant qu'enseignant, je veux attribuer un score de qualité au code afin d'évaluer objectivement  
**Story Points** : 8  
**Priorité** : Moyenne

**Critères d'acceptation** :
- [ ] Score sur 100
- [ ] Critères clairs (syntaxe, style, logique, complexité)
- [ ] Pondération configurable
- [ ] Détail par catégorie

---

### User Story 9 : [US] Afficher l'Historique des Corrections
**Feature parent** : Feature 5 - Rapport de Progression  
**Description** : En tant qu'étudiant, je veux voir l'historique de mes corrections afin de ne pas répéter les mêmes erreurs  
**Story Points** : 5  
**Priorité** : Basse

**Critères d'acceptation** :
- [ ] Liste chronologique des soumissions
- [ ] Comparaison avant/après
- [ ] Statistiques d'amélioration
- [ ] Export en PDF

---

### User Story 10 : [US] Générer des Graphiques de Progression
**Feature parent** : Feature 5 - Rapport de Progression  
**Description** : En tant qu'étudiant, je veux visualiser ma progression avec des graphiques afin de me motiver  
**Story Points** : 3  
**Priorité** : Basse

**Critères d'acceptation** :
- [ ] Graphique d'évolution du score
- [ ] Répartition des types d'erreurs
- [ ] Comparaison avec la moyenne de la classe
- [ ] Interface intuitive

---

## Sprint Goal (Proposition pour Sprint 1)
**"Mettre en place le système d'analyse de base capable de parser du code Python et de détecter les erreurs de syntaxe et variables non définies"**

## User Stories pour le Next Sprint (Sprint 1)
Basé sur une vélocité estimée de 20 story points par sprint :

1. ✅ US1 : Parser le Code Source (5 points)
2. ✅ US2 : Détecter les Erreurs de Syntaxe (3 points)
3. ✅ US3 : Identifier les Variables Non Définies (5 points)
4. ✅ US5 : Corriger les Indentations (3 points)
5. ✅ US4 : Détecter les Imports Inutilisés (2 points)

**Total Sprint 1 : 18 story points**

## Backlog pour les sprints futurs
- Sprint 2 : US6, US8, US7 (18 points)
- Sprint 3 : US9, US10 + nouvelles US (8+ points)

## Questions à poser au client
- [ ] Quels langages de programmation prioriser ? (Python uniquement ou multi-langage ?)
- [ ] Niveau de détail souhaité pour le feedback ?
- [ ] Intégration avec des plateformes existantes (Moodle, GitHub Classroom) ?
- [ ] Volume de code à traiter simultanément ?
- [ ] Délais de correction acceptables ?
