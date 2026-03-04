# Decorators

Decorators are a powerful Python tool that allows you to modify the behavior of functions and classes without changing their code. In QA automation, decorators are used everywhere: from pytest markers to retry logic and logging.

## Functions as First-Class Objects

In Python, functions are objects. You can assign them to variables, pass them as arguments, and return them from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
say_hello = greet
print(say_hello("QA Engineer"))  # Hello, QA Engineer!

# Passing a function as an argument
def execute(func, value):
    return func(value)

result = execute(greet, "Tester")
print(result)  # Hello, Tester!

# Returning a function from a function
def create_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = create_multiplier(2)
print(double(5))  # 10
```

::: info Why does this matter?
Understanding functions as objects is the foundation for working with decorators. A decorator is a function that takes another function and returns a new function.
:::

## Simple Decorator Pattern

A decorator is a wrapper function that adds behavior to another function.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# Using the @ syntax
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")
# Before function call
# Hello, World!
# After function call
```

::: tip What does @decorator do?
Writing `@my_decorator` before a function is syntactic sugar for:
```python
say_hello = my_decorator(say_hello)
```
:::

## functools.wraps

Without `functools.wraps`, the decorated function loses its name and documentation.

```python
from functools import wraps

# Without wraps — metadata is lost
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """My documentation."""
    pass

print(my_function.__name__)  # wrapper (wrong!)
print(my_function.__doc__)   # None (documentation is gone!)

# With wraps — metadata is preserved
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function():
    """My documentation."""
    pass

print(my_function.__name__)  # my_function (correct!)
print(my_function.__doc__)   # My documentation.
```

::: warning Always use @wraps
Without `@wraps` you lose `__name__`, `__doc__`, and other attributes of the original function. This is especially critical when working with pytest, where the function name is used as the test name.
:::

## Decorators with Arguments

If a decorator needs parameters, add another level of nesting.

```python
from functools import wraps

def repeat(times):
    """Decorator that repeats a function call N times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("QA")
# Hello, QA!
# Hello, QA!
# Hello, QA!
```

::: info Structure of a decorator with arguments
```
repeat(times=3)         → returns decorator
  decorator(func)       → returns wrapper
    wrapper(*args)      → executes the logic
```
So `@repeat(times=3)` first calls `repeat(3)`, which returns the actual decorator.
:::

## Built-in Decorators

### @staticmethod

A method that does not need access to the instance (`self`) or the class (`cls`).

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_positive(number):
        return number > 0

# Call without creating an instance
print(MathUtils.add(2, 3))        # 5
print(MathUtils.is_positive(-1))  # False
```

### @classmethod

A method that receives the class (`cls`) instead of the instance (`self`). Useful for alternative constructors.

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        return cls(name, role="admin")

    @classmethod
    def create_tester(cls, name):
        return cls(name, role="tester")

admin = User.create_admin("Elena")
tester = User.create_tester("Andrew")
print(admin.role)   # admin
print(tester.role)  # tester
```

### @property

Allows accessing a method as an attribute. Convenient for computed values and validation.

```python
class TestResult:
    def __init__(self, passed, failed):
        self._passed = passed
        self._failed = failed

    @property
    def total(self):
        return self._passed + self._failed

    @property
    def pass_rate(self):
        if self.total == 0:
            return 0.0
        return self._passed / self.total * 100

    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        if value < 0:
            raise ValueError("Count cannot be negative")
        self._passed = value

result = TestResult(passed=8, failed=2)
print(result.total)      # 10 (called without parentheses)
print(result.pass_rate)  # 80.0

result.passed = 9        # Using the setter
print(result.pass_rate)  # 90.0

result.passed = -1       # ValueError: Count cannot be negative
```

::: tip When to use @property?
- When you need a computed field (like `total` and `pass_rate`)
- When you need validation on setting a value (setter)
- When you want to make an attribute read-only (no setter)
:::

## Stacking Decorators

Decorators can be combined — they are applied bottom-up.

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(greet("World"))
# <b><i>Hello, World</i></b>
```

::: info Execution order
```python
@bold       # 2. Then bold wraps the result of italic
@italic     # 1. First italic wraps greet
def greet(name):
    ...
```
This is equivalent to: `greet = bold(italic(greet))`
:::

## Class-Based Decorators

A decorator can be a class with a `__call__` method.

```python
from functools import wraps

class CountCalls:
    """Counts the number of times a function is called."""

    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"{self.func.__name__} called {self.call_count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def process_data(data):
    return len(data)

process_data([1, 2, 3])  # process_data called 1 time(s)
process_data([4, 5])      # process_data called 2 time(s)
print(process_data.call_count)  # 2
```

::: tip When to use a class-based decorator?
- When the decorator needs to maintain state between calls (counter, cache)
- When the decorator logic is complex and requires multiple methods
- When you want to use decorator inheritance
:::

## QA Automation Examples

### Retry Decorator

Retries test execution on failure — essential for flaky tests.

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Retries a function call when an error occurs."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2, exceptions=(TimeoutError, ConnectionError))
def fetch_api_data(url):
    """Fetches data from an API with retry logic."""
    import requests
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

### Timer Decorator

Measures function execution time — useful for monitoring test performance.

```python
import time
from functools import wraps

def timer(func):
    """Measures function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} executed in {elapsed:.4f} sec")
        return result
    return wrapper

@timer
def run_heavy_test():
    """A test that takes a long time."""
    time.sleep(2)
    assert True

run_heavy_test()
# [TIMER] run_heavy_test executed in 2.0012 sec
```

### Logging Decorator

Automatically logs function calls — helps with debugging tests.

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_call(func):
    """Logs function calls with arguments and return values."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"Calling {func.__name__}({signature})")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} returned {result!r}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} raised error: {e}")
            raise
    return wrapper

@log_call
def login(username, password):
    """Authenticates a user."""
    if username == "admin" and password == "secret":
        return {"status": "success", "token": "abc123"}
    raise ValueError("Invalid credentials")

login("admin", "secret")
# INFO: Calling login('admin', 'secret')
# INFO: login returned {'status': 'success', 'token': 'abc123'}
```

### Pytest Markers as Decorators

Pytest extensively uses decorators for marking and parameterizing tests.

```python
import pytest

# Marker to skip a test
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

# Marker for expected failure
@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug():
    assert 1 + 1 == 3

# Parameterization — one test with different data
@pytest.mark.parametrize("username, password, expected", [
    ("admin", "admin123", True),
    ("user", "wrong", False),
    ("", "", False),
])
def test_login(username, password, expected):
    result = authenticate(username, password)
    assert result == expected

# Combining markers
@pytest.mark.smoke
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_homepage(browser):
    """Smoke test for homepage in different browsers."""
    pass

# Fixtures are decorators too
@pytest.fixture
def auth_token():
    """Gets an auth token before the test."""
    token = get_auth_token("admin", "secret")
    yield token
    revoke_token(token)

def test_protected_endpoint(auth_token):
    response = api_call("/protected", token=auth_token)
    assert response.status_code == 200
```

::: info Custom pytest markers
You can create custom markers to categorize tests:
```python
# pytest.ini or pyproject.toml
# [pytest]
# markers =
#     smoke: Quick smoke tests
#     regression: Regression tests
#     api: API tests

@pytest.mark.smoke
def test_login_page_loads():
    pass

@pytest.mark.regression
@pytest.mark.api
def test_create_user_via_api():
    pass
```
Run: `pytest -m smoke` — executes only smoke tests.
:::

### Comprehensive Example: API Test Decorator

```python
import time
from functools import wraps

def api_test(method="GET", expected_status=200, retries=2):
    """Universal decorator for API tests."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            last_error = None

            for attempt in range(1, retries + 1):
                try:
                    result = func(*args, **kwargs)
                    elapsed = time.perf_counter() - start
                    print(f"[{method}] {func.__name__} — "
                          f"{elapsed:.2f}s — PASSED")
                    return result
                except AssertionError as e:
                    last_error = e
                    if attempt < retries:
                        print(f"Attempt {attempt} failed, retrying...")
                        time.sleep(1)

            elapsed = time.perf_counter() - start
            print(f"[{method}] {func.__name__} — "
                  f"{elapsed:.2f}s — FAILED")
            raise last_error
        return wrapper
    return decorator

@api_test(method="POST", expected_status=201, retries=3)
def test_create_user():
    response = api_client.post("/users", json={"name": "Test"})
    assert response.status_code == 201
    assert "id" in response.json()
```

## Useful Links

- [Official Documentation — Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 — Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Real Python — Primer on Decorators](https://realpython.com/primer-on-python-decorators/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/file-io">← File I/O</a>
  <a href="/python_automation_courses/en/docs/python/error-handling">Error Handling →</a>
</div>
