"""Exercise 1: Waiting for Dynamic Content"""
from playwright.sync_api import sync_playwright, expect

def dynamic_content_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

        # TODO 1: Click the start button
        # Hint: page.locator("#start button").click()
        # page.YOUR_CODE_HERE

        # TODO 2: Wait for the loading indicator to be hidden
        # Hint: page.wait_for_selector("#loading", state="hidden")
        # page.YOUR_CODE_HERE

        # TODO 3: Wait for the finish element to be visible
        # Hint: page.wait_for_selector("#finish", state="visible")
        # page.YOUR_CODE_HERE

        # TODO 4: Use expect() to verify the text is "Hello World!"
        # Hint: expect(page.locator("#finish h4")).to_have_text("Hello World!")
        # expect(YOUR_CODE_HERE)

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    dynamic_content_exercise()
