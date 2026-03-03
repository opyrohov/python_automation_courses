"""
Lecture 5 - Exercise 3: Playwright Helper Functions
==================================================
Practice creating reusable automation helper functions.

Instructions:
1. Complete each TODO section
2. These are conceptual exercises (no actual browser automation)
3. Focus on function design and organization
4. Test your code by running: python exercise_03_playwright_helpers.py
5. Check your solutions against SOLUTIONS.md
"""

# Exercise 3.1: Create a Click Helper
# ===================================
# TODO: Create a function called 'click_element' that:
# - Takes selector as parameter
# - Prints: "Clicking element: [selector]"
# - Returns True
# Test with: "#submit-button"

# Your code here:


print("-" * 50)


# Exercise 3.2: Create a Fill Field Helper
# ========================================
# TODO: Create a function called 'fill_input' that:
# - Takes selector and value as parameters
# - Prints: "Filling [selector] with: [value]"
# - Returns True
# Test with: ("#email", "test@example.com")

# Your code here:


print("-" * 50)


# Exercise 3.3: Create a Navigation Helper
# ========================================
# TODO: Create a function called 'navigate' that:
# - Takes url parameter
# - Takes optional timeout parameter (default 30)
# - Prints: "Navigating to [url] (timeout: [timeout]s)"
# - Returns True
# Test with and without timeout

# Your code here:


print("-" * 50)


# Exercise 3.4: Create a Login Function
# =====================================
# TODO: Create a function called 'login_user' that:
# - Takes username and password
# - Takes optional remember_me (default False)
# - Simulates: filling username, password, optionally checking remember me, clicking login
# - Returns True if successful
# Test with different parameters

# Your code here:


print("-" * 50)


# Exercise 3.5: Create a Verification Helper
# ==========================================
# TODO: Create a function called 'verify_text_on_page' that:
# - Takes expected_text parameter
# - Simulates checking if text exists on page
# - Returns True if found, False otherwise
# - Prints appropriate message
# Test with: "Welcome to Dashboard"

# Your code here:


print("-" * 50)


# Exercise 3.6: Create a Form Fill Helper
# =======================================
# TODO: Create a function called 'fill_registration_form' that:
# - Takes: first_name, last_name, email, password
# - Takes optional: phone (default None), country (default "USA")
# - Simulates filling each field
# - Returns a dictionary with all filled values
# Test with complete and partial data

# Your code here:


print("-" * 50)


# Exercise 3.7: Create a Wait Helper
# ==================================
# TODO: Create a function called 'wait_for_element' that:
# - Takes selector and optional timeout (default 10)
# - Prints: "Waiting up to [timeout]s for: [selector]"
# - Simulates waiting
# - Returns True
# Test with different timeouts

# Your code here:


print("-" * 50)


# Exercise 3.8: Create a Screenshot Helper
# ========================================
# TODO: Create a function called 'capture_screenshot' that:
# - Takes screenshot_name
# - Takes optional path (default "screenshots/")
# - Prints: "Saving screenshot: [path][screenshot_name].png"
# - Returns the full file path
# Test with: "login_page"

# Your code here:


print("-" * 50)


# Exercise 3.9: Create a Multi-Step Test Function
# ===============================================
# TODO: Create a function called 'test_user_registration' that:
# - Uses the helper functions you created above
# - Simulates a complete registration flow:
#   1. Navigate to registration page
#   2. Fill registration form
#   3. Click submit button
#   4. Wait for success message
#   5. Verify success text
#   6. Take screenshot
# - Returns True if all steps succeed
# Run the complete test

# Your code here:


print("-" * 50)


# Exercise 3.10: Create a Data-Driven Test Helper
# ===============================================
# TODO: Create a function called 'run_login_tests' that:
# - Takes a list of test_data dictionaries
# - Each dictionary has: username, password, expected_result
# - For each test case:
#   - Print test case number
#   - Call login_user with the credentials
#   - Print expected vs actual result
# - Return summary: {"passed": count, "failed": count}
# Test with sample data

# Your code here:


# Sample test data:
test_data = [
    {"username": "valid@test.com", "password": "Pass123", "expected": "success"},
    {"username": "invalid@test.com", "password": "wrong", "expected": "failure"},
    {"username": "admin@test.com", "password": "Admin456", "expected": "success"}
]

print("-" * 50)


# Exercise 3.11: Create a Test Reporter
# =====================================
# TODO: Create a function called 'generate_test_report' that:
# - Takes test_name, test_results (dict with passed/failed/skipped counts)
# - Takes optional timestamp (default None)
# - Prints a formatted report with:
#   - Test name
#   - Timestamp (if provided)
#   - Passed count (green checkmark)
#   - Failed count (red X)
#   - Total count
#   - Success percentage
# - Returns the success percentage
# Test with sample results

# Your code here:


print("-" * 50)


# Exercise 3.12: Create a Page Object Helper
# ==========================================
# TODO: Create a function called 'create_login_page_helpers' that:
# - Returns a dictionary of helper functions for login page
# - Dictionary keys: "enter_username", "enter_password", "click_login", "get_error_message"
# - Each value is a lambda function that prints what it does
# - Test by calling each helper from the returned dictionary

# Your code here:


print("-" * 50)


# BONUS Exercise: Create a Test Retry Mechanism
# =============================================
# TODO: Create a function called 'retry_test' that:
# - Takes test_function, max_attempts (default 3)
# - Takes **kwargs to pass to test_function
# - Tries to run test_function up to max_attempts times
# - If test_function returns True, stop and return True
# - If all attempts fail, return False
# - Print attempt number and result each time
# Create a sample flaky_test function that fails twice then succeeds
# Test the retry mechanism

# Your code here:


print("=" * 50)
print("Exercise 3 Complete!")
print("You've created a library of reusable automation helpers!")
print("Compare your solutions with SOLUTIONS.md")
print("=" * 50)
