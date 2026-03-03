"""Exercise 2: Final Project - Complete Test Suite

Build a comprehensive, well-structured test suite for
https://the-internet.herokuapp.com

This is your final project for the course!

Requirements:
1. Test at least 5 different pages/features
2. Use Page Object Model for at least 2 pages
3. Use fixtures (conftest.py) for shared setup
4. Use parametrize for data-driven tests
5. Use markers (smoke, regression)
6. Add tracing/screenshot on failure
7. Follow all best practices from this lecture

Target site: https://the-internet.herokuapp.com

Run with:
    pytest exercise_02_final_project.py -v
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# PART 1: PAGE OBJECTS (create these)
# ============================================

# TODO: Create LoginPage class
# - navigate() method
# - login(username, password) method
# - get_flash_message() method
# - is_logged_in() property

# TODO: Create CheckboxesPage class
# - navigate() method
# - check(index) method
# - uncheck(index) method
# - is_checked(index) method
# - count() property


# ============================================
# PART 2: FIXTURES (create conftest.py)
# ============================================

# TODO: Create conftest.py with:
# - base_url fixture (session scope)
# - login_page fixture (returns LoginPage object)
# - checkboxes_page fixture (returns CheckboxesPage object)
# - authenticated_page fixture (logged-in page)
# - screenshot_on_failure fixture (saves screenshot if test fails)
# - pytest_runtest_makereport hook


# ============================================
# PART 3: SMOKE TESTS
# ============================================

@pytest.mark.smoke
def test_homepage_loads(page: Page):
    """Verify homepage is accessible."""
    page.goto(BASE_URL)
    expect(page).to_have_title("The Internet")


@pytest.mark.smoke
def test_login_page_accessible(page: Page):
    """Verify login page loads correctly."""
    page.goto(f"{BASE_URL}/login")
    expect(page.locator("h2")).to_have_text("Login Page")
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()


# ============================================
# PART 4: LOGIN TESTS
# ============================================

# TODO: Implement these tests using LoginPage page object

@pytest.mark.regression
@pytest.mark.parametrize("username,password,should_succeed", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("tomsmith", "wrong", False),
    ("wrong", "SuperSecretPassword!", False),
    ("", "", False),
])
def test_login_scenarios(page: Page, username, password, should_succeed):
    """Test various login scenarios."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if should_succeed:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# PART 5: CHECKBOX TESTS
# ============================================

# TODO: Implement using CheckboxesPage page object

@pytest.mark.regression
def test_checkbox_check_uncheck(page: Page):
    """Test checking and unchecking checkboxes."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")

    # Check first checkbox
    checkboxes.first.check()
    assert checkboxes.first.is_checked()

    # Uncheck second checkbox
    checkboxes.nth(1).uncheck()
    assert not checkboxes.nth(1).is_checked()


# ============================================
# PART 6: DROPDOWN TESTS
# ============================================

@pytest.mark.regression
@pytest.mark.parametrize("option_value,option_text", [
    ("1", "Option 1"),
    ("2", "Option 2"),
])
def test_dropdown_selection(page: Page, option_value, option_text):
    """Test selecting dropdown options."""
    page.goto(f"{BASE_URL}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(option_value)
    assert dropdown.input_value() == option_value


# ============================================
# PART 7: DYNAMIC CONTENT TESTS
# ============================================

@pytest.mark.regression
def test_dynamic_loading(page: Page):
    """Test dynamically loaded content."""
    page.goto(f"{BASE_URL}/dynamic_loading/1")
    page.locator("#start button").click()
    expect(page.locator("#finish h4")).to_have_text("Hello World!", timeout=10000)


# ============================================
# PART 8: ADDITIONAL TESTS (implement at least 2 more)
# ============================================

# TODO: Add tests for at least 2 more pages:
# Suggestions:
# - /add_remove_elements/ - Add/remove button tests
# - /drag_and_drop - Drag and drop tests
# - /hovers - Hover action tests
# - /javascript_alerts - Alert handling tests
# - /key_presses - Keyboard input tests
# - /upload - File upload tests
# - /frames - iframe tests
# - /windows - Multi-window tests


# ============================================
# GRADING CRITERIA:
#
# 1. [20%] Project structure (conftest.py, page objects, constants)
# 2. [20%] Page Object Model (at least 2 page objects)
# 3. [15%] Fixtures (proper scope, cleanup, composition)
# 4. [15%] Parametrized tests (at least 2 parametrized functions)
# 5. [10%] Markers (smoke, regression, run filtering)
# 6. [10%] Error handling (tracing/screenshots on failure)
# 7. [10%] Code quality (naming, AAA pattern, independence)
#
# BONUS:
# - CI/CD configuration (GitHub Actions workflow)
# - HTML or Allure reporting
# - Parallel execution with pytest-xdist
# - Custom fixtures for cross-cutting concerns
# ============================================
