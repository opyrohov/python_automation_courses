"""Example 3: Page Object with Rich Methods

Shows more sophisticated page object with:
- Granular action methods
- Combined convenience methods
- Getter methods for data
- Validation/assertion helper methods
"""
from playwright.sync_api import sync_playwright, expect


class LoginPage:
    """Login Page with comprehensive methods."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page

        # Form elements
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")

        # Messages
        self.flash_message = page.locator("#flash")
        self.error_message = page.locator(".flash.error")
        self.success_message = page.locator(".flash.success")

        # Page elements
        self.page_title = page.locator("h2")
        self.login_form = page.locator("#login")

    # ==================
    # NAVIGATION METHODS
    # ==================
    def navigate(self):
        """Navigate to login page."""
        self.page.goto(self.URL)

    def is_loaded(self):
        """Check if login page is loaded."""
        return self.login_form.is_visible()

    # ==================
    # GRANULAR ACTIONS
    # ==================
    def enter_username(self, username):
        """Enter username into the input field."""
        self.username_input.fill(username)

    def enter_password(self, password):
        """Enter password into the input field."""
        self.password_input.fill(password)

    def click_login_button(self):
        """Click the login button."""
        self.login_button.click()

    def clear_username(self):
        """Clear the username field."""
        self.username_input.clear()

    def clear_password(self):
        """Clear the password field."""
        self.password_input.clear()

    # ==================
    # COMBINED ACTIONS
    # ==================
    def login(self, username, password):
        """Perform complete login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_as_valid_user(self):
        """Login with known valid credentials."""
        self.login("tomsmith", "SuperSecretPassword!")

    def login_as_invalid_user(self):
        """Login with invalid credentials."""
        self.login("invalid", "invalid")

    # ==================
    # GETTER METHODS
    # ==================
    def get_page_title(self):
        """Get the page title text."""
        return self.page_title.text_content()

    def get_flash_message(self):
        """Get the flash message text."""
        return self.flash_message.text_content().strip()

    def get_username_value(self):
        """Get current value in username field."""
        return self.username_input.input_value()

    def get_password_value(self):
        """Get current value in password field."""
        return self.password_input.input_value()

    # ==================
    # VALIDATION METHODS
    # ==================
    def is_error_displayed(self):
        """Check if error message is visible."""
        return self.error_message.is_visible()

    def is_success_displayed(self):
        """Check if success message is visible."""
        return self.success_message.is_visible()

    def has_error_containing(self, text):
        """Check if error message contains specific text."""
        if not self.is_error_displayed():
            return False
        return text.lower() in self.get_flash_message().lower()

    def is_login_button_enabled(self):
        """Check if login button is enabled."""
        return self.login_button.is_enabled()


# ============================================
# TESTS DEMONSTRATING RICH METHODS
# ============================================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Page Object with Rich Methods ===\n")

    login_page = LoginPage(page)

    # TEST 1: Using granular methods
    print("--- Test 1: Granular Methods ---")
    login_page.navigate()

    assert login_page.is_loaded(), "Page not loaded"
    print(f"  Page title: {login_page.get_page_title()}")

    login_page.enter_username("testuser")
    login_page.enter_password("testpass")

    print(f"  Username value: {login_page.get_username_value()}")
    print(f"  Password value: {'*' * len(login_page.get_password_value())}")

    login_page.click_login_button()

    assert login_page.is_error_displayed()
    print(f"  ✓ Error: {login_page.get_flash_message()[:40]}...")

    # TEST 2: Using convenience methods
    print("\n--- Test 2: Convenience Methods ---")
    login_page.navigate()
    login_page.login_as_valid_user()

    page.wait_for_url("**/secure")
    print("  ✓ Logged in as valid user")

    page.goto(LoginPage.URL)

    # TEST 3: Using validation methods
    print("\n--- Test 3: Validation Methods ---")
    login_page.login_as_invalid_user()

    assert login_page.has_error_containing("invalid")
    print("  ✓ Error contains 'invalid'")

    assert not login_page.is_success_displayed()
    print("  ✓ No success message shown")

    browser.close()

    print("\n" + "=" * 50)
    print("Method Categories:")
    print("=" * 50)
    print("""
    1. NAVIGATION: navigate(), is_loaded()

    2. GRANULAR ACTIONS: enter_username(), click_login_button()
       - Fine-grained control
       - Useful for edge cases

    3. COMBINED ACTIONS: login(), login_as_valid_user()
       - Convenience methods
       - Common workflows

    4. GETTERS: get_page_title(), get_flash_message()
       - Retrieve page data
       - For assertions

    5. VALIDATION: is_error_displayed(), has_error_containing()
       - Boolean checks
       - Simplify test assertions
    """)
