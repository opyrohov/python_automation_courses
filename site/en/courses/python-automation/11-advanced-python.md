# Lecture 11: Advanced Python

Advanced Python concepts.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_11_Advanced_Python_Concepts/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_11_Advanced_Python_Concepts/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_11_Advanced_Python_Concepts/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Decorators
- Context Managers
- Generators
- Dataclasses

## Decorators

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
```

## Context Managers

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

with timer():
    # code to measure
    pass
```

## Generators

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))
```

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int = 0

user = User("Alice", "alice@example.com", 25)
print(user)  # User(name='Alice', email='alice@example.com', age=25)
```
