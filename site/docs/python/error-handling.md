# Обробка помилок

Механізм try/except в Python — перехоплення винятків, створення власних винятків та стратегії обробки помилок.

## try / except / else / finally

```python
# Базова обробка
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Ділення на нуль!")

# Повна конструкція
try:
    data = json.loads(response_text)
except json.JSONDecodeError as e:
    print(f"Невалідний JSON: {e}")
except Exception as e:
    print(f"Неочікувана помилка: {e}")
else:
    # Виконується якщо помилок НЕ було
    print(f"Дані отримано: {data}")
finally:
    # Виконується ЗАВЖДИ
    print("Обробку завершено")
```

## Типи винятків

```python
# Найпоширеніші винятки
ValueError       # Неправильне значення
TypeError        # Неправильний тип
KeyError         # Ключ не знайдено в словнику
IndexError       # Індекс за межами
AttributeError   # Атрибут не існує
FileNotFoundError # Файл не знайдено
ImportError      # Помилка імпорту
TimeoutError     # Час очікування вичерпано
ConnectionError  # Помилка з'єднання
PermissionError  # Немає доступу
```

```python
# Перехоплення кількох винятків
try:
    value = config["timeout"]
    timeout = int(value)
except KeyError:
    print("Ключ 'timeout' не знайдено")
    timeout = 30000
except (ValueError, TypeError):
    print("Невалідне значення timeout")
    timeout = 30000
```

## Власні винятки

```python
class TestError(Exception):
    """Базовий клас для помилок тестування."""
    pass

class ElementNotFoundError(TestError):
    """Елемент не знайдено на сторінці."""
    def __init__(self, selector: str, timeout: int = 30000):
        self.selector = selector
        self.timeout = timeout
        super().__init__(
            f"Елемент '{selector}' не знайдено за {timeout}ms"
        )

class APIError(TestError):
    """Помилка API запиту."""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"API Error {status_code}: {message}")

# Використання
def find_element(page, selector: str):
    element = page.query_selector(selector)
    if element is None:
        raise ElementNotFoundError(selector)
    return element

try:
    btn = find_element(page, "#submit-btn")
except ElementNotFoundError as e:
    print(f"Помилка: {e}")
    print(f"Селектор: {e.selector}")
```

## raise та re-raise

```python
# Виклик винятку
def validate_status_code(code: int) -> None:
    if code < 100 or code > 599:
        raise ValueError(f"Невалідний HTTP код: {code}")

# Re-raise — прокидання винятку далі
def safe_api_call(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError:
        logger.error(f"Не вдалося з'єднатися з {url}")
        raise  # прокидає той самий виняток далі
    except requests.HTTPError as e:
        logger.error(f"HTTP помилка: {e}")
        raise APIError(e.response.status_code, str(e))
```

## Контекстні менеджери

```python
# with — автоматичне закриття ресурсів
with open("data.json", "r") as f:
    data = json.load(f)
# файл автоматично закритий

# Власний контекстний менеджер
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.time() - self.start
        print(f"Виконано за {self.duration:.2f}s")
        return False  # не придушувати винятки

with Timer() as t:
    page.goto("https://example.com")
    page.wait_for_load_state("networkidle")
print(f"Завантаження: {t.duration:.2f}s")
```

::: tip Retry патерн для нестабільних тестів
```python
import time

def retry(func, attempts: int = 3, delay: float = 1.0):
    """Повторює виклик функції при помилці."""
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except Exception as e:
            last_error = e
            print(f"Спроба {attempt}/{attempts} невдала: {e}")
            if attempt < attempts:
                time.sleep(delay)
    raise last_error

# Використання
result = retry(
    lambda: page.get_by_text("Dashboard").click(),
    attempts=3,
    delay=2.0
)
```
:::

## Assertions у тестах

```python
# assert — для тестів
def test_login_success(page):
    page.goto("/login")
    page.fill("#email", "user@test.com")
    page.fill("#password", "password123")
    page.click("#submit")

    # Assertion з повідомленням
    assert page.url.endswith("/dashboard"), \
        f"Очікувався URL /dashboard, отримано: {page.url}"

    title = page.title()
    assert "Dashboard" in title, \
        f"Заголовок має містити 'Dashboard', отримано: '{title}'"
```

::: warning assert у продакшн коді
`assert` можна вимкнути прапором `-O`. Використовуйте `assert` тільки в тестах. Для продакшн коду використовуйте `raise` з відповідним винятком.
:::

## Корисні посилання

- [Документація: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Документація: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [PEP 3134 — Exception Chaining](https://peps.python.org/pep-3134/)
