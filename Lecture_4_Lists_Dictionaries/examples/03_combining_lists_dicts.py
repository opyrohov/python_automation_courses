"""
Example 3: Combining Lists and Dictionaries
Demonstrates how to work with lists of dictionaries and dictionaries of lists.
"""

print("=" * 60)
print("COMBINING LISTS AND DICTIONARIES")
print("=" * 60)
print()

# ============================================
# List of Dictionaries
# ============================================
print("1. LIST OF DICTIONARIES (Most Common!)")
print("-" * 40)

# Test users data
test_users = [
    {
        "username": "alice",
        "password": "pass123",
        "email": "alice@example.com",
        "role": "admin"
    },
    {
        "username": "bob",
        "password": "bob456",
        "email": "bob@example.com",
        "role": "user"
    },
    {
        "username": "carol",
        "password": "carol789",
        "email": "carol@example.com",
        "role": "user"
    }
]

print("All test users:")
for user in test_users:
    print(f"  {user['username']} ({user['role']}) - {user['email']}")

# Find specific user
print("\nFind user 'bob':")
for user in test_users:
    if user["username"] == "bob":
        print(f"  Found: {user}")

# Filter by role
print("\nAdmin users:")
admins = [user for user in test_users if user["role"] == "admin"]
for admin in admins:
    print(f"  {admin['username']}")
print()

# ============================================
# Dictionary of Lists
# ============================================
print("2. DICTIONARY OF LISTS")
print("-" * 40)

# Test results organized by category
test_results = {
    "passed": ["test_login", "test_logout", "test_profile"],
    "failed": ["test_payment", "test_checkout"],
    "skipped": ["test_admin_panel"]
}

print("Test Results Summary:")
for category, tests in test_results.items():
    print(f"  {category.upper()}: {len(tests)} tests")
    for test in tests:
        print(f"    - {test}")

# Add new test result
test_results["passed"].append("test_search")
print(f"\nAfter adding test_search to passed: {test_results['passed']}")
print()

# ============================================
# Real-World Example: Shopping Cart
# ============================================
print("3. SHOPPING CART SYSTEM")
print("-" * 40)

shopping_cart = [
    {
        "product": "Laptop",
        "price": 999.99,
        "quantity": 1,
        "category": "Electronics"
    },
    {
        "product": "Mouse",
        "price": 25.50,
        "quantity": 2,
        "category": "Electronics"
    },
    {
        "product": "Notebook",
        "price": 5.99,
        "quantity": 3,
        "category": "Office"
    }
]

print("Shopping Cart:")
total = 0
for item in shopping_cart:
    subtotal = item["price"] * item["quantity"]
    total += subtotal
    print(f"  {item['product']} x{item['quantity']} = ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f}")

# Group by category
by_category = {}
for item in shopping_cart:
    category = item["category"]
    if category not in by_category:
        by_category[category] = []
    by_category[category].append(item["product"])

print("\nItems by category:")
for category, products in by_category.items():
    print(f"  {category}: {', '.join(products)}")
print()

# ============================================
# Test Scenarios (Data-Driven Testing)
# ============================================
print("4. TEST SCENARIOS (DATA-DRIVEN TESTING)")
print("-" * 40)

login_test_cases = [
    {
        "test_name": "valid_credentials",
        "username": "valid_user",
        "password": "correct_pass",
        "expected": "success"
    },
    {
        "test_name": "invalid_username",
        "username": "wrong_user",
        "password": "correct_pass",
        "expected": "fail"
    },
    {
        "test_name": "invalid_password",
        "username": "valid_user",
        "password": "wrong_pass",
        "expected": "fail"
    },
    {
        "test_name": "empty_credentials",
        "username": "",
        "password": "",
        "expected": "fail"
    }
]

print("Login Test Scenarios:")
for test_case in login_test_cases:
    print(f"\nTest: {test_case['test_name']}")
    print(f"  Username: '{test_case['username']}'")
    print(f"  Password: '{test_case['password']}'")
    print(f"  Expected: {test_case['expected']}")
print()

# ============================================
# Configuration with Nested Structures
# ============================================
print("5. TEST CONFIGURATION")
print("-" * 40)

test_config = {
    "environments": {
        "dev": {
            "url": "https://dev.example.com",
            "database": "dev_db",
            "timeout": 5000
        },
        "staging": {
            "url": "https://staging.example.com",
            "database": "staging_db",
            "timeout": 10000
        },
        "prod": {
            "url": "https://example.com",
            "database": "prod_db",
            "timeout": 15000
        }
    },
    "browsers": ["chrome", "firefox", "safari"],
    "test_suites": {
        "smoke": ["test_login", "test_homepage"],
        "regression": ["test_login", "test_homepage", "test_checkout", "test_profile"],
        "full": ["all_tests"]
    }
}

# Access nested configuration
print("Production environment:")
prod_config = test_config["environments"]["prod"]
for key, value in prod_config.items():
    print(f"  {key}: {value}")

print("\nSupported browsers:")
for browser in test_config["browsers"]:
    print(f"  - {browser}")

print("\nTest suites:")
for suite_name, tests in test_config["test_suites"].items():
    print(f"  {suite_name}: {len(tests)} tests")
print()

# ============================================
# Student Records Example
# ============================================
print("6. STUDENT RECORDS SYSTEM")
print("-" * 40)

students = [
    {
        "id": "S001",
        "name": "Alice",
        "grades": [85, 90, 92, 88],
        "major": "Computer Science"
    },
    {
        "id": "S002",
        "name": "Bob",
        "grades": [78, 82, 80, 85],
        "major": "Mathematics"
    },
    {
        "id": "S003",
        "name": "Carol",
        "grades": [92, 95, 94, 96],
        "major": "Physics"
    }
]

print("Student Report Cards:")
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"\n{student['name']} ({student['id']})")
    print(f"  Major: {student['major']}")
    print(f"  Grades: {student['grades']}")
    print(f"  Average: {avg_grade:.2f}")
    print(f"  Status: {'Pass' if avg_grade >= 80 else 'Needs Improvement'}")
print()

# ============================================
# API Response Example
# ============================================
print("7. SIMULATED API RESPONSE")
print("-" * 40)

api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "User 1", "active": True},
            {"id": 2, "name": "User 2", "active": False},
            {"id": 3, "name": "User 3", "active": True}
        ],
        "total": 3,
        "page": 1
    },
    "metadata": {
        "timestamp": "2025-10-27T19:00:00",
        "version": "1.0"
    }
}

print("API Response:")
print(f"Status: {api_response['status']}")
print(f"Total users: {api_response['data']['total']}")

print("\nActive users:")
for user in api_response['data']['users']:
    if user['active']:
        print(f"  {user['name']} (ID: {user['id']})")
print()

# ============================================
# Form Field Mapping
# ============================================
print("8. FORM FIELD MAPPING")
print("-" * 40)

form_fields = [
    {"id": "username", "type": "text", "value": "john_doe", "required": True},
    {"id": "email", "type": "email", "value": "john@example.com", "required": True},
    {"id": "password", "type": "password", "value": "secret123", "required": True},
    {"id": "age", "type": "number", "value": "25", "required": False},
    {"id": "newsletter", "type": "checkbox", "value": "true", "required": False}
]

print("Form Fields to Fill:")
for field in form_fields:
    required_text = "(required)" if field["required"] else "(optional)"
    print(f"  {field['id']} [{field['type']}]: '{field['value']}' {required_text}")

# Generate fill commands
print("\nGenerated Fill Commands:")
for field in form_fields:
    if field["type"] == "checkbox":
        print(f"  page.check('#{field['id']}')")
    else:
        print(f"  page.fill('#{field['id']}', '{field['value']}')")
print()

# ============================================
# Matrix/Table Data
# ============================================
print("9. MATRIX/TABLE DATA")
print("-" * 40)

# Test results matrix
test_matrix = [
    {"browser": "Chrome", "test1": "pass", "test2": "pass", "test3": "fail"},
    {"browser": "Firefox", "test1": "pass", "test2": "fail", "test3": "pass"},
    {"browser": "Safari", "test1": "pass", "test2": "pass", "test3": "pass"}
]

print("Test Results Matrix:")
print(f"{'Browser':<15} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10}")
print("-" * 45)
for row in test_matrix:
    print(f"{row['browser']:<15} {row['test1']:<10} {row['test2']:<10} {row['test3']:<10}")

# Count passes and fails
total_tests = 0
total_passes = 0
for row in test_matrix:
    for key, value in row.items():
        if key != "browser":
            total_tests += 1
            if value == "pass":
                total_passes += 1

print(f"\nSummary: {total_passes}/{total_tests} tests passed")
print()

# ============================================
# Practical Tips
# ============================================
print("10. PRACTICAL TIPS")
print("-" * 40)

print("✓ Use lists when:")
print("  - Order matters")
print("  - You need to iterate in sequence")
print("  - Storing similar items")

print("\n✓ Use dictionaries when:")
print("  - Need key-value association")
print("  - Fast lookup by key")
print("  - Storing structured data")

print("\n✓ Use list of dictionaries when:")
print("  - Multiple records with same structure")
print("  - Database-like data")
print("  - Test data for data-driven testing")

print("\n✓ Use dictionary of lists when:")
print("  - Grouping items by category")
print("  - Multiple values per key")
print("  - Organizing test results")

print()
print("=" * 60)
print("✅ Combining lists and dictionaries examples completed!")
print("=" * 60)
