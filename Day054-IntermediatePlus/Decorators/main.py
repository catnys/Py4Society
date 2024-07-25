def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f'Executing {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} finished execution')
        return result
    return wrapper

@log_execution
def say_hello(name):
    print(f'Hello, {name}')

say_hello('Alice')