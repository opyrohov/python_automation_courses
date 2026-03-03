"""
Exercise 3: Playwright Automation Scenarios
Apply string manipulation and control flow to web automation scenarios.
Note: These are conceptual exercises - actual Playwright code comes in later lectures.
"""

# ============================================
# EXERCISE 1: Login Flow
# ============================================
print("Exercise 1: Login Flow Validation")
print("-" * 40)

# Simulate page state after login attempt
current_url = "https://example.com/dashboard"
page_title = "Dashboard - Welcome"
username_displayed = "John Doe"

# TODO: Validate successful login by checking:
# 1. URL contains "dashboard"
# 2. Page title contains "Dashboard"
# 3. Username is displayed
# Print validation results


print()

# ============================================
# EXERCISE 2: Error Message Handler
# ============================================
print("Exercise 2: Error Message Handler")
print("-" * 40)

# Different error messages that might appear
error_message = "Error: Invalid email format"
# Try also: "Error: Password is required"
# Try also: "Error: Account not found"
# Try also: "Network connection error"

# TODO: Handle different error types:
# - If contains "email": Print "Fix email format and retry"
# - If contains "password": Print "Enter a valid password"
# - If contains "account": Print "Check username or register"
# - If contains "network": Print "Check internet connection"
# - Otherwise: Print "Unknown error - contact support"


print()

# ============================================
# EXERCISE 3: Search Results Validation
# ============================================
print("Exercise 3: Search Results Validation")
print("-" * 40)

search_term = "Python Automation"
result_count = 25
first_result_title = "Learn Python Automation Testing"
first_result_url = "https://example.com/python-automation"

# TODO: Validate search results:
# 1. Check if result_count > 0
# 2. Check if search_term words appear in first_result_title (case-insensitive)
# 3. Check if first_result_url contains search terms (replace spaces with hyphens)
# Print validation results


print()

# ============================================
# EXERCISE 4: Form Field Validator
# ============================================
print("Exercise 4: Form Field Validator")
print("-" * 40)

# Form field values
email = "user@example.com"
phone = "123-456-7890"
age = "25"
website = "https://example.com"

# TODO: Validate each field:
# email: Must contain @ and .
# phone: Must be 12 characters long (including dashes)
# age: Must be a number and >= 18
# website: Must start with http:// or https://
# Print whether each field is valid or invalid


print()

# ============================================
# EXERCISE 5: Navigation Validator
# ============================================
print("Exercise 5: Navigation Validator")
print("-" * 40)

current_page = "home"
expected_pages = ["home", "products", "cart", "checkout", "confirmation"]

# TODO: Validate navigation flow:
# Check if current_page is in expected_pages
# Determine what the next page should be
# Print the expected navigation path


print()

# ============================================
# EXERCISE 6: Element State Checker
# ============================================
print("Exercise 6: Element State Checker")
print("-" * 40)

button_visible = True
button_enabled = False
button_text = "Submit Order"
form_valid = False

# TODO: Determine if action can proceed:
# Button should be clicked only if:
# - visible AND enabled AND form_valid
# Print why action cannot proceed if conditions aren't met


print()

# ============================================
# EXERCISE 7: Price Comparison
# ============================================
print("Exercise 7: Price Comparison")
print("-" * 40)

# Product prices scraped from website
original_price_text = "$99.99"
sale_price_text = "$79.99"

# TODO: Compare prices:
# 1. Extract numeric values from price strings (remove $)
# 2. Calculate discount amount and percentage
# 3. Check if discount is more than 15%
# 4. Print whether it's a good deal


print()

# ============================================
# EXERCISE 8: Shopping Cart Validator
# ============================================
print("Exercise 8: Shopping Cart Validator")
print("-" * 40)

cart_items = 3
expected_items = 3
cart_total_text = "Total: $145.97"
expected_total = 145.97

# TODO: Validate shopping cart:
# 1. Check if cart_items matches expected_items
# 2. Extract total from cart_total_text
# 3. Compare with expected_total
# 4. Print validation results


print()

# ============================================
# EXERCISE 9: Page Load Status
# ============================================
print("Exercise 9: Page Load Status Checker")
print("-" * 40)

page_loaded = True
required_element_visible = False
page_title = "Loading..."
wait_time = 3
max_wait = 5

# TODO: Determine page status:
# Check different scenarios:
# - If page not loaded: "Still loading..."
# - If loaded but element not visible and wait_time < max_wait: "Waiting for element..."
# - If loaded but element not visible and wait_time >= max_wait: "Timeout error"
# - If loaded and element visible: "Page ready"


print()

# ============================================
# EXERCISE 10: Test Result Reporter
# ============================================
print("Exercise 10: Test Result Reporter")
print("-" * 40)

test_name = "User Login Test"
expected_result = "Login successful"
actual_result = "Login successful"
execution_time = 2.5  # seconds

# TODO: Generate test report:
# 1. Compare expected_result with actual_result
# 2. Check if execution_time > 3 seconds (performance warning)
# 3. Print formatted test report with:
#    - Test name
#    - Status (PASS/FAIL)
#    - Execution time
#    - Performance warning if applicable


print()

# ============================================
# BONUS CHALLENGE: Multi-Step Form Wizard
# ============================================
print("BONUS: Multi-Step Form Wizard")
print("-" * 40)

current_step = 2
total_steps = 4
step_titles = ["Personal Info", "Address", "Payment", "Confirmation"]
completed_steps = [1]
current_step_valid = True

# TODO: Implement form wizard logic:
# 1. Print current step: "Step 2 of 4: Address"
# 2. Check if previous steps are completed
# 3. Determine if user can proceed to next step
# 4. Print next action: "Complete current step" or "Proceed to [next step]"
# 5. Calculate progress percentage


print()

print("=" * 40)
print("Amazing! Check SOLUTIONS.md for answers.")
print("=" * 40)
