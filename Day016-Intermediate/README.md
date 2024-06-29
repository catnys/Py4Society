# `Day 16 - Intermediate`


# Object-Oriented Programming (OOP) in Python

## Introduction to OOP
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior. OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them.

## Core Concepts of OOP
- **Encapsulation**: This concept is about binding the data (variables) and the methods (functions) together that manipulate the data into a single unit, or class. Encapsulation also helps to hide the internal representation, or state, of an object from the outside.
- **Inheritance**: This is a way to form new classes using classes that have already been defined. These new child classes inherit the attributes and behaviors of the parent class.
- **Polymorphism**: This concept provides a way to use a class exactly like its parent so there is no confusion with mixing types. But each child class keeps its own methods as they are.

## Example: Vehicle Management System
Below is a simple example of using OOP concepts in Python to manage different types of vehicles in a garage:

```python
class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_details(self):
        print(f"Vehicle: {self.name}, Color: {self.color}")

class Car(Vehicle):
    def __init__(self, name, color, horsepower):
        super().__init__(name, color)
        self.horsepower = horsepower

    def show_car_details(self):
        self.show_details()
        print(f"Horsepower: {self.horsepower}")

class Truck(Vehicle):
    def __init__(self, name, color, capacity):
        super().__init__(name, color)
        self.capacity = capacity

    def show_truck_details(self):
        self.show_details()
        print(f"Capacity: {self.capacity} tons")
```

This example demonstrates the basic OOP concepts within Python. Each class represents a type of vehicle with specific attributes and methods. Using inheritance, `Car` and `Truck` classes inherit from `Vehicle` class.
