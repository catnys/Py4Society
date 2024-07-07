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
4. [Basic Syntax](#basic-syntax-of-dictionary-comrehensions)
3. [Examples](#examples-of-dictionary-comprehension)
    - [Simple Dictionary Comprehension](#simple-dictionary-comprehension)
    - [Conditional Dictionary Comprehension](#conditional-dictionary-comprehension)
    - [Nested Dictionary Comprehension](#nested-dictionary-comprehension)
4. [Conclusion](#conclusion)
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


# Python Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries in Python. This README will guide you through the basics of using dictionary comprehensions, with examples to help you understand how to use them effectively.


## Introduction of Dictionary Comprehensions

Dictionary comprehensions offer a shorter syntax when you want to create a new dictionary based on the values of an existing iterable. It can be used to apply some operation to each item in the iterable or to filter out certain items from the iterable.

## Basic Syntax of Dictionary Comrehensions

The basic syntax of a dictionary comprehension is:

```python
{key_expression: value_expression for item in iterable}
```

Where:
- `key_expression` is the expression to determine the key.
- `value_expression` is the expression to determine the value.
- `item` is the current item in the iterable (like a list or range).
- `iterable` is the collection you are iterating over.

## Examples of Dictionary Comprehension

### Simple Dictionary Comprehension

Here’s a basic example where we create a dictionary of squares of numbers from 0 to 9:

```python
squares = {x: x ** 2 for x in range(10)}
print(squares)
```

Output:
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### Conditional Dictionary Comprehension

You can also add a condition to the dictionary comprehension to filter elements. For example, to get only even numbers and their squares:

```python
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)
```

Output:
```
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Nested Dictionary Comprehension

Dictionary comprehensions can be nested to create dictionaries of dictionaries. For example, creating a multiplication table:

```python
multiplication_table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 6)}
print(multiplication_table)
```

Output:
```
{
    1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
    2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
    3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
    4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
    5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
}
```

## Conclusion

Dictionary comprehensions are a powerful tool in Python that can make your code more readable and efficient. By mastering the basic syntax and exploring different examples, you can leverage dictionary comprehensions to write cleaner and more Pythonic code.

For more detailed information, refer to the [official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).


