"""Example 1: Auto-Waiting Demonstrations"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Auto-Waiting Demo ===\n")

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    print("1. Clicking button - auto-waits for element to be actionable...")
    page.locator("#start button").click()

    print("2. Waiting for result - using expect() which auto-waits...")
    # This automatically waits for element to appear and have text
    expect(page.locator("#finish h4")).to_have_text("Hello World!")
    print("   ✓ Text appeared!")

    print("\n3. Demonstrating auto-wait for visibility...")
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Remove checkbox button - auto-waits to be clickable
    page.locator("button").filter(has_text="Remove").click()

    # Verify it's gone - auto-waits and retries
    expect(page.locator("#checkbox")).not_to_be_visible()
    print("   ✓ Checkbox removed!")

    # Add it back - auto-waits
    page.locator("button").filter(has_text="Add").click()
    expect(page.locator("#checkbox")).to_be_visible()
    print("   ✓ Checkbox added back!")

    print("\n4. Auto-wait for input to be enabled...")
    page.locator("button").filter(has_text="Enable").click()

    # This waits for input to be enabled before filling
    page.locator("input[type='text']").fill("Auto-waited for me!")
    print("   ✓ Input filled after auto-waiting for enabled state!")

    print("\n✓ All auto-waiting examples complete!")
    print("Notice: No explicit waits needed - Playwright handled it all!")

    input("\nPress Enter to close...")
    browser.close()
