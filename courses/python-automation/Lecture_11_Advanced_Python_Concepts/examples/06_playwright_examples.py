"""
Lecture 11: Playwright Practical Examples
This file demonstrates how to apply advanced Python concepts in test automation.

Note: These are conceptual examples showing patterns you'll use with Playwright.
Actual Playwright implementation will be covered in later lectures.
"""

from datetime import datetime, timedelta
import functools
import time

# ============================================
# COMPREHENSIONS IN TESTING
# ============================================
print("=" * 60)
print("COMPREHENSIONS IN TESTING")
print("=" * 60)

# Example 1: Filter test data
all_test_users = [
    {"name": "user1", "role": "admin", "active": True},
    {"name": "user2", "role": "user", "active": True},
    {"name": "user3", "role": "admin", "active": False},
    {"name": "user4", "role": "user", "active": True},
]

# Get only active admin users
active_admins = [user for user in all_test_users
                 if user["role"] == "admin" and user["active"]]
print("All test users:", len(all_test_users))
print("Active admins:", active_admins)
print()

# Example 2: Generate test locators
button_ids = ["submit", "cancel", "delete", "save"]
button_selectors = [f"button#{btn_id}" for btn_id in button_ids]
print("Button selectors:", button_selectors)
print()

# Example 3: Transform test results
test_results = [
    {"name": "test_login", "status": "passed", "duration": 2.5},
    {"name": "test_logout", "status": "failed", "duration": 1.2},
    {"name": "test_register", "status": "passed", "duration": 3.1},
]

# Get only failed test names
failed_tests = [test["name"] for test in test_results if test["status"] == "failed"]
print("Failed tests:", failed_tests)

# Calculate total duration for passed tests
total_passed_duration = sum(test["duration"] for test in test_results
                           if test["status"] == "passed")
print(f"Total duration of passed tests: {total_passed_duration}s")
print()

# Example 4: Build test data matrix
usernames = ["alice", "bob"]
passwords = ["pass123", "pass456"]
test_combinations = [{"username": u, "password": p}
                    for u in usernames for p in passwords]
print("Test combinations:", test_combinations)
print()

# ============================================
# FLEXIBLE TEST HELPERS WITH *ARGS/**KWARGS
# ============================================
print("=" * 60)
print("FLEXIBLE TEST HELPERS WITH *ARGS/**KWARGS")
print("=" * 60)

# Example 1: Flexible assertion helper
def assert_elements_visible(*selectors, timeout=5):
    """
    Verify multiple elements are visible
    In real Playwright: page.locator(selector).is_visible()
    """
    print(f"Checking {len(selectors)} elements with {timeout}s timeout:")
    for selector in selectors:
        print(f"  ✓ '{selector}' is visible")
    return True

assert_elements_visible("#header", ".menu", "#footer", timeout=10)
print()

# Example 2: Flexible form filler
def fill_form(**field_values):
    """
    Fill form with any number of fields
    In real Playwright: page.fill(selector, value)
    """
    print("Filling form fields:")
    for field, value in field_values.items():
        print(f"  {field} = '{value}'")

fill_form(
    username="testuser",
    email="test@example.com",
    password="secret123",
    phone="555-1234"
)
print()

# Example 3: Custom wait with options
def wait_for_element(selector, **options):
    """
    Wait for element with flexible options
    In real Playwright: page.wait_for_selector(selector, **options)
    """
    timeout = options.get("timeout", 30000)
    state = options.get("state", "visible")
    print(f"Waiting for '{selector}' to be {state} (timeout: {timeout}ms)")
    return True

wait_for_element("#submit-btn", timeout=5000, state="enabled")
print()

# Example 4: Screenshot with flexible naming
def take_screenshot(test_name, *tags, timestamp=True):
    """Generate screenshot filename with tags"""
    filename_parts = [test_name]
    filename_parts.extend(tags)

    if timestamp:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_parts.append(ts)

    filename = "_".join(filename_parts) + ".png"
    print(f"Taking screenshot: {filename}")
    return filename

take_screenshot("test_login", "failed", "chrome", timestamp=True)
take_screenshot("test_checkout", "passed")
print()

# ============================================
# DECORATORS FOR TEST AUTOMATION
# ============================================
print("=" * 60)
print("DECORATORS FOR TEST AUTOMATION")
print("=" * 60)

# Example 1: Retry decorator for flaky tests
def retry_on_failure(max_attempts=3, delay=1):
    """Retry test if it fails"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}/{max_attempts}: {func.__name__}")
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        print(f"  ✓ Success on attempt {attempt}")
                    return result
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"  ✗ Failed after {max_attempts} attempts")
                        raise
                    print(f"  ✗ Failed: {e}, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=0.5)
def flaky_test():
    """Simulates a flaky test"""
    import random
    if random.random() > 0.7:  # 30% success rate
        return "Test passed"
    raise Exception("Element not found")

# Uncomment to test:
# flaky_test()
print()

# Example 2: Screenshot on failure decorator
def screenshot_on_failure(func):
    """Take screenshot if test fails"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            screenshot_name = f"{func.__name__}_failure_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            print(f"Test failed! Taking screenshot: {screenshot_name}")
            raise
    return wrapper

@screenshot_on_failure
def test_with_auto_screenshot():
    """Test that might fail"""
    print("Running test...")
    # If this raises, screenshot is taken
    return "Success"

test_with_auto_screenshot()
print()

# Example 3: Test timing decorator
def time_test(func):
    """Measure test execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} completed in {duration:.2f}s")
        return result
    return wrapper

@time_test
def slow_test():
    """Simulate slow test"""
    time.sleep(0.5)
    return "Done"

slow_test()
print()

# Example 4: Test data cleanup decorator
def cleanup_test_data(func):
    """Ensure test data is cleaned up after test"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Setting up test data for {func.__name__}")
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            print(f"Cleaning up test data for {func.__name__}")
    return wrapper

@cleanup_test_data
def test_with_cleanup():
    """Test that creates and cleans up data"""
    print("Executing test...")
    return "Test complete"

test_with_cleanup()
print()

# ============================================
# DATETIME IN TESTING
# ============================================
print("=" * 60)
print("DATETIME IN TESTING")
print("=" * 60)

# Example 1: Generate test data with dates
def generate_test_dates(start_date, num_days):
    """Generate list of test dates"""
    return [start_date + timedelta(days=i) for i in range(num_days)]

today = datetime.now().date()
test_dates = generate_test_dates(today, 7)
print("Test dates for next 7 days:")
for date in test_dates:
    print(f"  {date.strftime('%Y-%m-%d (%A)')}")
print()

# Example 2: Test expiration dates
def test_expiration_scenarios():
    """Test with various expiration dates"""
    today = datetime.now()
    scenarios = {
        "expired": today - timedelta(days=1),
        "expires_today": today,
        "expires_soon": today + timedelta(days=7),
        "expires_later": today + timedelta(days=30),
    }

    print("Testing expiration scenarios:")
    for scenario, date in scenarios.items():
        print(f"  {scenario}: {date.strftime('%Y-%m-%d')}")

test_expiration_scenarios()
print()

# Example 3: Format dates for form input
def format_date_for_input(date, format_type="US"):
    """Format date for different input types"""
    formats = {
        "US": "%m/%d/%Y",
        "EU": "%d/%m/%Y",
        "ISO": "%Y-%m-%d",
    }
    return date.strftime(formats[format_type])

test_date = datetime(2024, 12, 25)
print("Date formatting for forms:")
print(f"  US format: {format_date_for_input(test_date, 'US')}")
print(f"  EU format: {format_date_for_input(test_date, 'EU')}")
print(f"  ISO format: {format_date_for_input(test_date, 'ISO')}")
print()

# Example 4: Wait time calculations
def calculate_wait_time(deadline_str):
    """Calculate wait time until deadline"""
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    wait_time = (deadline - now).total_seconds()
    return max(0, wait_time)

future = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
wait_seconds = calculate_wait_time(future)
print(f"Wait time until {future}: {wait_seconds/3600:.2f} hours")
print()

# ============================================
# STRING METHODS IN TESTING
# ============================================
print("=" * 60)
print("STRING METHODS IN TESTING")
print("=" * 60)

# Example 1: Clean and validate page text
def validate_page_text(actual_text, expected_text):
    """Compare page text ignoring whitespace and case"""
    actual_clean = actual_text.strip().lower()
    expected_clean = expected_text.strip().lower()
    return actual_clean == expected_clean

actual = "  Welcome to Our Site!  \n"
expected = "welcome to our site!"
is_match = validate_page_text(actual, expected)
print(f"Text validation: {is_match}")
print(f"  Actual: '{actual}'")
print(f"  Expected: '{expected}'")
print()

# Example 2: Build dynamic selectors
def build_data_testid_selector(element_type, identifier):
    """Build data-testid selector"""
    clean_id = identifier.lower().replace(" ", "-")
    return f"[data-testid='{element_type}-{clean_id}']"

selectors = [
    build_data_testid_selector("button", "Submit Form"),
    build_data_testid_selector("input", "User Name"),
    build_data_testid_selector("link", "Contact Us"),
]
print("Generated selectors:")
for sel in selectors:
    print(f"  {sel}")
print()

# Example 3: Parse URLs
def parse_test_url(url):
    """Extract components from URL"""
    parts = url.split('?')
    base = parts[0]

    params = {}
    if len(parts) > 1:
        for param in parts[1].split('&'):
            key, value = param.split('=')
            params[key] = value

    return {"base": base, "params": params}

test_url = "https://example.com/search?q=python&page=1&limit=10"
parsed = parse_test_url(test_url)
print(f"URL: {test_url}")
print(f"Parsed: {parsed}")
print()

# Example 4: Extract test data from CSV line
def parse_csv_test_data(csv_line):
    """Parse CSV test data"""
    fields = csv_line.strip().split(',')
    return {
        "username": fields[0],
        "password": fields[1],
        "expected_role": fields[2],
    }

csv_data = "testuser1,pass123,admin"
test_data = parse_csv_test_data(csv_data)
print("Parsed test data:", test_data)
print()

# Example 5: Build XPath with string formatting
def build_text_xpath(element, text):
    """Build XPath to find element by text"""
    return f"//{element}[contains(text(), '{text}')]"

xpaths = [
    build_text_xpath("button", "Submit"),
    build_text_xpath("a", "Click here"),
    build_text_xpath("span", "Error"),
]
print("Generated XPaths:")
for xpath in xpaths:
    print(f"  {xpath}")
print()

# ============================================
# COMBINING CONCEPTS
# ============================================
print("=" * 60)
print("COMBINING CONCEPTS - REAL-WORLD SCENARIO")
print("=" * 60)

class TestDataGenerator:
    """Generate test data using comprehensions and datetime"""

    @staticmethod
    def generate_users(count, base_date=None):
        """Generate test users with comprehension"""
        if base_date is None:
            base_date = datetime.now()

        return [
            {
                "username": f"user{i}",
                "email": f"user{i}@test.com",
                "created_at": (base_date - timedelta(days=i)).strftime("%Y-%m-%d"),
                "role": "admin" if i % 3 == 0 else "user",
            }
            for i in range(1, count + 1)
        ]

    @staticmethod
    def generate_orders(*product_ids, **order_details):
        """Generate order data with flexible parameters"""
        base_order = {
            "order_id": f"ORD-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "products": list(product_ids),
            "created_at": datetime.now().isoformat(),
        }
        base_order.update(order_details)
        return base_order

# Generate test users
users = TestDataGenerator.generate_users(5)
print("Generated test users:")
for user in users:
    print(f"  {user}")
print()

# Generate test order
order = TestDataGenerator.generate_orders(
    101, 102, 103,
    customer="testuser",
    status="pending",
    total=99.99
)
print("Generated test order:")
print(f"  {order}")
print()

print("=" * 60)
print("These patterns will be used extensively in Playwright testing!")
print("=" * 60)
