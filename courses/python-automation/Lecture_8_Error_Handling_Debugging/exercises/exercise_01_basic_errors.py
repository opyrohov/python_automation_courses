"""
Lecture 8 - Exercise 1: Basic Error Handling
============================================
Practice try/except blocks and handling common errors.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_01_basic_errors.py
3. Check your solutions against SOLUTIONS.md
"""

print("=" * 50)
print("EXERCISE: Basic Error Handling")
print("=" * 50)
print()

# Exercise 1.1: Basic Try/Except
# ==============================
# TODO: Create a function safe_divide(a, b) that:
# - Divides a by b
# - Returns None if b is zero
# - Handles ZeroDivisionError

# Your code here:


# Test your function:
# print(safe_divide(10, 2))  # Should return 5.0
# print(safe_divide(10, 0))  # Should return None

print("-" * 50)


# Exercise 1.2: Multiple Exceptions
# =================================
# TODO: Create a function get_list_item(lst, index) that:
# - Returns the item at the given index
# - Returns "Index out of range" if IndexError
# - Returns "Invalid type" if TypeError
# - Handles both exceptions

# Your code here:


# Test your function:
# print(get_list_item([1, 2, 3], 1))  # Should return 2
# print(get_list_item([1, 2, 3], 10))  # Handle IndexError
# print(get_list_item("not a list", 0))  # Handle TypeError

print("-" * 50)


# Exercise 1.3: Try/Except/Else
# =============================
# TODO: Create a function convert_to_int(value) that:
# - Tries to convert value to int
# - If successful (else block), print "Conversion successful: {result}"
# - If ValueError, print "Cannot convert to integer"
# - Returns the integer or None

# Your code here:


# Test your function:
# convert_to_int("42")
# convert_to_int("abc")
# convert_to_int("100")

print("-" * 50)


# Exercise 1.4: Try/Except/Finally
# ================================
# TODO: Create a function read_file_lines(filename) that:
# - Opens and reads the file
# - Returns the number of lines
# - Uses finally to print "File operation complete"
# - Handles FileNotFoundError

# Your code here:


# Test your function:
# read_file_lines("existing_file.txt")
# read_file_lines("nonexistent.txt")

print("-" * 50)


# Exercise 1.5: Dictionary Access
# ===============================
# TODO: Create a function get_user_email(users, user_id) that:
# - Gets user email from users dictionary
# - Handles KeyError if user_id not found
# - Returns the email or "User not found"

# Your code here:


# Test your function:
# users = {
#     "user1": {"email": "user1@example.com"},
#     "user2": {"email": "user2@example.com"}
# }
# print(get_user_email(users, "user1"))
# print(get_user_email(users, "user999"))

print("-" * 50)


# Exercise 1.6: String to Number Validation
# =========================================
# TODO: Create a function validate_age(age_str) that:
# - Converts age_str to int
# - Raises ValueError if age < 0 or age > 150
# - Returns True if valid
# - Handles ValueError with appropriate message

# Your code here:


# Test your function:
# validate_age("25")
# validate_age("abc")
# validate_age("-5")
# validate_age("200")

print("-" * 50)


# Exercise 1.7: List Operations
# =============================
# TODO: Create a function safe_pop(lst, index=None) that:
# - Safely removes and returns item from list
# - Uses pop() with optional index
# - Handles IndexError
# - Returns None if error occurs

# Your code here:


# Test your function:
# numbers = [1, 2, 3, 4, 5]
# print(safe_pop(numbers))  # Remove last
# print(safe_pop(numbers, 0))  # Remove first
# print(safe_pop(numbers, 100))  # Handle error

print("-" * 50)


# Exercise 1.8: Nested Try/Except
# ===============================
# TODO: Create a function process_user_age(data) that:
# - Accesses data['user']['age']
# - Converts age to int
# - Handles KeyError (missing keys)
# - Handles ValueError (invalid age format)
# - Returns the age or None

# Your code here:


# Test your function:
# test_data = [
#     {"user": {"age": "25"}},  # Valid
#     {"user": {"name": "Bob"}},  # Missing age
#     {"user": {"age": "twenty"}},  # Invalid format
#     {"name": "Charlie"}  # Missing user
# ]
# for data in test_data:
#     print(process_user_age(data))

print("-" * 50)


# BONUS: Custom Exception
# ======================
# TODO: Create a custom exception InvalidCredentialsError
# Create a function validate_login(username, password) that:
# - Raises InvalidCredentialsError if username or password is empty
# - Raises InvalidCredentialsError if password < 6 characters
# - Returns True if valid

# Your code here:


# Test your function:
# try:
#     validate_login("testuser", "password123")
#     validate_login("", "password")
# except InvalidCredentialsError as e:
#     print(f"Login validation failed: {e}")

print("-" * 50)

print("=" * 50)
print("Exercise 1 Complete!")
print("Check SOLUTIONS.md for answers")
print("=" * 50)
