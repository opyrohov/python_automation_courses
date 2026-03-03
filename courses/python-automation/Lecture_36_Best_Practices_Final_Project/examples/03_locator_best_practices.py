"""Example 3: Locator Best Practices

Demonstrates robust locator strategies, preferred approaches,
and patterns to avoid for stable, maintainable tests.

Run with:
    pytest 03_locator_best_practices.py -v -s
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# LOCATOR PRIORITY (BEST → WORST)
# ============================================
#
# 1. get_by_role()    - Semantic, accessible
# 2. get_by_text()    - User-visible text
# 3. get_by_label()   - Form labels
# 4. get_by_test_id() - Dedicated test attribute
# 5. locator("#id")   - Stable ID
# 6. locator("[data-*]") - Data attributes
# 7. locator("css")   - CSS selectors
# 8. locator("xpath") - LAST resort


# ============================================
# BEST: SEMANTIC LOCATORS
# ============================================

def test_role_based_locators(page: Page):
    """get_by_role() - the most robust locator strategy.

    Uses ARIA roles to find elements semantically.
    """
    page.goto(f"{BASE_URL}/login")

    # Find by role + accessible name
    login_button = page.get_by_role("button", name="Login")
    assert login_button.is_visible()

    # Find headings
    heading = page.get_by_role("heading", name="Login Page")
    assert heading.is_visible()

    # Find links
    page.goto(f"{BASE_URL}")
    link = page.get_by_role("link", name="Form Authentication")
    assert link.is_visible()


def test_text_based_locators(page: Page):
    """get_by_text() - find by visible text content."""
    page.goto(f"{BASE_URL}/login")

    # Exact text match
    heading = page.get_by_text("Login Page", exact=True)
    assert heading.is_visible()

    # Partial text match (default)
    subheading = page.get_by_text("login to the secure area")
    assert subheading.is_visible()


def test_label_based_locators(page: Page):
    """get_by_label() - find form elements by their label."""
    page.goto(f"{BASE_URL}/login")

    # Find inputs by their label text
    username_input = page.get_by_label("Username")
    password_input = page.get_by_label("Password")

    username_input.fill("tomsmith")
    password_input.fill("SuperSecretPassword!")

    assert username_input.input_value() == "tomsmith"


# ============================================
# GOOD: STABLE ATTRIBUTE LOCATORS
# ============================================

def test_id_locators(page: Page):
    """IDs are stable - good choice when available."""
    page.goto(f"{BASE_URL}/login")

    username = page.locator("#username")
    password = page.locator("#password")

    username.fill("tomsmith")
    password.fill("SuperSecretPassword!")

    assert username.input_value() == "tomsmith"
    assert password.input_value() == "SuperSecretPassword!"


def test_data_attribute_locators(page: Page):
    """data-* attributes are stable and test-friendly.

    Ask developers to add data-testid attributes!
    """
    page.goto(f"{BASE_URL}/checkboxes")

    # Using type attribute (stable)
    checkboxes = page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


# ============================================
# CHAINING AND FILTERING
# ============================================

def test_locator_chaining(page: Page):
    """Chain locators to narrow down results."""
    page.goto(f"{BASE_URL}/login")

    # Chain: find form, then find elements within it
    form = page.locator("form#login")
    username = form.locator("#username")
    submit = form.locator("button[type='submit']")

    username.fill("tomsmith")
    assert submit.is_visible()


def test_locator_filtering(page: Page):
    """Filter locators for precise targeting."""
    page.goto(f"{BASE_URL}")

    # Filter links that contain specific text
    links = page.locator("ul li a")
    login_link = links.filter(has_text="Form Authentication")
    assert login_link.count() == 1

    login_link.click()
    assert "/login" in page.url


# ============================================
# HANDLING DYNAMIC CONTENT
# ============================================

def test_wait_for_dynamic_content(page: Page):
    """Use expect() for elements that appear dynamically."""
    page.goto(f"{BASE_URL}/dynamic_loading/1")

    # Click start button
    page.locator("#start button").click()

    # Use expect() to wait for dynamic content
    finish = page.locator("#finish h4")
    expect(finish).to_have_text("Hello World!", timeout=10000)


def test_handle_disappearing_elements(page: Page):
    """Check element state before interacting."""
    page.goto(f"{BASE_URL}/checkboxes")

    checkbox = page.locator("input[type='checkbox']").first

    # Check if element exists and is visible before acting
    if checkbox.is_visible():
        checkbox.check()
        assert checkbox.is_checked()


# ============================================
# ANTI-PATTERNS TO AVOID
# ============================================

def test_avoid_brittle_selectors(page: Page):
    """Shows BAD vs GOOD selectors."""
    page.goto(f"{BASE_URL}/login")

    # BAD: Position-dependent CSS
    # page.locator("div:nth-child(2) > div > form > div:nth-child(1) > input")

    # BAD: Deep XPath
    # page.locator("//html/body/div[2]/div/div/form/div[1]/div/input")

    # BAD: Class-based (classes change often)
    # page.locator(".large-12.columns .row input")

    # GOOD: Semantic or ID-based
    username = page.locator("#username")
    assert username.is_visible()

    # GOOD: Role-based
    button = page.get_by_role("button", name="Login")
    assert button.is_visible()


# ============================================
# LOCATOR ABSTRACTION IN PAGE OBJECTS
# ============================================

class LoginPage:
    """Page Object keeps locators in one place."""

    def __init__(self, page: Page):
        self.page = page
        # Define locators once
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login")
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        return self

    def get_flash_text(self) -> str:
        return self.flash_message.text_content()


def test_with_page_object(page: Page):
    """Clean test using Page Object for locator abstraction."""
    login = LoginPage(page).navigate()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "/secure" in page.url


# ============================================
# KEY POINTS:
#
# 1. Prefer get_by_role(), get_by_text(), get_by_label()
# 2. Use IDs and data-testid when semantic locators won't work
# 3. Chain locators to narrow scope
# 4. Use expect() for dynamic content
# 5. Avoid XPath and position-dependent CSS
# 6. Centralize locators in Page Objects
# 7. Ask developers to add data-testid attributes
#
# Run: pytest 03_locator_best_practices.py -v -s
# ============================================
