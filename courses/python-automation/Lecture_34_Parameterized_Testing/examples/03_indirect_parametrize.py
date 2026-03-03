"""Example 3: Indirect Parametrization

Demonstrates how to pass parameters to fixtures using indirect=True.
This lets you parametrize the fixture setup, not just the test.

Run with: pytest 03_indirect_parametrize.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# INDIRECT PARAMETRIZE
# ============================================
# indirect=True passes the parameter to the FIXTURE,
# not directly to the test function.

@pytest.fixture
def target_page(request, page: Page):
    """Fixture that navigates to the parametrized path."""
    path = request.param
    page.goto(f"{BASE_URL}{path}")
    return page


@pytest.mark.parametrize("target_page", [
    "/login",
    "/checkboxes",
    "/dropdown",
], indirect=True)
def test_pages_have_content(target_page):
    """Each parameter is passed to the target_page fixture."""
    assert target_page.title() == "The Internet"
    # Page is already navigated by the fixture!


# ============================================
# INDIRECT WITH COMPLEX DATA
# ============================================

@pytest.fixture
def login_result(request, page: Page):
    """Fixture that performs login with parametrized credentials."""
    creds = request.param
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(creds["username"])
    page.locator("#password").fill(creds["password"])
    page.locator("button[type='submit']").click()
    return page


@pytest.mark.parametrize("login_result", [
    {"username": "tomsmith", "password": "SuperSecretPassword!"},
    {"username": "wrong", "password": "wrong"},
], indirect=True, ids=["valid", "invalid"])
def test_login_result(login_result):
    """The fixture does the login, test checks the result."""
    # Page is already after login attempt
    url = login_result.url
    print(f"\n  Result URL: {url}")
    assert "the-internet" in url


# ============================================
# PARAMETRIZED FIXTURES (alternative approach)
# ============================================

@pytest.fixture(params=[
    "/login",
    "/checkboxes",
    "/dropdown",
], ids=["login", "checkboxes", "dropdown"])
def navigated_page(request, page: Page):
    """Fixture with built-in params (runs for each param)."""
    page.goto(f"{BASE_URL}{request.param}")
    return page


def test_page_loaded(navigated_page):
    """This test runs 3 times (once per fixture param)."""
    assert navigated_page.title() == "The Internet"


def test_page_has_heading(navigated_page):
    """This ALSO runs 3 times - each test using this fixture does."""
    heading = navigated_page.locator("h3, h2").first
    assert heading.is_visible()


# ============================================
# VIEWPORT FIXTURE WITH INDIRECT
# ============================================

@pytest.fixture
def viewport_page(request, page: Page):
    """Fixture that sets viewport from parameter."""
    viewport = request.param
    page.set_viewport_size(viewport)
    page.goto(BASE_URL)
    return page


@pytest.mark.parametrize("viewport_page", [
    {"width": 1920, "height": 1080},
    {"width": 375, "height": 812},
], indirect=True, ids=["desktop", "mobile"])
def test_viewport_heading(viewport_page):
    """Test heading visibility at different viewports."""
    heading = viewport_page.locator("h1")
    assert heading.is_visible()
    size = viewport_page.viewport_size
    print(f"\n  Viewport: {size['width']}x{size['height']}")


# ============================================
# MIXING DIRECT AND INDIRECT
# ============================================

@pytest.fixture
def page_at_path(request, page: Page):
    """Navigate to parametrized path."""
    page.goto(f"{BASE_URL}{request.param}")
    return page


@pytest.mark.parametrize(
    "page_at_path,expected_tag",
    [
        ("/login", "h2"),
        ("/checkboxes", "h3"),
        ("/dropdown", "h3"),
    ],
    indirect=["page_at_path"],  # Only page_at_path is indirect
    ids=["login", "checkboxes", "dropdown"],
)
def test_heading_tag(page_at_path, expected_tag):
    """page_at_path is indirect (fixture), expected_tag is direct."""
    heading = page_at_path.locator(expected_tag).first
    assert heading.is_visible()


# ============================================
# KEY POINTS:
#
# 1. indirect=True passes params to fixture via request.param
# 2. Fixture does setup, test does assertions
# 3. @pytest.fixture(params=[...]) - built-in parametrization
# 4. indirect=["name"] - only specific params are indirect
# 5. Complex data (dicts) can be passed to fixtures
# 6. Great for setup variations (viewport, auth, navigation)
# 7. All tests using parametrized fixture run for each param
#
# Run: pytest 03_indirect_parametrize.py -v --headed -s
# ============================================
