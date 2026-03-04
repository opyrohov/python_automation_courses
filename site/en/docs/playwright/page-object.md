# Page Object Model — Test Organization Pattern

Page Object Model (POM) is a design pattern that creates an object model for each page or component of a web application. It separates test logic from UI implementation details, making tests more readable and easier to maintain.

## Why POM is Needed

Without POM, tests become fragile and difficult to maintain. Changing a single selector may require changes in dozens of tests. POM solves this problem by encapsulating element interactions in one place.

::: tip Tip
The main POM principle: **tests describe WHAT to verify**, while Page Objects describe **HOW to interact** with the page.
:::

## Basic Page Object Structure

### Project Structure

```
tests/
├── conftest.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── products_page.py
├── test_login.py
├── test_dashboard.py
└── test_products.py
```

### Base Page Object

```python
# tests/pages/base_page.py
from playwright.sync_api import Page, expect

class BasePage:
    """Base class for all Page Objects."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        """Navigate to page by relative path."""
        self.page.goto(f"https://example.com{path}")

    def get_title(self) -> str:
        """Get page title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Get current URL."""
        return self.page.url

    def wait_for_page_loaded(self):
        """Wait for full page load."""
        self.page.wait_for_load_state("domcontentloaded")
```

## Example: Login Page

```python
# tests/pages/login_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the login page."""

    # Page URL
    URL = "/login"

    def __init__(self, page: Page):
        super().__init__(page)
        # Define locators
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Sign In")
        self.error_message = page.get_by_test_id("error-message")
        self.remember_checkbox = page.get_by_role("checkbox", name="Remember me")
        self.forgot_password_link = page.get_by_role("link", name="Forgot password?")

    def open(self):
        """Open the login page."""
        self.navigate(self.URL)
        return self

    def login(self, email: str, password: str):
        """Log in with specified credentials."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def login_with_remember(self, email: str, password: str):
        """Log in with 'Remember me' option."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.remember_checkbox.check()
        self.login_button.click()

    def get_error_text(self) -> str:
        """Get error message text."""
        return self.error_message.text_content()

    def expect_error_visible(self, message: str):
        """Verify error message is displayed."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(message)

    def expect_login_button_disabled(self):
        """Verify login button is disabled."""
        expect(self.login_button).to_be_disabled()
```

## Example: Dashboard Page

```python
# tests/pages/dashboard_page.py
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    """Page Object for the dashboard."""

    URL = "/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = page.get_by_test_id("welcome-msg")
        self.user_menu = page.get_by_test_id("user-menu")
        self.logout_button = page.get_by_role("menuitem", name="Logout")
        self.sidebar_links = page.locator("nav.sidebar").get_by_role("link")
        self.notification_badge = page.get_by_test_id("notification-count")
        self.stats_cards = page.locator(".stats-card")

    def open(self):
        """Open the dashboard."""
        self.navigate(self.URL)
        return self

    def get_welcome_text(self) -> str:
        """Get welcome text."""
        return self.welcome_message.text_content()

    def logout(self):
        """Log out of the account."""
        self.user_menu.click()
        self.logout_button.click()

    def navigate_to_section(self, section_name: str):
        """Navigate to section via sidebar menu."""
        self.sidebar_links.filter(has_text=section_name).click()

    def get_notification_count(self) -> int:
        """Get notification count."""
        text = self.notification_badge.text_content()
        return int(text) if text else 0

    def expect_page_loaded(self):
        """Verify the dashboard has loaded."""
        expect(self.page).to_have_url(re.compile(r".*/dashboard"))
        expect(self.welcome_message).to_be_visible()
        expect(self.sidebar_links.first).to_be_visible()
```

## Example: Products Page

```python
# tests/pages/products_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Page Object for the product catalog page."""

    URL = "/products"

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.get_by_placeholder("Search products...")
        self.category_filter = page.get_by_role("combobox", name="Category")
        self.sort_select = page.get_by_role("combobox", name="Sort by")
        self.product_cards = page.locator(".product-card")
        self.cart_badge = page.get_by_test_id("cart-count")
        self.loading_spinner = page.locator(".loading-spinner")

    def open(self):
        """Open the product catalog."""
        self.navigate(self.URL)
        self.loading_spinner.wait_for(state="hidden")
        return self

    def search(self, query: str):
        """Search for products."""
        self.search_input.fill(query)
        self.search_input.press("Enter")
        self.loading_spinner.wait_for(state="hidden")

    def filter_by_category(self, category: str):
        """Filter by category."""
        self.category_filter.select_option(label=category)
        self.loading_spinner.wait_for(state="hidden")

    def sort_by(self, option: str):
        """Sort products."""
        self.sort_select.select_option(label=option)
        self.loading_spinner.wait_for(state="hidden")

    def add_to_cart(self, product_name: str):
        """Add product to cart."""
        card = self.product_cards.filter(has_text=product_name)
        card.get_by_role("button", name="Buy").click()

    def get_product_count(self) -> int:
        """Get the number of displayed products."""
        return self.product_cards.count()

    def get_product_price(self, product_name: str) -> str:
        """Get the price of a specific product."""
        card = self.product_cards.filter(has_text=product_name)
        return card.locator(".price").text_content()

    def expect_products_loaded(self, count: int):
        """Verify products loaded."""
        expect(self.product_cards).to_have_count(count)

    def expect_empty_results(self):
        """Verify no results found."""
        expect(self.page.get_by_text("Nothing found")).to_be_visible()
        expect(self.product_cards).to_have_count(0)
```

## Writing Tests with POM

### conftest.py with Fixtures

```python
# tests/conftest.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.products_page import ProductsPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for the login page."""
    return LoginPage(page).open()

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """Fixture for the dashboard (with authentication)."""
    login = LoginPage(page).open()
    login.login("admin@example.com", "admin123")
    dashboard = DashboardPage(page)
    dashboard.expect_page_loaded()
    return dashboard

@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """Fixture for the product catalog."""
    return ProductsPage(page).open()
```

### Login Tests

```python
# tests/test_login.py
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestLogin:
    """Login page tests."""

    def test_successful_login(self, login_page: LoginPage, page):
        """Verify successful login."""
        login_page.login("user@example.com", "password123")
        dashboard = DashboardPage(page)
        dashboard.expect_page_loaded()

    def test_invalid_password(self, login_page: LoginPage):
        """Verify error on invalid password."""
        login_page.login("user@example.com", "wrong_password")
        login_page.expect_error_visible("Invalid email or password")

    def test_empty_fields(self, login_page: LoginPage):
        """Verify empty fields validation."""
        login_page.login("", "")
        login_page.expect_login_button_disabled()
```

### Product Catalog Tests

```python
# tests/test_products.py
from pages.products_page import ProductsPage

class TestProducts:
    """Product catalog tests."""

    def test_search_products(self, products_page: ProductsPage):
        """Verify product search."""
        products_page.search("Laptop")
        products_page.expect_products_loaded(5)

    def test_filter_by_category(self, products_page: ProductsPage):
        """Verify category filtering."""
        products_page.filter_by_category("Electronics")
        products_page.expect_products_loaded(8)

    def test_add_to_cart(self, products_page: ProductsPage):
        """Verify adding product to cart."""
        products_page.add_to_cart("Wireless Headphones")
        assert products_page.cart_badge.text_content() == "1"

    def test_empty_search_results(self, products_page: ProductsPage):
        """Verify search with no results."""
        products_page.search("nonexistent_product_xyz")
        products_page.expect_empty_results()
```

## Component Page Object

For repeating UI components (navigation, header, modals), create separate components:

```python
# tests/pages/components/header.py
from playwright.sync_api import Page, expect

class Header:
    """Header component (used on all pages)."""

    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator("header .logo")
        self.search = page.get_by_placeholder("Search...")
        self.cart_icon = page.get_by_test_id("cart-icon")
        self.user_avatar = page.get_by_test_id("user-avatar")

    def search_for(self, query: str):
        """Global search via header."""
        self.search.fill(query)
        self.search.press("Enter")

    def open_cart(self):
        """Open the cart."""
        self.cart_icon.click()

    def open_profile_menu(self):
        """Open the profile menu."""
        self.user_avatar.click()
```

```python
# tests/pages/dashboard_page.py (updated)
from pages.base_page import BasePage
from pages.components.header import Header

class DashboardPage(BasePage):
    """Page Object using components."""

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Header component
        # ... other locators
```

::: info Information
The component approach reduces code duplication. If the header changes, you only need to update the `Header` class, not every Page Object.
:::

## Useful Links

- [Playwright POM recommendations](https://playwright.dev/python/docs/pom)
- [Martin Fowler — PageObject Pattern](https://martinfowler.com/bliki/PageObject.html)
- [Testing best practices](https://playwright.dev/python/docs/best-practices)
