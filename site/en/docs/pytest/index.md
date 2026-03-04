# Pytest

Documentation on pytest — the most popular testing framework for Python.

## Sections

- [Fixtures](/en/docs/pytest/fixtures) - Test setup and teardown
- [Markers](/en/docs/pytest/markers) - Labels for test organization
- [Parametrization](/en/docs/pytest/parametrize) - Data-driven testing
- [Configuration](/en/docs/pytest/configuration) - pytest.ini, conftest.py
- [Plugins](/en/docs/pytest/plugins) - Extending functionality

## Quick Start

```python
import pytest

# Simple test
def test_addition():
    assert 1 + 1 == 2

# Test with fixture
@pytest.fixture
def sample_data():
    return {"name": "Test", "value": 42}

def test_with_fixture(sample_data):
    assert sample_data["name"] == "Test"

# Parametrized test
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (0, 0, 0),
])
def test_sum(a, b, expected):
    assert a + b == expected
```

## Basic Commands

```bash
# Run all tests
pytest

# Run with verbose
pytest -v

# Run specific file
pytest tests/test_login.py

# Run with marker
pytest -m smoke

# Parallel execution
pytest -n auto
```

## Useful Links

- [Official Pytest Documentation](https://docs.pytest.org/)
- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
