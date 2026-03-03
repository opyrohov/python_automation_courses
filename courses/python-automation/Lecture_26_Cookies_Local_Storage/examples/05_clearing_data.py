"""Example 5: Clearing Browser Data

Demonstrates different ways to clear cookies, localStorage,
and sessionStorage in Playwright tests.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Clearing Browser Data Demo ===\n")

    # Setup: Add some data
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Setting up test data...")

    # Add cookies
    context.add_cookies([
        {"name": "cookie1", "value": "value1", "domain": "the-internet.herokuapp.com", "path": "/"},
        {"name": "cookie2", "value": "value2", "domain": "the-internet.herokuapp.com", "path": "/"},
        {"name": "other_domain", "value": "value3", "domain": "example.com", "path": "/"}
    ])

    # Add localStorage
    page.evaluate("""() => {
        localStorage.setItem('local1', 'data1');
        localStorage.setItem('local2', 'data2');
    }""")

    # Add sessionStorage
    page.evaluate("""() => {
        sessionStorage.setItem('session1', 'data1');
        sessionStorage.setItem('session2', 'data2');
    }""")

    print("   Added: 3 cookies, 2 localStorage, 2 sessionStorage items")

    # Show current state
    print("\n2. Current state:")
    print(f"   Cookies: {len(context.cookies())}")
    print(f"   localStorage: {page.evaluate('localStorage.length')}")
    print(f"   sessionStorage: {page.evaluate('sessionStorage.length')}")

    # METHOD 1: Clear only cookies
    print("\n--- Method 1: Clear Cookies Only ---")
    context.clear_cookies()
    print("   Called context.clear_cookies()")
    print(f"   Cookies now: {len(context.cookies())}")
    print(f"   localStorage still has: {page.evaluate('localStorage.length')} items")

    # Restore cookies for next demo
    context.add_cookies([
        {"name": "cookie1", "value": "value1", "domain": "the-internet.herokuapp.com", "path": "/"}
    ])

    # METHOD 2: Clear only localStorage
    print("\n--- Method 2: Clear localStorage Only ---")
    page.evaluate("localStorage.clear()")
    print("   Called localStorage.clear()")
    print(f"   localStorage now: {page.evaluate('localStorage.length')}")
    print(f"   sessionStorage still has: {page.evaluate('sessionStorage.length')} items")
    print(f"   Cookies still has: {len(context.cookies())} items")

    # Restore localStorage
    page.evaluate("localStorage.setItem('restored', 'data')")

    # METHOD 3: Clear only sessionStorage
    print("\n--- Method 3: Clear sessionStorage Only ---")
    page.evaluate("sessionStorage.clear()")
    print("   Called sessionStorage.clear()")
    print(f"   sessionStorage now: {page.evaluate('sessionStorage.length')}")

    # METHOD 4: Clear all storage at once
    print("\n--- Method 4: Clear All Storage ---")

    # First, re-add all data
    context.add_cookies([
        {"name": "cookie1", "value": "value1", "domain": "the-internet.herokuapp.com", "path": "/"}
    ])
    page.evaluate("""() => {
        localStorage.setItem('local', 'data');
        sessionStorage.setItem('session', 'data');
    }""")
    print("   Re-added test data")

    # Clear everything
    context.clear_cookies()
    page.evaluate("""() => {
        localStorage.clear();
        sessionStorage.clear();
    }""")
    print("   Cleared all storage")
    print(f"   Cookies: {len(context.cookies())}")
    print(f"   localStorage: {page.evaluate('localStorage.length')}")
    print(f"   sessionStorage: {page.evaluate('sessionStorage.length')}")

    # METHOD 5: Fresh context (cleanest approach)
    print("\n--- Method 5: Fresh Context ---")
    context.close()

    fresh_context = browser.new_context()
    fresh_page = fresh_context.new_page()
    fresh_page.goto("https://the-internet.herokuapp.com/")

    print("   Created new context")
    print(f"   Cookies: {len(fresh_context.cookies())}")
    print(f"   localStorage: {fresh_page.evaluate('localStorage.length')}")
    print(f"   sessionStorage: {fresh_page.evaluate('sessionStorage.length')}")
    print("   ✓ Completely clean state!")

    # METHOD 6: Clear cookies for specific domain
    print("\n--- Method 6: Clear Specific Domain Cookies ---")

    fresh_context.add_cookies([
        {"name": "keep_me", "value": "important", "domain": "example.com", "path": "/"},
        {"name": "delete_me", "value": "temp", "domain": "the-internet.herokuapp.com", "path": "/"}
    ])
    print("   Added cookies for two domains")

    # Get cookies, filter, and restore
    all_cookies = fresh_context.cookies()
    keep_cookies = [c for c in all_cookies if c["domain"] != "the-internet.herokuapp.com"]

    fresh_context.clear_cookies()
    fresh_context.add_cookies(keep_cookies)

    print("   Cleared the-internet.herokuapp.com cookies only")
    remaining = fresh_context.cookies()
    for c in remaining:
        print(f"   - Kept: {c['name']} ({c['domain']})")

    fresh_context.close()

    print("\n=== Demo Complete ===")
    print("\nSummary of clearing methods:")
    print("  - context.clear_cookies() - Clear all cookies")
    print("  - localStorage.clear() - Clear localStorage (via evaluate)")
    print("  - sessionStorage.clear() - Clear sessionStorage (via evaluate)")
    print("  - browser.new_context() - Completely fresh state")

    browser.close()
