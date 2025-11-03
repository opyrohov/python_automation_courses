"""
Lecture 10 - Example 6: OOP Best Practices
==========================================
Learn Object-Oriented Programming best practices for test automation.
"""

print("=" * 60)
print("OOP BEST PRACTICES FOR TEST AUTOMATION")
print("=" * 60)
print()

# Best Practice 1: Single Responsibility Principle
# ================================================
print("1. Single Responsibility Principle (SRP)")
print("-" * 60)
print("Each class should have ONE reason to change.")
print()

# ❌ BAD: Class doing too much
class BadLoginPage:
    """BAD: Handles UI, validation, AND database operations."""

    def login(self, username, password):
        # UI interaction
        print("Filling login form")
        # Validation
        if len(password) < 8:
            print("Password too short")
        # Database check (shouldn't be in page object!)
        print("Checking database for user")


# ✅ GOOD: Separate responsibilities
class LoginPage:
    """GOOD: Only handles UI interactions."""

    def login(self, username, password):
        print("Filling login form")
        print("Clicking submit")


class LoginValidator:
    """Separate class for validation logic."""

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8


class UserRepository:
    """Separate class for database operations."""

    @staticmethod
    def user_exists(username):
        print(f"Checking if {username} exists in database")
        return True


print("✅ Each class has a single, clear responsibility")
print()
print("-" * 60)
print()

# Best Practice 2: DRY (Don't Repeat Yourself)
# ============================================
print("2. DRY - Don't Repeat Yourself")
print("-" * 60)
print("Don't duplicate code - use inheritance and methods!")
print()

# ❌ BAD: Code duplication
class BadHomePage:
    def click_logout(self):
        print("Waiting for logout button")
        print("Clicking logout")


class BadProfilePage:
    def click_logout(self):
        print("Waiting for logout button")  # DUPLICATED!
        print("Clicking logout")  # DUPLICATED!


# ✅ GOOD: Use base class
class BasePage:
    """Common functionality in base class."""

    def click_element(self, element_name):
        print(f"Waiting for {element_name}")
        print(f"Clicking {element_name}")


class GoodHomePage(BasePage):
    def click_logout(self):
        self.click_element("logout button")


class GoodProfilePage(BasePage):
    def click_logout(self):
        self.click_element("logout button")


print("✅ Code reuse through inheritance")
print()
print("-" * 60)
print()

# Best Practice 3: Composition Over Inheritance
# =============================================
print("3. Composition Over Inheritance")
print("-" * 60)
print("Sometimes composition is better than inheritance!")
print()

# Using Composition (HAS-A relationship)
class Logger:
    """Logging utility."""

    def log(self, message):
        print(f"[LOG] {message}")


class Screenshot:
    """Screenshot utility."""

    def take(self, name):
        print(f"📸 Screenshot: {name}.png")


class PageWithComposition:
    """Page using composition - HAS-A logger and screenshot."""

    def __init__(self, page):
        self.page = page
        self.logger = Logger()  # HAS-A relationship
        self.screenshot = Screenshot()  # HAS-A relationship

    def perform_action(self):
        self.logger.log("Performing action")
        self.screenshot.take("action_performed")


page = PageWithComposition("fake_page")
page.perform_action()

print()
print("✅ Use composition when you need multiple capabilities")
print()
print("-" * 60)
print()

# Best Practice 4: Meaningful Names
# =================================
print("4. Use Clear, Meaningful Names")
print("-" * 60)
print()

# ❌ BAD: Unclear names
class LP:
    def do_it(self, u, p):
        pass


# ✅ GOOD: Clear, descriptive names
class LoginPage:
    def login(self, username, password):
        pass


# ❌ BAD: Ambiguous
class DataHandler:
    pass


# ✅ GOOD: Specific
class UserTestDataGenerator:
    pass


print("✅ GOOD NAMES:")
print("   - LoginPage, HomePage, ProductPage (pages)")
print("   - TestLogin, TestCheckout (test classes)")
print("   - login(), get_title(), is_visible() (methods)")
print()
print("❌ BAD NAMES:")
print("   - LP, HP, PP (too short)")
print("   - Thing, Stuff, Handler (too vague)")
print("   - do_thing(), process() (unclear)")
print()
print("-" * 60)
print()

# Best Practice 5: Keep Methods Small
# ===================================
print("5. Keep Methods Small and Focused")
print("-" * 60)
print()

# ❌ BAD: Method doing too much
class BadCheckoutPage:
    def complete_checkout(self, user_data, payment_data, shipping_data):
        # Fill user info (10 lines)
        # Fill payment info (10 lines)
        # Fill shipping info (10 lines)
        # Verify and submit (10 lines)
        pass  # 40+ lines of code!


# ✅ GOOD: Break into smaller methods
class GoodCheckoutPage:
    def fill_user_info(self, user_data):
        """Fill user information."""
        print("Filling user info")

    def fill_payment_info(self, payment_data):
        """Fill payment information."""
        print("Filling payment info")

    def fill_shipping_info(self, shipping_data):
        """Fill shipping information."""
        print("Filling shipping info")

    def submit_order(self):
        """Submit the order."""
        print("Submitting order")

    def complete_checkout(self, user_data, payment_data, shipping_data):
        """Complete checkout process."""
        self.fill_user_info(user_data)
        self.fill_payment_info(payment_data)
        self.fill_shipping_info(shipping_data)
        self.submit_order()


checkout = GoodCheckoutPage()
checkout.complete_checkout({}, {}, {})

print()
print("✅ Small, focused methods are easier to:")
print("   - Read and understand")
print("   - Test individually")
print("   - Reuse in different flows")
print("   - Debug when issues occur")
print()
print("-" * 60)
print()

# Best Practice 6: Use Docstrings
# ===============================
print("6. Use Docstrings for Documentation")
print("-" * 60)
print()


class WellDocumentedPage:
    """
    Page object for the product listing page.

    This class handles all interactions with the product listing,
    including filtering, sorting, and adding items to cart.
    """

    def __init__(self, page):
        """
        Initialize the product page.

        Args:
            page: Playwright page instance
        """
        self.page = page

    def search_products(self, query):
        """
        Search for products using the search bar.

        Args:
            query (str): Search term to look for

        Returns:
            int: Number of results found

        Example:
            >>> product_page.search_products("laptop")
            15
        """
        print(f"Searching for: {query}")
        return 15


print("✅ Good docstrings include:")
print("   - Class purpose")
print("   - Method description")
print("   - Parameters and types")
print("   - Return values")
print("   - Usage examples")
print()
print("-" * 60)
print()

# Best Practice 7: Handle Exceptions Properly
# ===========================================
print("7. Handle Exceptions Properly")
print("-" * 60)
print()


class RobustPage:
    """Page with proper exception handling."""

    def __init__(self, page):
        self.page = page

    def click_element(self, selector):
        """Click element with error handling."""
        try:
            print(f"Clicking: {selector}")
            # self.page.click(selector)
        except Exception as e:
            print(f"❌ Failed to click {selector}")
            self.take_screenshot(f"error_{selector}")
            raise  # Re-raise after logging

    def take_screenshot(self, name):
        """Take screenshot for debugging."""
        print(f"📸 Error screenshot: {name}")


robust_page = RobustPage("fake")
robust_page.click_element("#submit")

print()
print("✅ Good exception handling:")
print("   - Catch specific exceptions")
print("   - Log errors clearly")
print("   - Take screenshots for debugging")
print("   - Re-raise after handling")
print()
print("-" * 60)
print()

# Best Practice 8: Avoid Deep Inheritance
# =======================================
print("8. Avoid Deep Inheritance Hierarchies")
print("-" * 60)
print()

print("❌ BAD: Too deep (hard to understand)")
print("""
    BasePage
        ↓
    AuthPage
        ↓
    UserPage
        ↓
    ProfilePage
        ↓
    EditProfilePage  # Too deep!
""")

print("✅ GOOD: Shallow (easy to understand)")
print("""
    BasePage
        ↓
    LoginPage
    HomePage
    ProfilePage
""")

print()
print("✅ Keep inheritance 2-3 levels deep maximum")
print()
print("-" * 60)
print()

# Best Practice 9: Use Class and Static Methods
# =============================================
print("9. Use Class and Static Methods Appropriately")
print("-" * 60)
print()


class TestHelpers:
    """Utility class with static methods."""

    @staticmethod
    def generate_random_email():
        """Generate random email - doesn't need instance."""
        import random
        return f"test{random.randint(1000, 9999)}@example.com"

    @staticmethod
    def format_currency(amount):
        """Format amount as currency."""
        return f"${amount:.2f}"


# Use without creating instance
email = TestHelpers.generate_random_email()
price = TestHelpers.format_currency(99.99)
print(f"Generated email: {email}")
print(f"Formatted price: {price}")

print()
print("✅ Use @staticmethod for utility functions")
print("   that don't need instance or class data")
print()
print("-" * 60)
print()

# Best Practice 10: Page Object Best Practices
# ============================================
print("10. Page Object Specific Best Practices")
print("-" * 60)
print()


class BestPracticePage:
    """Example of page object best practices."""

    def __init__(self, page):
        self.page = page

        # ✅ GOOD: Define selectors as constants
        self.USERNAME_INPUT = "#username"
        self.PASSWORD_INPUT = "#password"
        self.SUBMIT_BUTTON = "button[type='submit']"

    def login(self, username, password):
        """
        ✅ GOOD: Action methods (what user does)
        Not implementation details.
        """
        self._enter_username(username)
        self._enter_password(password)
        self._click_submit()

    def _enter_username(self, username):
        """✅ GOOD: Private method (implementation detail)."""
        print(f"Entering username: {username}")

    def _enter_password(self, password):
        """✅ GOOD: Private method."""
        print("Entering password: ******")

    def _click_submit(self):
        """✅ GOOD: Private method."""
        print("Clicking submit")

    def is_error_visible(self):
        """✅ GOOD: Return data, don't assert."""
        return True  # Return True/False

    def get_error_message(self):
        """✅ GOOD: Return data for test to assert."""
        return "Invalid credentials"


print("✅ PAGE OBJECT BEST PRACTICES:")
print()
print("DO:")
print("   ✅ Store selectors in __init__")
print("   ✅ Use UPPERCASE for selector constants")
print("   ✅ Create action methods (what user does)")
print("   ✅ Return data, let tests do assertions")
print("   ✅ Use _ prefix for private methods")
print()
print("DON'T:")
print("   ❌ Put assertions in page objects")
print("   ❌ Put test logic in page objects")
print("   ❌ Make page objects depend on each other")
print("   ❌ Hard-code test data in page objects")
print()
print("-" * 60)
print()

# Best Practice 11: Test Class Best Practices
# ===========================================
print("11. Test Class Best Practices")
print("-" * 60)
print()


class BestPracticeTest:
    """Example of test class best practices."""

    def setup_method(self):
        """✅ GOOD: Setup is clear and focused."""
        self.page = "fake_page"
        self.login_page = LoginPage(self.page)

    def test_login_with_valid_credentials(self):
        """
        ✅ GOOD: Clear test name describes what is tested.

        Given: User is on login page
        When: User enters valid credentials
        Then: User is logged in successfully
        """
        # Arrange
        username = "valid@user.com"
        password = "ValidPass123!"

        # Act
        self.login_page.login(username, password)

        # Assert
        # assert is_logged_in()
        print("✅ Test passed")


print("✅ TEST CLASS BEST PRACTICES:")
print()
print("DO:")
print("   ✅ Use descriptive test names")
print("   ✅ Follow Arrange-Act-Assert pattern")
print("   ✅ Test one thing per test")
print("   ✅ Use meaningful test data")
print("   ✅ Add docstrings explaining test purpose")
print()
print("DON'T:")
print("   ❌ Test multiple things in one test")
print("   ❌ Have test dependencies")
print("   ❌ Use unclear test names like test_1")
print("   ❌ Put complex logic in tests")
print()
print("-" * 60)
print()

# Summary: The Golden Rules
# =========================
print("=" * 60)
print("THE GOLDEN RULES OF OOP IN TEST AUTOMATION")
print("=" * 60)
print()
print("1️⃣  SINGLE RESPONSIBILITY")
print("   One class = one purpose")
print()
print("2️⃣  DRY (DON'T REPEAT YOURSELF)")
print("   Use inheritance and methods to avoid duplication")
print()
print("3️⃣  CLEAR NAMING")
print("   Names should explain purpose instantly")
print()
print("4️⃣  SMALL METHODS")
print("   Each method does one thing well")
print()
print("5️⃣  DOCUMENTATION")
print("   Docstrings for every class and method")
print()
print("6️⃣  ERROR HANDLING")
print("   Handle exceptions, log errors, take screenshots")
print()
print("7️⃣  SHALLOW HIERARCHIES")
print("   Keep inheritance 2-3 levels max")
print()
print("8️⃣  SEPARATION OF CONCERNS")
print("   Pages handle UI, tests handle assertions, data is separate")
print()
print("9️⃣  CONSISTENCY")
print("   Follow same patterns throughout your code")
print()
print("🔟 SIMPLICITY")
print("   Simple code is maintainable code")
print()
print("=" * 60)
print()
print("Remember: Good OOP makes your tests:")
print("   ✅ Easy to read")
print("   ✅ Easy to maintain")
print("   ✅ Easy to extend")
print("   ✅ Reliable and robust")
print("=" * 60)
