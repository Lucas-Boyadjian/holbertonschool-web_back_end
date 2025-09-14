# Python Async Function Project

## Description
This project is part of the Holberton School curriculum and focuses on asynchronous programming in Python using the `asyncio` library. You will learn how to create and manage coroutines, tasks, and measure execution time using `async/await` syntax. The exercises include launching multiple coroutines, measuring runtime, and working with `asyncio.Task` objects.

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
- Understand the `async/await` syntax in Python.
- Use `asyncio` to run concurrent coroutines.
- Create and manage `asyncio.Task` objects.
- Measure the execution time of asynchronous code.

---

## Requirements
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**.
- All files must end with a new line.
- The first line of all files must be exactly `#!/usr/bin/env python3`.
- All modules, classes, and functions must have documentation.
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
   cd holbertonschool-web_back_end/python_async_function
   ```

---

## Features
This project covers the following concepts:
1. **Basic async syntax**: Learn how to use `async` and `await` to define and run coroutines.
2. **Concurrent coroutines**: Run multiple coroutines concurrently using `asyncio.gather`.
3. **Task management**: Create and manage `asyncio.Task` objects to execute coroutines in the background.
4. **Runtime measurement**: Measure the execution time of asynchronous code.

---

## Files
Here is a description of the main files in the project:

| File                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0-basic_async_syntax.py`      | Implements a basic asynchronous function that waits for a random delay.     |
| `1-concurrent_coroutines.py`   | Runs multiple coroutines concurrently and returns their results.            |
| `2-measure_runtime.py`         | Measures the total runtime of multiple coroutines executed in parallel.     |
| `3-tasks.py`                   | Creates and manages `asyncio.Task` objects to execute coroutines.           |
| `4-tasks.py`                   | Implements advanced task management for asynchronous workflows.             |

---

## Usage
To execute a specific file, use the following command:
```bash
python3 <file-name>.py
```

### Example
Run the `0-main.py` file to test the basic asynchronous function:
```bash
python3 0-main.py
```

### Description of Scripts
1. **`0-basic_async_syntax.py`**:
   - Implements a coroutine that waits for a random delay between 0 and 10 seconds.
2. **`1-concurrent_coroutines.py`**:
   - Runs multiple coroutines concurrently and collects their results.
3. **`2-measure_runtime.py`**:
   - Measures the total runtime of running 4 coroutines in parallel.
4. **`3-tasks.py`**:
   - Creates `asyncio.Task` objects to execute coroutines in the background.
5. **`4-tasks.py`**:
   - Implements advanced task management for complex asynchronous workflows.

---

## Author
Lucas Boyadjian
```