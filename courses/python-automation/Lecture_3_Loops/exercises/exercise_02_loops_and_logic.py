"""
Exercise 2: Loops Combined with Logic
Practice combining loops with conditionals, strings, and comparisons from previous lectures.
"""

# ============================================
# EXERCISE 1: Grade Calculator
# ============================================
print("=== Exercise 1: Calculate Grades ===")
scores = [85, 92, 78, 95, 88, 76, 90, 82]

# TODO: Loop through scores and count how many are:
# - A grade (90+)
# - B grade (80-89)
# - C grade (70-79)
# - Below C (<70)
# Print the count for each category

# Your code here:
a_count = 0
b_count = 0
c_count = 0
below_c = 0


print(f"A grades: {a_count}")
print(f"B grades: {b_count}")
print(f"C grades: {c_count}")
print(f"Below C: {below_c}")
print()

# ============================================
# EXERCISE 2: Filter and Collect
# ============================================
print("=== Exercise 2: Find Long Words ===")
words = ["cat", "elephant", "dog", "programming", "hi", "automation", "test", "python"]

# TODO: Create a new list containing only words with more than 5 characters
# Print the original list and the filtered list

# Your code here:
long_words = []


print(f"Original: {words}")
print(f"Long words: {long_words}")
print()

# ============================================
# EXERCISE 3: Username Validation
# ============================================
print("=== Exercise 3: Validate Usernames ===")
usernames = ["john_doe", "ab", "jane-smith", "validuser123", "x", "test_user_name"]

# TODO: Validate each username based on these rules:
# - Must be at least 3 characters long
# - Must be at most 15 characters long
# - Can only contain letters, numbers, and underscores
# Print "Valid: username" or "Invalid: username (reason)"

# Your code here:


print()

# ============================================
# EXERCISE 4: Price Calculator
# ============================================
print("=== Exercise 4: Calculate Total with Discount ===")
items = [
    {"name": "Laptop", "price": 999.99, "quantity": 1},
    {"name": "Mouse", "price": 29.99, "quantity": 2},
    {"name": "Keyboard", "price": 79.99, "quantity": 1},
    {"name": "Monitor", "price": 299.99, "quantity": 2}
]

# TODO: Calculate the total cost of all items (price * quantity)
# If total is over $1000, apply a 10% discount
# Print each item's subtotal and the final total

# Your code here:
total = 0


print(f"Total before discount: ${total:.2f}")
# Apply discount if needed
# Print final total

print()

# ============================================
# EXERCISE 5: Password Strength Checker
# ============================================
print("=== Exercise 5: Check Password Strength ===")
passwords = [
    "abc123",
    "StrongPass123!",
    "weakpass",
    "MyP@ssw0rd",
    "12345678"
]

# TODO: For each password, check:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one digit
# Rate as: "Strong", "Medium", or "Weak" based on meeting 3, 2, or fewer criteria

# Your code here:


print()

# ============================================
# EXERCISE 6: Find and Replace
# ============================================
print("=== Exercise 6: Clean Data ===")
data = ["  apple  ", "BANANA", "  Cherry ", "ORANGE  ", "grape"]

# TODO: Clean each item in the list:
# - Remove leading/trailing spaces (strip)
# - Convert to lowercase
# - Capitalize first letter
# Create a new list with cleaned data

# Your code here:
cleaned_data = []


print(f"Original: {data}")
print(f"Cleaned: {cleaned_data}")
print()

# ============================================
# EXERCISE 7: Search with Multiple Conditions
# ============================================
print("=== Exercise 7: Find Matching Products ===")
products = [
    {"name": "Laptop", "category": "Electronics", "price": 999.99, "in_stock": True},
    {"name": "Desk", "category": "Furniture", "price": 299.99, "in_stock": True},
    {"name": "Mouse", "category": "Electronics", "price": 29.99, "in_stock": False},
    {"name": "Chair", "category": "Furniture", "price": 199.99, "in_stock": True},
    {"name": "Keyboard", "category": "Electronics", "price": 79.99, "in_stock": True}
]

# TODO: Find all Electronics products that are in stock and under $100
# Print the name and price of matching products

# Your code here:


print()

# ============================================
# EXERCISE 8: Group and Count
# ============================================
print("=== Exercise 8: Count by Category ===")
items = [
    "apple", "banana", "carrot", "broccoli",
    "cherry", "spinach", "orange", "lettuce"
]

# Fruits: apple, banana, cherry, orange
# Vegetables: carrot, broccoli, spinach, lettuce

# TODO: Count how many fruits and vegetables are in the list
# Loop through items and check which category each belongs to

# Your code here:
fruits = ["apple", "banana", "cherry", "orange"]
fruit_count = 0
vegetable_count = 0


print(f"Fruits: {fruit_count}")
print(f"Vegetables: {vegetable_count}")
print()

# ============================================
# EXERCISE 9: Find Min and Max
# ============================================
print("=== Exercise 9: Find Min and Max ===")
temperatures = [72, 68, 75, 70, 80, 65, 78, 73]

# TODO: Find the minimum and maximum temperatures using loops
# Don't use min() or max() functions - implement it yourself
# Also calculate the average temperature

# Your code here:
min_temp = temperatures[0]
max_temp = temperatures[0]
total_temp = 0


print(f"Temperatures: {temperatures}")
print(f"Min: {min_temp}°F")
print(f"Max: {max_temp}°F")
print(f"Average: {total_temp / len(temperatures):.1f}°F")
print()

# ============================================
# EXERCISE 10: Text Analysis
# ============================================
print("=== Exercise 10: Analyze Sentences ===")
sentences = [
    "Python is great for automation",
    "Testing is important",
    "I love coding",
    "Playwright makes testing easy"
]

# TODO: For each sentence:
# - Count the number of words (use split())
# - Check if it contains the word "test" or "Testing" (case-insensitive)
# - Print the sentence, word count, and whether it's test-related

# Your code here:


print()

# ============================================
# EXERCISE 11: Build Summary Report
# ============================================
print("=== Exercise 11: Test Results Summary ===")
test_results = [
    {"name": "Login Test", "status": "pass", "duration": 2.5},
    {"name": "Checkout Test", "status": "fail", "duration": 5.2},
    {"name": "Search Test", "status": "pass", "duration": 1.8},
    {"name": "Profile Test", "status": "pass", "duration": 3.1},
    {"name": "Cart Test", "status": "fail", "duration": 4.0}
]

# TODO: Generate a summary report:
# - Count passed and failed tests
# - Calculate total duration
# - Calculate average duration
# - Print the summary

# Your code here:


print()

# ============================================
# EXERCISE 12: Nested Data Processing
# ============================================
print("=== Exercise 12: Process User Orders ===")
users = [
    {"name": "Alice", "orders": [50, 75, 100]},
    {"name": "Bob", "orders": [25, 30]},
    {"name": "Charlie", "orders": [200, 150, 100, 50]}
]

# TODO: For each user:
# - Calculate their total spent (sum of orders)
# - Print user name and total
# - Also calculate grand total for all users

# Your code here:


print()

# ============================================
# BONUS CHALLENGE: Data Validation
# ============================================
print("=== BONUS: Comprehensive Data Validation ===")
form_submissions = [
    {"name": "John Doe", "email": "john@example.com", "age": 25, "country": "USA"},
    {"name": "Jane", "email": "invalid-email", "age": 17, "country": ""},
    {"name": "Bob Smith", "email": "bob@test.com", "age": 30, "country": "UK"},
    {"name": "X", "email": "x@y.com", "age": 150, "country": "Canada"}
]

# TODO: Validate each submission:
# - Name must be at least 3 characters
# - Email must contain "@" and "."
# - Age must be between 18 and 120
# - Country must not be empty
# For each submission, print if it's "Valid" or list the validation errors

# Your code here:


print()

print("=" * 50)
print("Excellent work combining loops with logic!")
print("Check SOLUTIONS.md to see the answers")
print("=" * 50)
