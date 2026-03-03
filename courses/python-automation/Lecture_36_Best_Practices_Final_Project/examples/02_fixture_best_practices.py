"""Example 2: Fixture Best Practices

Demonstrates advanced fixture patterns, scope selection,
composition, and common anti-patterns to avoid.

Run with:
    pytest 02_fixture_best_practices.py -v -s
"""
import pytest
from playwright.sync_api import Page, BrowserContext, Browser


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# SCOPE SELECTION
# ============================================
# function (default) - Fresh for EACH test (most isolated)
# class    - Shared within a test class
# module   - Shared within a test file
# session  - Shared across ALL tests (least isolated)

@pytest.fixture(scope="function")
def login_page(page: Page):
    """Per-test fixture: fresh login page for each test."""
    page.goto(f"{BASE_URL}/login")
    return page


@pytest.fixture(scope="session")
def base_url():
    """Session fixture: URL constant shared across all tests."""
    return BASE_URL


# ============================================
# YIELD FIXTURES (SETUP + CLEANUP)
# ============================================

@pytest.fixture
def authenticated_page(page: Page):
    """Fixture with setup AND cleanup using yield.

    Everything before yield = SETUP
    Everything after yield  = CLEANUP (runs even if test fails!)
    """
    # SETUP: Log in
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    yield page  # Test runs here

    # CLEANUP: Log out (always runs)
    logout_btn = page.locator('a[href="/logout"]')
    if logout_btn.is_visible():
        logout_btn.click()


def test_secure_area(authenticated_page: Page):
    """Uses fixture that handles login and logout."""
    assert "/secure" in authenticated_page.url
    heading = authenticated_page.locator("h2")
    assert "Secure Area" in heading.text_content()


# ============================================
# FIXTURE COMPOSITION (fixtures using fixtures)
# ============================================

@pytest.fixture
def navigated_page(page: Page, base_url):
    """Fixture that depends on another fixture."""
    page.goto(f"{base_url}/checkboxes")
    return page


def test_checkboxes_with_composed_fixtures(navigated_page: Page):
    """Uses a fixture that itself uses other fixtures."""
    checkboxes = navigated_page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


# ============================================
# PARAMETERIZED FIXTURES
# ============================================

@pytest.fixture(params=[
    "/login",
    "/checkboxes",
    "/dropdown",
], ids=["login", "checkboxes", "dropdown"])
def target_page(request, page: Page):
    """Fixture that runs test for each page path."""
    page.goto(f"{BASE_URL}{request.param}")
    return page


def test_page_has_heading(target_page: Page):
    """This test runs 3 times: once per fixture param."""
    heading = target_page.locator("h3, h2, h1").first
    assert heading.is_visible()


# ============================================
# FACTORY FIXTURES
# ============================================

@pytest.fixture
def create_page(context: BrowserContext):
    """Factory fixture: creates pages on demand.

    Returns a function that creates new pages.
    Useful when a test needs multiple pages.
    """
    pages = []

    def _create_page(url: str = None) -> Page:
        new_page = context.new_page()
        if url:
            new_page.goto(url)
        pages.append(new_page)
        return new_page

    yield _create_page

    # Cleanup: close all created pages
    for p in pages:
        if not p.is_closed():
            p.close()


def test_multiple_pages(create_page):
    """Uses factory to create multiple pages."""
    page1 = create_page(f"{BASE_URL}/login")
    page2 = create_page(f"{BASE_URL}/checkboxes")

    assert "Login" in page1.locator("h2").text_content()
    assert "Checkboxes" in page2.locator("h3").text_content()


# ============================================
# ANTI-PATTERNS TO AVOID
# ============================================

# ANTI-PATTERN 1: Too many fixtures stacked
#
# BAD:
# def test_bad(page, login_page, logged_in_page, secure_page, data):
#     # Which fixture does what? Confusing!
#
# GOOD: Use 1-3 fixtures per test max
# def test_good(authenticated_page):
#     ...

# ANTI-PATTERN 2: Fixtures with side effects that aren't cleaned up
#
# BAD:
# @pytest.fixture
# def bad_fixture(page):
#     page.goto("/admin")
#     page.locator("#create").click()  # Creates data but never deletes!
#     return page
#
# GOOD: Use yield and cleanup
# @pytest.fixture
# def good_fixture(page):
#     page.goto("/admin")
#     page.locator("#create").click()
#     yield page
#     page.locator("#delete").click()  # Cleanup!

# ANTI-PATTERN 3: Session-scoped fixtures that should be function-scoped
#
# BAD: Sharing state between tests
# @pytest.fixture(scope="session")
# def shared_page(browser):  # One page for all tests!
#     return browser.new_page()  # Tests interfere with each other
#
# GOOD: Use default function scope for page-level fixtures


# ============================================
# CONFTEST.PY BEST PRACTICES
# ============================================
#
# 1. Put shared fixtures in conftest.py (auto-discovered)
# 2. Use multiple conftest.py files for nested directories:
#
#    tests/
#    ├── conftest.py              # Shared across ALL tests
#    ├── login/
#    │   ├── conftest.py          # Login-specific fixtures
#    │   └── test_login.py
#    └── checkout/
#        ├── conftest.py          # Checkout-specific fixtures
#        └── test_checkout.py
#
# 3. Don't import conftest.py - pytest finds it automatically
# 4. Keep conftest.py focused - don't put test functions in it


def test_simple_with_login_page(login_page: Page):
    """Simple test using the login_page fixture."""
    assert login_page.locator("#username").is_visible()


# ============================================
# KEY POINTS:
#
# 1. Choose fixture scope wisely (function > session)
# 2. Use yield for setup + cleanup
# 3. Compose fixtures (fixtures using fixtures)
# 4. Factory fixtures for on-demand creation
# 5. 1-3 fixtures per test maximum
# 6. Cleanup side effects with yield
# 7. Use conftest.py for shared fixtures
#
# Run: pytest 02_fixture_best_practices.py -v -s
# ============================================
