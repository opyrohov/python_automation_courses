"""Example 3: Base URL and Timeout Configuration

Demonstrates how to configure a base URL to avoid repeating full URLs,
and how to set up various timeout levels.

Run with: pytest 03_base_url_and_timeouts.py -v --headed --base-url https://the-internet.herokuapp.com
"""
import pytest
from playwright.sync_api import Page


# ============================================
# BASE URL USAGE
# ============================================
# Set base URL via:
#   1. CLI: pytest --base-url https://the-internet.herokuapp.com
#   2. pytest.ini: base_url = https://the-internet.herokuapp.com
#   3. conftest.py fixture (see below)

@pytest.fixture(scope="session")
def base_url():
    """Override base_url fixture to set default URL."""
    return "https://the-internet.herokuapp.com"


# ============================================
# TESTS WITH BASE URL
# ============================================

def test_homepage(page: Page, base_url):
    """Navigate using base_url."""
    page.goto(base_url)
    assert page.title() == "The Internet"


def test_login_page(page: Page, base_url):
    """Navigate to a sub-page using base_url."""
    page.goto(f"{base_url}/login")
    assert page.locator("h2").text_content() == "Login Page"


def test_checkboxes(page: Page, base_url):
    """Another page using base_url."""
    page.goto(f"{base_url}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


# ============================================
# TIMEOUT CONFIGURATION
# ============================================

@pytest.fixture
def page_with_timeouts(page: Page):
    """Page with custom timeout settings."""
    # Default timeout for ALL actions (click, fill, locator operations)
    page.set_default_timeout(10000)  # 10 seconds

    # Default timeout specifically for navigation (goto, reload, etc.)
    page.set_default_navigation_timeout(15000)  # 15 seconds

    return page


def test_with_default_timeouts(page_with_timeouts, base_url):
    """Test using page with configured timeouts."""
    page_with_timeouts.goto(f"{base_url}/login")
    # All locator operations now have 10s timeout
    assert page_with_timeouts.locator("h2").text_content() == "Login Page"


# ============================================
# PER-ACTION TIMEOUTS
# ============================================

def test_per_action_timeout(page: Page, base_url):
    """Override timeout for specific actions."""
    # Navigation with custom timeout
    page.goto(f"{base_url}/login", timeout=20000)  # 20 seconds

    # Click with custom timeout
    page.locator("button[type='submit']").click(timeout=5000)  # 5 seconds

    # Wait for element with custom timeout
    page.locator("#flash").wait_for(timeout=5000)  # 5 seconds


def test_wait_for_element(page: Page, base_url):
    """Using explicit waits with timeouts."""
    page.goto(f"{base_url}/dynamic_loading/1")

    # Click start button
    page.locator("#start button").click()

    # Wait for result to appear (with timeout)
    result = page.locator("#finish h4")
    result.wait_for(state="visible", timeout=10000)

    assert result.text_content() == "Hello World!"


# ============================================
# TIMEOUT HIERARCHY
# ============================================
#
# Timeouts are checked in this order (most specific wins):
#
# 1. Per-action timeout:
#    page.locator("#btn").click(timeout=5000)
#
# 2. Page default timeout:
#    page.set_default_timeout(10000)
#
# 3. Browser context timeout (from browser_context_args)
#
# 4. Global default (30 seconds)
#


# ============================================
# NAVIGATION WAIT STATES
# ============================================

def test_wait_until_options(page: Page, base_url):
    """Different wait strategies for page.goto()."""
    # wait_until options:
    # - "load"        - wait for load event (default)
    # - "domcontentloaded" - wait for DOMContentLoaded
    # - "networkidle" - wait for no network activity (2+ seconds)
    # - "commit"      - wait for response received

    # Fast - don't wait for all resources
    page.goto(f"{base_url}/login", wait_until="domcontentloaded")
    assert page.locator("h2").is_visible()

    # Thorough - wait for network to be idle
    page.goto(f"{base_url}/login", wait_until="networkidle")
    assert page.locator("h2").is_visible()


# ============================================
# KEY POINTS:
#
# 1. base_url avoids repeating full URLs
# 2. Set via CLI, pytest.ini, or conftest.py
# 3. set_default_timeout() - all actions
# 4. set_default_navigation_timeout() - navigation only
# 5. Per-action timeout overrides defaults
# 6. wait_until controls page load strategy
# 7. Most specific timeout wins
#
# Run: pytest 03_base_url_and_timeouts.py -v --headed
# ============================================
