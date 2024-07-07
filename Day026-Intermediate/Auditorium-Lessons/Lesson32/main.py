# eval() converts correctly formatted string to dict
weather_c = eval(input())

# dictionary comprehension
weather_f = {print(day, temp) for (day, temp) in weather_c.items()}

print(weather_f)