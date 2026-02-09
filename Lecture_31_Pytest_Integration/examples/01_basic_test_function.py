"""Example 1: Basic Pytest Test Functions

Demonstrates how to write your first pytest tests with Playwright.
Instead of running scripts manually, pytest discovers and runs tests automatically.

Run with: pytest 01_basic_test_function.py -v --headed
"""
from playwright.sync_api import Page


# ============================================
# BASIC TEST FUNCTIONS
# ============================================

def test_page_title(page: Page):
    """Test that the page has the correct title."""
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"


def test_page_has_heading(page: Page):
    """Test that the main heading is visible."""
    page.goto("https://the-internet.herokuapp.com")
    heading = page.locator("h1")
    assert heading.is_visible()
    assert heading.text_content() == "Welcome to the-internet"


def test_page_has_links(page: Page):
    """Test that the page contains navigation links."""
    page.goto("https://the-internet.herokuapp.com")
    links = page.locator("#content ul li a")
    assert links.count() > 0


# ============================================
# LOGIN PAGE TESTS
# ============================================

def test_login_page_loads(page: Page):
    """Test that login page loads correctly."""
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.locator("h2").text_content() == "Login Page"
    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()


def test_successful_login(page: Page):
    """Test login with valid credentials."""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # Verify we're on the secure page
    assert "/secure" in page.url
    assert "You logged into a secure area!" in page.locator("#flash").text_content()


def test_failed_login(page: Page):
    """Test login with invalid credentials."""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wrong_user")
    page.locator("#password").fill("wrong_pass")
    page.locator("button[type='submit']").click()

    # Verify we stay on login page with error
    assert "/login" in page.url
    assert "Your username is invalid!" in page.locator("#flash").text_content()


# ============================================
# KEY POINTS:
#
# 1. File name starts with test_ (test_*.py)
# 2. Function names start with test_
# 3. 'page' parameter = automatic Playwright fixture
# 4. Use 'assert' for verification
# 5. Each test gets a FRESH page (isolated)
# 6. Browser opens/closes automatically
#
# Run: pytest 01_basic_test_function.py -v --headed
# ============================================
