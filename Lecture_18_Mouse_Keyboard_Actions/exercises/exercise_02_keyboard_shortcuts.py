"""Exercise 2: Keyboard Shortcuts"""
from playwright.sync_api import sync_playwright
import time

def keyboard_shortcuts_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        # Click search box
        page.locator("[name='q']").click()
        
        # TODO 1: Type some text using press_sequentially
        # Hint: page.keyboard.press_sequentially("your text")
        # page.keyboard.YOUR_CODE_HERE
        
        # TODO 2: Select all text using Ctrl+A
        # Hint: page.keyboard.press("Control+A")
        # page.keyboard.YOUR_CODE_HERE
        
        # TODO 3: Copy the text using Ctrl+C
        # Hint: page.keyboard.press("Control+C")
        # page.keyboard.YOUR_CODE_HERE
        
        # TODO 4: Clear and paste using Ctrl+V
        # page.keyboard.press("Delete")
        # page.keyboard.YOUR_CODE_HERE
        
        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    keyboard_shortcuts_exercise()
