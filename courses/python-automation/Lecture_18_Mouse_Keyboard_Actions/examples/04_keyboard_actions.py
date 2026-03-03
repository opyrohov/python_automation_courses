"""Example 4: Keyboard Actions and Shortcuts"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    print("=== Keyboard Actions Demo ===\n")
    
    page.goto("https://www.google.com")
    
    # Type in search box
    search_box = page.locator("[name='q']")
    search_box.click()
    
    print("1. Typing text...")
    page.keyboard.press_sequentially("Playwright automation", delay=100)
    time.sleep(1)
    
    print("2. Selecting all text (Ctrl+A)...")
    page.keyboard.press("Control+A")
    time.sleep(0.5)
    
    print("3. Copying text (Ctrl+C)...")
    page.keyboard.press("Control+C")
    time.sleep(0.5)
    
    print("4. Clearing and pasting (Ctrl+V)...")
    page.keyboard.press("Delete")
    page.keyboard.press("Control+V")
    time.sleep(1)
    
    print("5. Pressing Enter to search...")
    page.keyboard.press("Enter")
    time.sleep(2)
    
    print("\n✓ Keyboard actions complete")
    browser.close()
