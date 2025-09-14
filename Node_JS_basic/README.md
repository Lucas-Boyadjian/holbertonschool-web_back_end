# Node.js Basics

## Description
Ce projet a pour objectif de vous apprendre les bases de Node.js, une plateforme JavaScript côté serveur. Vous découvrirez comment exécuter du JavaScript avec Node.js, utiliser les modules, lire des fichiers, créer des serveurs HTTP simples et complexes, et organiser un serveur Express en plusieurs fichiers.

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
- **Node.js** (version 20.x.x ou supérieure)
- **npm** (version 9.x.x ou supérieure)
- Un éditeur de texte tel que **Visual Studio Code**

---

## Installation
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/<votre-utilisateur>/holbertonschool-web_back_end.git
   ```
2. Accédez au dossier du projet :
   ```bash
   cd holbertonschool-web_back_end/Node_JS_basic
   ```
3. Installez les dépendances nécessaires :
   ```bash
   npm install
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Exécution de JavaScript avec Node.js**.
2. **Utilisation des modules Node.js** pour structurer le code.
3. **Lecture de fichiers** de manière synchrone et asynchrone.
4. **Création de serveurs HTTP** avec le module `http`.
5. **Création de serveurs HTTP avec Express.js** pour simplifier le développement.
6. **Organisation d'un serveur Express** en plusieurs fichiers pour une meilleure maintenabilité.

---

## Fichiers
Voici une description des fichiers principaux du projet :

### **Fichiers principaux**
| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-console.js`                 | Fonction pour afficher un message dans la console.                         |
| `1-stdin.js`                   | Lecture de l'entrée utilisateur via `process.stdin`.                       |
| `2-read_file.js`               | Lecture d'un fichier CSV de manière synchrone.                             |
| `3-read_file_async.js`         | Lecture d'un fichier CSV de manière asynchrone avec Promises.               |
| `4-http.js`                    | Création d'un serveur HTTP simple avec le module `http`.                   |
| `5-http.js`                    | Serveur HTTP avec des routes pour afficher des données CSV.                |
| `6-http_express.js`            | Serveur HTTP simple avec Express.js.                                       |
| `7-http_express.js`            | Serveur HTTP complexe avec Express.js et des routes dynamiques.            |

### **Dossier `full_server/`**
| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `server.js`                    | Point d'entrée du serveur Express.                                         |
| `utils.js`                     | Contient la fonction `readDatabase` pour lire les fichiers CSV.            |
| `controllers/AppController.js` | Contrôleur pour gérer la page d'accueil.                                   |
| `controllers/StudentsController.js` | Contrôleur pour gérer les routes liées aux étudiants.                  |
| `routes/index.js`              | Définit les routes pour le serveur Express.                                |

### **Autres fichiers**
| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `database.csv`                 | Fichier CSV contenant les données des étudiants.                           |
| `test/test.js`                 | Tests pour valider le bon fonctionnement du projet.                        |

---

## Exécution
### **Exécuter un fichier spécifique**
Pour exécuter un fichier spécifique, utilisez la commande suivante :
```bash
node <nom-du-fichier>.js
```

Exemple :
```bash
node 0-console.js
```

### **Lancer le serveur Express**
Pour lancer le serveur Express dans le dossier `full_server/` :
1. Accédez au dossier `Node_JS_basic` :
   ```bash
   cd full_server
   ```
2. Lancez le serveur avec Nodemon :
   ```bash
   npm run dev
   ```
3. Accédez au serveur à l'adresse suivante :
   ```
   http://localhost:1245
   ```

---

## Auteur
Lucas Boyadjian

---