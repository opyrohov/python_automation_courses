"""
Lecture 9 - Exercise 1: Basic Classes
=====================================
Practice creating basic classes with __init__ and instance variables.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_01_basic_classes.py
3. Check your solutions against SOLUTIONS.md
"""

print("=" * 50)
print("EXERCISE: Basic Classes")
print("=" * 50)
print()

# Exercise 1.1: Create a Simple Class
# ===================================
# TODO: Create a class called 'Book' with:
# - __init__ that takes title and author
# - Instance variables: title, author

# Your code here:


# Test your Book class:
# book1 = Book("Python Basics", "John Doe")
# print(f"{book1.title} by {book1.author}")

print("-" * 50)


# Exercise 1.2: Add More Attributes
# =================================
# TODO: Create a class called 'Movie' with:
# - __init__ that takes title, director, year
# - All three as instance variables

# Your code here:


# Test your Movie class:
# movie = Movie("Inception", "Christopher Nolan", 2010)
# print(f"{movie.title} ({movie.year}) directed by {movie.director}")

print("-" * 50)


# Exercise 1.3: Default Values
# ============================
# TODO: Create a class called 'Product' with:
# - __init__ that takes name, price, in_stock (default=True)
# - All as instance variables

# Your code here:


# Test:
# product1 = Product("Laptop", 999.99)
# product2 = Product("Mouse", 29.99, False)
# print(f"{product1.name}: ${product1.price}, In Stock: {product1.in_stock}")
# print(f"{product2.name}: ${product2.price}, In Stock: {product2.in_stock}")

print("-" * 50)


# Exercise 1.4: Test User Class
# =============================
# TODO: Create a 'TestUser' class with:
# - __init__ that takes username, email, password
# - Instance variable 'is_active' set to True by default

# Your code here:


# Test:
# user = TestUser("testuser1", "test@example.com", "Pass123!")
# print(f"User: {user.username}, Active: {user.is_active}")

print("-" * 50)


# Exercise 1.5: Browser Config Class
# ==================================
# TODO: Create a 'BrowserConfig' class with:
# - __init__ that takes browser_type (default="chromium")
# - headless (default=False)
# - timeout (default=30000)

# Your code here:


# Test:
# config1 = BrowserConfig()
# config2 = BrowserConfig("firefox", True, 60000)
# print(f"Config 1: {config1.browser_type}, headless={config1.headless}")
# print(f"Config 2: {config2.browser_type}, headless={config2.headless}")

print("-" * 50)

print("=" * 50)
print("Exercise 1 Complete!")
print("Check SOLUTIONS.md for answers")
print("=" * 50)
