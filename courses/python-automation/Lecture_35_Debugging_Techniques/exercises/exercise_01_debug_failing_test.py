"""Exercise 1: Debug and Fix Failing Tests

Your task:
1. Each test below has a BUG that causes it to fail
2. Use debugging techniques to find the problem
3. Fix each test so it passes

Debugging tips:
- Run with --headed to see the browser
- Add page.pause() before the failing line
- Use PWDEBUG=1 for the inspector
- Check selectors in browser DevTools
- Read error messages carefully!

Run with: pytest exercise_01_debug_failing_test.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# BUG 1: Wrong selector
# ============================================

def test_login_bug_selector(page: Page):
    """BUG: One of the selectors is wrong. Find and fix it."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#pasword").fill("SuperSecretPassword!")  # BUG HERE
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


# ============================================
# BUG 2: Assertion too early
# ============================================

def test_dynamic_loading_bug_timing(page: Page):
    """BUG: Assertion runs before element appears."""
    page.goto(f"{BASE_URL}/dynamic_loading/1")
    page.locator("#start button").click()
    # BUG: element is still loading!
    assert page.locator("#finish h4").text_content() == "Hello World!"


# ============================================
# BUG 3: Multiple elements (strict mode)
# ============================================

def test_checkboxes_bug_strict(page: Page):
    """BUG: Locator matches multiple elements."""
    page.goto(f"{BASE_URL}/checkboxes")
    # BUG: "input" matches both checkboxes!
    page.locator("input").check()
    assert page.locator("input").is_checked()


# ============================================
# BUG 4: Wrong expected value
# ============================================

def test_dropdown_bug_expected(page: Page):
    """BUG: Expected value doesn't match actual text."""
    page.goto(f"{BASE_URL}/dropdown")
    page.locator("#dropdown").select_option(value="1")
    selected = page.locator("#dropdown option:checked")
    # BUG: Actual text might have whitespace or different format
    assert selected.text_content() == "Option1"


# ============================================
# BUG 5: Element in iframe
# ============================================

def test_iframe_bug_frame(page: Page):
    """BUG: Element is inside an iframe."""
    page.goto(f"{BASE_URL}/iframe")
    # BUG: #tinymce is inside an iframe!
    editor = page.locator("#tinymce")
    assert editor.is_visible()


# ============================================
# BUG 6: Wrong assertion logic
# ============================================

def test_login_error_bug_logic(page: Page):
    """BUG: Logic error in assertion."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("wrong_user")
    page.locator("#password").fill("wrong_pass")
    page.locator("button[type='submit']").click()
    # BUG: After failed login, URL should contain /login not /secure
    assert "/secure" in page.url
