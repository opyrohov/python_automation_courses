"""
Exercise 4: Write Your First Playwright Test

Complete the test functions below following the AAA pattern (Arrange, Act, Assert).
Each test is partially completed - fill in the missing parts.

Run with: pytest exercise_04_first_test.py
Run in headed mode: pytest exercise_04_first_test.py --headed
"""

import pytest
from playwright.sync_api import Page, expect


# Test 1: Complete this test - Navigate to a page and verify title
def test_playwright_homepage(page: Page):
    """
    Test that Playwright documentation homepage loads correctly.

    TODO:
    1. Navigate to https://playwright.dev
    2. Verify the title contains "Playwright"
    3. Verify the page URL is correct
    """
    # ARRANGE
    url = "https://playwright.dev"

    # ACT
    # TODO: Navigate to the URL
    # page.goto(???)

    # ASSERT
    # TODO: Check the title contains "Playwright"
    # expect(page).to_have_title(???)

    # TODO: Verify the URL
    # assert page.url == ???

    pass  # Remove this when you complete the test


# Test 2: Complete this test - Find and verify an element
def test_get_started_button_visible(page: Page):
    """
    Test that the "Get Started" button is visible on Playwright homepage.

    TODO:
    1. Navigate to https://playwright.dev
    2. Find the "Get started" link
    3. Verify it's visible
    4. Verify it has the correct text
    """
    # ARRANGE
    # TODO: Set up the URL and selector
    # url = ???
    # get_started_selector = ???

    # ACT
    # TODO: Navigate to the page
    # page.goto(???)

    # ASSERT
    # TODO: Check that "Get started" link is visible
    # expect(page.locator(???)).to_be_visible()

    pass  # Remove this when you complete the test


# Test 3: Complete this test - Interact with an element (click)
def test_click_get_started(page: Page):
    """
    Test clicking the "Get started" button navigates to docs.

    TODO:
    1. Navigate to https://playwright.dev
    2. Click "Get started"
    3. Verify URL changed to /docs/intro
    """
    # ARRANGE
    page.goto("https://playwright.dev")

    # ACT
    # TODO: Click the "Get started" link
    # page.click(???)

    # ASSERT
    # TODO: Verify URL contains "/docs/intro"
    # expect(page).to_have_url(???)

    pass  # Remove this when you complete the test


# Test 4: Write this test from scratch - Search functionality
def test_search_docs(page: Page):
    """
    Test the search functionality on Playwright docs.

    Requirements:
    1. Go to https://playwright.dev/docs/intro
    2. Click the search button (selector: button[class*="DocSearch"])
    3. Type "selectors" in the search box
    4. Verify search results appear

    Write this test using the AAA pattern!
    """
    # ARRANGE
    # TODO: Set up your test data and navigate to the page

    # ACT
    # TODO: Perform the search action

    # ASSERT
    # TODO: Verify search results appeared

    pass  # Remove this when you complete the test


# Test 5: Write this test from scratch - Form filling
def test_google_search(page: Page):
    """
    Test Google search functionality.

    Requirements:
    1. Navigate to https://www.google.com
    2. Fill in search box with "Playwright Python"
    3. Press Enter
    4. Verify search results page loads
    5. Verify search results container is visible

    Write the complete test!
    """
    # TODO: Write the entire test using AAA pattern

    pass  # Remove this when you complete the test


# Test 6: Challenge - Multiple assertions
@pytest.mark.skip(reason="Challenge test - remove this decorator when ready")
def test_playwright_python_docs(page: Page):
    """
    Challenge: Test Playwright Python docs page with multiple assertions.

    Requirements:
    1. Navigate to https://playwright.dev/python
    2. Verify the page title
    3. Verify navigation menu is visible
    4. Verify "Installation" link exists and is clickable
    5. Click "Installation"
    6. Verify URL changed
    7. Verify page content contains "pip install"

    Remove @pytest.mark.skip when ready to attempt!
    """
    # TODO: Complete this challenge

    pass


# Test 7: Challenge - Using markers
@pytest.mark.smoke
def test_quick_page_load(page: Page):
    """
    Smoke test: Quick check that the main page loads.
    This is marked as a smoke test - it should run fast!

    TODO: Complete this simple smoke test
    """
    # TODO: Just verify https://playwright.dev loads and title is correct

    pass


# Test 8: Challenge - Error handling
def test_404_page(page: Page):
    """
    Test that navigating to a non-existent page shows 404.

    Requirements:
    1. Navigate to https://playwright.dev/this-does-not-exist
    2. Verify response status is 404
    3. Verify page shows "Page Not Found" or similar

    Hint: Use page.goto() with wait_until parameter
    Hint: Check response status with response.status
    """
    # TODO: Complete this test

    pass


# Bonus Test: Write your own test!
def test_your_own_idea(page: Page):
    """
    Create your own test! Test any website you like.

    Ideas:
    - Test a Wikipedia page
    - Test Amazon product page
    - Test GitHub repository page
    - Test any public website

    Requirements:
    - Use AAA pattern
    - At least 3 assertions
    - Should test something meaningful
    """
    # TODO: Write your own creative test!

    pass


# ------------------------------------------------------------------------------
# HELPER FUNCTIONS (optional - use if helpful)
# ------------------------------------------------------------------------------

def navigate_and_verify(page: Page, url: str, expected_title: str):
    """
    Helper function: Navigate to URL and verify title.

    You can use this in your tests if you want!
    """
    page.goto(url)
    expect(page).to_have_title(expected_title)


def assert_element_visible(page: Page, selector: str):
    """
    Helper function: Assert element is visible.

    You can use this in your tests if you want!
    """
    expect(page.locator(selector)).to_be_visible()


# ------------------------------------------------------------------------------
# VERIFICATION CHECKLIST
# ------------------------------------------------------------------------------
"""
After completing the exercises, verify:

[ ] Test 1: Navigate and verify title ✓
[ ] Test 2: Find and verify element ✓
[ ] Test 3: Click element ✓
[ ] Test 4: Search functionality ✓
[ ] Test 5: Form filling ✓
[ ] Test 6: Multiple assertions (challenge) ✓
[ ] Test 7: Smoke test ✓
[ ] Test 8: Error handling ✓
[ ] Bonus: Your own test ✓

Run commands:
    pytest exercise_04_first_test.py              # Run all tests
    pytest exercise_04_first_test.py -v           # Verbose output
    pytest exercise_04_first_test.py --headed     # See browser
    pytest exercise_04_first_test.py -k "google"  # Run only google tests
    pytest exercise_04_first_test.py -m smoke     # Run only smoke tests
"""


# ------------------------------------------------------------------------------
# LEARNING NOTES
# ------------------------------------------------------------------------------
"""
Key Concepts Practiced:
1. AAA Pattern (Arrange, Act, Assert)
2. Page navigation with page.goto()
3. Element interactions (click, fill, press)
4. Assertions with expect() and assert
5. Locators and selectors
6. Test organization with pytest
7. Test markers for categorization
8. Error handling in tests

Common Playwright Methods:
- page.goto(url) - Navigate to URL
- page.click(selector) - Click element
- page.fill(selector, text) - Fill input field
- page.press(selector, key) - Press keyboard key
- page.is_visible(selector) - Check if element visible
- expect(page).to_have_title(text) - Assert title
- expect(page).to_have_url(pattern) - Assert URL
- expect(locator).to_be_visible() - Assert element visible

Tips:
- Always use AAA pattern for clarity
- Write descriptive test names
- One test = one thing tested
- Keep tests independent
- Use selectors that won't change often
- Add helpful comments

Good luck! 🚀
"""
