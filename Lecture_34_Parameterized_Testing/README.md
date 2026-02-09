# Lecture 34: Parameterized Testing

## Overview
Deep dive into parameterized testing with pytest. Learn advanced parametrize patterns, stacking multiple decorators, indirect parametrization, dynamic test generation, and best practices for data-driven testing.

## Topics Covered

### 1. Parametrize in Depth
- Single and multiple parameters
- Custom test IDs
- Parametrize with objects and dicts

### 2. Stacking Parametrize
- Multiple @parametrize decorators
- Cartesian product of parameters
- Matrix testing (browsers x viewports)

### 3. Indirect Parametrization
- Passing parameters to fixtures
- Dynamic fixture configuration
- Parametrized fixtures

### 4. Dynamic Test Generation
- Generating test cases programmatically
- pytest_generate_tests hook
- Loading parameters from external sources

### 5. Combining with Data Files
- Parametrize from JSON/CSV files
- Excel integration with openpyxl
- Filtering test data

### 6. Best Practices
- Naming and IDs
- Organizing large parameter sets
- Handling expected failures in parametrize

## Examples

1. **01_parametrize_basics.py** - Single, multiple, and dict parameters
2. **02_stacking_parametrize.py** - Multiple decorators and cartesian products
3. **03_indirect_parametrize.py** - Parametrizing fixtures
4. **04_dynamic_generation.py** - Programmatic test generation
5. **05_advanced_patterns.py** - Real-world patterns and best practices

## Exercises

1. **exercise_01_data_driven_login.py** - Comprehensive login test suite with parametrize
2. **exercise_02_matrix_testing.py** - Cross-browser and viewport matrix testing

## Key Concepts

### Stacking Parametrize (Cartesian Product)
```python
@pytest.mark.parametrize("browser", ["chromium", "firefox"])
@pytest.mark.parametrize("viewport", ["desktop", "mobile"])
def test_cross_browser(browser, viewport):
    # Runs 4 tests: chromium+desktop, chromium+mobile, firefox+desktop, firefox+mobile
    pass
```

### Indirect Parametrization
```python
@pytest.fixture
def user_page(request, page):
    role = request.param
    # setup based on role...
    return page

@pytest.mark.parametrize("user_page", ["admin", "guest"], indirect=True)
def test_access(user_page):
    pass
```

### Dynamic Generation
```python
def pytest_generate_tests(metafunc):
    if "login_data" in metafunc.fixturenames:
        data = load_json("test_data.json")
        metafunc.parametrize("login_data", data)
```

## Resources
- [Pytest Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Pytest Generate Tests](https://docs.pytest.org/en/stable/how-to/parametrize.html#basic-pytest-generate-tests-example)

## Next Lecture
Lecture 35: Debugging Techniques
