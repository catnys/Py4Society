# `Day 27 - Intermediate` 

# Python Command-Line Arguments Example

This project demonstrates how to handle command-line arguments in a Python script.

## Usage

Run the script with additional arguments as shown below:

```bash
python script.py arg1 arg2 arg3
```

## Description

The script prints out the name of the script itself, the number of arguments passed, and the list of those arguments.

- `sys.argv[0]`: The script name.
- `sys.argv[1]` to `sys.argv[n]`: The arguments provided.

## Example Script

```python
import sys

print("Script name:", sys.argv[0])
print("Number of arguments:", len(sys.argv) - 1)
print("The arguments are:", sys.argv[1:])
```

## Example Run

Assuming your script is named `script.py` and you pass three arguments:

```bash
python script.py one two three
```

The output will be:

```
Script name: script.py
Number of arguments: 3
The arguments are: ['one', 'two', 'three']
```
