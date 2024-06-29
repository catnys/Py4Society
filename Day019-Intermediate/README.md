# `Day 19 - Intermediate`


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
