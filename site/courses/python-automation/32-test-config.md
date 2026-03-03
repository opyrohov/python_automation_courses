# Lecture 32: Test Configuration & Setup

Конфігурація та налаштування тестів.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_32_Test_Configuration_Setup/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_32_Test_Configuration_Setup/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_32_Test_Configuration_Setup/exercises)

</div>

## pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
python_classes = Test*

addopts = -v --tb=short

markers =
    smoke: smoke tests
    regression: regression tests
    slow: slow running tests

filterwarnings =
    ignore::DeprecationWarning
```

## conftest.py

```python
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

@pytest.fixture
def base_url():
    return "https://staging.example.com"
```

## Змінні середовища

```python
# .env
BASE_URL=https://staging.example.com
API_KEY=secret123

# conftest.py
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:3000")
```

## pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
markers = [
    "smoke: smoke tests",
    "slow: slow tests"
]

[tool.playwright]
browsers = ["chromium"]
```

## Структура conftest

```
tests/
├── conftest.py          # Глобальні fixtures
├── test_login.py
├── auth/
│   ├── conftest.py      # Fixtures для auth тестів
│   └── test_auth.py
└── api/
    ├── conftest.py      # Fixtures для API тестів
    └── test_api.py
```
