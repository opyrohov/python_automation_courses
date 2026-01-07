"""Example 4: Mocking Responses

Demonstrates how to return fake/mock responses for API requests.
This is powerful for testing without a real backend.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Mocking Responses Demo ===\n")

    # EXAMPLE 1: Mock JSON response
    print("--- Example 1: Mock JSON response ---")

    mock_user = {
        "id": 999,
        "name": "Mock User",
        "email": "mock@test.com",
        "role": "admin"
    }

    def mock_user_api(route):
        print(f"  Mocking response for: {route.request.url}")
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_user)
        )

    page.route("**/api/user**", mock_user_api)
    print(f"  Mock user data: {mock_user}")
    print("  ✓ User API mock registered")

    # EXAMPLE 2: Mock HTML response
    print("\n--- Example 2: Mock HTML response ---")

    mock_html = """
    <!DOCTYPE html>
    <html>
    <head><title>Mocked Page</title></head>
    <body>
        <h1>This is a mocked page!</h1>
        <p>The real page was intercepted and replaced.</p>
        <div id="mock-indicator">MOCKED</div>
    </body>
    </html>
    """

    def mock_page(route):
        if route.request.resource_type == "document":
            print(f"  Mocking HTML for: {route.request.url}")
            route.fulfill(
                status=200,
                content_type="text/html",
                body=mock_html
            )
        else:
            route.continue_()

    page.route("**/broken_images", mock_page)

    page.goto("https://the-internet.herokuapp.com/broken_images")
    title = page.title()
    print(f"  Page title: {title}")

    mock_text = page.locator("#mock-indicator").text_content()
    print(f"  Mock indicator: {mock_text}")

    page.unroute("**/broken_images")

    # EXAMPLE 3: Simulate error responses
    print("\n--- Example 3: Simulate error responses ---")

    page.goto("https://the-internet.herokuapp.com/")

    # 404 Not Found
    def mock_404(route):
        print(f"  Returning 404 for: {route.request.url}")
        route.fulfill(
            status=404,
            content_type="application/json",
            body='{"error": "Not Found", "message": "Resource does not exist"}'
        )

    page.route("**/api/missing**", mock_404)

    # 500 Internal Server Error
    def mock_500(route):
        print(f"  Returning 500 for: {route.request.url}")
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error": "Internal Server Error", "message": "Something went wrong"}'
        )

    page.route("**/api/broken**", mock_500)

    # 401 Unauthorized
    def mock_401(route):
        print(f"  Returning 401 for: {route.request.url}")
        route.fulfill(
            status=401,
            content_type="application/json",
            body='{"error": "Unauthorized", "message": "Invalid or expired token"}'
        )

    page.route("**/api/protected**", mock_401)

    print("  ✓ Error mocks registered (404, 500, 401)")

    # EXAMPLE 4: Delayed response (simulate slow server)
    print("\n--- Example 4: Delayed response ---")
    import time

    def slow_response(route):
        print(f"  Delaying response for 2 seconds...")
        time.sleep(2)
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"data": "This took a while!"}'
        )

    page.route("**/api/slow**", slow_response)
    print("  ✓ Slow response mock registered")

    # EXAMPLE 5: Mock with different data based on request
    print("\n--- Example 5: Dynamic mock based on request ---")

    def dynamic_mock(route):
        url = route.request.url

        if "id=1" in url:
            data = {"id": 1, "name": "Product A", "price": 29.99}
        elif "id=2" in url:
            data = {"id": 2, "name": "Product B", "price": 49.99}
        else:
            data = {"error": "Product not found"}

        print(f"  Dynamic mock for: {url}")
        print(f"  Returning: {data}")

        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(data)
        )

    page.route("**/api/product**", dynamic_mock)
    print("  ✓ Dynamic product mock registered")

    # EXAMPLE 6: Mock response from file
    print("\n--- Example 6: Mock from file (conceptual) ---")

    def mock_from_file(route):
        # In real use: route.fulfill(path="mocks/data.json")
        print(f"  Would load mock from file for: {route.request.url}")
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"source": "file", "data": [1, 2, 3]}'
        )

    page.route("**/api/file-data**", mock_from_file)
    print("  ✓ File-based mock registered")
    print("  Usage: route.fulfill(path='mocks/response.json')")

    # Clean up all routes
    print("\n--- Cleanup ---")
    page.unroute("**/*")
    print("  All routes cleared")

    print("\n=== Demo Complete ===")
    print("\nMocking benefits:")
    print("  - Test without real backend")
    print("  - Test error handling (404, 500, etc.)")
    print("  - Test loading states (delayed responses)")
    print("  - Consistent test data")
    print("  - Faster tests (no network latency)")

    context.close()
    browser.close()
