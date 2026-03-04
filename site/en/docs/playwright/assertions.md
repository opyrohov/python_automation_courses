# Assertions — Checks and Expectations

Assertions are a key component of any test. Playwright provides the `expect` library with automatic retry (auto-retry), making tests stable and reliable. In this section, we will cover all types of assertions.

## expect Basics

Playwright assertions automatically retry the check during a given timeout (5 seconds by default), eliminating the need for explicit waits.

```python
from playwright.sync_api import Page, expect

def test_basic_assertions(page: Page):
    """Basic assertions with expect."""
    page.goto("https://example.com")

    # Check element visibility
    expect(page.get_by_role("heading", name="Home")).to_be_visible()

    # Negative check (element NOT visible)
    expect(page.get_by_text("Error")).not_to_be_visible()

    # Custom timeout for a specific check
    expect(page.get_by_text("Data loaded")).to_be_visible(timeout=15000)
```

::: tip Tip
Always use `expect` from Playwright instead of plain `assert`. Playwright assertions have a built-in retry mechanism, making tests more stable.
:::

## Visibility and State Checks

```python
def test_visibility_state_assertions(page: Page):
    """Visibility, accessibility, and element state checks."""
    page.goto("https://example.com/form")

    # Visibility
    expect(page.get_by_role("dialog")).to_be_visible()
    expect(page.get_by_role("dialog")).not_to_be_visible()

    # Hidden elements
    expect(page.locator(".loading-spinner")).to_be_hidden()

    # Element accessibility (enabled/disabled)
    expect(page.get_by_role("button", name="Save")).to_be_enabled()
    expect(page.get_by_role("button", name="Delete")).to_be_disabled()

    # Field editability
    expect(page.get_by_label("Name")).to_be_editable()
    expect(page.get_by_label("User ID")).not_to_be_editable()

    # Element presence in DOM (even if hidden)
    expect(page.locator("#hidden-data")).to_be_attached()

    # Focus on element
    page.get_by_label("Email").click()
    expect(page.get_by_label("Email")).to_be_focused()

    # Element emptiness
    expect(page.get_by_label("Notes")).to_be_empty()
```

## Text Checks

```python
import re

def test_text_assertions(page: Page):
    """Text content checks for elements."""
    page.goto("https://example.com/dashboard")

    # Exact text match
    expect(page.get_by_test_id("welcome-msg")).to_have_text("Welcome, John!")

    # Partial text match
    expect(page.get_by_test_id("welcome-msg")).to_contain_text("Welcome")

    # Check with regular expression
    expect(page.get_by_test_id("order-id")).to_have_text(re.compile(r"Order #\d{6}"))
    expect(page.get_by_test_id("price")).to_contain_text(re.compile(r"\d+\.\d{2} USD"))

    # Check text of a list of elements
    items = page.get_by_role("listitem")
    expect(items).to_have_text([
        "Home",
        "Products",
        "Contacts",
        "About Us",
    ])

    # Case-insensitive
    expect(page.get_by_test_id("status")).to_have_text(
        re.compile(r"active", re.IGNORECASE)
    )
```

## Attribute and CSS Checks

```python
def test_attribute_css_assertions(page: Page):
    """HTML attribute and CSS property checks."""
    page.goto("https://example.com")

    # Attribute check
    expect(page.get_by_role("link", name="Documentation")).to_have_attribute("href", "/docs")
    expect(page.get_by_role("img").first).to_have_attribute("alt", "Logo")

    # Attribute check with regular expression
    expect(page.get_by_role("link", name="API")).to_have_attribute(
        "href", re.compile(r"/api/v\d+")
    )

    # CSS class check
    expect(page.get_by_role("button", name="Active")).to_have_class(re.compile(r"active"))
    expect(page.locator(".nav-item").first).to_have_class("nav-item selected")

    # CSS property check
    expect(page.get_by_role("alert")).to_have_css("background-color", "rgb(255, 0, 0)")
    expect(page.locator(".modal")).to_have_css("display", "none")

    # ID check
    expect(page.get_by_role("main")).to_have_id("content")
```

## Form Value Checks

```python
def test_form_value_assertions(page: Page):
    """Form field value checks."""
    page.goto("https://example.com/profile")

    # Text field value check
    expect(page.get_by_label("Name")).to_have_value("John")

    # Check with regular expression
    expect(page.get_by_label("Phone")).to_have_value(re.compile(r"\+380\d{9}"))

    # Multiple selection values check
    expect(page.get_by_label("Skills")).to_have_values([
        re.compile(r"python"),
        re.compile(r"javascript"),
    ])

    # Checkbox state check
    expect(page.get_by_role("checkbox", name="Newsletter")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Promotional emails")).not_to_be_checked()
```

## Element Count Checks

```python
def test_count_assertions(page: Page):
    """Checks for the number of found elements."""
    page.goto("https://example.com/products")

    # Exact count
    expect(page.get_by_role("listitem")).to_have_count(10)

    # Check for element presence (greater than zero)
    items = page.get_by_role("listitem")
    count = items.count()
    assert count > 0, f"Expected more than 0 elements, got {count}"
```

## Page Assertions

```python
def test_page_assertions(page: Page):
    """Page-level checks."""
    page.goto("https://example.com/dashboard")

    # Page title check
    expect(page).to_have_title("Dashboard — Example")
    expect(page).to_have_title(re.compile(r"Dashboard"))

    # URL check
    expect(page).to_have_url("https://example.com/dashboard")
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    # After navigation
    page.get_by_role("link", name="Profile").click()
    expect(page).to_have_url(re.compile(r".*/profile"))
```

## API Response Assertions

```python
def test_api_response_assertions(page: Page):
    """API response checks."""
    page.goto("https://example.com")

    # Intercept and check API response
    with page.expect_response("**/api/users") as response_info:
        page.get_by_role("button", name="Load Users").click()
    response = response_info.value

    # Status code check
    assert response.status == 200

    # Response body check
    data = response.json()
    assert len(data["users"]) > 0
    assert data["users"][0]["name"] is not None

    # Response headers check
    assert response.headers["content-type"] == "application/json"
```

## Soft Assertions

```python
def test_soft_assertions(page: Page):
    """Soft assertions — continue execution after failure."""
    page.goto("https://example.com/profile")

    # All checks will execute, even if some fail
    expect(page.get_by_label("Name"), "Name check").to_have_value("John")
    expect(page.get_by_label("Email"), "Email check").to_have_value("john@example.com")
    expect(page.get_by_label("City"), "City check").to_have_value("Kyiv")
    expect(page.get_by_role("heading"), "Profile heading").to_have_text("My Profile")
```

::: info Information
The second parameter of `expect` is a message that will be displayed in case of a failed check. This helps quickly understand the cause of the error.
:::

## Timeout Configuration

```python
def test_custom_timeouts(page: Page):
    """Configuring timeouts for assertions."""
    page.goto("https://example.com")

    # Specific timeout for a single check
    expect(page.get_by_text("Data processed")).to_be_visible(timeout=30000)

    # Global timeout setting in conftest.py
    # expect.set_options(timeout=10000)
```

::: warning Warning
Do not use excessively large timeouts without need. If an element takes 30 seconds to appear, there might be a performance issue with the application.
:::

## Practical Example: User Dashboard Testing

```python
import re
from playwright.sync_api import Page, expect

def test_user_dashboard(page: Page):
    """Comprehensive user dashboard check."""
    page.goto("https://example.com/login")

    # Authentication
    page.get_by_label("Email").fill("admin@example.com")
    page.get_by_label("Password").fill("admin123")
    page.get_by_role("button", name="Sign In").click()

    # URL check after authentication
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    # Page title check
    expect(page).to_have_title(re.compile(r"Dashboard"))

    # Welcome message check
    expect(page.get_by_test_id("greeting")).to_contain_text("Welcome, Administrator")

    # Navigation menu check
    nav_items = page.locator("nav").get_by_role("link")
    expect(nav_items).to_have_count(5)

    # Statistics check
    expect(page.get_by_test_id("active-users")).to_have_text(re.compile(r"\d+"))
    expect(page.get_by_test_id("total-orders")).to_contain_text("orders")

    # Recent orders table check
    rows = page.get_by_role("table").get_by_role("row")
    expect(rows).to_have_count(11)  # 10 rows + header

    # Button state check
    expect(page.get_by_role("button", name="Export")).to_be_enabled()
    expect(page.get_by_role("button", name="Delete All")).to_be_disabled()

    # Profile icon check
    expect(page.get_by_alt_text("Avatar")).to_be_visible()
    expect(page.get_by_alt_text("Avatar")).to_have_attribute("src", re.compile(r"/avatars/"))
```

## Useful Links

- [Official Assertions Documentation](https://playwright.dev/python/docs/test-assertions)
- [All assertions list](https://playwright.dev/python/docs/api/class-locatorassertions)
- [Page assertions](https://playwright.dev/python/docs/api/class-pageassertions)
- [API Response assertions](https://playwright.dev/python/docs/api/class-apiresponseassertions)
