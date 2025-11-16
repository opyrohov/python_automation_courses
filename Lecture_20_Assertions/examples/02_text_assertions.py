"""Example 2: Text Assertions"""
from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Text Assertions Demo ===\n")

    # Example 1: to_have_text() - Exact match
    print("1. Testing to_have_text() - exact match...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("#start button").click()

    # Check exact text
    expect(page.locator("#finish h4")).to_have_text("Hello World!")
    print("   ✓ Text matches exactly: 'Hello World!'")

    # Example 2: to_contain_text() - Partial match
    print("\n2. Testing to_contain_text() - partial match...")
    page.goto("https://the-internet.herokuapp.com/")

    # Page heading contains "Welcome"
    expect(page.locator("h1")).to_contain_text("Welcome")
    print("   ✓ Heading contains 'Welcome'")

    # Example 3: to_have_text() with multiple elements
    print("\n3. Testing to_have_text() with array...")
    page.goto("https://the-internet.herokuapp.com/")

    # Get first 3 links and check their text
    links = page.locator("ul li a").all()[:3]
    expected_texts = ["A/B Testing", "Add/Remove Elements", "Basic Auth"]

    for i, link in enumerate(links):
        expect(link).to_have_text(expected_texts[i])
    print(f"   ✓ First 3 links have expected text")

    # Example 4: to_have_value() - Input values
    print("\n4. Testing to_have_value() - input values...")
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill username
    page.locator("#username").fill("testuser")
    expect(page.locator("#username")).to_have_value("testuser")
    print("   ✓ Username field has value 'testuser'")

    # Fill password
    page.locator("#password").fill("password123")
    expect(page.locator("#password")).to_have_value("password123")
    print("   ✓ Password field has value 'password123'")

    # Example 5: Using regex patterns
    print("\n5. Testing with regex patterns...")
    page.goto("https://playwright.dev/")

    # Match heading with regex
    expect(page.locator("h1").first).to_have_text(re.compile(r"Playwright.*", re.IGNORECASE))
    print("   ✓ Heading matches regex pattern")

    # Example 6: Negative text assertions
    print("\n6. Testing negative assertions...")
    page.goto("https://the-internet.herokuapp.com/")

    # Should NOT contain "Error"
    expect(page.locator("h1")).not_to_have_text("Error Page")
    expect(page.locator("h1")).not_to_contain_text("Error")
    print("   ✓ Heading does NOT contain 'Error'")

    # Example 7: Empty value
    print("\n7. Testing empty values...")
    page.goto("https://the-internet.herokuapp.com/login")

    # Initially empty
    expect(page.locator("#username")).to_have_value("")
    print("   ✓ Field is initially empty")

    # Fill and clear
    page.locator("#username").fill("test")
    page.locator("#username").fill("")
    expect(page.locator("#username")).to_have_value("")
    print("   ✓ Field is empty after clearing")

    # Example 8: Case sensitivity
    print("\n8. Testing case-insensitive matching...")
    page.goto("https://the-internet.herokuapp.com/")

    # Case-insensitive with regex
    expect(page.locator("h1")).to_have_text(re.compile(r"welcome.*internet", re.IGNORECASE))
    print("   ✓ Case-insensitive match successful")

    print("\n✓ All text assertion examples complete!")

    input("\nPress Enter to close...")
    browser.close()
