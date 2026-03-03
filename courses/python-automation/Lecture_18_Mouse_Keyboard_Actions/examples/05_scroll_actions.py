"""Example 5: Scroll Actions"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    print("=== Scroll Actions Demo ===\n")
    
    page.goto("https://playwright.dev/")
    
    print("1. Scrolling down 500px...")
    page.evaluate("window.scrollBy(0, 500)")
    time.sleep(1)
    
    print("2. Scrolling to specific position...")
    page.evaluate("window.scrollTo(0, 1000)")
    time.sleep(1)
    
    print("3. Scrolling back to top...")
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(1)
    
    print("4. Scrolling element into view...")
    # Find element at bottom and scroll to it
    footer = page.locator("footer").first
    footer.scroll_into_view_if_needed()
    time.sleep(1)
    
    print("5. Using mouse wheel to scroll...")
    page.mouse.wheel(0, -500)  # Scroll up 500px
    time.sleep(1)
    
    print("\n✓ Scroll actions complete")
    browser.close()
