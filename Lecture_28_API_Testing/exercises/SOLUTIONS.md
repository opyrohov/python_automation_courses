# Solutions - Lecture 28: API Testing with Playwright

## Exercise 1: Basic API Operations

```python
"""Exercise 1 Solution: Basic API Operations"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("=== Exercise 1: API Basics ===\n")

    # Create API context
    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    print("1. Created API context")

    # GET all posts
    response = api.get("/posts")
    assert response.ok, f"GET /posts failed: {response.status}"
    posts = response.json()
    print(f"\n2. GET /posts - Total posts: {len(posts)}")

    # GET single post
    response = api.get("/posts/1")
    assert response.ok, f"GET /posts/1 failed: {response.status}"
    post = response.json()
    print(f"\n3. GET /posts/1")
    print(f"   Title: {post['title'][:50]}...")
    print(f"   User ID: {post['userId']}")

    # POST new post
    new_post_data = {
        "title": "My Test Post",
        "body": "Test content created via API",
        "userId": 1
    }
    response = api.post("/posts", data=new_post_data)
    assert response.status == 201, f"POST failed: {response.status}"
    created_post = response.json()
    print(f"\n4. POST /posts")
    print(f"   Status: {response.status}")
    print(f"   Created ID: {created_post.get('id')}")
    print(f"   Title: {created_post.get('title')}")

    # PUT update post
    updated_data = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1
    }
    response = api.put("/posts/1", data=updated_data)
    assert response.ok, f"PUT failed: {response.status}"
    updated_post = response.json()
    print(f"\n5. PUT /posts/1")
    print(f"   Status: {response.status}")
    print(f"   Updated title: {updated_post.get('title')}")

    # DELETE post
    response = api.delete("/posts/1")
    assert response.ok, f"DELETE failed: {response.status}"
    print(f"\n6. DELETE /posts/1")
    print(f"   Status: {response.status}")
    print(f"   OK: {response.ok}")

    # BONUS: Get posts by userId
    response = api.get("/posts", params={"userId": 1, "_limit": 5})
    user_posts = response.json()
    print(f"\n7. BONUS: Posts by userId=1: {len(user_posts)}")

    # Dispose context
    api.dispose()
    print("\n8. Context disposed")

    print("\n✓ Exercise 1 completed successfully!")
```

### Key Points:
- Always check `response.ok` or `response.status` for errors
- Use `params={}` for query parameters in GET requests
- POST returns 201 Created, others return 200 OK
- Don't forget to dispose the context

---

## Exercise 2: Combined UI and API Test

```python
"""Exercise 2 Solution: Combined UI and API Test"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    print("=== Exercise 2: Combined UI + API Test ===\n")

    # Create API context
    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    print("1. Created API context")

    # Create browser and page
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    print("2. Created browser and page")

    # Get user data via API (setup/preparation)
    response = api.get("/users/1")
    assert response.ok
    user = response.json()
    print(f"\n3. API: Got user data")
    print(f"   Name: {user['name']}")
    print(f"   Email: {user['email']}")

    # Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print(f"\n4. UI: Navigated to login page")

    # Perform login
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    print("5. UI: Submitted login form")

    # Verify login in UI
    page.wait_for_url("**/secure")
    expect(page.locator(".flash.success")).to_be_visible()
    print("6. UI: ✓ Login successful!")

    # Check secure page content
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("7. UI: ✓ On secure page")

    # API verification - get additional data
    response = api.get("/posts/1")
    post = response.json()
    print(f"\n8. API: Verified backend accessible")
    print(f"   Post title: {post['title'][:40]}...")

    # Get user's posts
    response = api.get("/users/1/posts")
    user_posts = response.json()
    print(f"   User has {len(user_posts)} posts")

    # BONUS: Create test data via API
    print("\n--- BONUS: Test Data Setup ---")
    response = api.post("/posts", data={
        "title": "Test Post for UI",
        "body": "Created during test",
        "userId": 1
    })
    test_post = response.json()
    print(f"Created test post ID: {test_post.get('id')}")

    # BONUS: Cleanup via API
    api.delete(f"/posts/{test_post.get('id', 101)}")
    print("Cleaned up test data")

    # Cleanup
    api.dispose()
    context.close()
    browser.close()
    print("\n9. Cleaned up all resources")

    print("\n✓ Exercise 2 completed successfully!")
```

### Key Points:
- Create both API and browser contexts at the start
- Use API for fast setup and verification
- Use UI for actual user flow testing
- Clean up both contexts at the end

---

## Bonus Challenges

### Challenge 1: API Test Helper Class

```python
"""Bonus: Reusable API Test Helper"""
from playwright.sync_api import sync_playwright

class APIClient:
    def __init__(self, playwright, base_url):
        self.api = playwright.request.new_context(base_url=base_url)

    def get(self, path, **kwargs):
        response = self.api.get(path, **kwargs)
        self._log_request("GET", path, response)
        return response

    def post(self, path, data=None, **kwargs):
        response = self.api.post(path, data=data, **kwargs)
        self._log_request("POST", path, response)
        return response

    def put(self, path, data=None, **kwargs):
        response = self.api.put(path, data=data, **kwargs)
        self._log_request("PUT", path, response)
        return response

    def delete(self, path, **kwargs):
        response = self.api.delete(path, **kwargs)
        self._log_request("DELETE", path, response)
        return response

    def _log_request(self, method, path, response):
        status = "✓" if response.ok else "✗"
        print(f"  {status} {method} {path} -> {response.status}")

    def dispose(self):
        self.api.dispose()

# Usage
with sync_playwright() as p:
    client = APIClient(p, "https://jsonplaceholder.typicode.com")

    # All requests are logged automatically
    client.get("/posts/1")
    client.post("/posts", data={"title": "Test"})
    client.delete("/posts/1")

    client.dispose()
```

### Challenge 2: Auth Token Flow

```python
"""Bonus: Complete Auth Flow"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Step 1: Get auth token via API
    auth_api = p.request.new_context(
        base_url="https://api.example.com"  # Replace with real API
    )

    # Login to get token (example structure)
    # response = auth_api.post("/auth/login", data={
    #     "email": "test@example.com",
    #     "password": "password123"
    # })
    # token = response.json()["access_token"]

    token = "fake-token-for-demo"

    auth_api.dispose()

    # Step 2: Create authenticated API context
    api = p.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Authorization": f"Bearer {token}"
        }
    )

    # Step 3: Create authenticated browser context
    browser = p.chromium.launch()
    context = browser.new_context(
        extra_http_headers={
            "Authorization": f"Bearer {token}"
        }
    )
    page = context.new_page()

    # Now both API and browser share the same auth!

    api.dispose()
    browser.close()
```

### Challenge 3: Response Validator

```python
"""Bonus: JSON Schema Validation"""
from playwright.sync_api import sync_playwright

def validate_post(data):
    """Validate post structure."""
    required = ["id", "title", "body", "userId"]
    for field in required:
        assert field in data, f"Missing: {field}"

    assert isinstance(data["id"], int), "id must be int"
    assert isinstance(data["title"], str), "title must be str"
    assert len(data["title"]) > 0, "title cannot be empty"

    return True

def validate_user(data):
    """Validate user structure."""
    required = ["id", "name", "email", "username"]
    for field in required:
        assert field in data, f"Missing: {field}"

    assert "@" in data["email"], "Invalid email"

    return True

with sync_playwright() as p:
    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # Validate post
    response = api.get("/posts/1")
    post = response.json()
    validate_post(post)
    print("✓ Post validated")

    # Validate user
    response = api.get("/users/1")
    user = response.json()
    validate_user(user)
    print("✓ User validated")

    api.dispose()
```

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting to dispose
```python
# WRONG - Memory leak
api = p.request.new_context(base_url="...")
response = api.get("/data")
# Forgot api.dispose()!

# CORRECT
api = p.request.new_context(base_url="...")
try:
    response = api.get("/data")
finally:
    api.dispose()
```

### Mistake 2: Not checking response status
```python
# WRONG - Assumes success
response = api.get("/users/999999")
user = response.json()  # Might fail or return error!

# CORRECT
response = api.get("/users/999999")
if response.ok:
    user = response.json()
else:
    print(f"Error: {response.status}")
```

### Mistake 3: Wrong Content-Type for POST
```python
# WRONG - Sending JSON without proper handling
import json
response = api.post("/data", data=json.dumps({"key": "value"}))
# Server might not understand!

# CORRECT - Let Playwright handle it
response = api.post("/data", data={"key": "value"})
# Playwright automatically sets Content-Type: application/json
```
