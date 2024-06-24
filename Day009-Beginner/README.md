# `Day 9 - Beginner`

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
