# ООП

Об'єктно-орієнтоване програмування в Python — класи, об'єкти, наслідування, інкапсуляція та поліморфізм.

## Класи та об'єкти

```python
class User:
    """Клас для представлення користувача."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(name='{self.name}', email='{self.email}')"

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

# Створення об'єктів
user1 = User("John", "john@test.com")
user2 = User("Jane", "jane@test.com")

print(user1)       # John (john@test.com)
print(repr(user1)) # User(name='John', email='john@test.com')
```

## Атрибути та методи

```python
class TestConfig:
    # Атрибут класу — спільний для всіх об'єктів
    default_timeout = 30000

    def __init__(self, base_url: str, browser: str = "chromium"):
        # Атрибути екземпляра
        self.base_url = base_url
        self.browser = browser
        self._retries = 3  # "приватний" атрибут (конвенція)

    @property
    def retries(self) -> int:
        """Getter для retries."""
        return self._retries

    @retries.setter
    def retries(self, value: int) -> None:
        """Setter з валідацією."""
        if value < 0:
            raise ValueError("Retries не може бути від'ємним")
        self._retries = value

    @classmethod
    def from_env(cls, env: str) -> "TestConfig":
        """Фабричний метод для створення з оточення."""
        urls = {
            "dev": "https://dev.example.com",
            "staging": "https://staging.example.com",
            "prod": "https://example.com",
        }
        return cls(base_url=urls.get(env, urls["dev"]))

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Статичний метод — не потребує self чи cls."""
        return url.startswith(("http://", "https://"))

# Використання
config = TestConfig("https://example.com")
config.retries = 5
print(config.retries)  # 5

staging = TestConfig.from_env("staging")
print(TestConfig.is_valid_url("https://test.com"))  # True
```

## Наслідування

```python
class BasePage:
    """Базовий клас для всіх сторінок."""

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_load(self) -> None:
        self.page.wait_for_load_state("networkidle")


class LoginPage(BasePage):
    """Сторінка логіну — наслідує BasePage."""

    URL = "/login"

    def __init__(self, page):
        super().__init__(page)  # виклик конструктора батька
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.submit_btn = page.get_by_role("button", name="Sign In")

    def login(self, email: str, password: str) -> None:
        self.navigate(self.URL)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_btn.click()


class AdminLoginPage(LoginPage):
    """Адмін-логін — наслідує LoginPage."""

    URL = "/admin/login"

    def login_as_admin(self) -> None:
        self.login("admin@test.com", "admin123")
```

## Інкапсуляція

```python
class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url      # публічний
        self._token = token            # захищений (конвенція)
        self.__session_id = None       # приватний (name mangling)

    @property
    def token(self) -> str:
        return self._token

    def _build_headers(self) -> dict:
        """Захищений метод — для внутрішнього використання."""
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint: str) -> dict:
        """Публічний метод."""
        headers = self._build_headers()
        # виконання запиту...
        return {}
```

::: info Конвенції доступу
- `name` — публічний атрибут
- `_name` — захищений (за конвенцією, не примусово)
- `__name` — приватний (name mangling: `_ClassName__name`)
:::

## Поліморфізм

```python
from abc import ABC, abstractmethod

class BaseAssertion(ABC):
    """Абстрактний базовий клас."""

    @abstractmethod
    def check(self) -> bool:
        """Кожен підклас реалізує свою перевірку."""
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
        return "Елемент має бути видимим"


class TextAssertion(BaseAssertion):
    def __init__(self, locator, expected_text: str):
        self.locator = locator
        self.expected_text = expected_text

    def check(self) -> bool:
        return self.locator.text_content() == self.expected_text

    def get_message(self) -> str:
        return f"Текст має бути '{self.expected_text}'"


# Поліморфне використання
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

# Автоматично генеруються __init__, __repr__, __eq__
result = TestResult("test_login", "passed", 1.5, ["smoke"])
print(result)  # TestResult(name='test_login', status='passed', ...)
print(result.is_passed)  # True

# Порівняння
result2 = TestResult("test_login", "passed", 1.5, ["smoke"])
print(result == result2)  # True
```

## Корисні посилання

- [Документація: Класи](https://docs.python.org/3/tutorial/classes.html)
- [Документація: dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
