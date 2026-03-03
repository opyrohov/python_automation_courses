"""Example 4: Screenshots and Traces on Failure

Demonstrates how to automatically capture screenshots, traces, and videos
when tests fail, making debugging much easier.

Run with: pytest 04_screenshots_and_traces.py -v --headed
"""
import pytest
import os
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# AUTOMATIC SCREENSHOT ON FAILURE
# ============================================

@pytest.fixture
def screenshot_on_failure(page: Page, request):
    """Take a screenshot when a test fails."""
    yield page

    # After test: check if it failed
    if request.node.rep_call and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        test_name = request.node.name
        path = f"screenshots/{test_name}.png"
        page.screenshot(path=path)
        print(f"\n  Screenshot saved: {path}")


# Hook to capture test result for the fixture above
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result so fixtures can access it."""
    import pluggy
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ============================================
# SIMPLER APPROACH: Screenshot in fixture teardown
# ============================================

@pytest.fixture
def auto_screenshot_page(page: Page, request):
    """Simpler screenshot approach - always captures on failure."""
    yield page

    # Check if test failed
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/FAIL_{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"\n  FAILURE screenshot: {screenshot_path}")


# ============================================
# TRACE RECORDING
# ============================================

@pytest.fixture
def traced_page(context: BrowserContext, request):
    """Record trace for failing tests.

    Traces contain:
    - Screenshots at each step
    - DOM snapshots
    - Network requests
    - Console logs
    """
    # Start tracing BEFORE test
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page = context.new_page()
    yield page

    # Stop tracing AFTER test
    os.makedirs("traces", exist_ok=True)
    trace_path = f"traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_path)
    print(f"\n  Trace saved: {trace_path}")
    print(f"  View with: playwright show-trace {trace_path}")


# ============================================
# VIDEO RECORDING
# ============================================

@pytest.fixture
def video_context(browser, request):
    """Record video for each test."""
    os.makedirs("videos", exist_ok=True)
    context = browser.new_context(
        record_video_dir="videos",
        record_video_size={"width": 1280, "height": 720},
    )

    page = context.new_page()
    yield page

    context.close()
    # Video is saved automatically when context closes
    video_path = page.video.path()
    print(f"\n  Video saved: {video_path}")


# ============================================
# TESTS
# ============================================

def test_passing_with_screenshot(page: Page):
    """This test passes - no screenshot needed."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("h2").text_content() == "Login Page"


def test_with_trace(traced_page):
    """Test with trace recording - useful for debugging."""
    traced_page.goto(f"{BASE_URL}/login")
    traced_page.locator("#username").fill("tomsmith")
    traced_page.locator("#password").fill("SuperSecretPassword!")
    traced_page.locator("button[type='submit']").click()
    assert "/secure" in traced_page.url


def test_screenshot_on_any_test(page: Page, request):
    """Manual screenshot capture in test."""
    page.goto(f"{BASE_URL}/login")

    # Take screenshot at a specific point
    os.makedirs("screenshots", exist_ok=True)
    page.screenshot(path=f"screenshots/manual_{request.node.name}.png")

    assert page.locator("h2").is_visible()


# ============================================
# BUILT-IN PYTEST-PLAYWRIGHT OPTIONS
# ============================================
#
# pytest-playwright has built-in screenshot/trace support:
#
# Screenshots:
#   pytest --screenshot on        # Screenshot for every test
#   pytest --screenshot off       # No screenshots (default)
#   pytest --screenshot only-on-failure  # Only on failure
#
# Traces:
#   pytest --tracing on           # Trace for every test
#   pytest --tracing off          # No traces (default)
#   pytest --tracing retain-on-failure  # Only on failure
#
# Videos:
#   pytest --video on             # Video for every test
#   pytest --video off            # No videos (default)
#   pytest --video retain-on-failure  # Only on failure
#
# Output directory:
#   pytest --output test-results  # Where to save artifacts
#
# Example:
#   pytest --screenshot only-on-failure --tracing retain-on-failure --output results
#


# ============================================
# FULL PAGE SCREENSHOT
# ============================================

def test_full_page_screenshot(page: Page):
    """Capture full page screenshot (including scrollable area)."""
    page.goto(BASE_URL)

    os.makedirs("screenshots", exist_ok=True)

    # Regular screenshot (viewport only)
    page.screenshot(path="screenshots/viewport_only.png")

    # Full page screenshot (entire page with scroll)
    page.screenshot(path="screenshots/full_page.png", full_page=True)

    assert page.title() == "The Internet"


# ============================================
# KEY POINTS:
#
# 1. --screenshot only-on-failure for auto screenshots
# 2. --tracing retain-on-failure for auto traces
# 3. --video retain-on-failure for auto video
# 4. Trace viewer: playwright show-trace trace.zip
# 5. Custom fixtures for more control
# 6. full_page=True for full page screenshots
# 7. --output to set artifact directory
#
# Run: pytest 04_screenshots_and_traces.py -v --headed
# Or:  pytest 04_screenshots_and_traces.py --screenshot on --output results
# ============================================
