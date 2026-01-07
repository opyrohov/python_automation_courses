"""Example 3: Page Transitions

Demonstrates how page object methods can return different page objects
when navigating between pages (e.g., login returns SecurePage).
"""
from playwright.sync_api import sync_playwright


# ============================================
# BASE PAGE
# ============================================

class BasePage:
    """Base page for common functionality."""

    def __init__(self, page):
        self.page = page

    def get_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()


# ============================================
# LOGIN PAGE
# ============================================

class LoginPage(BasePage):
    """Login page with transition to SecurePage."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

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
        """Click login - check which page we land on."""
        self.login_button.click()

        # Return appropriate page based on result
        if "/secure" in self.page.url:
            return SecurePage(self.page)
        else:
            return self  # Stay on login page (error)

    def login(self, username, password):
        """Complete login flow - returns SecurePage on success."""
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()

    def login_expecting_error(self, username, password):
        """Login expecting failure - always returns LoginPage."""
        self.enter_username(username)
        self.enter_password(password)
        self.login_button.click()
        return self  # Expect to stay on login

    def get_error_message(self):
        """Get error message text."""
        return self.flash.text_content().strip()

    def has_error(self):
        """Check if error is displayed."""
        return self.flash.is_visible() and "error" in self.flash.get_attribute("class")


# ============================================
# SECURE PAGE (AFTER LOGIN)
# ============================================

class SecurePage(BasePage):
    """Secure area page - accessible after login."""

    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h2")
        self.flash = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")
        self.content = page.locator("#content")

    def get_heading(self):
        """Get page heading."""
        return self.heading.text_content()

    def get_welcome_message(self):
        """Get welcome/flash message."""
        return self.flash.text_content().strip()

    def is_logged_in(self):
        """Verify user is logged in."""
        return self.logout_button.is_visible()

    def logout(self):
        """Logout and return to LoginPage."""
        self.logout_button.click()
        return LoginPage(self.page)


# ============================================
# DEMO: PAGE TRANSITIONS
# ============================================

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=" * 60)
    print("PAGE TRANSITIONS DEMO")
    print("=" * 60)

    # --- Example 1: Successful Login Transition ---
    print("\n--- Example 1: Successful Login ---")

    # Start on LoginPage
    login_page = LoginPage(page)
    login_page.navigate()
    print(f"1. On: {login_page.__class__.__name__}")

    # login() returns SecurePage on success
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # Now we have a SecurePage object!
    print(f"2. Transitioned to: {secure_page.__class__.__name__}")
    print(f"   Is logged in: {secure_page.is_logged_in()}")
    print(f"   Heading: {secure_page.get_heading()}")

    # --- Example 2: Logout Transition ---
    print("\n--- Example 2: Logout ---")

    # logout() returns LoginPage
    login_page = secure_page.logout()

    print(f"3. Transitioned to: {login_page.__class__.__name__}")
    print(f"   URL: {login_page.get_url()}")

    # --- Example 3: Failed Login (No Transition) ---
    print("\n--- Example 3: Failed Login ---")

    # Login with bad credentials
    login_page.navigate()
    result_page = login_page.login("wrong", "wrong")

    # result_page is still LoginPage (no transition)
    print(f"4. Still on: {result_page.__class__.__name__}")
    print(f"   Has error: {result_page.has_error()}")

    # --- Example 4: Method Chaining with Transitions ---
    print("\n--- Example 4: Fluent Login Flow ---")

    # Chain through multiple pages
    secure = (LoginPage(page)
              .navigate()
              .enter_username("tomsmith")
              .enter_password("SuperSecretPassword!")
              .click_login())

    print(f"5. After chaining: {secure.__class__.__name__}")

    # Chain logout
    login = secure.logout()
    print(f"6. After logout: {login.__class__.__name__}")

    browser.close()

    print("\n" + "=" * 60)
    print("""
PAGE TRANSITION PATTERNS:

1. RETURN DIFFERENT PAGE ON SUCCESS
   def login(self, user, pwd):
       ...
       if success:
           return SecurePage(self.page)
       return self  # Stay on current page

2. ALWAYS RETURN SPECIFIC PAGE
   def logout(self):
       self.logout_btn.click()
       return LoginPage(self.page)  # Always returns LoginPage

3. EXPECT ERROR (STAY ON SAME PAGE)
   def login_expecting_error(self, user, pwd):
       ...
       return self  # Explicitly stay here

4. TYPE HINTS (Optional but helpful)
   def login(self) -> 'SecurePage':
       ...

BENEFITS:
- Type safety
- IDE autocomplete
- Clear navigation flow
- Tests read like user stories
""")
