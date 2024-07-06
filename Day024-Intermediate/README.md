# `Day 24 - Intermediate`

# Checking and Handling File Existence in Python

This README demonstrates how to check if a file exists in Python, read its contents if it exists, or create a new file and write to it if it does not exist. Two methods are illustrated: using `os.path.exists()` from the `os` module and `Path` from the `pathlib` module.

## Using `os.path.exists()`

The `os.path.exists()` method from the `os` module checks if a file exists at the specified path.

### Example Code

```python
import os

file_path = 'example.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
else:
    with open(file_path, 'w') as file:
        content = "This is a new file."
        file.write(content)
        print("File created and written to.")
```

### Explanation

1. **Check if the file exists**: `os.path.exists(file_path)` returns `True` if the file exists, `False` otherwise.
2. **Read from the file**: If the file exists, it is opened in read mode (`'r'`), and its contents are printed.
3. **Create and write to the file**: If the file does not exist, it is created and opened in write mode (`'w'`), and a default message is written to it.

## Using `pathlib.Path`

The `Path` class from the `pathlib` module provides an object-oriented approach to handle file paths.

### Example Code

```python
from pathlib import Path

file_path = Path('example.txt')

if file_path.exists():
    with file_path.open('r') as file:
        content = file.read()
        print("File content:")
        print(content)
else:
    with file_path.open('w') as file:
        content = "This is a new file."
        file.write(content)
        print("File created and written to.")
```

### Explanation

1. **Check if the file exists**: `file_path.exists()` returns `True` if the file exists, `False` otherwise.
2. **Read from the file**: If the file exists, it is opened in read mode (`'r'`), and its contents are printed.
3. **Create and write to the file**: If the file does not exist, it is created and opened in write mode (`'w'`), and a default message is written to it.

## To sum up

Both methods are effective for checking the existence of a file, reading from it if it exists, or creating and writing to it if it does not. Choose the method that best fits your programming style or project requirements.
