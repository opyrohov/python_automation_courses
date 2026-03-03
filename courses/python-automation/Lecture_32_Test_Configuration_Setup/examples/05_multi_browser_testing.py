"""Example 5: Multi-Browser Testing

Demonstrates how to run tests across multiple browsers
(Chromium, Firefox, WebKit) for cross-browser compatibility.

Run with:
    pytest 05_multi_browser_testing.py -v --headed
    pytest 05_multi_browser_testing.py -v --browser chromium --browser firefox
    pytest 05_multi_browser_testing.py -v --browser webkit
"""
import pytest
from playwright.sync_api import Page, Browser


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# BASIC CROSS-BROWSER TESTS
# ============================================
# These tests run on whichever browser is specified:
#   --browser chromium (default)
#   --browser firefox
#   --browser webkit

def test_homepage_loads(page: Page):
    """Test homepage on current browser."""
    page.goto(BASE_URL)
    assert page.title() == "The Internet"


def test_login_works(page: Page):
    """Test login on current browser."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


def test_checkboxes_work(page: Page):
    """Test checkboxes on current browser."""
    page.goto(f"{BASE_URL}/checkboxes")
    first_checkbox = page.locator("input[type='checkbox']").first
    first_checkbox.check()
    assert first_checkbox.is_checked()


def test_dropdown_works(page: Page):
    """Test dropdown on current browser."""
    page.goto(f"{BASE_URL}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(value="1")
    selected = dropdown.locator("option:checked")
    assert "Option 1" in selected.text_content()


# ============================================
# MANUAL MULTI-BROWSER TEST
# ============================================

def test_on_all_browsers_manually(playwright):
    """Manually test on all three browsers in one test.

    Use this when you need to test all browsers in a single test run
    without specifying --browser multiple times.
    """
    browsers = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }

    for name, browser_type in browsers.items():
        browser = browser_type.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)
        title = page.title()
        assert title == "The Internet", f"Failed on {name}: {title}"
        print(f"\n  {name}: {title} - OK")

        browser.close()


# ============================================
# BROWSER-SPECIFIC CONFIGURATION
# ============================================

def test_with_chrome_channel(playwright):
    """Use installed Google Chrome instead of bundled Chromium."""
    try:
        browser = playwright.chromium.launch(
            channel="chrome",  # Use installed Chrome
            headless=True,
        )
        page = browser.new_page()
        page.goto(BASE_URL)
        assert page.title() == "The Internet"
        print(f"\n  Chrome version: {browser.version}")
        browser.close()
    except Exception as e:
        pytest.skip(f"Chrome not available: {e}")


# ============================================
# PARAMETRIZE WITH BROWSER NAMES
# ============================================

@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_parametrized_browsers(playwright, browser_name):
    """Parametrized test across browsers."""
    browser_type = getattr(playwright, browser_name)

    try:
        browser = browser_type.launch(headless=True)
    except Exception as e:
        pytest.skip(f"{browser_name} not available: {e}")

    page = browser.new_page()
    page.goto(f"{BASE_URL}/login")

    # Fill and submit
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    assert "/secure" in page.url
    print(f"\n  {browser_name}: Login successful")

    browser.close()


# ============================================
# BROWSER-SPECIFIC VIEWPORT
# ============================================

@pytest.mark.parametrize("width,height,label", [
    (1920, 1080, "Desktop"),
    (1366, 768, "Laptop"),
    (768, 1024, "Tablet"),
    (375, 812, "Mobile"),
])
def test_responsive(page: Page, width, height, label):
    """Test responsive layout at different sizes."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(BASE_URL)

    assert page.title() == "The Internet"
    heading = page.locator("h1")
    assert heading.is_visible()
    print(f"\n  {label} ({width}x{height}): heading visible")


# ============================================
# COMPLETE PROJECT CONFIGURATION
# ============================================
#
# For a real project, configure in conftest.py:
#
# conftest.py:
# -------------------------------------------------
# import pytest
#
# @pytest.fixture(scope="session")
# def browser_type_launch_args():
#     return {
#         "headless": True,
#         "slow_mo": 0,
#     }
#
# @pytest.fixture(scope="session")
# def browser_context_args():
#     return {
#         "viewport": {"width": 1280, "height": 720},
#         "ignore_https_errors": True,
#     }
# -------------------------------------------------
#
# pytest.ini:
# -------------------------------------------------
# [pytest]
# addopts = -v --tb=short
# base_url = https://the-internet.herokuapp.com
# markers =
#     smoke: Quick smoke tests
#     regression: Full regression suite
# -------------------------------------------------
#
# Run commands:
#   pytest                                    # All tests, chromium
#   pytest --browser firefox                  # Firefox only
#   pytest --browser chromium --browser firefox  # Both browsers
#   pytest -m smoke --headed                  # Smoke tests, visible
#   pytest --screenshot only-on-failure       # Screenshots on failure
#   pytest --tracing retain-on-failure        # Traces on failure
#


# ============================================
# KEY POINTS:
#
# 1. --browser chromium/firefox/webkit
# 2. Multiple --browser flags for cross-browser
# 3. channel="chrome" for installed Chrome
# 4. playwright.devices for device emulation
# 5. Parametrize for browser/viewport combos
# 6. conftest.py for project-wide config
# 7. pytest.ini for CLI defaults
#
# Run: pytest 05_multi_browser_testing.py -v --headed
# Cross: pytest 05_multi_browser_testing.py -v --browser chromium --browser firefox
# ============================================
