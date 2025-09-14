# NoSQL

## Description
This project aims to introduce you to NoSQL databases, particularly MongoDB. You will learn how to manipulate NoSQL databases, perform CRUD operations (Create, Read, Update, Delete), and execute complex queries. You will also use Python to interact with MongoDB.

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
- **Python 3.x**
- **MongoDB** (version 5.x or higher)
- **pip** to install Python dependencies
- A text editor such as **Visual Studio Code**

---

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
   ```
2. Navigate to the project folder:
   ```bash
   cd holbertonschool-web_back_end/NoSQL
   ```
3. Install the required dependencies:
   ```bash
   pip install pymongo
   ```

---

## Features
This project covers the following concepts:
1. **Creating and using MongoDB databases**.
2. **Inserting documents** into a collection.
3. **Reading documents** with simple and complex filters.
4. **Updating documents** in a collection.
5. **Deleting documents** from a collection.
6. **Executing advanced queries** to analyze data.
7. **Using Python with MongoDB** to automate operations.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-list_databases`             | MongoDB script to list all databases.                                       |
| `1-use_or_create_database`     | MongoDB script to use or create a database.                                 |
| `2-insert`                     | MongoDB script to insert documents into a collection.                       |
| `3-all`                        | MongoDB script to retrieve all documents from a collection.                 |
| `4-match`                      | MongoDB script to retrieve documents matching a filter.                     |
| `5-count`                      | MongoDB script to count the number of documents in a collection.            |
| `6-update`                     | MongoDB script to update documents in a collection.                         |
| `7-delete`                     | MongoDB script to delete documents from a collection.                       |
| `8-all.py`                     | Python script to retrieve all documents from a collection.                  |
| `9-insert_school.py`           | Python script to insert a document into a collection.                       |
| `10-update_topics.py`          | Python script to update topics for a school.                                |
| `11-schools_by_topic.py`       | Python script to retrieve schools matching a specific topic.                |
| `12-log_stats.py`              | Python script to analyze log statistics in a MongoDB database.              |

---

## Execution
### **Run a MongoDB Script**
To execute a MongoDB script, use the following command in the MongoDB shell:
```bash
mongo <script-name>
```

Example:
```bash
mongo 0-list_databases
```

### **Run a Python Script**
To execute a Python script, use the following command:
```bash
python3 <script-name>.py
```

Example:
```bash
python3 8-all.py
```

---

## Author
Lucas Boyadjian

---
```