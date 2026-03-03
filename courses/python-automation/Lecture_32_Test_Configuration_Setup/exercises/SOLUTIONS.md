# Solutions - Lecture 32: Test Configuration & Setup

## Exercise 1: Complete Project Configuration

### pytest.ini
```ini
[pytest]
addopts = -v --tb=short
base_url = https://the-internet.herokuapp.com
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
```

### conftest.py + Tests
```python
"""Exercise 1 Solution: Project Configuration"""
import pytest
from playwright.sync_api import Page


# ============================================
# CONFIGURATION FIXTURES
# ============================================

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch options."""
    return {
        "headless": False,
        "slow_mo": 300,
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context options."""
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def base_url():
    """Base URL for all tests."""
    return "https://the-internet.herokuapp.com"


@pytest.fixture(autouse=True)
def setup_timeouts(page):
    """Set default timeouts for all tests."""
    page.set_default_timeout(10000)           # 10s for actions
    page.set_default_navigation_timeout(15000)  # 15s for navigation
    yield page


# ============================================
# PAGE FIXTURES
# ============================================

@pytest.fixture
def login_page(page, base_url):
    """Navigate to login page."""
    page.goto(f"{base_url}/login")
    return page


@pytest.fixture
def logged_in_page(page, base_url):
    """Login and return authenticated page."""
    page.goto(f"{base_url}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/secure")
    return page


# ============================================
# TESTS
# ============================================

@pytest.mark.smoke
def test_homepage_loads(page, base_url):
    """Verify homepage loads."""
    page.goto(base_url)
    assert page.title() == "The Internet"


@pytest.mark.smoke
def test_login_page_elements(login_page):
    """Verify login page elements are present."""
    assert login_page.locator("#username").is_visible()
    assert login_page.locator("#password").is_visible()
    assert login_page.locator("button[type='submit']").is_visible()


@pytest.mark.regression
def test_secure_area(logged_in_page):
    """Verify access after login."""
    assert "/secure" in logged_in_page.url
    heading = logged_in_page.locator("h2")
    assert heading.text_content().strip() == "Secure Area"


def test_viewport_configured(page, base_url):
    """Verify viewport is 1280x720."""
    page.goto(base_url)
    viewport = page.viewport_size
    assert viewport["width"] == 1280
    assert viewport["height"] == 720
```

### Key Points:
- `scope="session"` for browser/context config (runs once)
- `autouse=True` for timeout setup (every test)
- `base_url` fixture avoids URL repetition
- Fixtures build on each other: `page` → `login_page` → `logged_in_page`

---

## Exercise 2: Screenshots and Traces on Failure

```python
"""Exercise 2 Solution: Failure Handling"""
import pytest
import os
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# HOOK FOR TEST RESULT
# ============================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result so fixtures can access it."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ============================================
# SCREENSHOT FIXTURE
# ============================================

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    """Auto-capture screenshot when test fails."""
    yield page

    # After test: check if it failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/FAIL_{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"\n  Screenshot saved: {screenshot_path}")


# ============================================
# TRACE FIXTURE
# ============================================

@pytest.fixture
def traced_page(context, request):
    """Record trace for the test."""
    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    page = context.new_page()
    yield page

    # Stop tracing and save
    os.makedirs("traces", exist_ok=True)
    trace_path = f"traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_path)
    print(f"\n  Trace saved: {trace_path}")
    print(f"  View with: playwright show-trace {trace_path}")


# ============================================
# TESTS
# ============================================

def test_passing_test(page):
    """This passes - no screenshot captured."""
    page.goto(f"{BASE_URL}/login")
    assert page.locator("h2").text_content() == "Login Page"


def test_failing_assertion(page):
    """This FAILS intentionally - screenshot captured!"""
    page.goto(f"{BASE_URL}/login")
    # Intentional failure to demonstrate screenshot
    assert page.locator("h2").text_content() == "Wrong Title"


def test_with_trace(traced_page):
    """Test with trace recording."""
    traced_page.goto(f"{BASE_URL}/login")
    traced_page.locator("#username").fill("tomsmith")
    traced_page.locator("#password").fill("SuperSecretPassword!")
    traced_page.locator("button[type='submit']").click()
    assert "/secure" in traced_page.url


def test_manual_screenshot(page):
    """Manual screenshot at specific steps."""
    page.goto(f"{BASE_URL}/login")

    os.makedirs("screenshots", exist_ok=True)

    # Before login
    page.screenshot(path="screenshots/before_login.png")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    # After login
    page.screenshot(path="screenshots/after_login.png")
    assert "/secure" in page.url
```

### Key Points:
- `pytest_runtest_makereport` hook stores test outcome
- `request.node.rep_call.failed` checks if test failed
- `autouse=True` applies screenshot fixture to ALL tests
- Trace fixture creates page from context (to control tracing)
- `full_page=True` captures entire scrollable page
- `playwright show-trace trace.zip` opens the trace viewer

---

## Summary: Configuration Patterns

### Minimal Setup (recommended start)
```ini
# pytest.ini
[pytest]
addopts = -v
base_url = https://your-site.com
```

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args():
    return {"viewport": {"width": 1280, "height": 720}}
```

### Full Setup (production project)
```ini
# pytest.ini
[pytest]
addopts = -v --tb=short --strict-markers
testpaths = tests
base_url = https://your-site.com
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
```

```python
# conftest.py
import pytest
import os


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": True, "slow_mo": 0}


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }


@pytest.fixture(autouse=True)
def setup_timeouts(page):
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    yield page


# Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path=f"screenshots/FAIL_{request.node.name}.png")
```

### Running Tests
```bash
# Development
pytest --headed --slowmo 500

# CI/CD
pytest --screenshot only-on-failure --tracing retain-on-failure --output results

# Cross-browser
pytest --browser chromium --browser firefox --browser webkit
```

---

## Common Mistakes to Avoid

### Mistake 1: Both config files
```
# WRONG - don't use both!
pytest.ini     ← uses this one
pyproject.toml ← ignored!
```

### Mistake 2: Wrong fixture scope for browser config
```python
# WRONG - runs for each test (slow!)
@pytest.fixture(scope="function")
def browser_type_launch_args():
    return {"headless": False}

# CORRECT - runs once for all tests
@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": False}
```

### Mistake 3: Forgetting yield in autouse fixtures
```python
# WRONG - teardown never runs
@pytest.fixture(autouse=True)
def setup(page):
    page.set_default_timeout(10000)
    return page  # No teardown!

# CORRECT - yield enables teardown
@pytest.fixture(autouse=True)
def setup(page):
    page.set_default_timeout(10000)
    yield page
    # Teardown code here
```
