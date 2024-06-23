# `Day 6 - Beginner`

# Functions in Python

Functions are a key way to define behavior, logic, or algorithms and execute them as needed in Python. Functions help in making code reusable, organized, and more readable.

## Definition of a Function

A function in Python is defined using the `def` keyword, followed by a function name, parentheses, and a colon. The statements inside a function typically perform a task and often return a value.

### Syntax

```python
def function_name(parameters):
    # Function body
    # Return statement (optional)
```

### Example

```python
def greet(name):
    return f"Hello {name}!"
```

## Calling a Function

To execute a function, you call it by its name followed by parentheses enclosing its arguments.

### Example

```python
message = greet("Alice")
print(message)  # Outputs: Hello Alice!
```

## Parameters and Arguments

Parameters are variables listed inside the parentheses in the function definition. Arguments are values passed to these parameters during function calls.

### Types of Parameters

1. **Positional Parameters**: Values are assigned based on the order of parameters.
2. **Keyword Parameters**: Values are assigned to named parameters.
3. **Default Parameters**: Default values are provided to parameters, used if no argument is passed.

### Example

```python
def describe_pet(animal, name="unknown"):
    print(f"I have a {animal} named {name}.")
```

## Return Values

Functions can return values using the `return` statement. A function without a `return` statement returns `None` by default.

### Example

```python
def square(number):
    return number * number
```

## Scope and Lifetime of Variables

Variables defined inside a function have a local scope; they are accessible only within the function and cease to exist once the function execution is completed. Variables defined outside are considered global and can be accessed throughout the module.

---

# `REVISION` : Loops

# Loops in Python

Loops in Python are powerful constructs that allow you to repeat a block of code multiple times. Python supports several types of loops, including `for` and `while` loops, each with its own use cases and syntax.

## 1. `for` Loops

A `for` loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. Iterating over a sequence is called traversal.

### Syntax

```python
for variable in iterable:
    # Code to execute for each item in iterable
```

### Example

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

This will print each fruit in the list `fruits`.

## 2. `while` Loops

A `while` loop in Python performs repetition until a condition becomes false.

### Syntax

```python
while condition:
    # Code to execute as long as condition is true
```

### Example

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

This will print numbers 0 to 2.

## Loop Control Statements

To control the flow of your loops, Python provides several control statements:

- **`break`**: Exits the loop completely.
- **`continue`**: Skips the current iteration and moves to the next iteration.
- **`pass`**: Does nothing; it acts as a placeholder.

### Examples of Control Statements

**Break Example:**

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

**Continue Example:**

```python
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
```

**Pass Example:**

```python
for number in range(10):
    if number % 2 == 0:
        pass  # Do nothing
    else:
        print(number)
```