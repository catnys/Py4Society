# `Day 19 - Intermediate`

# Passing Functions to Functions in Python

In Python, functions are first-class objects. This means they can be passed around and used as arguments just like any other object (int, str, float, etc.). This feature provides a flexible way to create higher-order functions. These are functions that take other functions as arguments or return them as results.

## Concepts

### First-Class Objects
A first-class object in a programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.

### Higher-Order Functions
A higher-order function is any function that either:
- Takes one or more functions as arguments
- Returns a function as its result

## Example Usage

### Passing a Simple Function

```python
def greet(name):
    return "Hello, " + name

def call_function(f, arg):
    return f(arg)

result = call_function(greet, "Alice")
print(result)  # Output: Hello, Alice
```

### Using the Function as an Argument in Event Listeners

Here's how you can use this concept in event-driven programming with the `turtle` module:

```python
import turtle

def turn_left():
    turtle.left(90)

def on_space_press(fun):
    turtle.onkey(fun, "space")

screen = turtle.Screen()
on_space_press(turn_left)
screen.listen()
screen.mainloop()
```



----

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---


# Turtle Event Listeners

This guide provides a detailed overview of using event listeners in the Turtle graphics library. Event listeners allow you to respond to events such as mouse clicks or key presses, making your Turtle graphics interactive.

## Setup

First, ensure you have Python and Turtle installed. Turtle is usually included with the standard Python installation. You can import Turtle and initialize the screen as follows:

```python
import turtle

screen = turtle.Screen()
```

## Event Listeners

Turtle graphics provide various methods to bind functions to events like key presses or mouse interactions. Below are common event listeners and their usage:

### Key Press

To bind a function to a key press:

```python
def move_up():
    turtle.forward(20)

screen.onkey(move_up, "Up")
screen.listen()
```

### Key Release

To handle a key release:

```python
def stop():
    turtle.penup()

screen.onkeyrelease(stop, "Up")
screen.listen()
```

### Mouse Click

To respond to mouse clicks:

```python
def go_to_click(x, y):
    turtle.goto(x, y)

screen.onclick(go_to_click)
screen.listen()
```

## Finalize

Don't forget to keep the window open and listening:

```python
screen.mainloop()
```

By incorporating these event listeners, you can create interactive Turtle graphics programs that respond dynamically to user inputs.
