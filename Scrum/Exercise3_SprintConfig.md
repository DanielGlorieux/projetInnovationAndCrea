# Exercice 3 : Configuration du Sprint et Dashboard

## Objectif
Configurer Corrello pour gérer le sprint et visualiser les métriques de performance de l'équipe.

---

## 1. Configuration du Sprint dans Corrello

### Accès à Corrello
1. Aller sur : https://corrello.com/
2. Se connecter avec le compte créé en Exercice 1
3. Autoriser l'accès au tableau Trello

### Configuration du Sprint

#### Paramètres du Sprint
- **Nom du Sprint** : Sprint 1 - Analyse de Base
- **Date de début** : [Date de début du TD]
- **Date de fin** : [Date + 2 semaines]
- **Durée** : 10 jours ouvrables (2 semaines)
- **Objectif du Sprint** : Mettre en place le système d'analyse de base

#### Définition des colonnes
Mapper les colonnes Trello à Corrello :
- **To Do** → Non démarré
- **Sprint Backlog** → Planifié
- **In Progress** → En cours
- **Code Review** → En revue
- **Testing** → En test
- **Done** → Terminé

#### Configuration de la capacité
- **Vélocité moyenne** : 20 story points (à ajuster après quelques sprints)
- **Capacité d'équipe** : [Nombre de développeurs] × 5 points/personne = Total points
- **Jours de travail** : 10 jours
- **Points par jour** : Vélocité / Jours de travail = 2 points/jour

---

## 2. Déplacer les Cartes

### Processus de déplacement
1. **Product Backlog → Next Sprint** : Cartes qui respectent le DoR
2. **Next Sprint → Sprint Backlog** : Cartes validées pour le sprint actuel
3. **Sprint Backlog → In Progress** : Quand le travail commence
4. **In Progress → Done** : Quand les critères du DoD sont satisfaits

### Simulation d'un Sprint

#### Jour 1 (Lundi)
- US1 : Parser le Code Source → **In Progress**
- US2 : Détecter les Erreurs de Syntaxe → **Sprint Backlog**
- Burndown : 18 points restants

#### Jour 3 (Mercredi)
- US1 : Parser le Code Source → **Done** ✅ (5 points complétés)
- US2 : Détecter les Erreurs de Syntaxe → **In Progress**
- US3 : Identifier les Variables Non Définies → **In Progress**
- Burndown : 13 points restants

#### Jour 5 (Vendredi)
- US2 : Détecter les Erreurs de Syntaxe → **Done** ✅ (3 points complétés)
- US3 : Identifier les Variables Non Définies → **Code Review**
- US5 : Corriger les Indentations → **In Progress**
- Burndown : 10 points restants

#### Jour 7 (Mardi semaine 2)
- US3 : Identifier les Variables Non Définies → **Done** ✅ (5 points complétés)
- US5 : Corriger les Indentations → **Done** ✅ (3 points complétés)
- US4 : Détecter les Imports Inutilisés → **In Progress**
- Burndown : 2 points restants

#### Jour 10 (Vendredi semaine 2)
- US4 : Détecter les Imports Inutilisés → **Done** ✅ (2 points complétés)
- **Sprint terminé** 🎉
- Burndown : 0 points restants

---

## 3. Générer les Graphiques Burndown

### Burndown Chart - Sprint 1

```
Story Points
20 |●
18 |  ●___
16 |      \
14 |       \
12 |        ●
10 |         \___●
8  |             \
6  |              \
4  |               \
2  |                ●__
0  |___________________●___
   1  2  3  4  5  6  7  8  9  10
        Jours du Sprint
```

**Légende** :
- Ligne bleue : Idéal théorique
- Ligne rouge : Progression réelle

### Interprétation
- **Sprint réussi** : Toutes les US sont terminées
- **Vélocité réalisée** : 18 points
- **Vélocité prévue** : 18 points
- **Performance** : 100% ✅

---

## 4. Scénarios de Changement et Impact

### Scénario 1 : Ajout d'une US en cours de sprint
**Action** : Ajout de US11 (3 points) au jour 4

**Impact** :
- Burndown remonte de 10 à 13 points
- Risque de ne pas terminer le sprint
- Graphique montre une "bosse"
- **Décision** : Reporter US4 au prochain sprint

### Scénario 2 : Blocage technique
**Action** : US3 bloquée pendant 2 jours (jours 4-5)

**Impact** :
- Burndown plateau pendant 2 jours
- Pas de points complétés
- Graphique au-dessus de l'idéal
- **Action** : Daily standup pour débloquer

### Scénario 3 : US sous-estimée
**Action** : US1 prend 8 points au lieu de 5

**Impact** :
- Réévaluation en cours de sprint
- Burndown ajusté de 18 à 21 points
- Nécessité de retirer une US
- **Décision** : Reporter US4 (2 points)

### Scénario 4 : Membre absent
**Action** : 1 développeur absent 3 jours

**Impact** :
- Capacité réduite de 20 à 15 points
- Burndown plus lent
- **Action** : Réorganiser les US prioritaires

---

## 5. Dashboard et Graphiques de Performance

### Graphiques à Ajouter

#### 1. Velocity Chart (Vélocité)
Mesure les story points complétés par sprint

```
Sprint 1: ████████████████░░ 18 pts
Sprint 2: ██████████████████ 20 pts
Sprint 3: █████████████████░ 19 pts
Moyenne: 19 pts/sprint
```

**Utilité** : Prévoir la capacité future

#### 2. Cumulative Flow Diagram
Visualise le flux de travail

```
          Done
        /████████\
       / Testing  \
      /  In Review \
     /  In Progress \
    /   Sprint BL    \
   /  Next Sprint     \
  ────────────────────
  Jour 1 ... Jour 10
```

**Utilité** : Identifier les goulots d'étranglement

#### 3. Cycle Time
Temps moyen pour compléter une US

```
US1: 3 jours
US2: 2 jours
US3: 4 jours
US4: 2 jours
US5: 3 jours
Moyenne: 2.8 jours
```

**Utilité** : Optimiser le processus

#### 4. Lead Time
Temps depuis la création jusqu'à la complétion

```
Moyenne: 5 jours
75e percentile: 7 jours
95e percentile: 10 jours
```

**Utilité** : Prédire les délais

#### 5. Work in Progress (WIP)
Nombre de cartes en cours

```
Limite WIP: 3 cartes
Actuel: 2 cartes ✅
```

**Utilité** : Éviter la surcharge

#### 6. Burnup Chart
Vue cumulative du travail complété

```
100%|              ___●
    |          ___/
 75%|      ___/
    |  ___/
 50%|_/
    |________________
     Sprint 1 2 3 4 5
```

**Utilité** : Suivre l'avancement global

---

## 6. Métriques de Performance d'Équipe

### KPIs à Suivre

#### Productivité
- **Vélocité moyenne** : 19 points/sprint
- **Points complétés/jour** : 1.9
- **Taux de complétion** : 95%

#### Qualité
- **Bugs par US** : 0.2
- **Rework rate** : 5%
- **Code review time** : 0.5 jour

#### Prédictibilité
- **Sprint goal success rate** : 100%
- **Variance de vélocité** : ±2 points
- **Estimation accuracy** : 90%

#### Collaboration
- **Blockers résolus/jour** : 1.2
- **Temps de réponse** : < 4h
- **Participation daily** : 100%

---

## 7. Analyse et Amélioration Continue

### Questions à se poser
1. La vélocité est-elle stable ?
2. Y a-t-il des goulots d'étranglement ?
3. Les estimations sont-elles précises ?
4. Le WIP est-il sous contrôle ?
5. Le sprint goal est-il atteint ?

### Actions d'amélioration
- **Si vélocité en baisse** → Rétrospective pour identifier les obstacles
- **Si cycle time élevé** → Réduire le WIP
- **Si estimations inexactes** → Affiner le poker planning
- **Si bugs fréquents** → Renforcer les tests et code review

### Retrospective Sprint 1
**Ce qui a bien fonctionné** ✅
- Communication efficace
- US bien définies
- DoD respectée

**Ce qui peut être amélioré** 🔄
- Estimations plus précises pour les tâches techniques
- Anticiper les dépendances
- Temps de code review à réduire

**Actions pour Sprint 2** 🎯
- Ajouter un buffer de 10% sur les estimations
- Créer un diagramme de dépendances
- Définir des slots de code review quotidiens

---

## Checklist Exercice 3
- [ ] Corrello configuré et connecté
- [ ] Sprint créé avec dates et objectif
- [ ] Colonnes mappées correctement
- [ ] Cartes déplacées selon simulation
- [ ] Burndown chart généré
- [ ] Scénarios de changement testés
- [ ] Dashboard configuré avec minimum 4 graphiques
- [ ] Métriques de performance définies
- [ ] Analyse réalisée
- [ ] Plan d'amélioration établi
