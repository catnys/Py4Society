# `Day 28 - Intermediate`

# Using `*args` and `**kwargs` in Python

In Python, `*args` and `**kwargs` are used to pass a variable number of arguments to a function. They allow you to handle functions with flexible numbers of input parameters. Here's a detailed explanation of how to use them:

## Using `*args`
`*args` is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of positional arguments to your function.

Example:
```python
def example_function(*args):
    for arg in args:
        print(arg)

# Calling the function with different numbers of arguments
example_function(1, 2, 3)
example_function('a', 'b')
```

## Using `**kwargs`
`**kwargs` is used to pass a variable number of keyword arguments to a function. It allows you to handle named arguments that you have not defined beforehand.

Example:
```python
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
example_function(name='John', age=25)
example_function(city='New York', country='USA')
```

## Combining `*args` and `**kwargs`
You can use both `*args` and `**kwargs` in the same function definition to accept both positional and keyword arguments.

Example:
```python
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function with both positional and keyword arguments
example_function(1, 2, 3, name='John', age=25)
```

## Order of Parameters
When defining a function that uses both `*args` and `**kwargs`, you should follow this order:
1. Standard arguments
2. `*args`
3. Keyword-only arguments (if any)
4. `**kwargs`

Example:
```python
def example_function(a, b, *args, c=10, **kwargs):
    print(a, b)
    print("Positional arguments:", args)
    print("c:", c)
    print("Keyword arguments:", kwargs)

# Calling the function with different parameters
example_function(1, 2, 3, 4, 5, c=20, d=30, e=40)
```

## Practical Example
Here’s a practical example to illustrate the use of `*args` and `**kwargs` in a function that calculates the sum of all positional arguments and then applies a discount based on keyword arguments:

```python
def calculate_total(*args, discount=0, **kwargs):
    total = sum(args)
    if discount:
        total -= total * (discount / 100)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return total

# Example usage
print(calculate_total(100, 200, 300, discount=10, tax='Included', shipping='Free'))
```

This function sums up all positional arguments, applies a discount if provided, and prints any additional keyword arguments.

By using `*args` and `**kwargs`, you can create more flexible and dynamic functions that can handle a variety of input scenarios.
