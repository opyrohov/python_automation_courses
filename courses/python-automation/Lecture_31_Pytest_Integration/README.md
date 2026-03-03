# Lecture 31: Pytest Integration

## Overview
Introduction to pytest framework for running Playwright tests. Learn how to write test functions, use built-in fixtures, parameterize tests, organize with markers, and run tests from the command line.

## Topics Covered

### 1. From Scripts to Tests
- Why use pytest instead of running scripts manually
- Installing pytest and pytest-playwright
- Writing your first test function

### 2. Pytest Basics
- Test function naming conventions
- assert statements in pytest
- Test discovery rules

### 3. Playwright Fixtures
- Built-in `page` fixture
- `context` and `browser` fixtures
- Creating custom fixtures with `conftest.py`

### 4. Parameterized Tests
- `@pytest.mark.parametrize` decorator
- Testing multiple inputs with one function
- Multiple parameter combinations

### 5. Markers and Grouping
- Built-in markers (`skip`, `xfail`)
- Custom markers (`smoke`, `regression`)
- Running specific groups of tests

### 6. Running Tests
- Basic pytest commands
- Filtering tests by name, marker, file
- Useful flags (`-v`, `-s`, `--headed`, `-k`)

## Examples

1. **01_basic_test_function.py** - First pytest tests with Playwright
2. **02_pytest_fixtures.py** - Using page, context, browser fixtures
3. **03_parameterized_tests.py** - Testing multiple data sets
4. **04_markers_and_grouping.py** - Organizing tests with markers
5. **05_complete_test_suite.py** - Full test suite with all concepts

## Exercises

1. **exercise_01_write_basic_tests.py** - Write test functions for a web page
2. **exercise_02_fixtures_and_parametrize.py** - Use fixtures and parametrize

## Key Concepts

### Installation
```bash
pip install pytest pytest-playwright
playwright install
```

### Basic Test Function
```python
# test_example.py
from playwright.sync_api import Page

def test_page_title(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

### Parameterized Test
```python
import pytest

@pytest.mark.parametrize("url,title", [
    ("https://example.com", "Example Domain"),
    ("https://playwright.dev", "Playwright"),
])
def test_titles(page, url, title):
    page.goto(url)
    assert title in page.title()
```

### Custom Fixtures (conftest.py)
```python
import pytest

@pytest.fixture
def logged_in_page(page):
    page.goto("https://example.com/login")
    page.locator("#username").fill("user")
    page.locator("#password").fill("pass")
    page.locator("button").click()
    return page
```

### Running Tests
```bash
pytest                          # Run all tests
pytest test_file.py             # Run specific file
pytest -v                       # Verbose output
pytest -k "login"               # Filter by name
pytest -m smoke                 # Filter by marker
pytest --headed                 # Show browser
pytest --slowmo 500             # Slow down actions
```

## Resources
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-Playwright Plugin](https://playwright.dev/python/docs/test-runners)
- [Playwright Test Configuration](https://playwright.dev/python/docs/test-runners#cli-arguments)

## Next Lecture
Lecture 32: Advanced Pytest
