"""
Lecture 9 - Example 4: Instance Methods
=======================================
Learn how to define and use methods in classes.
"""

print("=" * 60)
print("EXAMPLE 4: INSTANCE METHODS")
print("=" * 60)
print()


# 1. What are Instance Methods?
# =============================
print("1. What are Instance Methods?")
print("-" * 40)
print("""
Instance methods are functions that belong to a class.
They can access and modify instance variables.
They always have 'self' as the first parameter.

Think of methods as:
- Actions an object can perform
- Behaviors of an object
- Operations you can do with the object
""")
print()


# 2. Basic Instance Method
# ========================
print("2. Basic Instance Method")
print("-" * 40)

class Dog:
    """Dog class with methods."""

    def __init__(self, name):
        self.name = name

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")

    def sit(self):
        """Make the dog sit."""
        print(f"{self.name} is now sitting")

dog = Dog("Buddy")
dog.bark()  # Call the method
dog.sit()   # Call another method
print()


# 3. Methods with Parameters
# ==========================
print("3. Methods with Parameters")
print("-" * 40)

class Calculator:
    """Calculator class with methods."""

    def __init__(self, name):
        self.name = name
        self.result = 0

    def add(self, a, b):
        """Add two numbers."""
        self.result = a + b
        print(f"{self.name}: {a} + {b} = {self.result}")
        return self.result

    def multiply(self, a, b):
        """Multiply two numbers."""
        self.result = a * b
        print(f"{self.name}: {a} × {b} = {self.result}")
        return self.result

calc = Calculator("MyCalc")
calc.add(5, 3)
calc.multiply(4, 7)
print()


# 4. Methods that Modify Instance Variables
# =========================================
print("4. Methods that Modify Instance Variables")
print("-" * 40)

class BankAccount:
    """Bank account with deposit and withdrawal."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        """Get current balance."""
        return self.balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Insufficient funds
print(f"Final balance: ${account.get_balance()}")
print()


# 5. Methods Calling Other Methods
# ================================
print("5. Methods Calling Other Methods")
print("-" * 40)

class Rectangle:
    """Rectangle with area and perimeter calculations."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)

    def describe(self):
        """Describe the rectangle using other methods."""
        print(f"Rectangle: {self.width} × {self.height}")
        print(f"Area: {self.area()}")          # Calling another method
        print(f"Perimeter: {self.perimeter()}")  # Calling another method

rect = Rectangle(5, 3)
rect.describe()
print()


# 6. Methods with Return Values
# =============================
print("6. Methods with Return Values")
print("-" * 40)

class User:
    """User class with getter methods."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        """Return full name."""
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        """Check if user is an adult."""
        return self.age >= 18

    def get_initials(self):
        """Get user initials."""
        return f"{self.first_name[0]}.{self.last_name[0]}."

user = User("Alice", "Smith", 25)
print(f"Full name: {user.get_full_name()}")
print(f"Initials: {user.get_initials()}")
print(f"Is adult: {user.is_adult()}")
print()


# 7. Methods for Validation
# =========================
print("7. Methods for Validation")
print("-" * 40)

class Email:
    """Email class with validation."""

    def __init__(self, address):
        self.address = address

    def is_valid(self):
        """Check if email is valid."""
        return "@" in self.address and "." in self.address

    def get_domain(self):
        """Get email domain."""
        if "@" in self.address:
            return self.address.split("@")[1]
        return None

email1 = Email("test@example.com")
email2 = Email("invalid-email")

print(f"{email1.address}: Valid? {email1.is_valid()}, Domain: {email1.get_domain()}")
print(f"{email2.address}: Valid? {email2.is_valid()}, Domain: {email2.get_domain()}")
print()


# 8. String Representation Methods
# ================================
print("8. String Representation Methods")
print("-" * 40)

class Product:
    """Product class with string representation."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """Return user-friendly string representation."""
        return f"{self.name} (${self.price})"

    def __repr__(self):
        """Return detailed string representation."""
        return f"Product(name='{self.name}', price={self.price})"

product = Product("Laptop", 999.99)
print(f"Using str(): {str(product)}")
print(f"Using repr(): {repr(product)}")
print(f"Direct print: {product}")  # Uses __str__
print()


# 9. Automation Example: Page Object Methods
# ==========================================
print("9. Automation Example: Page Object Methods")
print("-" * 40)

class LoginPage:
    """Login page with action methods."""

    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def enter_username(self, username):
        """Enter username into input field."""
        print(f"Entering username: {username}")
        # In real code: self.page.fill(self.username_input, username)

    def enter_password(self, password):
        """Enter password into input field."""
        print(f"Entering password: {'*' * len(password)}")
        # In real code: self.page.fill(self.password_input, password)

    def click_submit(self):
        """Click the submit button."""
        print("Clicking submit button")
        # In real code: self.page.click(self.submit_button)

    def login(self, username, password):
        """Complete login action."""
        print(f"\nPerforming login for: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

# Simulate usage
# login_page = LoginPage(page)
print("Creating login page...")
print("\nSimulating login:")
print("-" * 30)

# Simulated login
class FakePage:
    pass

login_page = LoginPage(FakePage())
login_page.login("testuser", "password123")
print()


# 10. Complex Method Example
# ==========================
print("10. Complex Method Example")
print("-" * 40)

class TestRunner:
    """Test runner with multiple methods."""

    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.tests = []
        self.passed = 0
        self.failed = 0

    def add_test(self, test_name):
        """Add a test to the suite."""
        self.tests.append(test_name)
        print(f"Added test: {test_name}")

    def run_test(self, test_name, passed):
        """Run a single test."""
        if passed:
            self.passed += 1
            print(f"✅ {test_name}: PASSED")
        else:
            self.failed += 1
            print(f"❌ {test_name}: FAILED")

    def run_all(self):
        """Run all tests."""
        print(f"\n{'=' * 40}")
        print(f"Running suite: {self.suite_name}")
        print(f"{'=' * 40}")
        # Simulate running tests
        for test in self.tests:
            # Simulated result
            import random
            result = random.choice([True, False])
            self.run_test(test, result)

    def get_summary(self):
        """Get test results summary."""
        total = self.passed + self.failed
        if total == 0:
            return "No tests run"
        success_rate = (self.passed / total) * 100
        return f"Tests: {total} | Passed: {self.passed} | Failed: {self.failed} | Success: {success_rate:.1f}%"

# Use the test runner
runner = TestRunner("Smoke Tests")
runner.add_test("test_login")
runner.add_test("test_signup")
runner.add_test("test_logout")
runner.run_all()
print(f"\n{runner.get_summary()}")
print()


print("=" * 60)
print("Key Takeaways:")
print("- Methods are functions inside a class")
print("- Always use 'self' as the first parameter")
print("- Methods can access instance variables with self.variable")
print("- Methods can call other methods")
print("- Use methods to define object behaviors")
print("- Perfect for page object actions")
print("=" * 60)
