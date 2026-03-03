"""Example 1: Test WITHOUT Page Object Model

This shows what tests look like without POM - notice the problems:
- Locators repeated everywhere
- Hard to maintain if selectors change
- Tests are verbose and hard to read
- No code reuse between tests
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Test WITHOUT Page Object Model ===\n")
    print("Notice the problems with this approach...\n")

    # TEST 1: Successful Login
    print("--- Test 1: Successful Login ---")

    # Navigate (hardcoded URL)
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill form (locators directly in test)
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # Assert (locators repeated)
    page.wait_for_url("**/secure")
    expect(page.locator(".flash.success")).to_be_visible()
    print("  ✓ Login successful")

    # Logout for next test
    page.locator("a[href='/logout']").click()

    # TEST 2: Failed Login
    print("\n--- Test 2: Failed Login ---")

    # Same locators repeated again!
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wronguser")
    page.locator("#password").fill("wrongpassword")
    page.locator("button[type='submit']").click()

    # Different assertion, but same locator pattern
    expect(page.locator(".flash.error")).to_be_visible()
    error_text = page.locator(".flash.error").text_content()
    print(f"  ✓ Error shown: {error_text.strip()[:30]}...")

    # TEST 3: Empty Fields Validation
    print("\n--- Test 3: Empty Fields ---")

    # Again, same locators!
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("")
    page.locator("#password").fill("")
    page.locator("button[type='submit']").click()

    expect(page.locator(".flash.error")).to_be_visible()
    print("  ✓ Error shown for empty fields")

    browser.close()

    print("\n" + "=" * 50)
    print("PROBLEMS with this approach:")
    print("=" * 50)
    print("""
    1. DUPLICATION: Same locators appear in every test
       - "#username" appears 3 times
       - "#password" appears 3 times
       - "button[type='submit']" appears 3 times

    2. MAINTENANCE NIGHTMARE:
       - If selector changes, must update ALL tests
       - What if we have 100 tests?

    3. NO REUSABILITY:
       - Login logic duplicated
       - Can't share between test files

    4. POOR READABILITY:
       - Tests mixed with implementation details
       - Hard to understand test intent

    5. FRAGILE:
       - Tests break easily
       - No abstraction layer

    SOLUTION: Page Object Model! (See next examples)
    """)
