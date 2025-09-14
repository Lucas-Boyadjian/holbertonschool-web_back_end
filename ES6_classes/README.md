# ES6 Classes

## Description
Ce projet a pour objectif de vous familiariser avec les classes en JavaScript, introduites avec ECMAScript 6 (ES6). Vous apprendrez à créer des classes, des constructeurs, des méthodes, des propriétés statiques, des sous-classes, et à utiliser des concepts avancés comme l'héritage et le polymorphisme.

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
   cd holbertonschool-web_back_end/ES6_classes
   ```
3. Installez les dépendances nécessaires :
   ```bash
   npm install
   ```

---

## Fonctionnalités
Ce projet couvre les concepts suivants :
1. **Création de classes** avec `class`.
2. **Constructeurs** pour initialiser les objets.
3. **Méthodes d'instance** pour définir des comportements.
4. **Propriétés statiques** pour des valeurs partagées entre toutes les instances.
5. **Héritage** avec `extends` pour créer des sous-classes.
6. **Polymorphisme** pour redéfinir des méthodes dans les sous-classes.
7. **Utilisation des getters et setters** pour accéder et modifier les propriétés.
8. **Gestion des erreurs** avec des classes personnalisées.

---

## Fichiers
Voici une description des fichiers principaux du projet :

| Fichier                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-classroom.js`               | Définition d'une classe `ClassRoom` avec un constructeur simple.            |
| `1-make_classrooms.js`         | Création de plusieurs instances de la classe `ClassRoom`.                   |
| `2-hbtn_course.js`             | Définition d'une classe `HolbertonCourse` avec des propriétés et des validations. |
| `3-currency.js`                | Définition d'une classe `Currency` pour gérer les devises.                  |
| `4-pricing.js`                 | Utilisation de la composition avec les classes `Pricing` et `Currency`.     |
| `5-building.js`                | Définition d'une classe `Building` avec des méthodes abstraites.            |
| `6-sky_high.js`                | Création d'une sous-classe `SkyHighBuilding` qui hérite de `Building`.       |
| `7-airport.js`                 | Définition d'une classe `Airport` avec une méthode `toString`.              |
| `8-hbtn_class.js`              | Définition d'une classe `HolbertonClass` avec des propriétés dynamiques.     |
| `9-hoisting.js`                | Explication du hoisting avec les classes.                                   |
| `10-car.js`                    | Définition d'une classe `Car` avec des propriétés et des méthodes avancées. |

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
