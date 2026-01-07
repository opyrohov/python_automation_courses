# Solutions - Lecture 27: Network Interception

## Exercise 1: Block Resources and Mock APIs

```python
"""Exercise 1 Solution: Block Resources and Mock APIs"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Block and Mock ===\n")

    blocked_images = 0

    # Block images handler
    def block_images(route):
        global blocked_images
        blocked_images += 1
        print(f"  Blocked image: {route.request.url[:50]}...")
        route.abort()

    # Register route to block images
    page.route("**/*.{png,jpg,jpeg,gif,svg,ico,webp}", block_images)
    print("1. Image blocking enabled")

    # Navigate to page
    page.goto("https://the-internet.herokuapp.com/")
    print(f"\n2. Images blocked: {blocked_images}")

    # Create mock for /api/user
    mock_user = {"id": 1, "name": "Test User", "premium": True}

    def mock_user_api(route):
        print(f"  Mocking /api/user request")
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_user)
        )

    page.route("**/api/user**", mock_user_api)
    print(f"\n3. Mock configured for /api/user")
    print(f"   Response: {mock_user}")

    # BONUS: Block external domains
    def block_external(route):
        url = route.request.url
        if "herokuapp.com" not in url:
            print(f"  Blocked external: {url[:50]}...")
            route.abort()
        else:
            route.continue_()

    page.route("**/*", block_external)
    print("\n4. External domain blocking enabled")

    # BONUS: Dynamic mock based on query params
    def dynamic_product_mock(route):
        url = route.request.url
        if "id=1" in url:
            data = {"id": 1, "name": "Basic Plan", "price": 9.99}
        elif "id=2" in url:
            data = {"id": 2, "name": "Pro Plan", "price": 19.99}
        elif "id=3" in url:
            data = {"id": 3, "name": "Enterprise", "price": 99.99}
        else:
            data = {"error": "Product not found"}

        route.fulfill(
            status=200 if "error" not in data else 404,
            content_type="application/json",
            body=json.dumps(data)
        )

    page.route("**/api/product**", dynamic_product_mock)
    print("\n5. Dynamic product mock enabled")

    # BONUS: Simulate 500 error
    def mock_500(route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error": "Internal Server Error"}'
        )

    page.route("**/api/crash", mock_500)
    print("6. Error simulation enabled for /api/crash")

    print("\n✓ Exercise 1 completed!")
    context.close()
    browser.close()
```

### Key Points:
- Use `route.abort()` to block requests
- Use `route.fulfill()` to return mock responses
- Pattern `**/*.{ext1,ext2}` matches multiple extensions
- Check URL content for dynamic responses

---

## Exercise 2: Test Error Handling

```python
"""Exercise 2 Solution: Test Error Handling"""
from playwright.sync_api import sync_playwright
import json
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 2: Test Error Handling ===\n")

    # 404 Not Found mock
    def mock_404(route):
        print("  Returning 404 Not Found")
        route.fulfill(
            status=404,
            content_type="application/json",
            body=json.dumps({
                "error": "Not Found",
                "message": "The requested resource does not exist",
                "code": 404
            })
        )

    page.route("**/api/not-found**", mock_404)
    print("1. 404 mock registered for /api/not-found")

    # 500 Internal Server Error mock
    def mock_500(route):
        print("  Returning 500 Internal Server Error")
        route.fulfill(
            status=500,
            content_type="application/json",
            body=json.dumps({
                "error": "Internal Server Error",
                "message": "An unexpected error occurred",
                "code": 500
            })
        )

    page.route("**/api/server-error**", mock_500)
    print("2. 500 mock registered for /api/server-error")

    # 401 Unauthorized mock
    def mock_401(route):
        print("  Returning 401 Unauthorized")
        route.fulfill(
            status=401,
            content_type="application/json",
            body=json.dumps({
                "error": "Unauthorized",
                "message": "Authentication required",
                "code": 401
            })
        )

    page.route("**/api/unauthorized**", mock_401)
    print("3. 401 mock registered for /api/unauthorized")

    # 403 Forbidden mock
    def mock_403(route):
        print("  Returning 403 Forbidden")
        route.fulfill(
            status=403,
            content_type="application/json",
            body=json.dumps({
                "error": "Forbidden",
                "message": "You don't have permission to access this resource",
                "code": 403
            })
        )

    page.route("**/api/forbidden**", mock_403)
    print("4. 403 mock registered for /api/forbidden")

    # Navigate to page
    page.goto("https://the-internet.herokuapp.com/")
    print("\n5. Navigated to test page")

    # BONUS: Slow response (2 seconds)
    def slow_response(route):
        print("  Delaying response for 2 seconds...")
        time.sleep(2)
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({
                "message": "This response was delayed",
                "delay": 2000
            })
        )

    page.route("**/api/slow**", slow_response)
    print("\n6. Slow response mock registered (2s delay)")

    # BONUS: Network failure
    def network_failure(route):
        print("  Simulating network failure")
        route.abort("failed")

    page.route("**/api/offline**", network_failure)
    print("7. Network failure mock registered")

    # BONUS: Timeout simulation
    def timeout_response(route):
        print("  Simulating timeout (10 seconds)...")
        time.sleep(10)  # Longer than typical timeout
        route.fulfill(status=200, body='{"late": true}')

    page.route("**/api/timeout**", timeout_response)
    print("8. Timeout simulation registered")

    # Verify mocks with expect_response
    print("\n--- Verification ---")

    # Test that we can capture mock responses
    print("\nAll error mocks configured:")
    print("  /api/not-found -> 404 Not Found")
    print("  /api/server-error -> 500 Internal Server Error")
    print("  /api/unauthorized -> 401 Unauthorized")
    print("  /api/forbidden -> 403 Forbidden")
    print("  /api/slow -> 200 (2s delay)")
    print("  /api/offline -> Network failure")
    print("  /api/timeout -> Timeout simulation")

    print("\n✓ Exercise 2 completed!")
    context.close()
    browser.close()
```

### Key Points:
- Use `route.fulfill(status=XXX)` for HTTP errors
- Include proper JSON error bodies for realistic testing
- Use `time.sleep()` inside handler for delayed responses
- Use `route.abort("failed")` for network failures

---

## Bonus Challenges

### Challenge 1: Complete Request Logger

```python
"""Bonus: Complete request/response logger"""
from playwright.sync_api import sync_playwright
import json

def create_logger():
    logs = []

    def log_request(request):
        logs.append({
            "type": "request",
            "url": request.url,
            "method": request.method,
            "resource_type": request.resource_type,
            "headers": dict(request.headers)
        })

    def log_response(response):
        logs.append({
            "type": "response",
            "url": response.url,
            "status": response.status,
            "headers": dict(response.headers)
        })

    def get_logs():
        return logs

    def save_logs(filename):
        with open(filename, "w") as f:
            json.dump(logs, f, indent=2)

    return log_request, log_response, get_logs, save_logs

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    log_req, log_res, get_logs, save_logs = create_logger()

    page.on("request", log_req)
    page.on("response", log_res)

    page.goto("https://example.com")

    # Save all network logs
    save_logs("network_log.json")
    print(f"Logged {len(get_logs())} network events")

    browser.close()
```

### Challenge 2: API Response Validator

```python
"""Bonus: Validate API responses match schema"""
from playwright.sync_api import sync_playwright

def validate_user_response(response):
    if "/api/user" in response.url and response.status == 200:
        try:
            data = response.json()
            required_fields = ["id", "name", "email"]

            for field in required_fields:
                if field not in data:
                    print(f"❌ Missing field: {field}")
                    return False

            print(f"✓ User response valid: {data}")
            return True
        except:
            print("❌ Invalid JSON response")
            return False

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.on("response", validate_user_response)

    # Mock valid response
    page.route("**/api/user", lambda r: r.fulfill(
        status=200,
        content_type="application/json",
        body='{"id": 1, "name": "Test", "email": "test@test.com"}'
    ))

    page.goto("https://example.com")
    browser.close()
```

### Challenge 3: Performance Monitor

```python
"""Bonus: Monitor slow requests"""
from playwright.sync_api import sync_playwright
import time

slow_requests = []
request_times = {}

def on_request(request):
    request_times[request.url] = time.time()

def on_response(response):
    url = response.url
    if url in request_times:
        duration = time.time() - request_times[url]
        if duration > 1.0:  # Slower than 1 second
            slow_requests.append({
                "url": url,
                "duration": round(duration, 2),
                "status": response.status
            })
            print(f"⚠️ Slow request: {url[:50]}... ({duration:.2f}s)")
        del request_times[url]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.on("request", on_request)
    page.on("response", on_response)

    page.goto("https://example.com")

    print(f"\nSlow requests: {len(slow_requests)}")
    for req in slow_requests:
        print(f"  {req['duration']}s - {req['url'][:60]}")

    browser.close()
```

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting route.continue_()
```python
# WRONG - Request hangs forever
def handler(route):
    print(f"Intercepted: {route.request.url}")
    # Forgot to call continue_(), abort(), or fulfill()!

# CORRECT - Always handle the route
def handler(route):
    print(f"Intercepted: {route.request.url}")
    route.continue_()  # Let it through
```

### Mistake 2: Wrong pattern syntax
```python
# WRONG - Missing **
page.route("/api/user", handler)  # Won't match!

# CORRECT - Use ** for any path prefix
page.route("**/api/user", handler)

# CORRECT - Match domain too
page.route("*://example.com/api/**", handler)
```

### Mistake 3: Not removing routes
```python
# WRONG - Routes accumulate
page.route("**/*", handler1)
page.goto(url1)
page.route("**/*", handler2)  # Now BOTH handlers run!
page.goto(url2)

# CORRECT - Remove previous routes
page.route("**/*", handler1)
page.goto(url1)
page.unroute("**/*")  # Remove old route
page.route("**/*", handler2)
page.goto(url2)
```

### Mistake 4: Blocking your own requests
```python
# WRONG - Blocks everything including the page itself
page.route("**/*", lambda r: r.abort())
page.goto("https://example.com")  # Error!

# CORRECT - Only block specific resource types
def selective_block(route):
    if route.request.resource_type in ["image", "font"]:
        route.abort()
    else:
        route.continue_()

page.route("**/*", selective_block)
```
