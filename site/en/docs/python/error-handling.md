# Error Handling

The try/except mechanism in Python — catching exceptions, creating custom exceptions, and error handling strategies.

## try / except / else / finally

```python
# Basic handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")

# Full structure
try:
    data = json.loads(response_text)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    # Executes if there were NO errors
    print(f"Data received: {data}")
finally:
    # Executes ALWAYS
    print("Processing complete")
```

## Exception Types

```python
# Most common exceptions
ValueError       # Invalid value
TypeError        # Invalid type
KeyError         # Key not found in dictionary
IndexError       # Index out of range
AttributeError   # Attribute does not exist
FileNotFoundError # File not found
ImportError      # Import error
TimeoutError     # Timeout expired
ConnectionError  # Connection error
PermissionError  # Access denied
```

```python
# Catching multiple exceptions
try:
    value = config["timeout"]
    timeout = int(value)
except KeyError:
    print("Key 'timeout' not found")
    timeout = 30000
except (ValueError, TypeError):
    print("Invalid timeout value")
    timeout = 30000
```

## Custom Exceptions

```python
class TestError(Exception):
    """Base class for testing errors."""
    pass

class ElementNotFoundError(TestError):
    """Element not found on the page."""
    def __init__(self, selector: str, timeout: int = 30000):
        self.selector = selector
        self.timeout = timeout
        super().__init__(
            f"Element '{selector}' not found within {timeout}ms"
        )

class APIError(TestError):
    """API request error."""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"API Error {status_code}: {message}")

# Usage
def find_element(page, selector: str):
    element = page.query_selector(selector)
    if element is None:
        raise ElementNotFoundError(selector)
    return element

try:
    btn = find_element(page, "#submit-btn")
except ElementNotFoundError as e:
    print(f"Error: {e}")
    print(f"Selector: {e.selector}")
```

## raise and re-raise

```python
# Raising an exception
def validate_status_code(code: int) -> None:
    if code < 100 or code > 599:
        raise ValueError(f"Invalid HTTP code: {code}")

# Re-raise — propagating the exception further
def safe_api_call(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError:
        logger.error(f"Failed to connect to {url}")
        raise  # re-raises the same exception
    except requests.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        raise APIError(e.response.status_code, str(e))
```

## Context Managers

```python
# with — automatic resource cleanup
with open("data.json", "r") as f:
    data = json.load(f)
# file is automatically closed

# Custom context manager
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.time() - self.start
        print(f"Executed in {self.duration:.2f}s")
        return False  # don't suppress exceptions

with Timer() as t:
    page.goto("https://example.com")
    page.wait_for_load_state("networkidle")
print(f"Load time: {t.duration:.2f}s")
```

::: tip Retry Pattern for Flaky Tests
```python
import time

def retry(func, attempts: int = 3, delay: float = 1.0):
    """Retries function call on failure."""
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except Exception as e:
            last_error = e
            print(f"Attempt {attempt}/{attempts} failed: {e}")
            if attempt < attempts:
                time.sleep(delay)
    raise last_error

# Usage
result = retry(
    lambda: page.get_by_text("Dashboard").click(),
    attempts=3,
    delay=2.0
)
```
:::

## Assertions in Tests

```python
# assert — for tests
def test_login_success(page):
    page.goto("/login")
    page.fill("#email", "user@test.com")
    page.fill("#password", "password123")
    page.click("#submit")

    # Assertion with message
    assert page.url.endswith("/dashboard"), \
        f"Expected URL /dashboard, got: {page.url}"

    title = page.title()
    assert "Dashboard" in title, \
        f"Title should contain 'Dashboard', got: '{title}'"
```

::: warning assert in Production Code
`assert` can be disabled with the `-O` flag. Use `assert` only in tests. For production code, use `raise` with the appropriate exception.
:::

## Useful Links

- [Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Documentation: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [PEP 3134 — Exception Chaining](https://peps.python.org/pep-3134/)
