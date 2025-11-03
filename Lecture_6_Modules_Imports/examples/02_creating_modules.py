"""
Lecture 6 - Example 2: Creating Your Own Modules
===============================================
Learn how to create and use your own modules.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import my_modules
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# 1. IMPORTING YOUR OWN MODULE
# ============================

from my_modules import greetings

print("1. Importing your own module:")
print(greetings.say_hello("Alice"))
print(greetings.say_goodbye("Bob"))
print(f"Module version: {greetings.MODULE_VERSION}")
print()

print("-" * 50)


# 2. IMPORTING SPECIFIC FUNCTIONS
# ===============================

from my_modules.greetings import say_hello, say_goodbye

print("2. Importing specific functions:")
print(say_hello("Charlie"))
print(say_goodbye("Diana"))
print()

print("-" * 50)


# 3. IMPORTING FROM CALCULATOR MODULE
# ===================================

from my_modules.calculator import add, subtract, multiply, divide

print("3. Using calculator module:")
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"20 / 4 = {divide(20, 4)}")
print()

print("-" * 50)


# 4. IMPORTING ENTIRE MODULE WITH ALIAS
# =====================================

from my_modules import calculator as calc

print("4. Using module alias:")
print(f"100 + 200 = {calc.add(100, 200)}")
print(f"PI value: {calc.PI}")
print()

print("-" * 50)


# 5. IMPORTING TEST HELPERS MODULE
# ================================

from my_modules.test_helpers import log_message, format_test_name, create_test_data

print("5. Using test helpers module:")
log_message("Test execution started")
log_message("Warning: Slow response", "WARNING")
log_message("Error occurred", "ERROR")

print(format_test_name("Login Functionality"))

test_user = create_test_data("testuser", "test@example.com", "SecurePass123")
print(f"Test user created: {test_user}")
print()

print("-" * 50)


# 6. IMPORTING FROM PACKAGE __init__.py
# =====================================

# These were made available in __init__.py
from my_modules import say_hello, add

print("6. Importing from package:")
print(say_hello("Package User"))
print(f"Quick add: {add(10, 20)}")
print()

print("-" * 50)


# 7. THE __name__ VARIABLE
# ========================

print("7. Understanding __name__:")
print(f"This file's __name__: {__name__}")
print(f"Greetings module __name__: {greetings.__name__}")
print()
print("When a file is run directly: __name__ == '__main__'")
print("When a file is imported: __name__ == module name")
print()

print("-" * 50)


# 8. PRACTICAL EXAMPLE - TEST SCENARIO
# ====================================

from my_modules.test_helpers import (
    log_message,
    format_test_name,
    create_test_data,
    generate_test_report
)
from my_modules.calculator import calculate_percentage

print("8. Complete test scenario:")
print()

# Start test
test_name = format_test_name("User Registration")
print(test_name)
log_message("Starting test execution")

# Create test data
user1 = create_test_data("alice", "alice@test.com", "pass123")
user2 = create_test_data("bob", "bob@test.com", "pass456")
log_message(f"Created test users: {user1['username']}, {user2['username']}")

# Simulate test results
log_message("Running test cases...")
report = generate_test_report(passed=15, failed=2, skipped=1)
log_message(f"Tests completed - Success rate: {report['success_rate']}%")

print(f"\nTest Report:")
print(f"  Total: {report['total']}")
print(f"  Passed: {report['passed']}")
print(f"  Failed: {report['failed']}")
print(f"  Skipped: {report['skipped']}")
print(f"  Success Rate: {report['success_rate']}%")
print()

print("-" * 50)


# 9. ORGANIZING YOUR TEST PROJECT
# ===============================

print("9. How to organize a test project:")
print()

project_structure = """
test_project/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_search.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── home_page.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── data_generators.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── test_data.py
└── requirements.txt
"""

print(project_structure)
print()

print("-" * 50)


# 10. MODULE BEST PRACTICES
# =========================

print("10. Module best practices:")
print()
print("✅ DO:")
print("  - One module = one clear purpose")
print("  - Use descriptive module names")
print("  - Add docstrings to modules and functions")
print("  - Group related functions together")
print("  - Use __init__.py for packages")
print()
print("❌ DON'T:")
print("  - Create modules with everything in them")
print("  - Use generic names like 'utils' or 'helpers' without context")
print("  - Create circular dependencies")
print("  - Put too much code in __init__.py")
print()

print("=" * 50)
print("Example complete! You've learned how to create modules.")
print("=" * 50)
