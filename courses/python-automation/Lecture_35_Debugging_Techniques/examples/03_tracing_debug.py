"""Example 3: Tracing for Debugging

Demonstrates how to record Playwright traces for post-mortem debugging.
Traces capture screenshots, DOM snapshots, network, and console for each action.

Run with: pytest 03_tracing_debug.py -v --headed -s
Or:       pytest 03_tracing_debug.py --tracing on --output trace-results
"""
import os
import pytest
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# MANUAL TRACING IN FIXTURE
# ============================================

@pytest.fixture
def traced_page(context: BrowserContext, request):
    """Record trace for every test using this fixture."""
    # Start tracing before test
    context.tracing.start(
        screenshots=True,   # Screenshot at each action
        snapshots=True,      # DOM snapshot at each action
        sources=True,        # Source code in trace
    )

    page = context.new_page()
    yield page

    # Save trace after test
    os.makedirs("traces", exist_ok=True)
    trace_path = f"traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_path)
    print(f"\n  Trace saved: {trace_path}")
    print(f"  View: playwright show-trace {trace_path}")


# ============================================
# TESTS WITH TRACING
# ============================================

def test_login_traced(traced_page):
    """Login test with full trace recording."""
    traced_page.goto(f"{BASE_URL}/login")
    traced_page.locator("#username").fill("tomsmith")
    traced_page.locator("#password").fill("SuperSecretPassword!")
    traced_page.locator("button[type='submit']").click()
    assert "/secure" in traced_page.url


def test_checkboxes_traced(traced_page):
    """Checkbox test with trace."""
    traced_page.goto(f"{BASE_URL}/checkboxes")
    first = traced_page.locator("input[type='checkbox']").first
    first.check()
    assert first.is_checked()


# ============================================
# TRACE ON FAILURE ONLY
# ============================================

@pytest.fixture
def trace_on_failure(context: BrowserContext, request):
    """Only save trace when test fails."""
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    yield page

    # Check test result
    os.makedirs("traces", exist_ok=True)
    trace_path = f"traces/{request.node.name}.zip"

    if request.node.rep_call and request.node.rep_call.failed:
        context.tracing.stop(path=trace_path)
        print(f"\n  FAILURE trace saved: {trace_path}")
    else:
        context.tracing.stop()  # Discard trace


# Hook to store test result
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ============================================
# BUILT-IN CLI FLAGS (easiest approach!)
# ============================================
#
# pytest-playwright has built-in tracing support:
#
# Record ALL traces:
#   pytest --tracing on --output test-results
#
# Only on failure:
#   pytest --tracing retain-on-failure --output test-results
#
# View trace:
#   playwright show-trace test-results/test-name/trace.zip
#
# Combined with screenshots and video:
#   pytest --tracing retain-on-failure \
#          --screenshot only-on-failure \
#          --video retain-on-failure \
#          --output test-results


def test_for_cli_tracing(page: Page):
    """Run with --tracing on to capture trace without code changes."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


# ============================================
# WHAT THE TRACE VIEWER SHOWS
# ============================================
#
# When you open trace with: playwright show-trace trace.zip
#
# 1. TIMELINE
#    - Visual timeline of all actions
#    - Click any action to see its state
#
# 2. SCREENSHOT
#    - Before and after each action
#    - See exactly what happened
#
# 3. DOM SNAPSHOT
#    - Full DOM at each step
#    - Inspect elements like DevTools
#
# 4. NETWORK
#    - All requests and responses
#    - Headers, body, timing
#
# 5. CONSOLE
#    - Browser console messages
#    - JavaScript errors
#
# 6. SOURCE
#    - Your test source code
#    - Highlighted current line


# ============================================
# TRACE WITH SPECIFIC ACTIONS
# ============================================

def test_trace_chunk(context: BrowserContext):
    """Trace only a specific part of the test."""
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")

    # Start tracing for the critical section
    context.tracing.start(screenshots=True, snapshots=True)

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # Stop and save trace
    os.makedirs("traces", exist_ok=True)
    context.tracing.stop(path="traces/login_only.zip")

    assert "/secure" in page.url
    print("\n  Partial trace saved: traces/login_only.zip")


# ============================================
# KEY POINTS:
#
# 1. context.tracing.start() / .stop(path=)
# 2. --tracing retain-on-failure (easiest!)
# 3. playwright show-trace trace.zip
# 4. Trace contains: screenshots, DOM, network, console
# 5. Can trace specific sections only
# 6. Combine with --screenshot and --video
# 7. Great for debugging flaky tests in CI
#
# Run: pytest 03_tracing_debug.py -v --headed -s
# Or:  pytest 03_tracing_debug.py --tracing on --output results
# ============================================
