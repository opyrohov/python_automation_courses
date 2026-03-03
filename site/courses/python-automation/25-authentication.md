# Lecture 25: Authentication

Аутентифікація в тестах.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_25_Authentication/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_25_Authentication/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_25_Authentication/exercises)

</div>

## Логін через UI

```python
def login(page, email, password):
    page.goto("/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")
```

## Збереження стану (Storage State)

```python
# Логін та збереження стану
context = browser.new_context()
page = context.new_page()
login(page, "user@test.com", "password")

# Зберегти стан
context.storage_state(path="auth.json")
context.close()

# Використання збереженого стану
context = browser.new_context(storage_state="auth.json")
page = context.new_page()
page.goto("/dashboard")  # Вже залогінений!
```

## Fixture для authenticated user

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
# Встановити заголовок для всіх запитів
context = browser.new_context(
    extra_http_headers={
        "Authorization": "Bearer your-token-here"
    }
)
```
