# `Day 13 - Beginner`

# 🚦 Debugging : Common Issues and Solutions

Debugging is an essential skill for any programmer. Understanding common pitfalls and effective debugging strategies can save you hours of frustration. This guide will walk through several Python code snippets, identify issues, and discuss how to resolve them.

## 1. Describe Problem

### Issue
The loop never reaches the condition to print "You got it" because `range(1, 20)` does not include `20`.

### Solution
Adjust the range to include `20`.

```python
def my_function():
  for i in range(1, 21):  # Change here
    if i == 20:
      print("You got it")
my_function()
```

## 2. Reproduce the Bug

### Issue
The `randint` function call potentially generates an index out of range for `dice_imgs`.

### Solution
Modify the range of `randint` to match the indices of `dice_imgs`.

```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # Change here
print(dice_imgs[dice_num])
```

## 3. Play Computer

### Issue
The condition misses including the year 1994.

### Solution
Adjust the comparison operators to include edge cases.

```python
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:  # Change here
  print("You are a millennial.")
elif year > 1994:
  print("You are a Gen Z.")
```

## 4. Fix the Errors

### Issue
`input` returns a string, which can't be compared with integers directly, and there's an indentation error.

### Solution
Convert `age` to `int` and fix the indentation.

```python
age = int(input("How old are you?"))  # Convert string to integer
if age > 18:
  print(f"You can drive at age {age}.")  # Fix indentation
```

## 5. Print is Your Friend

### Issue
The operator `==` is used instead of `=` which doesn't assign but compares, and it always returns `False`.

### Solution
Correct the assignment operator for `word_per_page`.

```python
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  # Change here
total_words = pages * word_per_page
print(total_words)
```

## 6. Use a Debugger

### Issue
`b_list.append(new_item)` is incorrectly indented, causing it to run only once.

### Solution
Correct the indentation so `append` occurs within the loop.

```python
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)  # Correct indentation
  print(b_list)

mutate([1,2,3,5,8,13])
```

## Conclusion

Effective debugging often involves understanding the common pitfalls of a programming language and logical thinking to track down and fix bugs. The examples provided here are just a starting point to help develop these critical skills.
