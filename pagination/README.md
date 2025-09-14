# Pagination

## Description
Ce projet a pour objectif de vous apprendre à implémenter des techniques de pagination en Python. La pagination est une méthode essentielle pour gérer et afficher de grandes quantités de données de manière efficace. Vous apprendrez à créer des fonctions pour la pagination simple, la pagination hypermédia, et à gérer des cas spécifiques comme la suppression de données.

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
- **Python 3.x**
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
   cd holbertonschool-web_back_end/pagination
   ```
3. Installez les dépendances nécessaires (si applicable) :
   ```bash
   pip install -r requirements.txt
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Pagination simple** : Implémentation d'une fonction pour diviser les données en pages.
2. **Pagination hypermédia** : Ajout de métadonnées pour enrichir les réponses paginées.
3. **Gestion des suppressions** : Gestion des cas où des données sont supprimées entre les requêtes.
4. **Utilisation de fichiers CSV** : Lecture et manipulation de données à partir d'un fichier CSV.

---

## Fichiers
Voici une description des fichiers principaux du projet :

| Fichier                              | Description                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| `0-simple_helper_function.py`        | Contient une fonction utilitaire pour calculer les index de pagination.     |
| `1-simple_pagination.py`             | Implémente une pagination simple pour diviser les données en pages.         |
| `2-hypermedia_pagination.py`         | Implémente une pagination avec des métadonnées hypermédia.                  |
| `3-hypermedia_del_pagination.py`     | Gère la pagination avec suppression de données entre les requêtes.          |
| `Popular_Baby_Names.csv`             | Fichier CSV contenant des données sur les prénoms populaires.               |

---

## Exécution
### **Exécuter un fichier Python**
Pour exécuter un fichier Python, utilisez la commande suivante :
```bash
python3 <nom-du-script>.py
```

Exemple :
```bash
python3 1-main.py
```

### **Données utilisées**
Le fichier `Popular_Baby_Names.csv` est utilisé comme source de données pour les exemples de pagination. Assurez-vous qu'il est présent dans le dossier avant d'exécuter les scripts.

---

## Auteur
Lucas Boyadjian

---
