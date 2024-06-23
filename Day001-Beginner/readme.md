# Day 1 - Beginner
<!-- Table of Contents -->
## Table of Contents

1. [Python Variable Naming Guide](#python-variable-naming-guide)
   1. [What is Python?](#what-is-python)
   2. [Basic Syntax in Python](#basic-syntax-in-python)
      1. [Variables](#variables)
         1. [PEP 8 Naming Conventions](#pep-8-naming-conventions)
         2. [Examples](#examples)
      2. [Why PEP 8?](#why-pep-8)
      3. [Basic Syntax Examples](#basic-syntax-examples)
   3. [Running and Debugging Python Files](#running-and-debugging-python-files)
      1. [How to Run a Python File](#how-to-run-a-python-file)
      2. [Debugging Python Code](#debugging-python-code)
         1. [Print Statements](#print-statements)
         2. [Using pdb (Python Debugger)](#using-pdb-python-debugger)
         3. [Integrated Development Environments (IDEs)](#integrated-development-environments-ides)
         4. [Logging](#logging)
   4. [Adding python3 to system path](#adding-python3-to-system-path)
      1. [For Windows](#for-windows)
         1. [Install Python](#install-python)
         2. [Verify Installation](#verify-installation)
      2. [For macOS and Linux](#for-macos-and-linux)
         1. [Install Python](#install-python-1)
         2. [Check if Python is in PATH](#check-if-python-is-in-path)
         3. [Create a Symbolic Link (Optional)](#create-a-symbolic-link-optional)
         4. [Running Python](#running-python)


--- 

## What is Python?

Python is a powerful, high-level programming language known for its readability, versatility, and ease of use. It supports multiple programming paradigms, making it suitable for a wide range of applications, including web development, data science, artificial intelligence, automation, and more.

## Basic Syntax in Python

### Variables

In Python, variables are essential for storing and representing data. Adhering to consistent naming conventions, especially those outlined in the PEP 8 style guide, contributes to code readability and maintainability.

1. **PEP 8 Naming Conventions:**
   - PEP 8 is the official style guide for Python code. It provides recommendations on how to structure and format your code for better consistency.
   - According to PEP 8:
     - Use lowercase letters with underscores for variable names (snake_case).
     - Avoid using single-character names unless they represent loop indices.
     - Use descriptive and meaningful names that convey the purpose of the variable.
     - Avoid using names that could be easily confused (e.g., 'l' (lowercase letter 'L') and 'O' (uppercase letter 'O') with '1').

2. **Examples:**

```python
   # Good variable names
   user_name = "JohnDoe"
   total_amount = 1000.50
   is_student = False

   # Avoid using generic names
   x = 5  # Less meaningful
   temp = "temperature"  # Lack of specificity
   data = [1, 2, 3]  # Context is unclear

   # Follow PEP 8 recommendations for function and method names
   def calculate_total(items):
       return sum(items)

   # Choose meaningful variable names in complex structures
   for index, value in enumerate(some_list):
       print(f"Item {index + 1}: {value}")
```

## Why PEP 8?
Readability: PEP 8 conventions enhance code readability, making it easier for developers to understand and collaborate on projects.
Consistency: Adopting a common style across projects helps maintain a uniform and professional codebase.
Tool Support: Many Python tools and IDEs support PEP 8, providing automatic formatting and highlighting for adherence to the guidelines.

## Basic Syntax Examples:
```py
# Variable assignment
age = 25
name = "John Doe"
is_student = True

# Mathematical operations
result = 10 + 5
product = 3 * 4

# Conditional statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Looping
for i in range(5):
    print("Iteration", i)

# Functions
def greet(name):
    print("Hello, " + name + "!")

# List
fruits = ['apple', 'banana', 'orange']

# Dictionary
person = {'name': 'Alice', 'age': 30, 'is_student': False}

```
--- 

# Running and Debugging Python Files

## How to Run a Python File

To run a Python file, follow these steps:

1. **Install Python:**
   - Make sure Python is installed on your machine. You can download the latest version from [Python's official website](https://www.python.org/downloads/).

2. **Open a Terminal or Command Prompt:**
   - Navigate to the directory containing your Python file using the `cd` command.

3. **Run the Python File:**
   - Use the following command to execute your Python script:
     ```bash
     python filename.py
     ```
     Replace `filename.py` with the actual name of your Python file.

   - If you're using Python 3, replace `python` with `python3`:
     ```bash
     python3 filename.py
     ```

## Debugging Python Code

Debugging is a crucial part of the development process. Here are some tips for debugging Python code:

1. **Print Statements:**
   - Insert `print` statements in your code to output variable values and trace the flow of your program.

```py
   print("Debugging point 1")
   variable = 42
   print("Variable:", variable)
```
Using pdb (Python Debugger):

Insert the following line at the point where you want to start debugging:
```py
import pdb; pdb.set_trace()
```
Run your Python script, and it will stop at the specified line. You can then inspect variables, step through code, and identify issues.

## Integrated Development Environments (IDEs):

Use an IDE like Visual Studio Code, PyCharm, or Jupyter Notebook, which provides a built-in debugger with features like breakpoints, variable inspection, and step-through execution.

## Logging:

Implement logging in your code using the logging module to capture information about the program's execution.
```py
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debugging message")
```

---
# Adding python3 to system path
To add Python 3 to your system's PATH and run it using the python command, you need to follow these general steps. Keep in mind that the exact steps may vary slightly depending on your operating system (Windows, macOS, or Linux).

## For Windows:
### Install Python:

* Download the latest Python 3 installer from Python's official website.
* During installation, make sure to check the box that says "Add Python 3.x to PATH."

### Verify Installation:

Open a new Command Prompt and type:
```bash
python --version
```
This should display the installed Python version.

---

## For macOS and Linux:
### Install Python:

* Many macOS and Linux systems come with Python pre-installed. However, you might want to install a specific version or update to the latest version.
* Use your package manager or download the installer from Python's official website.

### Check if Python is in PATH:

Open a terminal and type:
```bash
    python3 --version
```
If it displays the installed Python version, you can use python3 instead of python to avoid conflicts with the system's Python 2 version.

### Create a Symbolic Link (Optional):

You can create a symbolic link named python pointing to python3 to use the python command instead. This is optional and depends on your preferences.

```bash
sudo ln -s /usr/bin/python3 /usr/bin/python
```

### Running Python:
After adding Python to the PATH, you can run Python scripts using the python command in the terminal or Command Prompt.

Example:

```bash
    python your_script.py
```

Or, if you've set up a symbolic link:

```bash
    python3 your_script.py
```

Make sure to replace your_script.py with the actual name of your Python script.

Please note that, always be cautious when modifying your system's PATH, especially on Windows. Incorrect changes can lead to system issues. If you encounter problems, consult the documentation for your specific operating system or seek assistance from relevant forums or communities.