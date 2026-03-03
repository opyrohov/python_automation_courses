"""Example 1: Parametrize Basics - In Depth

Demonstrates various ways to use @pytest.mark.parametrize
beyond the basics: dict parameters, custom IDs, marks on specific cases.

Run with: pytest 01_parametrize_basics.py -v --headed
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# RECAP: Basic Parametrize
# ============================================

@pytest.mark.parametrize("path", [
    "/login",
    "/checkboxes",
    "/dropdown",
])
def test_pages_load(page: Page, path):
    """Single parameter - simplest form."""
    page.goto(f"{BASE_URL}{path}")
    assert page.title() == "The Internet"


# ============================================
# MULTIPLE PARAMETERS
# ============================================

@pytest.mark.parametrize("username,password,expected_url", [
    ("tomsmith", "SuperSecretPassword!", "/secure"),
    ("wrong", "wrong", "/login"),
    ("tomsmith", "bad", "/login"),
])
def test_login_scenarios(page: Page, username, password, expected_url):
    """Multiple parameters as comma-separated string."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    assert expected_url in page.url


# ============================================
# CUSTOM TEST IDs
# ============================================

@pytest.mark.parametrize("username,password,expected_url", [
    ("tomsmith", "SuperSecretPassword!", "/secure"),
    ("wrong", "wrong", "/login"),
    ("", "", "/login"),
], ids=["valid_credentials", "invalid_both", "empty_fields"])
def test_login_with_ids(page: Page, username, password, expected_url):
    """Custom IDs make test output readable."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    assert expected_url in page.url


# ============================================
# DICT PARAMETERS
# ============================================

LOGIN_CASES = [
    {
        "id": "valid_login",
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
        "should_succeed": True,
    },
    {
        "id": "wrong_username",
        "username": "wrong",
        "password": "SuperSecretPassword!",
        "should_succeed": False,
        "error": "Your username is invalid!",
    },
    {
        "id": "wrong_password",
        "username": "tomsmith",
        "password": "wrong",
        "should_succeed": False,
        "error": "Your password is invalid!",
    },
]


@pytest.mark.parametrize("case", LOGIN_CASES, ids=lambda c: c["id"])
def test_login_with_dicts(page: Page, case):
    """Using dictionaries for complex test data."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(case["username"])
    page.locator("#password").fill(case["password"])
    page.locator("button[type='submit']").click()

    if case["should_succeed"]:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url
        assert case["error"] in page.locator("#flash").text_content()


# ============================================
# pytest.param FOR MARKS AND IDs
# ============================================

@pytest.mark.parametrize("path,heading", [
    pytest.param("/login", "Login Page", id="login"),
    pytest.param("/checkboxes", "Checkboxes", id="checkboxes"),
    pytest.param("/dropdown", "Dropdown List", id="dropdown"),
    pytest.param(
        "/nonexistent", "404",
        id="not_found",
        marks=pytest.mark.xfail(reason="Page doesn't exist")
    ),
])
def test_page_headings(page: Page, path, heading):
    """pytest.param allows marks on individual test cases."""
    page.goto(f"{BASE_URL}{path}")
    h = page.locator("h3").first
    assert heading in h.text_content()


# ============================================
# PARAMETRIZE WITH LISTS/TUPLES
# ============================================

CHECKBOX_ACTIONS = [
    (0, "check", True),    # First checkbox, check it, expect checked
    (1, "uncheck", False), # Second checkbox, uncheck it, expect unchecked
]


@pytest.mark.parametrize("index,action,expected", CHECKBOX_ACTIONS,
                         ids=["check_first", "uncheck_second"])
def test_checkbox_actions(page: Page, index, action, expected):
    """Parametrize with tuples for multiple values."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkbox = page.locator("input[type='checkbox']").nth(index)

    if action == "check":
        checkbox.check()
    else:
        checkbox.uncheck()

    assert checkbox.is_checked() == expected


# ============================================
# KEY POINTS:
#
# 1. "param1,param2" - comma-separated names
# 2. ids=["name1", "name2"] - custom test names
# 3. ids=lambda - dynamic ID generation
# 4. Dict parameters for complex data
# 5. pytest.param() for per-case marks and IDs
# 6. Constants for large parameter sets
# 7. xfail on specific parametrized cases
#
# Run: pytest 01_parametrize_basics.py -v --headed
# ============================================
