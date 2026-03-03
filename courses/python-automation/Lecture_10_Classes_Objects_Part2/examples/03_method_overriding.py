"""
Lecture 10 - Example 3: Method Overriding
=========================================
Learn how to override parent methods in child classes.
"""

print("=" * 60)
print("METHOD OVERRIDING")
print("=" * 60)
print()

# What is Method Overriding?
# =========================
# Method overriding is when a child class provides a different
# implementation of a method that exists in the parent class.

print("1. Basic Method Overriding")
print("-" * 60)


class Shape:
    """Parent class for shapes."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Calculate area - to be overridden."""
        return 0

    def describe(self):
        """Describe the shape."""
        return f"This is a {self.name}"


class Rectangle(Shape):
    """Rectangle with specific area calculation."""

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        """Override area calculation for rectangle."""
        return self.width * self.height


class Circle(Shape):
    """Circle with specific area calculation."""

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Override area calculation for circle."""
        return 3.14159 * self.radius ** 2


# Test overridden methods
rect = Rectangle(5, 10)
circle = Circle(7)

print(f"{rect.describe()}")
print(f"Area: {rect.area()}")  # Uses Rectangle's area method
print()
print(f"{circle.describe()}")
print(f"Area: {circle.area():.2f}")  # Uses Circle's area method

print()
print("-" * 60)
print()

# Example 2: Complete Override vs Extend
# ======================================
print("2. Complete Override vs Extending Parent Method")
print("-" * 60)


class Animal:
    """Base animal class."""

    def speak(self):
        return "Some sound"

    def info(self):
        return "I am an animal"


class Dog(Animal):
    """Dog with COMPLETE override."""

    def speak(self):
        # Completely replace parent's method
        return "Woof! Woof!"


class Cat(Animal):
    """Cat EXTENDING parent's method."""

    def speak(self):
        # Call parent's method THEN add more
        parent_sound = super().speak()
        return f"{parent_sound} - Meow!"


dog = Dog()
cat = Cat()

print(f"Dog speaks (complete override): {dog.speak()}")
print(f"Cat speaks (extending parent): {cat.speak()}")

print()
print("-" * 60)
print()

# Example 3: When to Override vs When to Extend
# =============================================
print("3. Override vs Extend - When to Use Each")
print("-" * 60)


class Logger:
    """Base logger class."""

    def log(self, message):
        """Log a message."""
        print(f"[LOG] {message}")


class FileLogger(Logger):
    """Override: Completely different logging behavior."""

    def log(self, message):
        # Complete override - don't call parent
        print(f"[FILE] Writing to file: {message}")
        # In real code: write to file


class TimestampLogger(Logger):
    """Extend: Add timestamp to existing logging."""

    def log(self, message):
        # Extend - call parent then add functionality
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_with_time = f"[{timestamp}] {message}"
        super().log(message_with_time)  # Call parent's log


# Test both approaches
regular = Logger()
file_logger = FileLogger()
timestamp_logger = TimestampLogger()

print("Regular logger:")
regular.log("Application started")
print()

print("File logger (complete override):")
file_logger.log("Error occurred")
print()

print("Timestamp logger (extending parent):")
timestamp_logger.log("User logged in")

print()
print("-" * 60)
print()

# Example 4: Page Object Overriding
# ==================================
print("4. Page Object Method Overriding")
print("-" * 60)


class BasePage:
    """Base page for all pages."""

    def __init__(self, page):
        self.page = page

    def wait_for_load(self):
        """Wait for page to load - default behavior."""
        print("⏳ Waiting for page load (default)...")
        # self.page.wait_for_load_state("domcontentloaded")


class LoginPage(BasePage):
    """Login page with specific loading requirements."""

    def __init__(self, page):
        super().__init__(page)
        self.login_form = "#login-form"

    def wait_for_load(self):
        """Override: Wait for login form specifically."""
        print("⏳ Waiting for login form to appear...")
        # self.page.wait_for_selector(self.login_form)
        print("✅ Login form loaded")


class DashboardPage(BasePage):
    """Dashboard with additional loading checks."""

    def __init__(self, page):
        super().__init__(page)

    def wait_for_load(self):
        """Extend: Call parent then wait for dashboard elements."""
        # First do base page loading
        super().wait_for_load()

        # Then dashboard-specific loading
        print("⏳ Waiting for dashboard widgets...")
        # self.page.wait_for_selector(".widget")
        print("✅ Dashboard fully loaded")


# Simulate page usage
class FakePage:
    pass


page = FakePage()

print("LoginPage loading:")
login = LoginPage(page)
login.wait_for_load()
print()

print("DashboardPage loading:")
dashboard = DashboardPage(page)
dashboard.wait_for_load()

print()
print("-" * 60)
print()

# Example 5: Multiple Methods Override
# ====================================
print("5. Overriding Multiple Methods")
print("-" * 60)


class TestCase:
    """Base test case."""

    def setup(self):
        print("🔧 Base setup")

    def run(self):
        print("▶️  Running test")

    def teardown(self):
        print("🧹 Base teardown")


class UITest(TestCase):
    """UI test with browser setup."""

    def setup(self):
        super().setup()
        print("🌐 Starting browser")

    def run(self):
        super().run()
        print("🖱️  Interacting with UI")

    def teardown(self):
        print("🛑 Closing browser")
        super().teardown()


# Run the test
test = UITest()
test.setup()
test.run()
test.teardown()

print()
print("-" * 60)
print()

# Example 6: __str__ and __repr__ Override
# ========================================
print("6. Overriding Special Methods (__str__, __repr__)")
print("-" * 60)


class Product:
    """Product without override - default behavior."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class BetterProduct:
    """Product with overridden special methods."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"BetterProduct(name='{self.name}', price={self.price})"


# Compare
regular_product = Product("Laptop", 999.99)
better_product = BetterProduct("Laptop", 999.99)

print("Regular product (no override):")
print(regular_product)  # <__main__.Product object at 0x...>
print()

print("Better product (with override):")
print(better_product)  # Laptop - $999.99
print(repr(better_product))  # BetterProduct(name='Laptop', price=999.99)

print()
print("-" * 60)
print()

# Example 7: Preventing Override with NotImplementedError
# =======================================================
print("7. Forcing Child Classes to Implement Methods")
print("-" * 60)


class AbstractPage:
    """Abstract base page that REQUIRES children to implement methods."""

    def __init__(self, page):
        self.page = page

    def get_page_title(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Child classes must implement get_page_title()")

    def is_loaded(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Child classes must implement is_loaded()")


class ContactPage(AbstractPage):
    """Contact page implementing required methods."""

    def get_page_title(self):
        """Implementation for contact page."""
        return "Contact Us"

    def is_loaded(self):
        """Check if contact page is loaded."""
        return True  # self.page.locator("h1").text_content() == "Contact Us"


# This works because ContactPage implements required methods
contact = ContactPage(FakePage())
print(f"Page title: {contact.get_page_title()}")
print(f"Is loaded: {contact.is_loaded()}")

print()
print("If a child class doesn't implement required methods:")
print("It will raise NotImplementedError when called!")

print()
print("-" * 60)
print()

# Best Practices Summary
# =====================
print("=" * 60)
print("METHOD OVERRIDING BEST PRACTICES")
print("=" * 60)
print()
print("✅ WHEN TO COMPLETELY OVERRIDE:")
print("   - Behavior is completely different")
print("   - Parent implementation doesn't apply")
print("   - Example: Different calculation methods")
print()
print("✅ WHEN TO EXTEND (use super()):")
print("   - Adding to parent's functionality")
print("   - Parent behavior still needed")
print("   - Example: Adding logging, validation")
print()
print("✅ COMMON METHODS TO OVERRIDE:")
print("   - __init__() - Custom initialization")
print("   - __str__() - String representation")
print("   - __repr__() - Developer representation")
print("   - setup() / teardown() - Test setup")
print("   - Custom business logic methods")
print()
print("❌ AVOID:")
print("   - Changing method signatures (parameters)")
print("   - Breaking parent class contract")
print("   - Overriding without good reason")
print("=" * 60)

print()
print("=" * 60)
print("Key Takeaways:")
print("- Override methods to change behavior in child classes")
print("- Use super() when extending, not when completely replacing")
print("- Override special methods like __str__ for better output")
print("- Use NotImplementedError to force child implementation")
print("=" * 60)
