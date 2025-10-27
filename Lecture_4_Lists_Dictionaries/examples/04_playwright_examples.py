"""
Example 4: Playwright Automation Examples
Real-world examples of using lists and dictionaries in Playwright test automation.
Note: This file demonstrates concepts - actual Playwright code would need proper setup.
"""

print("=" * 60)
print("PLAYWRIGHT AUTOMATION EXAMPLES")
print("=" * 60)
print()

# ============================================
# Example 1: Multiple Test URLs
# ============================================
print("1. TESTING MULTIPLE PAGES")
print("-" * 40)

# List of pages to test
test_urls = [
    "https://example.com/",
    "https://example.com/about",
    "https://example.com/products",
    "https://example.com/contact",
    "https://example.com/pricing"
]

print("Pages to test:")
for url in test_urls:
    print(f"  Testing: {url}")
    # In real Playwright:
    # page.goto(url)
    # assert page.title() is not None

print(f"\nTotal pages to test: {len(test_urls)}")
print()

# ============================================
# Example 2: Form Data
# ============================================
print("2. FILLING REGISTRATION FORM")
print("-" * 40)

# User registration data
registration_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-0123",
    "password": "SecurePass123!",
    "confirm_password": "SecurePass123!",
    "country": "United States",
    "agree_terms": True
}

print("Registration form data:")
for field, value in registration_data.items():
    if "password" in field:
        print(f"  {field}: {'*' * len(str(value))}")
    else:
        print(f"  {field}: {value}")

print("\nGenerated Playwright code:")
print(f"  page.fill('#first_name', '{registration_data['first_name']}')")
print(f"  page.fill('#email', '{registration_data['email']}')")
print(f"  page.fill('#password', '{registration_data['password']}')")
if registration_data["agree_terms"]:
    print(f"  page.check('#agree_terms')")
print()

# ============================================
# Example 3: Page Object Locators
# ============================================
print("3. PAGE OBJECT LOCATORS")
print("-" * 40)

# Login page locators
login_page_locators = {
    "username_field": "#username",
    "password_field": "#password",
    "login_button": "button[type='submit']",
    "forgot_password_link": "a.forgot-password",
    "signup_link": "//a[text()='Sign up']",
    "error_message": ".error-message",
    "success_message": ".success-message"
}

print("Login page locators:")
for name, selector in login_page_locators.items():
    print(f"  {name}: {selector}")

print("\nUsage example:")
print(f"  page.fill('{login_page_locators['username_field']}', 'testuser')")
print(f"  page.fill('{login_page_locators['password_field']}', 'password')")
print(f"  page.click('{login_page_locators['login_button']}')")
print()

# ============================================
# Example 4: Data-Driven Login Tests
# ============================================
print("4. DATA-DRIVEN LOGIN TESTS")
print("-" * 40)

# Test scenarios
login_scenarios = [
    {
        "name": "Valid Login",
        "username": "valid_user",
        "password": "Valid@123",
        "expected_result": "success",
        "expected_url": "https://example.com/dashboard"
    },
    {
        "name": "Invalid Password",
        "username": "valid_user",
        "password": "WrongPass",
        "expected_result": "error",
        "expected_message": "Invalid credentials"
    },
    {
        "name": "Empty Username",
        "username": "",
        "password": "Valid@123",
        "expected_result": "error",
        "expected_message": "Username is required"
    },
    {
        "name": "SQL Injection Attempt",
        "username": "admin' OR '1'='1",
        "password": "any",
        "expected_result": "error",
        "expected_message": "Invalid credentials"
    }
]

print("Login test scenarios:")
for i, scenario in enumerate(login_scenarios, 1):
    print(f"\n  {i}. {scenario['name']}")
    print(f"     Username: {scenario['username']}")
    print(f"     Password: {'*' * len(scenario['password'])}")
    print(f"     Expected: {scenario['expected_result']}")

print(f"\nTotal scenarios: {len(login_scenarios)}")
print()

# ============================================
# Example 5: Navigation Menu Validation
# ============================================
print("5. NAVIGATION MENU VALIDATION")
print("-" * 40)

# Expected navigation items
expected_menu = ["Home", "Products", "About Us", "Contact", "Blog"]

# Simulated actual menu from page
actual_menu = ["Home", "Products", "Services", "Contact", "Blog"]

print(f"Expected menu: {expected_menu}")
print(f"Actual menu:   {actual_menu}")

# Find differences
missing = [item for item in expected_menu if item not in actual_menu]
extra = [item for item in actual_menu if item not in expected_menu]

if missing:
    print(f"\n❌ Missing items: {missing}")
if extra:
    print(f"⚠️  Extra items: {extra}")
if not missing and not extra:
    print("\n✅ Menu matches expected!")
print()

# ============================================
# Example 6: Browser Configuration
# ============================================
print("6. BROWSER CONFIGURATION")
print("-" * 40)

# Playwright browser configurations
browser_configs = [
    {
        "name": "Chrome Desktop",
        "browser_type": "chromium",
        "headless": False,
        "viewport": {"width": 1920, "height": 1080},
        "device_scale_factor": 1
    },
    {
        "name": "Firefox Desktop",
        "browser_type": "firefox",
        "headless": False,
        "viewport": {"width": 1920, "height": 1080},
        "device_scale_factor": 1
    },
    {
        "name": "Mobile Chrome",
        "browser_type": "chromium",
        "headless": False,
        "viewport": {"width": 375, "height": 667},
        "device_scale_factor": 2
    }
]

print("Browser configurations for cross-browser testing:")
for config in browser_configs:
    print(f"\n  {config['name']}:")
    print(f"    Browser: {config['browser_type']}")
    print(f"    Viewport: {config['viewport']['width']}x{config['viewport']['height']}")
    print(f"    Headless: {config['headless']}")
print()

# ============================================
# Example 7: Test Data Sets
# ============================================
print("7. PRODUCT SEARCH TEST DATA")
print("-" * 40)

# Search test data
search_tests = [
    {
        "query": "laptop",
        "expected_results": ["Dell Laptop", "HP Laptop", "MacBook Pro"],
        "min_results": 3
    },
    {
        "query": "headphones",
        "expected_results": ["Sony Headphones", "Bose QuietComfort"],
        "min_results": 2
    },
    {
        "query": "nonexistent12345",
        "expected_results": [],
        "min_results": 0
    }
]

print("Search test data:")
for test in search_tests:
    print(f"\n  Query: '{test['query']}'")
    print(f"  Expected results: {test['expected_results']}")
    print(f"  Minimum results: {test['min_results']}")

# Simulated test execution
print("\n  Simulated test:")
for test in search_tests:
    print(f"    Searching for '{test['query']}'...")
    print(f"    Expected at least {test['min_results']} results")
print()

# ============================================
# Example 8: Form Validation Tests
# ============================================
print("8. FORM VALIDATION TESTS")
print("-" * 40)

# Email validation test cases
email_validation_tests = [
    {"email": "valid@example.com", "should_pass": True},
    {"email": "user.name+tag@domain.co.uk", "should_pass": True},
    {"email": "invalid.email", "should_pass": False},
    {"email": "@example.com", "should_pass": False},
    {"email": "user@", "should_pass": False},
    {"email": "", "should_pass": False}
]

print("Email validation test cases:")
for test in email_validation_tests:
    status = "✓ Valid" if test["should_pass"] else "✗ Invalid"
    print(f"  {test['email']:<30} {status}")

print("\nTest execution:")
for test in email_validation_tests:
    expected = "to be accepted" if test["should_pass"] else "to be rejected"
    print(f"  Testing '{test['email']}' - expected {expected}")
print()

# ============================================
# Example 9: Element Collections
# ============================================
print("9. WORKING WITH ELEMENT COLLECTIONS")
print("-" * 40)

# Simulated product cards data
products_on_page = [
    {"name": "Laptop", "price": "$999", "rating": 4.5},
    {"name": "Mouse", "price": "$25", "rating": 4.0},
    {"name": "Keyboard", "price": "$75", "rating": 4.8},
    {"name": "Monitor", "price": "$299", "rating": 4.3}
]

print("Products found on page:")
for i, product in enumerate(products_on_page, 1):
    print(f"  {i}. {product['name']}")
    print(f"     Price: {product['price']}")
    print(f"     Rating: {product['rating']} ⭐")

# Filter high-rated products
high_rated = [p for p in products_on_page if p['rating'] >= 4.5]
print(f"\nHigh-rated products (>=4.5): {len(high_rated)}")
for product in high_rated:
    print(f"  - {product['name']}: {product['rating']} ⭐")
print()

# ============================================
# Example 10: Test Execution Report
# ============================================
print("10. TEST EXECUTION REPORT")
print("-" * 40)

# Test results
test_results = {
    "total": 25,
    "passed": 20,
    "failed": 3,
    "skipped": 2,
    "duration": "2m 15s",
    "failed_tests": [
        {
            "name": "test_checkout_payment",
            "error": "Payment gateway timeout",
            "screenshot": "checkout_error.png"
        },
        {
            "name": "test_product_filter",
            "error": "Filter button not clickable",
            "screenshot": "filter_error.png"
        },
        {
            "name": "test_user_profile_update",
            "error": "Profile save failed",
            "screenshot": "profile_error.png"
        }
    ]
}

print("Test Execution Summary")
print("=" * 40)
print(f"Total Tests:    {test_results['total']}")
print(f"Passed:         {test_results['passed']} ✓")
print(f"Failed:         {test_results['failed']} ✗")
print(f"Skipped:        {test_results['skipped']} ⊘")
print(f"Duration:       {test_results['duration']}")

pass_rate = (test_results['passed'] / test_results['total']) * 100
print(f"Pass Rate:      {pass_rate:.1f}%")

if test_results['failed'] > 0:
    print("\nFailed Tests:")
    for i, test in enumerate(test_results['failed_tests'], 1):
        print(f"\n  {i}. {test['name']}")
        print(f"     Error: {test['error']}")
        print(f"     Screenshot: {test['screenshot']}")
print()

# ============================================
# Example 11: Environment Configuration
# ============================================
print("11. ENVIRONMENT CONFIGURATION")
print("-" * 40)

# Multi-environment setup
environments = {
    "local": {
        "url": "http://localhost:3000",
        "api_url": "http://localhost:8000/api",
        "database": "local_db",
        "credentials": {"username": "admin", "password": "admin123"}
    },
    "staging": {
        "url": "https://staging.example.com",
        "api_url": "https://api-staging.example.com",
        "database": "staging_db",
        "credentials": {"username": "test_user", "password": "test_pass"}
    },
    "production": {
        "url": "https://example.com",
        "api_url": "https://api.example.com",
        "database": "prod_db",
        "credentials": {"username": "prod_user", "password": "***"}
    }
}

current_env = "staging"
print(f"Current environment: {current_env}")
print(f"URL: {environments[current_env]['url']}")
print(f"API: {environments[current_env]['api_url']}")
print(f"Username: {environments[current_env]['credentials']['username']}")

print("\nAll environments:")
for env_name, env_config in environments.items():
    print(f"  {env_name}: {env_config['url']}")
print()

# ============================================
# Example 12: Assertion Helper
# ============================================
print("12. ASSERTION HELPERS")
print("-" * 40)

# Expected vs Actual comparisons
assertions = [
    {
        "description": "Page title",
        "expected": "Dashboard - My App",
        "actual": "Dashboard - My App",
        "passed": True
    },
    {
        "description": "User count",
        "expected": 10,
        "actual": 10,
        "passed": True
    },
    {
        "description": "Navigation items",
        "expected": ["Home", "Products", "Contact"],
        "actual": ["Home", "Services", "Contact"],
        "passed": False
    }
]

print("Assertion Results:")
for assertion in assertions:
    status = "✓ PASS" if assertion["passed"] else "✗ FAIL"
    print(f"\n  {status}: {assertion['description']}")
    print(f"    Expected: {assertion['expected']}")
    print(f"    Actual:   {assertion['actual']}")

passed_assertions = [a for a in assertions if a["passed"]]
print(f"\nPassed: {len(passed_assertions)}/{len(assertions)}")
print()

print("=" * 60)
print("✅ Playwright examples completed!")
print("=" * 60)
print()
print("💡 Key Takeaways:")
print("   - Lists store multiple URLs, locators, and test data")
print("   - Dictionaries organize structured data like form fields")
print("   - Combining both enables powerful data-driven testing")
print("   - These patterns make tests more maintainable and scalable")
