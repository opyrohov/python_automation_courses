# Lecture 10: Classes & Objects (Part 2) - Exercise Solutions

This file contains complete solutions for all exercises in Lecture 10.

## Exercise 1: Inheritance

### Exercise 1.1: Basic Inheritance
```python
class Vehicle:
    """Parent vehicle class."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Display vehicle information."""
        print(f"{self.brand} {self.model} ({self.year})")


class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, brand, model, year, num_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.num_doors = num_doors

    def display_info(self):
        """Override to include number of doors."""
        print(f"{self.brand} {self.model} ({self.year}) - {self.num_doors} doors")


# Test
car = Car("Toyota", "Camry", 2023, 4)
car.display_info()  # Toyota Camry (2023) - 4 doors
```

### Exercise 1.2: Using super()
```python
class Person:
    """Person parent class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Introduce the person."""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")


class Student(Person):
    """Student class inheriting from Person."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent's __init__
        self.student_id = student_id

    def introduce(self):
        """Override to include student ID."""
        super().introduce()  # Call parent's introduce
        print(f"My student ID is {self.student_id}")


# Test
student = Student("Alice", 20, "STU001")
student.introduce()
# Hi, I'm Alice and I'm 20 years old
# My student ID is STU001
```

### Exercise 1.3: Multiple Child Classes
```python
class Shape:
    """Base shape class."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Calculate area - to be overridden."""
        return 0


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Calculate circle area."""
        return 3.14159 * self.radius ** 2


# Test
rect = Rectangle(5, 10)
circle = Circle(7)
print(f"Rectangle area: {rect.area()}")  # 50
print(f"Circle area: {circle.area():.2f}")  # 153.94
```

### Exercise 1.4: BasePage for Automation
```python
class BasePage:
    """Base page for all page objects."""

    def __init__(self, page, url):
        self.page = page
        self.url = url

    def navigate(self):
        """Navigate to the page."""
        print(f"Navigating to: {self.url}")
        # self.page.goto(self.url)

    def get_title(self):
        """Get page title."""
        # return self.page.title()
        return "Page Title"

    def click_element(self, selector):
        """Click an element."""
        print(f"Clicking: {selector}")
        # self.page.click(selector)


class LoginPage(BasePage):
    """Login page object."""

    def __init__(self, page):
        super().__init__(page, "https://example.com/login")
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def login(self, username, password):
        """Perform login."""
        print(f"Logging in as: {username}")
        # self.page.fill(self.username_input, username)
        # self.page.fill(self.password_input, password)
        self.click_element(self.submit_button)


# Test
class FakePage:
    pass

login_page = LoginPage(FakePage())
login_page.navigate()
login_page.login("testuser", "password123")
```

### Exercise 1.5: Multi-level Inheritance
```python
class Animal:
    """Base animal class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Make the animal speak."""
        print(f"{self.name} makes a sound")


class Mammal(Animal):
    """Mammal class."""

    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def get_fur_color(self):
        """Get fur color."""
        return self.fur_color


class Dog(Mammal):
    """Dog class."""

    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        """Override speak method."""
        print(f"{self.name} says Woof!")

    def get_breed(self):
        """Get breed."""
        return self.breed


# Test
dog = Dog("Buddy", "Brown", "Golden Retriever")
dog.speak()  # Buddy says Woof!
print(dog.get_fur_color())  # Brown
print(dog.get_breed())  # Golden Retriever
```

### BONUS Exercise 1.6: Abstract Base Class
```python
class Page:
    """Abstract base page."""

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Child must implement is_loaded()")

    def get_page_title(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Child must implement get_page_title()")


class ContactPage(Page):
    """Contact page implementation."""

    def is_loaded(self):
        """Check if page is loaded."""
        return True

    def get_page_title(self):
        """Get page title."""
        return "Contact Us"


# Test
contact = ContactPage("fake_page")
print(contact.get_page_title())  # Contact Us
print(contact.is_loaded())  # True
```

---

## Exercise 2: Building Reusable Page Objects

### Exercise 2.1: Create BasePage
```python
class BasePage:
    """Comprehensive base page for all page objects."""

    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        """Navigate to URL."""
        print(f"Navigating to: {url}")
        # self.page.goto(url)

    def click(self, selector):
        """Click element."""
        print(f"Clicking: {selector}")
        # self.page.click(selector)

    def fill(self, selector, text):
        """Fill input field."""
        print(f"Filling '{selector}' with: {text}")
        # self.page.fill(selector, text)

    def get_text(self, selector):
        """Get element text."""
        # return self.page.locator(selector).text_content()
        return "Sample Text"

    def is_visible(self, selector):
        """Check if element is visible."""
        # return self.page.is_visible(selector)
        return True

    def wait_for_element(self, selector):
        """Wait for element to appear."""
        print(f"Waiting for: {selector}")
        # self.page.wait_for_selector(selector)

    def take_screenshot(self, name):
        """Take screenshot."""
        print(f"Screenshot: {name}.png")
        # self.page.screenshot(path=f"{name}.png")
```

### Exercise 2.2: Create LoginPage from BasePage
```python
class LoginPage(BasePage):
    """Login page object."""

    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "button[type='submit']"
        self.error_message = ".error-message"

    def login(self, username, password):
        """Perform login."""
        print(f"Logging in as: {username}")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.submit_button)

    def get_error_message(self):
        """Get error message text."""
        return self.get_text(self.error_message)

    def is_error_visible(self):
        """Check if error is visible."""
        return self.is_visible(self.error_message)


# Test
class FakePage:
    pass

login_page = LoginPage(FakePage())
login_page.login("user@test.com", "password123")
```

### Exercise 2.3: Create HomePage from BasePage
```python
class HomePage(BasePage):
    """Home page object."""

    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = ".welcome"
        self.user_menu = ".user-menu"
        self.logout_button = "#logout"
        self.search_box = "#search"

    def get_welcome_text(self):
        """Get welcome message."""
        return self.get_text(self.welcome_message)

    def search(self, query):
        """Search for item."""
        print(f"Searching for: {query}")
        self.fill(self.search_box, query)

    def logout(self):
        """Click logout."""
        print("Logging out")
        self.click(self.logout_button)

    def get_current_user(self):
        """Get current user name."""
        return self.get_text(self.user_menu)
```

### Exercise 2.4: Create ProductPage from BasePage
```python
class ProductPage(BasePage):
    """Product page object."""

    def __init__(self, page):
        super().__init__(page)
        self.product_title = "h1.product-name"
        self.price = ".product-price"
        self.add_to_cart_btn = "#add-to-cart"
        self.quantity_input = "#quantity"
        self.stock_message = ".in-stock"

    def get_product_name(self):
        """Get product name."""
        return self.get_text(self.product_title)

    def get_product_price(self):
        """Get product price."""
        price_text = self.get_text(self.price)
        # return float(price_text.replace("$", ""))
        return 99.99

    def set_quantity(self, qty):
        """Set product quantity."""
        print(f"Setting quantity to: {qty}")
        self.fill(self.quantity_input, str(qty))

    def add_to_cart(self):
        """Add product to cart."""
        print("Adding to cart")
        self.click(self.add_to_cart_btn)

    def is_in_stock(self):
        """Check if product is in stock."""
        return self.is_visible(self.stock_message)
```

### Exercise 2.5: Create Enhanced BasePage
```python
class EnhancedBasePage:
    """Enhanced base page with additional methods."""

    def __init__(self, page, url=None):
        self.page = page
        self.url = url

    def open(self):
        """Navigate to page URL."""
        if self.url:
            print(f"Opening: {self.url}")
            # self.page.goto(self.url)
        else:
            raise ValueError("URL not set for this page")

    def refresh(self):
        """Refresh the page."""
        print("Refreshing page")
        # self.page.reload()

    def go_back(self):
        """Go back in browser history."""
        print("Going back")
        # self.page.go_back()

    def get_current_url(self):
        """Get current URL."""
        # return self.page.url
        return "https://example.com"

    def get_page_title(self):
        """Get page title."""
        # return self.page.title()
        return "Page Title"

    def wait_for_page_load(self):
        """Wait for page to load."""
        print("Waiting for page load...")
        # self.page.wait_for_load_state("networkidle")

    def is_element_enabled(self, selector):
        """Check if element is enabled."""
        # return self.page.is_enabled(selector)
        return True

    def get_element_count(self, selector):
        """Get count of elements."""
        # return self.page.locator(selector).count()
        return 1
```

### Exercise 2.6: Create CheckoutPage from EnhancedBasePage
```python
class CheckoutPage(EnhancedBasePage):
    """Checkout page object."""

    def __init__(self, page):
        super().__init__(page, "https://example.com/checkout")
        self.billing_fields = {
            "name": "#billing-name",
            "address": "#billing-address",
            "city": "#billing-city",
        }
        self.payment_fields = {
            "card_number": "#card-number",
            "cvv": "#cvv",
            "expiry": "#expiry",
        }
        self.shipping_fields = {
            "address": "#shipping-address",
            "city": "#shipping-city",
        }
        self.submit_button = "#complete-order"

    def fill_billing_info(self, billing_data):
        """Fill billing information."""
        print("Filling billing info")
        # for field, selector in self.billing_fields.items():
        #     self.page.fill(selector, billing_data[field])

    def fill_payment_info(self, payment_data):
        """Fill payment information."""
        print("Filling payment info")
        # Similar implementation

    def fill_shipping_info(self, shipping_data):
        """Fill shipping information."""
        print("Filling shipping info")
        # Similar implementation

    def complete_checkout(self, billing_data, payment_data, shipping_data):
        """Complete entire checkout process."""
        print("\nStarting checkout process...")
        self.fill_billing_info(billing_data)
        self.fill_payment_info(payment_data)
        self.fill_shipping_info(shipping_data)
        print("Clicking submit")
        # self.page.click(self.submit_button)
        self.take_screenshot("checkout_complete")
        self.wait_for_page_load()
        print("Checkout completed!")

    def take_screenshot(self, name):
        """Take screenshot."""
        print(f"Screenshot: {name}.png")
```

### BONUS Exercise 2.7: Create AuthBasePage
```python
class AuthBasePage(EnhancedBasePage):
    """Base page for authenticated pages."""

    def __init__(self, page, url=None):
        super().__init__(page, url)
        self.user_menu = ".user-menu"
        self.logout_link = "#logout"

    def verify_logged_in(self):
        """Verify user is logged in."""
        print("Verifying user is logged in")
        # return self.is_element_visible(self.user_menu)
        return True

    def get_logged_in_user(self):
        """Get logged in username."""
        # return self.get_element_text(self.user_menu)
        return "Test User"

    def logout(self):
        """Logout from application."""
        print("Logging out")
        # self.click(self.logout_link)


class DashboardPage(AuthBasePage):
    """Dashboard page."""

    def __init__(self, page):
        super().__init__(page, "https://example.com/dashboard")
        self.stats_widget = ".statistics"
        self.notifications = ".notifications"
        self.user_profile = "#user-profile"

    def get_statistics(self):
        """Get dashboard statistics."""
        self.wait_for_element(self.stats_widget)
        # return self.get_element_text(self.stats_widget)
        return "Stats: 100 tests passed"

    def get_notifications_count(self):
        """Get count of notifications."""
        # return self.get_element_count(self.notifications)
        return 5

    def open_user_profile(self):
        """Open user profile."""
        print("Opening user profile")
        # self.click(self.user_profile)

    def wait_for_element(self, selector):
        """Wait for element."""
        print(f"Waiting for: {selector}")


# Test
dashboard = DashboardPage(FakePage())
dashboard.verify_logged_in()
stats = dashboard.get_statistics()
print(stats)
```

### BONUS Exercise 2.8: Complete Test Flow
```python
def test_complete_purchase_flow():
    """Test complete purchase flow."""
    print("\n" + "=" * 60)
    print("COMPLETE PURCHASE FLOW TEST")
    print("=" * 60)

    # Initialize fake page
    page = FakePage()

    # Step 1: Login
    print("\n1. Logging in...")
    login_page = LoginPage(page)
    login_page.login("test@example.com", "password123")

    # Step 2: Navigate to home and search
    print("\n2. Searching for product...")
    home_page = HomePage(page)
    home_page.search("laptop")

    # Step 3: Add product to cart
    print("\n3. Adding product to cart...")
    product_page = ProductPage(page)
    product_page.set_quantity(1)
    product_page.add_to_cart()

    # Step 4: Complete checkout
    print("\n4. Completing checkout...")
    checkout_page = CheckoutPage(page)
    checkout_page.open()

    billing_data = {"name": "Test User", "address": "123 Main St", "city": "Test City"}
    payment_data = {"card_number": "4111111111111111", "cvv": "123", "expiry": "12/25"}
    shipping_data = {"address": "123 Main St", "city": "Test City"}

    checkout_page.complete_checkout(billing_data, payment_data, shipping_data)

    print("\n" + "=" * 60)
    print("PURCHASE FLOW TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)


# Run the test
test_complete_purchase_flow()
```

---

## Exercise 3: Organizing Test Code

### Exercise 3.1: Create BaseTest Class
```python
class BaseTest:
    """Base class for all tests."""

    def setup_method(self):
        """Setup before each test."""
        print("Setup: Test initialized")
        self.base_url = "https://example.com"
        self.page = "FakePage"

    def teardown_method(self):
        """Cleanup after each test."""
        print("Teardown: Test cleanup")

    def take_screenshot(self, name):
        """Take screenshot helper."""
        print(f"Screenshot: {name}.png")

    def wait_for_page_load(self):
        """Wait for page load helper."""
        print("Waiting for page load...")
```

### Exercise 3.2: Create TestLogin Class
```python
class TestLogin(BaseTest):
    """Login tests."""

    def setup_method(self):
        """Setup login tests."""
        super().setup_method()
        self.login_page = LoginPage(self.page)
        self.valid_username = "test@example.com"
        self.valid_password = "Test123!"

    def test_valid_login(self):
        """Test login with valid credentials."""
        print(f"\nTest: Valid login with {self.valid_username}")
        self.login_page.login(self.valid_username, self.valid_password)
        print("✅ Valid login test passed")

    def test_invalid_password(self):
        """Test login with invalid password."""
        print(f"\nTest: Invalid password for {self.valid_username}")
        self.login_page.login(self.valid_username, "WrongPassword")
        # assert error_visible
        print("✅ Invalid password test passed")

    def test_empty_credentials(self):
        """Test login with empty credentials."""
        print("\nTest: Empty credentials")
        self.login_page.login("", "")
        # assert validation_errors
        print("✅ Empty credentials test passed")


# Test
test = TestLogin()
test.setup_method()
test.test_valid_login()
test.teardown_method()
```

### Exercise 3.3: Create TestData Class
```python
import random


class TestData:
    """Class for managing test data."""

    # Class-level test data
    VALID_USERS = [
        {"email": "user1@test.com", "password": "Pass123!"},
        {"email": "user2@test.com", "password": "Pass456!"},
        {"email": "admin@test.com", "password": "Admin123!"},
    ]

    INVALID_PASSWORDS = [
        "123",  # Too short
        "password",  # No numbers
        "12345678",  # No letters
        "",  # Empty
    ]

    def get_valid_user(self, index=0):
        """Get a valid test user."""
        return self.VALID_USERS[index]

    def get_invalid_password(self, index=0):
        """Get an invalid password."""
        return self.INVALID_PASSWORDS[index]

    @staticmethod
    def generate_random_email():
        """Generate random email."""
        random_num = random.randint(1000, 9999)
        return f"test{random_num}@example.com"

    @staticmethod
    def generate_test_user():
        """Generate complete test user."""
        random_num = random.randint(1000, 9999)
        return {
            "email": f"test{random_num}@example.com",
            "password": "Test123!",
            "name": f"Test User {random_num}"
        }


# Test
data = TestData()
user = data.get_valid_user(0)
print(f"Test user: {user['email']}")
random_email = TestData.generate_random_email()
print(f"Random email: {random_email}")
```

### Exercise 3.4: Create TestFixtures Class
```python
class TestFixtures:
    """Test fixtures for creating test data."""

    @staticmethod
    def create_test_user():
        """Create a test user."""
        return {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Test123!",
            "first_name": "Test",
            "last_name": "User"
        }

    @staticmethod
    def create_test_product():
        """Create a test product."""
        return {
            "name": "Test Product",
            "price": 99.99,
            "stock": 10,
            "category": "Electronics"
        }

    @staticmethod
    def create_test_order():
        """Create a test order."""
        return {
            "user": TestFixtures.create_test_user(),
            "product": TestFixtures.create_test_product(),
            "quantity": 1,
            "total": 99.99
        }

    @staticmethod
    def cleanup_test_data():
        """Clean up test data."""
        print("Cleaning up test data...")

    @staticmethod
    def reset_database():
        """Reset database to initial state."""
        print("Resetting database...")


# Test
user = TestFixtures.create_test_user()
product = TestFixtures.create_test_product()
print(f"Created user: {user['email']}")
print(f"Created product: {product['name']}")
```

### Exercise 3.5: Create Complete Test Class
```python
class TestCheckout(BaseTest):
    """Checkout tests using all components."""

    def setup_method(self):
        """Setup checkout tests."""
        super().setup_method()

        # Initialize page objects
        self.login_page = LoginPage(self.page)
        self.product_page = ProductPage(self.page)
        self.checkout_page = CheckoutPage(self.page)

        # Get test data
        self.test_data = TestData()
        self.user = self.test_data.get_valid_user(0)

        # Get test fixtures
        self.product = TestFixtures.create_test_product()

    def teardown_method(self):
        """Cleanup after tests."""
        TestFixtures.cleanup_test_data()
        super().teardown_method()

    def test_checkout_with_valid_payment(self):
        """Test checkout with valid payment."""
        print("\nTest: Checkout with valid payment")

        # Login
        self.login_page.login(self.user['email'], self.user['password'])

        # Add product
        self.product_page.add_to_cart()

        # Checkout
        billing = payment = shipping = {}
        self.checkout_page.complete_checkout(billing, payment, shipping)

        print("✅ Valid payment checkout test passed")

    def test_checkout_with_invalid_payment(self):
        """Test checkout with invalid payment."""
        print("\nTest: Checkout with invalid payment")

        # Login
        self.login_page.login(self.user['email'], self.user['password'])

        # Try invalid payment
        print("Attempting invalid payment...")
        print("✅ Invalid payment test passed")


# Test
test = TestCheckout()
test.setup_method()
test.test_checkout_with_valid_payment()
test.teardown_method()
```

### Exercise 3.6: Create Test Suite with setup_class
```python
class TestUserManagement:
    """User management tests with class-level setup."""

    @classmethod
    def setup_class(cls):
        """Setup once before all tests."""
        print("\n" + "=" * 60)
        print("CLASS SETUP: Initializing test suite")
        print("=" * 60)
        cls.test_suite_name = "User Management Tests"
        cls.test_count = 0

    @classmethod
    def teardown_class(cls):
        """Cleanup once after all tests."""
        print("\n" + "=" * 60)
        print(f"CLASS TEARDOWN: Completed {cls.test_count} tests")
        print("=" * 60)

    def setup_method(self):
        """Setup before each test."""
        print(f"\nSetup: Test in {self.test_suite_name}")
        self.user_data = TestData.generate_test_user()

    def teardown_method(self):
        """Cleanup after each test."""
        print("Teardown: Test cleanup")
        TestUserManagement.test_count += 1

    def test_create_user(self):
        """Test creating a user."""
        print(f"Test: Create user {self.user_data['email']}")
        print("✅ Create user test passed")

    def test_update_user(self):
        """Test updating a user."""
        print("Test: Update user")
        print("✅ Update user test passed")

    def test_delete_user(self):
        """Test deleting a user."""
        print("Test: Delete user")
        print("✅ Delete user test passed")


# Test the lifecycle
TestUserManagement.setup_class()

test = TestUserManagement()

test.setup_method()
test.test_create_user()
test.teardown_method()

test.setup_method()
test.test_update_user()
test.teardown_method()

test.setup_method()
test.test_delete_user()
test.teardown_method()

TestUserManagement.teardown_class()
```

### Exercise 3.7: Create Helper Utilities
```python
import random
import string
from datetime import datetime, timedelta


class StringHelpers:
    """String utility methods."""

    @staticmethod
    def generate_random_string(length=10):
        """Generate random string."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def format_email(name):
        """Format name as email."""
        return f"{name.lower().replace(' ', '.')}@test.com"

    @staticmethod
    def clean_text(text):
        """Clean text by removing extra spaces."""
        return ' '.join(text.split())


class DateHelpers:
    """Date utility methods."""

    @staticmethod
    def get_current_date():
        """Get current date."""
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def format_date(date, format_str="%Y-%m-%d"):
        """Format date object."""
        return date.strftime(format_str)

    @staticmethod
    def add_days(days):
        """Get date after adding days."""
        future_date = datetime.now() + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")


class WaitHelpers:
    """Wait utility methods."""

    @staticmethod
    def wait_for_condition(condition, timeout=30):
        """Wait for condition to be true."""
        print(f"Waiting for condition (timeout: {timeout}s)")
        # Implementation would check condition in loop
        return True

    @staticmethod
    def wait_for_text(text):
        """Wait for specific text to appear."""
        print(f"Waiting for text: {text}")
        return True


# Test utilities
random_str = StringHelpers.generate_random_string(8)
email = StringHelpers.format_email("John Doe")
current_date = DateHelpers.get_current_date()
future_date = DateHelpers.add_days(7)

print(f"Random string: {random_str}")
print(f"Email: {email}")
print(f"Current date: {current_date}")
print(f"Date in 7 days: {future_date}")
```

### BONUS Exercise 3.9: Test Report Class
```python
class TestReport:
    """Class for tracking and reporting test results."""

    def __init__(self):
        """Initialize test report."""
        self.passed_tests = []
        self.failed_tests = []
        self.skipped_tests = []

    def add_pass(self, test_name):
        """Add passed test."""
        self.passed_tests.append(test_name)

    def add_fail(self, test_name, reason):
        """Add failed test."""
        self.failed_tests.append({"name": test_name, "reason": reason})

    def add_skip(self, test_name):
        """Add skipped test."""
        self.skipped_tests.append(test_name)

    def print_summary(self):
        """Print test summary report."""
        total = len(self.passed_tests) + len(self.failed_tests) + len(self.skipped_tests)
        passed = len(self.passed_tests)
        failed = len(self.failed_tests)
        skipped = len(self.skipped_tests)

        pass_percentage = (passed / total * 100) if total > 0 else 0

        print("\n" + "=" * 60)
        print("TEST SUMMARY REPORT")
        print("=" * 60)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed} ✅")
        print(f"Failed: {failed} ❌")
        print(f"Skipped: {skipped} ⊘")
        print(f"Pass Rate: {pass_percentage:.1f}%")

        if self.failed_tests:
            print("\nFailed Tests:")
            for test in self.failed_tests:
                print(f"  ❌ {test['name']}: {test['reason']}")

        print("=" * 60)


# Test
report = TestReport()
report.add_pass("test_login")
report.add_pass("test_logout")
report.add_fail("test_checkout", "Payment gateway error")
report.add_skip("test_refund")
report.print_summary()
```

---

## Key Takeaways

1. **Inheritance** allows code reuse and organization
2. **super()** calls parent class methods properly
3. **BasePage pattern** is essential for test automation
4. **Test organization** with classes improves maintainability
5. **Separation of concerns** keeps code clean (pages, tests, data, utilities)
6. **Helper classes** provide reusable functionality
7. **Proper setup/teardown** ensures test isolation

## Next Steps

- Practice creating your own page object hierarchies
- Build a complete test suite with proper organization
- Apply these patterns to real Playwright projects
- Explore pytest fixtures for more advanced test organization

Good luck with your automation journey!
