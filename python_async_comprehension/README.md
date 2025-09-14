# Python Async Comprehension

## Description
Ce projet a pour objectif de vous initier à l'utilisation des générateurs asynchrones et des compréhensions asynchrones en Python. Vous apprendrez à créer des fonctions asynchrones, à utiliser des générateurs pour produire des données de manière asynchrone, et à mesurer les performances des tâches asynchrones.

---

## Table des matières
- [Description](#description)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Fonctionnalités](#fonctionnalités)
- [Fichiers](#fichiers)
- [Exécution](#exécution)
- [Auteur](#auteur)

---

## Prérequis
Avant de commencer, assurez-vous d'avoir les outils suivants installés :
- **Python 3.10** ou une version supérieure
- **pip** pour installer les dépendances Python
- Un éditeur de texte tel que **Visual Studio Code**

---

## Installation
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/<votre-utilisateur>/holbertonschool-web_back_end.git
   ```
2. Accédez au dossier du projet :
   ```bash
   cd holbertonschool-web_back_end/python_async_comprehension
   ```
3. Installez les dépendances nécessaires (si applicable) :
   ```bash
   pip install -r requirements.txt
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Générateurs asynchrones** : Création de fonctions qui produisent des données de manière asynchrone.
2. **Compréhensions asynchrones** : Utilisation de compréhensions pour collecter des données produites par des générateurs asynchrones.
3. **Mesure des performances** : Calcul du temps d'exécution des tâches asynchrones.

---

## Fichiers
Voici une description des fichiers principaux du projet :

| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-async_generator.py`         | Implémente un générateur asynchrone qui produit des nombres aléatoires.     |
| `1-async_comprehension.py`     | Utilise une compréhension asynchrone pour collecter les données du générateur. |
| `2-measure_runtime.py`         | Mesure le temps d'exécution de plusieurs appels à une fonction asynchrone.  |

---

## Exécution
### **Exécuter un fichier Python**
Pour exécuter un fichier Python, utilisez la commande suivante :
```bash
python3 <nom-du-script>.py
```

Exemple :
```bash
python3 0-main.py
```

### **Description des scripts**
1. **`0-async_generator.py`** :
   - Produit 10 nombres aléatoires entre 0 et 10 avec un délai d'une seconde entre chaque.
2. **`1-async_comprehension.py`** :
   - Collecte les 10 nombres produits par le générateur asynchrone en utilisant une compréhension asynchrone.
3. **`2-measure_runtime.py`** :
   - Exécute la fonction de compréhension asynchrone 4 fois en parallèle et mesure le temps total d'exécution.

---

## Auteur
Lucas Boyadjian

---
