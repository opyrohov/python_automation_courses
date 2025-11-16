"""Exercise 1: Login Form - Fill and submit a login form"""
from playwright.sync_api import sync_playwright

def login_form_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        # TODO 1: Fill email field
        # Hint: Use get_by_placeholder or locator with data-qa="login-email"
        # page.YOUR_CODE_HERE.fill("test@example.com")

        # TODO 2: Fill password field
        # Hint: Use data-qa="login-password"
        # page.YOUR_CODE_HERE.fill("password123")

        # TODO 3: Click login button
        # Hint: Use get_by_role("button", name="Login")
        # page.YOUR_CODE_HERE.click()

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    login_form_exercise()
