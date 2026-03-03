"""Example 5: URL and Title Assertions"""
from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== URL & Title Assertions Demo ===\n")

    # Example 1: to_have_url() - Exact match
    print("1. Testing to_have_url() - exact match...")
    page.goto("https://the-internet.herokuapp.com/")

    expect(page).to_have_url("https://the-internet.herokuapp.com/")
    print("   ✓ URL matches exactly")

    # Example 2: to_have_url() - Wildcard pattern
    print("\n2. Testing to_have_url() - wildcard pattern...")
    page.goto("https://the-internet.herokuapp.com/login")

    # Pattern matching with **
    expect(page).to_have_url("**/login")
    print("   ✓ URL matches pattern '**/login'")

    # Example 3: to_have_url() - Regex
    print("\n3. Testing to_have_url() - regex pattern...")
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Regex pattern
    expect(page).to_have_url(re.compile(r".*/abtest$"))
    print("   ✓ URL matches regex pattern")

    # Example 4: to_have_title() - Exact match
    print("\n4. Testing to_have_title() - exact match...")
    page.goto("https://the-internet.herokuapp.com/")

    expect(page).to_have_title("The Internet")
    print("   ✓ Title matches exactly: 'The Internet'")

    # Example 5: to_have_title() - Regex
    print("\n5. Testing to_have_title() - regex pattern...")
    page.goto("https://playwright.dev/")

    # Title contains "Playwright"
    expect(page).to_have_title(re.compile(r".*Playwright.*"))
    print("   ✓ Title contains 'Playwright'")

    # Example 6: URL change after navigation
    print("\n6. Testing URL change after navigation...")
    page.goto("https://the-internet.herokuapp.com/")

    # Click on a link
    page.locator("a").filter(has_text="A/B Testing").click()

    # Verify URL changed
    expect(page).to_have_url("**/abtest")
    print("   ✓ URL changed after clicking link")

    # Example 7: URL with timeout
    print("\n7. Testing URL change with timeout...")
    page.goto("https://the-internet.herokuapp.com/")

    # Click link
    page.locator("a").filter(has_text="Dynamic Loading").click()

    # Wait for URL to change
    expect(page).to_have_url("**/dynamic_loading", timeout=5000)
    print("   ✓ URL changed within timeout")

    # Example 8: Negative URL assertions
    print("\n8. Testing negative URL assertions...")
    page.goto("https://the-internet.herokuapp.com/")

    # Should NOT be on login page
    expect(page).not_to_have_url("**/login")
    print("   ✓ Not on login page")

    # Example 9: Title change after navigation
    print("\n9. Testing title change after navigation...")
    page.goto("https://the-internet.herokuapp.com/")
    initial_title = page.title()

    # Navigate to different page
    page.locator("a").filter(has_text="Form Authentication").click()

    # Title should still be "The Internet" (same for all pages)
    expect(page).to_have_title("The Internet")
    print("   ✓ Title verified after navigation")

    # Example 10: URL query parameters
    print("\n10. Testing URL with query parameters...")
    page.goto("https://the-internet.herokuapp.com/login?user=test")

    # Check URL contains query parameter
    expect(page).to_have_url(re.compile(r".*\?user=test"))
    print("   ✓ URL contains query parameter")

    # Example 11: Complete navigation verification
    print("\n11. Testing complete navigation flow...")
    page.goto("https://the-internet.herokuapp.com/")

    # Initial state
    expect(page).to_have_url("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")
    print("   ✓ Initial page verified")

    # Navigate
    page.locator("a").filter(has_text="Checkboxes").click()

    # New state
    expect(page).to_have_url("**/checkboxes")
    expect(page).to_have_title("The Internet")
    print("   ✓ Navigation verified")

    print("\n✓ All URL & title assertion examples complete!")

    input("\nPress Enter to close...")
    browser.close()
