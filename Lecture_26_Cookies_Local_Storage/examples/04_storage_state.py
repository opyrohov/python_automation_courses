"""Example 4: Storage State

Demonstrates how to save and load complete storage state,
including both cookies and localStorage. This is the recommended
approach for authentication reuse across tests.
"""
from playwright.sync_api import sync_playwright, expect
import os
import json

STATE_FILE = "browser_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Storage State Demo ===\n")

    # PART 1: Create and save storage state
    print("--- PART 1: Create Storage State ---\n")

    context1 = browser.new_context()
    page1 = context1.new_page()

    # Login to create authenticated session
    page1.goto("https://the-internet.herokuapp.com/login")
    page1.locator("#username").fill("tomsmith")
    page1.locator("#password").fill("SuperSecretPassword!")
    page1.locator("button[type='submit']").click()
    page1.wait_for_url("**/secure")
    print("1. Logged in successfully")

    # Add some localStorage data
    page1.evaluate("""() => {
        localStorage.setItem('user_theme', 'dark');
        localStorage.setItem('user_language', 'en');
        localStorage.setItem('last_visit', new Date().toISOString());
    }""")
    print("2. Added localStorage data")

    # Save complete storage state
    context1.storage_state(path=STATE_FILE)
    print(f"3. Saved storage state to {STATE_FILE}")

    # Show what was saved
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
    print(f"\n4. Saved state contains:")
    print(f"   - Cookies: {len(state.get('cookies', []))}")
    print(f"   - Origins with localStorage: {len(state.get('origins', []))}")

    for origin in state.get("origins", []):
        print(f"\n   Origin: {origin['origin']}")
        for item in origin.get("localStorage", []):
            print(f"   - {item['name']}: {item['value'][:30]}...")

    context1.close()
    print("\n5. Closed first context")

    # PART 2: Load storage state in new context
    print("\n--- PART 2: Load Storage State ---\n")

    # Create new context WITH saved state
    context2 = browser.new_context(storage_state=STATE_FILE)
    page2 = context2.new_page()
    print("6. Created new context with saved state")

    # Navigate directly to protected page (no login needed!)
    page2.goto("https://the-internet.herokuapp.com/secure")
    print("7. Navigated directly to /secure")

    # Verify we're authenticated
    expect(page2.locator("h2")).to_have_text("Secure Area")
    print("8. ✓ Authenticated! We're on the secure page")

    # Verify localStorage was restored
    theme = page2.evaluate("localStorage.getItem('user_theme')")
    language = page2.evaluate("localStorage.getItem('user_language')")
    print(f"\n9. Restored localStorage:")
    print(f"   - theme: {theme}")
    print(f"   - language: {language}")

    context2.close()

    # PART 3: Get state without saving to file
    print("\n--- PART 3: Storage State as Dict ---\n")

    context3 = browser.new_context()
    page3 = context3.new_page()
    page3.goto("https://the-internet.herokuapp.com/")
    page3.evaluate("localStorage.setItem('test', 'value')")

    # Get state as dictionary (not saved to file)
    state_dict = context3.storage_state()
    print("10. Got storage state as dictionary")
    print(f"    Type: {type(state_dict)}")
    print(f"    Keys: {list(state_dict.keys())}")

    context3.close()

    # Cleanup
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
        print(f"\n11. Cleaned up {STATE_FILE}")

    print("\n=== Demo Complete ===")
    browser.close()
