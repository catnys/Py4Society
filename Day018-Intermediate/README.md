# `Day 18 Intermediate`

# Turtle Graphics in Python

## Introduction
The Turtle module in Python is a popular way to introduce programming to beginners. It provides a simple drawing environment where users can command a turtle to move around the screen. Commands control the turtle’s movement and drawing, teaching basic programming concepts like loops, conditions, and function calls through visual feedback.

## Getting Started with Turtle
To start using the Turtle module, you need to set up a basic drawing environment. Here's how you can do it:

```python
import turtle

# Create a screen
screen = turtle.Screen()
screen.title('My Turtle Program')

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
```

## Drawing Shapes
You can use commands like `forward()`, `right()`, and `left()` to control the movement of the turtle. Here's an example to draw a square:

```python
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees
```

## Example Program: Drawing a Star
Here's a simple example of how to draw a star using Turtle:

```python
import turtle

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)
    
turtle.done()
```

---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---

# Colorgram.py in Python

## Introduction
`colorgram.py` is a Python library designed to extract colors from images. It simplifies the process of finding the most frequent colors in an image, allowing for creative and analytical applications in fields such as graphic design, digital art, and data visualization.

## Installation
To use `colorgram.py`, you need to install it via pip. Run the following command in your terminal:
```bash
pip install colorgram.py
```

## How It Works
`colorgram.py` extracts color data from images by analyzing the image and identifying the most prevalent colors. The results include not only the RGB values but also information about the proportion of the image that each color occupies.

## Basic Usage
Here’s how you can use `colorgram.py` to extract colors from an image:

```python
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('path_to_image.jpg', 6)

# colors is a list of Color objects, which are 6 colors from the image.
for color in colors:
    rgb = color.rgb  # e.g., (255, 151, 210)
    proportion = color.proportion  # e.g., 0.34
```

## Detailed Example
Let's walk through a detailed example where we extract colors from an image and print their RGB values along with their proportions:

```python
import colorgram

# Extract colors
colors = colorgram.extract('path_to_image.jpg', 4)

# Display the color information
for color in colors:
    print(f"Color RGB: {color.rgb}, Proportion: {color.proportion:.2f}")
```

This script will output the RGB values and proportions of the top 4 colors in the specified image.

## Conclusion
`colorgram.py` offers a powerful way to analyze and utilize color data from images. It is particularly useful for projects requiring color analysis or the generation of color-based data visualizations.


