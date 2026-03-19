# EXAMEN DE CONTRÔLE DES CONNAISSANCES
## BASES DE DONNÉES VECTORIELLES

**Durée :** 2 heures  
**Documents :** Non autorisés  
**Matériel :** Python autorisé (bibliothèques standard uniquement)

---

## PARTIE 1 : QUESTIONS DE COURS (8 points)

### Question 1 (2 points)
Expliquez le principe de la recherche vectorielle et en quoi elle diffère de la recherche traditionnelle par mots-clés dans les bases de données relationnelles.

### Question 2 (2 points)
Décrivez les 4 étapes principales du processus de recherche vectorielle, de la transformation des données jusqu'à l'affichage des résultats.

### Question 3 (2 points)
Qu'est-ce que l'indexation ANN (Approximate Nearest Neighbors) ? Citez et expliquez brièvement deux algorithmes d'indexation utilisés dans les bases de données vectorielles.

### Question 4 (2 points)
Expliquez le "trilemme de la performance" dans les bases de données vectorielles. Quels sont les trois facteurs en jeu et pourquoi est-il difficile d'optimiser les trois simultanément ?

---

## PARTIE 2 : EXERCICES PRATIQUES (12 points)

### EXERCICE 1 : Prétraitement de données (3 points)

Écrivez une fonction Python `nettoyer_texte(fichier_txt)` qui permet de :
- Lire des données issues d'un fichier au format TXT
- Remplacer les adresses mails par « MAIL » et les numéros de téléphone par « TEL »
- Supprimer les espaces en trop et les caractères spéciaux (sauf les points)
- Passer toutes les données en minuscules
- Retourner le texte nettoyé

**Exemple d'entrée :**
```
Contactez Jean Dupont au 06.12.34.56.78 ou par email : jean.dupont@example.com    pour plus d'informations!!!
Mon numéro est le +33 6 12 34 56 78.
```

**Exemple de sortie attendue :**
```
contactez jean dupont au tel ou par email mail pour plus dinformations. mon numero est le tel.
```

---

### EXERCICE 2 : Découpage de texte (Chunking) (4 points)

#### 2.1 Découpage par blocs (1.5 points)
Écrivez une fonction Python `decouper_blocs(texte, n)` qui découpe un texte en blocs de `n` tokens (mots).

**Exemple :**
```python
texte = "Les bases de données vectorielles sont utilisées pour la recherche sémantique"
blocs = decouper_blocs(texte, 3)
# Résultat attendu : 
# ["Les bases de", "données vectorielles sont", "utilisées pour la", "recherche sémantique"]
```

#### 2.2 Découpage par phrases (1 point)
Écrivez une fonction Python `decouper_phrases(texte)` qui découpe un texte en phrases.

**Exemple :**
```python
texte = "ChromaDB est gratuit. Il fonctionne sur disque. Idéal pour la formation."
phrases = decouper_phrases(texte)
# Résultat attendu : 
# ["ChromaDB est gratuit", "Il fonctionne sur disque", "Idéal pour la formation"]
```

#### 2.3 Découpage avec chevauchement (1.5 points)
Ajoutez à la fonction `decouper_blocs` un paramètre de chevauchement `m` qui permet de créer un overlap de `m` mots entre les blocs consécutifs.

**Exemple :**
```python
texte = "Les bases de données vectorielles sont utilisées pour la recherche sémantique"
blocs = decouper_blocs_avec_overlap(texte, n=4, m=2)
# Résultat attendu : 
# ["Les bases de données", 
#  "de données vectorielles sont", 
#  "vectorielles sont utilisées pour",
#  "utilisées pour la recherche",
#  "la recherche sémantique"]
```

---

### EXERCICE 3 : Métriques de similarité (5 points)

#### 3.1 Implémentation (3 points)
Écrivez trois fonctions Python simples (sans utiliser de bibliothèques externes comme numpy) pour calculer :

a) **Le produit scalaire** `produit_scalaire(v1, v2)`  
b) **La similarité cosinus** `similarite_cosinus(v1, v2)`  
c) **La distance euclidienne** `distance_euclidienne(v1, v2)`

**Rappels mathématiques :**
- Produit scalaire : `v1 · v2 = Σ(v1[i] * v2[i])`
- Similarité cosinus : `cos(θ) = (v1 · v2) / (||v1|| * ||v2||)`
- Distance euclidienne : `d = √(Σ(v1[i] - v2[i])²)`

**Exemple de test :**
```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(produit_scalaire(v1, v2))      # Résultat : 32
print(similarite_cosinus(v1, v2))    # Résultat : ~0.9746
print(distance_euclidienne(v1, v2))  # Résultat : ~5.196
```

#### 3.2 Question théorique (2 points)
Pour chacune des trois métriques ci-dessus, expliquez dans quel type de recherche elle est la plus adaptée et pourquoi. Donnez un exemple concret d'utilisation pour chaque métrique.

---

## PARTIE 3 : CAS PRATIQUE (Bonus : 2 points)

### Sécurité et anonymisation

Soit la phrase suivante contenant des données personnelles :

```
"Le client Marc Traoré, né le 15/03/1985, ayant comme email marc.traore@gmail.com et numéro +226 70 12 34 56 a réservé le vol AF456."
```

**Question :**
En vous basant sur vos connaissances du cours et l'exercice 1, écrivez une fonction Python `anonymiser_donnees(texte)` qui anonymise cette phrase en :
- Remplaçant les noms propres par "CLIENT"
- Remplaçant les emails par "MAIL"
- Remplaçant les numéros de téléphone par "TEL"
- Remplaçant les dates au format JJ/MM/AAAA par "DATE"

**Résultat attendu :**
```
"Le client CLIENT, né le DATE, ayant comme email MAIL et numéro TEL a réservé le vol AF456."
```

---

## BARÈME RÉCAPITULATIF

| Partie | Points |
|--------|--------|
| Partie 1 : Questions de cours | 8 |
| Exercice 1 : Prétraitement | 3 |
| Exercice 2 : Chunking | 4 |
| Exercice 3 : Métriques | 5 |
| **Total** | **20** |
| Bonus | +2 |

---

**Bon courage !**
