# Функції

Функції в Python — визначення, параметри, повернення значень, декоратори та анонімні функції.

## Визначення функції

```python
# Базова функція
def greet(name: str) -> str:
    """Повертає привітання."""
    return f"Hello, {name}!"

result = greet("QA Engineer")
print(result)  # Hello, QA Engineer!

# Функція без повернення
def log_message(message: str) -> None:
    print(f"[LOG] {message}")
```

## Параметри

### Позиційні та іменовані

```python
def create_user(name: str, age: int, role: str = "Tester") -> dict:
    return {"name": name, "age": age, "role": role}

# Позиційні аргументи
create_user("John", 25)

# Іменовані аргументи
create_user(name="John", age=25, role="QA Lead")

# Змішані
create_user("John", age=25)
```

### Default параметри

```python
def run_test(
    url: str,
    browser: str = "chromium",
    headless: bool = True,
    timeout: int = 30000
) -> None:
    print(f"Running on {browser}, headless={headless}")

# Використання default значень
run_test("https://example.com")

# Перевизначення конкретних параметрів
run_test("https://example.com", headless=False, timeout=60000)
```

::: warning Мутабельні default значення
Ніколи не використовуйте мутабельні об'єкти як default параметри:
```python
# НЕПРАВИЛЬНО — список спільний між викликами
def add_item(item, items=[]):
    items.append(item)
    return items

# ПРАВИЛЬНО
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```
:::

### *args та **kwargs

```python
# *args — довільна кількість позиційних аргументів
def sum_all(*args: int) -> int:
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs — довільна кількість іменованих аргументів
def create_config(**kwargs) -> dict:
    return {key: value for key, value in kwargs.items()}

config = create_config(browser="firefox", timeout=5000, retries=3)
# {"browser": "firefox", "timeout": 5000, "retries": 3}

# Комбінування
def setup_test(name: str, *tags: str, **options) -> dict:
    return {
        "name": name,
        "tags": list(tags),
        "options": options
    }

setup_test("login", "smoke", "critical", timeout=30, retries=2)
```

## Повернення значень

```python
# Повернення кількох значень (кортеж)
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5])

# Раннє повернення
def validate_email(email: str) -> bool:
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True
```

## Lambda функції

```python
# Анонімні функції
square = lambda x: x ** 2
add = lambda a, b: a + b

# Використання з sort
users = [
    {"name": "Charlie", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
]

# Сортування за віком
users.sort(key=lambda u: u["age"])

# Сортування за ім'ям
users.sort(key=lambda u: u["name"])

# Використання з filter та map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
```

## Декоратори

```python
import time
from functools import wraps

# Декоратор для вимірювання часу
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} виконано за {duration:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Декоратор з параметрами
def retry(attempts: int = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Спроба {attempt}/{attempts} невдала: {e}")
                    if attempt == attempts:
                        raise
        return wrapper
    return decorator

@retry(attempts=3)
def unstable_api_call():
    # Виклик нестабільного API
    pass
```

::: tip Декоратори у тестуванні
```python
import pytest

# pytest маркери — це по суті декоратори
@pytest.mark.smoke
@pytest.mark.parametrize("browser", ["chromium", "firefox"])
def test_login(browser):
    pass

# Власний декоратор для логування тестів
def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"▶ Запуск: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✓ Завершено: {func.__name__}")
        return result
    return wrapper
```
:::

## Генератори

```python
# Функція-генератор з yield
def read_test_data(file_path: str):
    """Читає тестові дані порціями."""
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

# Використання
for data in read_test_data("test_data.txt"):
    print(data)

# Generator expression
squares = (x**2 for x in range(1000000))  # не займає пам'ять
```

## Корисні посилання

- [Документація: Функції](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 318 — Декоратори](https://peps.python.org/pep-0318/)
- [Real Python: Decorators](https://realpython.com/primer-on-python-decorators/)
