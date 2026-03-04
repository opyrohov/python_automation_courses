# Декоратори

Декоратори — це потужний інструмент Python, який дозволяє змінювати поведінку функцій та класів без зміни їхнього коду. У QA-автоматизації декоратори використовуються повсюдно: від pytest-маркерів до retry-логіки та логування.

## Функції як об'єкти першого класу

У Python функції — це об'єкти. Їх можна присвоювати змінним, передавати як аргументи та повертати з інших функцій.

```python
def greet(name):
    return f"Привіт, {name}!"

# Присвоєння функції змінній
say_hello = greet
print(say_hello("QA Engineer"))  # Привіт, QA Engineer!

# Передача функції як аргумент
def execute(func, value):
    return func(value)

result = execute(greet, "Тестувальник")
print(result)  # Привіт, Тестувальник!

# Повернення функції з функції
def create_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = create_multiplier(2)
print(double(5))  # 10
```

::: info Чому це важливо?
Розуміння функцій як об'єктів — це фундамент для роботи з декораторами. Декоратор — це функція, яка приймає іншу функцію та повертає нову функцію.
:::

## Простий декоратор

Декоратор — це функція-обгортка, яка додає поведінку до іншої функції.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До виклику функції")
        result = func(*args, **kwargs)
        print("Після виклику функції")
        return result
    return wrapper

# Використання через @
@my_decorator
def say_hello(name):
    print(f"Привіт, {name}!")

say_hello("World")
# До виклику функції
# Привіт, World!
# Після виклику функції
```

::: tip Що робить @decorator?
Запис `@my_decorator` перед функцією — це синтаксичний цукор для:
```python
say_hello = my_decorator(say_hello)
```
:::

## functools.wraps

Без `functools.wraps` декорована функція втрачає своє ім'я та документацію.

```python
from functools import wraps

# Без wraps — метадані втрачаються
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """Моя документація."""
    pass

print(my_function.__name__)  # wrapper (неправильно!)
print(my_function.__doc__)   # None (документація зникла!)

# З wraps — метадані зберігаються
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function():
    """Моя документація."""
    pass

print(my_function.__name__)  # my_function (правильно!)
print(my_function.__doc__)   # Моя документація.
```

::: warning Завжди використовуйте @wraps
Без `@wraps` ви втрачаєте `__name__`, `__doc__` та інші атрибути оригінальної функції. Це особливо критично при роботі з pytest, де ім'я функції використовується як ім'я тесту.
:::

## Декоратори з аргументами

Якщо декоратору потрібні параметри, додайте ще один рівень вкладеності.

```python
from functools import wraps

def repeat(times):
    """Декоратор, що повторює виклик функції N разів."""
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
    print(f"Привіт, {name}!")

say_hello("QA")
# Привіт, QA!
# Привіт, QA!
# Привіт, QA!
```

::: info Структура декоратора з аргументами
```
repeat(times=3)         → повертає decorator
  decorator(func)       → повертає wrapper
    wrapper(*args)      → виконує логіку
```
Тобто `@repeat(times=3)` спочатку викликає `repeat(3)`, який повертає справжній декоратор.
:::

## Вбудовані декоратори

### @staticmethod

Метод, який не потребує доступу до екземпляра (`self`) чи класу (`cls`).

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_positive(number):
        return number > 0

# Виклик без створення екземпляра
print(MathUtils.add(2, 3))        # 5
print(MathUtils.is_positive(-1))  # False
```

### @classmethod

Метод, що отримує клас (`cls`) замість екземпляра (`self`). Зручний для альтернативних конструкторів.

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

admin = User.create_admin("Олена")
tester = User.create_tester("Андрій")
print(admin.role)   # admin
print(tester.role)  # tester
```

### @property

Дозволяє звертатися до методу як до атрибута. Зручно для обчислюваних значень та валідації.

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
            raise ValueError("Кількість не може бути від'ємною")
        self._passed = value

result = TestResult(passed=8, failed=2)
print(result.total)      # 10 (виклик без дужок)
print(result.pass_rate)  # 80.0

result.passed = 9        # Використання setter
print(result.pass_rate)  # 90.0

result.passed = -1       # ValueError: Кількість не може бути від'ємною
```

::: tip Коли використовувати @property?
- Коли потрібно обчислюване поле (як `total` та `pass_rate`)
- Коли потрібна валідація при встановленні значення (setter)
- Коли хочете зробити атрибут тільки для читання (без setter)
:::

## Стекування декораторів

Декоратори можна комбінувати — вони застосовуються знизу вгору.

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
    return f"Привіт, {name}"

print(greet("World"))
# <b><i>Привіт, World</i></b>
```

::: info Порядок виконання
```python
@bold       # 2. Потім bold обгортає результат italic
@italic     # 1. Спочатку italic обгортає greet
def greet(name):
    ...
```
Це еквівалентно: `greet = bold(italic(greet))`
:::

## Декоратори на основі класів

Декоратор може бути класом із методом `__call__`.

```python
from functools import wraps

class CountCalls:
    """Підраховує кількість викликів функції."""

    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"{self.func.__name__} викликано {self.call_count} раз(ів)")
        return self.func(*args, **kwargs)

@CountCalls
def process_data(data):
    return len(data)

process_data([1, 2, 3])  # process_data викликано 1 раз(ів)
process_data([4, 5])      # process_data викликано 2 раз(ів)
print(process_data.call_count)  # 2
```

::: tip Коли використовувати клас-декоратор?
- Коли декоратору потрібно зберігати стан між викликами (лічильник, кеш)
- Коли логіка декоратора складна і потребує кількох методів
- Коли хочете використовувати наслідування декораторів
:::

## Приклади для QA-автоматизації

### Retry-декоратор

Повторює виконання тесту при невдачі — незамінний для нестабільних тестів.

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Повторює виклик функції при виникненні помилки."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Спроба {attempt}/{max_attempts} невдала: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2, exceptions=(TimeoutError, ConnectionError))
def fetch_api_data(url):
    """Отримує дані з API з retry-логікою."""
    import requests
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

### Timer-декоратор

Вимірює час виконання функції — корисно для моніторингу продуктивності тестів.

```python
import time
from functools import wraps

def timer(func):
    """Вимірює час виконання функції."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} виконано за {elapsed:.4f} сек")
        return result
    return wrapper

@timer
def run_heavy_test():
    """Тест, що займає багато часу."""
    time.sleep(2)
    assert True

run_heavy_test()
# [TIMER] run_heavy_test виконано за 2.0012 сек
```

### Logging-декоратор

Автоматично логує виклики функцій — допомагає при дебагу тестів.

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_call(func):
    """Логує виклик функції з аргументами та результатом."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"Виклик {func.__name__}({signature})")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} повернув {result!r}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} викликав помилку: {e}")
            raise
    return wrapper

@log_call
def login(username, password):
    """Авторизація користувача."""
    if username == "admin" and password == "secret":
        return {"status": "success", "token": "abc123"}
    raise ValueError("Невірні облікові дані")

login("admin", "secret")
# INFO: Виклик login('admin', 'secret')
# INFO: login повернув {'status': 'success', 'token': 'abc123'}
```

### Pytest-маркери як декоратори

Pytest активно використовує декоратори для маркування та параметризації тестів.

```python
import pytest

# Маркер для пропуску тесту
@pytest.mark.skip(reason="Не реалізовано")
def test_future_feature():
    pass

# Маркер для очікуваної помилки
@pytest.mark.xfail(reason="Відомий баг #123")
def test_known_bug():
    assert 1 + 1 == 3

# Параметризація — один тест з різними даними
@pytest.mark.parametrize("username, password, expected", [
    ("admin", "admin123", True),
    ("user", "wrong", False),
    ("", "", False),
])
def test_login(username, password, expected):
    result = authenticate(username, password)
    assert result == expected

# Комбінування маркерів
@pytest.mark.smoke
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_homepage(browser):
    """Smoke-тест головної сторінки в різних браузерах."""
    pass

# Фікстури — теж декоратори
@pytest.fixture
def auth_token():
    """Отримує токен авторизації перед тестом."""
    token = get_auth_token("admin", "secret")
    yield token
    revoke_token(token)

def test_protected_endpoint(auth_token):
    response = api_call("/protected", token=auth_token)
    assert response.status_code == 200
```

::: info Власні маркери pytest
Ви можете створювати власні маркери для категоризації тестів:
```python
# pytest.ini або pyproject.toml
# [pytest]
# markers =
#     smoke: Швидкі smoke-тести
#     regression: Регресійні тести
#     api: Тести API

@pytest.mark.smoke
def test_login_page_loads():
    pass

@pytest.mark.regression
@pytest.mark.api
def test_create_user_via_api():
    pass
```
Запуск: `pytest -m smoke` — виконає тільки smoke-тести.
:::

### Комплексний приклад: декоратор для API-тестів

```python
import time
from functools import wraps

def api_test(method="GET", expected_status=200, retries=2):
    """Універсальний декоратор для API-тестів."""
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
                        print(f"Спроба {attempt} невдала, повтор...")
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

## Корисні посилання

- [Офіційна документація — Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 — Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Real Python — Primer on Decorators](https://realpython.com/primer-on-python-decorators/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/file-io">← Робота з файлами</a>
  <a href="/python_automation_courses/docs/python/error-handling">Обробка помилок →</a>
</div>
