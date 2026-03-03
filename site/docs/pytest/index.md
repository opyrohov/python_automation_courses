# Pytest

Документація з pytest — найпопулярнішого фреймворку для тестування в Python.

## Розділи

- [Fixtures](/docs/pytest/fixtures) - Підготовка та очищення тестів
- [Markers](/docs/pytest/markers) - Мітки для організації тестів
- [Параметризація](/docs/pytest/parametrize) - Data-driven тестування
- [Конфігурація](/docs/pytest/configuration) - pytest.ini, conftest.py
- [Плагіни](/docs/pytest/plugins) - Розширення функціональності

## Швидкий старт

```python
import pytest

# Простий тест
def test_addition():
    assert 1 + 1 == 2

# Тест з fixture
@pytest.fixture
def sample_data():
    return {"name": "Test", "value": 42}

def test_with_fixture(sample_data):
    assert sample_data["name"] == "Test"

# Параметризований тест
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (0, 0, 0),
])
def test_sum(a, b, expected):
    assert a + b == expected
```

## Основні команди

```bash
# Запуск всіх тестів
pytest

# Запуск з verbose
pytest -v

# Запуск конкретного файлу
pytest tests/test_login.py

# Запуск з маркером
pytest -m smoke

# Паралельний запуск
pytest -n auto
```

## Корисні посилання

- [Офіційна документація Pytest](https://docs.pytest.org/)
- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
