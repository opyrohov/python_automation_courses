"""Example 3: Parameterized Tests

Demonstrates how to use @pytest.mark.parametrize to run the same test
with different input data. One function generates multiple test cases.

Run with: pytest 03_parameterized_tests.py -v --headed
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# SINGLE PARAMETER
# ============================================

@pytest.mark.parametrize("page_path", [
    "/login",
    "/checkboxes",
    "/dropdown",
    "/inputs",
])
def test_page_loads(page: Page, page_path):
    """Test that various pages load successfully."""
    page.goto(f"{BASE_URL}{page_path}")
    # Page should have some content
    assert page.locator("h3").is_visible() or page.locator("h2").is_visible()


# ============================================
# MULTIPLE PARAMETERS
# ============================================

@pytest.mark.parametrize("username,password,should_succeed", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("wrong", "wrong", False),
    ("tomsmith", "wrong", False),
    ("", "", False),
])
def test_login_scenarios(page: Page, username, password, should_succeed):
    """Test login with different credential combinations."""
    page.goto(f"{BASE_URL}/login")

    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if should_succeed:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# PARAMETRIZE WITH IDs
# ============================================

@pytest.mark.parametrize("option_value,option_text", [
    ("1", "Option 1"),
    ("2", "Option 2"),
], ids=["select-option-1", "select-option-2"])
def test_dropdown_selection(page: Page, option_value, option_text):
    """Test dropdown selection with named test IDs."""
    page.goto(f"{BASE_URL}/dropdown")

    dropdown = page.locator("#dropdown")
    dropdown.select_option(value=option_value)

    # Verify selected option
    selected = dropdown.locator("option:checked")
    assert selected.text_content().strip() == option_text


# ============================================
# PARAMETRIZE WITH VIEWPORT SIZES
# ============================================

@pytest.mark.parametrize("width,height,device_name", [
    (1920, 1080, "Desktop"),
    (1366, 768, "Laptop"),
    (768, 1024, "Tablet"),
    (375, 812, "Mobile"),
])
def test_responsive_layout(page: Page, width, height, device_name):
    """Test that page loads at different viewport sizes."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{BASE_URL}")

    # Page should load at any size
    assert page.title() == "The Internet"
    print(f"  [{device_name}] {width}x{height} - OK")


# ============================================
# PARAMETRIZE WITH ERROR MESSAGES
# ============================================

@pytest.mark.parametrize("username,password,error_fragment", [
    ("wrong", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
])
def test_login_error_messages(page: Page, username, password, error_fragment):
    """Test that correct error messages are shown."""
    page.goto(f"{BASE_URL}/login")

    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    assert error_fragment in flash.text_content()


# ============================================
# KEY POINTS:
#
# 1. @pytest.mark.parametrize("param", [values])
# 2. Multiple params: "param1,param2", [(v1,v2), ...]
# 3. ids= for readable test names
# 4. Each parameter set = separate test run
# 5. page fixture works with parametrize
# 6. Great for data-driven testing
#
# Run: pytest 03_parameterized_tests.py -v --headed -s
# ============================================
