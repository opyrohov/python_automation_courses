"""
Lecture 6 - Example 6: Playwright Imports and Setup
==================================================
Learn how to import and use Playwright for browser automation.

NOTE: This example shows import patterns and setup concepts.
Playwright needs to be installed:
pip install playwright
playwright install
"""

print("=" * 60)
print("PLAYWRIGHT IMPORTS AND SETUP")
print("=" * 60)
print()

# 1. CHECKING IF PLAYWRIGHT IS INSTALLED
# ======================================

print("1. Checking Playwright installation:")
print()

try:
    import playwright
    print(f"✅ Playwright is installed")
    print(f"   Version: {playwright.__version__}")
    print(f"   Location: {playwright.__file__}")
except ImportError:
    print("❌ Playwright is not installed")
    print("   Install with:")
    print("   pip install playwright")
    print("   playwright install")

print()
print("-" * 60)


# 2. PLAYWRIGHT IMPORT PATTERNS
# =============================

print("2. Playwright import patterns:")
print()

import_examples = """
# SYNC API (We'll use this in the course!)
# ========================================

# Basic import
from playwright.sync_api import sync_playwright

# Import with expect for assertions
from playwright.sync_api import sync_playwright, expect

# Import specific classes
from playwright.sync_api import Page, Browser, BrowserContext

# All-in-one import for tests
from playwright.sync_api import (
    sync_playwright,
    expect,
    Page,
    Browser,
    BrowserContext,
    Playwright
)


# ASYNC API (Advanced - for async/await patterns)
# ==============================================

# Async version
from playwright.async_api import async_playwright

# Async with expect
from playwright.async_api import async_playwright, expect


# PYTEST PLUGIN
# =============

# When using pytest-playwright
import pytest

# Fixtures are automatically available:
# - browser
# - context
# - page
"""

print(import_examples)
print()
print("-" * 60)


# 3. BASIC PLAYWRIGHT STRUCTURE
# =============================

print("3. Basic Playwright script structure:")
print()

basic_structure = """
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Create a page
        page = browser.new_page()

        # Navigate
        page.goto("https://example.com")

        # Interact with page
        page.click("#button")
        page.fill("#input", "text")

        # Close browser
        browser.close()

if __name__ == "__main__":
    run()
"""

print(basic_structure)
print()
print("-" * 60)


# 4. PLAYWRIGHT WITH PYTEST
# =========================

print("4. Using Playwright with pytest:")
print()

pytest_example = """
# Install pytest-playwright:
# pip install pytest-playwright

# test_example.py
from playwright.sync_api import Page, expect

def test_homepage(page: Page):
    # page fixture is provided by pytest-playwright
    page.goto("https://example.com")

    # Use expect for assertions
    expect(page).to_have_title("Example Domain")

    # Interact with elements
    page.click("text=More information")

def test_form_fill(page: Page):
    page.goto("https://example.com/form")
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")
    page.click("#submit")

    expect(page.locator("#success")).to_be_visible()


# Run with: pytest test_example.py
"""

print(pytest_example)
print()
print("-" * 60)


# 5. ORGANIZING PLAYWRIGHT TESTS
# ==============================

print("5. Organizing Playwright test projects:")
print()

project_structure = """
playwright_project/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_search.py
│   └── test_checkout.py
│
├── pages/                      # Page Object Models
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── checkout_page.py
│
├── utils/                      # Helper functions
│   ├── __init__.py
│   ├── helpers.py
│   ├── data_generators.py
│   └── api_helpers.py
│
├── config/                     # Configuration
│   ├── __init__.py
│   ├── settings.py
│   └── test_data.py
│
├── fixtures/                   # Pytest fixtures
│   ├── __init__.py
│   └── common_fixtures.py
│
├── reports/                    # Test reports (generated)
│
├── screenshots/                # Screenshots (generated)
│
├── requirements.txt            # Dependencies
├── pytest.ini                  # Pytest configuration
└── README.md                   # Project documentation
"""

print(project_structure)
print()
print("-" * 60)


# 6. PAGE OBJECT PATTERN IMPORTS
# ==============================

print("6. Page Object Pattern:")
print()

page_object_example = """
# pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#login-btn"

    def navigate(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def verify_error_message(self, message):
        expect(self.page.locator(".error")).to_contain_text(message)


# tests/test_login.py
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("testuser", "password123")
    # Verify redirect to dashboard...

def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid", "wrong")
    login_page.verify_error_message("Invalid credentials")
"""

print(page_object_example)
print()
print("-" * 60)


# 7. HELPER FUNCTIONS MODULE
# ==========================

print("7. Creating helper functions:")
print()

helpers_example = """
# utils/helpers.py
from playwright.sync_api import Page, expect
from datetime import datetime
from pathlib import Path

def take_screenshot(page: Page, name: str):
    '''Take a screenshot with timestamp'''
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)

    filename = f"{name}_{timestamp}.png"
    filepath = screenshot_dir / filename

    page.screenshot(path=str(filepath))
    return str(filepath)

def wait_and_click(page: Page, selector: str, timeout: int = 10000):
    '''Wait for element and click it'''
    page.wait_for_selector(selector, timeout=timeout)
    page.click(selector)

def fill_form(page: Page, form_data: dict):
    '''Fill multiple form fields'''
    for selector, value in form_data.items():
        page.fill(selector, value)


# tests/test_using_helpers.py
from playwright.sync_api import Page
from utils.helpers import take_screenshot, wait_and_click, fill_form

def test_with_helpers(page: Page):
    page.goto("https://example.com/form")

    # Use helper functions
    form_data = {
        "#name": "John Doe",
        "#email": "john@example.com",
        "#phone": "555-1234"
    }
    fill_form(page, form_data)

    wait_and_click(page, "#submit-button")

    take_screenshot(page, "form_submitted")
"""

print(helpers_example)
print()
print("-" * 60)


# 8. CONFIGURATION MODULE
# =======================

print("8. Configuration management:")
print()

config_example = """
# config/settings.py
from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Test environment
BASE_URL = "https://example.com"
TEST_ENV = "staging"

# Browser configuration
BROWSER_TYPE = "chromium"  # chromium, firefox, webkit
HEADLESS = False
SLOW_MO = 100  # Slow down by 100ms

# Timeouts
DEFAULT_TIMEOUT = 30000  # 30 seconds
NAVIGATION_TIMEOUT = 60000  # 60 seconds

# Test data
TEST_USERS = {
    "valid_user": {
        "username": "testuser@example.com",
        "password": "Test123!"
    },
    "admin_user": {
        "username": "admin@example.com",
        "password": "Admin123!"
    }
}


# tests/test_using_config.py
from playwright.sync_api import Page
from config.settings import BASE_URL, TEST_USERS, DEFAULT_TIMEOUT

def test_login_with_config(page: Page):
    page.set_default_timeout(DEFAULT_TIMEOUT)
    page.goto(f"{BASE_URL}/login")

    user = TEST_USERS["valid_user"]
    page.fill("#username", user["username"])
    page.fill("#password", user["password"])
    page.click("#login-button")
"""

print(config_example)
print()
print("-" * 60)


# 9. PYTEST CONFIGURATION
# =======================

print("9. pytest configuration for Playwright:")
print()

pytest_ini = """
# pytest.ini
[pytest]
# Playwright specific options
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Markers
markers =
    slow: marks tests as slow
    smoke: smoke tests
    regression: regression tests

# Playwright options (with pytest-playwright)
# These can be overridden via command line
base_url = https://example.com

# Report options
addopts =
    --verbose
    --html=reports/report.html
    --self-contained-html

# Run tests with:
# pytest                              # All tests
# pytest -m smoke                     # Only smoke tests
# pytest tests/test_login.py         # Specific file
# pytest -k "login"                   # Tests with "login" in name
# pytest --headed                     # Show browser
# pytest --browser firefox            # Use Firefox
"""

print(pytest_ini)
print()
print("-" * 60)


# 10. REQUIREMENTS.TXT FOR PLAYWRIGHT PROJECT
# ===========================================

print("10. Complete requirements.txt:")
print()

requirements = """
# requirements.txt

# Core testing
pytest==7.4.3
pytest-playwright==0.4.3

# Playwright
playwright==1.40.0

# Reporting
pytest-html==4.1.1
allure-pytest==2.13.2

# Test data generation
faker==20.1.0

# Configuration
python-dotenv==1.0.0
pyyaml==6.0.1

# API testing (optional)
requests==2.31.0

# Code quality (development)
black==23.12.0
flake8==6.1.0
mypy==1.7.1

# Install with:
# pip install -r requirements.txt
# playwright install
"""

print(requirements)

print()
print("=" * 60)
print("Example complete! You're ready to start Playwright automation!")
print("=" * 60)
print()
print("Next steps:")
print("1. Install Playwright: pip install playwright")
print("2. Install browsers: playwright install")
print("3. Move on to Lecture 7 for hands-on Playwright!")
