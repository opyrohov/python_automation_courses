"""Example 3: Drag and Drop"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    print("=== Drag and Drop Demo ===\n")
    
    page.goto("https://www.w3schools.com/html/html5_draganddrop.asp")
    
    print("1. Dragging element...")
    # Find draggable and droppable elements
    draggable = page.locator("#drag1")
    droppable = page.locator("#div1")
    
    # Perform drag and drop
    draggable.drag_to(droppable)
    time.sleep(2)
    
    print("2. ✓ Drag and drop completed")
    
    # Verify the element was dropped
    # (In real tests, you'd verify the DOM changed)
    
    time.sleep(2)
    print("\n✓ Drag and drop example complete")
    browser.close()
