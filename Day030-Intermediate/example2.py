try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is {result}")
