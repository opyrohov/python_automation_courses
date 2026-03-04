# Configuration

pytest settings — configuration files, command line options, and conftest.py.

## Configuration Files

### pyproject.toml (recommended)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short --strict-markers"
markers = [
    "smoke: Quick basic tests",
    "regression: Full regression suite",
    "api: API tests",
    "ui: UI tests",
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
    smoke: Quick basic tests
    regression: Full regression suite
```

### conftest.py

```python
# conftest.py — global fixtures and hooks
import pytest

def pytest_addoption(parser):
    """Adds custom CLI options."""
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        choices=["dev", "staging", "prod"],
        help="Environment for testing"
    )
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Browser for tests"
    )

@pytest.fixture(scope="session")
def env(request):
    """Returns the current environment."""
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
    """Returns the URL for the environment."""
    urls = {
        "dev": "https://dev.example.com",
        "staging": "https://staging.example.com",
        "prod": "https://example.com",
    }
    return urls[env]
```

## Command Line Options

```bash
# Basic options
pytest -v                    # Verbose output
pytest -q                    # Minimal output
pytest -x                    # Stop on first failure
pytest --maxfail=3           # Stop after 3 failures
pytest -s                    # Show print() output
pytest --tb=short            # Short traceback
pytest --tb=long             # Full traceback
pytest --tb=no               # No traceback

# Test selection
pytest tests/test_login.py              # Specific file
pytest tests/test_login.py::test_valid  # Specific test
pytest tests/test_login.py::TestClass   # Specific class
pytest -k "login"                       # By keyword
pytest -k "login and not slow"          # Combination
pytest -m smoke                         # By marker

# Parallel execution (pytest-xdist)
pytest -n auto               # Auto-detect number of processes
pytest -n 4                  # 4 parallel processes

# Reports
pytest --html=report.html    # HTML report
pytest --alluredir=allure-results  # Allure report
pytest --junitxml=report.xml # JUnit XML
```

## pytest Hooks

```python
# conftest.py

def pytest_configure(config):
    """Runs at pytest startup."""
    config.addinivalue_line("markers", "e2e: End-to-end tests")

def pytest_collection_modifyitems(config, items):
    """Modifies collected tests."""
    # Add slow marker to tests with 'slow' in the name
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)

def pytest_runtest_makereport(item, call):
    """Creates a test report."""
    if call.when == "call" and call.excinfo is not None:
        # Test failed — save screenshot
        print(f"FAILED: {item.name}")

def pytest_terminal_summary(terminalreporter, exitstatus):
    """Final summary."""
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    print(f"\nSummary: {passed} passed, {failed} failed")
```

## Environment Variables

```python
# .env file
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
        pytest.skip("API_KEY not set")
    return key
```

::: tip CI/CD Configuration
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

## Useful Links

- [Documentation: Configuration](https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref)
- [Documentation: conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py)
- [Documentation: Hooks](https://docs.pytest.org/en/stable/reference/reference.html#hooks)
