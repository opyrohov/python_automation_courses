"""
Lecture 9 - Example 6: Page Object Model (POM)
==============================================
Learn the Page Object Model pattern for Playwright automation.
"""

print("=" * 60)
print("EXAMPLE 6: PAGE OBJECT MODEL")
print("=" * 60)
print()


# 1. What is Page Object Model?
# =============================
print("1. What is Page Object Model (POM)?")
print("-" * 40)
print("""
Page Object Model is a design pattern where:
- Each web page is represented by a class
- Page elements (selectors) are defined as class attributes
- Page actions are defined as class methods
- Tests interact with page objects, not raw selectors

Benefits:
✅ Maintainability - Change selectors in one place
✅ Reusability - Use same page object in multiple tests
✅ Readability - Tests read like plain English
✅ Separation - Test logic separate from page logic
""")
print()


# 2. Bad Example: Without POM
# ===========================
print("2. Bad Example: Without POM")
print("-" * 40)
print("""
# Without POM - Messy and hard to maintain:
def test_login():
    page.fill("#username", "testuser")
    page.fill("#password", "password123")
    page.click("#submit-button")
    page.wait_for_selector(".welcome-message")
    assert page.locator(".welcome-message").is_visible()

Problems:
❌ Selectors scattered across tests
❌ If selector changes, update in many places
❌ Hard to reuse login logic
❌ Test code is unclear
""")
print()


# 3. Good Example: With POM
# =========================
print("3. Good Example: With POM")
print("-" * 40)

class LoginPage:
    """Page Object for Login Page."""

    def __init__(self, page):
        """Initialize with Playwright page."""
        self.page = page
        # Selectors defined in one place
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit-button"
        self.error_message = ".error-message"

    def enter_username(self, username):
        """Enter username."""
        print(f"Entering username: {username}")
        # self.page.fill(self.username_input, username)

    def enter_password(self, password):
        """Enter password."""
        print(f"Entering password: {'*' * len(password)}")
        # self.page.fill(self.password_input, password)

    def click_submit(self):
        """Click submit button."""
        print("Clicking submit button")
        # self.page.click(self.submit_button)

    def login(self, username, password):
        """Complete login action."""
        print(f"\n🔐 Logging in as: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def get_error_message(self):
        """Get error message text."""
        # return self.page.locator(self.error_message).text_content()
        return "Simulated error message"

print("LoginPage class created!")
print("\nUsage in test:")
print("  login_page = LoginPage(page)")
print("  login_page.login('testuser', 'password123')")
print()


# 4. Homepage Page Object
# =======================
print("4. Homepage Page Object")
print("-" * 40)

class HomePage:
    """Page Object for Home Page."""

    def __init__(self, page):
        self.page = page
        self.welcome_message = ".welcome-message"
        self.logout_button = "#logout"
        self.profile_link = "#profile"
        self.search_box = "#search"

    def is_logged_in(self):
        """Check if user is logged in."""
        print("Checking if user is logged in")
        # return self.page.locator(self.welcome_message).is_visible()
        return True

    def get_welcome_text(self):
        """Get welcome message text."""
        # return self.page.locator(self.welcome_message).text_content()
        return "Welcome, Test User!"

    def search(self, query):
        """Perform search."""
        print(f"🔍 Searching for: {query}")
        # self.page.fill(self.search_box, query)
        # self.page.press(self.search_box, "Enter")

    def logout(self):
        """Log out user."""
        print("Logging out")
        # self.page.click(self.logout_button)

print("HomePage class created!")
print()


# 5. Product Page Object
# ======================
print("5. Product Page Object")
print("-" * 40)

class ProductPage:
    """Page Object for Product Page."""

    def __init__(self, page):
        self.page = page
        self.product_title = "h1.product-title"
        self.product_price = ".product-price"
        self.add_to_cart_button = "#add-to-cart"
        self.quantity_input = "#quantity"
        self.cart_count = ".cart-count"

    def get_product_name(self):
        """Get product name."""
        # return self.page.locator(self.product_title).text_content()
        return "Sample Product"

    def get_price(self):
        """Get product price."""
        # price_text = self.page.locator(self.product_price).text_content()
        # return float(price_text.replace("$", ""))
        return 29.99

    def set_quantity(self, quantity):
        """Set product quantity."""
        print(f"Setting quantity to: {quantity}")
        # self.page.fill(self.quantity_input, str(quantity))

    def add_to_cart(self):
        """Add product to cart."""
        print("Adding product to cart")
        # self.page.click(self.add_to_cart_button)

    def get_cart_count(self):
        """Get number of items in cart."""
        # return int(self.page.locator(self.cart_count).text_content())
        return 1

print("ProductPage class created!")
print()


# 6. Base Page Pattern
# ====================
print("6. Base Page Pattern")
print("-" * 40)

class BasePage:
    """Base class for all page objects."""

    def __init__(self, page):
        self.page = page
        self.header = "header"
        self.footer = "footer"
        self.logo = ".logo"

    def navigate_to(self, url):
        """Navigate to a URL."""
        print(f"Navigating to: {url}")
        # self.page.goto(url)

    def get_title(self):
        """Get page title."""
        # return self.page.title()
        return "Sample Page Title"

    def wait_for_page_load(self):
        """Wait for page to load."""
        print("Waiting for page to load...")
        # self.page.wait_for_load_state("networkidle")

    def take_screenshot(self, name):
        """Take a screenshot."""
        print(f"📸 Taking screenshot: {name}.png")
        # self.page.screenshot(path=f"{name}.png")

    def click_logo(self):
        """Click the logo to go home."""
        print("Clicking logo")
        # self.page.click(self.logo)

print("BasePage class created!")
print("\nOther pages can inherit from BasePage:")
print("  class LoginPage(BasePage):")
print("      # Inherits all BasePage methods")
print()


# 7. Complete Test Flow with POM
# ==============================
print("7. Complete Test Flow with POM")
print("-" * 40)

# Simulated test
class FakePage:
    """Fake page object for demonstration."""
    def __init__(self):
        self.url = "https://example.com"

print("\n🧪 SIMULATED TEST EXECUTION:")
print("=" * 50)

# Create page objects
fake_page = FakePage()
login_page = LoginPage(fake_page)
home_page = HomePage(fake_page)
product_page = ProductPage(fake_page)

# Test flow
print("\n1. Login")
login_page.login("testuser@example.com", "SecurePass123")

print("\n2. Verify Homepage")
if home_page.is_logged_in():
    print(f"✅ {home_page.get_welcome_text()}")

print("\n3. Search for Product")
home_page.search("laptop")

print("\n4. Add Product to Cart")
print(f"Product: {product_page.get_product_name()}")
print(f"Price: ${product_page.get_price()}")
product_page.set_quantity(2)
product_page.add_to_cart()
print(f"Cart items: {product_page.get_cart_count()}")

print("\n5. Logout")
home_page.logout()

print("\n" + "=" * 50)
print("✅ Test completed successfully!")
print()


# 8. POM Best Practices
# =====================
print("8. POM Best Practices")
print("-" * 40)
print("""
✅ DO:
1. One page object per page/component
2. Store all selectors as class attributes
3. Create methods for user actions
4. Use descriptive method names
5. Return values from getter methods
6. Use a base page for common functionality

❌ DON'T:
1. Put test assertions in page objects
2. Make page objects depend on each other
3. Mix test logic with page logic
4. Hard-code test data in page objects
5. Create overly complex page objects
""")
print()


# 9. Organizing Page Objects
# ==========================
print("9. Organizing Page Objects")
print("-" * 40)
print("""
Recommended folder structure:

project/
├── pages/
│   ├── __init__.py
│   ├── base_page.py         # Base class
│   ├── login_page.py        # Login page
│   ├── home_page.py         # Home page
│   └── product_page.py      # Product page
├── tests/
│   ├── test_login.py        # Login tests
│   └── test_checkout.py     # Checkout tests
└── conftest.py              # Pytest fixtures

Usage in tests:
    from pages.login_page import LoginPage
    from pages.home_page import HomePage

    def test_login(page):
        login_page = LoginPage(page)
        login_page.login("user", "pass")

        home_page = HomePage(page)
        assert home_page.is_logged_in()
""")
print()


# 10. Advanced POM Example
# ========================
print("10. Advanced POM Example")
print("-" * 40)

class CheckoutPage:
    """Advanced page object with validation."""

    def __init__(self, page):
        self.page = page
        # Shipping fields
        self.first_name = "#shipping-first-name"
        self.last_name = "#shipping-last-name"
        self.address = "#shipping-address"
        self.city = "#shipping-city"
        self.zip_code = "#shipping-zip"

        # Payment fields
        self.card_number = "#card-number"
        self.expiry_date = "#expiry-date"
        self.cvv = "#cvv"

        # Buttons
        self.place_order_button = "#place-order"
        self.order_confirmation = ".order-confirmation"

    def fill_shipping_info(self, shipping_data):
        """Fill shipping information."""
        print("\n📦 Filling shipping information:")
        fields = {
            "first_name": shipping_data.get("first_name"),
            "last_name": shipping_data.get("last_name"),
            "address": shipping_data.get("address"),
            "city": shipping_data.get("city"),
            "zip": shipping_data.get("zip")
        }

        for field, value in fields.items():
            print(f"  {field}: {value}")
            # self.page.fill(getattr(self, field), value)

    def fill_payment_info(self, payment_data):
        """Fill payment information."""
        print("\n💳 Filling payment information:")
        print(f"  Card: {payment_data.get('card_number')}")
        print(f"  Expiry: {payment_data.get('expiry')}")
        print(f"  CVV: ***")
        # Implementation here

    def complete_checkout(self, shipping_data, payment_data):
        """Complete entire checkout process."""
        self.fill_shipping_info(shipping_data)
        self.fill_payment_info(payment_data)
        print("\n✓ Placing order...")
        # self.page.click(self.place_order_button)

    def get_order_number(self):
        """Get order confirmation number."""
        # confirmation_text = self.page.locator(self.order_confirmation).text_content()
        return "ORD-12345"

# Demo usage
checkout = CheckoutPage(FakePage())
shipping = {
    "first_name": "John",
    "last_name": "Doe",
    "address": "123 Main St",
    "city": "New York",
    "zip": "10001"
}
payment = {
    "card_number": "4111111111111111",
    "expiry": "12/25",
    "cvv": "123"
}
checkout.complete_checkout(shipping, payment)
print(f"\n✅ Order confirmed: {checkout.get_order_number()}")
print()


print("=" * 60)
print("Key Takeaways:")
print("- POM separates test logic from page logic")
print("- One class per page/component")
print("- Selectors and actions in page objects")
print("- Tests become more readable and maintainable")
print("- Easier to update when UI changes")
print("- Industry standard pattern for automation")
print("=" * 60)
