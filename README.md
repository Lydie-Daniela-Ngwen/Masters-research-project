# La détection automatique du sarcasme dans les commentaires Reddit et les titres de journaux

## 1. Le sarcasme

Le sarcasme est une forme de langage figuratif dans laquelle le sens exprimé peut être différent du sens réellement visé par le locuteur ou l'auteur. Il repose notamment sur un décalage entre ce qui est dit et ce qui est compris ou intentionné.

La définition du sarcasme ne fait cependant pas l'objet d'un consensus unique dans la littérature. Plusieurs travaux mettent notamment en avant l'existence d'une opposition, d'un décalage ou d'une incongruité entre l'énoncé produit et la situation, l'intention ou le sens attendu.

Ce travail porte sur la **détection automatique du sarcasme en français**, à partir de deux types de données : les commentaires Reddit et leur reddit parent et les titres de journaux accompagnés de leur châpo.

---

# 2. Les données

## 2.1. Collecte des données Reddit

Les données provenant de Reddit ont été collectées à l'aide de l'**API Reddit**, via la bibliothèque Python **PRAW (Python Reddit API Wrapper)**.

Les subreddits sélectionnés sont :

- `r/france`
- `r/AntiTaff`
- `r/paslegorafi`
- `r/politiquefrancaise`


Cependant, des titres de reddits et commentaires ont également été selectionnés à l'aide du marqueur du sarcasme sur reddit "/s", semblable aux hashtag sur tweeter. En outre, certains mots spécifiques, susceptibles d'exprimer le sarcasme ont éagelemt été cherché, notamment de termes tels que  :
- c'est pas comme si
- le pauvre
- bebou
- quelle surprise
- comme par hasard

Pour chaque publication Reddit collectée, les informations récupérées comprennent notamment :

- le titre du Reddit ;
- le commentaire ;
- le nom de l'auteur du commentaire.

Les données Reddit ont ensuite fait l'objet d'une annotation manuelle selon le guide d'annotation présenté dans la section ci-après.

## 2.2. Collecte des données issues de journaux

Le second jeu de données est constitué de contenus provenant de trois sources journalistiques :

- **Le Figaro**
- **Le Monde**
- **Le Gorafi**

La collecte des données s'est déroulée en deux étapes.

Dans un premier temps, un **web scraping** a été réalisé afin d'extraire les URL des pages à partir des différents sites.

Dans un second temps, ces URL ont été parcourues afin d'extraire les informations recherchées dans les pages correspondantes, à savoir :

- le titre de l'article ;
- le chapo de l'article.

La collecte et l'extraction des données ont été réalisées en Python à l'aide des bibliothèques **Requests** et **Beautiful Soup**.

Les données issues des journaux ont ensuite été annotées selon le même guide d'annotation que les données Reddit.

## 2.3. Constitution du jeu de données final

Après l'annotation, les deux jeux de données ont été combinés afin de constituer le jeu de données utilisé pour les expériences de détection automatique du sarcasme.

Afin de ne pas conserver certaines informations permettant d'identifier directement la provenance des données, les colonnes suivantes ont été supprimées avant la combinaison :

- la colonne contenant le **nom de l'auteur du commentaire** dans le jeu de données Reddit ;
- la colonne contenant la **source du journal** dans le jeu de données journalistique.

---

# 3. Guide d'annotation

Le guide d'annotation a été élaboré en s'inspirant notamment des travaux de **Jihen Karoui sur la détection automatique de l'ironie**. Ce choix repose sur les nombreuses similarités observées entre les phénomènes d'ironie et de sarcasme, notamment en ce qui concerne les mécanismes d'opposition et de décalage entre l'énoncé et son interprétation.

L'annotation est **binaire** : l'annotatrice doit déterminer si elle perçoit ou non un sarcasme dans l'énoncé.

Lorsqu'un sarcasme est identifié, l'annotatrice doit également déterminer le type de mécanisme impliqué.

## 3.1. Sarcasme avec opposition

Le sarcasme peut notamment se manifester par une opposition. Celle-ci peut être **explicite** ou **implicite**.

### Opposition explicite

L'opposition explicite peut prendre différentes formes.

#### Opposition de polarité

Elle correspond à une opposition entre deux segments présentant des polarités différentes.

Par exemple :

> « Super, j’ai renversé du café sur mon ordinateur »

On peut identifier ici :

- `[Super] P+`
- `[j’ai renversé du café sur mon ordinateur] P-`

où `P+` et `P-` correspondent respectivement aux polarités positive et négative.

#### Opposition entre des éléments sémantiquement non liés

L'opposition peut également être construite entre deux éléments qui ne sont pas sémantiquement liés.

Par exemple :

> « Ah ouais c’est clair que son ongle cassé c’est quand même la troisième guerre mondiale »

On peut identifier :

- `[son ongle cassé] P1`
- `[la troisième guerre mondiale] P2`

Les deux éléments sont ici mis en relation alors qu'ils renvoient à des situations sans commune mesure.

### Opposition implicite

L'opposition peut également être implicite, notamment lorsqu'elle repose sur un **décalage entre l'énoncé et la situation**.

Par exemple :

> « Comme je suis heureux que le week-end soit déjà fini »

On peut identifier :

- `[Comme je suis heureux] P1`
- `[que le week-end soit déjà fini] Pcont`

Le sarcasme repose ici sur le décalage entre l'expression d'une émotion positive et une situation généralement associée à une émotion négative.

## 3.2. Sarcasme sans opposition

Le sarcasme peut également se manifester sans opposition ou décalage explicite. Plusieurs indices peuvent alors être utilisés pour signaler une prise de distance ou un sens non littéral.

Parmi ces indices figurent notamment :

- la **citation avec prise de distance**, par exemple à l'aide de guillemets ;
- la **fausse affirmation** ;
- l'**hyperbole** ;
- l'utilisation d'**adjectifs ou d'adverbes** marquant une prise de distance ;
- l'**euphémisme** ;
- la **parodie** ;
- les **références culturelles**.

---

# 4. Prétraitement

Avant l'entraînement des modèles, les données ont fait l'objet d'un prétraitement commun.

Les différentes parties textuelles ont d'abord été combinées afin de former une seule séquence textuelle :

- pour les données Reddit : **titre du Reddit + commentaire** ;
- pour les données journalistiques : **titre + chapo**.

Les différentes parties sont séparées par le caractère `|`.

Les URL et les GIF présents dans les données ont été remplacés par des marqueurs spécifiques :

- les URL sont remplacées par `URL` ;
- les GIF sont remplacés par `GIF_TOKEN`.

Les espaces ont également été supprimés selon les étapes de prétraitement appliquées aux données.

Les **marqueurs typographiques ont été conservés**, car ils peuvent constituer des indices permettant de signaler le sarcasme. Il s'agit notamment :

- des majuscules ;
- de la ponctuation ;
- des emojis ;
- et, plus généralement, des marqueurs typographiques présents dans les énoncés.

Ces éléments peuvent en effet participer à l'expression ou à l'interprétation du sarcasme.

---

# 5. Modèles

Plusieurs approches de classification ont été expérimentées afin de comparer différentes méthodes de détection automatique du sarcasme.

## 5.1. Arbre de décision

Un **arbre de décision** a été utilisé comme modèle de référence (*baseline*).

Les données ont été divisées selon une proportion **80:20** entre les données utilisées pour l'entraînement et celles utilisées pour l'évaluation.

## 5.2. SVM

Un modèle **SVM (Support Vector Machine)** a également été utilisé pour la classification.

Les données ont été divisées selon une proportion **80:20** entre l'entraînement et l'évaluation.

## 5.3. LSTM bidirectionnel

Un **LSTM bidirectionnel (BiLSTM)** a ensuite été utilisé afin de prendre en compte les dépendances séquentielles dans les données textuelles.

Le modèle a été enrichi à l'aide des embeddings **ConceptNet Numberbatch**, et plus précisément de la ressource :

`conceptnet-numberbatch-17-06-300`

## 5.4. CamemBERT

Enfin, un modèle **CamemBERT** a été affiné (*fine-tuned*) pour la tâche de classification binaire du sarcasme.

---

# 6. Technologies utilisées

Le projet a été réalisé en Python et s'appuie notamment sur les outils et bibliothèques suivants :

- **Python**
- **Pandas**
- **NumPy**
- **scikit-learn**
- **TensorFlow / Keras**
- **PyTorch**
- **Hugging Face Transformers**
- **Gensim**
- **PRAW**
- **Requests**
- **Beautiful Soup**

---

# 7. Objectif

L'objectif de ce projet est d'étudier la possibilité de détecter automatiquement le sarcasme dans des contenus textuels en français, en comparant plusieurs approches de classification et en étudiant les différents indices linguistiques et contextuels susceptibles de contribuer à son identification.

Le projet s'inscrit notamment dans la continuité des travaux portant sur la détection automatique de l'ironie en français, tout en se concentrant sur le **sarcasme dans les commentaires Reddit et les titres de journaux**.

## 8. Installation

Les dépendances sont séparées selon les modèles utilisés dans le projet.

### CamemBERT
```bash
pip install -r requirements_camembert.txt

```

### LSTM
```bash
pip install -r requirements_lstm.txt
```

### Arbre de décision
```bash
pip install -r requirements_DT.txt
```

### Machine à vecteurs de Support
```bash
pip install -r requirements_SVM.txt
```
