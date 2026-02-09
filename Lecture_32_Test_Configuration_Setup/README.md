# Lecture 32: Test Configuration & Setup

## Overview
Learn how to configure pytest and Playwright for your test projects. Configure browser options, timeouts, base URL, automatic screenshots and traces on failure, and run tests across multiple browsers.

## Topics Covered

### 1. pytest.ini / pyproject.toml
- Configuring pytest settings
- Test paths and discovery
- Default command-line options
- Registering custom markers

### 2. conftest.py in Depth
- Fixture scopes (function, class, session)
- Browser and context configuration
- Shared setup across all tests

### 3. Browser Options
- Headless vs headed mode
- Slow motion for debugging
- Browser channel (Chrome, Edge)
- Viewport and device emulation

### 4. Base URL Configuration
- Setting base URL to avoid repetition
- Using `page.goto("/login")` with base URL
- Environment-specific URLs

### 5. Timeout Settings
- Global timeout configuration
- Per-test timeout
- Navigation timeout
- Action timeout (click, fill, etc.)

### 6. Screenshots & Traces on Failure
- Automatic screenshot on test failure
- Playwright trace recording
- Trace viewer for debugging
- Video recording

### 7. Multiple Browser Testing
- Running on Chromium, Firefox, WebKit
- Browser-specific configuration
- Cross-browser test strategy

## Examples

1. **01_pytest_ini_config.py** - pytest.ini and pyproject.toml configuration
2. **02_conftest_browser_options.py** - Browser and context configuration via conftest.py
3. **03_base_url_and_timeouts.py** - Base URL setup and timeout configuration
4. **04_screenshots_and_traces.py** - Automatic screenshots and traces on failure
5. **05_multi_browser_testing.py** - Running tests on multiple browsers

## Exercises

1. **exercise_01_project_config.py** - Set up a complete project configuration
2. **exercise_02_failure_handling.py** - Configure screenshots and traces on failure

## Key Concepts

### pytest.ini
```ini
[pytest]
addopts = -v --headed --slowmo 500
base_url = https://the-internet.herokuapp.com
markers =
    smoke: Quick smoke tests
    regression: Full regression tests
```

### conftest.py with Browser Options
```python
import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"slow_mo": 500}

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }
```

### Timeout Configuration
```python
# conftest.py
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
    }

# In test - per-action timeout
def test_with_timeout(page):
    page.goto("/login", timeout=10000)
    page.locator("#btn").click(timeout=5000)
```

### Running Multiple Browsers
```bash
pytest --browser chromium --browser firefox --browser webkit
```

## Resources
- [Pytest-Playwright Configuration](https://playwright.dev/python/docs/test-runners)
- [Playwright Browser Contexts](https://playwright.dev/python/docs/browser-contexts)
- [Playwright Trace Viewer](https://playwright.dev/python/docs/trace-viewer)

## Next Lecture
Lecture 33: Test Data Management
