"""Exercise 3: Dropdowns - Practice selecting options from dropdown menus"""
from playwright.sync_api import sync_playwright

def dropdown_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        # Navigate to signup
        page.get_by_placeholder("Name").first.fill("Test User")
        page.get_by_placeholder("Email Address").nth(1).fill("dropdown_test@example.com")
        page.get_by_role("button", name="Signup").click()

        # TODO 1: Select day of birth (e.g., "15")
        # Hint: Use locator("#days").select_option("15")
        # page.YOUR_CODE_HERE

        # TODO 2: Select month of birth (e.g., "March")
        # Hint: Use locator("#months").select_option("March")
        # page.YOUR_CODE_HERE

        # TODO 3: Select year of birth (e.g., "1995")
        # Hint: Use locator("#years").select_option("1995")
        # page.YOUR_CODE_HERE

        # TODO 4: Select country using label parameter
        # Hint: Use locator("#country").select_option(label="Canada")
        # page.YOUR_CODE_HERE

        # TODO 5: Verify country selection
        # Hint: Use input_value() to get selected value
        # selected_country = page.locator("#country").YOUR_METHOD_HERE
        # assert selected_country == "Canada", f"Expected 'Canada', got '{selected_country}'"

        print("✓ Exercise 3 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    dropdown_exercise()
