"""Example 3: Saving Authentication State"""
from playwright.sync_api import sync_playwright, expect
import json
import os

AUTH_FILE = "auth_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Saving Authentication State Demo ===\n")

    # Step 1: Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print("1. Navigated to login page")

    # Step 2: Perform login
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    print("2. Submitted login form")

    # Step 3: Wait for successful login
    page.wait_for_url("**/secure")
    expect(page.locator(".flash.success")).to_be_visible()
    print("3. Login successful")

    # Step 4: Save authentication state
    context.storage_state(path=AUTH_FILE)
    print(f"4. ✓ Authentication state saved to {AUTH_FILE}")

    # Step 5: Show what was saved
    print("\n--- Saved State Contents ---")
    with open(AUTH_FILE, "r") as f:
        state = json.load(f)

    print(f"Cookies saved: {len(state.get('cookies', []))}")
    for cookie in state.get("cookies", []):
        print(f"  - {cookie['name']}: {cookie['value'][:20]}...")

    print(f"\nOrigins saved: {len(state.get('origins', []))}")
    for origin in state.get("origins", []):
        print(f"  - {origin['origin']}")
        ls = origin.get("localStorage", [])
        if ls:
            print(f"    localStorage items: {len(ls)}")

    # Step 6: Verify file exists
    file_size = os.path.getsize(AUTH_FILE)
    print(f"\nFile size: {file_size} bytes")

    print("\n=== Demo Complete ===")
    print(f"Auth state saved to: {os.path.abspath(AUTH_FILE)}")
    print("You can now use this file in other tests!")

    context.close()
    browser.close()
