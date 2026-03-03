# Solutions - Lecture 29: Page Object Model (Part 1)

## Exercise 1: Create Your First Page Object

```python
"""Exercise 1 Solution: Add/Remove Elements Page Object"""
from playwright.sync_api import sync_playwright


class AddRemoveElementsPage:
    """Page Object for Add/Remove Elements page."""

    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page):
        self.page = page

        # Locators
        self.add_button = page.locator("button", has_text="Add Element")
        self.delete_buttons = page.locator("button", has_text="Delete")
        self.page_heading = page.locator("h3")

    def navigate(self):
        """Navigate to the page."""
        self.page.goto(self.URL)
        return self

    def is_loaded(self):
        """Check if page is loaded."""
        return self.add_button.is_visible()

    def click_add_element(self):
        """Click the Add Element button."""
        self.add_button.click()
        return self

    def click_add_multiple(self, count):
        """Add multiple elements."""
        for _ in range(count):
            self.click_add_element()
        return self

    def get_delete_button_count(self):
        """Get number of Delete buttons."""
        return self.delete_buttons.count()

    def click_delete_button(self, index=0):
        """Click Delete button at specified index."""
        self.delete_buttons.nth(index).click()
        return self

    def click_first_delete(self):
        """Click the first Delete button."""
        return self.click_delete_button(0)

    def click_last_delete(self):
        """Click the last Delete button."""
        count = self.get_delete_button_count()
        if count > 0:
            self.click_delete_button(count - 1)
        return self

    def delete_all(self):
        """Delete all elements."""
        while self.get_delete_button_count() > 0:
            self.click_first_delete()
        return self

    def get_heading(self):
        """Get page heading text."""
        return self.page_heading.text_content()


# Test the page object
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print("=== Exercise 1 Solution ===\n")

    # Create page object
    add_remove = AddRemoveElementsPage(page)

    # Navigate
    add_remove.navigate()
    assert add_remove.is_loaded()
    print(f"1. Page loaded: {add_remove.get_heading()}")

    # Initial state
    initial_count = add_remove.get_delete_button_count()
    print(f"2. Initial delete buttons: {initial_count}")
    assert initial_count == 0

    # Add elements
    add_remove.click_add_element()
    add_remove.click_add_element()
    add_remove.click_add_element()
    print(f"3. After adding 3: {add_remove.get_delete_button_count()}")
    assert add_remove.get_delete_button_count() == 3

    # Delete one
    add_remove.click_delete_button(0)
    print(f"4. After deleting 1: {add_remove.get_delete_button_count()}")
    assert add_remove.get_delete_button_count() == 2

    # Add more using convenience method
    add_remove.click_add_multiple(3)
    print(f"5. After adding 3 more: {add_remove.get_delete_button_count()}")
    assert add_remove.get_delete_button_count() == 5

    # Delete all
    add_remove.delete_all()
    print(f"6. After delete all: {add_remove.get_delete_button_count()}")
    assert add_remove.get_delete_button_count() == 0

    # Method chaining demo
    print("\n7. Method chaining:")
    (add_remove
        .click_add_element()
        .click_add_element()
        .click_first_delete())
    print(f"   Final count: {add_remove.get_delete_button_count()}")

    browser.close()
    print("\n✓ Exercise 1 completed!")
```

### Key Points:
- Locators defined once in `__init__`
- Methods return `self` for chaining
- Convenience methods like `click_add_multiple()`
- Validation method `is_loaded()`

---

## Exercise 2: Refactor Test to Use POM

```python
"""Exercise 2 Solution: Checkbox Page with Refactored Test"""
from playwright.sync_api import sync_playwright, expect


class CheckboxPage:
    """Page Object for Checkboxes page."""

    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page):
        self.page = page

        # Locators
        self.checkboxes = page.locator("input[type='checkbox']")
        self.page_heading = page.locator("h3")

    def navigate(self):
        """Navigate to checkboxes page."""
        self.page.goto(self.URL)
        return self

    def is_loaded(self):
        """Check if page is loaded."""
        return self.page_heading.is_visible()

    def get_checkbox_count(self):
        """Get total number of checkboxes."""
        return self.checkboxes.count()

    def get_checkbox(self, index):
        """Get checkbox locator at index."""
        return self.checkboxes.nth(index)

    def is_checkbox_checked(self, index):
        """Check if checkbox at index is checked."""
        return self.get_checkbox(index).is_checked()

    def check_checkbox(self, index):
        """Check the checkbox at index."""
        checkbox = self.get_checkbox(index)
        if not checkbox.is_checked():
            checkbox.check()
        return self

    def uncheck_checkbox(self, index):
        """Uncheck the checkbox at index."""
        checkbox = self.get_checkbox(index)
        if checkbox.is_checked():
            checkbox.uncheck()
        return self

    def toggle_checkbox(self, index):
        """Toggle checkbox at index."""
        self.get_checkbox(index).click()
        return self

    def check_all(self):
        """Check all checkboxes."""
        for i in range(self.get_checkbox_count()):
            self.check_checkbox(i)
        return self

    def uncheck_all(self):
        """Uncheck all checkboxes."""
        for i in range(self.get_checkbox_count()):
            self.uncheck_checkbox(i)
        return self

    def get_checked_count(self):
        """Get number of checked checkboxes."""
        count = 0
        for i in range(self.get_checkbox_count()):
            if self.is_checkbox_checked(i):
                count += 1
        return count

    def get_state_summary(self):
        """Get summary of checkbox states."""
        states = []
        for i in range(self.get_checkbox_count()):
            states.append(self.is_checkbox_checked(i))
        return states


# Refactored test using Page Object
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 2 Solution: Refactored Test ===\n")

    # Create page object
    checkbox_page = CheckboxPage(page)

    # Navigate
    checkbox_page.navigate()
    assert checkbox_page.is_loaded()
    print(f"1. Navigated to checkboxes page")
    print(f"   Found {checkbox_page.get_checkbox_count()} checkboxes")

    # Check initial state
    initial_state = checkbox_page.get_state_summary()
    print(f"2. Initial state: {initial_state}")

    # Check checkbox 0, uncheck checkbox 1
    checkbox_page.check_checkbox(0)
    checkbox_page.uncheck_checkbox(1)
    print("3. Checked CB0, unchecked CB1")

    # Verify
    assert checkbox_page.is_checkbox_checked(0)
    assert not checkbox_page.is_checkbox_checked(1)
    print(f"4. Verified: {checkbox_page.get_state_summary()}")

    # Toggle both
    checkbox_page.toggle_checkbox(0)
    checkbox_page.toggle_checkbox(1)
    print("5. Toggled both")
    print(f"   State now: {checkbox_page.get_state_summary()}")

    # Check all
    checkbox_page.check_all()
    print(f"6. Checked all: {checkbox_page.get_state_summary()}")
    assert checkbox_page.get_checked_count() == 2

    # Uncheck all
    checkbox_page.uncheck_all()
    print(f"7. Unchecked all: {checkbox_page.get_state_summary()}")
    assert checkbox_page.get_checked_count() == 0

    browser.close()
    print("\n✓ Exercise 2 completed!")


# Comparison
print("\n" + "=" * 50)
print("COMPARISON: Before vs After")
print("=" * 50)
print("""
BEFORE (without POM):
    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    if not checkbox1.is_checked():
        checkbox1.check()

AFTER (with POM):
    checkbox_page.check_checkbox(0)

BENEFITS:
✓ Cleaner, more readable code
✓ Locators in one place
✓ Reusable methods
✓ Easy to maintain
""")
```

### Key Points:
- Single locator for all checkboxes, use `.nth()` for specific ones
- State checking with `is_checkbox_checked()`
- Convenience methods like `check_all()`, `get_state_summary()`
- Test code is much cleaner and readable

---

## Bonus: Page Object Template

```python
"""Template for creating new Page Objects"""

class PageTemplate:
    """Template page object - copy and modify for new pages."""

    # Page URL
    URL = "https://example.com/page"

    def __init__(self, page):
        """Initialize with Playwright page."""
        self.page = page

        # ================
        # LOCATORS
        # ================
        # Group by function/area

        # Navigation
        self.nav_home = page.locator("...")
        self.nav_about = page.locator("...")

        # Form elements
        self.input_name = page.locator("...")
        self.input_email = page.locator("...")
        self.submit_btn = page.locator("...")

        # Messages/alerts
        self.success_msg = page.locator("...")
        self.error_msg = page.locator("...")

        # Page elements
        self.page_title = page.locator("...")

    # ================
    # NAVIGATION
    # ================
    def navigate(self):
        """Navigate to page."""
        self.page.goto(self.URL)
        return self

    def is_loaded(self):
        """Check if page is loaded."""
        return self.page_title.is_visible()

    # ================
    # ACTIONS
    # ================
    def fill_form(self, name, email):
        """Fill the form."""
        self.input_name.fill(name)
        self.input_email.fill(email)
        return self

    def submit(self):
        """Submit the form."""
        self.submit_btn.click()
        return self

    # ================
    # GETTERS
    # ================
    def get_title(self):
        """Get page title text."""
        return self.page_title.text_content()

    def get_error(self):
        """Get error message."""
        return self.error_msg.text_content()

    # ================
    # VALIDATION
    # ================
    def has_error(self):
        """Check if error is displayed."""
        return self.error_msg.is_visible()

    def has_success(self):
        """Check if success is displayed."""
        return self.success_msg.is_visible()
```

---

## Common Mistakes to Avoid

### Mistake 1: Defining locators outside __init__
```python
# WRONG - locators as class attributes
class BadPage:
    username = page.locator("#username")  # Error! page not defined

# CORRECT - locators in __init__
class GoodPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
```

### Mistake 2: Not returning self for chaining
```python
# WRONG - breaks chaining
def click_button(self):
    self.button.click()
    # Nothing returned!

# CORRECT - enables chaining
def click_button(self):
    self.button.click()
    return self
```

### Mistake 3: Assertions in page objects
```python
# WRONG - assertions belong in tests
class BadPage:
    def login(self, user, pwd):
        self.fill_form(user, pwd)
        assert self.success.is_visible()  # Don't do this!

# CORRECT - return data, assert in test
class GoodPage:
    def login(self, user, pwd):
        self.fill_form(user, pwd)
        return self

    def is_login_successful(self):
        return self.success.is_visible()

# In test:
page.login("user", "pass")
assert page.is_login_successful()
```
