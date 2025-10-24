"""
Lecture 3: Playwright Automation Examples with Loops
This file demonstrates how loops are used in web automation scenarios.
Note: These are conceptual examples showing the logic - actual Playwright code comes later.
"""

# ============================================
# EXAMPLE 1: ITERATING THROUGH MULTIPLE ELEMENTS
# ============================================
print("=== Example 1: Processing Multiple Buttons ===")

# Simulating finding multiple buttons on a page
buttons = [
    {"text": "Home", "enabled": True},
    {"text": "Products", "enabled": True},
    {"text": "About", "enabled": False},
    {"text": "Contact", "enabled": True}
]

print(f"Found {len(buttons)} navigation buttons:")

for button in buttons:
    if button["enabled"]:
        print(f"  ✓ Clicking button: {button['text']}")
    else:
        print(f"  ⊗ Skipping disabled button: {button['text']}")

print()

# ============================================
# EXAMPLE 2: FILLING MULTIPLE FORM FIELDS
# ============================================
print("=== Example 2: Filling Form Fields ===")

# Form fields to fill
form_data = {
    "First Name": "John",
    "Last Name": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "555-1234",
    "Address": "123 Main St"
}

print("Filling out form:")
for field_name, value in form_data.items():
    print(f"  Filling '{field_name}': {value}")

print("  ✓ Form submitted")

print()

# ============================================
# EXAMPLE 3: VALIDATING MULTIPLE ELEMENTS
# ============================================
print("=== Example 3: Validating Page Elements ===")

# Expected elements on the page
expected_elements = [
    {"type": "heading", "text": "Welcome to Our Site"},
    {"type": "button", "text": "Get Started"},
    {"type": "link", "text": "Learn More"},
    {"type": "image", "alt": "Hero Banner"}
]

print("Validating page elements:")
all_found = True

for element in expected_elements:
    # Simulate checking if element exists
    found = True  # In real code, this would actually search the page

    if found:
        print(f"  ✓ Found {element['type']}: {element.get('text', element.get('alt'))}")
    else:
        print(f"  ✗ Missing {element['type']}: {element.get('text', element.get('alt'))}")
        all_found = False

if all_found:
    print("\n✓ All elements validated successfully")
else:
    print("\n✗ Some elements missing")

print()

# ============================================
# EXAMPLE 4: PROCESSING TABLE ROWS
# ============================================
print("=== Example 4: Processing Table Data ===")

# Simulating table data from a web page
products = [
    {"name": "Laptop", "price": 999.99, "stock": 5},
    {"name": "Mouse", "price": 29.99, "stock": 50},
    {"name": "Keyboard", "price": 79.99, "stock": 30},
    {"name": "Monitor", "price": 299.99, "stock": 0},
    {"name": "Headphones", "price": 149.99, "stock": 15}
]

print("Products in stock:")
in_stock_count = 0

for product in products:
    if product["stock"] > 0:
        in_stock_count += 1
        print(f"  • {product['name']}: ${product['price']} ({product['stock']} available)")
    else:
        print(f"  ⊗ {product['name']}: OUT OF STOCK")

print(f"\nTotal in stock: {in_stock_count}/{len(products)}")

print()

# ============================================
# EXAMPLE 5: CLICKING MULTIPLE CHECKBOXES
# ============================================
print("=== Example 5: Selecting Multiple Checkboxes ===")

# Checkbox options
options = [
    {"label": "I agree to terms and conditions", "should_check": True},
    {"label": "Send me promotional emails", "should_check": False},
    {"label": "Subscribe to newsletter", "should_check": True},
    {"label": "Remember my preferences", "should_check": True}
]

print("Processing checkboxes:")
for option in options:
    if option["should_check"]:
        print(f"  ☑ Checking: {option['label']}")
    else:
        print(f"  ☐ Leaving unchecked: {option['label']}")

print()

# ============================================
# EXAMPLE 6: SEARCHING THROUGH RESULTS
# ============================================
print("=== Example 6: Finding Specific Search Result ===")

# Simulating search results
search_results = [
    {"title": "Python Basics Tutorial", "url": "/python-basics"},
    {"title": "JavaScript Guide", "url": "/javascript"},
    {"title": "Python Automation with Playwright", "url": "/python-automation"},
    {"title": "Web Testing Best Practices", "url": "/web-testing"},
    {"title": "Advanced Python Techniques", "url": "/advanced-python"}
]

target = "Automation"
print(f"Searching for: '{target}'")

found = False
for result in search_results:
    if target.lower() in result["title"].lower():
        print(f"  ✓ Found: {result['title']}")
        print(f"    URL: {result['url']}")
        found = True
        break  # Found what we need, stop searching

if not found:
    print(f"  ✗ No results found for '{target}'")

print()

# ============================================
# EXAMPLE 7: DATA-DRIVEN TESTING
# ============================================
print("=== Example 7: Data-Driven Login Testing ===")

# Test data for multiple login scenarios
test_cases = [
    {"username": "admin", "password": "admin123", "should_pass": True},
    {"username": "user", "password": "wrongpass", "should_pass": False},
    {"username": "", "password": "pass123", "should_pass": False},
    {"username": "testuser", "password": "test123", "should_pass": True}
]

print("Running login test cases:")
passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    print(f"  Username: '{test['username']}'")
    print(f"  Password: {'*' * len(test['password'])}")

    # Simulate login attempt
    actual_result = test["should_pass"]  # In real test, this would be actual login result

    if actual_result == test["should_pass"]:
        print(f"  ✓ PASS - Behaved as expected")
        passed += 1
    else:
        print(f"  ✗ FAIL - Unexpected result")
        failed += 1

print(f"\nTest Results: {passed} passed, {failed} failed")

print()

# ============================================
# EXAMPLE 8: NAVIGATING THROUGH PAGES
# ============================================
print("=== Example 8: Multi-Page Navigation ===")

pages = [
    "/home",
    "/products",
    "/about",
    "/contact",
    "/faq"
]

print("Navigating through site pages:")
for page in pages:
    print(f"  → Navigating to: {page}")
    print(f"     Verifying page loaded...")
    print(f"     ✓ Page {page} verified")

print()

# ============================================
# EXAMPLE 9: RETRY LOGIC FOR FLAKY ELEMENTS
# ============================================
print("=== Example 9: Retry Logic for Element Interaction ===")

max_retries = 3
element_name = "Submit Button"

for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt} to click {element_name}...")

    # Simulate element interaction (succeeds on 2nd try)
    if attempt == 2:
        print(f"  ✓ Successfully clicked {element_name}")
        break
    else:
        print(f"  ✗ Element not ready, retrying...")
else:
    print(f"  ✗ Failed to click {element_name} after {max_retries} attempts")

print()

# ============================================
# EXAMPLE 10: WAITING FOR ELEMENTS TO APPEAR
# ============================================
print("=== Example 10: Polling for Element ===")

max_wait = 10  # seconds
element_name = "Loading Spinner"

print(f"Waiting for '{element_name}' to disappear...")

for second in range(1, max_wait + 1):
    print(f"  Waiting... {second}s")

    # Simulate element disappearing after 3 seconds
    if second >= 3:
        print(f"  ✓ '{element_name}' disappeared")
        break
else:
    print(f"  ⚠ Timeout: '{element_name}' still present after {max_wait}s")

print()

# ============================================
# EXAMPLE 11: COLLECTING DATA FROM MULTIPLE PAGES
# ============================================
print("=== Example 11: Scraping Multiple Pages ===")

all_items = []

for page_num in range(1, 4):
    print(f"\nScraping page {page_num}:")

    # Simulate items on this page
    items_on_page = [
        f"Item {(page_num - 1) * 3 + 1}",
        f"Item {(page_num - 1) * 3 + 2}",
        f"Item {(page_num - 1) * 3 + 3}"
    ]

    for item in items_on_page:
        print(f"  • Found: {item}")
        all_items.append(item)

print(f"\nTotal items collected: {len(all_items)}")
print(f"Items: {all_items}")

print()

# ============================================
# EXAMPLE 12: VALIDATING LIST OF LINKS
# ============================================
print("=== Example 12: Validating Navigation Links ===")

# Simulating links found on page
links = [
    {"text": "Home", "href": "/home", "expected": True},
    {"text": "Products", "href": "/products", "expected": True},
    {"text": "About", "href": "/about", "expected": True},
    {"text": "Blog", "href": "/blog", "expected": True},
    {"text": "Admin", "href": "/admin", "expected": False}  # Shouldn't be visible
]

print("Validating navigation links:")
issues = []

for link in links:
    if link["expected"]:
        print(f"  ✓ '{link['text']}' → {link['href']} (expected)")
    else:
        print(f"  ⚠ '{link['text']}' → {link['href']} (should not be visible!)")
        issues.append(link)

if len(issues) == 0:
    print("\n✓ All links validated successfully")
else:
    print(f"\n⚠ Found {len(issues)} unexpected link(s)")

print()

# ============================================
# EXAMPLE 13: FILLING MULTIPLE FORMS (BATCH)
# ============================================
print("=== Example 13: Batch Form Submission ===")

# Multiple users to register
users = [
    {"name": "Alice Smith", "email": "alice@example.com"},
    {"name": "Bob Johnson", "email": "bob@example.com"},
    {"name": "Charlie Brown", "email": "charlie@example.com"}
]

print("Registering multiple users:")
for i, user in enumerate(users, 1):
    print(f"\nRegistering user {i}/{len(users)}:")
    print(f"  Name: {user['name']}")
    print(f"  Email: {user['email']}")
    print(f"  → Filling form...")
    print(f"  → Submitting...")
    print(f"  ✓ User registered successfully")

print(f"\n✓ All {len(users)} users registered")

print()

# ============================================
# EXAMPLE 14: SKIPPING DISABLED ELEMENTS
# ============================================
print("=== Example 14: Processing Enabled Buttons Only ===")

buttons = [
    {"id": "btn1", "text": "Save", "enabled": True},
    {"id": "btn2", "text": "Delete", "enabled": False},
    {"id": "btn3", "text": "Edit", "enabled": True},
    {"id": "btn4", "text": "Cancel", "enabled": True},
    {"id": "btn5", "text": "Submit", "enabled": False}
]

print("Testing clickable buttons:")
tested = 0

for button in buttons:
    if not button["enabled"]:
        print(f"  ⊗ Skipping disabled button: {button['text']}")
        continue

    print(f"  ✓ Testing button: {button['text']}")
    tested += 1

print(f"\nTested {tested}/{len(buttons)} buttons")

print()

# ============================================
# EXAMPLE 15: EXTRACTING AND VALIDATING PRICES
# ============================================
print("=== Example 15: Validating Product Prices ===")

products = [
    {"name": "Laptop", "price": "$999.99"},
    {"name": "Mouse", "price": "$29.99"},
    {"name": "Keyboard", "price": "INVALID"},
    {"name": "Monitor", "price": "$299.99"},
    {"name": "Webcam", "price": "$79.99"}
]

print("Validating product prices:")
valid_count = 0
invalid_items = []

for product in products:
    price = product["price"]

    if price.startswith("$") and price[1:].replace(".", "").isdigit():
        print(f"  ✓ {product['name']}: {price}")
        valid_count += 1
    else:
        print(f"  ✗ {product['name']}: Invalid price '{price}'")
        invalid_items.append(product["name"])

print(f"\nValidation: {valid_count}/{len(products)} valid prices")
if invalid_items:
    print(f"Items with invalid prices: {', '.join(invalid_items)}")

print()

# ============================================
# EXAMPLE 16: COMBINING LOOPS WITH PREVIOUS CONCEPTS
# ============================================
print("=== Example 16: Complete Test Scenario ===")

# Combining loops with string manipulation and conditionals
test_data = [
    {"username": "user1@test.com", "password": "Pass123!", "expected_result": "success"},
    {"username": "user2@test.com", "password": "weak", "expected_result": "error"},
    {"username": "invalid-email", "password": "Pass123!", "expected_result": "error"},
    {"username": "user3@test.com", "password": "SecurePass456!", "expected_result": "success"}
]

print("Running comprehensive login tests:")
for i, data in enumerate(test_cases, 1):
    print(f"\nTest {i}:")

    # Validate email format (string manipulation from Lecture 2)
    if "@" not in data["username"] or "." not in data["username"]:
        print(f"  ✗ Invalid email format: {data['username']}")
        continue

    # Validate password strength (conditionals from Lecture 2)
    if len(data["password"]) < 8:
        print(f"  ✗ Password too short")
        continue

    print(f"  Username: {data['username']}")
    print(f"  Password: {'*' * len(data['password'])}")
    print(f"  ✓ Credentials validated")

print()

print("=" * 50)
print("These examples demonstrate loop patterns in automation:")
print("  • Iterating through multiple web elements")
print("  • Filling forms with multiple fields")
print("  • Processing tables and lists of data")
print("  • Data-driven testing with test cases")
print("  • Retry logic for flaky operations")
print("  • Batch operations across multiple pages")
print("  • Validating collections of elements")
print("=" * 50)
