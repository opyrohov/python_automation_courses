"""Example 2: Basic Page Object

This shows the basic structure of a Page Object class.
Locators are defined once, methods encapsulate actions.
"""
from playwright.sync_api import sync_playwright, expect


# ============================================
# PAGE OBJECT CLASS
# ============================================
class LoginPage:
    """Page Object for the Login Page."""

    # URL for this page
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        """Initialize with Playwright page object."""
        self.page = page

        # Define all locators in ONE place
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".flash.error")
        self.success_message = page.locator(".flash.success")

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.URL)

    def login(self, username, password):
        """Perform login with given credentials."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        """Get error message text."""
        return self.error_message.text_content()

    def is_error_visible(self):
        """Check if error message is visible."""
        return self.error_message.is_visible()

    def is_success_visible(self):
        """Check if success message is visible."""
        return self.success_message.is_visible()


# ============================================
# TESTS USING PAGE OBJECT
# ============================================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Test WITH Basic Page Object ===\n")

    # Create page object instance
    login_page = LoginPage(page)

    # TEST 1: Successful Login
    print("--- Test 1: Successful Login ---")
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")

    page.wait_for_url("**/secure")
    expect(page.locator(".flash.success")).to_be_visible()
    print("  ✓ Login successful")

    # Go back for next test
    page.goto(LoginPage.URL)

    # TEST 2: Failed Login
    print("\n--- Test 2: Failed Login ---")
    login_page.login("wronguser", "wrongpassword")

    assert login_page.is_error_visible()
    error = login_page.get_error_text()
    print(f"  ✓ Error shown: {error.strip()[:30]}...")

    # TEST 3: Empty Fields
    print("\n--- Test 3: Empty Fields ---")
    login_page.navigate()
    login_page.login("", "")

    assert login_page.is_error_visible()
    print("  ✓ Error shown for empty fields")

    browser.close()

    print("\n" + "=" * 50)
    print("BENEFITS of Page Object Model:")
    print("=" * 50)
    print("""
    1. SINGLE SOURCE OF TRUTH:
       - Locators defined ONCE in the class
       - Change in one place, affects all tests

    2. REUSABLE:
       - login() method can be used anywhere
       - Same page object for all login tests

    3. READABLE:
       - login_page.login("user", "pass")
       - Clear intent, no implementation details

    4. MAINTAINABLE:
       - If selector changes: update LoginPage only
       - Tests don't need to change

    5. ENCAPSULATION:
       - Tests don't know HOW login works
       - Tests only know WHAT to do
    """)
