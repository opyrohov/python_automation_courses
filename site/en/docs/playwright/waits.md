# Waits — Waiting Strategies

Correct handling of waits is one of the most important parts of stable automation. Playwright has a powerful auto-wait mechanism, but sometimes additional strategies are needed. In this section, we will cover all approaches to waiting.

## Auto-wait — Automatic Waiting

Playwright automatically waits for an element to become ready for interaction before performing an action. This significantly reduces the need for explicit waits.

```python
from playwright.sync_api import Page, expect

def test_auto_wait(page: Page):
    """Playwright automatically waits before performing actions."""
    page.goto("https://example.com")

    # Playwright will wait until the button becomes:
    # - attached to the DOM
    # - visible
    # - stable (not animating)
    # - able to receive events (not covered by another element)
    # - enabled
    page.get_by_role("button", name="Save").click()

    # Same for fill — waits until the field becomes available
    page.get_by_label("Name").fill("John")
```

::: tip Tip
In most cases, auto-wait is sufficient. Don't add unnecessary explicit waits — they slow down tests and may mask real issues.
:::

## wait_for_selector

```python
def test_wait_for_selector(page: Page):
    """Waiting for an element to appear or disappear."""
    page.goto("https://example.com")

    # Wait for element to appear in DOM
    page.wait_for_selector(".loading-complete")

    # Wait for element to become visible
    page.wait_for_selector("#results-table", state="visible")

    # Wait for element to disappear
    page.wait_for_selector(".spinner", state="hidden")

    # Wait for element to be removed from DOM
    page.wait_for_selector(".temp-notification", state="detached")

    # Wait with custom timeout
    page.wait_for_selector("#slow-content", state="visible", timeout=30000)
```

## wait_for_load_state

```python
def test_wait_for_load_state(page: Page):
    """Waiting for page load states."""
    page.goto("https://example.com")

    # Wait for initial DOM loading to complete
    page.wait_for_load_state("domcontentloaded")

    # Wait for full page load (all resources)
    page.wait_for_load_state("load")

    # Wait for network activity to finish
    # (no requests for 500ms)
    page.wait_for_load_state("networkidle")
```

::: warning Warning
`networkidle` can be unreliable on pages with constant requests (websockets, polling). Use it carefully and prefer waiting for specific elements.
:::

## wait_for_url

```python
import re

def test_wait_for_url(page: Page):
    """Waiting for URL change."""
    page.goto("https://example.com/login")

    # Perform authentication
    page.get_by_label("Email").fill("user@test.com")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign In").click()

    # Wait for specific URL
    page.wait_for_url("**/dashboard")

    # Wait for URL by regular expression
    page.wait_for_url(re.compile(r".*/dashboard\?.*"))

    # Wait with timeout
    page.wait_for_url("**/dashboard", timeout=15000)
```

## Locator Waiting

```python
def test_locator_wait_for(page: Page):
    """Using wait_for on locators."""
    page.goto("https://example.com")

    # Wait for element to appear via locator
    page.get_by_test_id("data-loaded").wait_for(state="visible")

    # Wait for loading indicator to disappear
    page.locator(".loading-overlay").wait_for(state="hidden")

    # Wait for element to appear in DOM (even if hidden)
    page.locator("#lazy-component").wait_for(state="attached")

    # Wait for element to be removed from DOM
    page.get_by_text("Temporary message").wait_for(state="detached")
```

## Waiting for Network Requests

```python
def test_wait_for_request_response(page: Page):
    """Waiting for specific network requests and responses."""
    page.goto("https://example.com")

    # Wait for API response
    with page.expect_response("**/api/products") as response_info:
        page.get_by_role("button", name="Load Products").click()
    response = response_info.value
    assert response.status == 200

    # Wait for response with condition
    with page.expect_response(
        lambda response: response.url.endswith("/api/search") and response.status == 200
    ) as response_info:
        page.get_by_label("Search").fill("Laptop")
        page.get_by_label("Search").press("Enter")
    data = response_info.value.json()
    assert len(data["results"]) > 0

    # Wait for request
    with page.expect_request("**/api/orders") as request_info:
        page.get_by_role("button", name="Place Order").click()
    request = request_info.value
    assert request.method == "POST"
```

## Waiting for Page Events

```python
def test_wait_for_events(page: Page):
    """Waiting for various page events."""
    page.goto("https://example.com")

    # Wait for new window (popup)
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Open in new window").click()
    popup = popup_info.value
    popup.wait_for_load_state()
    assert "New Page" in popup.title()

    # Wait for console message
    with page.expect_console_message() as msg_info:
        page.get_by_role("button", name="Execute").click()
    message = msg_info.value
    assert "Operation completed" in message.text

    # Wait for WebSocket connection
    with page.expect_websocket() as ws_info:
        page.get_by_role("button", name="Connect").click()
    ws = ws_info.value
    assert ws.url.endswith("/ws")
```

## Waiting with expect (retry assertions)

```python
def test_expect_with_retry(page: Page):
    """expect checks automatically retry until success."""
    page.goto("https://example.com/async-page")

    # expect automatically retries the check during timeout
    expect(page.get_by_test_id("status")).to_have_text("Completed")

    # Wait for text change
    page.get_by_role("button", name="Start Processing").click()
    expect(page.get_by_test_id("progress")).to_have_text("100%", timeout=30000)

    # Wait for element to appear
    expect(page.get_by_text("Results ready")).to_be_visible(timeout=15000)

    # Wait for element count change
    expect(page.get_by_role("listitem")).to_have_count(5, timeout=10000)

    # Wait for URL change
    expect(page).to_have_url(re.compile(r".*/results"))
```

::: info Information
`expect` is the recommended way to wait in tests. It both waits and verifies, reducing code and making tests more readable.
:::

## Custom Waits

```python
def test_custom_wait(page: Page):
    """Creating custom wait conditions."""
    page.goto("https://example.com")

    # Wait via evaluate (JavaScript in browser)
    page.wait_for_function("document.querySelectorAll('.item').length >= 10")

    # Wait with value condition
    page.wait_for_function(
        "() => document.querySelector('#counter').textContent === '100'"
    )

    # Wait with parameters
    page.wait_for_function(
        "selector => document.querySelector(selector).classList.contains('loaded')",
        arg="#main-content"
    )

    # Wait for animation to complete
    page.wait_for_function(
        "() => getComputedStyle(document.querySelector('.modal')).opacity === '1'"
    )
```

## Timeouts and Configuration

```python
from playwright.sync_api import sync_playwright

def configure_timeouts():
    """Configuring different timeout levels."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Default timeout for all actions (click, fill, etc.)
        page.set_default_timeout(15000)  # 15 seconds

        # Timeout for navigation (goto, reload)
        page.set_default_navigation_timeout(30000)  # 30 seconds

        # Global timeout for expect
        expect.set_options(timeout=10000)  # 10 seconds

        page.goto("https://example.com")
        browser.close()
```

## Practical Example: Testing Dynamic Content

```python
import re
from playwright.sync_api import Page, expect

def test_dynamic_content_loading(page: Page):
    """Testing a page with dynamic content loading."""
    page.goto("https://example.com/products")

    # Wait for skeleton loader to disappear
    page.locator(".skeleton-loader").wait_for(state="hidden")

    # Check products loaded
    expect(page.get_by_role("listitem")).to_have_count(12, timeout=10000)

    # Filter with API response waiting
    with page.expect_response("**/api/products?category=electronics") as resp:
        page.get_by_role("combobox", name="Category").select_option("electronics")
    assert resp.value.status == 200

    # Wait for list update
    expect(page.get_by_role("listitem")).to_have_count(5)

    # Infinite scroll — loading new items
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    with page.expect_response("**/api/products?page=2"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Check that new items appeared
    expect(page.get_by_role("listitem")).not_to_have_count(5)

    # Search with autocomplete
    page.get_by_placeholder("Search products...").press_sequentially("Lap", delay=200)
    expect(page.locator(".autocomplete-item")).to_have_count(3, timeout=5000)
    page.locator(".autocomplete-item").first.click()

    # Check product page loaded
    expect(page).to_have_url(re.compile(r".*/products/\d+"))
    expect(page.get_by_role("heading", level=1)).to_be_visible()
```

## Anti-patterns — What to Avoid

```python
import time

def test_bad_waits_example(page: Page):
    """BAD example — do NOT do this."""
    page.goto("https://example.com")

    # BAD: hard delay
    # time.sleep(5)  # Don't use!

    # BAD: excessively long timeout for simple operations
    # page.wait_for_selector("#button", timeout=60000)

    # GOOD: use auto-wait and expect
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Saved")).to_be_visible()
```

::: warning Warning
Never use `time.sleep()` in Playwright tests. It makes tests slow and unreliable. Use auto-wait, `expect`, or specific wait methods.
:::

## Useful Links

- [Official Auto-waiting Documentation](https://playwright.dev/python/docs/actionability)
- [Navigation and waiting](https://playwright.dev/python/docs/navigations)
- [Network events](https://playwright.dev/python/docs/network)
- [Waiting recommendations](https://playwright.dev/python/docs/best-practices)
