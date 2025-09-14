# Pagination

## Description
This project aims to teach you how to implement pagination techniques in Python. Pagination is an essential method for managing and displaying large amounts of data efficiently. You will learn how to create functions for simple pagination, hypermedia pagination, and handle specific cases like data deletion.

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
   cd holbertonschool-web_back_end/pagination
   ```
3. Install the required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

---

## Features
This project covers the following concepts:
1. **Simple pagination**: Implementation of a function to divide data into pages.
2. **Hypermedia pagination**: Adding metadata to enrich paginated responses.
3. **Handling deletions**: Managing cases where data is deleted between requests.
4. **Using CSV files**: Reading and manipulating data from a CSV file.

---

## Files
Here is a description of the main files in the project:

| File                              | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `0-simple_helper_function.py`     | Contains a utility function to calculate pagination indices.                |
| `1-simple_pagination.py`          | Implements simple pagination to divide data into pages.                     |
| `2-hypermedia_pagination.py`      | Implements pagination with hypermedia metadata.                             |
| `3-hypermedia_del_pagination.py`  | Handles pagination with data deletion between requests.                     |
| `Popular_Baby_Names.csv`          | CSV file containing data on popular baby names.                             |

---

## Execution
### **Run a Python File**
To execute a Python file, use the following command:
```bash
python3 <file-name>.py
```

Example:
```bash
python3 1-main.py
```

### **Data Used**
The file `Popular_Baby_Names.csv` is used as the data source for pagination examples. Ensure it is present in the folder before running the scripts.

---

## Author
Lucas Boyadjian

---
```