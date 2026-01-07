"""Example 1: BasePage Class

Demonstrates how to create a base class with common functionality
that all page objects can inherit from.
"""
from playwright.sync_api import sync_playwright
import os


class BasePage:
    """Base class for all page objects.

    Contains common methods that all pages need.
    """

    def __init__(self, page):
        """Initialize with Playwright page object."""
        self.page = page

    # ==================
    # NAVIGATION
    # ==================
    def get_url(self):
        """Get current URL."""
        return self.page.url

    def get_title(self):
        """Get page title."""
        return self.page.title()

    def go_back(self):
        """Navigate back."""
        self.page.go_back()
        return self

    def go_forward(self):
        """Navigate forward."""
        self.page.go_forward()
        return self

    def refresh(self):
        """Refresh the page."""
        self.page.reload()
        return self

    # ==================
    # SCREENSHOTS
    # ==================
    def take_screenshot(self, name):
        """Take a screenshot."""
        # Create screenshots folder if needed
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{name}.png"
        self.page.screenshot(path=path)
        print(f"Screenshot saved: {path}")
        return self

    # ==================
    # WAITS
    # ==================
    def wait_for_load(self):
        """Wait for page to load completely."""
        self.page.wait_for_load_state("networkidle")
        return self

    def wait_for_url(self, url_pattern):
        """Wait for URL to match pattern."""
        self.page.wait_for_url(url_pattern)
        return self

    # ==================
    # COMMON ACTIONS
    # ==================
    def scroll_to_top(self):
        """Scroll to top of page."""
        self.page.evaluate("window.scrollTo(0, 0)")
        return self

    def scroll_to_bottom(self):
        """Scroll to bottom of page."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        return self


# ============================================
# PAGE THAT INHERITS FROM BASE
# ============================================

class LoginPage(BasePage):
    """Login page inheriting from BasePage."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        # Call parent __init__
        super().__init__(page)

        # Define page-specific locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def navigate(self):
        """Navigate to login page."""
        self.page.goto(self.URL)
        return self

    def enter_credentials(self, username, password):
        """Enter username and password."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        return self

    def click_login(self):
        """Click login button."""
        self.login_button.click()
        return self

    def login(self, username, password):
        """Perform complete login."""
        self.enter_credentials(username, password)
        self.click_login()
        return self

    def get_flash_message(self):
        """Get flash message text."""
        return self.flash_message.text_content().strip()


# ============================================
# DEMO
# ============================================

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=" * 50)
    print("BASEPAGE DEMO")
    print("=" * 50)

    # Create login page (inherits from BasePage)
    login = LoginPage(page)

    # Navigate using page-specific method
    login.navigate()
    print(f"\n1. Page title: {login.get_title()}")
    print(f"   Page URL: {login.get_url()}")

    # Use inherited methods from BasePage
    login.wait_for_load()
    print("2. Page loaded (from BasePage)")

    # Take screenshot using inherited method
    login.take_screenshot("login_page")
    print("3. Screenshot taken (from BasePage)")

    # Use page-specific methods
    login.enter_credentials("tomsmith", "SuperSecretPassword!")
    print("4. Credentials entered (from LoginPage)")

    # Scroll using inherited method
    login.scroll_to_bottom()
    print("5. Scrolled to bottom (from BasePage)")

    login.scroll_to_top()
    print("6. Scrolled to top (from BasePage)")

    # Login
    login.click_login()
    print("7. Logged in")

    # Refresh using inherited method
    login.refresh()
    print("8. Page refreshed (from BasePage)")

    browser.close()

    print("\n" + "=" * 50)
    print("""
BASEPAGE BENEFITS:

1. DRY (Don't Repeat Yourself)
   - Common methods written once
   - All pages inherit them

2. CONSISTENCY
   - Same API across all pages
   - Predictable behavior

3. MAINTAINABILITY
   - Change once, affects all pages
   - Easy to add new common methods

4. EXTENSIBILITY
   - Pages add their own methods
   - Override base methods if needed
""")
