"""Example 3: Modifying Requests

Demonstrates how to modify request headers, URLs, and POST data.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Modifying Requests Demo ===\n")

    # EXAMPLE 1: Add custom headers
    print("--- Example 1: Adding custom headers ---")

    def add_custom_headers(route):
        headers = route.request.headers.copy()
        headers["X-Custom-Header"] = "TestValue123"
        headers["X-Test-Mode"] = "true"
        print(f"  Added custom headers to: {route.request.url[:50]}...")
        route.continue_(headers=headers)

    page.route("**/the-internet.herokuapp.com/**", add_custom_headers)

    page.goto("https://the-internet.herokuapp.com/")
    print("  ✓ Headers added to all requests")

    page.unroute("**/the-internet.herokuapp.com/**")

    # EXAMPLE 2: Add Authorization header
    print("\n--- Example 2: Adding Authorization header ---")

    def add_auth_header(route):
        headers = route.request.headers.copy()
        headers["Authorization"] = "Bearer my-secret-token-123"
        print(f"  Added auth to: {route.request.url}")
        route.continue_(headers=headers)

    # This would work for API requests
    page.route("**/api/**", add_auth_header)
    print("  ✓ Auth header interceptor registered (would apply to /api/* requests)")

    page.unroute("**/api/**")

    # EXAMPLE 3: Modify User-Agent
    print("\n--- Example 3: Modifying User-Agent ---")

    original_ua = None
    modified_ua = "Custom-Bot/1.0 (Playwright Test)"

    def modify_user_agent(route):
        global original_ua
        headers = route.request.headers.copy()
        original_ua = headers.get("user-agent", "Unknown")
        headers["user-agent"] = modified_ua
        route.continue_(headers=headers)

    page.route("**/*", modify_user_agent)

    page.goto("https://the-internet.herokuapp.com/")

    print(f"  Original UA: {original_ua[:50]}...")
    print(f"  Modified UA: {modified_ua}")

    page.unroute("**/*")

    # EXAMPLE 4: URL redirection
    print("\n--- Example 4: URL redirection ---")

    def redirect_url(route):
        original_url = route.request.url
        # Redirect /broken_images to home page
        if "broken_images" in original_url:
            new_url = "https://the-internet.herokuapp.com/"
            print(f"  Redirecting: {original_url}")
            print(f"  To: {new_url}")
            route.continue_(url=new_url)
        else:
            route.continue_()

    page.route("**/*", redirect_url)

    page.goto("https://the-internet.herokuapp.com/broken_images")
    current_url = page.url
    print(f"  Current URL: {current_url}")

    page.unroute("**/*")

    # EXAMPLE 5: Log and inspect POST data
    print("\n--- Example 5: Inspecting POST data ---")

    def inspect_post(route):
        request = route.request
        if request.method == "POST":
            print(f"  POST to: {request.url}")
            print(f"  Content-Type: {request.headers.get('content-type', 'N/A')}")
            if request.post_data:
                print(f"  Body: {request.post_data[:100]}")
        route.continue_()

    page.route("**/*", inspect_post)

    # Navigate to login page and submit form
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    page.unroute("**/*")

    # EXAMPLE 6: Modify POST data
    print("\n--- Example 6: Modifying POST data (conceptual) ---")

    def modify_post_data(route):
        request = route.request
        if request.method == "POST" and request.post_data:
            # Parse and modify
            try:
                # For JSON data
                data = json.loads(request.post_data)
                data["modified"] = True
                data["timestamp"] = "2024-01-01"
                modified_body = json.dumps(data)
                print(f"  Modified POST data: {modified_body[:50]}...")
                route.continue_(post_data=modified_body)
            except json.JSONDecodeError:
                # For form data, just pass through
                route.continue_()
        else:
            route.continue_()

    print("  (Interceptor ready for JSON POST requests)")

    print("\n=== Demo Complete ===")
    print("\nModification use cases:")
    print("  - Add authentication headers")
    print("  - Modify API request bodies")
    print("  - Change User-Agent for testing")
    print("  - Redirect URLs for testing")
    print("  - Add tracking/debugging headers")

    context.close()
    browser.close()
