"""Example 5: Reporting & Monitoring

Demonstrates test reporting tools, result tracking,
and monitoring strategies for test suites.

Run with:
    pytest 05_reporting_monitoring.py -v -s
"""
import pytest
import json
import time
from pathlib import Path
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# PYTEST-HTML REPORTS
# ============================================
#
# Install: pip install pytest-html
#
# Generate HTML report:
#   pytest --html=reports/report.html --self-contained-html
#
# Customize report in conftest.py:
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # Add screenshot to report on failure
#         if report.failed:
#             page = item.funcargs.get("page")
#             if page:
#                 screenshot = page.screenshot()
#                 import base64
#                 encoded = base64.b64encode(screenshot).decode()
#                 extras.append(pytest_html.extras.image(encoded, mime_type="image/png"))
#         report.extras = extras


# ============================================
# ALLURE REPORTS
# ============================================
#
# Install: pip install allure-pytest
#
# Generate Allure results:
#   pytest --alluredir=allure-results
#
# View report:
#   allure serve allure-results
#
# Use Allure decorators:

# @allure.feature("Login")
# @allure.story("Valid Login")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login_allure(page):
#     with allure.step("Navigate to login page"):
#         page.goto(f"{BASE_URL}/login")
#     with allure.step("Fill credentials"):
#         page.locator("#username").fill("tomsmith")
#         page.locator("#password").fill("SuperSecretPassword!")
#     with allure.step("Submit form"):
#         page.locator("button[type='submit']").click()
#     with allure.step("Verify redirect"):
#         assert "/secure" in page.url


# ============================================
# CUSTOM TEST RESULT TRACKER
# ============================================

class TestResultTracker:
    """Simple result tracker that saves to JSON."""

    def __init__(self, output_dir: str = "test-results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.results = []

    def record(self, test_name: str, status: str, duration: float, error: str = None):
        """Record a test result."""
        self.results.append({
            "test": test_name,
            "status": status,
            "duration_seconds": round(duration, 2),
            "error": error,
        })

    def save(self, filename: str = "results.json"):
        """Save results to JSON file."""
        output_path = self.output_dir / filename
        with open(output_path, "w") as f:
            json.dump({
                "total": len(self.results),
                "passed": sum(1 for r in self.results if r["status"] == "passed"),
                "failed": sum(1 for r in self.results if r["status"] == "failed"),
                "results": self.results,
            }, f, indent=2)
        return output_path

    def summary(self) -> str:
        """Return summary string."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "passed")
        failed = total - passed
        return f"Total: {total}, Passed: {passed}, Failed: {failed}"


# ============================================
# PERFORMANCE MONITORING
# ============================================

@pytest.fixture
def timed_page(page: Page, request):
    """Fixture that measures page load and test duration."""
    start = time.time()

    yield page

    duration = time.time() - start
    test_name = request.node.name
    print(f"\n  [TIMING] {test_name}: {duration:.2f}s")

    # Warn if test takes too long
    if duration > 10:
        print(f"  [WARNING] {test_name} took over 10 seconds!")


def test_login_performance(timed_page: Page):
    """Test with automatic timing."""
    timed_page.goto(f"{BASE_URL}/login")
    timed_page.locator("#username").fill("tomsmith")
    timed_page.locator("#password").fill("SuperSecretPassword!")
    timed_page.locator("button[type='submit']").click()
    assert "/secure" in timed_page.url


def test_checkboxes_performance(timed_page: Page):
    """Another timed test."""
    timed_page.goto(f"{BASE_URL}/checkboxes")
    checkbox = timed_page.locator("input[type='checkbox']").first
    checkbox.check()
    assert checkbox.is_checked()


# ============================================
# PAGE LOAD METRICS
# ============================================

def test_page_load_metrics(page: Page):
    """Measure actual page load performance metrics."""
    page.goto(f"{BASE_URL}/login")

    # Get performance timing from browser
    metrics = page.evaluate("""() => {
        const perf = performance.timing;
        return {
            dns: perf.domainLookupEnd - perf.domainLookupStart,
            connection: perf.connectEnd - perf.connectStart,
            response: perf.responseEnd - perf.requestStart,
            dom_ready: perf.domContentLoadedEventEnd - perf.navigationStart,
            full_load: perf.loadEventEnd - perf.navigationStart,
        };
    }""")

    print(f"\n  Page Load Metrics:")
    print(f"    DNS lookup:   {metrics['dns']}ms")
    print(f"    Connection:   {metrics['connection']}ms")
    print(f"    Response:     {metrics['response']}ms")
    print(f"    DOM ready:    {metrics['dom_ready']}ms")
    print(f"    Full load:    {metrics['full_load']}ms")

    # Assert reasonable load time
    assert metrics["full_load"] < 10000, "Page took over 10s to load!"


# ============================================
# FLAKY TEST DETECTION
# ============================================
#
# Strategy 1: Run tests multiple times
#   pytest --count=5 test_file.py  (needs pytest-repeat)
#
# Strategy 2: Track results over time
#   - Save test results to JSON after each run
#   - Compare results across runs
#   - Tests that alternate pass/fail are flaky
#
# Strategy 3: Use pytest-rerunfailures
#   pytest --reruns 3
#   Tests that pass on retry were flaky


def test_consistent_result(page: Page):
    """A test that should always pass (not flaky)."""
    page.goto(f"{BASE_URL}/login")
    heading = page.locator("h2")
    assert heading.text_content() == "Login Page"


# ============================================
# JUNIT XML REPORTS (for CI tools)
# ============================================
#
# Generate JUnit XML:
#   pytest --junitxml=reports/junit.xml
#
# Most CI tools (Jenkins, GitHub Actions, GitLab CI)
# can parse JUnit XML for test result visualization.


# ============================================
# KEY POINTS:
#
# 1. pytest-html for HTML reports
# 2. Allure for rich interactive reports
# 3. JUnit XML for CI tool integration
# 4. Custom trackers for project-specific needs
# 5. Performance monitoring with timing fixtures
# 6. Page load metrics via browser performance API
# 7. Track flaky tests with repeated runs
#
# Run: pytest 05_reporting_monitoring.py -v -s
# ============================================
