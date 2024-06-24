# `Day 10 - Beginner`

# Functions: Outputs, Multiple Return Values, and More

Python functions are powerful tools that facilitate code reusability, readability, and organization. This guide delves into specific aspects of Python functions, particularly focusing on output behaviors, handling multiple return values, and the use of functions with dictionaries.

## Multiple Return Values

In Python, a function can return multiple values using tuples. This feature is incredibly useful for cases where you need to return several results from a single function.

### Example of Multiple Return Values

```python
def get_user_info():
    name = "John Doe"
    age = 30
    city = "New York"
    return name, age, city

user_name, user_age, user_city = get_user_info()
print(user_name, user_age, user_city)
```

## `print` vs `return`

Understanding the difference between `print` and `return` in functions is crucial for writing effective Python code.

- **`print`**: Outputs data to the console. It is generally used for logging or debugging purposes during development.
- **`return`**: Exits the function and optionally passes back an expression to the caller. The returned value can be stored and manipulated further.

### Key Differences

```python
def function_with_print():
    print("This is printed inside the function.")

def function_with_return():
    return "This is returned from the function."

function_with_print()
result = function_with_return()
print("Received:", result)
```

## Combining Dictionaries with Functions

Functions can be designed to manipulate dictionaries, which is useful for managing collections of data efficiently.

### Function to Merge Dictionaries

```python
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict_a = {"name": "Alice", "age": 25}
dict_b = {"job": "Engineer", "city": "Seattle"}

combined_dict = merge_dictionaries(dict_a, dict_b)
print(combined_dict)
```

## Practical Example: Function with Multiple Operations

Combining these concepts, here is a more complex function that utilizes multiple return values, works with dictionaries, and showcases the practical difference between `print` and `return`.

```python
def process_data():
    dict1 = {"x": 1, "y": 2}
    dict2 = {"z": 3, "w": 4}

    # Merging dictionaries
    merged_dict = {**dict1, **dict2}

    # Returning multiple values
    return merged_dict, sum(merged_dict.values())

# Function call
data, total = process_data()
print("Merged Data:", data)
print("Sum of Values:", total)
```
