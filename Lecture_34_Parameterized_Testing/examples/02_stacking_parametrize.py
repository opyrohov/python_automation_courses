"""Example 2: Stacking Parametrize - Cartesian Product

Demonstrates how stacking multiple @pytest.mark.parametrize decorators
creates a cartesian product (all combinations) of parameters.

Run with: pytest 02_stacking_parametrize.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# STACKING = CARTESIAN PRODUCT
# ============================================
# Two decorators with 2 values each = 2 x 2 = 4 tests!

@pytest.mark.parametrize("password", [
    "SuperSecretPassword!",
    "wrong_password",
])
@pytest.mark.parametrize("username", [
    "tomsmith",
    "wrong_user",
])
def test_login_matrix(page: Page, username, password):
    """All combinations: tomsmith+correct, tomsmith+wrong, wrong+correct, wrong+wrong."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if username == "tomsmith" and password == "SuperSecretPassword!":
        assert "/secure" in page.url
    else:
        assert "/login" in page.url

    print(f"\n  {username} + {password[:10]}... -> {page.url.split('/')[-1]}")


# ============================================
# VIEWPORT x PAGE MATRIX
# ============================================

@pytest.mark.parametrize("path", [
    "/login",
    "/checkboxes",
    "/dropdown",
])
@pytest.mark.parametrize("width,height", [
    (1920, 1080),
    (375, 812),
], ids=["desktop", "mobile"])
def test_responsive_pages(page: Page, width, height, path):
    """3 pages x 2 viewports = 6 tests."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{BASE_URL}{path}")
    assert page.title() == "The Internet"
    print(f"\n  {path} @ {width}x{height}")


# ============================================
# THREE-LEVEL STACKING
# ============================================

@pytest.mark.parametrize("action", ["check", "uncheck"])
@pytest.mark.parametrize("checkbox_index", [0, 1], ids=["first", "second"])
def test_checkbox_matrix(page: Page, checkbox_index, action):
    """2 checkboxes x 2 actions = 4 tests."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkbox = page.locator("input[type='checkbox']").nth(checkbox_index)

    if action == "check":
        checkbox.check()
        assert checkbox.is_checked()
    else:
        checkbox.uncheck()
        assert not checkbox.is_checked()

    print(f"\n  Checkbox {checkbox_index}: {action}")


# ============================================
# STACKING WITH MARKS
# ============================================

@pytest.mark.parametrize("option_value", [
    pytest.param("1", id="option_1"),
    pytest.param("2", id="option_2"),
])
@pytest.mark.parametrize("width,height", [
    pytest.param(1280, 720, id="desktop"),
    pytest.param(375, 812, id="mobile"),
])
def test_dropdown_responsive(page: Page, width, height, option_value):
    """Dropdown options x viewports with named IDs."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{BASE_URL}/dropdown")

    dropdown = page.locator("#dropdown")
    dropdown.select_option(value=option_value)

    selected = dropdown.locator("option:checked")
    assert f"Option {option_value}" in selected.text_content()


# ============================================
# WHEN TO USE STACKING
# ============================================
#
# USE stacking when:
#   - You want ALL combinations (matrix)
#   - Parameters are independent
#   - Cross-browser x viewport testing
#   - Feature x configuration testing
#
# DON'T stack when:
#   - Parameters are related (use single parametrize with tuples)
#   - Not all combinations make sense
#   - Too many combinations (exponential growth!)
#
# Example: 3 browsers x 4 viewports x 5 pages = 60 tests!
#


# ============================================
# KEY POINTS:
#
# 1. Stacking = cartesian product (all combos)
# 2. N x M parameters = N*M test cases
# 3. Order: bottom decorator applied first
# 4. Great for matrix/cross-browser testing
# 5. Be careful with too many combinations
# 6. Use pytest.param for IDs with stacking
# 7. Parameters must be independent
#
# Run: pytest 02_stacking_parametrize.py -v --headed -s
# ============================================
