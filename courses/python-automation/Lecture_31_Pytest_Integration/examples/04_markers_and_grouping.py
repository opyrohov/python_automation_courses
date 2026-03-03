"""Example 4: Test Markers and Grouping

Demonstrates how to use pytest markers to categorize tests
and run specific groups from the command line.

Run with:
    pytest 04_markers_and_grouping.py -v --headed
    pytest 04_markers_and_grouping.py -v -m smoke --headed
    pytest 04_markers_and_grouping.py -v -m regression --headed
    pytest 04_markers_and_grouping.py -v -m "smoke and not slow" --headed
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# SMOKE TESTS - Quick, critical path
# ============================================

@pytest.mark.smoke
def test_homepage_loads(page: Page):
    """Smoke test: verify homepage loads."""
    page.goto(BASE_URL)
    assert page.title() == "The Internet"


@pytest.mark.smoke
def test_login_page_accessible(page: Page):
    """Smoke test: verify login page is accessible."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("h2").text_content() == "Login Page"


@pytest.mark.smoke
def test_successful_login(page: Page):
    """Smoke test: verify login works."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


# ============================================
# REGRESSION TESTS - Detailed checks
# ============================================

@pytest.mark.regression
def test_login_form_elements(page: Page):
    """Regression: verify all form elements present."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("button[type='submit']").is_visible()
    assert page.locator("h4").is_visible()  # Subheading


@pytest.mark.regression
def test_invalid_username_error(page: Page):
    """Regression: verify error for invalid username."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("invalid_user")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    assert "Your username is invalid!" in flash.text_content()


@pytest.mark.regression
def test_invalid_password_error(page: Page):
    """Regression: verify error for invalid password."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("wrong_password")
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    assert "Your password is invalid!" in flash.text_content()


# ============================================
# BUILT-IN MARKERS
# ============================================

@pytest.mark.skip(reason="Feature not implemented yet")
def test_password_reset(page: Page):
    """This test is skipped - feature doesn't exist."""
    page.goto(f"{BASE_URL}/forgot_password")
    # Would test password reset flow
    pass


@pytest.mark.xfail(reason="Known bug - empty login shows wrong error")
def test_empty_login_message(page: Page):
    """Expected to fail - known bug in the application."""
    page.goto(f"{BASE_URL}/login")
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    # This assertion might fail due to known bug
    assert "Please enter your credentials" in flash.text_content()


# ============================================
# MULTIPLE MARKERS
# ============================================

@pytest.mark.smoke
@pytest.mark.regression
def test_logout(page: Page):
    """Both smoke and regression: verify logout works."""
    # Login first
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # Logout
    page.locator("a[href='/logout']").click()
    assert "/login" in page.url


@pytest.mark.regression
@pytest.mark.slow
def test_all_links_on_homepage(page: Page):
    """Regression + slow: check all links on homepage."""
    page.goto(BASE_URL)
    links = page.locator("#content ul li a")
    count = links.count()

    assert count > 0
    print(f"\n  Found {count} links on homepage")

    # Check first 5 links load successfully
    for i in range(min(5, count)):
        link_text = links.nth(i).text_content()
        print(f"  Link {i+1}: {link_text}")


# ============================================
# KEY POINTS:
#
# 1. @pytest.mark.smoke - quick critical tests
# 2. @pytest.mark.regression - detailed tests
# 3. @pytest.mark.skip - skip a test
# 4. @pytest.mark.xfail - expected failure
# 5. Multiple markers on one test
# 6. pytest -m "smoke" to filter
# 7. Register markers in pytest.ini
#
# Run: pytest 04_markers_and_grouping.py -v -m smoke --headed
# ============================================
