"""Example 1: HTTP Basic Authentication"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== HTTP Basic Authentication Demo ===\n")

    # Method 1: Credentials in URL
    print("1. Method 1: Credentials in URL")
    page = browser.new_page()
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    # Verify we're authenticated
    expect(page.locator("p")).to_contain_text("Congratulations")
    print("   ✓ Successfully authenticated via URL credentials")
    page.close()

    # Method 2: Using http_credentials context option (Recommended)
    print("\n2. Method 2: http_credentials option")
    context = browser.new_context(
        http_credentials={
            "username": "admin",
            "password": "admin"
        }
    )
    page = context.new_page()

    # Navigate without credentials in URL
    page.goto("https://the-internet.herokuapp.com/basic_auth")

    # Verify authentication
    expect(page.locator("p")).to_contain_text("Congratulations")
    print("   ✓ Successfully authenticated via http_credentials")

    # Get the success message
    message = page.locator("p").text_content()
    print(f"   Message: {message}")

    context.close()

    # Method 3: Wrong credentials (to show failure)
    print("\n3. Testing with wrong credentials")
    context = browser.new_context(
        http_credentials={
            "username": "wrong",
            "password": "wrong"
        }
    )
    page = context.new_page()

    # This will fail - we'll get 401 error
    response = page.goto("https://the-internet.herokuapp.com/basic_auth")
    print(f"   Response status: {response.status}")

    if response.status == 401:
        print("   ✓ Got 401 Unauthorized as expected")
    else:
        print("   Unexpected response")

    context.close()

    print("\n=== Demo Complete ===")
    browser.close()
