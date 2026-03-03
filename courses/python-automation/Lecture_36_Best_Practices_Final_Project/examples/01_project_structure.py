"""Example 1: Project Structure Best Practices

Demonstrates how to organize a scalable Playwright test project
with proper separation of concerns.

Run with:
    pytest 01_project_structure.py -v -s
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# RECOMMENDED PROJECT STRUCTURE
# ============================================
#
# my_automation_project/
# │
# ├── tests/                     # All test files
# │   ├── conftest.py           # Shared fixtures & hooks
# │   ├── test_login.py         # Login feature tests
# │   ├── test_checkboxes.py    # Checkbox feature tests
# │   └── test_dropdown.py      # Dropdown feature tests
# │
# ├── pages/                     # Page Object Model
# │   ├── __init__.py
# │   ├── base_page.py          # Base class for all pages
# │   ├── login_page.py         # Login page actions & locators
# │   └── secure_page.py        # Secure area page
# │
# ├── fixtures/                  # Custom fixtures
# │   ├── __init__.py
# │   └── data_fixtures.py      # Test data generators
# │
# ├── test_data/                 # Static test data
# │   ├── users.json
# │   └── config.json
# │
# ├── reports/                   # Test reports (gitignored)
# │
# ├── pytest.ini                 # Pytest configuration
# ├── requirements.txt           # Dependencies
# ├── .env                       # Environment variables
# └── README.md                  # Project documentation


# ============================================
# PRINCIPLE 1: ONE TEST = ONE THING
# ============================================

def test_login_page_displays_form(page: Page):
    """Test ONLY that the form is visible."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("button[type='submit']").is_visible()


def test_login_page_has_correct_heading(page: Page):
    """Test ONLY the heading text."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("h2").text_content() == "Login Page"


# ============================================
# PRINCIPLE 2: ARRANGE - ACT - ASSERT
# ============================================

def test_successful_login_aaa_pattern(page: Page):
    """Follow the Arrange-Act-Assert pattern."""
    # ARRANGE: Set up preconditions
    page.goto(f"{BASE_URL}/login")
    username = "tomsmith"
    password = "SuperSecretPassword!"

    # ACT: Perform the action under test
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    # ASSERT: Verify the expected outcome
    assert "/secure" in page.url
    assert "You logged into a secure area!" in page.locator("#flash").text_content()


# ============================================
# PRINCIPLE 3: DESCRIPTIVE TEST NAMES
# ============================================

# BAD names:
# def test_1(page): ...
# def test_login(page): ...
# def test_it_works(page): ...

# GOOD names (describe what is tested and expected outcome):
def test_login_with_valid_credentials_redirects_to_secure_area(page: Page):
    """Name tells you what's tested and what's expected."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


def test_login_with_invalid_username_shows_error_message(page: Page):
    """Clear naming: input condition + expected result."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("invalid")
    page.locator("#password").fill("invalid")
    page.locator("button[type='submit']").click()
    assert "Your username is invalid!" in page.locator("#flash").text_content()


# ============================================
# PRINCIPLE 4: INDEPENDENT TESTS
# ============================================

# BAD: Tests depend on each other
# def test_step_1_open_page(page): ...
# def test_step_2_fill_form(page): ...  # Needs step 1!
# def test_step_3_submit(page): ...     # Needs step 2!

# GOOD: Each test is self-contained
def test_checkbox_can_be_checked(page: Page):
    """This test stands alone - no dependency on other tests."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()
    assert checkbox.is_checked()


def test_checkbox_can_be_unchecked(page: Page):
    """Independent of the previous test - fresh page state."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkbox = page.locator("input[type='checkbox']").nth(1)
    checkbox.uncheck()
    assert not checkbox.is_checked()


# ============================================
# PRINCIPLE 5: USE CONSTANTS FOR SHARED VALUES
# ============================================

# Define URLs, selectors, and test data as constants
LOGIN_URL = f"{BASE_URL}/login"
SECURE_URL = f"{BASE_URL}/secure"
VALID_USER = "tomsmith"
VALID_PASS = "SuperSecretPassword!"


def test_login_with_constants(page: Page):
    """Using constants makes tests easier to maintain."""
    page.goto(LOGIN_URL)
    page.locator("#username").fill(VALID_USER)
    page.locator("#password").fill(VALID_PASS)
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


# ============================================
# KEY POINTS:
#
# 1. Organize files by feature (test_login.py, test_cart.py)
# 2. One test = one thing to verify
# 3. Follow Arrange-Act-Assert pattern
# 4. Use descriptive test names
# 5. Keep tests independent (no shared state)
# 6. Use constants for repeated values
# 7. Keep test files focused and small
#
# Run: pytest 01_project_structure.py -v
# ============================================
