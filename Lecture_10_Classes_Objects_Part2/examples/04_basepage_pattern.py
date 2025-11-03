"""
Lecture 10 - Example 4: BasePage Pattern
========================================
Learn the BasePage pattern for building reusable page objects.
"""

print("=" * 60)
print("BASEPAGE PATTERN FOR PLAYWRIGHT")
print("=" * 60)
print()

# What is the BasePage Pattern?
# =============================
# The BasePage pattern is a design where you create a base class
# containing common functionality used by all page objects.
# Every page object then inherits from this base class.

print("1. Creating a BasePage Class")
print("-" * 60)


class BasePage:
    """
    Base class for all page objects.
    Contains common functionality used across all pages.
    """

    def __init__(self, page):
        """
        Initialize base page.

        Args:
            page: Playwright page instance
        """
        self.page = page

    def navigate_to(self, url):
        """Navigate to a URL."""
        print(f"🌐 Navigating to: {url}")
        # self.page.goto(url)

    def get_title(self):
        """Get page title."""
        # return self.page.title()
        return "Page Title"

    def get_url(self):
        """Get current URL."""
        # return self.page.url
        return "https://example.com"

    def click_element(self, selector):
        """Click an element."""
        print(f"🖱️  Clicking: {selector}")
        # self.page.click(selector)

    def fill_input(self, selector, text):
        """Fill an input field."""
        print(f"⌨️  Filling '{selector}' with: {text}")
        # self.page.fill(selector, text)

    def get_text(self, selector):
        """Get text from element."""
        # return self.page.locator(selector).text_content()
        return "Sample Text"

    def is_visible(self, selector):
        """Check if element is visible."""
        # return self.page.is_visible(selector)
        return True

    def wait_for_selector(self, selector, timeout=30000):
        """Wait for element to appear."""
        print(f"⏳ Waiting for: {selector}")
        # self.page.wait_for_selector(selector, timeout=timeout)

    def take_screenshot(self, filename):
        """Take a screenshot."""
        print(f"📸 Taking screenshot: {filename}")
        # self.page.screenshot(path=filename)


print("✅ BasePage created with common methods")
print()
print("-" * 60)
print()

# Example 2: Using BasePage in Page Objects
# =========================================
print("2. Creating Page Objects from BasePage")
print("-" * 60)


class LoginPage(BasePage):
    """Login page inheriting from BasePage."""

    def __init__(self, page):
        super().__init__(page)
        # Define page-specific selectors
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "button[type='submit']"
        self.error_message = ".error-message"

    def login(self, username, password):
        """
        Perform login action.
        Uses inherited methods from BasePage!
        """
        print(f"🔐 Logging in as: {username}")
        # Use parent's fill_input method
        self.fill_input(self.username_input, username)
        self.fill_input(self.password_input, password)
        # Use parent's click_element method
        self.click_element(self.submit_button)

    def get_error_message(self):
        """Get error message text."""
        # Use parent's get_text method
        return self.get_text(self.error_message)

    def is_error_visible(self):
        """Check if error message is visible."""
        # Use parent's is_visible method
        return self.is_visible(self.error_message)


class HomePage(BasePage):
    """Home page inheriting from BasePage."""

    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = ".welcome"
        self.logout_button = "#logout"
        self.profile_link = "a[href='/profile']"
        self.settings_link = "a[href='/settings']"

    def get_welcome_text(self):
        """Get welcome message."""
        return self.get_text(self.welcome_message)

    def logout(self):
        """Click logout button."""
        print("🚪 Logging out")
        self.click_element(self.logout_button)

    def go_to_profile(self):
        """Navigate to profile."""
        self.click_element(self.profile_link)

    def go_to_settings(self):
        """Navigate to settings."""
        self.click_element(self.settings_link)


# Simulate usage
class FakePage:
    pass


page = FakePage()
login_page = LoginPage(page)
login_page.login("testuser", "password123")

print()
print("-" * 60)
print()

# Example 3: Enhanced BasePage with More Features
# ===============================================
print("3. Enhanced BasePage with Advanced Features")
print("-" * 60)


class EnhancedBasePage:
    """Enhanced base page with more utility methods."""

    def __init__(self, page):
        self.page = page

    # Navigation methods
    def navigate_to(self, url):
        """Navigate to URL."""
        print(f"🌐 Navigating to: {url}")

    def go_back(self):
        """Go back in browser history."""
        print("⬅️  Going back")
        # self.page.go_back()

    def refresh(self):
        """Refresh the page."""
        print("🔄 Refreshing page")
        # self.page.reload()

    # Interaction methods
    def click(self, selector):
        """Click element with logging."""
        print(f"🖱️  Clicking: {selector}")
        # self.page.click(selector)

    def double_click(self, selector):
        """Double click element."""
        print(f"🖱️  Double clicking: {selector}")
        # self.page.dblclick(selector)

    def hover(self, selector):
        """Hover over element."""
        print(f"👆 Hovering: {selector}")
        # self.page.hover(selector)

    # Form methods
    def fill(self, selector, text):
        """Fill input field."""
        print(f"⌨️  Filling '{selector}' with '{text}'")

    def check(self, selector):
        """Check a checkbox."""
        print(f"☑️  Checking: {selector}")
        # self.page.check(selector)

    def select_option(self, selector, value):
        """Select from dropdown."""
        print(f"📋 Selecting '{value}' in {selector}")
        # self.page.select_option(selector, value)

    # Wait methods
    def wait_for_element(self, selector, timeout=30000):
        """Wait for element."""
        print(f"⏳ Waiting for: {selector}")

    def wait_for_page_load(self):
        """Wait for page to fully load."""
        print("⏳ Waiting for page load...")
        # self.page.wait_for_load_state("networkidle")

    # Assertion helpers
    def is_element_visible(self, selector):
        """Check if element is visible."""
        return True  # self.page.is_visible(selector)

    def get_element_text(self, selector):
        """Get element text content."""
        return "Sample Text"  # self.page.locator(selector).text_content()

    def get_element_count(self, selector):
        """Get count of elements matching selector."""
        return 1  # self.page.locator(selector).count()

    # Screenshot and debugging
    def screenshot(self, name):
        """Take screenshot."""
        print(f"📸 Screenshot: {name}.png")

    def scroll_to_element(self, selector):
        """Scroll element into view."""
        print(f"📜 Scrolling to: {selector}")
        # self.page.locator(selector).scroll_into_view_if_needed()


print("✅ Enhanced BasePage with 20+ utility methods")
print()
print("-" * 60)
print()

# Example 4: Specialized Base Classes
# ===================================
print("4. Creating Specialized Base Classes")
print("-" * 60)


class AuthBasePage(EnhancedBasePage):
    """Base page for authenticated pages."""

    def __init__(self, page):
        super().__init__(page)
        self.header_user_menu = ".user-menu"
        self.logout_link = "#logout"

    def verify_logged_in(self):
        """Verify user is logged in."""
        print("✅ Verifying user is logged in")
        return self.is_element_visible(self.header_user_menu)

    def get_current_user(self):
        """Get currently logged in username."""
        return self.get_element_text(self.header_user_menu)

    def logout(self):
        """Logout from any authenticated page."""
        print("🚪 Logging out")
        self.click(self.logout_link)


class DashboardPage(AuthBasePage):
    """Dashboard page - inherits authentication checks."""

    def __init__(self, page):
        super().__init__(page)
        self.stats_widget = ".statistics"
        self.chart_widget = ".chart"

    def get_statistics(self):
        """Get dashboard statistics."""
        # Has access to all EnhancedBasePage AND AuthBasePage methods!
        self.wait_for_element(self.stats_widget)
        return self.get_element_text(self.stats_widget)


dashboard = DashboardPage(FakePage())
dashboard.verify_logged_in()  # From AuthBasePage
dashboard.wait_for_element(".statistics")  # From EnhancedBasePage
dashboard.get_statistics()  # From DashboardPage

print()
print("-" * 60)
print()

# Example 5: Complete Real-World Example
# ======================================
print("5. Complete Page Object Hierarchy")
print("-" * 60)


class RealBasePage:
    """Production-ready base page."""

    def __init__(self, page, url=None):
        self.page = page
        self.url = url

    def open(self):
        """Open the page."""
        if self.url:
            print(f"🌐 Opening: {self.url}")
            # self.page.goto(self.url)
        else:
            raise ValueError("URL not set for this page")

    def click(self, selector):
        """Click with error handling."""
        try:
            print(f"🖱️  Clicking: {selector}")
            # self.page.click(selector)
        except Exception as e:
            print(f"❌ Failed to click {selector}: {e}")
            self.screenshot("click_error")
            raise

    def fill(self, selector, value):
        """Fill with error handling."""
        try:
            print(f"⌨️  Filling '{selector}' with '{value}'")
            # self.page.fill(selector, value)
        except Exception as e:
            print(f"❌ Failed to fill {selector}: {e}")
            self.screenshot("fill_error")
            raise

    def screenshot(self, name):
        """Take screenshot with timestamp."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        print(f"📸 Screenshot saved: {filename}")
        # self.page.screenshot(path=f"screenshots/{filename}")


class RealLoginPage(RealBasePage):
    """Production login page."""

    def __init__(self, page):
        super().__init__(page, url="https://example.com/login")
        self.username_field = "#email"
        self.password_field = "#password"
        self.login_button = "button[type='submit']"

    def login_as(self, username, password):
        """Complete login flow with error handling."""
        print(f"\n🔐 Login Flow Started for: {username}")
        print("=" * 50)

        try:
            # Open the page
            self.open()

            # Fill credentials
            self.fill(self.username_field, username)
            self.fill(self.password_field, "******")

            # Submit
            self.click(self.login_button)

            print("✅ Login completed successfully")
            print("=" * 50)

        except Exception as e:
            print(f"❌ Login failed: {e}")
            print("=" * 50)
            raise


# Use it
login = RealLoginPage(FakePage())
login.login_as("test@example.com", "password123")

print()
print("-" * 60)
print()

# Benefits Summary
# ===============
print("=" * 60)
print("BASEPAGE PATTERN BENEFITS")
print("=" * 60)
print()
print("✅ CODE REUSE")
print("   - Write common methods once")
print("   - All pages inherit them automatically")
print()
print("✅ CONSISTENCY")
print("   - Same behavior across all pages")
print("   - Standardized method names")
print()
print("✅ MAINTAINABILITY")
print("   - Update BasePage to update all pages")
print("   - Single point of change")
print()
print("✅ ERROR HANDLING")
print("   - Centralized error handling")
print("   - Automatic screenshots on failure")
print()
print("✅ TESTING")
print("   - Easier to test common functionality")
print("   - Mock BasePage for unit tests")
print()
print("=" * 60)

print()
print("=" * 60)
print("Key Takeaways:")
print("- BasePage contains methods ALL pages need")
print("- Every page object inherits from BasePage")
print("- Reduces code duplication significantly")
print("- Makes maintenance much easier")
print("- Industry standard pattern for Playwright/Selenium")
print("=" * 60)
