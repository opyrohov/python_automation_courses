"""
Lecture 9 - Example 1: Class Basics
===================================
Learn the fundamentals of creating and using classes in Python.
"""

print("=" * 60)
print("EXAMPLE 1: CLASS BASICS")
print("=" * 60)
print()


# 1. What is a Class?
# ===================
print("1. What is a Class?")
print("-" * 40)
print("""
A class is a blueprint or template for creating objects.
Think of it like:
- A cookie cutter (class) that makes cookies (objects)
- A blueprint (class) that builds houses (objects)
- A car factory (class) that produces cars (objects)
""")
print()


# 2. Creating Your First Class
# ============================
print("2. Creating Your First Class")
print("-" * 40)

class Dog:
    """A simple class representing a dog."""
    pass  # Empty class for now

# Create an instance (object) of the class
my_dog = Dog()
print(f"Created a dog object: {my_dog}")
print(f"Type: {type(my_dog)}")
print()


# 3. Class with Attributes
# ========================
print("3. Class with Attributes")
print("-" * 40)

class Car:
    """A simple car class."""
    # Class-level attribute (shared by all instances)
    wheels = 4

# Create instances
car1 = Car()
car2 = Car()

print(f"car1 has {car1.wheels} wheels")
print(f"car2 has {car2.wheels} wheels")
print(f"All cars have {Car.wheels} wheels")
print()


# 4. Multiple Instances
# =====================
print("4. Multiple Instances")
print("-" * 40)

class Student:
    """A simple student class."""
    school = "Python Automation Academy"

# Create multiple students
student1 = Student()
student2 = Student()
student3 = Student()

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")
print(f"Student 3: {student3}")
print(f"All students attend: {Student.school}")
print()


# 5. Adding Data to Instances
# ===========================
print("5. Adding Data to Instances")
print("-" * 40)

class Person:
    """A simple person class."""
    pass

# Create a person and add attributes
person1 = Person()
person1.name = "Alice"
person1.age = 25

person2 = Person()
person2.name = "Bob"
person2.age = 30

print(f"{person1.name} is {person1.age} years old")
print(f"{person2.name} is {person2.age} years old")
print()


# 6. Why Use Classes?
# ===================
print("6. Why Use Classes?")
print("-" * 40)
print("""
Classes help you:
1. Organize related data and functions together
2. Create reusable code
3. Model real-world concepts
4. Build complex programs more easily

Without classes (messy):
    username1 = "testuser1"
    password1 = "pass123"
    email1 = "test1@example.com"

    username2 = "testuser2"
    password2 = "pass456"
    email2 = "test2@example.com"

With classes (organized):
    user1 = User("testuser1", "pass123", "test1@example.com")
    user2 = User("testuser2", "pass456", "test2@example.com")
""")
print()


# 7. Class vs Instance
# ====================
print("7. Class vs Instance")
print("-" * 40)

class Animal:
    """An animal class."""
    species = "Unknown"  # Class attribute

# The class itself
print(f"Animal class: {Animal}")
print(f"Default species: {Animal.species}")

# Instances of the class
dog = Animal()
cat = Animal()

print(f"\ndog instance: {dog}")
print(f"cat instance: {cat}")
print(f"Are they the same? {dog is cat}")  # False - different objects
print()


# 8. Automation Example: Test Case Class
# ======================================
print("8. Automation Example: Test Case Class")
print("-" * 40)

class TestCase:
    """Represents a test case."""
    status = "Not Run"

# Create test cases
test1 = TestCase()
test2 = TestCase()
test3 = TestCase()

print(f"Test 1 status: {test1.status}")
print(f"Test 2 status: {test2.status}")
print(f"Test 3 status: {test3.status}")

# Change status for specific test
test1.status = "Passed"
test2.status = "Failed"

print(f"\nAfter running tests:")
print(f"Test 1: {test1.status}")
print(f"Test 2: {test2.status}")
print(f"Test 3: {test3.status}")  # Still "Not Run"
print()


# 9. When to Use Classes
# ======================
print("9. When to Use Classes")
print("-" * 40)
print("""
Use classes when you need to:
✅ Group related data together
✅ Create multiple similar objects
✅ Organize complex functionality
✅ Implement page objects for automation
✅ Build reusable components

Examples in automation:
- Page objects (LoginPage, HomePage)
- Test data (User, Product)
- Test utilities (Browser, Logger)
- API clients (APIClient)
""")
print()


# 10. Class Naming Conventions
# ============================
print("10. Class Naming Conventions")
print("-" * 40)
print("""
Python class naming rules:
✅ Use PascalCase (capitalize each word)
✅ Use descriptive names
✅ Singular nouns (Dog, not Dogs)

Good examples:
    class User:
    class LoginPage:
    class TestCase:
    class BrowserManager:

Bad examples:
    class user:           # Should be User
    class login_page:     # Should be LoginPage
    class Users:          # Should be User (singular)
    class x:              # Not descriptive
""")


print("=" * 60)
print("Key Takeaways:")
print("- Classes are blueprints for creating objects")
print("- Objects are instances of classes")
print("- Each instance is separate and independent")
print("- Classes help organize and reuse code")
print("- Use PascalCase for class names")
print("=" * 60)
