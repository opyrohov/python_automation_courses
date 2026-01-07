"""Example 4: Project Structure for Page Object Model

This file demonstrates the recommended project structure
for organizing page objects in a real project.

RECOMMENDED STRUCTURE:
======================

project/
├── pages/                    # All page objects
│   ├── __init__.py          # Export all pages
│   ├── base_page.py         # BasePage class
│   ├── login_page.py        # LoginPage
│   ├── secure_page.py       # SecurePage
│   └── components/          # Reusable components
│       ├── __init__.py
│       ├── header.py
│       └── footer.py
│
├── tests/                   # All tests
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures
│   ├── test_login.py
│   └── test_secure.py
│
├── utils/                   # Helper utilities
│   ├── __init__.py
│   └── helpers.py
│
├── data/                    # Test data
│   ├── users.json
│   └── config.json
│
├── conftest.py             # Root conftest
├── pytest.ini              # Pytest config
└── requirements.txt        # Dependencies

======================
EXAMPLE IMPLEMENTATION:
======================
"""

# ============================================
# FILE: pages/base_page.py
# ============================================

class BasePage:
    """Base class for all page objects."""

    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")
        return self


# ============================================
# FILE: pages/login_page.py
# ============================================

# from pages.base_page import BasePage  # In real project
# from pages.secure_page import SecurePage  # In real project

class LoginPage(BasePage):
    """Login page object."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        if "/secure" in self.page.url:
            return SecurePage(self.page)
        return self

    def has_error(self):
        return "error" in (self.flash.get_attribute("class") or "")


# ============================================
# FILE: pages/secure_page.py
# ============================================

# from pages.base_page import BasePage  # In real project
# from pages.login_page import LoginPage  # In real project

class SecurePage(BasePage):
    """Secure area page object."""

    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h2")
        self.logout_button = page.locator("a[href='/logout']")

    def get_heading(self):
        return self.heading.text_content()

    def is_logged_in(self):
        return self.logout_button.is_visible()

    def logout(self):
        self.logout_button.click()
        return LoginPage(self.page)


# ============================================
# FILE: pages/__init__.py
# ============================================

# Export all pages for easy importing
# from pages.base_page import BasePage
# from pages.login_page import LoginPage
# from pages.secure_page import SecurePage

# Usage in tests:
# from pages import LoginPage, SecurePage


# ============================================
# FILE: tests/conftest.py
# ============================================

"""
import pytest
from playwright.sync_api import sync_playwright
from pages import LoginPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)
"""


# ============================================
# FILE: tests/test_login.py
# ============================================

"""
from pages import LoginPage, SecurePage

def test_successful_login(login_page):
    login_page.navigate()
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    assert isinstance(secure_page, SecurePage)
    assert secure_page.is_logged_in()

def test_failed_login(login_page):
    login_page.navigate()
    result = login_page.login("wrong", "wrong")

    assert isinstance(result, LoginPage)
    assert result.has_error()
"""


# ============================================
# DEMO - SIMULATING PROJECT STRUCTURE
# ============================================

from playwright.sync_api import sync_playwright


def demo_project_structure():
    """Demonstrate how the project structure works."""
    print("=" * 60)
    print("PROJECT STRUCTURE DEMO")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # In a real project, you would import:
        # from pages import LoginPage

        print("\n--- Simulating Test File ---")
        print("# from pages import LoginPage, SecurePage")

        # Create page object
        login_page = LoginPage(page)
        print("\nlogin_page = LoginPage(page)")

        # Navigate
        login_page.navigate()
        print("login_page.navigate()")
        print(f"  -> Title: {login_page.get_title()}")

        # Login
        secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
        print("\nsecure_page = login_page.login('tomsmith', '...')")
        print(f"  -> Type: {secure_page.__class__.__name__}")
        print(f"  -> Logged in: {secure_page.is_logged_in()}")

        # Logout
        login_page = secure_page.logout()
        print("\nlogin_page = secure_page.logout()")
        print(f"  -> Type: {login_page.__class__.__name__}")

        browser.close()

    print("\n" + "=" * 60)
    print("""
PROJECT STRUCTURE BENEFITS:

1. ORGANIZATION
   - Pages in one place
   - Tests in another
   - Easy to find files

2. IMPORTS
   - Clean imports: from pages import LoginPage
   - No circular dependencies

3. REUSABILITY
   - Share pages across tests
   - Components for common elements

4. MAINTAINABILITY
   - Change page → affects one file
   - Tests stay clean

5. SCALABILITY
   - Add new pages easily
   - Add new tests easily
""")


if __name__ == "__main__":
    demo_project_structure()
