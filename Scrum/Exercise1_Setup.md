# Exercice 1 : Configuration du Tableau Trello Scrum

## Objectif
Créer et configurer un tableau Trello pour gérer un projet avec la méthode SCRUM.

## Étapes à suivre

### 1. Créer le tableau Scrum Board
- Accéder à : https://trello.com/templates/engineering/scrum-board-dFzygb01
- Utiliser ce modèle pour créer votre tableau
- Lire les règles et exemples de cartes proposés

### 2. Définir DoR (Definition of Ready) et DoD (Definition of Done)

#### Definition of Ready (DoR) - Proposition
Une User Story est "prête" quand :
- [ ] Le titre est clair et explicite
- [ ] La description suit le format : "En tant que [rôle], je veux [action] afin de [bénéfice]"
- [ ] Les critères d'acceptation sont définis
- [ ] Les story points sont estimés
- [ ] La priorité est définie
- [ ] Les dépendances sont identifiées
- [ ] L'équipe comprend ce qui doit être fait

#### Definition of Done (DoD) - Proposition
Une User Story est "terminée" quand :
- [ ] Le code est écrit et testé
- [ ] Les tests unitaires passent
- [ ] La revue de code est effectuée
- [ ] La documentation est mise à jour
- [ ] La fonctionnalité est validée par le Product Owner
- [ ] Le code est mergé dans la branche principale
- [ ] Aucun bug bloquant n'est présent

### 3. Ajouter des membres
- Inviter les membres de l'équipe via email
- Assigner des rôles : Product Owner, Scrum Master, Développeurs

### 4. Configurer Agile Tools
- Installer le Power-Up "Agile Tools"
- Activer les story points
- Configurer l'échelle de story points (ex: 1, 2, 3, 5, 8, 13, 21)

### 5. Configurer Corrello
- Créer un compte Corrello
- Connecter le tableau Trello
- Configurer les sprints
- Activer les graphiques (Burndown, Velocity, etc.)

### 6. Configurer les étiquettes
Créer les étiquettes suivantes :
- 🔵 **Bleu** : Epic
- 🟢 **Vert** : Feature  
- 🟡 **Jaune** : User Story
- 🔴 **Rouge** : Bug
- 🟣 **Violet** : Technical Debt

### 7. Créer des modèles de carte

#### Modèle Epic
```
Titre: [EPIC] Nom de l'Epic

Description:
Vision: [Description de la vision globale]
Objectif: [Objectif principal]
Features associées: 
- [Liste des features]

Story Points: [Estimation globale]
Priorité: [Haute/Moyenne/Basse]
```

#### Modèle Feature
```
Titre: [FEATURE] Nom de la Feature

Description:
En tant que [rôle]
Je veux [fonctionnalité]
Afin de [bénéfice]

Epic parent: [Nom de l'Epic]
User Stories associées:
- [Liste des US]

Story Points: [Estimation]
Priorité: [Haute/Moyenne/Basse]
```

#### Modèle User Story
```
Titre: [US] Nom de la User Story

Description:
En tant que [rôle]
Je veux [action]
Afin de [bénéfice]

Critères d'acceptation:
- [ ] Critère 1
- [ ] Critère 2
- [ ] Critère 3

Feature parent: [Nom de la Feature]
Story Points: [1/2/3/5/8/13/21]
Priorité: [Haute/Moyenne/Basse]

Notes techniques:
[Détails d'implémentation si nécessaire]
```

### 8. Configurer les champs personnalisés
Ajouter les champs suivants :
- **Story Points** (Nombre) - via Agile Tools
- **Priorité** (Liste) : Haute, Moyenne, Basse
- **Type** (Liste) : Epic, Feature, User Story, Bug
- **Sprint** (Texte)
- **Estimation temps** (Nombre)

### 9. BONUS : Installer Forms by Blue Cat
- Installer : https://trello.com/power-ups/6139de588901011c01baf52f
- Créer des formulaires pour faciliter la création de cartes
- Standardiser la saisie des informations

## Checklist finale
- [ ] Tableau créé depuis le modèle
- [ ] DoR définie et documentée
- [ ] DoD définie et documentée
- [ ] Membres ajoutés et rôles assignés
- [ ] Agile Tools configuré
- [ ] Corrello configuré
- [ ] Étiquettes créées
- [ ] Modèles de carte créés
- [ ] Champs personnalisés ajoutés
- [ ] Forms by Blue Cat installé (bonus)
