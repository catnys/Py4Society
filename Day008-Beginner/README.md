# `Day 8 - Beginner`


# `REVISION` : Functions Parameters and Return Types

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
