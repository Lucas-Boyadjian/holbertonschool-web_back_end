# Python - Variable Annotations

## Description
This project is part of the Holberton School curriculum and focuses on advanced Python concepts, specifically type annotations. You will learn how to use type annotations to specify function signatures and variable types, understand duck typing, and validate your code using `mypy`. The goal is to improve code readability, maintainability, and robustness by leveraging Python's type hinting system.

---

## Table of Contents
- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Features](#features)
- [Files](#files)
- [Usage](#usage)
- [Author](#author)

---

## Learning Objectives
By the end of this project, you will be able to:
- Understand type annotations in Python 3.
- Use type annotations for function signatures and variable types.
- Apply duck typing to write flexible and reusable code.
- Validate your code using `mypy` for static type checking.

---

## Requirements
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**.
- All files must end with a new line.
- The first line of all files must be exactly `#!/usr/bin/env python3`.
- All modules, classes, and functions must include documentation.
- All files must be executable.
- Code must follow **pycodestyle** (version 2.5).

---

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
   ```
2. Navigate to the project folder:
   ```bash
   cd holbertonschool-web_back_end/python_variable_annotations
   ```

---

## Features
This project covers the following concepts:
1. **Type annotations for variables**: Learn how to annotate variables with specific types.
2. **Type annotations for functions**: Specify input and output types for functions.
3. **Duck typing**: Use `typing` tools like `Iterable`, `Sequence`, and `Mapping` to write flexible code.
4. **Static type checking**: Validate your code with `mypy` to catch type-related errors before runtime.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-add.py`                     | Function that adds two floating-point numbers with type annotations.        |
| `1-concat.py`                  | Function that concatenates two strings with type annotations.               |
| `2-floor.py`                   | Function that returns the floor of a floating-point number.                 |
| `3-to_str.py`                  | Function that converts a floating-point number to a string.                 |
| `4-define_variables.py`        | Defines and annotates variables with specific types.                        |
| `5-sum_list.py`                | Function that calculates the sum of a list of floats.                       |
| `6-sum_mixed_list.py`          | Function that calculates the sum of a list containing integers and floats.   |
| `7-to_kv.py`                   | Function that converts a key-value pair into a tuple with specific types.   |
| `8-make_multiplier.py`         | Function that returns a multiplier function with type annotations.          |
| `9-element_length.py`          | Function that returns a list of tuples with elements and their lengths.     |

---

## Usage
### **Run a Python File**
To execute a Python file, use the following command:
```bash
python3 <file-name>.py
```

### **Example**
Run the `0-main.py` file to test the `add` function:
```bash
python3 0-main.py
```

### **Validate Type Annotations**
You can validate the type annotations in your code using `mypy`:
```bash
mypy <file-name>.py
```

Example:
```bash
mypy 0-add.py
```

---

## Author
Lucas Boyadjian
```