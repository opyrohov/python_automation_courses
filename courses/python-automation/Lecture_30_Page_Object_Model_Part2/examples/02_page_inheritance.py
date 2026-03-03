"""Example 2: Page Object Inheritance

Demonstrates inheritance patterns with multiple page objects
that share common functionality through a base class.
"""
from playwright.sync_api import sync_playwright, expect


# ============================================
# BASE PAGE
# ============================================

class BasePage:
    """Base page with common functionality."""

    def __init__(self, page):
        self.page = page
        # Common header/footer elements
        self.header = page.locator("h1, h2, h3").first

    def get_title(self):
        """Get page title."""
        return self.page.title()

    def get_url(self):
        """Get current URL."""
        return self.page.url

    def get_heading(self):
        """Get main heading text."""
        return self.header.text_content()

    def is_loaded(self):
        """Check if page is loaded - override in subclass."""
        return self.header.is_visible()


# ============================================
# SPECIFIC PAGES INHERITING FROM BASE
# ============================================

class AddRemovePage(BasePage):
    """Add/Remove Elements page."""

    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page):
        super().__init__(page)
        self.add_button = page.locator("button", has_text="Add Element")
        self.delete_buttons = page.locator(".added-manually")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def add_element(self):
        self.add_button.click()
        return self

    def get_element_count(self):
        return self.delete_buttons.count()

    def delete_element(self, index=0):
        self.delete_buttons.nth(index).click()
        return self


class CheckboxPage(BasePage):
    """Checkboxes page."""

    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page):
        super().__init__(page)
        self.checkboxes = page.locator("input[type='checkbox']")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def check(self, index):
        cb = self.checkboxes.nth(index)
        if not cb.is_checked():
            cb.check()
        return self

    def uncheck(self, index):
        cb = self.checkboxes.nth(index)
        if cb.is_checked():
            cb.uncheck()
        return self

    def is_checked(self, index):
        return self.checkboxes.nth(index).is_checked()


class DropdownPage(BasePage):
    """Dropdown page."""

    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, page):
        super().__init__(page)
        self.dropdown = page.locator("#dropdown")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def select_option(self, value):
        self.dropdown.select_option(value)
        return self

    def get_selected_value(self):
        return self.dropdown.input_value()


class HoversPage(BasePage):
    """Hovers page."""

    URL = "https://the-internet.herokuapp.com/hovers"

    def __init__(self, page):
        super().__init__(page)
        self.figures = page.locator(".figure")
        self.captions = page.locator(".figcaption")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def hover_on_figure(self, index):
        self.figures.nth(index).hover()
        return self

    def get_caption_text(self, index):
        return self.captions.nth(index).text_content()

    def is_caption_visible(self, index):
        return self.captions.nth(index).is_visible()


# ============================================
# DEMO
# ============================================

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print("=" * 60)
    print("PAGE INHERITANCE DEMO")
    print("=" * 60)

    # All pages inherit from BasePage
    # All have: get_title(), get_url(), get_heading(), is_loaded()

    # --- Test AddRemovePage ---
    print("\n--- AddRemovePage ---")
    add_remove = AddRemovePage(page)
    add_remove.navigate()

    # Using inherited method
    print(f"Title: {add_remove.get_title()}")
    print(f"Heading: {add_remove.get_heading()}")
    print(f"Is loaded: {add_remove.is_loaded()}")

    # Using page-specific method
    add_remove.add_element().add_element().add_element()
    print(f"Elements added: {add_remove.get_element_count()}")

    # --- Test CheckboxPage ---
    print("\n--- CheckboxPage ---")
    checkbox = CheckboxPage(page)
    checkbox.navigate()

    # Using inherited method
    print(f"Title: {checkbox.get_title()}")
    print(f"Heading: {checkbox.get_heading()}")

    # Using page-specific method
    checkbox.check(0).uncheck(1)
    print(f"Checkbox 0 checked: {checkbox.is_checked(0)}")
    print(f"Checkbox 1 checked: {checkbox.is_checked(1)}")

    # --- Test DropdownPage ---
    print("\n--- DropdownPage ---")
    dropdown = DropdownPage(page)
    dropdown.navigate()

    # Using inherited method
    print(f"Heading: {dropdown.get_heading()}")

    # Using page-specific method
    dropdown.select_option("1")
    print(f"Selected: Option {dropdown.get_selected_value()}")

    # --- Test HoversPage ---
    print("\n--- HoversPage ---")
    hovers = HoversPage(page)
    hovers.navigate()

    # Using inherited method
    print(f"Heading: {hovers.get_heading()}")

    # Using page-specific method
    hovers.hover_on_figure(0)
    print(f"Caption visible: {hovers.is_caption_visible(0)}")
    print(f"Caption text: {hovers.get_caption_text(0).strip()}")

    browser.close()

    print("\n" + "=" * 60)
    print("""
INHERITANCE PATTERNS:

class BasePage:
    - Common locators (header, footer, nav)
    - Common methods (get_title, get_url)
    - Validation (is_loaded)

class SpecificPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Call parent!
        # Add page-specific locators

    # Add page-specific methods

BENEFITS:
- Shared code in one place
- Consistent interface
- Easy to extend
- Less duplication
""")
