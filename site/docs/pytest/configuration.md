# Конфігурація

Налаштування pytest — конфігураційні файли, опції командного рядка та conftest.py.

## Конфігураційні файли

### pyproject.toml (рекомендовано)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short --strict-markers"
markers = [
    "smoke: Швидкі базові тести",
    "regression: Повний регресійний набір",
    "api: Тести API",
    "ui: Тести UI",
]
filterwarnings = [
    "ignore::DeprecationWarning",
]
```

### pytest.ini

```ini
[pytest]
testpaths = tests
addopts = -v --tb=short
markers =
    smoke: Швидкі базові тести
    regression: Повний регресійний набір
```

### conftest.py

```python
# conftest.py — глобальні фікстури та хуки
import pytest

def pytest_addoption(parser):
    """Додає кастомні CLI опції."""
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        choices=["dev", "staging", "prod"],
        help="Середовище для тестування"
    )
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Браузер для тестів"
    )

@pytest.fixture(scope="session")
def env(request):
    """Повертає поточне середовище."""
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
    """Повертає URL для середовища."""
    urls = {
        "dev": "https://dev.example.com",
        "staging": "https://staging.example.com",
        "prod": "https://example.com",
    }
    return urls[env]
```

## Опції командного рядка

```bash
# Базові опції
pytest -v                    # Детальний вивід
pytest -q                    # Мінімальний вивід
pytest -x                    # Зупинка на першому провалі
pytest --maxfail=3           # Зупинка після 3 провалів
pytest -s                    # Показати print() вивід
pytest --tb=short            # Короткий traceback
pytest --tb=long             # Повний traceback
pytest --tb=no               # Без traceback

# Вибір тестів
pytest tests/test_login.py              # Конкретний файл
pytest tests/test_login.py::test_valid  # Конкретний тест
pytest tests/test_login.py::TestClass   # Конкретний клас
pytest -k "login"                       # За ключовим словом
pytest -k "login and not slow"          # Комбінація
pytest -m smoke                         # За маркером

# Паралельний запуск (pytest-xdist)
pytest -n auto               # Автовизначення кількості процесів
pytest -n 4                  # 4 паралельні процеси

# Звіти
pytest --html=report.html    # HTML звіт
pytest --alluredir=allure-results  # Allure звіт
pytest --junitxml=report.xml # JUnit XML
```

## Хуки pytest

```python
# conftest.py

def pytest_configure(config):
    """Виконується при старті pytest."""
    config.addinivalue_line("markers", "e2e: End-to-end тести")

def pytest_collection_modifyitems(config, items):
    """Модифікує зібрані тести."""
    # Додати маркер slow до тестів з 'slow' у назві
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)

def pytest_runtest_makereport(item, call):
    """Створює звіт про тест."""
    if call.when == "call" and call.excinfo is not None:
        # Тест провалився — зберегти скріншот
        print(f"FAILED: {item.name}")

def pytest_terminal_summary(terminalreporter, exitstatus):
    """Фінальний підсумок."""
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    print(f"\nПідсумок: {passed} пройшло, {failed} провалено")
```

## Змінні оточення

```python
# .env файл
# BASE_URL=https://staging.example.com
# API_KEY=secret123

# conftest.py
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://localhost:3000")

@pytest.fixture(scope="session")
def api_key():
    key = os.getenv("API_KEY")
    if not key:
        pytest.skip("API_KEY не встановлено")
    return key
```

::: tip CI/CD конфігурація
```yaml
# GitHub Actions
- name: Run tests
  env:
    BASE_URL: https://staging.example.com
    API_KEY: ${{ secrets.API_KEY }}
  run: |
    pytest tests/ -v --tb=short -n auto --html=report.html
```
:::

## Корисні посилання

- [Документація: Configuration](https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref)
- [Документація: conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py)
- [Документація: Hooks](https://docs.pytest.org/en/stable/reference/reference.html#hooks)
