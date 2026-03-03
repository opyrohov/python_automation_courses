"""Exercise 2: Custom Wait Conditions"""
from playwright.sync_api import sync_playwright

def custom_wait_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # TODO 1: Add 3 elements by clicking the "Add Element" button 3 times
        # Hint: Use a for loop and page.locator("button").first.click()
        # for i in range(3):
        #     page.YOUR_CODE_HERE

        # TODO 2: Wait for exactly 3 elements using wait_for_function
        # Hint: page.wait_for_function("() => document.querySelectorAll('.added-manually').length === 3")
        # page.YOUR_CODE_HERE

        # TODO 3: Verify by getting the count
        # Hint: count = page.locator(".added-manually").count()
        # count = page.YOUR_CODE_HERE
        # assert count == 3, f"Expected 3 elements, got {count}"

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    custom_wait_exercise()
