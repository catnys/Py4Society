# `Day 26 - Intermediate`

# List Comprehensions in Python

List comprehensions provide a concise way to create lists in Python. This README will guide you through the basics of using list comprehensions, with examples to help you understand how to use them effectively.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Syntax](#basic-syntax)
3. [Examples](#examples)
    - [Simple List Comprehension](#simple-list-comprehension)
    - [Conditional List Comprehension](#conditional-list-comprehension)
    - [Nested List Comprehension](#nested-list-comprehension)
4. [Conclusion](#conclusion)

## Introduction

List comprehensions offer a shorter syntax when you want to create a new list based on the values of an existing list. It can be used to apply some operation to each item in the list or to filter out certain items from the list.

## Basic Syntax

The basic syntax of a list comprehension is:

```python
[expression for item in iterable]
```

Where:
- `expression` is the current item in the iteration, but it is also the outcome, which can be manipulated as needed.
- `item` is the current item in the iterable (like a list or range).
- `iterable` is the collection you are iterating over.

## Examples

### Simple List Comprehension

Here’s a basic example where we create a list of squares of numbers from 0 to 9:

```python
squares = [x ** 2 for x in range(10)]
print(squares)
```

Output:
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Conditional List Comprehension

You can also add a condition to the list comprehension to filter elements. For example, to get only even numbers:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

Output:
```
[0, 2, 4, 6, 8]
```

### Nested List Comprehension

List comprehensions can be nested to create lists of lists. For example, a multiplication table:

```python
table = [[x * y for y in range(1, 6)] for x in range(1, 6)]
print(table)
```

Output:
```
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
```

## Conclusion

List comprehensions are a powerful tool in Python that can make your code more readable and efficient. By mastering the basic syntax and exploring different examples, you can leverage list comprehensions to write cleaner and more Pythonic code.

For more detailed information, refer to the [official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).
