# `Day 9 - Beginner`

# Lists 

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
