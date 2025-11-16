"""Exercise 2: Checkboxes - Practice checking and unchecking"""
from playwright.sync_api import sync_playwright

def checkbox_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        # Navigate to signup
        page.get_by_placeholder("Name").first.fill("Test User")
        page.get_by_placeholder("Email Address").nth(1).fill("test@example.com")
        page.get_by_role("button", name="Signup").click()

        # TODO 1: Check newsletter checkbox
        # Hint: Use locator("#newsletter")
        # page.YOUR_CODE_HERE.check()

        # TODO 2: Check special offers checkbox
        # Hint: Use locator("#optin")
        # page.YOUR_CODE_HERE.check()

        # TODO 3: Verify both are checked
        # Hint: Use is_checked()
        # assert page.locator("#newsletter").YOUR_METHOD_HERE
        # assert page.locator("#optin").YOUR_METHOD_HERE

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    checkbox_exercise()
