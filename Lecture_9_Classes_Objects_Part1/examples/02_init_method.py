"""
Lecture 9 - Example 2: The __init__ Method
==========================================
Learn how to initialize objects with the constructor method.
"""

print("=" * 60)
print("EXAMPLE 2: THE __init__ METHOD")
print("=" * 60)
print()


# 1. What is __init__?
# ===================
print("1. What is __init__?")
print("-" * 40)
print("""
__init__ is a special method called a constructor.
It runs automatically when you create a new object.
Use it to set up initial values for your object.

Think of it like:
- Setting up a new phone when you first turn it on
- Filling out a form when creating an account
- Configuring settings when starting a game
""")
print()


# 2. Basic __init__ Method
# ========================
print("2. Basic __init__ Method")
print("-" * 40)

class Dog:
    """A dog class with initialization."""

    def __init__(self):
        """Initialize a new dog."""
        print("A new dog was created!")
        self.name = "Unknown"
        self.age = 0

# Create a dog - __init__ runs automatically
my_dog = Dog()
print(f"Dog name: {my_dog.name}")
print(f"Dog age: {my_dog.age}")
print()


# 3. __init__ with Parameters
# ===========================
print("3. __init__ with Parameters")
print("-" * 40)

class Cat:
    """A cat class with parameters."""

    def __init__(self, name, age):
        """Initialize a cat with name and age."""
        self.name = name
        self.age = age
        print(f"Created cat: {name}, age {age}")

# Create cats with different attributes
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Fluffy", 5)

print(f"{cat1.name} is {cat1.age} years old")
print(f"{cat2.name} is {cat2.age} years old")
print()


# 4. The self Parameter
# =====================
print("4. The self Parameter")
print("-" * 40)
print("""
'self' represents the instance being created.
It's how you attach data to a specific object.

When you write:
    self.name = name

You're saying:
    "This instance's name attribute should be set to the value of name"
""")

class Person:
    """A person class demonstrating self."""

    def __init__(self, name, age):
        """Initialize person with name and age."""
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"person1.name = {person1.name}")
print(f"person2.name = {person2.name}")
print(f"Different objects: {person1 is person2}")
print()


# 5. Default Parameter Values
# ===========================
print("5. Default Parameter Values")
print("-" * 40)

class User:
    """User class with default values."""

    def __init__(self, username, email, active=True):
        """Initialize user with optional active status."""
        self.username = username
        self.email = email
        self.active = active

# Create users with and without default
user1 = User("testuser1", "test1@example.com")
user2 = User("testuser2", "test2@example.com", active=False)

print(f"{user1.username}: active={user1.active}")
print(f"{user2.username}: active={user2.active}")
print()


# 6. Multiple Instance Variables
# ==============================
print("6. Multiple Instance Variables")
print("-" * 40)

class Product:
    """Product class with multiple attributes."""

    def __init__(self, id, name, price, in_stock):
        """Initialize product with all attributes."""
        self.id = id
        self.name = name
        self.price = price
        self.in_stock = in_stock

product = Product(101, "Laptop", 999.99, True)

print(f"Product ID: {product.id}")
print(f"Name: {product.name}")
print(f"Price: ${product.price}")
print(f"In Stock: {product.in_stock}")
print()


# 7. Computed Attributes
# ======================
print("7. Computed Attributes")
print("-" * 40)

class Rectangle:
    """Rectangle class with computed area."""

    def __init__(self, width, height):
        """Initialize rectangle and compute area."""
        self.width = width
        self.height = height
        self.area = width * height  # Computed when created

rect = Rectangle(5, 3)

print(f"Width: {rect.width}")
print(f"Height: {rect.height}")
print(f"Area: {rect.area}")
print()


# 8. Validation in __init__
# =========================
print("8. Validation in __init__")
print("-" * 40)

class BankAccount:
    """Bank account with validation."""

    def __init__(self, account_number, balance):
        """Initialize bank account with validation."""
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.account_number = account_number
        self.balance = balance
        print(f"Account {account_number} created with ${balance}")

# Valid account
account1 = BankAccount("ACC001", 1000)

# Invalid account (commented out to not crash)
try:
    account2 = BankAccount("ACC002", -500)
except ValueError as e:
    print(f"Error creating account: {e}")
print()


# 9. Automation Example: Page Object
# ==================================
print("9. Automation Example: Page Object")
print("-" * 40)

class LoginPage:
    """Page object for login page."""

    def __init__(self, page):
        """Initialize login page with Playwright page object."""
        self.page = page
        # Store all selectors as instance variables
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"
        self.error_message = ".error"
        print("LoginPage initialized")

# Simulate creating page object
# login_page = LoginPage(playwright_page)
print("In real code: login_page = LoginPage(page)")
print()


# 10. Complex Initialization
# ==========================
print("10. Complex Initialization")
print("-" * 40)

class TestSuite:
    """Test suite with complex initialization."""

    def __init__(self, name, test_cases, config):
        """Initialize test suite with configuration."""
        self.name = name
        self.test_cases = test_cases
        self.config = config
        self.total_tests = len(test_cases)
        self.passed = 0
        self.failed = 0
        self.status = "Not Started"

        print(f"Test Suite: {name}")
        print(f"Total Tests: {self.total_tests}")

# Create test suite
test_cases = ["test_login", "test_signup", "test_logout"]
config = {"browser": "chromium", "headless": True}

suite = TestSuite("Smoke Tests", test_cases, config)

print(f"\nSuite name: {suite.name}")
print(f"Test cases: {suite.test_cases}")
print(f"Config: {suite.config}")
print()


print("=" * 60)
print("Key Takeaways:")
print("- __init__ is called automatically when creating objects")
print("- Use parameters to customize each instance")
print("- self.attribute creates instance variables")
print("- You can have default parameter values")
print("- Validation can happen in __init__")
print("- Perfect for setting up page objects")
print("=" * 60)
