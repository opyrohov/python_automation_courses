"""Example 4: Reusing Authentication State"""
from playwright.sync_api import sync_playwright, expect
import os

AUTH_FILE = "auth_state.json"

# Check if auth file exists
if not os.path.exists(AUTH_FILE):
    print(f"ERROR: {AUTH_FILE} not found!")
    print("Please run 03_save_auth_state.py first to create the auth file.")
    exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Reusing Authentication State Demo ===\n")

    # Create context with saved authentication state
    context = browser.new_context(
        storage_state=AUTH_FILE
    )
    page = context.new_page()
    print("1. Created context with saved auth state")

    # Go directly to protected page - no login needed!
    page.goto("https://the-internet.herokuapp.com/secure")
    print("2. Navigated directly to secure page")

    # Verify we're logged in
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("3. ✓ Verified we're in Secure Area")

    success_message = page.locator(".flash.success")
    expect(success_message).to_be_visible()
    print("4. ✓ Success message visible - we're authenticated!")

    # Show we can access other protected pages too
    page.goto("https://the-internet.herokuapp.com/")
    print("5. Navigated to home page")

    # Go back to secure page
    page.goto("https://the-internet.herokuapp.com/secure")
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("6. ✓ Still authenticated on secure page")

    # Compare with fresh context (no auth)
    print("\n--- Testing Fresh Context (No Auth) ---")
    fresh_context = browser.new_context()  # No storage_state
    fresh_page = fresh_context.new_page()

    # Try to access secure page without auth
    fresh_page.goto("https://the-internet.herokuapp.com/secure")

    # Should be redirected to login
    if "/login" in fresh_page.url:
        print("7. ✓ Fresh context redirected to login (as expected)")
    else:
        print("7. Fresh context unexpectedly accessed secure page")

    fresh_context.close()

    print("\n=== Demo Complete ===")
    print("Key takeaway: With storage_state, we skip login completely!")

    context.close()
    browser.close()
