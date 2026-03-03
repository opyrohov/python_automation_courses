"""Example 2: Form-Based Login"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Form-Based Login Demo ===\n")

    # Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print("1. Navigated to login page")

    # Verify we're on login page
    expect(page.locator("h2")).to_have_text("Login Page")
    print("2. Verified login page loaded")

    # Fill in credentials
    page.locator("#username").fill("tomsmith")
    print("3. Entered username")

    page.locator("#password").fill("SuperSecretPassword!")
    print("4. Entered password")

    # Click login button
    page.locator("button[type='submit']").click()
    print("5. Clicked login button")

    # Wait for navigation to complete
    page.wait_for_url("**/secure")
    print("6. Navigated to secure page")

    # Verify successful login
    success_message = page.locator(".flash.success")
    expect(success_message).to_be_visible()
    print("7. ✓ Login successful - success message visible")

    # Get the success message text
    message_text = success_message.text_content()
    print(f"   Message: {message_text.strip()}")

    # Verify we can access secure content
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("8. ✓ Verified access to secure area")

    # Demonstrate logout
    page.locator("a[href='/logout']").click()
    page.wait_for_url("**/login")
    print("9. Logged out successfully")

    # Verify we're back to login
    expect(page.locator("h2")).to_have_text("Login Page")
    print("10. ✓ Back on login page")

    print("\n=== Demo Complete ===")
    browser.close()
