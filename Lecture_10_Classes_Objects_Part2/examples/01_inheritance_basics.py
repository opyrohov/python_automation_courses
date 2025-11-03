"""
Lecture 10 - Example 1: Inheritance Basics
==========================================
Learn the fundamentals of inheritance in Python.
"""

print("=" * 60)
print("INHERITANCE BASICS")
print("=" * 60)
print()

# What is Inheritance?
# ===================
# Inheritance allows a class to inherit attributes and methods from another class.
# The class being inherited from is called the PARENT (or BASE/SUPER) class.
# The class that inherits is called the CHILD (or DERIVED/SUB) class.

print("1. Basic Inheritance")
print("-" * 60)


# Parent class (Base class)
class Animal:
    """Base class representing an animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        """Make the animal speak."""
        print(f"{self.name} makes a sound")

    def info(self):
        """Display animal info."""
        print(f"{self.name} is a {self.species}")


# Child class inherits from Animal
class Dog(Animal):
    """Dog class inherits from Animal."""

    def speak(self):
        """Override parent's speak method."""
        print(f"{self.name} says Woof!")


# Create instances
generic_animal = Animal("Unknown", "Animal")
dog = Dog("Buddy", "Dog")

# Call methods
generic_animal.speak()  # Unknown makes a sound
dog.speak()  # Buddy says Woof! (overridden method)

# Dog inherits info() method from Animal
dog.info()  # Buddy is a Dog

print()
print("-" * 60)
print()

# Example 2: Multiple Child Classes
# ==================================
print("2. Multiple Child Classes")
print("-" * 60)


class Cat(Animal):
    """Cat class also inherits from Animal."""

    def speak(self):
        print(f"{self.name} says Meow!")


class Bird(Animal):
    """Bird class also inherits from Animal."""

    def speak(self):
        print(f"{self.name} says Tweet!")

    def fly(self):
        """Birds can fly (unique to Bird class)."""
        print(f"{self.name} is flying!")


# Create instances
cat = Cat("Whiskers", "Cat")
bird = Bird("Tweety", "Bird")

# All inherit from Animal
cat.speak()  # Whiskers says Meow!
bird.speak()  # Tweety says Tweet!

# Bird has unique method
bird.fly()  # Tweety is flying!

# All have info() from Animal
cat.info()  # Whiskers is a Cat
bird.info()  # Tweety is a Bird

print()
print("-" * 60)
print()

# Example 3: Adding Child-Specific Attributes
# ===========================================
print("3. Child Classes with Additional Attributes")
print("-" * 60)


class Vehicle:
    """Base vehicle class."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")


class Car(Vehicle):
    """Car class with additional attributes."""

    def __init__(self, brand, model, num_doors):
        # Initialize parent attributes
        self.brand = brand
        self.model = model
        # Add child-specific attribute
        self.num_doors = num_doors

    def display_info(self):
        """Override to show car-specific info."""
        print(f"{self.brand} {self.model} with {self.num_doors} doors")


car = Car("Toyota", "Camry", 4)
car.display_info()  # Toyota Camry with 4 doors

print()
print("-" * 60)
print()

# Example 4: Checking Inheritance
# ================================
print("4. Checking Inheritance Relationships")
print("-" * 60)

# isinstance() checks if an object is an instance of a class
print(f"dog is instance of Dog: {isinstance(dog, Dog)}")  # True
print(f"dog is instance of Animal: {isinstance(dog, Animal)}")  # True
print(f"dog is instance of Cat: {isinstance(dog, Cat)}")  # False

# issubclass() checks if a class is a subclass of another
print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")  # True
print(f"Cat is subclass of Animal: {issubclass(Cat, Animal)}")  # True
print(f"Dog is subclass of Cat: {issubclass(Dog, Cat)}")  # False

print()
print("-" * 60)
print()

# Example 5: Real Automation Example
# ===================================
print("5. Test Automation Example")
print("-" * 60)


class Page:
    """Base page class for automation."""

    def __init__(self, url):
        self.url = url
        self.is_loaded = False

    def load(self):
        """Load the page."""
        print(f"Loading page: {self.url}")
        self.is_loaded = True


class LoginPage(Page):
    """Login page class."""

    def __init__(self, url):
        self.url = url
        self.is_loaded = False
        # Add login-specific attributes
        self.username_field = "#username"
        self.password_field = "#password"

    def login(self, username, password):
        """Perform login."""
        print(f"Logging in as: {username}")


class HomePage(Page):
    """Home page class."""

    def __init__(self, url):
        self.url = url
        self.is_loaded = False
        self.welcome_message = ".welcome"

    def get_welcome_text(self):
        """Get welcome message."""
        return "Welcome, User!"


# Use page objects
login_page = LoginPage("https://example.com/login")
home_page = HomePage("https://example.com/home")

# Both inherit load() method
login_page.load()  # Loading page: https://example.com/login
home_page.load()  # Loading page: https://example.com/home

# Each has specific methods
login_page.login("testuser", "password123")
print(home_page.get_welcome_text())

print()
print("-" * 60)
print()

# Why Use Inheritance?
# ===================
print("WHY USE INHERITANCE?")
print("-" * 60)
print("✅ CODE REUSE: Write common code once in parent class")
print("✅ ORGANIZATION: Group related classes together")
print("✅ MAINTAINABILITY: Update common code in one place")
print("✅ EXTENSIBILITY: Easily add new child classes")
print("✅ CONSISTENCY: All child classes have same base functionality")
print()

print("=" * 60)
print("Key Takeaways:")
print("- Child classes inherit attributes and methods from parent")
print("- Use ParentClass in parentheses: class Child(Parent):")
print("- Child classes can override parent methods")
print("- Child classes can add new methods and attributes")
print("- isinstance() and issubclass() check relationships")
print("=" * 60)
