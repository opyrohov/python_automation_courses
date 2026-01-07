"""Example 1: Cookie Basics

Demonstrates how to get, add, and inspect cookies in Playwright.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Cookie Basics Demo ===\n")

    # Navigate to a site that sets cookies
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Get all cookies
    cookies = context.cookies()
    print(f"\n2. Current cookies: {len(cookies)}")
    for cookie in cookies:
        print(f"   - {cookie['name']}: {cookie['value'][:20]}...")

    # Add a custom cookie
    context.add_cookies([
        {
            "name": "test_cookie",
            "value": "hello_playwright",
            "domain": "the-internet.herokuapp.com",
            "path": "/"
        }
    ])
    print("\n3. Added custom cookie 'test_cookie'")

    # Verify cookie was added
    cookies = context.cookies()
    test_cookie = next((c for c in cookies if c["name"] == "test_cookie"), None)
    if test_cookie:
        print(f"   ✓ Cookie found: {test_cookie['name']} = {test_cookie['value']}")

    # Add cookie with more options
    context.add_cookies([
        {
            "name": "user_preference",
            "value": "dark_mode",
            "domain": "the-internet.herokuapp.com",
            "path": "/",
            "httpOnly": False,
            "secure": False,
            "sameSite": "Lax"
        }
    ])
    print("\n4. Added 'user_preference' cookie with options")

    # Get cookies for specific URL
    url_cookies = context.cookies(["https://the-internet.herokuapp.com/login"])
    print(f"\n5. Cookies for /login page: {len(url_cookies)}")

    # Display all cookie details
    print("\n6. All cookie details:")
    all_cookies = context.cookies()
    for i, cookie in enumerate(all_cookies, 1):
        print(f"\n   Cookie {i}:")
        print(f"   - Name: {cookie['name']}")
        print(f"   - Value: {cookie['value']}")
        print(f"   - Domain: {cookie['domain']}")
        print(f"   - Path: {cookie['path']}")
        print(f"   - Secure: {cookie.get('secure', False)}")
        print(f"   - HttpOnly: {cookie.get('httpOnly', False)}")

    # Clear all cookies
    context.clear_cookies()
    print("\n7. Cleared all cookies")

    # Verify cookies are cleared
    remaining = context.cookies()
    print(f"   Remaining cookies: {len(remaining)}")

    print("\n=== Demo Complete ===")
    context.close()
    browser.close()
