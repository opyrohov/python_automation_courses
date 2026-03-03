# Lecture 27: Network Interception

## Overview
Learn how to intercept, monitor, modify, and mock network requests in Playwright. Essential for testing API interactions, simulating error conditions, and improving test performance.

## Topics Covered

### 1. Monitoring Network Requests
```python
# Listen to all requests
page.on("request", lambda req: print(f">> {req.method} {req.url}"))

# Listen to all responses
page.on("response", lambda res: print(f"<< {res.status} {res.url}"))

# Listen to request failures
page.on("requestfailed", lambda req: print(f"!! Failed: {req.url}"))

# Listen to request finished
page.on("requestfinished", lambda req: print(f"✓ Done: {req.url}"))
```

### 2. Request Object Properties
```python
def log_request(request):
    print(f"URL: {request.url}")
    print(f"Method: {request.method}")
    print(f"Headers: {request.headers}")
    print(f"Post Data: {request.post_data}")
    print(f"Resource Type: {request.resource_type}")
    # Types: document, stylesheet, image, script, xhr, fetch, etc.

page.on("request", log_request)
```

### 3. Response Object Properties
```python
def log_response(response):
    print(f"URL: {response.url}")
    print(f"Status: {response.status}")
    print(f"Status Text: {response.status_text}")
    print(f"Headers: {response.headers}")

    # Get response body (async in sync API)
    if "application/json" in response.headers.get("content-type", ""):
        body = response.json()
        print(f"JSON Body: {body}")

page.on("response", log_response)
```

### 4. Route Interception
```python
# Intercept all requests matching pattern
def handle_route(route):
    print(f"Intercepted: {route.request.url}")
    route.continue_()  # Let it through

page.route("**/*", handle_route)

# Intercept specific URLs
page.route("**/api/**", handle_api)
page.route("**/*.png", handle_images)
```

### 5. Blocking Requests
```python
# Block all images
page.route("**/*.{png,jpg,jpeg,gif,svg}", lambda route: route.abort())

# Block specific domains
page.route("**/ads.example.com/**", lambda route: route.abort())

# Block by resource type
def block_by_type(route):
    if route.request.resource_type in ["image", "stylesheet", "font"]:
        route.abort()
    else:
        route.continue_()

page.route("**/*", block_by_type)
```

### 6. Modifying Requests
```python
# Modify headers
def add_auth_header(route):
    headers = route.request.headers.copy()
    headers["Authorization"] = "Bearer token123"
    route.continue_(headers=headers)

page.route("**/api/**", add_auth_header)

# Modify POST data
def modify_post_data(route):
    post_data = route.request.post_data
    modified = post_data.replace("old", "new")
    route.continue_(post_data=modified)

page.route("**/submit", modify_post_data)
```

### 7. Mocking Responses
```python
# Return mock JSON response
def mock_api(route):
    route.fulfill(
        status=200,
        content_type="application/json",
        body='{"id": 1, "name": "Mock User"}'
    )

page.route("**/api/user", mock_api)

# Return mock from file
def mock_from_file(route):
    route.fulfill(path="mocks/response.json")

page.route("**/api/data", mock_from_file)

# Simulate error
def mock_error(route):
    route.fulfill(status=500, body="Internal Server Error")

page.route("**/api/flaky", mock_error)
```

### 8. Waiting for Network Events
```python
# Wait for specific request
with page.expect_request("**/api/login") as request_info:
    page.click("#login-btn")
request = request_info.value
print(f"Login request sent: {request.post_data}")

# Wait for specific response
with page.expect_response("**/api/login") as response_info:
    page.click("#login-btn")
response = response_info.value
print(f"Login response: {response.status}")

# Wait for response with condition
with page.expect_response(
    lambda res: "api/data" in res.url and res.status == 200
) as response_info:
    page.click("#load-data")
```

## Common Use Cases

### 1. Speed Up Tests by Blocking Resources
```python
# Block unnecessary resources
page.route("**/*.{png,jpg,jpeg,gif,svg,woff,woff2}", lambda r: r.abort())
page.route("**/analytics.js", lambda r: r.abort())
page.route("**/ads/**", lambda r: r.abort())
```

### 2. Test Error Handling
```python
# Simulate 500 error
page.route("**/api/submit", lambda r: r.fulfill(status=500))
page.click("#submit")
expect(page.locator(".error-message")).to_be_visible()

# Simulate network failure
page.route("**/api/data", lambda r: r.abort("failed"))
```

### 3. Test Loading States
```python
# Delay response
def slow_response(route):
    time.sleep(3)  # Simulate slow server
    route.continue_()

page.route("**/api/data", slow_response)
page.click("#load")
expect(page.locator(".loading-spinner")).to_be_visible()
```

### 4. Mock API for Isolated Tests
```python
# Mock user data
page.route("**/api/user", lambda r: r.fulfill(
    status=200,
    content_type="application/json",
    body='{"id": 1, "name": "Test User", "role": "admin"}'
))

page.goto("/dashboard")
expect(page.locator(".user-name")).to_have_text("Test User")
```

## Files in This Lecture

### Examples
- `01_monitoring_requests.py` - Logging network traffic
- `02_blocking_requests.py` - Blocking images, ads, scripts
- `03_modifying_requests.py` - Adding headers, changing data
- `04_mocking_responses.py` - Returning fake API responses
- `05_waiting_network.py` - Waiting for specific requests/responses

### Exercises
- `exercise_01_block_and_mock.py` - Block resources and mock APIs
- `exercise_02_test_error_handling.py` - Test app error scenarios
- `SOLUTIONS.md` - Complete solutions

## Quick Reference

```python
# Event listeners
page.on("request", handler)
page.on("response", handler)
page.on("requestfailed", handler)
page.on("requestfinished", handler)

# Route interception
page.route(pattern, handler)
page.unroute(pattern)

# Route handler actions
route.continue_()                    # Let request through
route.continue_(headers={...})       # Modify and continue
route.abort()                        # Block request
route.abort("failed")                # Simulate network error
route.fulfill(status=200, body="")   # Return mock response
route.fulfill(path="file.json")      # Return file contents

# Wait for network
page.expect_request(pattern)
page.expect_response(pattern)
page.expect_response(lambda r: condition)

# Request properties
request.url
request.method
request.headers
request.post_data
request.resource_type

# Response properties
response.url
response.status
response.status_text
response.headers
response.json()
response.text()
response.body()
```
