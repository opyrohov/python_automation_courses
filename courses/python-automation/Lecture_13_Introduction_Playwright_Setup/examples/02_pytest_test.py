"""
Example 2: Playwright with Pytest

This shows how to use Playwright with pytest-playwright.
The 'page' fixture is provided automatically!

Run: pytest 02_pytest_test.py
Run in headed mode: pytest 02_pytest_test.py --headed
"""

import pytest
from playwright.sync_api import Page, expect


def test_playwright_homepage(page: Page):
    """
    Test that Playwright homepage loads correctly.

    The 'page' fixture is provided by pytest-playwright.
    No need to manually launch browser or create page!
    """

    # ARRANGE
    url = "https://playwright.dev"

    # ACT
    page.goto(url)

    # ASSERT
    # expect() provides auto-waiting - it will retry until condition is met
    expect(page).to_have_title("Playwright")
    expect(page).to_have_url(url)

    # Additional assertions
    assert "Playwright" in page.title()
    assert page.url == url

    print(f"✅ Successfully loaded {url}")


def test_get_started_button_visible(page: Page):
    """Test that the 'Get started' button is visible on the homepage."""

    # ARRANGE
    page.goto("https://playwright.dev")

    # ACT
    get_started_link = page.locator("a:has-text('Get started')")

    # ASSERT
    expect(get_started_link).to_be_visible()

    print("✅ 'Get started' button is visible")


def test_navigation_to_docs(page: Page):
    """Test that clicking 'Get started' navigates to docs."""

    # ARRANGE
    page.goto("https://playwright.dev")

    # ACT
    page.click("a:has-text('Get started')")

    # ASSERT
    expect(page).to_have_url("**/docs/intro")

    print("✅ Successfully navigated to docs")


@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_cross_browser(page: Page, browser_name: str):
    """
    Test that works across all browsers.

    Run: pytest 02_pytest_test.py::test_cross_browser --browser chromium --browser firefox --browser webkit
    """

    # Navigate
    page.goto("https://playwright.dev")

    # Verify
    expect(page).to_have_title("Playwright")

    print(f"✅ Test passed in browser")


if __name__ == "__main__":
    # Run tests programmatically
    pytest.main([__file__, "-v", "--headed"])
