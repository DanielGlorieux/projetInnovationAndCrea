# 🚀 Quickstart — RAG Chatbot (Documentation Helper)

Ce projet est un chatbot **RAG** (Retrieval-Augmented Generation) qui utilise **Google Gemini** comme LLM et **Pinecone** comme base de données vectorielle. Les données de documentation LangChain sont déjà ingérées dans l'index Pinecone `proj-rag`.

---

## Prérequis

| Outil   | Version minimale |
|---------|-----------------|
| Python  | 3.11+           |
| Node.js | 18+             |
| npm     | 9+              |

## 1. Cloner le dépôt

```bash
git clone https://github.com/DanielGlorieux/projetInnovationAndCrea.git
cd projetInnovationAndCrea/projetLLMDocumentationHelperDaniel-master
```

## 2. Configurer les variables d'environnement

Copiez le fichier `.env` et ajoutez vos clés API :

```bash
cp .env .env.local   # optionnel, pour garder un backup
```

Éditez `.env` :

```
GOOGLE_API_KEY=votre_clé_google_gemini
PINECONE_API_KEY=votre_clé_pinecone
INDEX_NAME=proj-rag
```

- **GOOGLE_API_KEY** : obtenez-la sur [Google AI Studio](https://makersuite.google.com/app/apikey)
- **PINECONE_API_KEY** : obtenez-la sur [Pinecone Console](https://app.pinecone.io/)

## 3. Installer et lancer le backend (Flask)

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur backend
python app.py
```

Le serveur Flask démarre sur **http://localhost:5000**.

Vous pouvez tester avec :

```bash
curl http://localhost:5000/health
```

Réponse attendue :

```json
{"message":"Daniel_Glorieux_Search_AI API is running","status":"healthy"}
```

## 4. Installer et lancer le frontend (React)

Dans un **deuxième terminal** :

```bash
cd frontend
npm install
npm start
```

Le frontend React démarre sur **http://localhost:3000** et communique automatiquement avec le backend Flask sur le port 5000.

## 5. Utiliser le chatbot

1. Ouvrez **http://localhost:3000** dans votre navigateur.
2. Posez une question dans la zone de texte, par exemple : *"Comment utiliser LangChain avec Python ?"*
3. Le chatbot interroge Pinecone pour retrouver les documents pertinents, puis Gemini génère une réponse enrichie avec les sources.

---

## Architecture

```
projetLLMDocumentationHelperDaniel-master/
├── app.py              # Backend Flask (API REST)
├── consts.py           # Constantes (INDEX_NAME)
├── requirements.txt    # Dépendances Python
├── .env                # Variables d'environnement (non commité)
├── Procfile            # Pour déploiement Heroku/Netlify
├── runtime.txt         # Version Python
└── frontend/           # Frontend React
    ├── package.json
    ├── public/
    └── src/
        ├── App.js      # Composant principal du chatbot
        ├── App.css     # Styles
        ├── index.js    # Point d'entrée React
        └── index.css   # Styles globaux
```

## Endpoints API

| Méthode | URL                  | Description                          |
|---------|----------------------|--------------------------------------|
| GET     | `/health`            | Vérification de santé du serveur     |
| POST    | `/api/chat`          | Envoyer une question au chatbot      |
| GET     | `/api/config-status` | Statut de la configuration           |
| GET     | `/api/user-info`     | Informations utilisateur             |
| GET     | `/api/system-info`   | Informations système                 |
| POST    | `/api/clear-chat`    | Effacer l'historique de conversation |

### Exemple d'appel à `/api/chat`

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "Qu'\''est-ce que LangChain ?", "chat_history": []}'
```

---

## Dépannage

- **Le backend ne démarre pas ?** Vérifiez que les clés API dans `.env` sont correctes.
- **Le frontend ne se connecte pas au backend ?** Vérifiez que Flask tourne bien sur le port 5000.
- **Erreur Pinecone ?** Assurez-vous que l'index `proj-rag` existe dans votre compte Pinecone.
