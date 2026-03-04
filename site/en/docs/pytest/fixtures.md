# Fixtures

Fixtures in pytest — a mechanism for preparing and cleaning up the test environment.

## Basic Fixture

```python
import pytest

@pytest.fixture
def user_data():
    """Returns test user data."""
    return {
        "name": "John Doe",
        "email": "john@test.com",
        "password": "SecurePass123"
    }

def test_login(user_data):
    assert user_data["email"] == "john@test.com"
    assert len(user_data["password"]) >= 8
```

## Fixture Scope

```python
# function — for each test (default)
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# class — once per class
@pytest.fixture(scope="class")
def api_client():
    client = APIClient(base_url="https://api.example.com")
    yield client
    client.close()

# module — once per file
@pytest.fixture(scope="module")
def database():
    db = Database.connect("test_db")
    yield db
    db.disconnect()

# session — once per entire run
@pytest.fixture(scope="session")
def browser():
    browser = playwright.chromium.launch()
    yield browser
    browser.close()
```

::: warning Scope Order
`session` > `module` > `class` > `function`

A fixture with a narrower scope cannot depend on a fixture with a wider scope in reverse direction.
:::

## yield — Setup and Teardown

```python
@pytest.fixture
def authenticated_page(page):
    # SETUP — runs before the test
    page.goto("/login")
    page.fill("#email", "user@test.com")
    page.fill("#password", "password123")
    page.click("#submit")
    page.wait_for_url("**/dashboard")

    yield page  # Pass to the test

    # TEARDOWN — runs after the test
    page.goto("/logout")
    page.wait_for_url("**/login")
```

## conftest.py

The `conftest.py` file is automatically available to all tests in the directory.

```python
# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
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

## Factory Fixtures

```python
@pytest.fixture
def create_user():
    """Factory for creating users."""
    created_users = []

    def _create_user(name: str = "Test User", role: str = "tester"):
        user = {"name": name, "role": role, "id": len(created_users) + 1}
        created_users.append(user)
        return user

    yield _create_user

    # Clean up all created users
    for user in created_users:
        print(f"Deleting user: {user['name']}")

def test_multiple_users(create_user):
    admin = create_user("Admin", "admin")
    tester = create_user("Tester", "tester")
    assert admin["role"] == "admin"
    assert tester["role"] == "tester"
```

## autouse

```python
@pytest.fixture(autouse=True)
def log_test_name(request):
    """Automatically logs the name of each test."""
    print(f"\n▶ Starting: {request.node.name}")
    yield
    print(f"✓ Completed: {request.node.name}")

# Automatic cookie cleanup
@pytest.fixture(autouse=True)
def clear_cookies(page):
    yield
    page.context.clear_cookies()
```

## Built-in Fixtures

```python
# tmp_path — temporary directory
def test_save_report(tmp_path):
    report_file = tmp_path / "report.json"
    report_file.write_text('{"status": "passed"}')
    assert report_file.exists()

# request — test information
@pytest.fixture
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")

# capsys — capturing stdout/stderr
def test_output(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

# monkeypatch — patching values
def test_env_variable(monkeypatch):
    monkeypatch.setenv("BASE_URL", "https://test.example.com")
    import os
    assert os.getenv("BASE_URL") == "https://test.example.com"
```

## Useful Links

- [Documentation: Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Documentation: conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html)
