# Exercise Solutions - Lecture 18: Mouse & Keyboard Actions

## Exercise 1: Hover to Reveal Menu

```python
from playwright.sync_api import sync_playwright

def hover_menu_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/howto/howto_css_dropdown.asp")
        
        # Solution 1: Hover over dropdown button
        page.locator(".dropbtn").first.hover()
        
        # Solution 2: Verify dropdown is visible
        is_visible = page.locator(".dropdown-content").first.is_visible()
        assert is_visible, "Dropdown should be visible after hover"
        
        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 2: Keyboard Shortcuts

```python
from playwright.sync_api import sync_playwright
import time

def keyboard_shortcuts_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        page.locator("[name='q']").click()
        
        # Solution 1: Type text
        page.keyboard.press_sequentially("Playwright automation")
        time.sleep(0.5)
        
        # Solution 2: Select all (Ctrl+A)
        page.keyboard.press("Control+A")
        time.sleep(0.5)
        
        # Solution 3: Copy (Ctrl+C)
        page.keyboard.press("Control+C")
        time.sleep(0.5)
        
        # Solution 4: Paste (Ctrl+V)
        page.keyboard.press("Delete")
        page.keyboard.press("Control+V")
        
        print("✓ Exercise 2 complete!")
        browser.close()
```

## Key Takeaways
- **hover()** - Reveals hidden elements and tooltips
- **dblclick()** - Double click action
- **click(button="right")** - Right click/context menu
- **drag_to()** - Drag and drop elements
- **keyboard.press()** - Keyboard shortcuts
- **keyboard.press_sequentially()** - Type text character by character
- **scroll_into_view_if_needed()** - Scroll element into view
