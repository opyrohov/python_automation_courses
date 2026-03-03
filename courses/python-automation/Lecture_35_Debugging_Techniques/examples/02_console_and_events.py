"""Example 2: Console Logs and Browser Events

Demonstrates how to capture browser console messages, JavaScript errors,
network requests, and other events for debugging.

Run with: pytest 02_console_and_events.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page, ConsoleMessage, Request, Response


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# CAPTURING CONSOLE MESSAGES
# ============================================

def test_capture_console(page: Page):
    """Capture all browser console messages."""
    messages = []

    def on_console(msg: ConsoleMessage):
        messages.append(f"[{msg.type}] {msg.text}")
        print(f"  CONSOLE [{msg.type}]: {msg.text}")

    page.on("console", on_console)
    page.goto(f"{BASE_URL}/javascript_alerts")

    # Trigger an alert (which may produce console output)
    page.locator("button", has_text="Click for JS Alert").click()
    page.on("dialog", lambda dialog: dialog.accept())

    print(f"\n  Total console messages: {len(messages)}")


# ============================================
# CAPTURING JAVASCRIPT ERRORS
# ============================================

def test_capture_js_errors(page: Page):
    """Capture JavaScript errors on the page."""
    errors = []

    def on_page_error(error):
        errors.append(str(error))
        print(f"  JS ERROR: {error}")

    page.on("pageerror", on_page_error)
    page.goto(f"{BASE_URL}/javascript_error")

    # This page has a known JS error
    print(f"\n  JavaScript errors found: {len(errors)}")
    for err in errors:
        print(f"    - {err[:80]}")


# ============================================
# MONITORING NETWORK REQUESTS
# ============================================

def test_monitor_network(page: Page):
    """Monitor network requests and responses."""
    requests_log = []

    def on_request(request: Request):
        requests_log.append({
            "method": request.method,
            "url": request.url,
        })

    def on_response(response: Response):
        if response.status >= 400:
            print(f"  FAILED REQUEST: {response.status} {response.url}")

    page.on("request", on_request)
    page.on("response", on_response)

    page.goto(f"{BASE_URL}/login")

    print(f"\n  Total requests: {len(requests_log)}")
    for req in requests_log[:5]:
        print(f"    {req['method']} {req['url'][:60]}")


# ============================================
# NETWORK LOGGING FIXTURE
# ============================================

@pytest.fixture
def page_with_logging(page: Page):
    """Page with network and console logging enabled."""
    # Console messages
    page.on("console", lambda msg: print(f"  [console.{msg.type}] {msg.text}"))

    # JS errors
    page.on("pageerror", lambda err: print(f"  [JS ERROR] {err}"))

    # Failed responses (4xx, 5xx)
    page.on("response", lambda resp:
        print(f"  [HTTP {resp.status}] {resp.url[:60]}")
        if resp.status >= 400 else None
    )

    return page


def test_with_logging(page_with_logging):
    """All browser events are logged automatically."""
    page_with_logging.goto(f"{BASE_URL}/login")
    page_with_logging.locator("#username").fill("tomsmith")
    page_with_logging.locator("#password").fill("SuperSecretPassword!")
    page_with_logging.locator("button[type='submit']").click()
    assert "/secure" in page_with_logging.url


# ============================================
# PYTHON LOGGING MODULE
# ============================================

import logging

logger = logging.getLogger(__name__)


def test_with_python_logging(page: Page):
    """Using Python's logging module for structured output."""
    logger.info("Starting login test")

    page.goto(f"{BASE_URL}/login")
    logger.info(f"Navigated to {page.url}")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    logger.info("Filled credentials")

    page.locator("button[type='submit']").click()
    logger.info(f"After login: {page.url}")

    assert "/secure" in page.url
    logger.info("Login test PASSED")


# ============================================
# SCREENSHOT AT SPECIFIC POINTS
# ============================================

import os


def test_debug_with_screenshots(page: Page):
    """Take screenshots at key points for visual debugging."""
    os.makedirs("debug_screenshots", exist_ok=True)

    page.goto(f"{BASE_URL}/login")
    page.screenshot(path="debug_screenshots/step1_page_loaded.png")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.screenshot(path="debug_screenshots/step2_form_filled.png")

    page.locator("button[type='submit']").click()
    page.screenshot(path="debug_screenshots/step3_after_login.png")

    assert "/secure" in page.url
    print("\n  Screenshots saved to debug_screenshots/")


# ============================================
# EVALUATE JAVASCRIPT FOR DEBUGGING
# ============================================

def test_evaluate_js(page: Page):
    """Execute JavaScript for debugging information."""
    page.goto(f"{BASE_URL}/login")

    # Get page info via JavaScript
    title = page.evaluate("document.title")
    url = page.evaluate("window.location.href")
    cookie_count = page.evaluate("document.cookie.split(';').length")
    element_count = page.evaluate("document.querySelectorAll('*').length")

    print(f"\n  Title: {title}")
    print(f"  URL: {url}")
    print(f"  Cookies: {cookie_count}")
    print(f"  DOM elements: {element_count}")

    assert title == "The Internet"


# ============================================
# KEY POINTS:
#
# 1. page.on("console") - capture browser console
# 2. page.on("pageerror") - capture JS errors
# 3. page.on("request/response") - monitor network
# 4. Python logging module for structured logs
# 5. Screenshots at specific steps
# 6. page.evaluate() for JS debugging info
# 7. Create logging fixture for reuse
#
# Run: pytest 02_console_and_events.py -v --headed -s
# ============================================
