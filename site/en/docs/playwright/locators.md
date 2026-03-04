# Locators — Element Finding Strategies

Locators in Playwright are the primary way to find elements on a page. Playwright offers several finding strategies, from recommended semantic locators to classic CSS and XPath selectors.

## Recommended Locators

Playwright recommends using semantic locators based on element roles and text. They are the most resistant to layout changes.

### get_by_role

```python
from playwright.sync_api import Page, expect

def test_role_locators(page: Page):
    """Finding elements by their ARIA role."""
    page.goto("https://example.com")

    # Buttons
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Delete", exact=True).click()

    # Links
    page.get_by_role("link", name="Home").click()

    # Headings
    heading = page.get_by_role("heading", name="Welcome", level=1)
    expect(heading).to_be_visible()

    # Input fields
    page.get_by_role("textbox", name="Search").fill("Playwright")

    # Checkboxes and radio buttons
    page.get_by_role("checkbox", name="I agree").check()
    page.get_by_role("radio", name="Option A").check()

    # Dropdown list
    page.get_by_role("combobox", name="Country").select_option("Ukraine")

    # Table rows
    row = page.get_by_role("row", name="John Smith")
    expect(row).to_be_visible()
```

::: tip Tip
`get_by_role` is the best choice for most situations. It is based on accessibility and works the way a user sees the page.
:::

### get_by_text

```python
def test_text_locators(page: Page):
    """Finding elements by text content."""
    page.goto("https://example.com")

    # Search by partial text
    page.get_by_text("Welcome").click()

    # Exact text match
    page.get_by_text("Sign In", exact=True).click()

    # Search by regular expression
    page.get_by_text(re.compile(r"Order #\d+")).click()
```

### get_by_label

```python
def test_label_locators(page: Page):
    """Finding form fields by their labels."""
    page.goto("https://example.com/register")

    # Filling registration form through labels
    page.get_by_label("First Name").fill("John")
    page.get_by_label("Last Name").fill("Smith")
    page.get_by_label("Email").fill("john@example.com")
    page.get_by_label("Password").fill("SecurePass123!")
    page.get_by_label("Confirm Password").fill("SecurePass123!")
```

### get_by_placeholder

```python
def test_placeholder_locators(page: Page):
    """Finding fields by placeholder text."""
    page.goto("https://example.com")

    page.get_by_placeholder("Enter your email").fill("user@test.com")
    page.get_by_placeholder("Search products...").fill("Laptop")
```

### get_by_alt_text

```python
def test_alt_text_locators(page: Page):
    """Finding images by alternative text."""
    page.goto("https://example.com")

    # Finding image by alt text
    logo = page.get_by_alt_text("Company Logo")
    expect(logo).to_be_visible()

    page.get_by_alt_text("Profile Photo").click()
```

### get_by_title

```python
def test_title_locators(page: Page):
    """Finding elements by title attribute."""
    page.goto("https://example.com")

    page.get_by_title("Profile Settings").click()
    page.get_by_title("Close Window").click()
```

### get_by_test_id

```python
def test_testid_locators(page: Page):
    """Finding elements by data-testid attribute."""
    page.goto("https://example.com")

    # By default looks for data-testid attribute
    page.get_by_test_id("submit-button").click()
    page.get_by_test_id("user-menu").click()
    page.get_by_test_id("cart-counter").text_content()
```

::: info Information
The attribute for `get_by_test_id` can be changed in configuration:
```python
playwright.selectors.set_test_id_attribute("data-qa")
```
:::

## CSS and XPath Selectors

```python
def test_css_xpath_locators(page: Page):
    """Classic CSS and XPath selectors."""
    page.goto("https://example.com")

    # CSS selectors
    page.locator("css=#login-form").is_visible()
    page.locator(".btn-primary").click()
    page.locator("input[type='email']").fill("user@test.com")
    page.locator("div.card >> span.price").text_content()
    page.locator("[data-qa='submit']").click()

    # XPath selectors
    page.locator("xpath=//button[contains(text(), 'Save')]").click()
    page.locator("xpath=//div[@class='menu']//a[@href='/profile']").click()
    page.locator("xpath=//table//tr[td[text()='Active']]").count()
```

::: warning Warning
CSS and XPath selectors are more fragile — they depend on HTML structure. Prefer semantic locators (`get_by_role`, `get_by_text`, etc.).
:::

## Locator Filtering

```python
def test_locator_filtering(page: Page):
    """Narrowing search using filters."""
    page.goto("https://example.com/products")

    # Filter by text
    page.get_by_role("listitem").filter(has_text="Laptop").click()

    # Filter by nested locator
    page.get_by_role("listitem").filter(
        has=page.get_by_role("button", name="Buy")
    ).first.click()

    # Filter by absence of text
    page.get_by_role("listitem").filter(has_not_text="Sold Out").count()

    # Chaining filters
    products = (
        page.get_by_role("listitem")
        .filter(has_text="Laptop")
        .filter(has=page.locator(".in-stock"))
    )
    expect(products).to_have_count(3)
```

## Combining and Chaining Locators

```python
def test_chaining_locators(page: Page):
    """Building complex locators through chaining."""
    page.goto("https://example.com")

    # Search inside a container
    sidebar = page.locator(".sidebar")
    sidebar.get_by_role("link", name="Profile").click()

    # Locator chaining
    page.locator(".product-card").locator(".price").first.text_content()

    # nth — select by index
    page.get_by_role("listitem").nth(2).click()

    # first / last
    page.get_by_role("button", name="Delete").first.click()
    page.get_by_role("link").last.click()

    # or_ — combining locators
    save_btn = page.get_by_role("button", name="Save").or_(
        page.get_by_role("button", name="Save")
    )
    save_btn.click()

    # and_ — intersecting locators
    active_btn = page.get_by_role("button").and_(page.locator(".active"))
    active_btn.click()
```

## Working with Frame and iFrame

```python
def test_frame_locators(page: Page):
    """Finding elements inside frames."""
    page.goto("https://example.com/with-iframe")

    # Finding frame and interacting with its elements
    frame = page.frame_locator("iframe#payment-form")
    frame.get_by_label("Card Number").fill("4111111111111111")
    frame.get_by_label("CVV").fill("123")
    frame.get_by_role("button", name="Pay").click()

    # Nested frames
    nested = page.frame_locator("#outer").frame_locator("#inner")
    nested.get_by_text("Content").is_visible()
```

## Practical Example: Testing a Form

```python
import re
from playwright.sync_api import Page, expect

def test_registration_form(page: Page):
    """Comprehensive registration form test with various locators."""
    page.goto("https://example.com/register")

    # Filling fields through semantic locators
    page.get_by_label("First Name").fill("Olena")
    page.get_by_label("Last Name").fill("Kovalenko")
    page.get_by_label("Email").fill("olena@example.com")
    page.get_by_label("Phone").fill("+380991234567")
    page.get_by_placeholder("Create a password").fill("MyPass123!")

    # Selecting from a dropdown
    page.get_by_role("combobox", name="City").select_option("Kyiv")

    # Checkbox and radio button
    page.get_by_role("checkbox", name="I agree to the terms").check()
    page.get_by_role("radio", name="Female").check()

    # Submitting the form
    page.get_by_role("button", name="Register").click()

    # Verifying successful registration
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
    expect(page.get_by_text(re.compile(r"Olena"))).to_be_visible()
```

## Useful Links

- [Official Locators Documentation](https://playwright.dev/python/docs/locators)
- [Locator selection recommendations](https://playwright.dev/python/docs/best-practices#use-locators)
- [ARIA roles reference](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
- [Playwright Codegen — locator generation](https://playwright.dev/python/docs/codegen)
