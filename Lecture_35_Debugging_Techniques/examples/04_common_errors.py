"""Example 4: Common Errors and Solutions

Demonstrates common Playwright errors, why they happen,
and how to fix them. Each test shows a problem and solution.

Run with: pytest 04_common_errors.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# ERROR 1: TimeoutError - Element not found
# ============================================

def test_timeout_error_wrong_selector(page: Page):
    """PROBLEM: Selector doesn't match any element."""
    page.goto(f"{BASE_URL}/login")

    # WRONG: This selector doesn't exist
    # page.locator("#wrong-id").click()  # TimeoutError!

    # FIX: Use correct selector
    page.locator("#username").click()
    print("\n  Fix: Check selector in DevTools or use page.pause()")


def test_timeout_error_dynamic_content(page: Page):
    """PROBLEM: Element appears after a delay."""
    page.goto(f"{BASE_URL}/dynamic_loading/1")
    page.locator("#start button").click()

    # WRONG: Element hasn't appeared yet (it's loading)
    # result = page.locator("#finish h4").text_content()  # May timeout!

    # FIX: Wait for element to be visible
    result_locator = page.locator("#finish h4")
    result_locator.wait_for(state="visible", timeout=10000)
    result = result_locator.text_content()
    assert result == "Hello World!"
    print("\n  Fix: Use wait_for() or expect() for dynamic content")


# ============================================
# ERROR 2: Strict Mode Violation
# ============================================

def test_strict_mode_violation(page: Page):
    """PROBLEM: Locator matches multiple elements."""
    page.goto(f"{BASE_URL}/checkboxes")

    # WRONG: "input" matches BOTH checkboxes
    # page.locator("input").check()  # Strict mode error!

    # FIX 1: Be more specific
    page.locator("input[type='checkbox']").first.check()

    # FIX 2: Use nth()
    page.locator("input[type='checkbox']").nth(0).check()

    # FIX 3: Use .first or .last
    page.locator("input[type='checkbox']").last.uncheck()

    print("\n  Fix: Use .first, .nth(n), or more specific selector")


# ============================================
# ERROR 3: Element not attached to DOM
# ============================================

def test_element_detached(page: Page):
    """PROBLEM: Element removed from DOM after action."""
    page.goto(f"{BASE_URL}/add_remove_elements/")

    # Add element
    page.locator("button", has_text="Add Element").click()

    # Get reference to delete button
    delete_btn = page.locator(".added-manually").first

    # Delete it
    delete_btn.click()

    # WRONG: Element is gone now
    # delete_btn.click()  # Element detached!

    # FIX: Re-query after DOM changes
    remaining = page.locator(".added-manually")
    assert remaining.count() == 0
    print("\n  Fix: Re-query locators after DOM changes")


# ============================================
# ERROR 4: Navigation errors
# ============================================

def test_navigation_timeout(page: Page):
    """PROBLEM: Page takes too long to load."""
    # FIX: Use wait_until option and custom timeout
    try:
        page.goto(f"{BASE_URL}/login",
                  wait_until="domcontentloaded",  # Don't wait for ALL resources
                  timeout=15000)
        print("\n  Fix: Use wait_until='domcontentloaded' for faster navigation")
    except PlaywrightTimeoutError:
        print("\n  Navigation timed out - check network or increase timeout")


# ============================================
# ERROR 5: Frame/iframe errors
# ============================================

def test_element_in_frame(page: Page):
    """PROBLEM: Element is inside an iframe."""
    page.goto(f"{BASE_URL}/iframe")

    # WRONG: Element is in an iframe, not in main page
    # page.locator("#tinymce").fill("text")  # Not found!

    # FIX: Access the frame first
    frame = page.frame_locator("iframe#mce_0_ifr")
    frame.locator("#tinymce").click()
    print("\n  Fix: Use page.frame_locator() for iframe content")


# ============================================
# ERROR 6: Assertions with auto-waiting
# ============================================

def test_assertion_timing(page: Page):
    """PROBLEM: assert checks instantly, doesn't wait."""
    page.goto(f"{BASE_URL}/dynamic_loading/1")
    page.locator("#start button").click()

    # WRONG: Plain assert doesn't wait!
    # assert page.locator("#finish h4").is_visible()  # May be False!

    # FIX: Use expect() which auto-waits
    from playwright.sync_api import expect
    expect(page.locator("#finish h4")).to_be_visible(timeout=10000)
    print("\n  Fix: Use expect() instead of assert for timing-sensitive checks")


# ============================================
# DEBUGGING CHECKLIST
# ============================================
#
# When a test fails, check these in order:
#
# 1. SELECTOR
#    □ Open DevTools → Elements → Check if selector matches
#    □ Use page.pause() to try selectors interactively
#    □ Check for typos in IDs/classes
#
# 2. TIMING
#    □ Is element loaded yet? Add wait_for() or expect()
#    □ Is there an animation/transition? Add small wait
#    □ Is navigation complete? Check wait_until option
#
# 3. FRAMES
#    □ Is element inside an iframe? Use frame_locator()
#    □ Is element in a shadow DOM? Use locator() which pierces shadow
#
# 4. MULTIPLE ELEMENTS
#    □ Does locator match multiple? Use .first, .nth(), or refine
#    □ Check count() to verify number of matches
#
# 5. STATE
#    □ Is element visible? Check is_visible()
#    □ Is element enabled? Check is_enabled()
#    □ Is element attached? Re-query after DOM changes
#
# 6. ENVIRONMENT
#    □ Different between local and CI? Check headless mode
#    □ Different viewport? Check viewport size
#    □ Network issues? Check request logs


# ============================================
# DEBUGGING HELPER FUNCTIONS
# ============================================

def debug_element(page: Page, selector: str):
    """Print debug info about a selector."""
    locator = page.locator(selector)
    count = locator.count()
    print(f"\n  Selector: {selector}")
    print(f"  Matches: {count}")
    if count > 0:
        print(f"  Visible: {locator.first.is_visible()}")
        print(f"  Enabled: {locator.first.is_enabled()}")
        print(f"  Text: {locator.first.text_content()[:50]}")
    else:
        print("  Element NOT FOUND!")


def test_debug_helper(page: Page):
    """Using debug helper function."""
    page.goto(f"{BASE_URL}/login")

    debug_element(page, "#username")      # Found
    debug_element(page, "#wrong-id")      # Not found
    debug_element(page, "input")          # Multiple


# ============================================
# KEY POINTS:
#
# 1. TimeoutError = selector wrong or element not loaded
# 2. Strict mode = locator matches multiple elements
# 3. expect() auto-waits, assert does NOT
# 4. Re-query locators after DOM changes
# 5. Use frame_locator() for iframe content
# 6. wait_until="domcontentloaded" for faster navigation
# 7. Follow the debugging checklist!
#
# Run: pytest 04_common_errors.py -v --headed -s
# ============================================
