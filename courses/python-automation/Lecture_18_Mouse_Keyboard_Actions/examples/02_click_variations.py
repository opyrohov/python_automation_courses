"""Example 2: Click Variations - Double click, right click"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    print("=== Click Variations Demo ===\n")
    
    # Example: Double click
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
    page.frame_locator("#iframeResult").locator("p").first.dblclick()
    time.sleep(1)
    print("1. ✓ Double click executed")
    
    # Example: Right click (context menu)
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_oncontextmenu")
    page.frame_locator("#iframeResult").locator("div").first.click(button="right")
    time.sleep(1)
    print("2. ✓ Right click executed")
    
    # Example: Click with modifiers
    page.goto("https://example.com")
    # Click with Control key (usually opens in new tab)
    # Note: In automation, this might not open a new tab in the same way
    page.locator("a").first.click(modifiers=["Control"])
    time.sleep(1)
    print("3. ✓ Click with modifier executed")
    
    time.sleep(2)
    print("\n✓ Click variations complete")
    browser.close()
