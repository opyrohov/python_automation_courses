"""Example 5: Complete Page Object Implementation

A complete, production-ready example with:
- Multiple page objects
- Proper project structure simulation
- Real test scenarios
"""
from playwright.sync_api import sync_playwright, expect


# ============================================
# PAGE OBJECTS
# ============================================

class BasePage:
    """Base class for all page objects."""

    def __init__(self, page):
        self.page = page

    def get_title(self):
        """Get page title."""
        return self.page.title()

    def get_url(self):
        """Get current URL."""
        return self.page.url


class LoginPage(BasePage):
    """Login Page Object."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")
        self.page_heading = page.locator("h2")

    def navigate(self):
        """Navigate to login page."""
        self.page.goto(self.URL)
        return self

    def enter_username(self, username):
        """Enter username."""
        self.username_input.fill(username)
        return self

    def enter_password(self, password):
        """Enter password."""
        self.password_input.fill(password)
        return self

    def click_login(self):
        """Click login button."""
        self.login_button.click()
        return self

    def login(self, username, password):
        """Perform login and return SecurePage if successful."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        # Return appropriate page based on result
        if "/secure" in self.page.url:
            return SecurePage(self.page)
        return self

    def login_expecting_error(self, username, password):
        """Login expecting failure, stay on LoginPage."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_flash_message(self):
        """Get flash message text."""
        return self.flash_message.text_content().strip()

    def has_error(self):
        """Check for error message."""
        return "error" in self.flash_message.get_attribute("class")

    def has_success(self):
        """Check for success message."""
        return "success" in self.flash_message.get_attribute("class")


class SecurePage(BasePage):
    """Secure Area Page Object."""

    def __init__(self, page):
        super().__init__(page)

        self.page_heading = page.locator("h2")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")

    def get_heading(self):
        """Get page heading."""
        return self.page_heading.text_content()

    def get_flash_message(self):
        """Get flash message."""
        return self.flash_message.text_content().strip()

    def logout(self):
        """Logout and return to LoginPage."""
        self.logout_button.click()
        return LoginPage(self.page)

    def is_logged_in(self):
        """Verify user is logged in."""
        return "/secure" in self.page.url and self.logout_button.is_visible()


# ============================================
# TEST SUITE
# ============================================

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=" * 60)
    print("COMPLETE PAGE OBJECT MODEL DEMO")
    print("=" * 60)

    # ==================
    # TEST 1: Successful Login
    # ==================
    print("\n--- TEST 1: Successful Login ---")

    login_page = LoginPage(page)
    login_page.navigate()

    # Verify we're on login page
    assert "Login" in login_page.get_title()
    print("  ✓ On login page")

    # Perform login
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # Verify successful login
    assert secure_page.is_logged_in()
    print(f"  ✓ Logged in successfully")
    print(f"    Heading: {secure_page.get_heading()}")

    # ==================
    # TEST 2: Logout
    # ==================
    print("\n--- TEST 2: Logout ---")

    returned_login = secure_page.logout()
    assert not returned_login.has_error()
    print("  ✓ Logged out successfully")

    # ==================
    # TEST 3: Invalid Credentials
    # ==================
    print("\n--- TEST 3: Invalid Credentials ---")

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_expecting_error("invalid_user", "invalid_pass")

    assert login_page.has_error()
    error_msg = login_page.get_flash_message()
    assert "invalid" in error_msg.lower()
    print(f"  ✓ Error displayed: {error_msg[:40]}...")

    # ==================
    # TEST 4: Empty Credentials
    # ==================
    print("\n--- TEST 4: Empty Credentials ---")

    login_page.navigate()
    login_page.login_expecting_error("", "")

    assert login_page.has_error()
    print("  ✓ Error displayed for empty credentials")

    # ==================
    # TEST 5: Method Chaining
    # ==================
    print("\n--- TEST 5: Method Chaining ---")

    result = (LoginPage(page)
              .navigate()
              .enter_username("tomsmith")
              .enter_password("SuperSecretPassword!")
              .click_login())

    page.wait_for_url("**/secure")
    print("  ✓ Login via method chaining")

    # ==================
    # TEST 6: Full User Journey
    # ==================
    print("\n--- TEST 6: Full User Journey ---")

    # Start fresh
    login = LoginPage(page)
    login.navigate()
    print("  1. Navigated to login")

    # Try invalid first
    login.login_expecting_error("wrong", "wrong")
    assert login.has_error()
    print("  2. Invalid login rejected")

    # Then valid login
    secure = login.login("tomsmith", "SuperSecretPassword!")
    assert secure.is_logged_in()
    print("  3. Valid login succeeded")

    # Access secure content
    heading = secure.get_heading()
    print(f"  4. Accessed: {heading}")

    # Logout
    login = secure.logout()
    print("  5. Logged out")

    # Verify back on login
    assert login.page.url.endswith("/login")
    print("  6. Back on login page")

    print("\n  ✓ Full user journey completed!")

    browser.close()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("""
    This example demonstrated:

    1. BASE PAGE CLASS
       - Common methods for all pages
       - Inheritance reduces duplication

    2. MULTIPLE PAGE OBJECTS
       - LoginPage, SecurePage
       - Each page has its own class

    3. PAGE TRANSITIONS
       - login() returns SecurePage
       - logout() returns LoginPage

    4. VALIDATION METHODS
       - is_logged_in(), has_error()
       - Simplify test assertions

    5. FLUENT INTERFACE
       - Method chaining for readability
       - return self pattern

    6. REAL TEST SCENARIOS
       - Success, failure, edge cases
       - Full user journeys
    """)
