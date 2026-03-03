"""Exercise 2: Matrix Testing - Cross-Browser and Viewport

Your task:
1. Use stacking parametrize for matrix testing
2. Use indirect parametrization for viewport fixture
3. Create a comprehensive responsive test suite

Requirements:

Tests to write:
- test_responsive_pages: Stack viewport x page_path parameters
  Viewports: desktop (1920x1080), tablet (768x1024), mobile (375x812)
  Pages: /login, /checkboxes, /dropdown

- test_viewport_heading: Use indirect parametrize with viewport fixture
  The fixture should set viewport_size and navigate to a URL

- test_checkbox_actions: Stack checkbox_index x action parameters
  Checkboxes: 0, 1
  Actions: check, uncheck

- test_dropdown_viewport: Stack dropdown option x viewport

Bonus:
- Use pytest_generate_tests to load page data from a JSON file

Run with: pytest exercise_02_matrix_testing.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# TODO: test_responsive_pages (stacked parametrize)
# ============================================

# @pytest.mark.parametrize("path", ["/login", "/checkboxes", "/dropdown"])
# @pytest.mark.parametrize("width,height", [
#     (1920, 1080),
#     (768, 1024),
#     (375, 812),
# ], ids=["desktop", "tablet", "mobile"])
# def test_responsive_pages(page: Page, width, height, path):
#     page.set_viewport_size({"width": width, "height": height})
#     page.goto(f"{BASE_URL}{path}")
#     assert page.title() == "The Internet"
#     print(f"\n  {path} @ {width}x{height}")


# ============================================
# TODO: test_viewport_heading (indirect parametrize)
# ============================================

# @pytest.fixture
# def viewport_page(request, page: Page):
#     """Fixture: set viewport from parameter."""
#     config = request.param
#     page.set_viewport_size({"width": config["width"], "height": config["height"]})
#     page.goto(f"{BASE_URL}{config['path']}")
#     return page
#
# @pytest.mark.parametrize("viewport_page", [
#     {"width": 1920, "height": 1080, "path": "/login"},
#     {"width": 375, "height": 812, "path": "/login"},
# ], indirect=True, ids=["desktop_login", "mobile_login"])
# def test_viewport_heading(viewport_page):
#     assert viewport_page.locator("h2").is_visible()


# ============================================
# TODO: test_checkbox_actions (stacked)
# ============================================

# @pytest.mark.parametrize("action", ["check", "uncheck"])
# @pytest.mark.parametrize("index", [0, 1], ids=["first", "second"])
# def test_checkbox_actions(page: Page, index, action):
#     page.goto(f"{BASE_URL}/checkboxes")
#     checkbox = page.locator("input[type='checkbox']").nth(index)
#     if action == "check":
#         checkbox.check()
#         assert checkbox.is_checked()
#     else:
#         checkbox.uncheck()
#         assert not checkbox.is_checked()


# ============================================
# TODO: test_dropdown_viewport (stacked)
# ============================================

# @pytest.mark.parametrize("option", ["1", "2"])
# @pytest.mark.parametrize("width,height", [
#     (1280, 720),
#     (375, 812),
# ], ids=["desktop", "mobile"])
# def test_dropdown_viewport(page: Page, width, height, option):
#     page.set_viewport_size({"width": width, "height": height})
#     page.goto(f"{BASE_URL}/dropdown")
#     page.locator("#dropdown").select_option(value=option)
#     selected = page.locator("#dropdown option:checked")
#     assert f"Option {option}" in selected.text_content()
