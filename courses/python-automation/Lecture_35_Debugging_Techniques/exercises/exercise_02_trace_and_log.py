"""Exercise 2: Add Tracing and Logging to Tests

Your task:
1. Create a debug fixture with console logging and tracing
2. Create a logging utility for page state
3. Write tests that use these debug tools

Requirements:

Fixtures:
- debug_page: Fixture that:
  - Starts tracing (screenshots + snapshots)
  - Logs console messages to print
  - Logs JS errors to print
  - On failure: saves screenshot + trace
  - On success: discards trace

Functions:
- log_page_state(page, label): Print URL, title, element counts
- log_locator_info(page, selector): Print match count, visibility, text

Tests:
- test_login_with_debug: Login test using debug_page fixture
- test_checkboxes_with_logging: Use log_page_state at key points
- test_find_element: Use log_locator_info to debug selectors

Run with: pytest exercise_02_trace_and_log.py -v --headed -s
"""
import os
import pytest
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# TODO: Hook for test result
# ============================================

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, f"rep_{rep.when}", rep)


# ============================================
# TODO: Debug fixture
# ============================================

# @pytest.fixture
# def debug_page(context: BrowserContext, request):
#     """Full debug fixture with tracing and logging."""
#     # Start tracing
#     # Create page
#     # Add console listener: page.on("console", ...)
#     # Add error listener: page.on("pageerror", ...)
#
#     # yield page
#
#     # After test:
#     # If failed: save screenshot + trace
#     # If passed: discard trace
#     pass


# ============================================
# TODO: log_page_state utility
# ============================================

# def log_page_state(page: Page, label: str = ""):
#     """Print current page state."""
#     # Print: label, URL, title, viewport
#     # Count: forms, buttons, inputs, links
#     pass


# ============================================
# TODO: log_locator_info utility
# ============================================

# def log_locator_info(page: Page, selector: str):
#     """Print info about a locator."""
#     # Print: selector, match count
#     # If matches > 0: visible, enabled, text content
#     pass


# ============================================
# TODO: Tests
# ============================================

# def test_login_with_debug(debug_page):
#     """Login test with full debug support."""
#     debug_page.goto(f"{BASE_URL}/login")
#     debug_page.locator("#username").fill("tomsmith")
#     debug_page.locator("#password").fill("SuperSecretPassword!")
#     debug_page.locator("button[type='submit']").click()
#     assert "/secure" in debug_page.url


# def test_checkboxes_with_logging(page: Page):
#     """Use log_page_state at key points."""
#     page.goto(f"{BASE_URL}/checkboxes")
#     log_page_state(page, "AFTER LOAD")
#
#     page.locator("input[type='checkbox']").first.check()
#     log_page_state(page, "AFTER CHECK")
#
#     assert page.locator("input[type='checkbox']").first.is_checked()


# def test_find_element(page: Page):
#     """Use log_locator_info to debug selectors."""
#     page.goto(f"{BASE_URL}/login")
#     log_locator_info(page, "#username")
#     log_locator_info(page, "#password")
#     log_locator_info(page, "button")
#     log_locator_info(page, "#nonexistent")
