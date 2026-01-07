"""Example 1: Basic Screenshots"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Basic Screenshots Demo ===\n")

    # Navigate to a page
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Basic screenshot - captures visible viewport
    page.screenshot(path="screenshot_basic.png")
    print("2. Basic screenshot saved: screenshot_basic.png")

    # Screenshot as bytes (no file saved)
    screenshot_bytes = page.screenshot()
    print(f"3. Screenshot as bytes: {len(screenshot_bytes)} bytes")

    # Save bytes manually
    with open("screenshot_from_bytes.png", "wb") as f:
        f.write(screenshot_bytes)
    print("4. Saved bytes to file: screenshot_from_bytes.png")

    # Navigate to a longer page
    page.goto("https://the-internet.herokuapp.com/tables")

    # Viewport only screenshot
    page.screenshot(path="screenshot_viewport.png")
    print("5. Viewport screenshot saved: screenshot_viewport.png")

    # Full page screenshot - captures entire scrollable page
    page.screenshot(path="screenshot_full_page.png", full_page=True)
    print("6. Full page screenshot saved: screenshot_full_page.png")

    print("\n=== Demo Complete ===")
    browser.close()
