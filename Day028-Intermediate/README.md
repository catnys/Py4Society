# `Day 28 - Intermediate`


# Tkinter

Tkinter is the standard GUI (Graphical User Interface) library for Python. Python, when combined with Tkinter, provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

## Table of Contents

- [Installation](#installation)
- [Basic Example](#basic-example)
- [Widgets](#widgets)
- [Layouts](#layouts)
- [Events and Bindings](#events-and-bindings)
- [Canvas](#canvas)
- [Menu](#menu)
- [Advanced Features](#advanced-features)
- [RECAP Kwargs and Args](#recap-using-args-and-kwargs-in-python)
- [Using Args](#using-args)
- [Using Kwargs](#using-kwargs)
- [Resources](#resources)

## Installation

Tkinter is included with standard Linux, Microsoft Windows, and macOS installs of Python. No extra installation is necessary. If you need to install it separately, you can do so with the following commands:

### On Linux
```bash
sudo apt-get install python3-tk
```

### On macOS
```bash
brew install python-tk
```

### On Windows
Tkinter is included with the Python installer. Ensure you select it during installation.

## Basic Example

Here's a basic example of a Tkinter application:

```python
import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter App")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
```

## Widgets

Tkinter provides various widgets (controls) for building user interfaces. Some commonly used widgets include:

- **Label:** Displays text or images.
- **Button:** Triggers an action when clicked.
- **Entry:** Allows the user to input a single line of text.
- **Text:** Allows the user to input multiple lines of text.
- **Frame:** A container widget used to organize other widgets.
- **Canvas:** A widget for drawing shapes, graphs, and images.
- **Listbox:** Displays a list of items.
- **Scrollbar:** Adds scrolling capability to other widgets.
- **Combobox:** A dropdown list combined with an entry field.

## Layouts

Tkinter uses geometry managers to control the placement of widgets within a window. The three main geometry managers are:

- **pack:** Packs widgets into a frame.
- **grid:** Organizes widgets in a table-like structure.
- **place:** Places widgets at an absolute position.

### Example using pack:
```python
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.pack(side=tk.LEFT)

label2 = tk.Label(root, text="Label 2")
label2.pack(side=tk.RIGHT)

root.mainloop()
```

### Example using grid:
```python
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

root.mainloop()
```

## Events and Bindings

Tkinter allows you to bind functions to various events, such as key presses or mouse clicks.

### Example:
```python
import tkinter as tk

def on_click(event):
    print("Button clicked")

root = tk.Tk()

button = tk.Button(root, text="Click Me")
button.bind("<Button-1>", on_click)
button.pack()

root.mainloop()
```

## Canvas

The Canvas widget is used for drawing shapes, such as lines, ovals, rectangles, and more.

### Example:
```python
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_line(0, 0, 200, 200)
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

root.mainloop()
```

## Menu

Menus can be added to Tkinter applications to provide dropdown options.

### Example:
```python
import tkinter as tk

def on_new():
    print("New file")

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_new)
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
```

## Advanced Features

Tkinter also supports more advanced features such as dialogs, toplevel windows, and custom widget styling.

### Example of a Dialog:
```python
import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "This is a message box")

root = tk.Tk()

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

root.mainloop()
```

# `RECAP`: Using `*args` and `**kwargs` in Python

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


## Resources

- [Official Python Documentation for Tkinter](https://docs.python.org/3/library/tk.html)
- [Tkinter Wiki](https://wiki.python.org/moin/TkInter)
- [Effbot Tkinterbook](http://effbot.org/tkinterbook/)
- [Python GUI Programming with Tkinter](https://realpython.com/python-gui-tkinter/)

