"""Example 2: conftest.py - Browser and Context Configuration

Demonstrates how to configure browser launch options and context settings
using pytest-playwright's special fixtures in conftest.py.

IMPORTANT: In a real project, fixtures go in conftest.py (not in test files).
This file shows them together for learning purposes.
"""
import pytest
from playwright.sync_api import Page, BrowserContext, Browser


# ============================================
# BROWSER LAUNCH OPTIONS
# ============================================
# These fixtures are recognized by pytest-playwright
# and override default browser behavior.

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure how the browser is launched.

    scope="session" means this runs ONCE for all tests.
    """
    return {
        "headless": False,     # Show browser window
        "slow_mo": 500,        # 500ms delay between actions
        # "channel": "chrome",  # Use installed Chrome
        # "args": ["--start-maximized"],  # Browser arguments
    }


# ============================================
# BROWSER CONTEXT OPTIONS
# ============================================

@pytest.fixture(scope="session")
def browser_context_args():
    """Configure browser context (like an incognito window).

    Each test gets its own context with these settings.
    """
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        # "locale": "uk-UA",
        # "timezone_id": "Europe/Kyiv",
        # "permissions": ["geolocation"],
        # "geolocation": {"latitude": 50.4501, "longitude": 30.5234},
        # "color_scheme": "dark",
    }


# ============================================
# CUSTOM PAGE FIXTURE
# ============================================

@pytest.fixture
def configured_page(page: Page):
    """Custom page fixture with additional setup."""
    # Set default navigation timeout
    page.set_default_navigation_timeout(15000)  # 15 seconds

    # Set default timeout for actions (click, fill, etc.)
    page.set_default_timeout(10000)  # 10 seconds

    return page


# ============================================
# FIXTURE SCOPES EXPLAINED
# ============================================

@pytest.fixture(scope="function")
def fresh_page(page: Page):
    """scope='function' (default) - runs for EACH test.

    Each test gets its own page.
    """
    return page


@pytest.fixture(scope="session")
def shared_browser(browser: Browser):
    """scope='session' - runs ONCE for all tests.

    All tests share the same browser instance.
    """
    return browser


# ============================================
# TESTS
# ============================================

def test_browser_is_visible(page: Page):
    """Test with configured browser (headless=False, slow_mo=500)."""
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"
    # You should see the browser window and slow actions


def test_viewport_is_configured(page: Page):
    """Test that viewport is set to 1280x720."""
    page.goto("https://the-internet.herokuapp.com")
    viewport = page.viewport_size
    assert viewport["width"] == 1280
    assert viewport["height"] == 720


def test_with_configured_page(configured_page):
    """Test using our custom page fixture with timeouts."""
    configured_page.goto("https://the-internet.herokuapp.com/login")
    # Actions will timeout after 10 seconds
    assert configured_page.locator("h2").text_content() == "Login Page"


def test_custom_viewport(browser: Browser):
    """Test with a custom viewport (mobile simulation)."""
    context = browser.new_context(
        viewport={"width": 375, "height": 812},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"
    context.close()


# ============================================
# DEVICE EMULATION
# ============================================

def test_iphone_emulation(playwright):
    """Test with iPhone device emulation."""
    iphone = playwright.devices["iPhone 13"]
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(**iphone)
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"

    # Check viewport matches iPhone
    viewport = page.viewport_size
    print(f"\n  iPhone viewport: {viewport['width']}x{viewport['height']}")

    context.close()
    browser.close()


# ============================================
# KEY POINTS:
#
# 1. browser_type_launch_args - browser launch config
# 2. browser_context_args - context config (viewport, etc.)
# 3. scope="session" - runs once for all tests
# 4. scope="function" - runs for each test (default)
# 5. Custom fixtures can wrap 'page' with extra setup
# 6. playwright.devices for device emulation
# 7. In real projects, put fixtures in conftest.py
#
# Run: pytest 02_conftest_browser_options.py -v -s
# ============================================
