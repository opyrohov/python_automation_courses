"""Exercise 2: Configure Screenshots and Traces on Failure

Your task:
1. Create a fixture that captures screenshots on test failure
2. Create a fixture that records traces
3. Write tests that demonstrate failure handling (some intentionally fail)

Requirements:

Fixtures:
- screenshot_on_failure: Auto-captures screenshot when test fails
  - Save to screenshots/ folder
  - Name: FAIL_{test_name}.png
  - Use full_page=True

- traced_context: Records a Playwright trace
  - Start trace with screenshots=True, snapshots=True
  - Save trace to traces/ folder
  - Name: {test_name}.zip

- pytest_runtest_makereport hook: Store test result for fixtures

Tests:
- test_passing_test: A normal passing test (no screenshot)
- test_failing_assertion: Intentionally fails (should get screenshot)
- test_with_trace: Uses traced_context, performs some actions
- test_manual_screenshot: Takes a manual screenshot at a specific step

Run with: pytest exercise_02_failure_handling.py -v --headed
Note: Some tests are expected to fail (that's the point!)
"""
import pytest
import os
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# HOOK FOR TEST RESULT
# ============================================

# TODO: Implement pytest_runtest_makereport hook
# This stores the test result so fixtures can check if test failed
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, f"rep_{rep.when}", rep)


# ============================================
# SCREENSHOT FIXTURE
# ============================================

# TODO: Create screenshot_on_failure fixture
# @pytest.fixture(autouse=True)
# def screenshot_on_failure(page, request):
#     yield page
#
#     # After test: check if failed
#     # if failed:
#     #   - Create screenshots/ directory
#     #   - Save screenshot as FAIL_{test_name}.png
#     #   - Use full_page=True
#     #   - Print path for debugging


# ============================================
# TRACE FIXTURE
# ============================================

# TODO: Create traced_context fixture
# @pytest.fixture
# def traced_page(context, request):
#     # Start tracing (screenshots=True, snapshots=True, sources=True)
#     # Create page from context
#     # yield page
#     # Stop tracing and save to traces/{test_name}.zip
#     # Print path and view command


# ============================================
# TESTS
# ============================================

# TODO: test_passing_test - should pass, no screenshot
# def test_passing_test(page):
#     page.goto(f"{BASE_URL}/login")
#     assert page.locator("h2").text_content() == "Login Page"


# TODO: test_failing_assertion - should FAIL and get screenshot
# def test_failing_assertion(page):
#     page.goto(f"{BASE_URL}/login")
#     # This will fail intentionally!
#     assert page.locator("h2").text_content() == "Wrong Title"


# TODO: test_with_trace - use traced_page fixture
# def test_with_trace(traced_page):
#     traced_page.goto(f"{BASE_URL}/login")
#     traced_page.locator("#username").fill("tomsmith")
#     traced_page.locator("#password").fill("SuperSecretPassword!")
#     traced_page.locator("button[type='submit']").click()
#     assert "/secure" in traced_page.url


# TODO: test_manual_screenshot - take screenshot at specific step
# def test_manual_screenshot(page):
#     page.goto(f"{BASE_URL}/login")
#     # Take screenshot before login
#     os.makedirs("screenshots", exist_ok=True)
#     page.screenshot(path="screenshots/before_login.png")
#
#     page.locator("#username").fill("tomsmith")
#     page.locator("#password").fill("SuperSecretPassword!")
#     page.locator("button[type='submit']").click()
#
#     # Take screenshot after login
#     page.screenshot(path="screenshots/after_login.png")
#     assert "/secure" in page.url
