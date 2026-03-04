# Lecture 25: Authentication

Authentication in tests.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_25_Authentication/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_25_Authentication/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_25_Authentication/exercises" target="_blank">📝 Вправи</a>
</div>

## Login via UI

```python
def login(page, email, password):
    page.goto("/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")
```

## Saving State (Storage State)

```python
# Login and save state
context = browser.new_context()
page = context.new_page()
login(page, "user@test.com", "password")

# Save state
context.storage_state(path="auth.json")
context.close()

# Using saved state
context = browser.new_context(storage_state="auth.json")
page = context.new_page()
page.goto("/dashboard")  # Already logged in!
```

## Fixture for authenticated user

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("/login")
    page.get_by_label("Email").fill("user@test.com")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")

    storage = context.storage_state()
    context.close()
    return storage

@pytest.fixture
def authenticated_page(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()
```

## HTTP Authentication

```python
# Basic auth
context = browser.new_context(
    http_credentials={
        "username": "admin",
        "password": "secret"
    }
)
```

## API Token

```python
# Set header for all requests
context = browser.new_context(
    extra_http_headers={
        "Authorization": "Bearer your-token-here"
    }
)
```
