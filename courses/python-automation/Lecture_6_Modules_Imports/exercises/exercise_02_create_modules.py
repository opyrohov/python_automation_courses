"""
Lecture 6 - Exercise 2: Creating Your Own Modules
================================================
Practice creating and using your own modules.

Instructions:
1. Complete each TODO section
2. Create the required module files
3. Test your code by running: python exercise_02_create_modules.py
4. Check your solutions against SOLUTIONS.md
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import exercise_modules
parent_dir = Path(__file__).parent
sys.path.insert(0, str(parent_dir))

print("=" * 50)
print("EXERCISE: Creating Your Own Modules")
print("=" * 50)
print()

# Exercise 2.1: Create a Simple Module
# ====================================
# TODO: Create a file called 'string_utils.py' in the exercises folder
# Add these functions to it:
#   - reverse_string(text): Returns the reversed string
#   - capitalize_words(text): Capitalizes each word
#   - count_vowels(text): Counts the number of vowels

# Then import and test your module here:

# Your code here:
# from string_utils import reverse_string, capitalize_words, count_vowels


print("-" * 50)


# Exercise 2.2: Create a Math Utilities Module
# ============================================
# TODO: Create a file called 'math_utils.py' in the exercises folder
# Add these functions to it:
#   - is_even(num): Returns True if number is even
#   - is_prime(num): Returns True if number is prime
#   - factorial(num): Returns factorial of number

# Then import and test your module here:

# Your code here:
# from math_utils import is_even, is_prime, factorial


print("-" * 50)


# Exercise 2.3: Create a Test Data Generator Module
# =================================================
# TODO: Create a file called 'test_data_gen.py' in the exercises folder
# Add these functions to it:
#   - generate_email(): Returns a random test email
#   - generate_username(): Returns a random username
#   - generate_password(): Returns a random password

# Use Python's random module to generate random data

# Then import and test your module here:

# Your code here:
# from test_data_gen import generate_email, generate_username, generate_password


print("-" * 50)


# Exercise 2.4: Understanding __name__
# ====================================
# TODO: In your string_utils.py file, add this at the bottom:
# if __name__ == "__main__":
#     print("Testing string_utils module")
#     print(reverse_string("hello"))

# Run string_utils.py directly and observe the output
# Then import it here and notice it doesn't print the test

print("When you run string_utils.py directly, __name__ is '__main__'")
print("When you import it, __name__ is 'string_utils'")
print()

print("-" * 50)


# Exercise 2.5: Module with Constants
# ===================================
# TODO: Create a file called 'config.py' in the exercises folder
# Add these constants:
#   - BASE_URL = "https://example.com"
#   - DEFAULT_TIMEOUT = 30
#   - TEST_BROWSER = "chrome"
#   - ADMIN_USER = {"username": "admin", "password": "admin123"}

# Import and use the constants here:

# Your code here:
# from config import BASE_URL, DEFAULT_TIMEOUT, TEST_BROWSER, ADMIN_USER


print("-" * 50)


# Exercise 2.6: Import Your Module with Alias
# ===========================================
# TODO: Import your string_utils module with the alias 'su'
# Use it to reverse the string "Playwright"

# Your code here:


print("-" * 50)


# Exercise 2.7: Create a Test Helpers Module
# ==========================================
# TODO: Create a file called 'test_helpers.py' in the exercises folder
# Add these functions:
#   - log_test_step(step_name): Prints "[TEST] {step_name}"
#   - create_test_user(name, email): Returns a dict with name, email, and a random id
#   - verify_status_code(actual, expected): Prints pass/fail message

# Import and test your module here:

# Your code here:
# from test_helpers import log_test_step, create_test_user, verify_status_code


print("-" * 50)


# Exercise 2.8: Organize Related Functions
# ========================================
# TODO: Create a file called 'validators.py' in the exercises folder
# Add these validation functions:
#   - is_valid_email(email): Checks if email contains @ and .
#   - is_strong_password(password): Checks if password is at least 8 chars
#   - is_valid_phone(phone): Checks if phone has at least 10 digits

# Import and test your validators:

# Your code here:
# from validators import is_valid_email, is_strong_password, is_valid_phone


print("-" * 50)


# BONUS Exercise: Create a Package
# ================================
# TODO: Create a folder called 'my_test_utils' in the exercises folder
# Inside it, create:
#   - __init__.py (with some imports)
#   - data_generators.py (with generate_test_data function)
#   - assertions.py (with custom assertion functions)

# Import from your package:

# Your code here:
# from my_test_utils import data_generators
# from my_test_utils.assertions import assert_contains


print("=" * 50)
print("Exercise 2 Complete!")
print("You've created your own modules!")
print("Compare your solutions with SOLUTIONS.md")
print("=" * 50)
