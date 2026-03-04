# Lecture 9: Classes and Objects. Part 1

Fundamentals of object-oriented programming.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_9_Classes_Objects_Part1/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_9_Classes_Objects_Part1/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_9_Classes_Objects_Part1/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Classes and objects
- Attributes and methods
- Constructor `__init__`
- self

## Basic Class

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, I'm {self.name}"

# Creating an object
user = User("Alice", "alice@example.com")
print(user.greet())
```

## Class Attributes vs Instance Attributes

```python
class Counter:
    count = 0  # Class attribute

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # Instance attribute

c1 = Counter()  # count = 1
c2 = Counter()  # count = 2
print(Counter.count)  # 2
```

## Methods

```python
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self  # For chaining

    def multiply(self, x):
        self.value *= x
        return self

calc = Calculator(10)
calc.add(5).multiply(2)  # 30
```
