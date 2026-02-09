# Solutions - Lecture 35: Debugging Techniques

## Exercise 1: Debug and Fix Failing Tests

```python
"""Exercise 1 Solution: Fixed Tests"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


# BUG 1: Wrong selector (#pasword → #password)
def test_login_bug_selector(page: Page):
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")  # FIX: #password
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


# BUG 2: Need to wait for element (use expect or wait_for)
def test_dynamic_loading_bug_timing(page: Page):
    page.goto(f"{BASE_URL}/dynamic_loading/1")
    page.locator("#start button").click()
    # FIX: Wait for element to be visible first
    expect(page.locator("#finish h4")).to_be_visible(timeout=10000)
    assert page.locator("#finish h4").text_content() == "Hello World!"


# BUG 3: Multiple elements (use .first)
def test_checkboxes_bug_strict(page: Page):
    page.goto(f"{BASE_URL}/checkboxes")
    # FIX: Use .first to target specific checkbox
    page.locator("input[type='checkbox']").first.check()
    assert page.locator("input[type='checkbox']").first.is_checked()


# BUG 4: Wrong expected value (whitespace in actual text)
def test_dropdown_bug_expected(page: Page):
    page.goto(f"{BASE_URL}/dropdown")
    page.locator("#dropdown").select_option(value="1")
    selected = page.locator("#dropdown option:checked")
    # FIX: Use strip() or correct expected text
    assert selected.text_content().strip() == "Option 1"  # Note the space!


# BUG 5: Element is inside iframe
def test_iframe_bug_frame(page: Page):
    page.goto(f"{BASE_URL}/iframe")
    # FIX: Access via frame_locator
    frame = page.frame_locator("iframe#mce_0_ifr")
    editor = frame.locator("#tinymce")
    expect(editor).to_be_visible()


# BUG 6: Wrong assertion logic
def test_login_error_bug_logic(page: Page):
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill("wrong_user")
    page.locator("#password").fill("wrong_pass")
    page.locator("button[type='submit']").click()
    # FIX: Failed login stays on /login, not /secure
    assert "/login" in page.url
    assert "invalid" in page.locator("#flash").text_content().lower()
```

### Bug Summary:
| Bug | Problem | Fix |
|-----|---------|-----|
| 1 | Typo: `#pasword` | `#password` |
| 2 | No wait for dynamic content | `expect().to_be_visible()` |
| 3 | Locator matches 2 elements | `.first` |
| 4 | Missing space: `"Option1"` | `"Option 1"` with `.strip()` |
| 5 | Element in iframe | `frame_locator()` |
| 6 | Wrong URL assertion | `/login` not `/secure` |

---

## Exercise 2: Tracing and Logging

```python
"""Exercise 2 Solution: Debug Fixtures and Utilities"""
import os
import pytest
from playwright.sync_api import Page, BrowserContext


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# HOOK
# ============================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ============================================
# DEBUG FIXTURE
# ============================================

@pytest.fixture
def debug_page(context: BrowserContext, request):
    """Full debug fixture with tracing and logging."""
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()

    # Console logging
    page.on("console", lambda msg:
        print(f"  [console.{msg.type}] {msg.text}"))

    # JS error logging
    page.on("pageerror", lambda err:
        print(f"  [JS ERROR] {err}"))

    yield page

    # After test
    os.makedirs("debug_output", exist_ok=True)
    test_name = request.node.name

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # Save screenshot
        page.screenshot(
            path=f"debug_output/FAIL_{test_name}.png",
            full_page=True,
        )
        print(f"\n  Screenshot: debug_output/FAIL_{test_name}.png")

        # Save trace
        context.tracing.stop(path=f"debug_output/FAIL_{test_name}.zip")
        print(f"  Trace: debug_output/FAIL_{test_name}.zip")
    else:
        context.tracing.stop()  # Discard


# ============================================
# UTILITIES
# ============================================

def log_page_state(page: Page, label: str = ""):
    """Print current page state."""
    print(f"\n  === PAGE STATE {label} ===")
    print(f"  URL:     {page.url}")
    print(f"  Title:   {page.title()}")

    viewport = page.viewport_size
    if viewport:
        print(f"  Viewport: {viewport['width']}x{viewport['height']}")

    forms = page.locator("form").count()
    buttons = page.locator("button").count()
    inputs = page.locator("input").count()
    links = page.locator("a").count()
    print(f"  Forms: {forms}, Buttons: {buttons}, Inputs: {inputs}, Links: {links}")


def log_locator_info(page: Page, selector: str):
    """Print info about a locator."""
    locator = page.locator(selector)
    count = locator.count()
    print(f"\n  Selector: '{selector}'")
    print(f"  Matches: {count}")
    if count > 0:
        first = locator.first
        print(f"  Visible: {first.is_visible()}")
        print(f"  Enabled: {first.is_enabled()}")
        text = first.text_content() or ""
        print(f"  Text: '{text[:50]}'")
    else:
        print("  NOT FOUND!")


# ============================================
# TESTS
# ============================================

def test_login_with_debug(debug_page):
    """Login with full debug support."""
    debug_page.goto(f"{BASE_URL}/login")
    debug_page.locator("#username").fill("tomsmith")
    debug_page.locator("#password").fill("SuperSecretPassword!")
    debug_page.locator("button[type='submit']").click()
    assert "/secure" in debug_page.url


def test_checkboxes_with_logging(page: Page):
    """Logging at key points."""
    page.goto(f"{BASE_URL}/checkboxes")
    log_page_state(page, "AFTER LOAD")

    page.locator("input[type='checkbox']").first.check()
    log_page_state(page, "AFTER CHECK")

    assert page.locator("input[type='checkbox']").first.is_checked()


def test_find_element(page: Page):
    """Debug selectors with log_locator_info."""
    page.goto(f"{BASE_URL}/login")
    log_locator_info(page, "#username")
    log_locator_info(page, "#password")
    log_locator_info(page, "button")
    log_locator_info(page, "#nonexistent")
```

### Key Points:
- Debug fixture combines tracing + logging + screenshot on failure
- `log_page_state` gives quick overview of page
- `log_locator_info` helps debug selector issues
- Hook stores test result for fixture to check

---

## Debugging Quick Reference

```
VISUAL:
  pytest --headed --slowmo 1000    # See browser, slow
  PWDEBUG=1 pytest --headed        # Playwright Inspector
  page.pause()                     # Breakpoint

ARTIFACTS:
  pytest --screenshot only-on-failure --output results
  pytest --tracing retain-on-failure --output results
  playwright show-trace results/trace.zip

LOGGING:
  page.on("console", lambda m: print(m.text))
  page.on("pageerror", lambda e: print(e))
  pytest -s                        # Show print output

VS CODE:
  F5 with launch.json for pytest
  Set breakpoints on lines
  Watch variables in debug panel

COMMON FIXES:
  TimeoutError    → fix selector or wait_for()
  Strict mode     → .first / .nth(n)
  Detached        → re-query locator
  In iframe       → frame_locator()
  Timing          → expect() not assert
```
