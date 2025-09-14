# NoSQL

## Description
Ce projet a pour objectif de vous initier aux bases de données NoSQL, en particulier MongoDB. Vous apprendrez à manipuler des bases de données NoSQL, à effectuer des opérations CRUD (Create, Read, Update, Delete), et à exécuter des requêtes complexes. Vous utiliserez également Python pour interagir avec MongoDB.

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
- **MongoDB** (version 5.x ou supérieure)
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
   cd holbertonschool-web_back_end/NoSQL
   ```
3. Installez les dépendances nécessaires :
   ```bash
   pip install pymongo
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Création et utilisation de bases de données MongoDB**.
2. **Insertion de documents** dans une collection.
3. **Lecture de documents** avec des filtres simples et complexes.
4. **Mise à jour de documents** dans une collection.
5. **Suppression de documents** dans une collection.
6. **Exécution de requêtes avancées** pour analyser les données.
7. **Utilisation de Python avec MongoDB** pour automatiser les opérations.

---

## Fichiers
Voici une description des fichiers principaux du projet :

| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-list_databases`             | Script MongoDB pour lister toutes les bases de données.                     |
| `1-use_or_create_database`     | Script MongoDB pour utiliser ou créer une base de données.                  |
| `2-insert`                     | Script MongoDB pour insérer des documents dans une collection.              |
| `3-all`                        | Script MongoDB pour récupérer tous les documents d'une collection.          |
| `4-match`                      | Script MongoDB pour récupérer des documents correspondant à un filtre.      |
| `5-count`                      | Script MongoDB pour compter le nombre de documents dans une collection.     |
| `6-update`                     | Script MongoDB pour mettre à jour des documents dans une collection.        |
| `7-delete`                     | Script MongoDB pour supprimer des documents dans une collection.            |
| `8-all.py`                     | Script Python pour récupérer tous les documents d'une collection.           |
| `9-insert_school.py`           | Script Python pour insérer un document dans une collection.                 |
| `10-update_topics.py`          | Script Python pour mettre à jour les sujets d'une école.                   |
| `11-schools_by_topic.py`       | Script Python pour récupérer les écoles correspondant à un sujet donné.     |
| `12-log_stats.py`              | Script Python pour analyser les statistiques des logs dans une base MongoDB.|

---

## Exécution
### **Exécuter un script MongoDB**
Pour exécuter un script MongoDB, utilisez la commande suivante dans le shell MongoDB :
```bash
mongo <nom-du-script>
```

Exemple :
```bash
mongo 0-list_databases
```

### **Exécuter un script Python**
Pour exécuter un script Python, utilisez la commande suivante :
```bash
python3 <nom-du-script>.py
```

Exemple :
```bash
python3 8-all.py
```

---

## Auteur
Lucas Boyadjian

---