# Best Practices

Best practices for writing Python code — PEP 8, typing, linters, and project organization.

## PEP 8 — Code Style

### Naming

```python
# Variables and functions — snake_case
user_name = "John"
max_retries = 3

def get_user_data(user_id: int) -> dict:
    pass

# Classes — PascalCase
class LoginPage:
    pass

class APIClient:
    pass

# Constants — UPPER_SNAKE_CASE
MAX_TIMEOUT = 30000
BASE_URL = "https://example.com"
DEFAULT_BROWSER = "chromium"

# Private attributes — with underscore
_internal_cache = {}

class Config:
    def __init__(self):
        self._token = None        # protected
        self.__session = None     # private
```

### Formatting

```python
# Indentation — 4 spaces
def function():
    if condition:
        do_something()

# Maximum line length — 79-120 characters
# Breaking long lines
result = (
    first_variable
    + second_variable
    - third_variable
)

long_list = [
    "element_one",
    "element_two",
    "element_three",
]

# Spaces around operators
x = 1
y = x + 2
is_valid = x == 1 and y > 0

# No spaces in default parameters
def func(name: str, timeout: int = 30000):
    pass
```

## Type Hints

```python
from typing import Optional

# Basic types
name: str = "John"
age: int = 25
score: float = 95.5
active: bool = True

# Collections
names: list[str] = ["Alice", "Bob"]
config: dict[str, int] = {"timeout": 30000}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (49.84, 24.02)

# Optional — can be None
def find_user(user_id: int) -> Optional[dict]:
    """Returns a user or None."""
    pass

# Union types (Python 3.10+)
def process(value: str | int) -> str:
    return str(value)

# Function as parameter
from typing import Callable
def retry(func: Callable[[], bool], attempts: int = 3) -> bool:
    pass
```

::: tip Type Checking
Use `mypy` for static type checking:
```bash
pip install mypy
mypy tests/ --ignore-missing-imports
```
:::

## Linters and Formatters

### Ruff (recommended)

```bash
# Installation
pip install ruff

# Check
ruff check .

# Auto-fix
ruff check --fix .

# Formatting (instead of black)
ruff format .
```

```toml
# pyproject.toml
[tool.ruff]
line-length = 120
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I"]
```

## QA Project Structure

```
automation-project/
├── pages/                    # Page Object Models
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                    # Tests
│   ├── __init__.py
│   ├── conftest.py          # Fixtures
│   ├── test_login.py
│   └── test_dashboard.py
├── utils/                    # Utilities
│   ├── __init__.py
│   ├── api_client.py
│   └── data_generator.py
├── test_data/                # Test data
│   ├── users.json
│   └── config.yaml
├── conftest.py               # Global fixtures
├── pytest.ini                # pytest configuration
├── pyproject.toml            # Project configuration
├── requirements.txt          # Dependencies
└── README.md
```

## Docstrings

```python
def login(email: str, password: str, remember: bool = False) -> bool:
    """Performs user login.

    Args:
        email: User's email address.
        password: Login password.
        remember: Whether to remember the session.

    Returns:
        True if login is successful, False otherwise.

    Raises:
        ValueError: If the email is invalid.
        ConnectionError: If the server is unavailable.
    """
    pass
```

## Clean Code Principles

```python
# DRY — Don't Repeat Yourself
# BAD
def test_login_valid():
    page.goto("/login")
    page.fill("#email", "user@test.com")
    page.fill("#password", "pass123")
    page.click("#submit")

def test_login_invalid():
    page.goto("/login")
    page.fill("#email", "invalid@test.com")
    page.fill("#password", "wrong")
    page.click("#submit")

# GOOD — extract shared logic
def perform_login(page, email: str, password: str):
    page.goto("/login")
    page.fill("#email", email)
    page.fill("#password", password)
    page.click("#submit")

def test_login_valid(page):
    perform_login(page, "user@test.com", "pass123")
    assert page.url.endswith("/dashboard")

def test_login_invalid(page):
    perform_login(page, "invalid@test.com", "wrong")
    assert page.get_by_text("Invalid credentials").is_visible()
```

```python
# KISS — Keep It Simple
# BAD — over-engineering
def is_element_visible(page, selector, timeout=5000, retry=3, log=True):
    for i in range(retry):
        try:
            el = page.wait_for_selector(selector, timeout=timeout//retry)
            if el and el.is_visible():
                if log: logger.info(f"Found: {selector}")
                return True
        except: pass
    return False

# GOOD — use built-in capabilities
def is_element_visible(page, selector: str) -> bool:
    return page.locator(selector).is_visible()
```

## Useful Links

- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [Ruff — Python linter](https://docs.astral.sh/ruff/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
