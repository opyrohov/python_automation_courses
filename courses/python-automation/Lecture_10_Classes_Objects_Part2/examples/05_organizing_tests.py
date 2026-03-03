"""
Lecture 10 - Example 5: Organizing Test Code
============================================
Learn how to organize test automation code using classes.
"""

print("=" * 60)
print("ORGANIZING TEST CODE WITH CLASSES")
print("=" * 60)
print()

# Why Organize Tests with Classes?
# =================================
# Using classes to organize tests provides:
# - Shared setup/teardown logic
# - Grouped related tests
# - Reusable test utilities
# - Better test structure

print("1. Basic Test Class Structure")
print("-" * 60)


class TestLogin:
    """
    Test class for login functionality.
    Groups all login-related tests together.
    """

    def setup_method(self):
        """Run before each test method."""
        print("🔧 Setup: Initializing test")
        self.test_user = "testuser@example.com"
        self.test_password = "Test123!"

    def teardown_method(self):
        """Run after each test method."""
        print("🧹 Teardown: Cleaning up")

    def test_valid_login(self):
        """Test login with valid credentials."""
        print(f"✅ Testing valid login with {self.test_user}")
        # assert login_successful

    def test_invalid_password(self):
        """Test login with invalid password."""
        print(f"❌ Testing invalid password for {self.test_user}")
        # assert error_message_shown

    def test_empty_fields(self):
        """Test login with empty fields."""
        print("❌ Testing empty login fields")
        # assert validation_errors


# Simulate running tests
print("Running TestLogin:")
test = TestLogin()

test.setup_method()
test.test_valid_login()
test.teardown_method()
print()

test.setup_method()
test.test_invalid_password()
test.teardown_method()

print()
print("-" * 60)
print()

# Example 2: Base Test Class
# ==========================
print("2. Creating a Base Test Class")
print("-" * 60)


class BaseTest:
    """Base class for all tests with common setup."""

    def setup_method(self):
        """Common setup for all tests."""
        print("🔧 BaseTest: Common setup")
        self.base_url = "https://example.com"
        self.timeout = 30000
        print(f"   Base URL: {self.base_url}")

    def teardown_method(self):
        """Common teardown for all tests."""
        print("🧹 BaseTest: Common teardown")

    def take_screenshot(self, name):
        """Helper method available to all tests."""
        print(f"📸 Taking screenshot: {name}")

    def wait_for_page_load(self):
        """Helper method available to all tests."""
        print("⏳ Waiting for page load...")


class TestHomePage(BaseTest):
    """Home page tests inherit common functionality."""

    def setup_method(self):
        """Setup specific to HomePage tests."""
        super().setup_method()  # Call parent setup
        print("🏠 TestHomePage: Additional setup")
        self.home_url = f"{self.base_url}/home"

    def test_home_page_loads(self):
        """Test home page loads successfully."""
        print(f"✅ Testing home page loads: {self.home_url}")
        self.wait_for_page_load()  # Use inherited method

    def test_navigation_menu(self):
        """Test navigation menu."""
        print("✅ Testing navigation menu")
        self.take_screenshot("nav_menu")  # Use inherited method


# Run tests
print("Running TestHomePage:")
home_test = TestHomePage()
home_test.setup_method()
home_test.test_home_page_loads()
home_test.teardown_method()

print()
print("-" * 60)
print()

# Example 3: Test Data Management
# ===============================
print("3. Managing Test Data with Classes")
print("-" * 60)


class TestData:
    """Class to manage test data."""

    # Class-level data (shared across all instances)
    VALID_USERS = [
        {"email": "user1@test.com", "password": "Pass123!"},
        {"email": "user2@test.com", "password": "Pass456!"},
    ]

    INVALID_PASSWORDS = ["123", "short", ""]

    def __init__(self):
        """Instance-level data."""
        self.current_user = None

    def get_valid_user(self, index=0):
        """Get a valid test user."""
        return self.VALID_USERS[index]

    def get_random_email(self):
        """Generate random email."""
        import random
        random_num = random.randint(1000, 9999)
        return f"test{random_num}@example.com"


class TestRegistration(BaseTest):
    """Registration tests using TestData."""

    def setup_method(self):
        super().setup_method()
        self.test_data = TestData()

    def test_register_new_user(self):
        """Test user registration."""
        email = self.test_data.get_random_email()
        print(f"✅ Testing registration with: {email}")

    def test_register_existing_user(self):
        """Test registration with existing email."""
        user = self.test_data.get_valid_user()
        print(f"❌ Testing duplicate registration: {user['email']}")


# Run test
reg_test = TestRegistration()
reg_test.setup_method()
reg_test.test_register_new_user()

print()
print("-" * 60)
print()

# Example 4: Page Object Integration
# ==================================
print("4. Integrating Page Objects with Test Classes")
print("-" * 60)


# Page Objects
class BasePage:
    """Base page class."""

    def __init__(self, page):
        self.page = page


class LoginPage(BasePage):
    """Login page object."""

    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#username"
        self.password_input = "#password"

    def login(self, username, password):
        """Perform login."""
        print(f"🔐 Logging in: {username}")


class HomePage(BasePage):
    """Home page object."""

    def __init__(self, page):
        super().__init__(page)
        self.welcome_msg = ".welcome"

    def is_logged_in(self):
        """Check if user is logged in."""
        return True


# Test Class using Page Objects
class TestLoginFlow(BaseTest):
    """Login flow tests using page objects."""

    def setup_method(self):
        super().setup_method()
        # Initialize page objects
        self.page = "FakePage"
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)

    def test_successful_login_flow(self):
        """Test complete login flow."""
        print("\n🧪 Test: Successful Login Flow")
        print("=" * 50)

        # Use page objects
        self.login_page.login("user@test.com", "password")
        assert self.home_page.is_logged_in()

        print("✅ Login flow test passed")
        print("=" * 50)


# Run test
login_flow_test = TestLoginFlow()
login_flow_test.setup_method()
login_flow_test.test_successful_login_flow()

print()
print("-" * 60)
print()

# Example 5: Test Fixtures and Helpers
# ====================================
print("5. Creating Reusable Test Fixtures")
print("-" * 60)


class TestFixtures:
    """Class containing reusable test fixtures."""

    @staticmethod
    def create_test_user():
        """Create a test user."""
        return {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Test123!"
        }

    @staticmethod
    def create_test_product():
        """Create a test product."""
        return {
            "name": "Test Product",
            "price": 99.99,
            "stock": 10
        }

    @staticmethod
    def cleanup_test_data():
        """Clean up test data."""
        print("🧹 Cleaning up test data...")


class TestShoppingCart(BaseTest):
    """Shopping cart tests using fixtures."""

    def setup_method(self):
        super().setup_method()
        self.user = TestFixtures.create_test_user()
        self.product = TestFixtures.create_test_product()

    def teardown_method(self):
        TestFixtures.cleanup_test_data()
        super().teardown_method()

    def test_add_to_cart(self):
        """Test adding product to cart."""
        print(f"🛒 Adding {self.product['name']} to cart")
        print(f"   User: {self.user['email']}")


# Run test
cart_test = TestShoppingCart()
cart_test.setup_method()
cart_test.test_add_to_cart()
cart_test.teardown_method()

print()
print("-" * 60)
print()

# Example 6: Complete Test Suite Organization
# ===========================================
print("6. Complete Test Suite Structure")
print("-" * 60)

print("""
📁 Test Suite Structure:
========================

tests/
├── conftest.py                 # Pytest configuration
├── base/
│   ├── base_test.py           # BaseTest class
│   └── test_fixtures.py       # Shared fixtures
├── pages/
│   ├── base_page.py           # BasePage class
│   ├── login_page.py          # LoginPage
│   ├── home_page.py           # HomePage
│   └── product_page.py        # ProductPage
├── test_data/
│   ├── users.py               # User test data
│   └── products.py            # Product test data
├── utilities/
│   ├── helpers.py             # Helper functions
│   └── config.py              # Configuration
└── test_suites/
    ├── test_login.py          # Login tests
    ├── test_products.py       # Product tests
    └── test_checkout.py       # Checkout tests
""")

print()
print("-" * 60)
print()

# Example 7: Real-World Test Class
# ================================
print("7. Complete Real-World Test Class")
print("-" * 60)


class TestUserAuthentication(BaseTest):
    """
    Complete test class for user authentication.
    Demonstrates all best practices.
    """

    @classmethod
    def setup_class(cls):
        """Run once before all tests in the class."""
        print("\n🏗️  Class Setup: Initializing test suite")
        cls.test_suite_name = "User Authentication Tests"

    @classmethod
    def teardown_class(cls):
        """Run once after all tests in the class."""
        print("🏁 Class Teardown: Test suite completed\n")

    def setup_method(self):
        """Run before each test."""
        super().setup_method()
        print(f"🔧 Setting up test in {self.test_suite_name}")
        self.page = "FakePage"
        self.login_page = LoginPage(self.page)

    def teardown_method(self):
        """Run after each test."""
        print("🧹 Cleaning up test")
        super().teardown_method()

    def test_login_with_valid_credentials(self):
        """
        Test ID: AUTH-001
        Test login with valid username and password.
        Expected: User is logged in successfully.
        """
        print("\n📝 Test: AUTH-001 - Valid Login")
        self.login_page.login("valid@user.com", "ValidPass123!")
        print("✅ PASS: User logged in successfully\n")

    def test_login_with_invalid_credentials(self):
        """
        Test ID: AUTH-002
        Test login with invalid credentials.
        Expected: Error message is shown.
        """
        print("\n📝 Test: AUTH-002 - Invalid Login")
        self.login_page.login("invalid@user.com", "WrongPass")
        print("✅ PASS: Error message displayed\n")

    def test_logout_functionality(self):
        """
        Test ID: AUTH-003
        Test logout functionality.
        Expected: User is logged out successfully.
        """
        print("\n📝 Test: AUTH-003 - Logout")
        print("✅ PASS: User logged out successfully\n")


# Run the test class
print("=" * 60)
print("RUNNING TEST SUITE")
print("=" * 60)

auth_tests = TestUserAuthentication()
TestUserAuthentication.setup_class()

auth_tests.setup_method()
auth_tests.test_login_with_valid_credentials()
auth_tests.teardown_method()

auth_tests.setup_method()
auth_tests.test_login_with_invalid_credentials()
auth_tests.teardown_method()

TestUserAuthentication.teardown_class()

print()
print("-" * 60)
print()

# Best Practices Summary
# =====================
print("=" * 60)
print("TEST ORGANIZATION BEST PRACTICES")
print("=" * 60)
print()
print("✅ CLASS ORGANIZATION:")
print("   - One test class per feature/page")
print("   - Clear, descriptive class names (TestFeatureName)")
print("   - Group related tests together")
print()
print("✅ SETUP/TEARDOWN:")
print("   - Use setup_method() for test-specific setup")
print("   - Use setup_class() for suite-wide setup")
print("   - Always clean up in teardown")
print()
print("✅ TEST DATA:")
print("   - Separate test data from test logic")
print("   - Use classes to organize test data")
print("   - Create reusable fixtures")
print()
print("✅ PAGE OBJECTS:")
print("   - Initialize page objects in setup")
print("   - Keep test logic in test methods")
print("   - Keep page logic in page objects")
print()
print("✅ NAMING:")
print("   - test_method_name() for test methods")
print("   - TestClassName for test classes")
print("   - Use descriptive, clear names")
print()
print("=" * 60)

print()
print("=" * 60)
print("Key Takeaways:")
print("- Use classes to organize related tests")
print("- Create BaseTest for common functionality")
print("- Separate concerns: tests, pages, data, utilities")
print("- Use setup/teardown for initialization and cleanup")
print("- Keep tests clean and readable")
print("=" * 60)
