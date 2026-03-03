"""
Exercise 3: Playwright Automation Scenarios
Practice using lists and dictionaries in realistic test automation scenarios.
"""

# ============================================
# EXERCISE 1: Store Multiple Test URLs
# ============================================
print("=== Exercise 1: Test Multiple URLs ===")
# TODO: Create a list of 5 test URLs (can be fake/example URLs)
# TODO: Loop through the URLs and print each one with "Testing: {url}"

# Your code here:


print()

# ============================================
# EXERCISE 2: Test User Credentials
# ============================================
print("=== Exercise 2: User Credentials ===")
# TODO: Create a dictionary with login credentials:
# - username
# - password
# - email
# TODO: Print a message: "Logging in as {username} with password {password}"

# Your code here:


print()

# ============================================
# EXERCISE 3: Multiple Locators
# ============================================
print("=== Exercise 3: Multiple Locators ===")
# TODO: Create a list of CSS selectors for different buttons:
# Example: "#submit-btn", ".login-button", "[data-test='register']"
# TODO: Loop through and print "Clicking: {selector}"

# Your code here:


print()

# ============================================
# EXERCISE 4: Form Field Mapping
# ============================================
print("=== Exercise 4: Form Field Mapping ===")
# TODO: Create a dictionary that maps form field IDs to values:
# - "username" -> "testuser"
# - "password" -> "Test123!"
# - "email" -> "test@example.com"
# - "age" -> "25"
# TODO: Loop through the dictionary and print:
# "Fill field '{field}' with '{value}'"

# Your code here:


print()

# ============================================
# EXERCISE 5: Test Configuration
# ============================================
print("=== Exercise 5: Test Configuration ===")
# TODO: Create a config dictionary with:
# - base_url: "https://example.com"
# - timeout: 5000
# - headless: True
# - viewport: {"width": 1920, "height": 1080}
# TODO: Print the base_url
# TODO: Print the viewport width

# Your code here:


print()

# ============================================
# EXERCISE 6: Multiple Test Users
# ============================================
print("=== Exercise 6: Multiple Test Users ===")
# TODO: Create a list of 3 user dictionaries, each with:
# - username
# - password
# - role (admin/user/guest)
# TODO: Loop through users and print:
# "Testing login for {username} with role {role}"

# Your code here:


print()

# ============================================
# EXERCISE 7: Expected vs Actual Results
# ============================================
print("=== Exercise 7: Verify Navigation Menu ===")
expected_menu_items = ["Home", "About", "Services", "Contact"]
actual_menu_items = ["Home", "About", "Products", "Contact"]  # Note: "Products" instead of "Services"

# TODO: Compare expected vs actual
# TODO: Print which items match and which don't
# Hint: Loop through expected and check if each item is in actual

# Your code here:


print()

# ============================================
# EXERCISE 8: Test Data for Form
# ============================================
print("=== Exercise 8: Registration Form Data ===")
# TODO: Create a dictionary with registration form data:
# - first_name
# - last_name
# - email
# - phone
# - country
# - agree_to_terms (boolean)
# TODO: Print all fields in format: "Field: {key}, Value: {value}"

# Your code here:


print()

# ============================================
# EXERCISE 9: Page Locators Dictionary
# ============================================
print("=== Exercise 9: Page Object Locators ===")
# TODO: Create a dictionary of locators for a login page:
# - login_button
# - username_field
# - password_field
# - forgot_password_link
# - remember_me_checkbox
# TODO: Print each locator with a description

# Your code here:


print()

# ============================================
# EXERCISE 10: Store Test Results
# ============================================
print("=== Exercise 10: Test Results ===")
# TODO: Create a dictionary to store test results:
# - passed: empty list
# - failed: empty list
# - skipped: empty list
# TODO: Add some test names to each category
# Example: results["passed"].append("test_login")
# TODO: Print summary: "{x} passed, {y} failed, {z} skipped"

# Your code here:


print()

# ============================================
# CHALLENGE: Data-Driven Testing
# ============================================
print("=== CHALLENGE: Data-Driven Login Tests ===")
# TODO: Create a list of test scenarios (dictionaries) with:
# - username
# - password
# - expected_result ("success" or "fail")
# - test_name

# Include at least 4 scenarios:
# 1. Valid credentials -> success
# 2. Invalid username -> fail
# 3. Invalid password -> fail
# 4. Empty credentials -> fail

# TODO: Loop through scenarios and print for each:
# "Test: {test_name}"
# "Input: {username} / {password}"
# "Expected: {expected_result}"
# "---"

# Your code here:


print()

# ============================================
# CHALLENGE: Shopping Cart System
# ============================================
print("=== CHALLENGE: Shopping Cart ===")
# TODO: Create a shopping cart system with:
# - A list of item dictionaries with: name, price, quantity
# - Calculate and print the total cost
# - Print each item with subtotal: "{name} x{quantity} = ${subtotal}"

# Your code here:


print()

# ============================================
# CHALLENGE: Test Environment Configuration
# ============================================
print("=== CHALLENGE: Multi-Environment Config ===")
# TODO: Create a dictionary of environments (dev, staging, prod)
# Each environment should have:
# - url
# - database
# - api_key (can be fake)
# - timeout

# TODO: Create a function (or just code) that:
# - Takes an environment name as input
# - Prints the configuration for that environment

# Your code here:


print()

print("🎉 Amazing! You're ready to use lists and dictionaries in test automation!")
print("💡 Remember: Lists for sequences, Dictionaries for labeled data!")
