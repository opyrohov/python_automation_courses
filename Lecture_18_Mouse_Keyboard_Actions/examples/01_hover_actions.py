"""Example 1: Hover Actions - Reveal hidden elements"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    print("=== Hover Actions Demo ===\n")
    
    # Example: Hover to reveal menu
    page.goto("https://www.w3schools.com/howto/howto_css_dropdown.asp")
    
    print("1. Hovering over dropdown button...")
    dropdown = page.locator(".dropbtn").first
    dropdown.hover()
    time.sleep(1)
    
    print("2. Menu items should now be visible")
    # The dropdown content becomes visible on hover
    dropdown_content = page.locator(".dropdown-content").first
    print(f"   Dropdown visible: {dropdown_content.is_visible()}")
    
    time.sleep(2)
    print("\n✓ Hover actions complete")
    browser.close()
