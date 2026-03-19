# CORRIGÉ - EXAMEN DE CONTRÔLE DES CONNAISSANCES
## BASES DE DONNÉES VECTORIELLES

---

## PARTIE 1 : QUESTIONS DE COURS (8 points)

### Question 1 (2 points)
**Réponse :**
La recherche vectorielle change de paradigme en recherchant le **sens** plutôt que des mots-clés exacts. Dans une base de données relationnelle traditionnelle, on cherche des correspondances exactes (ex: "animaux de compagnie" nécessite de définir la catégorie et d'écrire une requête SQL spécifique). Avec la recherche vectorielle, les données sont transformées en vecteurs numériques (embeddings) dans un espace multidimensionnel, ce qui permet de trouver des résultats similaires sémantiquement (ex: "animaux domestiques" trouvera aussi "chien", "chat" sans requête exacte).

### Question 2 (2 points)
**Réponse - Les 4 étapes :**
1. **L'Embedding** : Transformation des données en vecteurs numériques dans un espace vectoriel à n dimensions (n ≥ 300)
2. **Calcul des métriques de similarité** : Mesure de la proximité entre vecteurs via produit scalaire, similarité cosinus ou distance euclidienne
3. **Indexation ANN** : Utilisation d'algorithmes (HNSW, IVF) pour rechercher efficacement les vecteurs similaires
4. **Affichage des résultats** : Retour des k résultats les plus proches avec leurs données associées

### Question 3 (2 points)
**Réponse :**
L'indexation ANN (Approximate Nearest Neighbors) utilise des algorithmes pour rechercher rapidement les vecteurs les plus similaires sans parcourir toute la base.

Deux algorithmes :
- **HNSW (Hierarchical Navigable Small World)** : Recherche à travers un réseau de chemins hiérarchiques, comme un graphe navigable
- **IVF (Inverted File Index)** : Divise l'espace vectoriel en zones (clusters) et ne cherche que dans la zone où se trouve la requête

### Question 4 (2 points)
**Réponse :**
Le trilemme de la performance implique trois facteurs :
1. **Vitesse des requêtes**
2. **Pertinence des résultats**
3. **Utilisation de la mémoire**

Améliorer l'un dégrade les deux autres. Ex: augmenter les paramètres HNSW (ef, M) améliore la pertinence mais réduit la vitesse et augmente la mémoire utilisée.

---

## PARTIE 2 : EXERCICES PRATIQUES (12 points)

### EXERCICE 1 : Prétraitement de données (3 points)

```python
import re

def nettoyer_texte(fichier_txt):
    # Lire le fichier
    with open(fichier_txt, 'r', encoding='utf-8') as f:
        texte = f.read()
    
    # Remplacer les emails par MAIL
    # Pattern pour email: quelquechose@quelquechose.quelquechose
    texte = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'MAIL', texte)
    
    # Remplacer les numéros de téléphone par TEL
    # Patterns courants: +33 6 12 34 56 78, 06.12.34.56.78, etc.
    texte = re.sub(r'\+?\d{1,3}[\s.-]?\d{1,2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}', 'TEL', texte)
    texte = re.sub(r'\b\d{2}[.\s-]?\d{2}[.\s-]?\d{2}[.\s-]?\d{2}[.\s-]?\d{2}\b', 'TEL', texte)
    
    # Supprimer caractères spéciaux sauf les points
    texte = re.sub(r'[^\w\s.]', '', texte)
    
    # Supprimer espaces multiples
    texte = re.sub(r'\s+', ' ', texte)
    
    # Passer en minuscules
    texte = texte.lower()
    
    # Nettoyer les espaces autour des points
    texte = texte.strip()
    
    return texte
```

---

### EXERCICE 2 : Découpage de texte (4 points)

#### 2.1 Découpage par blocs (1.5 points)

```python
def decouper_blocs(texte, n):
    # Découper le texte en mots
    mots = texte.split()
    
    # Créer des blocs de n mots
    blocs = []
    for i in range(0, len(mots), n):
        bloc = ' '.join(mots[i:i+n])
        blocs.append(bloc)
    
    return blocs
```

#### 2.2 Découpage par phrases (1 point)

```python
def decouper_phrases(texte):
    # Découper par points
    phrases = texte.split('.')
    
    # Nettoyer les espaces et retirer les chaînes vides
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    
    return phrases
```

#### 2.3 Découpage avec chevauchement (1.5 points)

```python
def decouper_blocs_avec_overlap(texte, n, m):
    # Découper le texte en mots
    mots = texte.split()
    
    # Créer des blocs avec chevauchement
    blocs = []
    i = 0
    while i < len(mots):
        bloc = ' '.join(mots[i:i+n])
        blocs.append(bloc)
        # Avancer de (n - m) pour créer un chevauchement de m mots
        i += (n - m)
        
        # Éviter une boucle infinie si m >= n
        if m >= n:
            i += 1
    
    return blocs
```

---

### EXERCICE 3 : Métriques de similarité (5 points)

#### 3.1 Implémentation (3 points)

```python
import math

def produit_scalaire(v1, v2):
    """Calcule le produit scalaire de deux vecteurs"""
    resultat = 0
    for i in range(len(v1)):
        resultat += v1[i] * v2[i]
    return resultat


def similarite_cosinus(v1, v2):
    """Calcule la similarité cosinus entre deux vecteurs"""
    # Produit scalaire
    dot_product = produit_scalaire(v1, v2)
    
    # Norme de v1
    norme_v1 = math.sqrt(sum(x**2 for x in v1))
    
    # Norme de v2
    norme_v2 = math.sqrt(sum(x**2 for x in v2))
    
    # Similarité cosinus
    if norme_v1 == 0 or norme_v2 == 0:
        return 0
    
    return dot_product / (norme_v1 * norme_v2)


def distance_euclidienne(v1, v2):
    """Calcule la distance euclidienne entre deux vecteurs"""
    somme = 0
    for i in range(len(v1)):
        somme += (v1[i] - v2[i]) ** 2
    
    return math.sqrt(somme)
```

#### 3.2 Question théorique (2 points)

**Réponse :**

1. **Produit scalaire** :
   - **Utilisation** : Mesure la direction ET la magnitude des vecteurs
   - **Adapté pour** : Recherche où l'intensité compte (ex: systèmes de recommandation, scoring)
   - **Exemple** : Recommander des produits où le nombre d'achats et la valeur comptent

2. **Similarité cosinus** :
   - **Utilisation** : Mesure uniquement l'angle entre vecteurs (direction), indépendant de la magnitude
   - **Adapté pour** : Recherche sémantique, comparaison de documents de tailles différentes
   - **Exemple** : Comparer des documents textuels (un court tweet vs un long article peuvent être sémantiquement similaires)

3. **Distance euclidienne** :
   - **Utilisation** : Mesure la distance "physique" dans l'espace vectoriel
   - **Adapté pour** : Recherche où les différences absolues comptent
   - **Exemple** : Reconnaissance d'images, classification où chaque dimension a une signification précise et mesurable

---

## PARTIE 3 : CAS PRATIQUE (Bonus : 2 points)

```python
import re

def anonymiser_donnees(texte):
    # Remplacer les dates au format JJ/MM/AAAA
    texte = re.sub(r'\b\d{2}/\d{2}/\d{4}\b', 'DATE', texte)
    
    # Remplacer les emails
    texte = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'MAIL', texte)
    
    # Remplacer les numéros de téléphone
    texte = re.sub(r'\+?\d{1,3}[\s.-]?\d{1,2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}', 'TEL', texte)
    
    # Remplacer les noms propres (motif simple: majuscule suivie de minuscules)
    # Cette méthode simple remplace les mots commençant par une majuscule
    # Une approche plus sophistiquée utiliserait du NER (Named Entity Recognition)
    mots = texte.split()
    mots_anonymises = []
    
    for i, mot in enumerate(mots):
        # Si le mot commence par une majuscule et n'est pas en début de phrase
        if mot[0].isupper() and i > 0 and not mots[i-1].endswith('.'):
            # Vérifier si c'est un prénom/nom (pas "Le", "La", etc.)
            if len(mot) > 2 and mot not in ['Le', 'La', 'Les', 'Un', 'Une', 'Des']:
                mots_anonymises.append('CLIENT')
            else:
                mots_anonymises.append(mot)
        else:
            mots_anonymises.append(mot)
    
    texte = ' '.join(mots_anonymises)
    
    return texte


# Version alternative plus simple et directe pour ce cas précis:
def anonymiser_donnees_v2(texte):
    # Remplacer les dates
    texte = re.sub(r'\b\d{2}/\d{2}/\d{4}\b', 'DATE', texte)
    
    # Remplacer les emails
    texte = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'MAIL', texte)
    
    # Remplacer les téléphones
    texte = re.sub(r'\+?\d{1,3}[\s.-]?\d{1,2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}', 'TEL', texte)
    
    # Remplacer les noms de personnes (pattern: Prénom Nom)
    texte = re.sub(r'\b[A-Z][a-z]+\s+[A-Z][a-zé]+\b', 'CLIENT', texte)
    
    return texte
```

---

**FIN DU CORRIGÉ**
