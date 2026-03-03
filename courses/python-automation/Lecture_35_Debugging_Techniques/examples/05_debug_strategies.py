"""Example 5: Complete Debugging Workflow

Demonstrates a full debugging strategy combining all techniques:
logging, screenshots, traces, error handling, and flaky test detection.

Run with: pytest 05_debug_strategies.py -v --headed -s
"""
import os
import time
import logging
import pytest
from playwright.sync_api import Page, BrowserContext, expect


BASE_URL = "https://the-internet.herokuapp.com"

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# ============================================
# STRATEGY 1: VERBOSE TEST WITH LOGGING
# ============================================

def test_login_verbose(page: Page):
    """Add logging to understand test flow."""
    logger.info("Starting login test")

    page.goto(f"{BASE_URL}/login")
    logger.info(f"Page loaded: {page.url}")
    logger.info(f"Title: {page.title()}")

    page.locator("#username").fill("tomsmith")
    logger.info("Username filled")

    page.locator("#password").fill("SuperSecretPassword!")
    logger.info("Password filled")

    page.locator("button[type='submit']").click()
    logger.info(f"After click: {page.url}")

    assert "/secure" in page.url
    logger.info("Login test PASSED")


# ============================================
# STRATEGY 2: DEBUG FIXTURE (all-in-one)
# ============================================

@pytest.fixture
def debug_page(context: BrowserContext, request):
    """All-in-one debug fixture: logging + trace + screenshot on failure."""

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()

    # Log console messages
    page.on("console", lambda msg:
        logger.debug(f"Browser console [{msg.type}]: {msg.text}"))

    # Log JS errors
    page.on("pageerror", lambda err:
        logger.error(f"JavaScript error: {err}"))

    # Log failed requests
    page.on("response", lambda resp:
        logger.warning(f"HTTP {resp.status}: {resp.url[:60]}")
        if resp.status >= 400 else None)

    yield page

    # After test: save artifacts on failure
    os.makedirs("debug_output", exist_ok=True)
    test_name = request.node.name

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # Save screenshot
        page.screenshot(path=f"debug_output/FAIL_{test_name}.png", full_page=True)
        logger.info(f"Failure screenshot: debug_output/FAIL_{test_name}.png")

        # Save trace
        context.tracing.stop(path=f"debug_output/FAIL_{test_name}.zip")
        logger.info(f"Failure trace: debug_output/FAIL_{test_name}.zip")
    else:
        context.tracing.stop()  # Discard trace for passing tests


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def test_with_debug_fixture(debug_page):
    """Test with full debug support."""
    debug_page.goto(f"{BASE_URL}/login")
    debug_page.locator("#username").fill("tomsmith")
    debug_page.locator("#password").fill("SuperSecretPassword!")
    debug_page.locator("button[type='submit']").click()
    assert "/secure" in debug_page.url


# ============================================
# STRATEGY 3: RETRY FLAKY TESTS
# ============================================
#
# Install: pip install pytest-rerunfailures
#
# Usage:
#   pytest --reruns 3                    # Retry failed 3 times
#   pytest --reruns 3 --reruns-delay 2   # With 2s delay
#
# Or per-test:
#   @pytest.mark.flaky(reruns=3, reruns_delay=1)
#   def test_flaky(): ...


# ============================================
# STRATEGY 4: WAIT UTILITIES
# ============================================

def wait_for_stable(page: Page, selector: str, timeout: int = 5000):
    """Wait for element to be stable (visible + enabled + not moving)."""
    locator = page.locator(selector)
    locator.wait_for(state="visible", timeout=timeout)
    # Additional stability check
    expect(locator).to_be_enabled(timeout=timeout)
    return locator


def test_with_wait_utility(page: Page):
    """Using wait utility for reliable element interaction."""
    page.goto(f"{BASE_URL}/login")

    username = wait_for_stable(page, "#username")
    username.fill("tomsmith")

    password = wait_for_stable(page, "#password")
    password.fill("SuperSecretPassword!")

    button = wait_for_stable(page, "button[type='submit']")
    button.click()

    assert "/secure" in page.url


# ============================================
# STRATEGY 5: ELEMENT STATE DUMP
# ============================================

def dump_page_state(page: Page, label: str = ""):
    """Dump current page state for debugging."""
    print(f"\n  === PAGE STATE {label} ===")
    print(f"  URL:     {page.url}")
    print(f"  Title:   {page.title()}")

    viewport = page.viewport_size
    if viewport:
        print(f"  Viewport: {viewport['width']}x{viewport['height']}")

    # Count key elements
    forms = page.locator("form").count()
    buttons = page.locator("button").count()
    inputs = page.locator("input").count()
    links = page.locator("a").count()
    print(f"  Forms: {forms}, Buttons: {buttons}, Inputs: {inputs}, Links: {links}")
    print(f"  ========================")


def test_with_state_dump(page: Page):
    """Dump page state at key points."""
    page.goto(f"{BASE_URL}/login")
    dump_page_state(page, "AFTER LOAD")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    dump_page_state(page, "AFTER LOGIN")

    assert "/secure" in page.url


# ============================================
# VS CODE DEBUGGING
# ============================================
#
# 1. Create .vscode/launch.json:
# {
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Pytest: Current File",
#             "type": "debugpy",
#             "request": "launch",
#             "module": "pytest",
#             "args": [
#                 "${file}",
#                 "-v",
#                 "--headed",
#                 "-s"
#             ],
#             "console": "integratedTerminal"
#         }
#     ]
# }
#
# 2. Set breakpoints by clicking left of line numbers
# 3. Press F5 to start debugging
# 4. Use Step Over (F10), Step Into (F11), Continue (F5)
# 5. Watch variables in the Debug panel


# ============================================
# DEBUGGING QUICK REFERENCE
# ============================================
#
# VISUAL DEBUGGING:
#   pytest --headed --slowmo 1000
#   PWDEBUG=1 pytest --headed
#   page.pause()
#
# ARTIFACTS:
#   pytest --screenshot only-on-failure
#   pytest --tracing retain-on-failure
#   pytest --video retain-on-failure
#   playwright show-trace trace.zip
#
# LOGGING:
#   page.on("console", lambda m: print(m.text))
#   page.on("pageerror", lambda e: print(e))
#   pytest -s  (show print output)
#
# COMMON FIXES:
#   TimeoutError    → fix selector or add wait
#   Strict mode     → use .first or .nth(n)
#   Detached        → re-query after DOM change
#   In iframe       → use frame_locator()
#   Timing          → use expect() not assert


# ============================================
# KEY POINTS:
#
# 1. Add logging for test flow visibility
# 2. Debug fixture: trace + screenshot + console
# 3. pytest-rerunfailures for flaky tests
# 4. Wait utilities for reliable interactions
# 5. Page state dump for quick diagnostics
# 6. VS Code launch.json for IDE debugging
# 7. Always check: selector, timing, frames, state
#
# Run: pytest 05_debug_strategies.py -v --headed -s
# ============================================
