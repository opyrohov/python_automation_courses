# Playwright Cheatsheet

Quick reference for Playwright for Python.

## Installation

```bash
pip install playwright
playwright install
```

## Basic Structure

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    # ... tests
    browser.close()
```

## Locators (recommended)

```python
# By role (best option)
page.get_by_role("button", name="Submit")
page.get_by_role("link", name="Home")
page.get_by_role("textbox", name="Email")
page.get_by_role("checkbox", name="Agree")

# By text
page.get_by_text("Welcome")
page.get_by_text("Welcome", exact=True)

# By label
page.get_by_label("Email")

# By placeholder
page.get_by_placeholder("Enter email")

# By test-id (most stable)
page.get_by_test_id("submit-btn")

# By alt text (for images)
page.get_by_alt_text("Logo")

# By title
page.get_by_title("Close")
```

## Locators (CSS/XPath)

```python
# CSS selectors
page.locator("button.submit")
page.locator("#login-form input[type='email']")
page.locator("div.card >> text=Buy Now")

# XPath
page.locator("//button[@type='submit']")
page.locator("xpath=//div[@class='container']//a")
```

## Actions

```python
# Click
page.get_by_role("button").click()
page.get_by_role("button").dblclick()
page.get_by_role("button").click(button="right")

# Text input
page.get_by_label("Email").fill("user@test.com")
page.get_by_label("Email").type("user@test.com")  # character by character
page.get_by_label("Email").clear()

# Checkbox / Radio
page.get_by_role("checkbox").check()
page.get_by_role("checkbox").uncheck()
page.get_by_role("checkbox").set_checked(True)

# Select
page.get_by_role("combobox").select_option("value")
page.get_by_role("combobox").select_option(label="Option 1")
page.get_by_role("combobox").select_option(index=2)

# Hover
page.get_by_text("Menu").hover()

# Drag and drop
page.locator("#source").drag_to(page.locator("#target"))

# Upload
page.get_by_label("Upload").set_input_files("file.pdf")
page.get_by_label("Upload").set_input_files(["file1.pdf", "file2.pdf"])
```

## Assertions

```python
from playwright.sync_api import expect

# Visibility
expect(page.get_by_text("Welcome")).to_be_visible()
expect(page.get_by_text("Error")).not_to_be_visible()

# Text
expect(page.locator("h1")).to_have_text("Title")
expect(page.locator("h1")).to_contain_text("Title")

# Attributes
expect(page.locator("input")).to_have_attribute("type", "email")
expect(page.locator("input")).to_have_value("test@example.com")

# State
expect(page.get_by_role("button")).to_be_enabled()
expect(page.get_by_role("button")).to_be_disabled()
expect(page.get_by_role("checkbox")).to_be_checked()

# Count
expect(page.locator(".item")).to_have_count(5)

# URL and Title
expect(page).to_have_url("https://example.com/dashboard")
expect(page).to_have_title("Dashboard")
```

## Waits

```python
# Wait for element
page.get_by_role("button").wait_for()
page.get_by_role("button").wait_for(state="visible")
page.get_by_role("button").wait_for(state="hidden")

# Wait for navigation
page.wait_for_url("**/dashboard")

# Wait for load
page.wait_for_load_state("networkidle")
page.wait_for_load_state("domcontentloaded")

# Timeout
page.get_by_role("button").click(timeout=5000)
```

## Screenshots & Video

```python
# Screenshot
page.screenshot(path="screenshot.png")
page.screenshot(path="full.png", full_page=True)
page.locator(".card").screenshot(path="element.png")

# Video (in launch)
browser = p.chromium.launch()
context = browser.new_context(record_video_dir="videos/")
page = context.new_page()
# ... actions
context.close()  # video is saved on close
```

## Multiple Elements

```python
# All elements
cards = page.locator(".card")
count = cards.count()

# Iteration
for i in range(cards.count()):
    print(cards.nth(i).text_content())

# First / Last
cards.first.click()
cards.last.click()

# Filter
page.locator(".card").filter(has_text="Buy").click()
page.locator(".card").filter(has=page.get_by_role("button")).click()
```

## API Testing

```python
# GET
response = page.request.get("https://api.example.com/users")
assert response.ok
data = response.json()

# POST
response = page.request.post(
    "https://api.example.com/users",
    data={"name": "John", "email": "john@test.com"}
)

# With headers
response = page.request.get(
    "https://api.example.com/users",
    headers={"Authorization": "Bearer token123"}
)
```

## Network Interception

```python
# Mock response
page.route("**/api/users", lambda route: route.fulfill(
    status=200,
    body='[{"id": 1, "name": "Mock User"}]'
))

# Block requests
page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

# Modify
def handle_route(route):
    response = route.fetch()
    route.fulfill(
        response=response,
        headers={**response.headers, "X-Custom": "value"}
    )
page.route("**/api/*", handle_route)
```

## Page Object Model

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Sign In")

    def goto(self):
        self.page.goto("/login")

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
```
