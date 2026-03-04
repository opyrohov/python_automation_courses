# Lecture 32: Test Configuration

Test configuration and setup.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_32_Test_Configuration_Setup/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_32_Test_Configuration_Setup/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_32_Test_Configuration_Setup/exercises" target="_blank">📝 Вправи</a>
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

## Environment Variables

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

## conftest Structure

```
tests/
├── conftest.py          # Global fixtures
├── test_login.py
├── auth/
│   ├── conftest.py      # Fixtures for auth tests
│   └── test_auth.py
└── api/
    ├── conftest.py      # Fixtures for API tests
    └── test_api.py
```
