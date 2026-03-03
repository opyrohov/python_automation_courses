"""Example 2: Pytest Fixtures with Playwright

Demonstrates how fixtures provide reusable setup/teardown logic.
Playwright's pytest plugin provides built-in fixtures: page, context, browser.

Run with: pytest 02_pytest_fixtures.py -v --headed
"""
import pytest
from playwright.sync_api import Page, BrowserContext, Browser


# ============================================
# BUILT-IN FIXTURES: page, context, browser
# ============================================

def test_page_fixture(page: Page):
    """The 'page' fixture gives a fresh browser tab."""
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"
    # page is automatically closed after this test


def test_context_fixture(context: BrowserContext):
    """The 'context' fixture gives a browser context (like incognito).

    You can create multiple pages from one context.
    """
    # Create two pages in the same context
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://the-internet.herokuapp.com")
    page2.goto("https://the-internet.herokuapp.com/login")

    assert page1.title() == "The Internet"
    assert "Login" in page2.locator("h2").text_content()


def test_browser_fixture(browser: Browser):
    """The 'browser' fixture gives the browser instance.

    You can create custom contexts with specific settings.
    """
    # Create context with custom viewport
    context = browser.new_context(
        viewport={"width": 375, "height": 812}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"
    context.close()


# ============================================
# CUSTOM FIXTURES
# ============================================

@pytest.fixture
def login_page(page: Page):
    """Fixture that navigates to the login page."""
    page.goto("https://the-internet.herokuapp.com/login")
    return page


@pytest.fixture
def logged_in_page(page: Page):
    """Fixture that performs login and returns authenticated page."""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/secure")
    return page


# ============================================
# TESTS USING CUSTOM FIXTURES
# ============================================

def test_login_form_visible(login_page):
    """Test that login form elements are visible."""
    assert login_page.locator("#username").is_visible()
    assert login_page.locator("#password").is_visible()
    assert login_page.locator("button[type='submit']").is_visible()


def test_login_page_heading(login_page):
    """Test login page heading."""
    heading = login_page.locator("h2")
    assert heading.text_content() == "Login Page"


def test_secure_area_accessible(logged_in_page):
    """Test that secure area is accessible after login."""
    assert "/secure" in logged_in_page.url
    heading = logged_in_page.locator("h2")
    assert heading.text_content().strip() == "Secure Area"


def test_logout_button_visible(logged_in_page):
    """Test that logout button is visible after login."""
    logout = logged_in_page.locator("a[href='/logout']")
    assert logout.is_visible()


# ============================================
# FIXTURE WITH YIELD (SETUP + TEARDOWN)
# ============================================

@pytest.fixture
def checkbox_page(page: Page):
    """Fixture with setup and teardown using yield."""
    # SETUP: Navigate to checkboxes page
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    print("\n[Setup] Navigated to checkboxes page")

    yield page  # Test runs here

    # TEARDOWN: Runs after test completes
    print("[Teardown] Checkbox test completed")


def test_checkboxes_exist(checkbox_page):
    """Test using fixture with yield."""
    checkboxes = checkbox_page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


# ============================================
# KEY POINTS:
#
# 1. Built-in fixtures: page, context, browser
# 2. Each test gets a FRESH page (isolation)
# 3. Custom fixtures with @pytest.fixture
# 4. Fixtures can use other fixtures (page)
# 5. yield for setup + teardown
# 6. conftest.py shares fixtures across files
#
# Run: pytest 02_pytest_fixtures.py -v --headed -s
# ============================================
