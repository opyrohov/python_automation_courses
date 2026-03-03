"""Example 5: Waiting for Network Events

Demonstrates how to wait for specific network requests and responses.
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Waiting for Network Events Demo ===\n")

    # EXAMPLE 1: Wait for specific request
    print("--- Example 1: Wait for specific request ---")

    page.goto("https://the-internet.herokuapp.com/login")

    print("  Waiting for login request...")
    with page.expect_request("**/authenticate") as request_info:
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

    request = request_info.value
    print(f"  ✓ Request captured!")
    print(f"    URL: {request.url}")
    print(f"    Method: {request.method}")

    # EXAMPLE 2: Wait for specific response
    print("\n--- Example 2: Wait for specific response ---")

    page.goto("https://the-internet.herokuapp.com/login")

    print("  Waiting for login response...")
    with page.expect_response("**/authenticate") as response_info:
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

    response = response_info.value
    print(f"  ✓ Response captured!")
    print(f"    Status: {response.status}")
    print(f"    URL: {response.url}")

    # EXAMPLE 3: Wait with condition
    print("\n--- Example 3: Wait for response with condition ---")

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    print("  Waiting for successful response...")
    with page.expect_response(
        lambda response: response.status == 200 and "dynamic_loading" in response.url
    ) as response_info:
        page.click("#start button")

    response = response_info.value
    print(f"  ✓ Conditional response captured!")
    print(f"    URL: {response.url}")
    print(f"    Status: {response.status}")

    # Wait for finish element
    page.wait_for_selector("#finish")

    # EXAMPLE 4: Wait for navigation
    print("\n--- Example 4: Wait for navigation request ---")

    page.goto("https://the-internet.herokuapp.com/")

    print("  Clicking link and waiting for navigation...")
    with page.expect_request("**/login") as request_info:
        page.click("a[href='/login']")

    request = request_info.value
    print(f"  ✓ Navigation request captured: {request.url}")

    # EXAMPLE 5: Capture multiple requests
    print("\n--- Example 5: Capture multiple requests ---")

    captured_requests = []

    def capture_all(request):
        if "herokuapp" in request.url:
            captured_requests.append({
                "url": request.url,
                "method": request.method,
                "type": request.resource_type
            })

    page.on("request", capture_all)

    page.goto("https://the-internet.herokuapp.com/")

    print(f"  Captured {len(captured_requests)} requests:")
    for i, req in enumerate(captured_requests[:5], 1):
        print(f"    {i}. [{req['type']}] {req['url'][:50]}...")

    if len(captured_requests) > 5:
        print(f"    ... and {len(captured_requests) - 5} more")

    # EXAMPLE 6: Wait for API response and verify data
    print("\n--- Example 6: Verify response data ---")

    # Set up mock API for demonstration
    page.route("**/api/data", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='{"items": [1, 2, 3], "total": 3}'
    ))

    # In real scenario, you'd interact with page to trigger API call
    # Here we just demonstrate the pattern

    print("  Mock API set up")
    print("  Pattern: expect_response() + response.json()")

    # EXAMPLE 7: Request/Response timing
    print("\n--- Example 7: Measure request timing ---")
    import time

    page.goto("https://the-internet.herokuapp.com/")

    start_time = time.time()

    with page.expect_response("**/slow_resources") as response_info:
        # This would trigger a slow request in real app
        pass  # Skip actual navigation for demo

    # Conceptual - in real use:
    # response = response_info.value
    # elapsed = time.time() - start_time
    # print(f"  Request took: {elapsed:.2f}s")

    print("  Pattern: time.time() before/after expect_response()")

    # EXAMPLE 8: Wait for download
    print("\n--- Example 8: Wait for download (conceptual) ---")

    print("  Pattern:")
    print("  with page.expect_download() as download_info:")
    print("      page.click('#download-btn')")
    print("  download = download_info.value")
    print("  download.save_as('file.pdf')")

    print("\n=== Demo Complete ===")
    print("\nWaiting patterns:")
    print("  - expect_request(pattern) - Wait for request")
    print("  - expect_response(pattern) - Wait for response")
    print("  - expect_response(lambda) - Wait with condition")
    print("  - expect_download() - Wait for file download")
    print("  - on('request/response') - Capture all events")

    context.close()
    browser.close()
