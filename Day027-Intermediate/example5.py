def calculate_total(*args, discount=0, **kwargs):
    total = sum(args)
    if discount:
        total -= total * (discount / 100)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return total

# Example usage
print(calculate_total(100, 200, 300, discount=10, tax='Included', shipping='Free'))
