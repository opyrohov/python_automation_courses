"""
Lecture 2: Playwright Automation Examples
This file demonstrates how strings and control flow are used in web automation scenarios.
Note: These are conceptual examples showing the logic - actual Playwright code comes later.
"""

# ============================================
# EXAMPLE 1: CHECKING PAGE TITLE
# ============================================
print("=== Example 1: Page Title Validation ===")

# Simulating getting page title from a web page
current_page_title = "Login - My Application"
expected_title = "Login - My Application"

print(f"Current page title: '{current_page_title}'")
print(f"Expected title: '{expected_title}'")

if current_page_title == expected_title:
    print("✓ Page title is correct")
else:
    print("✗ Page title mismatch")

# Flexible matching - check if title contains keyword
if "Login" in current_page_title:
    print("✓ Page contains 'Login' keyword")

print()

# ============================================
# EXAMPLE 2: VERIFYING TEXT ON PAGE
# ============================================
print("=== Example 2: Text Verification ===")

# Simulating text content from a web page
welcome_message = "Welcome back, John Doe!"
expected_user = "John Doe"

print(f"Welcome message: '{welcome_message}'")

if expected_user in welcome_message:
    print(f"✓ User '{expected_user}' is logged in")
else:
    print(f"✗ User '{expected_user}' not found in welcome message")

# Extract username from message
if "Welcome back," in welcome_message:
    username = welcome_message.replace("Welcome back,", "").strip().replace("!", "")
    print(f"Extracted username: '{username}'")

print()

# ============================================
# EXAMPLE 3: CONDITIONAL BUTTON CLICKING
# ============================================
print("=== Example 3: Conditional Actions ===")

# Simulating button state
is_button_visible = True
is_button_enabled = True
button_text = "Submit"

print(f"Button visible: {is_button_visible}")
print(f"Button enabled: {is_button_enabled}")
print(f"Button text: '{button_text}'")

if is_button_visible and is_button_enabled:
    print("✓ Button is clickable")
    if button_text == "Submit":
        print("→ Clicking Submit button")
    elif button_text == "Cancel":
        print("→ Clicking Cancel button")
else:
    if not is_button_visible:
        print("✗ Button is not visible")
    if not is_button_enabled:
        print("✗ Button is disabled")

print()

# ============================================
# EXAMPLE 4: FORM VALIDATION
# ============================================
print("=== Example 4: Form Input Validation ===")

# Simulating form inputs
email_input = "user@example.com"
password_input = "SecurePass123"
terms_accepted = True

print("Validating form inputs...")

# Email validation
if "@" in email_input and "." in email_input:
    print(f"✓ Email format is valid: {email_input}")
else:
    print(f"✗ Invalid email format: {email_input}")

# Password validation
if len(password_input) >= 8:
    print(f"✓ Password meets length requirement")
else:
    print(f"✗ Password too short (minimum 8 characters)")

# Terms acceptance
if terms_accepted:
    print("✓ Terms and conditions accepted")
else:
    print("✗ Must accept terms and conditions")

# Overall form validation
if (
    "@" in email_input and
    "." in email_input and
    len(password_input) >= 8 and
    terms_accepted
):
    print("\n→ Form is valid - ready to submit")
else:
    print("\n✗ Form has validation errors - cannot submit")

print()

# ============================================
# EXAMPLE 5: ERROR MESSAGE HANDLING
# ============================================
print("=== Example 5: Error Message Handling ===")

# Simulating different error scenarios
error_message = "Invalid username or password"

print(f"Error message: '{error_message}'")

if "Invalid username" in error_message.lower():
    print("→ Login failed due to invalid credentials")
    print("→ Action: Retry with correct credentials")
elif "account locked" in error_message.lower():
    print("→ Account is locked")
    print("→ Action: Contact support")
elif "network error" in error_message.lower():
    print("→ Network issue detected")
    print("→ Action: Check connection and retry")
else:
    print("→ Unknown error")
    print(f"→ Error details: {error_message}")

print()

# ============================================
# EXAMPLE 6: DYNAMIC ELEMENT SELECTION
# ============================================
print("=== Example 6: Dynamic Element Selection ===")

# Simulating different page states
page_state = "logged_in"
user_role = "admin"

print(f"Page state: {page_state}")
print(f"User role: {user_role}")

if page_state == "logged_out":
    print("→ Looking for Login button")
    print("→ Will click: Login")
elif page_state == "logged_in":
    print("→ User is logged in")

    if user_role == "admin":
        print("→ Admin panel should be visible")
        print("→ Will navigate to: Admin Dashboard")
    elif user_role == "user":
        print("→ Regular user view")
        print("→ Will navigate to: User Dashboard")
else:
    print("→ Unknown page state")

print()

# ============================================
# EXAMPLE 7: URL VALIDATION & NAVIGATION
# ============================================
print("=== Example 7: URL Validation ===")

current_url = "https://example.com/dashboard"
expected_url = "https://example.com/dashboard"
base_url = "https://example.com"

print(f"Current URL: {current_url}")
print(f"Expected URL: {expected_url}")

# Exact match
if current_url == expected_url:
    print("✓ URL matches exactly")

# Check if on correct domain
if base_url in current_url:
    print("✓ On correct domain")

# Check specific page
if "/dashboard" in current_url:
    print("✓ On dashboard page")
elif "/login" in current_url:
    print("⚠ On login page - need to authenticate")
elif "/error" in current_url:
    print("✗ Error page detected")

print()

# ============================================
# EXAMPLE 8: ELEMENT COUNT VALIDATION
# ============================================
print("=== Example 8: Element Count Validation ===")

# Simulating counting elements on a page
product_count = 12
expected_min = 1
expected_max = 20

print(f"Products found: {product_count}")
print(f"Expected range: {expected_min}-{expected_max}")

if product_count == 0:
    print("✗ No products found on page")
elif product_count < expected_min:
    print(f"⚠ Too few products ({product_count} < {expected_min})")
elif product_count > expected_max:
    print(f"⚠ Too many products ({product_count} > {expected_max})")
else:
    print(f"✓ Product count is within expected range")

print()

# ============================================
# EXAMPLE 9: WAIT CONDITION LOGIC
# ============================================
print("=== Example 9: Wait Condition Logic ===")

# Simulating element states over time
is_element_visible = False
is_page_loaded = True
timeout_seconds = 5
elapsed_seconds = 3

print(f"Page loaded: {is_page_loaded}")
print(f"Element visible: {is_element_visible}")
print(f"Elapsed time: {elapsed_seconds}s / {timeout_seconds}s")

if is_page_loaded:
    if is_element_visible:
        print("✓ Element is visible - proceed with action")
    else:
        if elapsed_seconds < timeout_seconds:
            print("⏳ Element not visible yet - continue waiting")
        else:
            print("✗ Timeout - element did not appear")
else:
    print("⏳ Waiting for page to load")

print()

# ============================================
# EXAMPLE 10: TEST RESULT REPORTING
# ============================================
print("=== Example 10: Test Result Reporting ===")

test_name = "Login Functionality Test"
test_passed = True
actual_result = "User successfully logged in"
expected_result = "User successfully logged in"

print(f"Test: {test_name}")
print(f"Expected: {expected_result}")
print(f"Actual: {actual_result}")

if test_passed and actual_result == expected_result:
    print("✓ TEST PASSED")
else:
    print("✗ TEST FAILED")
    if actual_result != expected_result:
        print(f"  Mismatch: expected '{expected_result}' but got '{actual_result}'")

print()

# ============================================
# EXAMPLE 11: SEARCH RESULT VALIDATION
# ============================================
print("=== Example 11: Search Result Validation ===")

search_query = "Python Automation"
result_title = "Python Automation Tutorial - Learn Web Testing"
result_count = 15

print(f"Search query: '{search_query}'")
print(f"First result: '{result_title}'")
print(f"Total results: {result_count}")

# Check if search query appears in result
search_words = search_query.split()
matches = 0

for word in search_words:
    if word.lower() in result_title.lower():
        matches += 1

if matches == len(search_words):
    print(f"✓ All search terms found in result")
elif matches > 0:
    print(f"⚠ Partial match: {matches}/{len(search_words)} terms found")
else:
    print("✗ No search terms found in result")

# Check result count
if result_count == 0:
    print("✗ No results found")
elif result_count > 0:
    print(f"✓ Found {result_count} results")

print()

# ============================================
# EXAMPLE 12: STATUS CODE HANDLING
# ============================================
print("=== Example 12: HTTP Status Code Handling ===")

response_status = 200
response_text = "Page loaded successfully"

print(f"Status code: {response_status}")
print(f"Response: {response_text}")

if response_status == 200:
    print("✓ Request successful")
    print("→ Proceeding with test")
elif response_status == 404:
    print("✗ Page not found")
    print("→ Test failed - page does not exist")
elif response_status == 500:
    print("✗ Server error")
    print("→ Test failed - server issue")
elif 300 <= response_status < 400:
    print("⚠ Redirect detected")
    print("→ Following redirect")
elif response_status >= 400:
    print("✗ Client/Server error")
    print(f"→ Test failed with status {response_status}")

print()

print("=" * 50)
print("These examples show the logic used in automation.")
print("In real Playwright code, you'll use these concepts to:")
print("  • Verify text and elements on pages")
print("  • Make decisions based on page state")
print("  • Handle different scenarios dynamically")
print("  • Validate test results")
print("=" * 50)
