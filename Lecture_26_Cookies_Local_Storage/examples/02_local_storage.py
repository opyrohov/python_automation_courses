"""Example 2: Local Storage

Demonstrates how to work with localStorage in Playwright.
localStorage persists across browser sessions until explicitly cleared.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Local Storage Demo ===\n")

    # Navigate to a page
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Set a simple value
    page.evaluate("localStorage.setItem('theme', 'dark')")
    print("\n2. Set localStorage item: theme = 'dark'")

    # Get the value back
    theme = page.evaluate("localStorage.getItem('theme')")
    print(f"   Retrieved value: {theme}")

    # Set multiple values
    page.evaluate("""() => {
        localStorage.setItem('language', 'en');
        localStorage.setItem('notifications', 'true');
        localStorage.setItem('fontSize', '16');
    }""")
    print("\n3. Set multiple localStorage items")

    # Store complex data (JSON)
    user_settings = {
        "name": "Test User",
        "email": "test@example.com",
        "preferences": {
            "theme": "dark",
            "compact": True
        }
    }
    page.evaluate(f"localStorage.setItem('userSettings', '{json.dumps(user_settings)}')")
    print("\n4. Stored JSON object in localStorage")

    # Retrieve and parse JSON
    stored_settings = page.evaluate("localStorage.getItem('userSettings')")
    parsed = json.loads(stored_settings)
    print(f"   Retrieved: {parsed['name']} ({parsed['email']})")

    # Get all localStorage items
    all_data = page.evaluate("""() => {
        const data = {};
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            data[key] = localStorage.getItem(key);
        }
        return data;
    }""")
    print(f"\n5. All localStorage items ({len(all_data)} total):")
    for key, value in all_data.items():
        display_value = value[:30] + "..." if len(value) > 30 else value
        print(f"   - {key}: {display_value}")

    # Get localStorage length
    length = page.evaluate("localStorage.length")
    print(f"\n6. localStorage length: {length}")

    # Check if key exists
    has_theme = page.evaluate("localStorage.getItem('theme') !== null")
    has_missing = page.evaluate("localStorage.getItem('nonexistent') !== null")
    print(f"\n7. Key existence check:")
    print(f"   - 'theme' exists: {has_theme}")
    print(f"   - 'nonexistent' exists: {has_missing}")

    # Remove specific item
    page.evaluate("localStorage.removeItem('fontSize')")
    print("\n8. Removed 'fontSize' from localStorage")

    # Verify removal
    font_size = page.evaluate("localStorage.getItem('fontSize')")
    print(f"   fontSize after removal: {font_size}")

    # Clear all localStorage
    page.evaluate("localStorage.clear()")
    print("\n9. Cleared all localStorage")

    # Verify clear
    final_length = page.evaluate("localStorage.length")
    print(f"   localStorage length after clear: {final_length}")

    print("\n=== Demo Complete ===")
    context.close()
    browser.close()
