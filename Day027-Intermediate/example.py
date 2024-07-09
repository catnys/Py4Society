def example_function(*args):
    for arg in args:
        print(arg)

# Calling the function with different numbers of arguments
example_function(1, 2, 3)
example_function('a', 'b')


"""
- *args is used to pass a variable number of non-keyword arguments to a function. 
- It allows you to pass any number of positional arguments to your function.
"""