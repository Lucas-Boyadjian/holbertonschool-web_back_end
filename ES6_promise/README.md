# ES6 Promises

## Description
Ce projet a pour objectif de vous apprendre à utiliser les Promises en JavaScript, introduites avec ES6. Les Promises permettent de gérer des opérations asynchrones de manière plus lisible et structurée. Vous apprendrez à créer, utiliser et combiner des Promises, ainsi qu'à gérer les erreurs dans des flux asynchrones.

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
   cd holbertonschool-web_back_end/ES6_promise
   ```
3. Installez les dépendances nécessaires :
   ```bash
   npm install
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Création de Promises** avec `new Promise`.
2. **Utilisation de `.then()`** pour chaîner des opérations.
3. **Gestion des erreurs** avec `.catch()`.
4. **Combinaison de Promises** avec `Promise.all` et `Promise.race`.
5. **Utilisation de `async/await`** pour simplifier le code asynchrone.
6. **Gestion des erreurs dans les fonctions asynchrones**.
7. **Utilisation avancée des Promises** pour des cas complexes.

---

## Fichiers
Voici une description des fichiers principaux du projet :

| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-promise.js`                 | Création d'une Promise simple.                                              |
| `1-promise.js`                 | Promise qui se résout ou se rejette en fonction d'une condition.            |
| `2-then.js`                    | Utilisation de `.then()` pour chaîner des opérations.                       |
| `3-all.js`                     | Utilisation de `Promise.all` pour exécuter plusieurs Promises en parallèle. |
| `4-user-promise.js`            | Création d'une Promise pour simuler un utilisateur.                         |
| `5-photo-reject.js`            | Promise qui rejette avec une erreur.                                        |
| `6-final-user.js`              | Gestion de plusieurs Promises avec `Promise.allSettled`.                    |
| `7-load_balancer.js`           | Utilisation de `Promise.race` pour retourner la première Promise résolue.   |
| `8-try.js`                     | Gestion des erreurs avec `try/catch` dans une fonction asynchrone.          |
| `9-try.js`                     | Utilisation avancée de `try/catch` pour gérer les erreurs.                  |
| `100-await.js`                 | Utilisation de `async/await` pour simplifier le code asynchrone.            |
| `utils.js`                     | Contient des fonctions utilitaires pour les Promises.                      |

---

## Exécution
Pour exécuter un fichier spécifique, utilisez la commande suivante :
```bash
node <nom-du-fichier>.js
```

Exemple :
```bash
node 0-main.js
```

---

## Auteur
Lucas Boyadjian

---
