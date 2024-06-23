# `Day 5 - Beginner`
# Loops
## What are For and While Loops?
### For Loop:
A for loop is a programming construct that allows you to repeatedly execute a block of code a specific number of times. It's particularly useful when you know in advance how many times you want to repeat a certain action.

### While Loop:
A while loop, on the other hand, allows you to repeat a block of code as long as a certain condition is true. It's useful when you don't know in advance how many times you need to repeat the code, but you know the condition under which the loop should continue.

## When to Use For and While Loops?
### For Loop:
Use a for loop when you know the number of iterations in advance or when iterating over a sequence (like a list or range).

### While Loop:
Use a while loop when you need to repeat a block of code until a specific condition is met. It's handy when the number of iterations is not known beforehand.

## Syntax/Usage of For and While Loops:

### For Loop Syntax:

python
for variable in iterable:
    # Code to be repeated
variable: Represents the current item in the iteration.
iterable: A sequence of elements (e.g., a list, range, string) over which the loop will iterate.


### While Loop Syntax:

python
while condition:
    # Code to be repeated
condition: A boolean expression that determines whether the loop should continue.

## Best Practices for Using For and While Loops:

### For Loops:

Use for loops when the number of iterations is known.
Ensure that the iterable is appropriate and well-defined.
Be cautious with modifying the iterable inside the loop to avoid unexpected behavior.

### While Loops:

Double-check that the condition will eventually become false to avoid infinite loops.
Be careful when modifying variables inside the loop; ensure progress toward the loop termination condition.
Initialize loop control variables before the loop.

### Example Usage of For and While Loops:
**For Loop Example:**

```python
# Print numbers 0 to 4 using a for loop
for i in range(5):
    print(i)
```

**While Loop Example:**

```python
# Print numbers 0 to 4 using a while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

---

## What is iterator ?
An iterator in Python is an object that allows you to iterate (loop) over a sequence of elements, one at a time, without having to know the underlying details of the sequence's implementation. In simpler terms, an iterator is an object that implements the Python **`iter__()`** and **`next__()`** methods.

- **`iter__()`** method: This method returns the iterator object itself. It is called when the loop is initiated.

- **`next__()`** method: This method returns the next value from the iterator. It is called in each iteration of the loop.

Python provides several built-in objects that are iterable, and you often encounter them in loops. Lists, tuples, dictionaries, sets, strings, and even files are examples of iterable objects in Python. These objects can be used directly in for loops because they have built-in iterators.

Here is a brief example using a list:

```python
my_list = [1, 2, 3, 4, 5]

# Using a for loop with an iterable
for item in my_list:
    print(item)
```
In this example, my_list is an iterable object, and the for loop automatically uses its iterator to loop through each element.

Additionally, the range() function in Python returns an iterable object. When used in a for loop, it automatically generates a sequence of numbers.

```python
# Using a for loop with range
for i in range(5):
    print(i)
```
So, while the term "iterator" might not be explicitly mentioned when using a for loop in Python, the concept is still there. Behind the scenes, these loops utilize iterators provided by iterable objects to traverse their elements. If you need more control over the iteration process, you can also create your own custom iterators in Python by implementing the __iter__() and __next__() methods in a class.





