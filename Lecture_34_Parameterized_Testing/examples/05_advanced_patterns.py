"""Example 5: Advanced Parametrize Patterns

Demonstrates real-world patterns: handling xfail in parametrize,
class-based test organization, and best practices.

Run with: pytest 05_advanced_patterns.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# PATTERN 1: xfail / skip PER CASE
# ============================================

@pytest.mark.parametrize("path,heading", [
    pytest.param("/login", "Login Page", id="login"),
    pytest.param("/checkboxes", "Checkboxes", id="checkboxes"),
    pytest.param(
        "/broken_link", "Not Found",
        id="broken",
        marks=pytest.mark.xfail(reason="Known broken link"),
    ),
    pytest.param(
        "/slow_page", "Slow",
        id="slow",
        marks=pytest.mark.skip(reason="Too slow for CI"),
    ),
])
def test_pages_with_marks(page: Page, path, heading):
    """Individual test cases can have their own marks."""
    page.goto(f"{BASE_URL}{path}")
    assert heading in page.locator("h3, h2").first.text_content()


# ============================================
# PATTERN 2: CLASS-BASED PARAMETRIZE
# ============================================

@pytest.mark.parametrize("username,password", [
    ("tomsmith", "SuperSecretPassword!"),
])
class TestLoginFlow:
    """All methods in this class receive the parameters."""

    def test_can_login(self, page: Page, username, password):
        page.goto(f"{BASE_URL}/login")
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("button[type='submit']").click()
        assert "/secure" in page.url

    def test_can_see_secure_area(self, page: Page, username, password):
        page.goto(f"{BASE_URL}/login")
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("button[type='submit']").click()
        expect(page.locator("h2")).to_have_text(" Secure Area")


# ============================================
# PATTERN 3: DATA CLASSES FOR READABILITY
# ============================================

class LoginCase:
    """Data class for login test cases."""

    def __init__(self, username, password, should_succeed, description=""):
        self.username = username
        self.password = password
        self.should_succeed = should_succeed
        self.description = description

    def __repr__(self):
        return self.description or f"{self.username}"


CASES = [
    LoginCase("tomsmith", "SuperSecretPassword!", True, "valid_login"),
    LoginCase("wrong", "wrong", False, "invalid_both"),
    LoginCase("tomsmith", "bad", False, "wrong_password"),
    LoginCase("", "", False, "empty_fields"),
]


@pytest.mark.parametrize("case", CASES, ids=str)
def test_login_dataclass(page: Page, case):
    """Using data class for clear test representation."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(case.username)
    page.locator("#password").fill(case.password)
    page.locator("button[type='submit']").click()

    if case.should_succeed:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# PATTERN 4: EXPECTED RESULTS TABLE
# ============================================

# Clean table format for test data
TEST_TABLE = [
    # username          password                    success   error_fragment
    ("tomsmith",       "SuperSecretPassword!",       True,    None),
    ("wrong",          "SuperSecretPassword!",       False,   "username is invalid"),
    ("tomsmith",       "wrong_password",             False,   "password is invalid"),
]


@pytest.mark.parametrize(
    "username,password,success,error_fragment",
    TEST_TABLE,
    ids=["valid", "bad_user", "bad_pass"],
)
def test_login_table(page: Page, username, password, success, error_fragment):
    """Table-style parametrize for clarity."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if success:
        assert "/secure" in page.url
    else:
        flash = page.locator("#flash").text_content()
        assert error_fragment in flash


# ============================================
# PATTERN 5: HELPER TO BUILD CASES
# ============================================

def login_case(username, password, *, succeeds=False, error=None, id=None,
               marks=()):
    """Helper to create readable parametrize cases."""
    return pytest.param(
        {"username": username, "password": password,
         "succeeds": succeeds, "error": error},
        id=id or username or "empty",
        marks=marks,
    )


@pytest.mark.parametrize("data", [
    login_case("tomsmith", "SuperSecretPassword!", succeeds=True, id="valid"),
    login_case("wrong", "wrong", error="username is invalid", id="bad_user"),
    login_case("tomsmith", "bad", error="password is invalid", id="bad_pass"),
    login_case("admin", "admin", error="username is invalid", id="guess",
               marks=pytest.mark.xfail(reason="May be valid in some envs")),
])
def test_login_with_helper(page: Page, data):
    """Using helper function for readable test cases."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(data["username"])
    page.locator("#password").fill(data["password"])
    page.locator("button[type='submit']").click()

    if data["succeeds"]:
        assert "/secure" in page.url
    else:
        assert data["error"] in page.locator("#flash").text_content()


# ============================================
# PATTERN 6: PARAMETRIZE WITH expect()
# ============================================

@pytest.mark.parametrize("path,selector,text", [
    ("/login", "h2", "Login Page"),
    ("/checkboxes", "h3", "Checkboxes"),
    ("/dropdown", "h3", "Dropdown List"),
])
def test_with_playwright_expect(page: Page, path, selector, text):
    """Combining parametrize with Playwright expect()."""
    page.goto(f"{BASE_URL}{path}")
    expect(page.locator(selector).first).to_contain_text(text)


# ============================================
# KEY POINTS:
#
# 1. pytest.param(marks=xfail) for known failures
# 2. Class-level parametrize applies to all methods
# 3. Data classes/objects for complex test data
# 4. Table format for clear param organization
# 5. Helper functions for readable case creation
# 6. Combine with expect() for auto-waiting
# 7. Keep test logic simple, data separate
#
# Run: pytest 05_advanced_patterns.py -v --headed
# ============================================
