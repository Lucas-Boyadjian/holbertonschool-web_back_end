# Python Async Comprehension

## Description
This project aims to introduce you to the use of asynchronous generators and asynchronous comprehensions in Python. You will learn how to create asynchronous functions, use generators to produce data asynchronously, and measure the performance of asynchronous tasks.

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
- **Python 3.10** or higher
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
   cd holbertonschool-web_back_end/python_async_comprehension
   ```
3. Install the required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

---

## Features
This project covers the following concepts:
1. **Asynchronous generators**: Creating functions that produce data asynchronously.
2. **Asynchronous comprehensions**: Using comprehensions to collect data produced by asynchronous generators.
3. **Performance measurement**: Calculating the runtime of asynchronous tasks.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-async_generator.py`         | Implements an asynchronous generator that produces random numbers.          |
| `1-async_comprehension.py`     | Uses an asynchronous comprehension to collect data from the generator.      |
| `2-measure_runtime.py`         | Measures the runtime of multiple calls to an asynchronous function.         |

---

## Execution
### **Run a Python File**
To execute a Python file, use the following command:
```bash
python3 <file-name>.py
```

Example:
```bash
python3 0-main.py
```

### **Description of Scripts**
1. **`0-async_generator.py`**:
   - Produces 10 random numbers between 0 and 10 with a one-second delay between each.
2. **`1-async_comprehension.py`**:
   - Collects the 10 numbers produced by the asynchronous generator using an asynchronous comprehension.
3. **`2-measure_runtime.py`**:
   - Executes the asynchronous comprehension function 4 times in parallel and measures the total runtime.

---

## Author
Lucas Boyadjian

---
```