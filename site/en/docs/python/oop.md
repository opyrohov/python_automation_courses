# OOP

Object-oriented programming in Python — classes, objects, inheritance, encapsulation, and polymorphism.

## Classes and Objects

```python
class User:
    """Class representing a user."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(name='{self.name}', email='{self.email}')"

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

# Creating objects
user1 = User("John", "john@test.com")
user2 = User("Jane", "jane@test.com")

print(user1)       # John (john@test.com)
print(repr(user1)) # User(name='John', email='john@test.com')
```

## Attributes and Methods

```python
class TestConfig:
    # Class attribute — shared across all objects
    default_timeout = 30000

    def __init__(self, base_url: str, browser: str = "chromium"):
        # Instance attributes
        self.base_url = base_url
        self.browser = browser
        self._retries = 3  # "private" attribute (convention)

    @property
    def retries(self) -> int:
        """Getter for retries."""
        return self._retries

    @retries.setter
    def retries(self, value: int) -> None:
        """Setter with validation."""
        if value < 0:
            raise ValueError("Retries cannot be negative")
        self._retries = value

    @classmethod
    def from_env(cls, env: str) -> "TestConfig":
        """Factory method to create from environment."""
        urls = {
            "dev": "https://dev.example.com",
            "staging": "https://staging.example.com",
            "prod": "https://example.com",
        }
        return cls(base_url=urls.get(env, urls["dev"]))

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Static method — does not require self or cls."""
        return url.startswith(("http://", "https://"))

# Usage
config = TestConfig("https://example.com")
config.retries = 5
print(config.retries)  # 5

staging = TestConfig.from_env("staging")
print(TestConfig.is_valid_url("https://test.com"))  # True
```

## Inheritance

```python
class BasePage:
    """Base class for all pages."""

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_load(self) -> None:
        self.page.wait_for_load_state("networkidle")


class LoginPage(BasePage):
    """Login page — inherits from BasePage."""

    URL = "/login"

    def __init__(self, page):
        super().__init__(page)  # call parent constructor
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.submit_btn = page.get_by_role("button", name="Sign In")

    def login(self, email: str, password: str) -> None:
        self.navigate(self.URL)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_btn.click()


class AdminLoginPage(LoginPage):
    """Admin login — inherits from LoginPage."""

    URL = "/admin/login"

    def login_as_admin(self) -> None:
        self.login("admin@test.com", "admin123")
```

## Encapsulation

```python
class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url      # public
        self._token = token            # protected (convention)
        self.__session_id = None       # private (name mangling)

    @property
    def token(self) -> str:
        return self._token

    def _build_headers(self) -> dict:
        """Protected method — for internal use."""
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint: str) -> dict:
        """Public method."""
        headers = self._build_headers()
        # executing request...
        return {}
```

::: info Access Conventions
- `name` — public attribute
- `_name` — protected (by convention, not enforced)
- `__name` — private (name mangling: `_ClassName__name`)
:::

## Polymorphism

```python
from abc import ABC, abstractmethod

class BaseAssertion(ABC):
    """Abstract base class."""

    @abstractmethod
    def check(self) -> bool:
        """Each subclass implements its own check."""
        pass

    @abstractmethod
    def get_message(self) -> str:
        pass


class VisibilityAssertion(BaseAssertion):
    def __init__(self, locator):
        self.locator = locator

    def check(self) -> bool:
        return self.locator.is_visible()

    def get_message(self) -> str:
        return "Element should be visible"


class TextAssertion(BaseAssertion):
    def __init__(self, locator, expected_text: str):
        self.locator = locator
        self.expected_text = expected_text

    def check(self) -> bool:
        return self.locator.text_content() == self.expected_text

    def get_message(self) -> str:
        return f"Text should be '{self.expected_text}'"


# Polymorphic usage
def run_assertions(assertions: list[BaseAssertion]) -> None:
    for assertion in assertions:
        if not assertion.check():
            raise AssertionError(assertion.get_message())
```

## Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class TestResult:
    name: str
    status: str
    duration: float
    tags: list[str] = field(default_factory=list)

    @property
    def is_passed(self) -> bool:
        return self.status == "passed"

# Automatically generates __init__, __repr__, __eq__
result = TestResult("test_login", "passed", 1.5, ["smoke"])
print(result)  # TestResult(name='test_login', status='passed', ...)
print(result.is_passed)  # True

# Comparison
result2 = TestResult("test_login", "passed", 1.5, ["smoke"])
print(result == result2)  # True
```

## Useful Links

- [Documentation: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Documentation: dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
