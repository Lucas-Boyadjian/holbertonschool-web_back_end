# Holberton School - Web Back-End

Ce dépôt contient plusieurs projets liés au développement back-end, couvrant des concepts tels que Node.js, ES6, NoSQL, pagination, et programmation asynchrone en Python.

---

## Table des matières
- Dossiers
  - ES6 Basics
  - ES6 Classes
  - ES6 Data Manipulation
  - ES6 Promises
  - Node.js Basics
  - NoSQL
  - Pagination
  - Python Async Comprehension
  - Python Async Function
- Auteur

---

## Dossiers

### **ES6 Basics**
Ce projet couvre les bases d'ES6, une version moderne de JavaScript. Vous apprendrez à utiliser des fonctionnalités telles que les constantes, les variables à portée de bloc, les fonctions fléchées, les paramètres par défaut, et bien plus.

#### **Structure :**
- **Fichiers principaux :**
  - `0-constants.js` : Utilisation des constantes avec `const`.
  - `1-block-scoped.js` : Variables à portée de bloc avec `let`.
  - `2-arrow.js` : Introduction aux fonctions fléchées.
  - `3-default-parameter.js` : Paramètres par défaut dans les fonctions.
  - `4-rest-parameter.js` : Utilisation de l'opérateur rest (`...`).
  - `5-spread-operator.js` : Utilisation de l'opérateur spread (`...`).
  - `6-string-interpolation.js` : Interpolation de chaînes avec les templates literals.
  - `7-getBudgetObject.js` : Création d'objets modernes.
  - `8-getBudgetCurrentYear.js` : Propriétés dynamiques dans les objets.
  - `9-getFullBudget.js` : Combinaison d'objets.
  - `10-loops.js` : Boucles modernes comme `for...of`.
  - `11-createEmployeesObject.js` : Création d'objets pour représenter des employés.
  - `12-createReportObject.js` : Création d'objets imbriqués pour des rapports.

---

### **ES6 Classes**
Ce projet explore les classes en JavaScript, introduites avec ES6. Vous apprendrez à créer des classes, des constructeurs, des méthodes, des propriétés statiques, et à utiliser l'héritage.

#### **Structure :**
- **Fichiers principaux :**
  - `0-classroom.js` : Classe `ClassRoom` avec un constructeur simple.
  - `1-make_classrooms.js` : Création de plusieurs instances de `ClassRoom`.
  - `2-hbtn_course.js` : Classe `HolbertonCourse` avec des validations.
  - `3-currency.js` : Classe `Currency` pour gérer les devises.
  - `4-pricing.js` : Classe `Pricing` utilisant la composition avec `Currency`.
  - `5-building.js` : Classe abstraite `Building`.
  - `6-sky_high.js` : Sous-classe `SkyHighBuilding` héritant de `Building`.
  - `7-airport.js` : Classe `Airport` avec une méthode `toString`.
  - `8-hbtn_class.js` : Classe `HolbertonClass` avec des propriétés dynamiques.
  - `9-hoisting.js` : Explication du hoisting avec les classes.
  - `10-car.js` : Classe `Car` avec des propriétés avancées.

---

### **ES6 Data Manipulation**
Ce projet se concentre sur la manipulation de données en JavaScript avec ES6. Vous apprendrez à utiliser des tableaux, des objets, des ensembles (`Set`), et des tableaux typés (`TypedArray`).

#### **Structure :**
- **Fichiers principaux :**
  - `0-get_list_students.js` : Liste d'objets représentant des étudiants.
  - `1-get_list_student_ids.js` : Extraction des IDs des étudiants.
  - `2-get_students_by_loc.js` : Filtrage des étudiants par localisation.
  - `3-get_ids_sum.js` : Calcul de la somme des IDs.
  - `4-update_grade_by_city.js` : Mise à jour des notes par ville.
  - `5-typed_arrays.js` : Utilisation des tableaux typés.
  - `6-set.js` : Introduction aux ensembles (`Set`).
  - `7-has_array_values.js` : Vérification des valeurs dans un tableau.
  - `8-clean_set.js` : Nettoyage d'un ensemble.
  - `9-groceries_list.js` : Liste de courses avec un `Map`.
  - `10-update_uniq_items.js` : Mise à jour des valeurs dans un `Map`.

---

### **ES6 Promises**
Ce projet vous initie aux Promises en JavaScript pour gérer les opérations asynchrones.

#### **Structure :**
- **Fichiers principaux :**
  - `0-promise.js` : Création d'une Promise simple.
  - `1-promise.js` : Promise conditionnelle.
  - `2-then.js` : Utilisation de `.then()` pour chaîner des opérations.
  - `3-all.js` : Utilisation de `Promise.all`.
  - `4-user-promise.js` : Promise simulant un utilisateur.
  - `5-photo-reject.js` : Promise qui rejette avec une erreur.
  - `6-final-user.js` : Utilisation de `Promise.allSettled`.
  - `7-load_balancer.js` : Utilisation de `Promise.race`.
  - `8-try.js` : Gestion des erreurs avec `try/catch`.
  - `100-await.js` : Utilisation de `async/await`.

---

### **Node.js Basics**
Ce projet couvre les bases de Node.js, y compris la création de serveurs HTTP et l'utilisation de modules.

#### **Structure :**
- **Fichiers principaux :**
  - `0-console.js` : Affichage dans la console.
  - `1-stdin.js` : Lecture de l'entrée utilisateur.
  - `2-read_file.js` : Lecture synchrone d'un fichier.
  - `3-read_file_async.js` : Lecture asynchrone d'un fichier.
  - `4-http.js` : Serveur HTTP simple.
  - `5-http.js` : Serveur HTTP avec des routes.
  - `6-http_express.js` : Serveur HTTP avec Express.js.
  - `7-http_express.js` : Serveur Express avec des routes dynamiques.

---

### **NoSQL**
Ce projet vous initie aux bases de données NoSQL, en particulier MongoDB.

#### **Structure :**
- **Fichiers principaux :**
  - `0-list_databases` : Lister les bases de données.
  - `1-use_or_create_database` : Utiliser ou créer une base de données.
  - `2-insert` : Insérer des documents.
  - `3-all` : Récupérer tous les documents.
  - `4-match` : Filtrer les documents.
  - `5-count` : Compter les documents.
  - `6-update` : Mettre à jour des documents.
  - `7-delete` : Supprimer des documents.
  - `12-log_stats.py` : Analyser les logs dans MongoDB.

---

### **Pagination**
Ce projet vous apprend à implémenter des techniques de pagination en Python.

#### **Structure :**
- **Fichiers principaux :**
  - `0-simple_helper_function.py` : Calcul des index de pagination.
  - `1-simple_pagination.py` : Pagination simple.
  - `2-hypermedia_pagination.py` : Pagination avec métadonnées hypermédia.
  - `3-hypermedia_del_pagination.py` : Gestion des suppressions dans la pagination.

---

### **Python Async Comprehension**
Ce projet explore les générateurs et compréhensions asynchrones en Python.

#### **Structure :**
- **Fichiers principaux :**
  - `0-async_generator.py` : Générateur asynchrone.
  - `1-async_comprehension.py` : Compréhension asynchrone.
  - `2-measure_runtime.py` : Mesure des performances des tâches asynchrones.

---

### **Python Async Function**
Ce projet couvre les bases des fonctions asynchrones en Python.

#### **Structure :**
- **Fichiers principaux :**
  - `0-basic_async_syntax.py` : Fonction asynchrone simple.
  - `1-concurrent_coroutines.py` : Coroutines concurrentes.
  - `2-measure_runtime.py` : Mesure des performances.
  - `3-tasks.py` : Gestion des tâches avec `asyncio.create_task`.

---

## Auteur
Lucas Boyadjian

---
