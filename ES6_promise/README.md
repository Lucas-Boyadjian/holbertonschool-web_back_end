# ES6 Promises

## Description
This project aims to teach you how to use Promises in JavaScript, introduced with ES6. Promises allow you to handle asynchronous operations in a more readable and structured way. You will learn how to create, use, and combine Promises, as well as handle errors in asynchronous flows.

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
   cd holbertonschool-web_back_end/ES6_promise
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

---

## Features
This project covers the following concepts:
1. **Creating Promises** with `new Promise`.
2. **Using `.then()`** to chain operations.
3. **Error handling** with `.catch()`.
4. **Combining Promises** with `Promise.all` and `Promise.race`.
5. **Using `async/await`** to simplify asynchronous code.
6. **Error handling in asynchronous functions**.
7. **Advanced use of Promises** for complex cases.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-promise.js`                 | Creates a simple Promise.                                                   |
| `1-promise.js`                 | A Promise that resolves or rejects based on a condition.                   |
| `2-then.js`                    | Uses `.then()` to chain operations.                                         |
| `3-all.js`                     | Uses `Promise.all` to execute multiple Promises in parallel.                |
| `4-user-promise.js`            | Creates a Promise to simulate a user.                                       |
| `5-photo-reject.js`            | A Promise that rejects with an error.                                       |
| `6-final-user.js`              | Handles multiple Promises with `Promise.allSettled`.                        |
| `7-load_balancer.js`           | Uses `Promise.race` to return the first resolved Promise.                   |
| `8-try.js`                     | Handles errors with `try/catch` in an asynchronous function.                |
| `9-try.js`                     | Advanced use of `try/catch` for error handling.                             |
| `100-await.js`                 | Uses `async/await` to simplify asynchronous code.                           |
| `utils.js`                     | Contains utility functions for Promises.                                    |

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