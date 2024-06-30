# `Day 21 - Intermediate`

# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. It promotes code reusability and establishes a relationship between different classes.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Concepts](#basic-concepts)
3. [Types of Inheritance](#types-of-inheritance)
   - [Single Inheritance](#single-inheritance)
   - [Multiple Inheritance](#multiple-inheritance)
   - [Multilevel Inheritance](#multilevel-inheritance)
   - [Hierarchical Inheritance](#hierarchical-inheritance)
   - [Hybrid Inheritance](#hybrid-inheritance)
4. [Using the `super()` Function](#using-the-super-function)
5. [Method Overriding](#method-overriding)
6. [Practical Examples](#practical-examples)
7. [Conclusion](#conclusion)
8. [Introduction to The `super()` Method](#Introduction-to-The-super-Method)
9. [Using `super()`](#using-super)
10. [Calling Parent Methods](#calling-parent-methods)
11. [Using `super().__init__()`](#using-super-init)
12. [Practical Examples](#practical-examples)
13. [Conclusion](#conclusion)

## Introduction

Inheritance allows one class (the child or derived class) to inherit the properties and behaviors (methods) of another class (the parent or base class). This helps in building complex systems by reusing existing code and creating a logical structure.

## Basic Concepts

- **Parent Class**: The class whose properties and methods are inherited.
- **Child Class**: The class that inherits from the parent class.
- **`super()` Function**: A built-in function that returns a temporary object of the superclass, allowing access to its methods.

## Types of Inheritance

### Single Inheritance

A child class inherits from a single parent class.

```python
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
```

### Multiple Inheritance

A child class inherits from more than one parent class.

```python
class Parent1:
    def method1(self):
        print("This is method1 from Parent1.")

class Parent2:
    def method2(self):
        print("This is method2 from Parent2.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method.")
```

### Multilevel Inheritance

A child class becomes a parent class for another child class.

```python
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
```

### Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

```python
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")
```

### Hybrid Inheritance

A combination of two or more types of inheritance.

## Using the `super()` Function

The `super()` function is used to call methods from the parent class.

```python
class Parent:
    def display(self):
        print("Parent display method.")

class Child(Parent):
    def display(self):
        super().display()
        print("Child display method.")
```

## Method Overriding

Method overriding occurs when a child class provides a specific implementation of a method already defined in its parent class.

```python
class Parent:
    def show(self):
        print("Parent show method.")

class Child(Parent):
    def show(self):
        print("Child show method.")
```

## Practical Examples

Here's a practical example of inheritance in Python:

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Using the classes
dog = Dog()
cat = Cat()
dog.sound()  # Outputs: Bark
cat.sound()  # Outputs: Meow
```


# The `super()` Method in Python Inheritance

The `super()` method in Python is a powerful tool in object-oriented programming, specifically in the context of inheritance. It allows you to call methods from a parent class within a child class, facilitating code reuse and the extension of functionality.

## Introduction to The `super()` Method

In Python, `super()` provides a way to call methods from a parent class, ensuring that you can build on top of existing functionality without repeating code. This is particularly useful in cases of multiple inheritance or when modifying the behavior of inherited methods.

## Using `super()`

The `super()` function returns a temporary object of the superclass, allowing you to call its methods. This is particularly helpful for accessing inherited methods that have been overridden in a subclass.

```python
class Parent:
    def display(self):
        print("Parent display method.")

class Child(Parent):
    def display(self):
        super().display()
        print("Child display method.")
```

In this example, `super().display()` calls the `display` method of the `Parent` class from the `Child` class.

## Calling Parent Methods

`super()` is commonly used to call parent methods in a child class, enabling the extension of the parent class’s functionality.

```python
class Parent:
    def greet(self):
        print("Hello from Parent.")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child.")
```

## Using `super().__init__()`

In Python, the `__init__` method is a constructor used to initialize objects. When using inheritance, you might need to call the parent class’s constructor to ensure proper initialization.

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized with name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"Child initialized with name: {self.name} and age: {self.age}")
```

In this example, `super().__init__(name)` calls the `__init__` method of the `Parent` class, ensuring that the `name` attribute is properly initialized.

## Practical Examples

Here's a practical example of using `super()` and `super().__init__()` in Python:

```python
class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal: {self.species}")

    def sound(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name
        print(f"Dog: {self.name}")

    def sound(self):
        super().sound()
        print("Bark")

dog = Dog("Canine", "Rex")
dog.sound()
```

Output:
```
Animal: Canine
Dog: Rex
Some sound
Bark
```

## Conclusion

Inheritance is a powerful feature in Python that enhances code reusability and readability. By understanding the types and principles of inheritance, developers can create more structured and maintainable code.
