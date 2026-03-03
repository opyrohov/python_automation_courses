# Best Practices

Кращі практики написання Python коду — PEP 8, типізація, лінтери та організація проєкту.

## PEP 8 — Стиль коду

### Іменування

```python
# Змінні та функції — snake_case
user_name = "John"
max_retries = 3

def get_user_data(user_id: int) -> dict:
    pass

# Класи — PascalCase
class LoginPage:
    pass

class APIClient:
    pass

# Константи — UPPER_SNAKE_CASE
MAX_TIMEOUT = 30000
BASE_URL = "https://example.com"
DEFAULT_BROWSER = "chromium"

# Приватні атрибути — з підкресленням
_internal_cache = {}

class Config:
    def __init__(self):
        self._token = None        # захищений
        self.__session = None     # приватний
```

### Форматування

```python
# Відступи — 4 пробіли
def function():
    if condition:
        do_something()

# Максимальна довжина рядка — 79-120 символів
# Розбиття довгих рядків
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

# Пробіли навколо операторів
x = 1
y = x + 2
is_valid = x == 1 and y > 0

# Без пробілів у параметрах за замовчуванням
def func(name: str, timeout: int = 30000):
    pass
```

## Type Hints

```python
from typing import Optional

# Базові типи
name: str = "John"
age: int = 25
score: float = 95.5
active: bool = True

# Колекції
names: list[str] = ["Alice", "Bob"]
config: dict[str, int] = {"timeout": 30000}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (49.84, 24.02)

# Optional — може бути None
def find_user(user_id: int) -> Optional[dict]:
    """Повертає користувача або None."""
    pass

# Union типи (Python 3.10+)
def process(value: str | int) -> str:
    return str(value)

# Функція як параметр
from typing import Callable
def retry(func: Callable[[], bool], attempts: int = 3) -> bool:
    pass
```

::: tip Перевірка типів
Використовуйте `mypy` для статичної перевірки типів:
```bash
pip install mypy
mypy tests/ --ignore-missing-imports
```
:::

## Лінтери та форматери

### Ruff (рекомендовано)

```bash
# Встановлення
pip install ruff

# Перевірка
ruff check .

# Автоматичне виправлення
ruff check --fix .

# Форматування (замість black)
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

## Структура QA проєкту

```
automation-project/
├── pages/                    # Page Object Models
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                    # Тести
│   ├── __init__.py
│   ├── conftest.py          # Фікстури
│   ├── test_login.py
│   └── test_dashboard.py
├── utils/                    # Утиліти
│   ├── __init__.py
│   ├── api_client.py
│   └── data_generator.py
├── test_data/                # Тестові дані
│   ├── users.json
│   └── config.yaml
├── conftest.py               # Глобальні фікстури
├── pytest.ini                # Конфігурація pytest
├── pyproject.toml            # Конфігурація проєкту
├── requirements.txt          # Залежності
└── README.md
```

## Docstrings

```python
def login(email: str, password: str, remember: bool = False) -> bool:
    """Виконує вхід користувача.

    Args:
        email: Email адреса користувача.
        password: Пароль для входу.
        remember: Чи запам'ятовувати сесію.

    Returns:
        True якщо вхід успішний, False інакше.

    Raises:
        ValueError: Якщо email невалідний.
        ConnectionError: Якщо сервер недоступний.
    """
    pass
```

## Принципи чистого коду

```python
# DRY — Don't Repeat Yourself
# ПОГАНО
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

# ДОБРЕ — винести спільну логіку
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
# ПОГАНО — надмірна складність
def is_element_visible(page, selector, timeout=5000, retry=3, log=True):
    for i in range(retry):
        try:
            el = page.wait_for_selector(selector, timeout=timeout//retry)
            if el and el.is_visible():
                if log: logger.info(f"Found: {selector}")
                return True
        except: pass
    return False

# ДОБРЕ — використовувати вбудовані можливості
def is_element_visible(page, selector: str) -> bool:
    return page.locator(selector).is_visible()
```

## Корисні посилання

- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [Ruff — Python linter](https://docs.astral.sh/ruff/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
