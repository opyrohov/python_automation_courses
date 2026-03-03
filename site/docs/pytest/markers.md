# Markers

Маркери в pytest — мітки для організації, фільтрації та управління виконанням тестів.

## Вбудовані маркери

### skip та skipif

```python
import pytest
import sys

# Безумовний пропуск
@pytest.mark.skip(reason="Функціонал ще не реалізовано")
def test_new_feature():
    pass

# Умовний пропуск
@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Тест тільки для Linux"
)
def test_linux_only():
    pass

# Програмний пропуск
def test_with_condition():
    if not has_database_connection():
        pytest.skip("Немає з'єднання з БД")
    # ... тест продовжується
```

### xfail

```python
# Очікуваний провал
@pytest.mark.xfail(reason="Відомий баг #123")
def test_known_bug():
    assert broken_function() == expected_result

# Строгий xfail — якщо тест пройде, це ПОМИЛКА
@pytest.mark.xfail(strict=True, reason="Не має працювати")
def test_strict_xfail():
    assert 1 + 1 == 3

# Умовний xfail
@pytest.mark.xfail(
    condition=sys.version_info < (3, 11),
    reason="Потрібен Python 3.11+"
)
def test_new_python_feature():
    pass
```

## Користувацькі маркери

### Реєстрація маркерів

```ini
# pytest.ini
[pytest]
markers =
    smoke: Швидкі базові тести
    regression: Повний регресійний набір
    critical: Критично важливі тести
    slow: Повільні тести
    api: Тести API
    ui: Тести UI
```

### Використання

```python
import pytest

@pytest.mark.smoke
@pytest.mark.critical
def test_login():
    """Критичний smoke тест."""
    pass

@pytest.mark.regression
@pytest.mark.ui
def test_complex_form():
    """UI регресійний тест."""
    pass

@pytest.mark.api
def test_create_user():
    """API тест."""
    pass

# Маркер на весь клас
@pytest.mark.ui
class TestDashboard:
    def test_widgets(self):
        pass

    def test_navigation(self):
        pass
```

### Запуск з маркерами

```bash
# Запуск тільки smoke тестів
pytest -m smoke

# Запуск smoke АБО critical
pytest -m "smoke or critical"

# Запуск НЕ slow тестів
pytest -m "not slow"

# Комбінація
pytest -m "smoke and not api"
pytest -m "(smoke or regression) and not slow"
```

## Маркер parametrize

```python
@pytest.mark.parametrize("email,password,expected", [
    ("valid@test.com", "Pass123!", True),
    ("invalid", "Pass123!", False),
    ("valid@test.com", "", False),
    ("", "", False),
])
def test_login_validation(email, password, expected):
    result = validate_login(email, password)
    assert result == expected
```

::: tip Детальніше про параметризацію
Дивіться розділ [Параметризація](/docs/pytest/parametrize) для поглибленого вивчення.
:::

## Маркери для управління порядком

```python
# pytest-ordering плагін
@pytest.mark.order(1)
def test_create_account():
    pass

@pytest.mark.order(2)
def test_login():
    pass

@pytest.mark.order(3)
def test_delete_account():
    pass
```

## Фільтрація з маркерами в conftest

```python
# conftest.py
def pytest_collection_modifyitems(config, items):
    """Автоматично додає маркер slow до тестів довших за 5с."""
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)
```

## Корисні посилання

- [Документація: Markers](https://docs.pytest.org/en/stable/how-to/mark.html)
- [Документація: Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
