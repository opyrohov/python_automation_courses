"""Exercise 1: Visibility and Text Assertions"""
from playwright.sync_api import sync_playwright, expect

def visibility_text_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

        # TODO 1: Assert that the start button is visible
        # Hint: expect(page.locator("#start button")).to_be_visible()
        # expect(YOUR_CODE_HERE)

        # TODO 2: Assert that the finish element is hidden initially
        # Hint: expect(page.locator("#finish")).to_be_hidden()
        # expect(YOUR_CODE_HERE)

        # Click the start button
        page.locator("#start button").click()

        # TODO 3: Wait for and assert that the finish element becomes visible
        # Hint: expect(page.locator("#finish")).to_be_visible()
        # expect(YOUR_CODE_HERE)

        # TODO 4: Assert that the finish heading has text "Hello World!"
        # Hint: expect(page.locator("#finish h4")).to_have_text("Hello World!")
        # expect(YOUR_CODE_HERE)

        # TODO 5: Assert that the loading indicator is now hidden
        # Hint: expect(page.locator("#loading")).to_be_hidden()
        # expect(YOUR_CODE_HERE)

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    visibility_text_exercise()
