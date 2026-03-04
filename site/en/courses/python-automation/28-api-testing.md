# Lecture 28: API Testing

API testing with Playwright.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_28_API_Testing/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_28_API_Testing/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_28_API_Testing/exercises" target="_blank">📝 Вправи</a>
</div>

## APIRequestContext

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create API context
    api = p.request.new_context(
        base_url="https://api.example.com"
    )

    # GET request
    response = api.get("/users")
    print(response.json())

    api.dispose()
```

## HTTP Methods

```python
# GET
response = api.get("/users")
response = api.get("/users/1")

# POST
response = api.post("/users", data={
    "name": "John",
    "email": "john@example.com"
})

# PUT
response = api.put("/users/1", data={
    "name": "John Updated"
})

# PATCH
response = api.patch("/users/1", data={
    "email": "new@example.com"
})

# DELETE
response = api.delete("/users/1")
```

## Headers and Authorization

```python
api = p.request.new_context(
    base_url="https://api.example.com",
    extra_http_headers={
        "Authorization": "Bearer token123",
        "Content-Type": "application/json"
    }
)
```

## Assertions

```python
response = api.get("/users")

# Status
assert response.ok  # 2xx
assert response.status == 200

# Body
data = response.json()
assert len(data) > 0
assert data[0]["name"] == "John"

# Headers
assert response.headers["content-type"] == "application/json"
```

## API + UI Tests

```python
def test_create_user_via_api_and_verify_in_ui(page, api):
    # Create via API
    response = api.post("/users", data={
        "name": "Test User",
        "email": "test@example.com"
    })
    user_id = response.json()["id"]

    # Verify via UI
    page.goto(f"/users/{user_id}")
    expect(page.get_by_text("Test User")).to_be_visible()
```

## Fixture for API

```python
# conftest.py
import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def api(playwright: Playwright):
    api = playwright.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={"Authorization": "Bearer token"}
    )
    yield api
    api.dispose()
```
