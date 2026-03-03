"""
Exercise 3: Playwright Automation Scenarios
Practice using loops in web automation contexts.
Note: These are logic exercises simulating Playwright scenarios.
"""

# ============================================
# EXERCISE 1: Click Multiple Buttons
# ============================================
print("=== Exercise 1: Navigate Through Menu ===")

menu_items = ["Home", "Products", "Services", "About", "Contact"]

# TODO: Simulate clicking each menu item
# Print "Clicking: [item name]" for each one

# Your code here:


print()

# ============================================
# EXERCISE 2: Fill Form Fields
# ============================================
print("=== Exercise 2: Complete Registration Form ===")

# TODO: Create a dictionary with form field names and values for:
# First Name, Last Name, Email, Phone, Address
# Loop through and simulate filling each field
# Print "Filling [field]: [value]"

# Your code here:
form_data = {
    # Add your form fields here
}


print()

# ============================================
# EXERCISE 3: Validate Multiple Elements
# ============================================
print("=== Exercise 3: Check Page Elements ===")

expected_elements = [
    {"type": "heading", "text": "Welcome"},
    {"type": "button", "text": "Sign In"},
    {"type": "button", "text": "Register"},
    {"type": "link", "text": "Forgot Password"}
]

# Simulate some elements being found, some missing
found_elements = ["Welcome", "Sign In", "Register"]

# TODO: Check if each expected element is in found_elements
# Print "✓ Found" or "✗ Missing" for each

# Your code here:


print()

# ============================================
# EXERCISE 4: Process Table Data
# ============================================
print("=== Exercise 4: Extract Product Information ===")

products_table = [
    {"id": 1, "name": "Laptop", "price": 999, "stock": 5},
    {"id": 2, "name": "Mouse", "price": 29, "stock": 50},
    {"id": 3, "name": "Keyboard", "price": 79, "stock": 0},
    {"id": 4, "name": "Monitor", "price": 299, "stock": 10}
]

# TODO: Loop through products and:
# - Print products that are out of stock (stock = 0)
# - Count how many products are available (stock > 0)
# - Find the most expensive product

# Your code here:


print()

# ============================================
# EXERCISE 5: Select Multiple Checkboxes
# ============================================
print("=== Exercise 5: Configure Preferences ===")

preferences = [
    {"id": "news", "label": "Email Newsletter", "default": True},
    {"id": "promo", "label": "Promotional Offers", "default": False},
    {"id": "update", "label": "Product Updates", "default": True},
    {"id": "survey", "label": "Surveys", "default": False}
]

# TODO: Simulate selecting checkboxes
# Select only the ones with default: True
# Print "☑ Selecting: [label]" or "☐ Skipping: [label]"

# Your code here:


print()

# ============================================
# EXERCISE 6: Search and Click Result
# ============================================
print("=== Exercise 6: Find and Click Search Result ===")

search_results = [
    "Python Tutorial for Beginners",
    "JavaScript Basics Guide",
    "Playwright Automation Testing",
    "Selenium WebDriver Tips",
    "Python Automation Tools"
]

target_keyword = "Playwright"

# TODO: Search through results for one containing target_keyword
# When found, print "Clicking on: [result]" and break
# If not found, print "No results found for: [keyword]"

# Your code here:


print()

# ============================================
# EXERCISE 7: Data-Driven Login Tests
# ============================================
print("=== Exercise 7: Run Multiple Login Tests ===")

test_cases = [
    {"username": "valid@user.com", "password": "Pass123!", "should_succeed": True},
    {"username": "invalid@user.com", "password": "wrong", "should_succeed": False},
    {"username": "admin@site.com", "password": "Admin123!", "should_succeed": True}
]

# TODO: For each test case:
# - Print test case number and credentials
# - Simulate login attempt
# - Print "✓ Test passed" if result matches should_succeed
# - Print "✗ Test failed" if result doesn't match

# Your code here:


print()

# ============================================
# EXERCISE 8: Navigate Multiple Pages
# ============================================
print("=== Exercise 8: Crawl Website Pages ===")

pages = [
    {"url": "/home", "title": "Home Page"},
    {"url": "/products", "title": "Products"},
    {"url": "/about", "title": "About Us"},
    {"url": "/contact", "title": "Contact"}
]

# TODO: For each page:
# - Print "Navigating to: [url]"
# - Print "Verifying title: [title]"
# - Print "✓ Page verified"

# Your code here:


print()

# ============================================
# EXERCISE 9: Retry Failed Operations
# ============================================
print("=== Exercise 9: Retry Click with Timeout ===")

element_name = "Submit Button"
max_retries = 5

# Simulate element becoming clickable after 3 attempts
attempts_until_success = 3

# TODO: Implement retry logic
# - Try to click the element
# - If attempt number < attempts_until_success, print "Element not ready, retrying..."
# - If attempt number >= attempts_until_success, print "✓ Successfully clicked"
# - Use break when successful
# - If all retries exhausted, print "✗ Failed to click after [max_retries] attempts"

# Your code here:


print()

# ============================================
# EXERCISE 10: Wait for Element to Disappear
# ============================================
print("=== Exercise 10: Wait for Loading Spinner ===")

# Simulate spinner disappearing after 4 seconds
spinner_disappears_at = 4
max_wait_seconds = 10

# TODO: Use a loop to wait for the spinner to disappear
# - For each second, print "Waiting... [second]s"
# - When second reaches spinner_disappears_at, print "✓ Spinner disappeared"
# - Break when spinner disappears
# - If max_wait_seconds reached, print "⚠ Timeout: Spinner still visible"

# Your code here:


print()

# ============================================
# EXERCISE 11: Scrape Multiple Pages
# ============================================
print("=== Exercise 11: Collect Data from Pagination ===")

# Simulate 3 pages of products
pages_data = [
    ["Product A", "Product B", "Product C"],
    ["Product D", "Product E", "Product F"],
    ["Product G", "Product H"]
]

# TODO: Loop through each page and collect all products
# Print "Page [number]: Found [count] products"
# Create a list with all products
# Print total products collected

# Your code here:
all_products = []


print()

# ============================================
# EXERCISE 12: Validate Navigation Links
# ============================================
print("=== Exercise 12: Check All Links on Page ===")

links = [
    {"text": "Home", "href": "/home", "should_exist": True},
    {"text": "Blog", "href": "/blog", "should_exist": True},
    {"text": "Admin", "href": "/admin", "should_exist": False},
    {"text": "Help", "href": "/help", "should_exist": True}
]

# TODO: Validate each link
# - If should_exist is True, print "✓ Link '[text]' exists"
# - If should_exist is False, print "⚠ Link '[text]' should not be visible!"
# Count how many validation issues found

# Your code here:


print()

# ============================================
# EXERCISE 13: Batch Form Submissions
# ============================================
print("=== Exercise 13: Register Multiple Users ===")

users_to_register = [
    {"name": "Alice Johnson", "email": "alice@example.com", "role": "user"},
    {"name": "Bob Smith", "email": "bob@example.com", "role": "admin"},
    {"name": "Charlie Brown", "email": "charlie@example.com", "role": "user"}
]

# TODO: For each user:
# - Print "Registering user [count]/[total]"
# - Print user details
# - Simulate filling form and submitting
# - Print "✓ User registered successfully"

# Your code here:


print()

# ============================================
# EXERCISE 14: Filter and Click Elements
# ============================================
print("=== Exercise 14: Click Only Enabled Buttons ===")

buttons = [
    {"id": "save", "text": "Save", "enabled": True},
    {"id": "delete", "text": "Delete", "enabled": False},
    {"id": "edit", "text": "Edit", "enabled": True},
    {"id": "cancel", "text": "Cancel", "enabled": True},
    {"id": "submit", "text": "Submit", "enabled": False}
]

# TODO: Click only enabled buttons
# Use continue to skip disabled buttons
# Print "Clicking: [text]" for enabled buttons
# Print "Skipping disabled: [text]" for disabled buttons
# Count how many buttons were clicked

# Your code here:


print()

# ============================================
# EXERCISE 15: Validate Form Error Messages
# ============================================
print("=== Exercise 15: Check Form Validation ===")

# Simulate submitting form with invalid data
validation_errors = [
    {"field": "email", "message": "Invalid email format"},
    {"field": "password", "message": "Password too short"},
    {"field": "age", "message": "Must be 18 or older"}
]

expected_errors = ["email", "password", "age", "phone"]

# TODO: Check if all expected error fields have validation messages
# Print each error found
# Print which expected errors are missing

# Your code here:


print()

# ============================================
# BONUS CHALLENGE: Complete E2E Test
# ============================================
print("=== BONUS: End-to-End Shopping Test ===")

# Simulate complete shopping flow
products_to_add = [
    {"name": "Laptop", "quantity": 1, "price": 999},
    {"name": "Mouse", "quantity": 2, "price": 29},
    {"name": "Keyboard", "quantity": 1, "price": 79}
]

shipping_info = {
    "name": "John Doe",
    "address": "123 Main St",
    "city": "New York",
    "zip": "10001"
}

# TODO: Simulate complete checkout process:
# 1. Loop through products and add to cart
#    - Print "Adding [quantity]x [name] to cart"
# 2. Calculate total cost
# 3. Print "Cart total: $[total]"
# 4. Loop through shipping_info and fill form
#    - Print "Filling [field]: [value]"
# 5. Print "✓ Order completed successfully"

# Your code here:


print()

print("=" * 50)
print("Outstanding work on automation scenarios!")
print("These patterns will be essential when you")
print("start writing real Playwright tests!")
print("Check SOLUTIONS.md to see the answers")
print("=" * 50)
