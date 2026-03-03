"""Exercise 1: Hover to Reveal Menu"""
from playwright.sync_api import sync_playwright

def hover_menu_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/howto/howto_css_dropdown.asp")
        
        # TODO 1: Hover over the dropdown button to reveal menu
        # Hint: Use .locator(".dropbtn").first.hover()
        # page.YOUR_CODE_HERE
        
        # TODO 2: Verify dropdown content is visible
        # Hint: Use .locator(".dropdown-content").first.is_visible()
        # is_visible = page.YOUR_CODE_HERE
        # assert is_visible, "Dropdown should be visible after hover"
        
        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    hover_menu_exercise()
