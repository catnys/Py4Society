# Target is the number up to which we count
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0: # use elif (Not if)
    print("Fizz")
  elif number % 5 == 0: # use elif (Not if)
    print("Buzz")
  else:
    print(number) # remove square brackets []
