# Actions — Interacting with Elements

Playwright provides a wide range of methods for interacting with elements on a page — from simple clicks to complex drag-and-drop operations. In this section, we will cover the main actions and their practical application in QA automation.

## Clicks

### Basic Clicks

```python
from playwright.sync_api import Page

def test_click_actions(page: Page):
    """Various click options on elements."""
    page.goto("https://example.com")

    # Regular click
    page.get_by_role("button", name="Save").click()

    # Double click
    page.get_by_text("Edit Title").dblclick()

    # Right-click (context menu)
    page.get_by_role("row").first.click(button="right")

    # Click with key modifiers
    page.get_by_role("link", name="Document").click(modifiers=["Control"])  # Ctrl+Click

    # Click with delay (simulating long press)
    page.get_by_role("button", name="Menu").click(delay=1000)

    # Click at a specific position within the element
    page.locator(".canvas").click(position={"x": 100, "y": 200})

    # Force click (ignores visibility check)
    page.locator(".hidden-trigger").click(force=True)
```

### Hover (cursor hovering)

```python
def test_hover_actions(page: Page):
    """Hovering cursor over an element."""
    page.goto("https://example.com")

    # Hover to show submenu
    page.get_by_role("menuitem", name="Products").hover()
    page.get_by_role("menuitem", name="Laptops").click()

    # Hover to display tooltip
    page.get_by_role("button", name="Info").hover()
    tooltip = page.get_by_role("tooltip")
    assert tooltip.is_visible()
```

## Text Input

### fill and type

```python
def test_input_actions(page: Page):
    """Entering text into form fields."""
    page.goto("https://example.com/form")

    # fill — instantly fills the field (clears previous content)
    page.get_by_label("Name").fill("John Smith")

    # clear — clearing the field
    page.get_by_label("Name").clear()

    # press_sequentially — character-by-character input (simulates real typing)
    page.get_by_label("Search").press_sequentially("Playwright", delay=100)

    # Filling multiple form fields
    page.get_by_label("Email").fill("john@example.com")
    page.get_by_label("Password").fill("SecurePassword123!")
    page.get_by_label("Confirmation").fill("SecurePassword123!")
```

::: tip Tip
Use `fill()` for regular field filling. `press_sequentially()` is useful when you need to emulate character-by-character input, for example, for autocomplete fields.
:::

### Key Presses

```python
def test_keyboard_actions(page: Page):
    """Working with the keyboard."""
    page.goto("https://example.com")

    # Pressing individual keys
    page.get_by_label("Search").press("Enter")

    # Key combinations
    page.get_by_role("textbox").press("Control+a")    # Select all
    page.get_by_role("textbox").press("Control+c")    # Copy
    page.get_by_role("textbox").press("Control+v")    # Paste

    # Special keys
    page.get_by_label("Comment").press("Tab")          # Move to next field
    page.keyboard.press("Escape")                      # Close modal window

    # Entering text via keyboard (globally)
    page.keyboard.type("Hello, world!")
    page.keyboard.press("Shift+Enter")                 # New line
```

## Working with Dropdowns

```python
def test_select_actions(page: Page):
    """Interacting with select elements."""
    page.goto("https://example.com/form")

    # Select by value
    page.get_by_label("Country").select_option("UA")

    # Select by text
    page.get_by_label("City").select_option(label="Kyiv")

    # Select by index
    page.get_by_label("Month").select_option(index=5)

    # Multiple selection
    page.get_by_label("Skills").select_option(["python", "javascript", "sql"])
```

## Checkboxes and Radio Buttons

```python
from playwright.sync_api import expect

def test_checkbox_radio_actions(page: Page):
    """Interacting with checkboxes and radio buttons."""
    page.goto("https://example.com/settings")

    # Checkboxes
    page.get_by_role("checkbox", name="Receive notifications").check()
    page.get_by_role("checkbox", name="Dark theme").uncheck()

    # Checking checkbox state
    expect(page.get_by_role("checkbox", name="Receive notifications")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Dark theme")).not_to_be_checked()

    # Toggling state
    checkbox = page.get_by_role("checkbox", name="Developer mode")
    checkbox.set_checked(True)
    checkbox.set_checked(False)

    # Radio buttons
    page.get_by_role("radio", name="English").check()
    expect(page.get_by_role("radio", name="English")).to_be_checked()
```

## File Upload

```python
def test_file_upload(page: Page):
    """Uploading files to the page."""
    page.goto("https://example.com/upload")

    # Uploading a single file
    page.get_by_label("Choose file").set_input_files("tests/data/document.pdf")

    # Uploading multiple files
    page.get_by_label("Choose files").set_input_files([
        "tests/data/photo1.jpg",
        "tests/data/photo2.jpg",
    ])

    # Clearing file selection
    page.get_by_label("Choose file").set_input_files([])

    # Upload via file chooser dialog
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Upload").click()
    file_chooser = fc_info.value
    file_chooser.set_files("tests/data/report.xlsx")
```

## File Download

```python
def test_file_download(page: Page):
    """Downloading files from the page."""
    page.goto("https://example.com/reports")

    # Waiting for file download
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Report").click()
    download = download_info.value

    # Saving the file
    download.save_as("downloads/" + download.suggested_filename)

    # Checking the downloaded file
    assert download.suggested_filename == "report_2024.pdf"
    assert download.failure() is None  # Check for no errors
```

## Drag and Drop

```python
def test_drag_and_drop(page: Page):
    """Dragging elements."""
    page.goto("https://example.com/kanban")

    # Simple drag and drop
    page.locator("#task-1").drag_to(page.locator("#column-done"))

    # Drag and drop with manual control
    source = page.locator(".draggable-item").first
    target = page.locator(".drop-zone")

    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()
```

## Dialog Windows

```python
def test_dialog_handling(page: Page):
    """Handling dialog windows (alert, confirm, prompt)."""
    page.goto("https://example.com")

    # Handling alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Show alert").click()

    # Handling confirm — click "OK"
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm deletion").click()

    # Handling confirm — click "Cancel"
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm deletion").click()

    # Handling prompt — enter text
    page.on("dialog", lambda dialog: dialog.accept("New name"))
    page.get_by_role("button", name="Rename").click()
```

::: warning Warning
The dialog handler must be set **before** the action that triggers the dialog. Otherwise, Playwright will automatically close the dialog.
:::

## Navigation

```python
def test_navigation_actions(page: Page):
    """Page navigation."""
    # Navigate to URL
    page.goto("https://example.com")

    # Navigate with state waiting
    page.goto("https://example.com/dashboard", wait_until="networkidle")

    # Browser navigation buttons
    page.go_back()
    page.go_forward()

    # Page reload
    page.reload()

    # Wait for navigation after click
    with page.expect_navigation():
        page.get_by_role("link", name="Catalog").click()
```

## Practical Example: Checkout Flow

```python
from playwright.sync_api import Page, expect

def test_checkout_flow(page: Page):
    """Order checkout test in an online store."""
    page.goto("https://example-shop.com")

    # Product search
    page.get_by_placeholder("Search products...").fill("Headphones")
    page.get_by_placeholder("Search products...").press("Enter")

    # Product selection
    page.get_by_role("link", name="Wireless Headphones Pro").click()

    # Color selection
    page.get_by_role("radio", name="Black").check()

    # Quantity selection
    page.get_by_label("Quantity").select_option("2")

    # Add to cart
    page.get_by_role("button", name="Add to Cart").click()
    expect(page.get_by_text("Product added to cart")).to_be_visible()

    # Go to cart
    page.get_by_role("link", name="Cart").click()

    # Fill delivery form
    page.get_by_label("First Name").fill("John")
    page.get_by_label("Last Name").fill("Smith")
    page.get_by_label("Phone").fill("+380501234567")
    page.get_by_label("City").select_option(label="Kyiv")
    page.get_by_label("Post Office").fill("Office #25")

    # Payment method selection
    page.get_by_role("radio", name="Cash on delivery").check()

    # Order confirmation
    page.get_by_role("button", name="Place Order").click()

    # Verify successful order
    expect(page.get_by_role("heading", name="Order Placed")).to_be_visible()
    expect(page.get_by_text("Order Number")).to_be_visible()
```

## Useful Links

- [Official Actions Documentation](https://playwright.dev/python/docs/input)
- [Working with page events](https://playwright.dev/python/docs/events)
- [Working with files](https://playwright.dev/python/docs/downloads)
- [Navigation](https://playwright.dev/python/docs/navigations)
