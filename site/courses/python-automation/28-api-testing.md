# Lecture 28: API Testing

Тестування API з Playwright.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_28_API_Testing/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_28_API_Testing/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_28_API_Testing/exercises)

</div>

## APIRequestContext

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Створення API context
    api = p.request.new_context(
        base_url="https://api.example.com"
    )

    # GET запит
    response = api.get("/users")
    print(response.json())

    api.dispose()
```

## HTTP методи

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

## Заголовки та авторизація

```python
api = p.request.new_context(
    base_url="https://api.example.com",
    extra_http_headers={
        "Authorization": "Bearer token123",
        "Content-Type": "application/json"
    }
)
```

## Перевірки

```python
response = api.get("/users")

# Статус
assert response.ok  # 2xx
assert response.status == 200

# Тіло
data = response.json()
assert len(data) > 0
assert data[0]["name"] == "John"

# Заголовки
assert response.headers["content-type"] == "application/json"
```

## API + UI тести

```python
def test_create_user_via_api_and_verify_in_ui(page, api):
    # Створити через API
    response = api.post("/users", data={
        "name": "Test User",
        "email": "test@example.com"
    })
    user_id = response.json()["id"]

    # Перевірити через UI
    page.goto(f"/users/{user_id}")
    expect(page.get_by_text("Test User")).to_be_visible()
```

## Fixture для API

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
