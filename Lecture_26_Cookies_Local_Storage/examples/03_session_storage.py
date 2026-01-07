"""Example 3: Session Storage

Demonstrates how to work with sessionStorage in Playwright.
sessionStorage is cleared when the page session ends (tab/window closes).
Each tab has its own separate sessionStorage.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Session Storage Demo ===\n")

    # Navigate to a page
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Set session storage items
    page.evaluate("""() => {
        sessionStorage.setItem('sessionId', 'sess_123456');
        sessionStorage.setItem('currentStep', '3');
        sessionStorage.setItem('formData', JSON.stringify({
            field1: 'value1',
            field2: 'value2'
        }));
    }""")
    print("\n2. Set sessionStorage items")

    # Get session storage items
    session_id = page.evaluate("sessionStorage.getItem('sessionId')")
    current_step = page.evaluate("sessionStorage.getItem('currentStep')")
    print(f"\n3. Retrieved values:")
    print(f"   - sessionId: {session_id}")
    print(f"   - currentStep: {current_step}")

    # Get all sessionStorage items
    all_session_data = page.evaluate("""() => {
        const data = {};
        for (let i = 0; i < sessionStorage.length; i++) {
            const key = sessionStorage.key(i);
            data[key] = sessionStorage.getItem(key);
        }
        return data;
    }""")
    print(f"\n4. All sessionStorage items:")
    for key, value in all_session_data.items():
        print(f"   - {key}: {value}")

    # Navigate to another page (same tab) - sessionStorage persists
    page.goto("https://the-internet.herokuapp.com/login")
    print("\n5. Navigated to /login page")

    # Verify sessionStorage still exists
    session_id_after = page.evaluate("sessionStorage.getItem('sessionId')")
    print(f"   sessionId still available: {session_id_after}")

    # Open a new tab - sessionStorage is NOT shared
    print("\n6. Opening new tab...")
    page2 = context.new_page()
    page2.goto("https://the-internet.herokuapp.com/")

    session_id_new_tab = page2.evaluate("sessionStorage.getItem('sessionId')")
    print(f"   sessionId in new tab: {session_id_new_tab}")
    print("   ↳ Each tab has its own sessionStorage!")

    # Set different data in new tab
    page2.evaluate("sessionStorage.setItem('tabId', 'tab_2')")
    print("\n7. Set 'tabId' in new tab")

    # Compare storage in both tabs
    tab1_data = page.evaluate("sessionStorage.length")
    tab2_data = page2.evaluate("sessionStorage.length")
    print(f"\n8. Comparing tabs:")
    print(f"   - Tab 1 items: {tab1_data}")
    print(f"   - Tab 2 items: {tab2_data}")

    # Clear sessionStorage in first tab
    page.evaluate("sessionStorage.clear()")
    print("\n9. Cleared sessionStorage in Tab 1")

    # Tab 2 is unaffected
    tab2_length = page2.evaluate("sessionStorage.length")
    print(f"   Tab 2 still has {tab2_length} item(s)")

    page2.close()

    print("\n=== Demo Complete ===")
    print("\nNote: sessionStorage is:")
    print("  - Per-tab (not shared between tabs)")
    print("  - Cleared when tab closes")
    print("  - Persists during navigation within same tab")

    context.close()
    browser.close()
