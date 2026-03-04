# Markers

Markers in pytest — labels for organizing, filtering, and controlling test execution.

## Built-in Markers

### skip and skipif

```python
import pytest
import sys

# Unconditional skip
@pytest.mark.skip(reason="Feature not yet implemented")
def test_new_feature():
    pass

# Conditional skip
@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Linux only test"
)
def test_linux_only():
    pass

# Programmatic skip
def test_with_condition():
    if not has_database_connection():
        pytest.skip("No database connection")
    # ... test continues
```

### xfail

```python
# Expected failure
@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug():
    assert broken_function() == expected_result

# Strict xfail — if the test passes, it is an ERROR
@pytest.mark.xfail(strict=True, reason="Should not work")
def test_strict_xfail():
    assert 1 + 1 == 3

# Conditional xfail
@pytest.mark.xfail(
    condition=sys.version_info < (3, 11),
    reason="Requires Python 3.11+"
)
def test_new_python_feature():
    pass
```

## Custom Markers

### Registering Markers

```ini
# pytest.ini
[pytest]
markers =
    smoke: Quick basic tests
    regression: Full regression suite
    critical: Critically important tests
    slow: Slow tests
    api: API tests
    ui: UI tests
```

### Usage

```python
import pytest

@pytest.mark.smoke
@pytest.mark.critical
def test_login():
    """Critical smoke test."""
    pass

@pytest.mark.regression
@pytest.mark.ui
def test_complex_form():
    """UI regression test."""
    pass

@pytest.mark.api
def test_create_user():
    """API test."""
    pass

# Marker on entire class
@pytest.mark.ui
class TestDashboard:
    def test_widgets(self):
        pass

    def test_navigation(self):
        pass
```

### Running with Markers

```bash
# Run only smoke tests
pytest -m smoke

# Run smoke OR critical
pytest -m "smoke or critical"

# Run NOT slow tests
pytest -m "not slow"

# Combination
pytest -m "smoke and not api"
pytest -m "(smoke or regression) and not slow"
```

## parametrize Marker

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

::: tip More on Parametrization
See the [Parametrization](/en/docs/pytest/parametrize) section for in-depth coverage.
:::

## Markers for Order Management

```python
# pytest-ordering plugin
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

## Filtering with Markers in conftest

```python
# conftest.py
def pytest_collection_modifyitems(config, items):
    """Automatically adds the slow marker to tests longer than 5s."""
    for item in items:
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)
```

## Useful Links

- [Documentation: Markers](https://docs.pytest.org/en/stable/how-to/mark.html)
- [Documentation: Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
