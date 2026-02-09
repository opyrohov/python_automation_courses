"""Example 5: Complete Test Suite

Demonstrates a full test suite combining all concepts:
test functions, fixtures, parametrize, markers, and Page Object Model.

Run with: pytest 05_complete_test_suite.py -v --headed
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# PAGE OBJECT (integrated with pytest)
# ============================================

class LoginPage:
    """Login page object for use with pytest."""

    URL = f"{BASE_URL}/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    def get_flash_text(self):
        return self.flash_message.text_content().strip()

    def has_error(self):
        return "error" in (self.flash_message.get_attribute("class") or "")

    def has_success(self):
        return "success" in (self.flash_message.get_attribute("class") or "")


class SecurePage:
    """Secure area page object."""

    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator("h2")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")

    def get_heading(self):
        return self.heading.text_content().strip()

    def is_logged_in(self):
        return self.logout_button.is_visible()

    def logout(self):
        self.logout_button.click()
        return LoginPage(self.page)


# ============================================
# FIXTURES
# ============================================

@pytest.fixture
def login_page(page: Page):
    """Provide a LoginPage navigated and ready."""
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def secure_page(page: Page):
    """Provide a SecurePage after successful login."""
    lp = LoginPage(page)
    lp.navigate()
    lp.login("tomsmith", "SuperSecretPassword!")
    page.wait_for_url("**/secure")
    return SecurePage(page)


# ============================================
# SMOKE TESTS
# ============================================

@pytest.mark.smoke
def test_login_page_loads(login_page):
    """Verify login page loads with all elements."""
    assert login_page.username_input.is_visible()
    assert login_page.password_input.is_visible()
    assert login_page.login_button.is_visible()


@pytest.mark.smoke
def test_valid_login(login_page):
    """Verify login with correct credentials."""
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.has_success()
    assert "/secure" in login_page.page.url


@pytest.mark.smoke
def test_secure_area_accessible(secure_page):
    """Verify secure area is accessible after login."""
    assert secure_page.is_logged_in()
    assert secure_page.get_heading() == "Secure Area"


@pytest.mark.smoke
def test_logout(secure_page):
    """Verify logout returns to login page."""
    login = secure_page.logout()
    assert "/login" in login.page.url


# ============================================
# REGRESSION TESTS
# ============================================

@pytest.mark.regression
@pytest.mark.parametrize("username,password,error_text", [
    ("wrong", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
])
def test_login_error_messages(login_page, username, password, error_text):
    """Verify correct error messages for invalid credentials."""
    login_page.login(username, password)
    assert login_page.has_error()
    assert error_text in login_page.get_flash_text()


@pytest.mark.regression
def test_login_logout_cycle(login_page):
    """Verify full login-logout cycle."""
    # Login
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "/secure" in login_page.page.url

    # Create secure page and logout
    secure = SecurePage(login_page.page)
    assert secure.is_logged_in()

    result = secure.logout()
    assert "/login" in result.page.url


@pytest.mark.regression
def test_secure_page_heading(secure_page):
    """Verify secure page content."""
    heading = secure_page.get_heading()
    assert heading == "Secure Area"


# ============================================
# PARAMETRIZED TESTS
# ============================================

@pytest.mark.parametrize("page_path,heading_text", [
    ("/login", "Login Page"),
    ("/checkboxes", "Checkboxes"),
    ("/dropdown", "Dropdown List"),
    ("/inputs", "Inputs"),
], ids=["login", "checkboxes", "dropdown", "inputs"])
def test_page_headings(page: Page, page_path, heading_text):
    """Verify page headings across different pages."""
    page.goto(f"{BASE_URL}{page_path}")
    heading = page.locator("h3").first
    assert heading_text in heading.text_content()


# ============================================
# PLAYWRIGHT EXPECT ASSERTIONS
# ============================================

@pytest.mark.smoke
def test_with_expect(page: Page):
    """Using Playwright's expect() for auto-waiting assertions."""
    page.goto(f"{BASE_URL}/login")

    # expect() auto-waits for the condition
    expect(page.locator("h2")).to_have_text("Login Page")
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_enabled()


@pytest.mark.regression
def test_login_with_expect(page: Page):
    """Login test using Playwright expect assertions."""
    page.goto(f"{BASE_URL}/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # expect() waits automatically
    expect(page).to_have_url("**/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


# ============================================
# KEY POINTS:
#
# 1. Page Objects work great with pytest fixtures
# 2. Fixtures provide page objects ready to use
# 3. Combine parametrize + markers + fixtures
# 4. expect() provides auto-waiting assertions
# 5. Organize by smoke / regression
# 6. Each test is independent and isolated
#
# Run all:        pytest 05_complete_test_suite.py -v --headed
# Smoke only:     pytest 05_complete_test_suite.py -v -m smoke --headed
# Regression:     pytest 05_complete_test_suite.py -v -m regression --headed
# By keyword:     pytest 05_complete_test_suite.py -v -k "login" --headed
# ============================================
