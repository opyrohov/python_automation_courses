"""Example 1: Monitoring Network Requests

Demonstrates how to listen to and log network traffic in Playwright.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print("=== Monitoring Network Requests Demo ===\n")

    # Track request counts
    request_count = 0
    response_count = 0

    # Listen to all requests
    def on_request(request):
        global request_count
        request_count += 1
        print(f">> [{request.method}] {request.url[:80]}...")
        print(f"   Type: {request.resource_type}")

    # Listen to all responses
    def on_response(response):
        global response_count
        response_count += 1
        status_emoji = "✓" if response.status < 400 else "✗"
        print(f"<< {status_emoji} [{response.status}] {response.url[:80]}...")

    # Listen to failed requests
    def on_request_failed(request):
        print(f"!! FAILED: {request.url}")
        print(f"   Error: {request.failure}")

    # Register event handlers
    page.on("request", on_request)
    page.on("response", on_response)
    page.on("requestfailed", on_request_failed)

    print("1. Navigating to page...\n")
    page.goto("https://the-internet.herokuapp.com/")

    print(f"\n--- Summary ---")
    print(f"Total requests: {request_count}")
    print(f"Total responses: {response_count}")

    # Navigate to another page to see more requests
    print("\n2. Navigating to dynamic loading page...\n")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    print(f"\n--- Updated Summary ---")
    print(f"Total requests: {request_count}")
    print(f"Total responses: {response_count}")

    # Click button to trigger XHR
    print("\n3. Clicking Start button to trigger XHR...\n")
    page.click("#start button")
    page.wait_for_selector("#finish")

    print(f"\n--- Final Summary ---")
    print(f"Total requests: {request_count}")
    print(f"Total responses: {response_count}")

    print("\n=== Demo Complete ===")
    browser.close()
