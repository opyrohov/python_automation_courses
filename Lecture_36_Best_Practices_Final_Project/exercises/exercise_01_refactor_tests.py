"""Exercise 1: Refactor Messy Tests

The tests below work but violate best practices.
Your task: Refactor them to follow the patterns from this lecture.

Issues to fix:
1. Tests are not independent (shared state)
2. No Arrange-Act-Assert pattern
3. Poor naming
4. Duplicate code
5. Brittle selectors
6. No fixtures used
7. Magic strings everywhere

Target site: https://the-internet.herokuapp.com

Run with:
    pytest exercise_01_refactor_tests.py -v
"""
from playwright.sync_api import Page


# ============================================
# MESSY TESTS - REFACTOR THESE!
# ============================================

def test_1(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(1) > div > input").fill("tomsmith")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(2) > div > input").fill("SuperSecretPassword!")
    page.locator("div:nth-child(1) > div > div > form > button").click()
    assert "/secure" in page.url
    page.locator('a[href="/logout"]').click()
    assert "/login" in page.url


def test_2(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(1) > div > input").fill("wrong")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(2) > div > input").fill("wrong")
    page.locator("div:nth-child(1) > div > div > form > button").click()
    assert "Your username is invalid!" in page.locator("#flash").text_content()


def test_3(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(1) > div > input").fill("tomsmith")
    page.locator("div:nth-child(1) > div > div > form > div:nth-child(2) > div > input").fill("wrong")
    page.locator("div:nth-child(1) > div > div > form > button").click()
    assert "Your password is invalid!" in page.locator("#flash").text_content()


def test_4(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input").first.check()
    assert page.locator("input").first.is_checked()


def test_5(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.locator("input").nth(1).uncheck()
    assert not page.locator("input").nth(1).is_checked()


def test_6(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("1")
    assert page.locator("#dropdown").input_value() == "1"
    page.locator("#dropdown").select_option("2")
    assert page.locator("#dropdown").input_value() == "2"


# ============================================
# YOUR REFACTORED VERSION GOES BELOW
# ============================================
# Requirements:
#
# 1. Create constants for URL and credentials
# 2. Use descriptive test names
# 3. Follow Arrange-Act-Assert pattern
# 4. Use stable selectors (#id, role-based)
# 5. Create a conftest.py with:
#    - login_page fixture
#    - checkboxes_page fixture
# 6. Use @pytest.mark.parametrize where appropriate
# 7. Add custom markers (smoke, regression)
# 8. Each test should test ONE thing
#
# Hint: test_1 should be split into 2 tests:
#   - test_successful_login_redirects_to_secure_area
#   - test_logout_redirects_to_login_page
