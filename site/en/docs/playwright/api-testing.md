# API Testing — Testing API with Playwright

Playwright allows testing APIs without launching a browser using `APIRequestContext`. This is useful for testing backends, preparing test data, or combining API and UI tests. In this section, we will cover all aspects of API testing.

## APIRequestContext Basics

```python
from playwright.sync_api import sync_playwright, APIRequestContext

def test_basic_api_request():
    """Basic API request without a browser."""
    with sync_playwright() as p:
        # Create API request context
        api_context = p.request.new_context(
            base_url="https://api.example.com",
            extra_http_headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        # GET request
        response = api_context.get("/users")
        assert response.ok  # Check status 2xx
        assert response.status == 200

        # Get data
        users = response.json()
        assert len(users) > 0

        # Close context
        api_context.dispose()
```

## HTTP Methods

### GET Requests

```python
def test_get_requests(api_context: APIRequestContext):
    """Various GET request options."""

    # Simple GET request
    response = api_context.get("/api/users")
    assert response.status == 200
    users = response.json()

    # GET with query parameters
    response = api_context.get("/api/users", params={
        "page": 1,
        "limit": 10,
        "sort": "name",
        "order": "asc",
    })
    data = response.json()
    assert len(data["items"]) <= 10

    # GET specific resource
    response = api_context.get("/api/users/42")
    assert response.status == 200
    user = response.json()
    assert user["id"] == 42
```

### POST Requests

```python
def test_post_requests(api_context: APIRequestContext):
    """Creating resources via POST."""

    # POST with JSON body
    response = api_context.post("/api/users", data={
        "name": "John Smith",
        "email": "john@example.com",
        "role": "tester",
    })
    assert response.status == 201
    created_user = response.json()
    assert created_user["name"] == "John Smith"
    assert "id" in created_user

    # POST with form-data
    response = api_context.post("/api/feedback", form={
        "name": "Olena",
        "message": "Great service!",
        "rating": "5",
    })
    assert response.status == 201

    # POST with multipart (file upload)
    response = api_context.post("/api/upload", multipart={
        "file": {
            "name": "report.pdf",
            "mimeType": "application/pdf",
            "buffer": open("tests/data/report.pdf", "rb").read(),
        },
        "description": "Monthly report",
    })
    assert response.status == 200
```

### PUT and PATCH Requests

```python
def test_put_patch_requests(api_context: APIRequestContext):
    """Updating resources via PUT and PATCH."""

    # PUT — full resource update
    response = api_context.put("/api/users/42", data={
        "name": "John Johnson",
        "email": "john.j@example.com",
        "role": "senior_tester",
    })
    assert response.status == 200
    updated = response.json()
    assert updated["name"] == "John Johnson"

    # PATCH — partial resource update
    response = api_context.patch("/api/users/42", data={
        "role": "lead_tester",
    })
    assert response.status == 200
    patched = response.json()
    assert patched["role"] == "lead_tester"
```

### DELETE Requests

```python
def test_delete_requests(api_context: APIRequestContext):
    """Deleting resources via DELETE."""

    # Delete resource
    response = api_context.delete("/api/users/42")
    assert response.status == 204  # No Content

    # Verify resource is deleted
    response = api_context.get("/api/users/42")
    assert response.status == 404
```

## Setup via pytest Fixtures

```python
# conftest.py
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    """Fixture for API context with basic settings."""
    context = playwright.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    yield context
    context.dispose()

@pytest.fixture(scope="session")
def auth_api_context(playwright: Playwright) -> APIRequestContext:
    """Fixture for authenticated API context."""
    # Get token
    context = playwright.request.new_context(
        base_url="https://api.example.com",
    )
    response = context.post("/auth/login", data={
        "email": "admin@example.com",
        "password": "admin123",
    })
    token = response.json()["access_token"]
    context.dispose()

    # Create authenticated context
    auth_context = playwright.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
    )
    yield auth_context
    auth_context.dispose()
```

## Response Validation

```python
import re

def test_response_validation(api_context: APIRequestContext):
    """Detailed API response validation."""
    response = api_context.get("/api/users/1")

    # Status code check
    assert response.status == 200
    assert response.ok  # True for statuses 200-299

    # Status text check
    assert response.status_text == "OK"

    # Response headers check
    headers = response.headers
    assert headers["content-type"] == "application/json; charset=utf-8"
    assert "x-request-id" in headers

    # Response body check
    user = response.json()
    assert user["id"] == 1
    assert isinstance(user["name"], str)
    assert len(user["name"]) > 0
    assert re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", user["email"])
    assert user["role"] in ["admin", "user", "tester"]

    # Nested objects check
    assert "address" in user
    assert user["address"]["city"] is not None

    # Arrays check
    assert isinstance(user["permissions"], list)
    assert len(user["permissions"]) > 0
```

::: tip Tip
For complex JSON schema validation, you can use the `jsonschema` or `pydantic` libraries together with Playwright.
:::

## Testing CRUD Operations

```python
def test_full_crud_cycle(api_context: APIRequestContext):
    """Full CRUD operations cycle for a resource."""

    # CREATE — create a new user
    create_response = api_context.post("/api/users", data={
        "name": "Test User",
        "email": "test_crud@example.com",
        "role": "tester",
    })
    assert create_response.status == 201
    user_id = create_response.json()["id"]

    # READ — read the created user
    read_response = api_context.get(f"/api/users/{user_id}")
    assert read_response.status == 200
    user = read_response.json()
    assert user["name"] == "Test User"

    # UPDATE — update the user
    update_response = api_context.put(f"/api/users/{user_id}", data={
        "name": "Updated User",
        "email": "test_crud@example.com",
        "role": "senior_tester",
    })
    assert update_response.status == 200
    assert update_response.json()["name"] == "Updated User"

    # DELETE — delete the user
    delete_response = api_context.delete(f"/api/users/{user_id}")
    assert delete_response.status == 204

    # Verify deletion
    verify_response = api_context.get(f"/api/users/{user_id}")
    assert verify_response.status == 404
```

## Combining API and UI Tests

```python
from playwright.sync_api import Page, expect

def test_api_prepare_ui_verify(page: Page):
    """Prepare data via API, verify via UI."""

    # Create test data via API
    api = page.context.request
    response = api.post("https://api.example.com/products", data={
        "name": "Test Product for UI",
        "price": 999.99,
        "category": "electronics",
    })
    product_id = response.json()["id"]

    # Verify via UI
    page.goto(f"https://example.com/products/{product_id}")
    expect(page.get_by_role("heading", level=1)).to_have_text("Test Product for UI")
    expect(page.get_by_test_id("price")).to_contain_text("999.99")

    # Cleanup via API
    api.delete(f"https://api.example.com/products/{product_id}")


def test_ui_action_api_verify(page: Page):
    """Action via UI, verification via API."""

    # Create an order via UI
    page.goto("https://example.com/products/1")
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Checkout").click()
    page.get_by_label("Address").fill("123 Main Street")
    page.get_by_role("button", name="Confirm").click()

    # Get order ID from UI
    order_text = page.get_by_test_id("order-number").text_content()
    order_id = order_text.split("#")[1]

    # Verify via API
    api = page.context.request
    response = api.get(f"https://api.example.com/orders/{order_id}")
    order = response.json()
    assert order["status"] == "pending"
    assert order["address"] == "123 Main Street"
```

::: info Information
Combining API and UI tests is a powerful strategy. API requests are faster for preparing and cleaning up test data, while UI tests verify what the user sees.
:::

## API Error Testing

```python
def test_api_error_handling(api_context: APIRequestContext):
    """Testing API error handling."""

    # 400 Bad Request — invalid data
    response = api_context.post("/api/users", data={
        "email": "not-an-email",
    })
    assert response.status == 400
    error = response.json()
    assert "validation" in error["error"].lower()

    # 401 Unauthorized — without authentication
    response = api_context.get("/api/admin/settings")
    assert response.status == 401

    # 404 Not Found — non-existent resource
    response = api_context.get("/api/users/999999")
    assert response.status == 404

    # 409 Conflict — duplicate
    api_context.post("/api/users", data={
        "name": "Duplicate",
        "email": "duplicate@example.com",
    })
    response = api_context.post("/api/users", data={
        "name": "Duplicate 2",
        "email": "duplicate@example.com",
    })
    assert response.status == 409

    # 422 Unprocessable Entity — semantic error
    response = api_context.post("/api/orders", data={
        "product_id": 1,
        "quantity": -5,  # Negative quantity
    })
    assert response.status == 422
```

## Network Request Interception

```python
def test_intercept_api_requests(page: Page):
    """Intercepting and modifying API requests in the browser."""

    # Mocking API response
    page.route("**/api/users", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='[{"id": 1, "name": "Mock User"}]',
    ))
    page.goto("https://example.com/users")
    expect(page.get_by_text("Mock User")).to_be_visible()

    # Intercepting and modifying response
    def modify_response(route):
        response = route.fetch()  # Execute real request
        body = response.json()
        # Modify data
        for user in body:
            user["name"] = user["name"].upper()
        route.fulfill(response=response, json=body)

    page.route("**/api/users", modify_response)

    # Blocking requests (e.g., analytics)
    page.route("**/analytics/**", lambda route: route.abort())
```

::: warning Warning
Mocking API responses is useful for test isolation, but does not replace full integration testing with a real backend.
:::

## Useful Links

- [Official API Testing Documentation](https://playwright.dev/python/docs/api-testing)
- [APIRequestContext API](https://playwright.dev/python/docs/api/class-apirequestcontext)
- [Network interception](https://playwright.dev/python/docs/network)
- [Request mocking](https://playwright.dev/python/docs/mock)
