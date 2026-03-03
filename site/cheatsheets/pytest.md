# Pytest Cheatsheet

Швидкий довідник по pytest.

## Встановлення

```bash
pip install pytest pytest-playwright
```

## Запуск тестів

```bash
# Всі тести
pytest

# Verbose
pytest -v

# Конкретний файл
pytest tests/test_login.py

# Конкретний тест
pytest tests/test_login.py::test_valid_login

# По маркеру
pytest -m smoke
pytest -m "not slow"

# По keyword
pytest -k "login or register"

# Зупинка на першій помилці
pytest -x

# Останні N падінь
pytest --lf  # last failed
pytest --ff  # failed first

# Паралельно (pytest-xdist)
pytest -n auto
pytest -n 4

# З виводом print
pytest -s

# Показати локальні змінні
pytest -l

# Повторити flaky тести
pytest --reruns 3
```

## Структура тесту

```python
import pytest

def test_simple():
    """Простий тест"""
    assert 1 + 1 == 2

def test_exception():
    """Перевірка винятку"""
    with pytest.raises(ValueError):
        int("not a number")

def test_exception_message():
    """Перевірка повідомлення"""
    with pytest.raises(ValueError, match="invalid literal"):
        int("not a number")
```

## Fixtures

```python
import pytest

@pytest.fixture
def user():
    """Базова fixture"""
    return {"name": "John", "age": 30}

def test_user_name(user):
    assert user["name"] == "John"

# Fixture з setup/teardown
@pytest.fixture
def database():
    db = create_connection()  # setup
    yield db
    db.close()  # teardown

# Fixture scope
@pytest.fixture(scope="module")
def browser():
    """Один браузер на весь модуль"""
    b = launch_browser()
    yield b
    b.close()

# scope варіанти: function (default), class, module, package, session

# Автоматична fixture
@pytest.fixture(autouse=True)
def setup_logging():
    """Виконується для кожного тесту"""
    logging.info("Test started")
    yield
    logging.info("Test ended")
```

## Параметризація

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello", 5),
    ("world", 5),
    ("", 0),
])
def test_string_length(input, expected):
    assert len(input) == expected

# Множинна параметризація (комбінації)
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_multiply(x, y):
    # Виконається 4 рази: (1,3), (1,4), (2,3), (2,4)
    assert x * y > 0

# ID для параметрів
@pytest.mark.parametrize("email", [
    pytest.param("valid@test.com", id="valid_email"),
    pytest.param("invalid", id="invalid_email"),
])
def test_email(email):
    pass
```

## Markers

```python
import pytest

# Вбудовані маркери
@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
def test_unix():
    pass

@pytest.mark.xfail(reason="Known bug")
def test_buggy():
    pass

# Власні маркери
@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.slow
def test_full_report():
    pass

# Запуск: pytest -m smoke
```

## conftest.py

```python
# conftest.py - спільні fixtures для директорії

import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://staging.example.com"

@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)

# Hooks
def pytest_configure(config):
    """Виконується перед тестами"""
    config.addinivalue_line("markers", "smoke: smoke tests")

def pytest_collection_modifyitems(items):
    """Модифікація зібраних тестів"""
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)
```

## pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
python_classes = Test*

markers =
    smoke: smoke tests
    slow: slow tests

addopts = -v --tb=short

filterwarnings =
    ignore::DeprecationWarning
```

## Assertions

```python
# Базові
assert result == expected
assert result != unexpected
assert result is True
assert result is None
assert result is not None

# Колекції
assert item in collection
assert item not in collection
assert len(collection) == 5

# Приблизні значення
assert result == pytest.approx(3.14, rel=0.01)
assert result == pytest.approx(100, abs=5)

# Regex
import re
assert re.match(r"\d{3}-\d{4}", phone)
```

## Playwright + Pytest

```python
# test_login.py
import pytest
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("/login")
    page.get_by_label("Email").fill("user@test.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Sign In").click()

    expect(page).to_have_url("/dashboard")

# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
```

## Корисні плагіни

```bash
# Паралельний запуск
pip install pytest-xdist

# HTML звіти
pip install pytest-html

# Повторний запуск flaky тестів
pip install pytest-rerunfailures

# Порядок виконання
pip install pytest-ordering

# Таймаути
pip install pytest-timeout

# Coverage
pip install pytest-cov
pytest --cov=src --cov-report=html
```
