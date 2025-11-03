"""
Exercise 3: Write Playwright Tests with Pytest

Complete the test functions below using pytest-playwright.

Run: pytest exercise_03_pytest_tests.py
Run in headed mode: pytest exercise_03_pytest_tests.py --headed
"""

import pytest
from playwright.sync_api import Page, expect


# ============================================================================
# Basic Tests
# ============================================================================

def test_example_com(page: Page):
    """
    Exercise 1: Test example.com

    TODO:
    1. Navigate to https://example.com
    2. Verify the title is "Example Domain"
    3. Verify the URL is correct
    """

    # TODO: Navigate to the URL
    # page.goto(???)

    # TODO: Verify title
    # expect(page).to_have_title(???)

    # TODO: Verify URL
    # expect(page).to_have_url(???)

    pass  # Remove this when you complete the test


def test_playwright_homepage(page: Page):
    """
    Exercise 2: Test Playwright homepage

    TODO:
    1. Navigate to https://playwright.dev
    2. Verify title contains "Playwright"
    3. Verify URL is correct
    """

    # TODO: Your test code here

    pass


def test_get_started_button_exists(page: Page):
    """
    Exercise 3: Verify "Get started" button exists

    TODO:
    1. Navigate to https://playwright.dev
    2. Find the "Get started" link
    3. Verify it's visible

    Hint: Use page.locator("a:has-text('Get started')")
    """

    # TODO: Your test code here

    pass


def test_navigation_to_docs(page: Page):
    """
    Exercise 4: Test navigation to docs

    TODO:
    1. Navigate to https://playwright.dev
    2. Click "Get started" link
    3. Verify URL contains "/docs/intro"

    Hint: Use expect(page).to_have_url("**/docs/intro")
    """

    # TODO: Your test code here

    pass


# ============================================================================
# Screenshot Tests
# ============================================================================

def test_take_screenshot(page: Page):
    """
    Exercise 5: Take a screenshot in a test

    TODO:
    1. Navigate to https://playwright.dev
    2. Take a screenshot and save as "test_screenshot.png"
    3. Verify page title

    Note: pytest-playwright automatically takes screenshots on failure!
    """

    # TODO: Your test code here

    pass


def test_full_page_screenshot(page: Page):
    """
    Exercise 6: Take a full page screenshot

    TODO:
    1. Navigate to https://example.com
    2. Take a full page screenshot
    3. Save as "full_page.png"
    """

    # TODO: Your test code here

    pass


# ============================================================================
# Multiple Browser Tests
# ============================================================================

@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://playwright.dev",
])
def test_multiple_urls(page: Page, url: str):
    """
    Exercise 7: Test multiple URLs

    This test will run twice - once for each URL!

    TODO:
    1. Navigate to the URL (it's passed as parameter)
    2. Verify page loads successfully
    3. Print the title

    Run: pytest exercise_03_pytest_tests.py::test_multiple_urls -v
    """

    # TODO: Your test code here

    pass


# ============================================================================
# Test Markers
# ============================================================================

@pytest.mark.smoke
def test_smoke_quick_check(page: Page):
    """
    Exercise 8: Smoke test

    TODO:
    1. Navigate to https://example.com
    2. Quick check that page loads
    3. Verify title

    Run only smoke tests: pytest -m smoke
    """

    # TODO: Your test code here

    pass


@pytest.mark.slow
def test_slow_operation(page: Page):
    """
    Exercise 9: Slow test with marker

    TODO:
    1. Navigate to https://playwright.dev
    2. Wait for 2 seconds (page.wait_for_timeout(2000))
    3. Verify page loaded

    Run: pytest -m slow
    Skip slow tests: pytest -m "not slow"
    """

    # TODO: Your test code here

    pass


# ============================================================================
# Page Information Tests
# ============================================================================

def test_get_page_info(page: Page):
    """
    Exercise 10: Get and verify page information

    TODO:
    1. Navigate to https://playwright.dev
    2. Get and print:
       - Page title
       - Current URL
       - Viewport size
    3. Verify title contains "Playwright"
    """

    # TODO: Your test code here
    # Hints:
    # title = page.title()
    # url = page.url
    # viewport = page.viewport_size

    pass


# ============================================================================
# Error Handling Tests
# ============================================================================

def test_404_page(page: Page):
    """
    Exercise 11: Test 404 error page

    TODO:
    1. Navigate to https://playwright.dev/this-page-does-not-exist
    2. Check that response status is 404
    3. Verify page contains "Page Not Found" or similar text

    Hint: response = page.goto(url)
          response.status == 404
    """

    # TODO: Your test code here

    pass


# ============================================================================
# Advanced: Your Own Test
# ============================================================================

def test_your_own_website(page: Page):
    """
    Exercise 12: Test your own favorite website!

    TODO:
    Create a test for any website you choose:
    1. Navigate to the website
    2. Verify something on the page (title, element, URL)
    3. Maybe click something
    4. Take a screenshot

    Be creative! This is your test!
    """

    # TODO: Your creative test here!

    pass


# ============================================================================
# Pytest Configuration
# ============================================================================

# Add this to pytest.ini to configure markers:
"""
[pytest]
markers =
    smoke: Quick smoke tests
    slow: Slow running tests
    regression: Full regression tests
"""


# ============================================================================
# Helpful Commands
# ============================================================================
"""
Run all tests:
    pytest exercise_03_pytest_tests.py

Run in headed mode (see browser):
    pytest exercise_03_pytest_tests.py --headed

Run specific test:
    pytest exercise_03_pytest_tests.py::test_example_com

Run with verbose output:
    pytest exercise_03_pytest_tests.py -v

Run only smoke tests:
    pytest exercise_03_pytest_tests.py -m smoke

Run with specific browser:
    pytest exercise_03_pytest_tests.py --browser firefox
    pytest exercise_03_pytest_tests.py --browser webkit

Run with slow motion:
    pytest exercise_03_pytest_tests.py --headed --slowmo 1000

Stop on first failure:
    pytest exercise_03_pytest_tests.py -x

Show print statements:
    pytest exercise_03_pytest_tests.py -s
"""
