# Lecture 5: Functions

Functions in Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_5_Functions/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Defining functions
- Parameters and arguments
- Return values
- Scope
- Lambda functions

## Defining a Function

```python
# Basic function
def greet():
    print("Hello!")

greet()  # call

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Parameters and Arguments

```python
# Positional parameters
def add(a, b):
    return a + b

result = add(2, 3)  # 5

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # "Hello, Alice!"
greet("Bob", "Hi")          # "Hi, Bob!"

# Keyword arguments
greet(greeting="Hey", name="Charlie")

# *args (arbitrary number of positional arguments)
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs (arbitrary number of keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")
```

## Return Values

```python
# Single value
def square(x):
    return x ** 2

# Multiple values (tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

# Without return, returns None
def greet(name):
    print(f"Hello, {name}!")  # None
```

## Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

## Scope

```python
# Global vs Local
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)   # can read
    print(local_var)

my_function()
# print(local_var)  # NameError!

# Modifying global
counter = 0

def increment():
    global counter
    counter += 1
```

## Lambda Functions

```python
# Anonymous functions
square = lambda x: x ** 2
add = lambda a, b: a + b

# With sorted/map/filter
numbers = [3, 1, 4, 1, 5]

# Sorting
sorted(numbers, key=lambda x: -x)  # [5, 4, 3, 1, 1]

# Map
squares = list(map(lambda x: x ** 2, numbers))

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## Docstrings

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area of the rectangle

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width
```

## Exercises

::: tip Exercise 1
Write a function to check whether a number is prime.
:::

::: tip Exercise 2
Create a calculator function that takes two numbers and an operation.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/examples)
