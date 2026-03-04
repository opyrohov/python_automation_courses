# Functions

Functions in Python — definition, parameters, return values, decorators, and anonymous functions.

## Function Definition

```python
# Basic function
def greet(name: str) -> str:
    """Returns a greeting."""
    return f"Hello, {name}!"

result = greet("QA Engineer")
print(result)  # Hello, QA Engineer!

# Function without return
def log_message(message: str) -> None:
    print(f"[LOG] {message}")
```

## Parameters

### Positional and Keyword

```python
def create_user(name: str, age: int, role: str = "Tester") -> dict:
    return {"name": name, "age": age, "role": role}

# Positional arguments
create_user("John", 25)

# Keyword arguments
create_user(name="John", age=25, role="QA Lead")

# Mixed
create_user("John", age=25)
```

### Default Parameters

```python
def run_test(
    url: str,
    browser: str = "chromium",
    headless: bool = True,
    timeout: int = 30000
) -> None:
    print(f"Running on {browser}, headless={headless}")

# Using default values
run_test("https://example.com")

# Overriding specific parameters
run_test("https://example.com", headless=False, timeout=60000)
```

::: warning Mutable Default Values
Never use mutable objects as default parameters:
```python
# WRONG — the list is shared between calls
def add_item(item, items=[]):
    items.append(item)
    return items

# CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```
:::

### *args and **kwargs

```python
# *args — arbitrary number of positional arguments
def sum_all(*args: int) -> int:
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs — arbitrary number of keyword arguments
def create_config(**kwargs) -> dict:
    return {key: value for key, value in kwargs.items()}

config = create_config(browser="firefox", timeout=5000, retries=3)
# {"browser": "firefox", "timeout": 5000, "retries": 3}

# Combining
def setup_test(name: str, *tags: str, **options) -> dict:
    return {
        "name": name,
        "tags": list(tags),
        "options": options
    }

setup_test("login", "smoke", "critical", timeout=30, retries=2)
```

## Return Values

```python
# Returning multiple values (tuple)
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5])

# Early return
def validate_email(email: str) -> bool:
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True
```

## Lambda Functions

```python
# Anonymous functions
square = lambda x: x ** 2
add = lambda a, b: a + b

# Using with sort
users = [
    {"name": "Charlie", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
]

# Sort by age
users.sort(key=lambda u: u["age"])

# Sort by name
users.sort(key=lambda u: u["name"])

# Using with filter and map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
```

## Decorators

```python
import time
from functools import wraps

# Decorator for measuring time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} executed in {duration:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with parameters
def retry(attempts: int = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt}/{attempts} failed: {e}")
                    if attempt == attempts:
                        raise
        return wrapper
    return decorator

@retry(attempts=3)
def unstable_api_call():
    # Calling an unstable API
    pass
```

::: tip Decorators in Testing
```python
import pytest

# pytest markers are essentially decorators
@pytest.mark.smoke
@pytest.mark.parametrize("browser", ["chromium", "firefox"])
def test_login(browser):
    pass

# Custom decorator for test logging
def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"▶ Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✓ Completed: {func.__name__}")
        return result
    return wrapper
```
:::

## Generators

```python
# Generator function with yield
def read_test_data(file_path: str):
    """Reads test data in chunks."""
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

# Usage
for data in read_test_data("test_data.txt"):
    print(data)

# Generator expression
squares = (x**2 for x in range(1000000))  # doesn't consume memory
```

## Useful Links

- [Documentation: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 318 — Decorators](https://peps.python.org/pep-0318/)
- [Real Python: Decorators](https://realpython.com/primer-on-python-decorators/)
