def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
example_function(name='John', age=25)
example_function(city='New York', country='USA')

"""
- **kwargs is used to pass a variable number of keyword arguments to a function.
- It allows you to handle named arguments that you have not defined beforehand.
"""