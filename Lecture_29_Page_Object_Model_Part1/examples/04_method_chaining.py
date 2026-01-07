"""Example 4: Method Chaining (Fluent Interface)

Shows how to implement method chaining for more readable code.
Each method returns 'self' to allow chaining.
"""
from playwright.sync_api import sync_playwright, expect


class LoginPage:
    """Login Page with fluent interface (method chaining)."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".flash.error")
        self.success_message = page.locator(".flash.success")

    def navigate(self):
        """Navigate to login page."""
        self.page.goto(self.URL)
        return self  # Return self for chaining

    def enter_username(self, username):
        """Enter username."""
        self.username_input.fill(username)
        return self  # Return self for chaining

    def enter_password(self, password):
        """Enter password."""
        self.password_input.fill(password)
        return self  # Return self for chaining

    def click_login(self):
        """Click login button."""
        self.login_button.click()
        return self  # Return self for chaining

    def wait_for_error(self):
        """Wait for error message to appear."""
        self.error_message.wait_for(state="visible")
        return self

    def wait_for_success(self):
        """Wait for success message to appear."""
        self.success_message.wait_for(state="visible")
        return self

    def clear_form(self):
        """Clear both input fields."""
        self.username_input.clear()
        self.password_input.clear()
        return self

    # Combined method also returns self
    def login(self, username, password):
        """Perform login."""
        return (self
                .enter_username(username)
                .enter_password(password)
                .click_login())

    # Getter methods don't return self (they return data)
    def get_error_text(self):
        """Get error message text."""
        return self.error_message.text_content()

    def is_error_visible(self):
        """Check if error is visible."""
        return self.error_message.is_visible()


class SecurePage:
    """Secure Page (after login)."""

    def __init__(self, page):
        self.page = page
        self.logout_button = page.locator("a[href='/logout']")
        self.welcome_message = page.locator("h2")
        self.success_message = page.locator(".flash.success")

    def logout(self):
        """Click logout button."""
        self.logout_button.click()
        return LoginPage(self.page)  # Return to login page

    def get_welcome_text(self):
        """Get welcome message."""
        return self.welcome_message.text_content()


# ============================================
# TESTS WITH METHOD CHAINING
# ============================================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Method Chaining Demo ===\n")

    # TEST 1: Chained methods
    print("--- Test 1: Chained Login ---")

    login_page = LoginPage(page)

    # Without chaining (verbose)
    # login_page.navigate()
    # login_page.enter_username("tomsmith")
    # login_page.enter_password("SuperSecretPassword!")
    # login_page.click_login()

    # With chaining (fluent)
    login_page.navigate().enter_username("tomsmith").enter_password("SuperSecretPassword!").click_login()

    page.wait_for_url("**/secure")
    print("  ✓ Logged in with chained methods")

    # TEST 2: Multi-line chaining (more readable)
    print("\n--- Test 2: Multi-line Chaining ---")

    page.goto(LoginPage.URL)

    (LoginPage(page)
        .navigate()
        .enter_username("wronguser")
        .enter_password("wrongpass")
        .click_login()
        .wait_for_error())

    print("  ✓ Error displayed with chained methods")

    # TEST 3: Chaining with assertions
    print("\n--- Test 3: Chaining + Assertions ---")

    login = LoginPage(page)
    (login
        .navigate()
        .clear_form()
        .enter_username("tomsmith")
        .enter_password("SuperSecretPassword!")
        .click_login())

    page.wait_for_url("**/secure")
    secure = SecurePage(page)
    print(f"  Welcome: {secure.get_welcome_text()}")

    # TEST 4: Page transitions
    print("\n--- Test 4: Page Transitions ---")

    # Logout returns LoginPage
    returned_login = secure.logout()
    assert returned_login.page.url.endswith("/login")
    print("  ✓ Logged out, returned to login page")

    browser.close()

    print("\n" + "=" * 50)
    print("Method Chaining Benefits:")
    print("=" * 50)
    print("""
    1. READABLE CODE:
       login_page.navigate().login("user", "pass")

    2. FLUENT INTERFACE:
       Reads like natural language

    3. MULTI-LINE FORMATTING:
       (page
           .navigate()
           .enter_username("user")
           .click_login())

    4. IMPORTANT RULE:
       - Action methods return 'self'
       - Getter methods return data
       - Page transition methods return new page object

    5. WHEN NOT TO CHAIN:
       - When you need the return value
       - When readability suffers
    """)
