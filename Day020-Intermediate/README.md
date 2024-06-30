# `Day 20 - Intermediate`


# Adding Attributes to a Class in Python

In Python, classes are used to define custom objects, and attributes are variables that belong to these objects. You can add attributes to a class in several ways:

## 1. During Class Definition

Attributes can be added directly within the class definition. They are shared among all instances of the class.

```python
class MyClass:
    shared_attribute = 'I am shared by all instances'
```

## 2. Within the `__init__` Method

Attributes specific to each instance are usually added within the `__init__` method.

```python
class MyClass:
    def __init__(self, value):
        self.instance_attribute = value
```

## 3. Dynamically Adding Attributes

Attributes can also be added to instances dynamically after they have been created.

```python
obj = MyClass('Hello')
obj.new_attribute = 'I am new'
```

## 4. Using `setattr()`

The `setattr()` function can be used to set an attribute on an object dynamically.

```python
setattr(obj, 'another_attribute', 'I was set using setattr')
```

## Example

Here's a complete example demonstrating different ways to add attributes:

```python
class Example:
    class_attribute = 'Class Level'

    def __init__(self, value):
        self.instance_attribute = value

# Creating an instance
example = Example('Instance Level')

# Dynamically adding an attribute
example.dynamic_attribute = 'Dynamic Value'

# Using setattr
setattr(example, 'setattr_attribute', 'Set using setattr')

print(example.class_attribute)          # Output: Class Level
print(example.instance_attribute)       # Output: Instance Level
print(example.dynamic_attribute)        # Output: Dynamic Value
print(example.__dict__)                 # Shows all attributes of the instance
```
