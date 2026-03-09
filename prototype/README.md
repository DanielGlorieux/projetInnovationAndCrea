# AquaIA — Prototype Dashboard

Prototype React de l'interface web **AquaIA**, un système de surveillance intelligente des eaux souterraines par IA et IoT au Sahel.

Ce prototype représente la **Couche Interface** de l'architecture AquaIA décrite dans la présentation du projet :

- **Tableau de bord** avec indicateurs clés (capteurs en ligne, niveau moyen, alertes, précision IA)
- **Graphique interactif** d'évolution du niveau d'eau avec prédictions LSTM (IA)
- **Carte des capteurs** positionnés au Burkina Faso avec état en temps réel
- **Tableau des capteurs IoT** avec mesures (niveau, température, conductivité, pH, batterie)
- **Panneau d'alertes communautaires** (SMS/App) avec statut d'envoi

## Démarrage

```bash
cd prototype
npm install
npm run dev
```

Ouvrir http://localhost:5173 dans le navigateur.

## Scripts

| Commande | Description |
|----------|-------------|
| `npm run dev` | Serveur de développement (Vite) |
| `npm run build` | Build de production |
| `npm run lint` | Linting ESLint |
| `npm run preview` | Prévisualisation du build |

## Technologies

- **React 19** + **Vite 6** — Framework UI et bundler
- **SVG pur** — Graphiques et carte (sans dépendances externes)
- **Données simulées** — Mock data représentant des capteurs piézométriques IoT

## Architecture du Prototype

```
prototype/
├── src/
│   ├── components/
│   │   ├── AlertsPanel.jsx      # Alertes communautaires SMS/App
│   │   ├── SensorMap.jsx        # Carte Burkina Faso avec capteurs
│   │   ├── SensorTable.jsx      # Tableau détaillé des capteurs IoT
│   │   ├── StatsOverview.jsx    # Indicateurs clés du dashboard
│   │   └── WaterLevelChart.jsx  # Graphique niveaux + prédictions IA
│   ├── data/
│   │   └── mockData.js          # Données simulées (capteurs, alertes)
│   ├── App.jsx                  # Composant principal
│   ├── App.css                  # Styles des composants
│   ├── index.css                # Styles globaux
│   └── main.jsx                 # Point d'entrée React
├── index.html
└── package.json
```

---

*Projet Challenge Innovation — Institut 2iE — 2025-2026*
