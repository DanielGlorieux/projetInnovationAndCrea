# Évaluation — Bases de Données Vectorielles

**Cours :** Bases de Données Vectorielles (BDV)  
**Durée :** 1 h 30  
**Documents autorisés :** aucun  
**Barème total :** 20 points

---

## Partie 1 — Prétraitement du texte (6 points)

### Question 1 (2 points)

Écrivez une fonction Python `traiter_fichier(chemin: str) -> str` qui :

1. Lit le contenu d'un fichier TXT en UTF-8.  
2. Remplace toutes les adresses e-mail par la chaîne `MAIL`.  
3. Remplace tous les numéros de téléphone (formats français et international) par la chaîne `TEL`.  
4. Convertit l'intégralité du texte en minuscules.  
5. Supprime les caractères spéciaux, à l'exception des points (`.`).  
6. Supprime les espaces en trop (espaces multiples, tabulations, retours à la ligne).

> **Indication :** Utilisez le module `re` de la bibliothèque standard Python.

---

### Question 2 (1 point)

Donnez le résultat de l'application de votre fonction `traiter_fichier` sur la chaîne suivante :

```
"Contactez Marie à marie@test.fr ou au +33 6 12 34 56 78 !!!"
```

Réponse attendue (format texte brut) :

```
contactez marie à mail ou au tel
```

---

### Question 3 (1 point)

Expliquez pourquoi il est important de **remplacer** les e-mails et téléphones plutôt que de les **supprimer** dans un pipeline RAG (Retrieval-Augmented Generation).

---

### Question 4 (2 points)

Expliquez l'ordre des opérations dans le pipeline de nettoyage.  
Pourquoi faut-il remplacer les e-mails et numéros de téléphone **avant** la suppression des caractères spéciaux ?

---

## Partie 2 — Découpage du texte (chunking) (6 points)

### Question 5 (2 points)

Écrivez une fonction Python `decouper_en_blocs(texte: str, n: int) -> list` qui découpe un texte en blocs de `n` tokens (mots).

Appliquez votre fonction sur le texte suivant avec `n = 3` :

```
"les bases de données vectorielles stockent des embeddings"
```

Donnez la liste de blocs attendue.

---

### Question 6 (2 points)

Écrivez une fonction Python `decouper_par_phrases(texte: str) -> list` qui découpe un texte en phrases individuelles (séparées par `.`, `!` ou `?`).

Appliquez votre fonction sur :

```
"L'IA transforme le monde. Les embeddings sont utiles ! Comprends-tu ?"
```

Donnez la liste de phrases attendue.

---

### Question 7 (2 points)

Modifiez la fonction précédente pour obtenir `decouper_phrases_avec_chevauchement(texte: str, m: int) -> list`, où chaque chunk est préfixé par les `m` derniers mots du chunk précédent.

Appliquez votre fonction sur :

```
"un deux trois. quatre cinq six. sept huit neuf."
```

avec `m = 2`. Donnez la liste de chunks attendue.

---

## Partie 3 — Métriques de similarité (5 points)

### Question 8 (3 points)

Écrivez les trois fonctions Python suivantes **sans utiliser NumPy** :

- `produit_scalaire(v1, v2)` — produit scalaire de deux vecteurs  
- `similarite_cosinus(v1, v2)` — similarité cosinus  
- `distance_euclidienne(v1, v2)` — distance euclidienne (L2)

Appliquez chacune sur `v1 = [1, 2, 3]` et `v2 = [4, 5, 6]` et donnez les résultats numériques.

---

### Question 9 (2 points)

Complétez le tableau suivant en indiquant pour chaque cas d'usage la métrique **la plus adaptée** et justifiez brièvement votre choix.

| Cas d'usage | Métrique recommandée | Justification |
|---|---|---|
| Recherche sémantique dans un corpus de textes | | |
| Clustering de données GPS (coordonnées) | | |
| Système de recommandation collaborative (scores non normalisés) | | |
| Comparaison de documents de longueurs très différentes | | |

---

## Partie 4 — Bases de données vectorielles (3 points)

### Question 10 (1 point)

Définissez ce qu'est un **vecteur d'embedding** et expliquez comment il est généré à partir d'un texte.

---

### Question 11 (1 point)

Citez deux bases de données vectorielles vues en cours et décrivez une différence principale entre elles.

---

### Question 12 (1 point)

Dans le contexte d'un pipeline RAG, expliquez le rôle de la base de données vectorielle lors de la phase de **retrieval** (récupération de contexte).

---

## Barème récapitulatif

| Partie | Points |
|---|---|
| Partie 1 — Prétraitement du texte | 6 |
| Partie 2 — Découpage (chunking) | 6 |
| Partie 3 — Métriques de similarité | 5 |
| Partie 4 — Bases de données vectorielles | 3 |
| **Total** | **20** |
