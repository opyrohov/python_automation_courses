"""
Lecture 5 - Example 5: Playwright Automation Examples
====================================================
Practical examples of using functions in test automation.
"""

# NOTE: These are simplified examples showing the concepts.
# Real Playwright code would use actual browser automation.

# 1. REUSABLE LOGIN FUNCTION
# ==========================

def login(username, password, remember_me=False):
    """
    Reusable login function for tests.

    Args:
        username: User's email or username
        password: User's password
        remember_me: Whether to check 'Remember Me' (default: False)

    Returns:
        bool: True if login successful
    """
    print(f"🔐 Logging in as: {username}")
    print(f"   Password: {'*' * len(password)}")

    # Simulate filling form
    print("   Filling username field...")
    print("   Filling password field...")

    if remember_me:
        print("   Checking 'Remember Me'...")

    print("   Clicking 'Login' button...")
    print("   ✅ Login successful!")
    return True

# Usage
print("Test 1: Basic Login")
login("testuser@example.com", "SecurePass123")

print("\n" + "-" * 50 + "\n")

print("Test 2: Login with Remember Me")
login("admin@example.com", "AdminPass456", remember_me=True)

print("\n" + "=" * 50 + "\n")


# 2. NAVIGATION HELPER FUNCTIONS
# ==============================

def navigate_to(url, wait_for_load=True, timeout=30):
    """
    Navigate to a URL with options.

    Args:
        url: The URL to navigate to
        wait_for_load: Wait for page load event (default: True)
        timeout: Maximum wait time in seconds (default: 30)

    Returns:
        bool: True if navigation successful
    """
    print(f"🌐 Navigating to: {url}")
    print(f"   Timeout: {timeout}s")

    if wait_for_load:
        print("   Waiting for page load...")

    print("   ✅ Navigation complete!")
    return True

def go_back():
    """Navigate back in browser history."""
    print("⬅️  Going back...")
    return True

def refresh_page():
    """Refresh the current page."""
    print("🔄 Refreshing page...")
    return True

# Usage
print("Navigation Test:")
navigate_to("https://example.com/login")
navigate_to("https://example.com/dashboard", timeout=10)
go_back()
refresh_page()

print("\n" + "=" * 50 + "\n")


# 3. ELEMENT INTERACTION HELPERS
# ==============================

def click_element(selector, wait_for_visible=True):
    """
    Click an element with optional wait.

    Args:
        selector: CSS selector or element identifier
        wait_for_visible: Wait for element to be visible (default: True)

    Returns:
        bool: True if click successful
    """
    print(f"🖱️  Clicking element: {selector}")

    if wait_for_visible:
        print("   Waiting for element to be visible...")

    print("   Element clicked!")
    return True

def fill_field(selector, value, clear_first=True):
    """
    Fill a form field with a value.

    Args:
        selector: Field selector
        value: Value to enter
        clear_first: Clear field before filling (default: True)

    Returns:
        bool: True if fill successful
    """
    print(f"⌨️  Filling field: {selector}")

    if clear_first:
        print("   Clearing field first...")

    print(f"   Entering: {value}")
    return True

def select_dropdown(selector, option):
    """
    Select an option from a dropdown.

    Args:
        selector: Dropdown selector
        option: Option to select

    Returns:
        bool: True if selection successful
    """
    print(f"📋 Selecting from dropdown: {selector}")
    print(f"   Option: {option}")
    return True

# Usage
print("Element Interaction Test:")
click_element("#submit-button")
fill_field("#email", "test@example.com")
fill_field("#phone", "555-1234", clear_first=False)
select_dropdown("#country", "United States")

print("\n" + "=" * 50 + "\n")


# 4. FORM FILLING FUNCTION
# ========================

def fill_form(form_data, submit=True):
    """
    Fill a form with dictionary of field data.

    Args:
        form_data: Dictionary of {field_selector: value}
        submit: Whether to submit form after filling (default: True)

    Returns:
        bool: True if successful
    """
    print("📝 Filling form...")

    for field, value in form_data.items():
        print(f"   {field}: {value}")

    if submit:
        print("   Submitting form...")
        print("   ✅ Form submitted!")

    return True

# Usage
print("Form Fill Test:")
user_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "555-1234",
    "address": "123 Main St"
}
fill_form(user_data)

print("\n" + "=" * 50 + "\n")


# 5. VERIFICATION/ASSERTION HELPERS
# =================================

def verify_text_present(text, case_sensitive=True):
    """
    Verify text is present on the page.

    Args:
        text: Text to search for
        case_sensitive: Whether search is case-sensitive (default: True)

    Returns:
        bool: True if text found
    """
    print(f"🔍 Verifying text: '{text}'")

    if not case_sensitive:
        print("   (Case-insensitive)")

    print("   ✅ Text found!")
    return True

def verify_element_visible(selector):
    """
    Verify element is visible on the page.

    Args:
        selector: Element selector

    Returns:
        bool: True if element visible
    """
    print(f"👁️  Verifying element visible: {selector}")
    print("   ✅ Element is visible!")
    return True

def verify_url_contains(expected_url):
    """
    Verify current URL contains expected string.

    Args:
        expected_url: Expected URL substring

    Returns:
        bool: True if URL matches
    """
    current_url = "https://example.com/dashboard"
    print(f"🔗 Verifying URL contains: {expected_url}")
    print(f"   Current URL: {current_url}")

    if expected_url in current_url:
        print("   ✅ URL verification passed!")
        return True
    else:
        print("   ❌ URL verification failed!")
        return False

# Usage
print("Verification Test:")
verify_text_present("Welcome")
verify_element_visible("#nav-menu")
verify_url_contains("/dashboard")

print("\n" + "=" * 50 + "\n")


# 6. WAIT HELPER FUNCTIONS
# ========================

def wait_for_element(selector, timeout=10):
    """
    Wait for element to appear.

    Args:
        selector: Element selector
        timeout: Maximum wait time in seconds (default: 10)

    Returns:
        bool: True if element appeared
    """
    print(f"⏳ Waiting for element: {selector}")
    print(f"   Timeout: {timeout}s")
    print("   ✅ Element appeared!")
    return True

def wait_for_text(text, timeout=10):
    """
    Wait for specific text to appear.

    Args:
        text: Text to wait for
        timeout: Maximum wait time in seconds (default: 10)

    Returns:
        bool: True if text appeared
    """
    print(f"⏳ Waiting for text: '{text}'")
    print(f"   Timeout: {timeout}s")
    print("   ✅ Text appeared!")
    return True

# Usage
print("Wait Test:")
wait_for_element("#loading-spinner", timeout=5)
wait_for_text("Data loaded successfully", timeout=15)

print("\n" + "=" * 50 + "\n")


# 7. SCREENSHOT/REPORTING HELPERS
# ===============================

def take_screenshot(name, full_page=False):
    """
    Take a screenshot of the page.

    Args:
        name: Screenshot filename
        full_page: Capture full page or viewport (default: False)

    Returns:
        str: Screenshot file path
    """
    screenshot_path = f"screenshots/{name}.png"
    print(f"📸 Taking screenshot: {name}")

    if full_page:
        print("   Mode: Full page")
    else:
        print("   Mode: Viewport only")

    print(f"   Saved to: {screenshot_path}")
    return screenshot_path

def log_test_step(step_description, status="info"):
    """
    Log a test step with status.

    Args:
        step_description: Description of the step
        status: Status level (info/success/error)
    """
    icons = {
        "info": "ℹ️ ",
        "success": "✅",
        "error": "❌"
    }

    icon = icons.get(status, "ℹ️ ")
    print(f"{icon} {step_description}")

# Usage
print("Screenshot and Logging Test:")
take_screenshot("login_page")
take_screenshot("full_dashboard", full_page=True)

log_test_step("Starting login test", "info")
log_test_step("Login successful", "success")
log_test_step("Navigation error occurred", "error")

print("\n" + "=" * 50 + "\n")


# 8. DATA-DRIVEN TEST HELPER
# ==========================

def run_test_with_data(test_name, test_data_list, test_function):
    """
    Run a test with multiple sets of data.

    Args:
        test_name: Name of the test
        test_data_list: List of test data dictionaries
        test_function: Function to execute for each data set

    Returns:
        dict: Test results summary
    """
    print(f"🧪 Running Data-Driven Test: {test_name}\n")

    passed = 0
    failed = 0

    for i, data in enumerate(test_data_list, 1):
        print(f"Test Case {i}:")
        try:
            test_function(data)
            print("   ✅ Passed")
            passed += 1
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            failed += 1
        print()

    print(f"Results: {passed} passed, {failed} failed")
    return {"passed": passed, "failed": failed, "total": passed + failed}

# Example test function
def test_login_with_data(data):
    """Test login with given data."""
    print(f"   Username: {data['username']}")
    print(f"   Password: {data['password']}")
    print(f"   Expected: {data['expected_result']}")

    # Simulate login
    if data['expected_result'] == 'success':
        print("   Login succeeded")
    else:
        raise Exception("Login failed as expected")

# Test data
login_test_data = [
    {"username": "valid@test.com", "password": "Pass123!", "expected_result": "success"},
    {"username": "invalid@test.com", "password": "wrong", "expected_result": "failure"},
    {"username": "admin@test.com", "password": "Admin456!", "expected_result": "success"}
]

# Run data-driven test
results = run_test_with_data("Login Test", login_test_data, test_login_with_data)

print("\n" + "=" * 50 + "\n")


# 9. COMPLETE TEST EXAMPLE
# ========================

def complete_login_test():
    """Complete test combining multiple helper functions."""
    print("🧪 Running Complete Login Test\n")

    # Step 1: Navigate
    log_test_step("Navigating to login page", "info")
    navigate_to("https://example.com/login")
    take_screenshot("01_login_page")

    # Step 2: Fill form
    log_test_step("Filling login form", "info")
    fill_field("#username", "testuser@example.com")
    fill_field("#password", "SecurePass123")

    # Step 3: Submit
    log_test_step("Submitting form", "info")
    click_element("#login-button")

    # Step 4: Wait for dashboard
    log_test_step("Waiting for dashboard", "info")
    wait_for_text("Welcome", timeout=10)

    # Step 5: Verify
    log_test_step("Verifying successful login", "info")
    verify_url_contains("/dashboard")
    verify_element_visible("#user-menu")
    take_screenshot("02_dashboard")

    log_test_step("Test completed successfully", "success")
    return True

# Run the complete test
complete_login_test()

print("\n" + "=" * 50)
print("Example complete! You've learned Playwright automation with functions.")
print("=" * 50)
