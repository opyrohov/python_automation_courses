# Lecture 28: API Testing with Playwright

## Overview
Learn how to make API requests directly with Playwright without a browser. This is faster than UI testing and perfect for backend validation, test data setup, and combining API with UI tests.

## Topics Covered

### 1. Creating API Request Context
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create API context (no browser needed!)
    api = p.request.new_context(
        base_url="https://api.example.com"
    )

    # Make requests
    response = api.get("/users")
    print(response.json())

    # Dispose when done
    api.dispose()
```

### 2. GET Requests
```python
# Simple GET
response = api.get("/users")
print(response.status)  # 200
print(response.json())  # [{"id": 1, "name": "John"}, ...]

# GET with query parameters
response = api.get("/users", params={
    "page": 1,
    "limit": 10,
    "sort": "name"
})

# GET with headers
response = api.get("/users", headers={
    "Authorization": "Bearer token123"
})
```

### 3. POST Requests
```python
# POST JSON data
response = api.post("/users", data={
    "name": "John Doe",
    "email": "john@example.com"
})

# POST with explicit JSON
import json
response = api.post("/users",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"name": "John"})
)

# POST form data
response = api.post("/login", form={
    "username": "admin",
    "password": "secret"
})
```

### 4. PUT/PATCH/DELETE Requests
```python
# PUT - full update
response = api.put("/users/1", data={
    "name": "John Updated",
    "email": "john.new@example.com"
})

# PATCH - partial update
response = api.patch("/users/1", data={
    "name": "John Patched"
})

# DELETE
response = api.delete("/users/1")
print(response.status)  # 204 No Content
```

### 5. Response Handling
```python
response = api.get("/users/1")

# Status and headers
print(response.status)           # 200
print(response.status_text)      # "OK"
print(response.headers)          # dict of headers
print(response.ok)               # True if status 200-299

# Body
print(response.text())           # Raw text
print(response.json())           # Parsed JSON
print(response.body())           # Raw bytes

# Check specific header
content_type = response.headers.get("content-type")
```

### 6. Authentication
```python
# Bearer token
api = p.request.new_context(
    base_url="https://api.example.com",
    extra_http_headers={
        "Authorization": "Bearer your-token-here"
    }
)

# Basic auth
import base64
credentials = base64.b64encode(b"user:password").decode()
api = p.request.new_context(
    extra_http_headers={
        "Authorization": f"Basic {credentials}"
    }
)

# API Key
api = p.request.new_context(
    extra_http_headers={
        "X-API-Key": "your-api-key"
    }
)
```

### 7. Combining UI and API Tests
```python
# Setup: Create test data via API
api = p.request.new_context(base_url="https://api.example.com")
response = api.post("/users", data={"name": "Test User"})
user_id = response.json()["id"]

# Test: Verify in UI
browser = p.chromium.launch()
page = browser.new_page()
page.goto(f"https://example.com/users/{user_id}")
expect(page.locator(".user-name")).to_have_text("Test User")

# Cleanup: Delete via API
api.delete(f"/users/{user_id}")
```

### 8. API Response Assertions
```python
from playwright.sync_api import expect

response = api.get("/users/1")

# Assert status
assert response.status == 200
assert response.ok

# Assert JSON structure
data = response.json()
assert "id" in data
assert "name" in data
assert data["id"] == 1

# Assert with expect (Playwright style)
expect(response).to_be_ok()
```

## Common Use Cases

### 1. Test Data Setup
```python
def create_test_user(api):
    response = api.post("/users", data={
        "name": "Test User",
        "email": f"test_{time.time()}@example.com"
    })
    return response.json()["id"]

# Use in test
user_id = create_test_user(api)
page.goto(f"/users/{user_id}")
```

### 2. Skip Login via API
```python
# Get auth token via API
response = api.post("/auth/login", data={
    "username": "admin",
    "password": "secret"
})
token = response.json()["token"]

# Use token in browser
context = browser.new_context(
    extra_http_headers={"Authorization": f"Bearer {token}"}
)
```

### 3. Verify Backend State
```python
# UI action
page.fill("#name", "New Name")
page.click("#save")

# Verify via API
response = api.get(f"/users/{user_id}")
assert response.json()["name"] == "New Name"
```

## Files in This Lecture

### Examples
- `01_basic_requests.py` - GET, POST, PUT, DELETE basics
- `02_authentication.py` - Auth headers, tokens, API keys
- `03_response_handling.py` - Status, headers, body parsing
- `04_crud_operations.py` - Complete CRUD example
- `05_ui_api_combined.py` - Combining API and UI tests

### Exercises
- `exercise_01_api_basics.py` - Basic API operations
- `exercise_02_ui_api_test.py` - Combined UI and API test
- `SOLUTIONS.md` - Complete solutions

## Quick Reference

```python
# Create context
api = p.request.new_context(base_url="https://api.example.com")

# Methods
api.get(url, params={}, headers={})
api.post(url, data={}, form={}, headers={})
api.put(url, data={})
api.patch(url, data={})
api.delete(url)

# Response
response.status          # HTTP status code
response.ok              # True if 2xx
response.json()          # Parse JSON body
response.text()          # Raw text body
response.headers         # Response headers

# Cleanup
api.dispose()
```

## Benefits of API Testing

| Aspect | UI Testing | API Testing |
|--------|-----------|-------------|
| Speed | Slow (browser) | Fast (no browser) |
| Stability | Flaky (UI changes) | Stable (contract) |
| Coverage | User flows | Backend logic |
| Setup | Complex | Simple |
| Best for | E2E validation | Data setup, backend |
