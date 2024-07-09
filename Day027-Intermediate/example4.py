def example_function(a, b, *args, c=10, **kwargs):
    print(a, b)
    print("Positional arguments:", args)
    print("c:", c)
    print("Keyword arguments:", kwargs)

# Calling the function with different parameters
example_function(1, 2, 3, 4, 5, c=20, d=30, e=40)

# output: 1, 2 Positional arguments: (3, 4, 5) c: 20, Keyword arguments: {'d': 30, 'e': 40}
