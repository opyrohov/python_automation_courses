"""
Lecture 10 - Exercise 3: Organizing Test Code
=============================================
Practice organizing test code with classes and best practices.
"""

print("=" * 50)
print("EXERCISE: Organizing Test Code")
print("=" * 50)
print()

# Exercise 3.1: Create BaseTest Class
# ===================================
# TODO: Create a BaseTest class with:
# - setup_method() that initializes:
#   - self.base_url
#   - self.page (simulated)
#   - Print "Setup: Test initialized"
# - teardown_method() that:
#   - Prints "Teardown: Test cleanup"
#   - Cleans up resources
# - take_screenshot(name) helper method
# - wait_for_page_load() helper method

# Your code here:


print("-" * 50)


# Exercise 3.2: Create TestLogin Class
# ====================================
# TODO: Create TestLogin class that inherits from BaseTest:
# - setup_method() that:
#   - Calls super().setup_method()
#   - Initializes LoginPage
#   - Sets test credentials
# - test_valid_login() method
# - test_invalid_password() method
# - test_empty_credentials() method
# Each test should print what it's testing

# Your code here:


# Test:
# test = TestLogin()
# test.setup_method()
# test.test_valid_login()
# test.teardown_method()

print("-" * 50)


# Exercise 3.3: Create TestData Class
# ===================================
# TODO: Create a TestData class for managing test data:
# - Class variable VALID_USERS (list of user dictionaries)
# - Class variable INVALID_PASSWORDS (list)
# - get_valid_user(index) method
# - get_invalid_password(index) method
# - generate_random_email() static method
# - generate_test_user() static method

# Your code here:


# Test:
# data = TestData()
# user = data.get_valid_user(0)
# print(f"Test user: {user['email']}")

print("-" * 50)


# Exercise 3.4: Create TestFixtures Class
# =======================================
# TODO: Create TestFixtures class with static methods:
# - create_test_user() - returns user dictionary
# - create_test_product() - returns product dictionary
# - create_test_order() - returns order dictionary
# - cleanup_test_data() - prints cleanup message
# - reset_database() - prints reset message

# Your code here:


print("-" * 50)


# Exercise 3.5: Create Complete Test Class
# ========================================
# TODO: Create TestCheckout class that uses everything:
# - Inherits from BaseTest
# - setup_method() initializes:
#   - Page objects (LoginPage, ProductPage, CheckoutPage)
#   - Test data using TestData
#   - Test fixtures using TestFixtures
# - test_checkout_with_valid_payment() method
# - test_checkout_with_invalid_payment() method
# - teardown_method() that cleans up

# Your code here:


print("-" * 50)


# Exercise 3.6: Create Test Suite with setup_class
# ================================================
# TODO: Create TestUserManagement class with:
# - setup_class() class method that runs once before all tests
# - teardown_class() class method that runs once after all tests
# - setup_method() that runs before each test
# - teardown_method() that runs after each test
# - test_create_user()
# - test_update_user()
# - test_delete_user()

# Your code here:


# Test the lifecycle:
# TestUserManagement.setup_class()
# test = TestUserManagement()
# test.setup_method()
# test.test_create_user()
# test.teardown_method()
# TestUserManagement.teardown_class()

print("-" * 50)


# Exercise 3.7: Create Helper Utilities
# =====================================
# TODO: Create utility classes:
#
# 1. StringHelpers class with static methods:
#    - generate_random_string(length)
#    - format_email(name)
#    - clean_text(text)
#
# 2. DateHelpers class with static methods:
#    - get_current_date()
#    - format_date(date, format)
#    - add_days(days)
#
# 3. WaitHelpers class with static methods:
#    - wait_for_condition(condition, timeout)
#    - wait_for_text(text)

# Your code here:


print("-" * 50)


# BONUS Exercise 3.8: Complete Test Organization
# ==============================================
# TODO: Create a complete test organization structure:
#
# 1. BaseTest (base for all tests)
# 2. BasePage (base for all pages)
# 3. LoginPage, HomePage, ProductPage (inherit from BasePage)
# 4. TestLogin, TestProducts (inherit from BaseTest)
# 5. TestData class
# 6. TestFixtures class
# 7. Utilities classes
#
# Then create a run_test_suite() function that:
# - Initializes test classes
# - Runs multiple tests
# - Shows test results
# - Demonstrates the complete organization

# Your code here:


# def run_test_suite():
#     """Run complete test suite."""
#     print("\n" + "=" * 60)
#     print("RUNNING TEST SUITE")
#     print("=" * 60)
#
#     # Your implementation here
#
#     pass
#
# run_test_suite()

print("-" * 50)


# BONUS Exercise 3.9: Test Report Class
# =====================================
# TODO: Create a TestReport class that tracks test results:
# - __init__() initializes counters
# - add_pass(test_name) method
# - add_fail(test_name, reason) method
# - add_skip(test_name) method
# - print_summary() method that shows:
#   - Total tests run
#   - Passed count
#   - Failed count
#   - Skipped count
#   - Pass percentage

# Your code here:


# Test:
# report = TestReport()
# report.add_pass("test_login")
# report.add_pass("test_logout")
# report.add_fail("test_checkout", "Payment gateway error")
# report.print_summary()

print("-" * 50)

print("=" * 50)
print("Exercise 3 Complete!")
print("You've mastered test organization!")
print("Check SOLUTIONS.md for complete implementations")
print("=" * 50)
