# Node.js Basics

## Description
This project aims to teach you the basics of Node.js, a JavaScript runtime built on Chrome's V8 engine. You will learn how to execute JavaScript with Node.js, use modules, read files, create simple and complex HTTP servers, and organize an Express server into multiple files.

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
   cd holbertonschool-web_back_end/Node_JS_basic
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

---

## Features
This project covers the following concepts:
1. **Executing JavaScript with Node.js**.
2. **Using Node.js modules** to structure code.
3. **Reading files** synchronously and asynchronously.
4. **Creating HTTP servers** with the `http` module.
5. **Creating HTTP servers with Express.js** to simplify development.
6. **Organizing an Express server** into multiple files for better maintainability.

---

## Files
Here is a description of the main files in the project:

### **Main Files**
| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-console.js`                 | Function to display a message in the console.                              |
| `1-stdin.js`                   | Reads user input via `process.stdin`.                                       |
| `2-read_file.js`               | Reads a CSV file synchronously.                                            |
| `3-read_file_async.js`         | Reads a CSV file asynchronously using Promises.                            |
| `4-http.js`                    | Creates a simple HTTP server using the `http` module.                      |
| `5-http.js`                    | HTTP server with routes to display CSV data.                               |
| `6-http_express.js`            | Simple HTTP server using Express.js.                                       |
| `7-http_express.js`            | Complex HTTP server using Express.js with dynamic routes.                  |

### **`full_server/` Directory**
| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `server.js`                    | Entry point for the Express server.                                         |
| `utils.js`                     | Contains the `readDatabase` function to read CSV files.                    |
| `controllers/AppController.js` | Controller to handle the homepage.                                          |
| `controllers/StudentsController.js` | Controller to handle student-related routes.                          |
| `routes/index.js`              | Defines routes for the Express server.                                     |

### **Other Files**
| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `database.csv`                 | CSV file containing student data.                                           |
| `test/test.js`                 | Tests to validate the functionality of the project.                         |

---

## Execution
### **Run a Specific File**
To execute a specific file, use the following command:
```bash
node <file-name>.js
```

Example:
```bash
node 0-console.js
```

### **Run the Express Server**
To run the Express server in the `full_server/` directory:
1. Navigate to the `Node_JS_basic` folder:
   ```bash
   cd full_server
   ```
2. Start the server with Nodemon:
   ```bash
   npm run dev
   ```
3. Access the server at the following address:
   ```
   http://localhost:1245
   ```

---

## Author
Lucas Boyadjian

---
```