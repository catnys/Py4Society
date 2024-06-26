# `Day 11 - Beginner`

# Project: `Blackjack Game`

## Overview
This Python-based Blackjack game allows players to compete against a computer dealer. The game adheres to standard Blackjack rules, where the objective is to achieve a score of 21 or as close as possible without going over.

## Features
- Unlimited deck size without jokers.
- Ace values are dynamically counted as 1 or 11.
- Simple command-line interface for easy gameplay.
- Dealer plays automatically with a minimum score rule of 17.

---

# Scopes: Global vs Local

Understanding scopes in Python is crucial for effective programming, especially when it comes to managing variable visibility and lifecycle across different parts of your code. This guide explores the differences between global and local scopes and how they influence variable behavior in Python.

## What is Scope?

**Scope** refers to the region of a program where a variable is accessible. Python supports different types of scopes, including local and global, which determine the visibility and lifetime of a variable.

## Global Scope

Variables declared outside any function belong to the **global scope**. These variables are accessible from any part of the code, including inside functions.

### Example of Global Scope

```python
x = "global"

def access_global():
    print("Inside function:", x)

access_global()
print("In global scope:", x)
```

## Local Scope

Variables declared inside a function belong to the **local scope** of that function. They are only accessible within the function where they are declared.

### Example of Local Scope

```python
def my_function():
    y = "local"
    print("Inside function:", y)

my_function()

# Uncommenting the next line will raise an error because y is not accessible outside the function.
# print("In global scope:", y)
```

## Differences between Global and Local Scope

- **Accessibility**: Global variables can be accessed throughout the program, while local variables can only be accessed within their respective functions.
- **Lifetime**: Global variables live as long as the program runs, whereas local variables are destroyed once the function execution completes.
- **Modification**: Changes to global variables affect their values throughout the entire program. Local variables, however, are independent in their functions.

## Using Global Variables in a Local Scope

You can access and modify global variables inside a local scope using the `global` keyword.

### Example of Modifying Global Variable

```python
z = "initial"

def modify_global():
    global z
    z = "modified"
    print("Inside function:", z)

modify_global()
print("In global scope:", z)
```

## Conclusion

Understanding the distinction between global and local scopes helps prevent bugs related to variable mismanagement and aids in maintaining clean, understandable code. By appropriately leveraging these scopes, developers can optimize data handling and ensure that their programs are both efficient and robust.

---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---


# Python Scoping Rules: Block Scope and Global Variables

Understanding the scoping rules in Python is essential for managing variable visibility and modifying global variables effectively. This guide explores the concept of block scope in Python and details how to modify global variables.

## Does Python Have Block Scope?

In many programming languages, variables declared inside blocks (like loops or conditionals) are scoped to that block. However, Python handles scoping differently.

### Block Scope in Python

Python does not have block scope. Variables declared in a block are accessible outside the block as well. This is a fundamental difference from languages like JavaScript or C++.

#### Example Demonstrating Lack of Block Scope

```python
if True:
    x = 10
print("Outside the block:", x)  # Output will be 10

for i in range(5):
    y = i * 2
print("Outside the loop:", y)  # Output will be 8
```

In the above examples, `x` and `y` are accessible outside the blocks where they were declared, indicating that Python does not restrict their scope to within the blocks.

## Modifying a Global Variable

Global variables in Python are those declared at the top level of a script or module or outside any function. They can be accessed globally, but modifying them inside a function requires special handling.

### How to Modify a Global Variable

To modify a global variable within a function, you must declare the variable as `global` inside the function. This declaration tells Python that you intend to use the global version of the variable, not a local one.

#### Example of Modifying a Global Variable

```python
z = "initial"  # Global variable

def modify_global():
    global z  # Declare that we use the global variable
    z = "modified"  # Modify the global variable
    print("Inside function:", z)

modify_global()
print("Outside function:", z)  # Output will be 'modified'
```

Using the `global` keyword, the function `modify_global` changes the value of `z` globally.

## Conclusion

Python's scoping rules are different from many other languages due to its lack of block scope. Understanding these rules helps in effectively managing and modifying variables, particularly global variables, ensuring your code behaves as expected.
