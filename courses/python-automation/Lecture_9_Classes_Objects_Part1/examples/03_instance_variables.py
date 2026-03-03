"""
Lecture 9 - Example 3: Instance Variables
=========================================
Learn how to work with instance attributes and data.
"""

print("=" * 60)
print("EXAMPLE 3: INSTANCE VARIABLES")
print("=" * 60)
print()


# 1. What are Instance Variables?
# ===============================
print("1. What are Instance Variables?")
print("-" * 40)
print("""
Instance variables are data that belongs to a specific object.
Each instance has its own copy of these variables.

Think of it like:
- Your name on your ID card (unique to you)
- Settings on your phone (different from others')
- Your score in a game (not shared with other players)
""")
print()


# 2. Creating Instance Variables
# ==============================
print("2. Creating Instance Variables")
print("-" * 40)

class Student:
    """Student class with instance variables."""

    def __init__(self, name, grade):
        """Initialize student."""
        self.name = name      # Instance variable
        self.grade = grade    # Instance variable
        self.courses = []     # Instance variable (empty list)

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

print(f"{student1.name}: Grade {student1.grade}")
print(f"{student2.name}: Grade {student2.grade}")
print()


# 3. Accessing Instance Variables
# ===============================
print("3. Accessing Instance Variables")
print("-" * 40)

class Car:
    """Car class demonstrating attribute access."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Toyota", "Camry", 2022)

# Access using dot notation
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")
print(f"Full name: {car.year} {car.make} {car.model}")
print()


# 4. Modifying Instance Variables
# ===============================
print("4. Modifying Instance Variables")
print("-" * 40)

class Counter:
    """Counter class with modifiable attribute."""

    def __init__(self, start=0):
        self.count = start

counter = Counter(10)
print(f"Initial count: {counter.count}")

# Modify the instance variable
counter.count += 5
print(f"After adding 5: {counter.count}")

counter.count -= 3
print(f"After subtracting 3: {counter.count}")
print()


# 5. Instance Variables vs Class Variables
# ========================================
print("5. Instance Variables vs Class Variables")
print("-" * 40)

class Employee:
    """Employee class demonstrating both variable types."""

    company = "Tech Corp"  # Class variable (shared)

    def __init__(self, name, salary):
        self.name = name          # Instance variable (unique)
        self.salary = salary      # Instance variable (unique)

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Instance variables are different
print(f"{emp1.name}: ${emp1.salary}")
print(f"{emp2.name}: ${emp2.salary}")

# Class variable is shared
print(f"{emp1.name} works at {emp1.company}")
print(f"{emp2.name} works at {emp2.company}")

# Changing class variable affects all
Employee.company = "New Tech Inc"
print(f"\nAfter company name change:")
print(f"{emp1.name} works at {emp1.company}")
print(f"{emp2.name} works at {emp2.company}")
print()


# 6. List and Dict Instance Variables
# ===================================
print("6. List and Dict Instance Variables")
print("-" * 40)

class ShoppingCart:
    """Shopping cart with list of items."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # Each cart has its own list
        self.total = 0

cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

# Add items to cart1
cart1.items.append("Laptop")
cart1.items.append("Mouse")

# Add items to cart2
cart2.items.append("Keyboard")

print(f"{cart1.customer_name}'s cart: {cart1.items}")
print(f"{cart2.customer_name}'s cart: {cart2.items}")
print()


# 7. Dynamic Attribute Creation
# =============================
print("7. Dynamic Attribute Creation")
print("-" * 40)

class Person:
    """Person class with dynamic attributes."""

    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(f"Name: {person.name}")

# Add new attributes dynamically
person.age = 25
person.city = "New York"

print(f"Age: {person.age}")
print(f"City: {person.city}")
print()


# 8. Private Variables Convention
# ===============================
print("8. Private Variables Convention")
print("-" * 40)

class BankAccount:
    """Bank account with 'private' balance."""

    def __init__(self, account_number):
        self.account_number = account_number
        self._balance = 0  # Leading underscore = "private"

    def deposit(self, amount):
        """Public method to deposit money."""
        self._balance += amount

    def get_balance(self):
        """Public method to get balance."""
        return self._balance

account = BankAccount("ACC001")
account.deposit(1000)

print(f"Account: {account.account_number}")
print(f"Balance: ${account.get_balance()}")
print("\nNote: _balance is meant to be private")
print("But Python doesn't enforce this - it's just a convention")
print()


# 9. Automation Example: Test Result
# ==================================
print("9. Automation Example: Test Result")
print("-" * 40)

class TestResult:
    """Class to store test execution results."""

    def __init__(self, test_name):
        self.test_name = test_name
        self.status = "Not Run"
        self.duration = 0
        self.error_message = None
        self.screenshot_path = None

result = TestResult("test_login")

# Update attributes during test execution
result.status = "Passed"
result.duration = 2.5

print(f"Test: {result.test_name}")
print(f"Status: {result.status}")
print(f"Duration: {result.duration}s")
print(f"Error: {result.error_message}")
print()


# 10. Complex Data Structures
# ===========================
print("10. Complex Data Structures")
print("-" * 40)

class TestUser:
    """Test user with complex data."""

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.preferences = {
            "theme": "dark",
            "notifications": True,
            "language": "en"
        }
        self.login_history = []
        self.permissions = ["read", "write"]

user = TestUser("testuser", "test@example.com")

print(f"Username: {user.username}")
print(f"Email: {user.email}")
print(f"Preferences: {user.preferences}")
print(f"Theme: {user.preferences['theme']}")
print(f"Permissions: {user.permissions}")

# Modify nested data
user.preferences["theme"] = "light"
user.login_history.append("2024-01-01 10:00")

print(f"\nUpdated theme: {user.preferences['theme']}")
print(f"Login history: {user.login_history}")
print()


print("=" * 60)
print("Key Takeaways:")
print("- Instance variables belong to specific objects")
print("- Each instance has its own copy of variables")
print("- Use self.variable_name to create them")
print("- Access with object.variable_name")
print("- Class variables are shared across all instances")
print("- _variable suggests 'private' (convention only)")
print("=" * 60)
