# `Day 12 - Beginner`
# `REVISION`

# Functions Parameters and Return Types

## Introduction to Functions
In Python, a function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Parameters in Functions
Parameters are the variables listed inside the parentheses in the function definition. They are used to pass values to functions. Here's a simple function that uses a parameter:

```python
def greet(name):
    print(f"Hello, {name}!")
```

In this function, `name` is a parameter through which you can pass a string to the function.

## Return Types in Functions
Functions can return values. Every function in Python has a return type, even if it does not explicitly return a value (in which case it returns `None`). Here's how you can specify a function that returns a value:

```python
def add(a, b):
    return a + b
```

In this example, `add` function takes two parameters `a` and `b`, adds them, and returns the result. The return type is implicitly the type of the value that is returned, in this case, an integer or a float.

## Examples
Here are a few more examples demonstrating different kinds of parameter and return types:

### Function with multiple parameters
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type} and its name is {pet_name}.")
```

### Function returning a dictionary
```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
```

### Function with default parameter values
```python
def describe_city(city_name, country='Italy'):
    """Describe a city and its country."""
    print(f"{city_name} is in {country}.")
```



---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---

# Functions: Returning Multiple Values

This README provides an overview of how Python functions can return multiple values using tuples, including syntax and practical examples.

## Table of Contents
- Overview
- How Multiple Returns Work
- Practical Examples

## Overview
In Python, functions can return multiple values. While it may seem like a function is returning several values at once, it is technically returning a single tuple containing all the values. This allows for flexible and concise code.

## How Multiple Returns Work
When you define a function that seems to return multiple values, Python is actually packing those values into a tuple. Here's a basic example:

```python
def get_dimensions():
    width = 5
    height = 10
    return width, height
```

You can capture these multiple values into separate variables through unpacking:

```python
width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")
```

## Practical Examples

### Returning User Information
This function returns multiple pieces of user information:

```python
def get_user_info():
    name = "Alice"
    age = 30
    email = "alice@example.com"
    return name, age, email

# Unpacking the values
user_name, user_age, user_email = get_user_info()
print(user_name, user_age, user_email)
```

### Calculating Statistics
A function that returns multiple statistics:

```python
def calculate_statistics(data):
    min_val = min(data)
    max_val = max(data)
    average_val = sum(data) / len(data)
    return min_val, max_val, average_val

# Example data
data = [10, 20, 30, 40, 50]
min_value, max_value, average = calculate_statistics(data)
print(f"Min: {min_value}, Max: {max_value}, Average: {average}")
```

---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

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

---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---


# 🌸 Lists 

## Introduction to Python Lists

Python lists are versatile data structures that allow you to store multiple items in a single variable. Lists are ordered, mutable, and can contain items of varying data types, including a mix of integers, strings, and even other lists.

## Implementation of Lists

To implement a list in Python, you can assign items within square brackets `[]`, separated by commas. Here's how you can create and manipulate a list:

### Creating a List

```python
my_list = [1, 2, 3, "hello", True]
```

### Adding Items to a List

```python
my_list.append("new item")
my_list.insert(1, "inserted item")
```

### Removing Items from a List

```python
my_list.remove("hello")  # Removes the first occurrence of "hello"
del my_list[0]  # Removes the item at index 0
```

## Best Practices for Using Lists

1. **Clarity and Simplicity**: Keep list operations straightforward to enhance code readability and maintainability.
2. **List Comprehensions**: Use list comprehensions for more concise and readable code when creating new lists.
3. **Avoiding Index Errors**: Always check the length of the list before accessing it by index to prevent runtime errors.

## Nested Lists in Python

Nested lists are lists that contain other lists. They are useful for creating matrix-like structures, or complex data structures like trees.

### Implementation of Nested Lists

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Accessing Items in Nested Lists

```python
# Accessing the first item of the first nested list
print(nested_list[0][0])
```

## Nested List Examples

### Example 1: Easy

Creating a 2x3 matrix using a nested list.

```python
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
```

### Example 2: Advanced

Creating a 3D list where each element is a 3x3 matrix.

```python
three_d_list = [
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]
print(three_d_list)
```


---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---


# 📚 Dictionaries

## Introduction to Python Dictionaries

Python dictionaries are data structures that store data in key-value pairs. Each key is connected to a value, allowing for efficient data retrieval by key rather than by index, making dictionaries ideal for situations where item lookup and data organization are paramount.

## Implementation of Dictionaries

Dictionaries in Python are created using curly braces `{}` with pairs separated by commas, and each key and value separated by a colon `:`.

### Creating a Dictionary

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
```

### Adding and Updating Entries

```python
my_dict["email"] = "john@example.com"  # Adds a new key-value pair
my_dict["age"] = 31  # Updates the value for the key "age"
```

### Removing Entries

```python
del my_dict["age"]  # Removes the entry with the key "age"
my_dict.pop("city")  # Removes the entry with the key "city" and returns its value
```

## Dictionary Operations Examples

### Example 1: Basic Operations

```python
# Define a dictionary
person = {"name": "Alice", "profession": "Engineer"}

# Access elements
profession = person["profession"]

# Update elements
person["profession"] = "Designer"

# Print updated dictionary
print(person)
```

### Example 2: Iterating Over a Dictionary

```python
# Define a dictionary
data = {"a": 1, "b": 2, "c": 3}

# Iterate over keys and values
for key, value in data.items():
    print(f"Key: {key}, Value: {value}")
```

### Example 3: Dictionary Comprehensions

```python
# Create a dictionary with keys as integers and values as squares of the keys
squares = {x: x*x for x in range(6)}
print(squares)
```

### Example 4: Nested Dictionaries

```python
# Define a nested dictionary
users = {
    "user1": {"name": "Mark", "age": 25},
    "user2": {"name": "Katy", "age": 28}
}

# Access data from the nested dictionary
print(users["user1"]["name"])
```

## Keep-In-Mind Questions

1. **What are dictionaries in Python?**
   - Dictionaries are collections of items that are unordered and indexed by keys.

2. **How do you retrieve a value from a dictionary?**
   - You can retrieve a value from a dictionary by using its key: `dictionary[key]`.

3. **Can a Python dictionary store multiple data types?**
   - Yes, both keys and values in a Python dictionary can be of any data type.

4. **What will happen if you try to access a key that does not exist in the dictionary?**
   - Python will raise a `KeyError` unless you use the `get` method, which returns `None` if the key is not found.

## Differences Between Python Dictionaries and Hash Tables
1. Abstraction Level: Python dictionaries are a high-level abstraction of hash tables. While you interact directly with dictionaries in Python, hash tables are often used behind the scenes to implement dictionaries in many programming languages, including Python.

2. Data Structure Type: In Python, dictionaries are recognized as a built-in data type, while hash tables are generally a concept used in the implementation of dictionaries and other data structures.

3. Usage: Dictionaries in Python are used directly in programs to handle data. In contrast, hash tables are usually more of a theoretical model for how dictionaries could be implemented to ensure maximum efficiency.
