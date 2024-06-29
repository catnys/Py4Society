# `Day17 - Intermediate`

## Summarizing the OOP Concept
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which are instances of classes. These objects can have data (attributes) and associated functionality (methods). OOP allows for logical grouping of data and functions and facilitates code reusability through inheritance.

## Key Features of OOP
- **Encapsulation**: Encapsulation is the mechanism of hiding the internal details of an object and exposing only what is necessary. This can be achieved using private, protected, and public modifiers.
- **Inheritance**: Inheritance is a way to form new classes using classes that have already been defined. It helps in code reuse and establishes a relationship between the new and existing classes.
- **Polymorphism**: Polymorphism allows methods to do different things based on the object it is acting upon. This can be achieved through method overriding and overloading.

## Python Classes and the `__init__` Constructor
In Python, classes are created using the `class` keyword. The `__init__` method in Python is equivalent to a constructor in other object-oriented languages. It is called when an object is created and allows the class to initialize the attributes of the object.

### Example Class with `__init__`

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        
# Creating an object of Car
my_car = Car('Toyota', 'Corolla', 2022)
my_car.display_info()
```

## Conclusion
Understanding OOP in Python can significantly improve the way you design and write your software, making it more organized and manageable.
