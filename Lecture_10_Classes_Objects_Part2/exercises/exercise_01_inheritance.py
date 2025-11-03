"""
Lecture 10 - Exercise 1: Inheritance
====================================
Practice implementing inheritance in Python.
"""

print("=" * 50)
print("EXERCISE: Inheritance")
print("=" * 50)
print()

# Exercise 1.1: Basic Inheritance
# ===============================
# TODO: Create a 'Vehicle' parent class with:
# - __init__(brand, model, year)
# - display_info() method that prints vehicle details
#
# Then create a 'Car' child class that inherits from Vehicle with:
# - __init__(brand, model, year, num_doors)
# - Override display_info() to include number of doors

# Your code here:


# Test:
# car = Car("Toyota", "Camry", 2023, 4)
# car.display_info()
# Expected output: Toyota Camry (2023) - 4 doors

print("-" * 50)


# Exercise 1.2: Using super()
# ===========================
# TODO: Create a 'Person' parent class with:
# - __init__(name, age)
# - introduce() method
#
# Then create a 'Student' child class with:
# - __init__(name, age, student_id)
# - Use super().__init__() to call parent's __init__
# - Override introduce() to add student ID info

# Your code here:


# Test:
# student = Student("Alice", 20, "STU001")
# student.introduce()
# Expected: Prints name, age, and student ID

print("-" * 50)


# Exercise 1.3: Multiple Child Classes
# ====================================
# TODO: Create a 'Shape' parent class with:
# - __init__(name)
# - area() method that returns 0
#
# Then create TWO child classes:
# 1. Rectangle(Shape):
#    - __init__(width, height)
#    - Override area() to return width * height
#
# 2. Circle(Shape):
#    - __init__(radius)
#    - Override area() to return 3.14159 * radius * radius

# Your code here:


# Test:
# rect = Rectangle(5, 10)
# circle = Circle(7)
# print(f"Rectangle area: {rect.area()}")  # 50
# print(f"Circle area: {circle.area():.2f}")  # 153.94

print("-" * 50)


# Exercise 1.4: BasePage for Automation
# =====================================
# TODO: Create a 'BasePage' class with:
# - __init__(page, url)
# - navigate() method
# - get_title() method
# - click_element(selector) method
#
# Then create a 'LoginPage' class that inherits from BasePage with:
# - __init__(page)
# - Call super().__init__(page, "https://example.com/login")
# - Add selectors: username_input, password_input, submit_button
# - Add login(username, password) method

# Your code here:


# Test (simulated):
# class FakePage:
#     pass
#
# login_page = LoginPage(FakePage())
# login_page.navigate()
# login_page.login("testuser", "password123")

print("-" * 50)


# Exercise 1.5: Multi-level Inheritance
# =====================================
# TODO: Create three classes with inheritance chain:
#
# 1. Animal (base class):
#    - __init__(name)
#    - speak() method
#
# 2. Mammal (inherits from Animal):
#    - __init__(name, fur_color)
#    - Use super().__init__()
#    - Add get_fur_color() method
#
# 3. Dog (inherits from Mammal):
#    - __init__(name, fur_color, breed)
#    - Use super().__init__()
#    - Override speak() to print "Woof!"
#    - Add get_breed() method

# Your code here:


# Test:
# dog = Dog("Buddy", "Brown", "Golden Retriever")
# dog.speak()  # Buddy says Woof!
# print(dog.get_fur_color())  # Brown
# print(dog.get_breed())  # Golden Retriever

print("-" * 50)


# BONUS Exercise 1.6: Abstract Base Class
# =======================================
# TODO: Create a 'Page' class that forces child classes to implement methods:
# - __init__(page)
# - is_loaded() that raises NotImplementedError
# - get_page_title() that raises NotImplementedError
#
# Then create 'ContactPage' that implements these methods:
# - is_loaded() returns True
# - get_page_title() returns "Contact Us"

# Your code here:


# Test:
# contact = ContactPage("fake_page")
# print(contact.get_page_title())  # Contact Us
# print(contact.is_loaded())  # True

print("-" * 50)

print("=" * 50)
print("Exercise 1 Complete!")
print("Check SOLUTIONS.md to verify your answers")
print("=" * 50)
