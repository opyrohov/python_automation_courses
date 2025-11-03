"""
Lecture 10 - Example 2: The super() Function
============================================
Master the super() function for calling parent methods.
"""

print("=" * 60)
print("THE super() FUNCTION")
print("=" * 60)
print()

# What is super()?
# ===============
# super() is a built-in function that gives you access to methods
# in a parent class from within a child class.
# It's most commonly used to call the parent's __init__() method.

print("1. Using super() in __init__")
print("-" * 60)


class Person:
    """Parent class for a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person.__init__ called for {name}")

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")


class Employee(Person):
    """Employee inherits from Person."""

    def __init__(self, name, age, employee_id):
        # Call parent's __init__ using super()
        super().__init__(name, age)
        # Add employee-specific attribute
        self.employee_id = employee_id
        print(f"Employee.__init__ called for {name}")

    def introduce(self):
        # Call parent's introduce method
        super().introduce()
        # Add employee-specific info
        print(f"My employee ID is {self.employee_id}")


# Create an employee
emp = Employee("Alice", 30, "EMP001")
print()
emp.introduce()

print()
print("-" * 60)
print()

# Example 2: Without super() vs With super()
# ==========================================
print("2. Comparison: Without vs With super()")
print("-" * 60)

print("❌ WITHOUT super() (Code Duplication):")
print()


class BadEmployee(Person):
    """Example of NOT using super() - BAD PRACTICE!"""

    def __init__(self, name, age, employee_id):
        # Duplicating parent's initialization code
        self.name = name
        self.age = age
        # Child-specific
        self.employee_id = employee_id


print("✅ WITH super() (Good Practice):")
print()


class GoodEmployee(Person):
    """Example using super() - GOOD PRACTICE!"""

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Reuse parent's code
        self.employee_id = employee_id


# Both work, but GoodEmployee is better!
bad_emp = BadEmployee("Bob", 25, "EMP002")
good_emp = GoodEmployee("Carol", 28, "EMP003")

bad_emp.introduce()
good_emp.introduce()

print()
print("-" * 60)
print()

# Example 3: super() with Methods
# ================================
print("3. Using super() in Regular Methods")
print("-" * 60)


class Vehicle:
    """Base vehicle class."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("🔑 Starting engine...")
        print(f"✅ {self.brand} {self.model} engine started")


class ElectricCar(Vehicle):
    """Electric car with battery."""

    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        # First, do electric car specific checks
        print(f"🔋 Checking battery ({self.battery_capacity}kWh)...")

        # Then call parent's start method
        super().start_engine()

        # Add more electric-specific stuff
        print("⚡ Electric motor ready!")


# Test it
tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.start_engine()

print()
print("-" * 60)
print()

# Example 4: Automation Example - BasePage
# ========================================
print("4. Real Automation Example: Page Objects")
print("-" * 60)


class BasePage:
    """Base page with common functionality."""

    def __init__(self, page, url):
        self.page = page
        self.url = url
        print(f"📄 BasePage initialized for {url}")

    def navigate(self):
        print(f"🌐 Navigating to {self.url}")
        # self.page.goto(self.url)

    def wait_for_load(self):
        print("⏳ Waiting for page to load...")
        # self.page.wait_for_load_state("networkidle")


class LoginPage(BasePage):
    """Login page with specific functionality."""

    def __init__(self, page, url):
        # Call parent's __init__
        super().__init__(page, url)

        # Add login-specific selectors
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"
        print("🔐 LoginPage initialized with selectors")

    def navigate(self):
        # Use parent's navigate
        super().navigate()
        # Add login-specific waiting
        super().wait_for_load()
        print("✅ Login page ready")

    def login(self, username, password):
        print(f"👤 Logging in as {username}")
        # self.page.fill(self.username_input, username)
        # self.page.fill(self.password_input, password)
        # self.page.click(self.submit_button)


# Simulate usage
class FakePage:
    pass


login_page = LoginPage(FakePage(), "https://example.com/login")
print()
login_page.navigate()
print()
login_page.login("testuser", "password123")

print()
print("-" * 60)
print()

# Example 5: Multiple Levels of Inheritance
# =========================================
print("5. Multiple Levels with super()")
print("-" * 60)


class Animal:
    """Level 1: Base class."""

    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__: {name}")

    def make_sound(self):
        print(f"{self.name} makes a sound")


class Mammal(Animal):
    """Level 2: Inherits from Animal."""

    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
        print(f"Mammal.__init__: {fur_color} fur")

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is a mammal")


class Dog(Mammal):
    """Level 3: Inherits from Mammal."""

    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed
        print(f"Dog.__init__: {breed} breed")

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} barks: Woof!")


# Create a dog - watch the initialization chain
print("Creating a Dog:")
dog = Dog("Buddy", "Brown", "Golden Retriever")
print()
print("Calling make_sound():")
dog.make_sound()

print()
print("-" * 60)
print()

# Example 6: super() Best Practices
# =================================
print("6. super() Best Practices")
print("-" * 60)


class BaseTest:
    """Base test class."""

    def __init__(self):
        self.test_name = "Base Test"
        self.setup_complete = False

    def setup(self):
        """Setup test environment."""
        print("🔧 BaseTest setup:")
        print("  - Initializing test environment")
        self.setup_complete = True


class PlaywrightTest(BaseTest):
    """Playwright test with browser setup."""

    def __init__(self):
        super().__init__()
        self.browser = None
        self.page = None

    def setup(self):
        """Setup Playwright browser."""
        # ALWAYS call parent's setup first
        super().setup()

        # Then do Playwright-specific setup
        print("🌐 PlaywrightTest setup:")
        print("  - Launching browser")
        print("  - Creating new page")
        self.browser = "Chromium"
        self.page = "Page instance"


class LoginTest(PlaywrightTest):
    """Specific login test."""

    def __init__(self):
        super().__init__()
        self.test_name = "Login Test"

    def setup(self):
        """Setup for login test."""
        # Call parent's setup (which calls grandparent's too!)
        super().setup()

        # Login-specific setup
        print("🔐 LoginTest setup:")
        print("  - Preparing test data")
        print("  - Setting up test user")


# Run the test
test = LoginTest()
print()
test.setup()

print()
print("-" * 60)
print()

# Summary
# =======
print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("✅ Use super().__init__() to call parent's __init__")
print("✅ Use super().method_name() to call parent's methods")
print("✅ super() avoids code duplication")
print("✅ super() makes maintenance easier")
print("✅ Always call super() FIRST in __init__")
print("✅ super() works through multiple inheritance levels")
print()
print("SYNTAX: super().parent_method()")
print("=" * 60)
