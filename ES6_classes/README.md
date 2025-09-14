# ES6 Classes

## Description
This project aims to familiarize you with classes in JavaScript, introduced with ECMAScript 6 (ES6). You will learn how to create classes, constructors, methods, static properties, subclasses, and use advanced concepts such as inheritance and polymorphism.

---

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Files](#files)
- [Execution](#execution)
- [Author](#author)

---

## Prerequisites
Before starting, make sure you have the following tools installed:
- **Node.js** (version 20.x.x or higher)
- **npm** (version 9.x.x or higher)
- A text editor such as **Visual Studio Code**

---

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
   ```
2. Navigate to the project folder:
   ```bash
   cd holbertonschool-web_back_end/ES6_classes
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

---

## Features
This project covers the following concepts:
1. **Class creation** using `class`.
2. **Constructors** to initialize objects.
3. **Instance methods** to define behaviors.
4. **Static properties** for values shared across all instances.
5. **Inheritance** using `extends` to create subclasses.
6. **Polymorphism** to override methods in subclasses.
7. **Getters and setters** to access and modify properties.
8. **Error handling** with custom classes.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-classroom.js`               | Defines a `ClassRoom` class with a simple constructor.                      |
| `1-make_classrooms.js`         | Creates multiple instances of the `ClassRoom` class.                       |
| `2-hbtn_course.js`             | Defines a `HolbertonCourse` class with properties and validations.          |
| `3-currency.js`                | Defines a `Currency` class to manage currencies.                           |
| `4-pricing.js`                 | Uses composition with `Pricing` and `Currency` classes.                    |
| `5-building.js`                | Defines a `Building` class with abstract methods.                          |
| `6-sky_high.js`                | Creates a `SkyHighBuilding` subclass inheriting from `Building`.           |
| `7-airport.js`                 | Defines an `Airport` class with a `toString` method.                       |
| `8-hbtn_class.js`              | Defines a `HolbertonClass` class with dynamic properties.                  |
| `9-hoisting.js`                | Explains hoisting with classes.                                            |
| `10-car.js`                    | Defines a `Car` class with advanced properties and methods.                |

---

## Execution
To execute a specific file, use the following command:
```bash
node <file-name>.js
```

Example:
```bash
node 0-main.js
```

---

## Author
Lucas Boyadjian

---
```