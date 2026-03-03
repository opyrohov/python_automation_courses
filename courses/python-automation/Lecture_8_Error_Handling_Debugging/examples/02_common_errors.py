"""
Lecture 8 - Example 2: Common Python Errors
===========================================
Learn about the most common Python errors and how to fix them.
"""

print("=" * 60)
print("EXAMPLE 2: COMMON PYTHON ERRORS")
print("=" * 60)
print()


# 1. SyntaxError: Invalid Python Syntax
# =====================================
print("1. SyntaxError")
print("-" * 40)
print("❌ Common causes:")
print("   - Missing colons")
print("   - Mismatched parentheses/brackets")
print("   - Invalid indentation")
print()

# WRONG:
# if True
#     print("Missing colon")

# WRONG:
# print("Mismatched parentheses"

# RIGHT:
if True:
    print("✅ Correct syntax with colon")
print()


# 2. NameError: Variable Not Defined
# ==================================
print("2. NameError")
print("-" * 40)

# WRONG:
# print(undefined_variable)  # NameError

# RIGHT:
name = "Alice"
print(f"✅ Variable defined: {name}")

# Common in automation:
try:
    print(page_title)  # Not defined yet
except NameError:
    print("❌ NameError: 'page_title' is not defined")
    page_title = "Default Title"
    print(f"✅ Now defined: {page_title}")
print()


# 3. TypeError: Wrong Data Type
# =============================
print("3. TypeError")
print("-" * 40)

# WRONG:
try:
    result = "5" + 5  # Can't add string and int
except TypeError as e:
    print(f"❌ TypeError: {e}")

# RIGHT:
result = int("5") + 5
print(f"✅ Correct: {result}")

# Common in automation: Wrong argument types
def click_element(selector, timeout):
    """Simulate clicking with timeout."""
    if not isinstance(selector, str):
        raise TypeError("Selector must be a string")
    if not isinstance(timeout, (int, float)):
        raise TypeError("Timeout must be a number")
    print(f"✅ Clicking '{selector}' with timeout {timeout}ms")

click_element("#submit", 5000)

try:
    click_element(123, "5000")  # Wrong types
except TypeError as e:
    print(f"❌ {e}")
print()


# 4. ValueError: Invalid Value
# ============================
print("4. ValueError")
print("-" * 40)

# WRONG:
try:
    age = int("twenty")  # Can't convert to int
except ValueError as e:
    print(f"❌ ValueError: {e}")

# RIGHT:
age = int("20")
print(f"✅ Correct: {age}")

# Common in automation: Invalid data
def set_age(age_str):
    """Set user age with validation."""
    try:
        age = int(age_str)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")
        print(f"✅ Age set to: {age}")
    except ValueError as e:
        print(f"❌ Invalid age: {e}")

set_age("25")
set_age("abc")
set_age("-5")
print()


# 5. IndexError: List Index Out of Range
# ======================================
print("5. IndexError")
print("-" * 40)

fruits = ["apple", "banana", "orange"]

# WRONG:
try:
    print(fruits[10])  # Index doesn't exist
except IndexError as e:
    print(f"❌ IndexError: {e}")

# RIGHT:
if len(fruits) > 0:
    print(f"✅ First fruit: {fruits[0]}")

# Safe access function
def safe_get(lst, index, default=None):
    """Safely get item from list."""
    try:
        return lst[index]
    except IndexError:
        return default

print(f"✅ Safe access: {safe_get(fruits, 1)}")
print(f"✅ Safe access with default: {safe_get(fruits, 10, 'Not found')}")
print()


# 6. KeyError: Dictionary Key Not Found
# =====================================
print("6. KeyError")
print("-" * 40)

user = {
    "name": "Alice",
    "email": "alice@example.com"
}

# WRONG:
try:
    print(user["age"])  # Key doesn't exist
except KeyError as e:
    print(f"❌ KeyError: {e}")

# RIGHT:
print(f"✅ Using get(): {user.get('age', 'Not specified')}")

# Common in automation: Missing test data
def get_test_user_data(user_id):
    """Get test user data safely."""
    test_users = {
        "user1": {"name": "Test User 1", "email": "test1@example.com"},
        "user2": {"name": "Test User 2", "email": "test2@example.com"}
    }

    if user_id not in test_users:
        raise KeyError(f"Test user '{user_id}' not found")

    return test_users[user_id]

try:
    print(f"✅ User found: {get_test_user_data('user1')}")
    get_test_user_data('user999')
except KeyError as e:
    print(f"❌ {e}")
print()


# 7. AttributeError: Attribute Doesn't Exist
# ==========================================
print("7. AttributeError")
print("-" * 40)

# WRONG:
try:
    text = "hello"
    text.append("!")  # Strings don't have append
except AttributeError as e:
    print(f"❌ AttributeError: {e}")

# RIGHT:
text = "hello" + "!"
print(f"✅ Correct: {text}")

# Common in automation: Calling wrong method
class Page:
    """Simulate a page object."""
    def __init__(self):
        self.title = "Test Page"

    def get_title(self):
        return self.title

page = Page()
print(f"✅ Page title: {page.get_title()}")

try:
    page.click()  # Method doesn't exist
except AttributeError as e:
    print(f"❌ AttributeError: {e}")
print()


# 8. FileNotFoundError
# ===================
print("8. FileNotFoundError")
print("-" * 40)

# WRONG:
try:
    with open("nonexistent.txt", 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"❌ FileNotFoundError: {e}")

# RIGHT: Check if file exists first
from pathlib import Path

def read_config(filename):
    """Read config file safely."""
    config_path = Path(filename)

    if not config_path.exists():
        print(f"❌ Config file not found: {filename}")
        return {}

    with open(config_path, 'r') as f:
        print(f"✅ Reading config from: {filename}")
        return f.read()

read_config("config.json")
print()


# 9. ZeroDivisionError
# ===================
print("9. ZeroDivisionError")
print("-" * 40)

# WRONG:
try:
    result = 100 / 0
except ZeroDivisionError:
    print("❌ ZeroDivisionError: Cannot divide by zero")

# RIGHT:
def safe_divide(a, b):
    """Safely divide two numbers."""
    if b == 0:
        print("❌ Cannot divide by zero")
        return None
    return a / b

print(f"✅ 100 / 5 = {safe_divide(100, 5)}")
print(f"✅ 100 / 0 = {safe_divide(100, 0)}")

# Automation example: Calculate success rate
def calculate_success_rate(passed, total):
    """Calculate test success rate."""
    if total == 0:
        print("❌ No tests run")
        return 0.0

    rate = (passed / total) * 100
    print(f"✅ Success rate: {rate:.1f}%")
    return rate

calculate_success_rate(45, 50)
calculate_success_rate(0, 0)
print()


# 10. ImportError / ModuleNotFoundError
# =====================================
print("10. ImportError / ModuleNotFoundError")
print("-" * 40)

# WRONG:
try:
    import nonexistent_module
except ModuleNotFoundError as e:
    print(f"❌ ModuleNotFoundError: {e}")

# RIGHT: Check and provide helpful message
def safe_import(module_name):
    """Safely import a module."""
    try:
        __import__(module_name)
        print(f"✅ Module '{module_name}' imported successfully")
        return True
    except ModuleNotFoundError:
        print(f"❌ Module '{module_name}' not found")
        print(f"   Install it with: pip install {module_name}")
        return False

safe_import("json")  # Built-in module
safe_import("playwright")  # Might not be installed
print()


# 11. IndentationError
# ===================
print("11. IndentationError")
print("-" * 40)
print("❌ Common causes:")
print("   - Mixing tabs and spaces")
print("   - Inconsistent indentation")
print("   - Missing indentation after colon")
print()

# WRONG (in actual code):
# def test_login():
# print("Testing login")  # IndentationError

# RIGHT:
def test_login():
    print("✅ Testing login with correct indentation")

test_login()
print()


# 12. AssertionError (Common in Testing)
# ======================================
print("12. AssertionError (Common in Testing)")
print("-" * 40)

def verify_title(actual, expected):
    """Verify page title matches expected."""
    try:
        assert actual == expected, f"Expected '{expected}', got '{actual}'"
        print(f"✅ Title matches: {expected}")
    except AssertionError as e:
        print(f"❌ AssertionError: {e}")

verify_title("Home Page", "Home Page")
verify_title("Wrong Page", "Home Page")
print()


# 13. Error Prevention Checklist
# ==============================
print("13. Error Prevention Checklist")
print("-" * 40)
print("""
✅ Before running code:
1. Check variable names are correct (NameError)
2. Verify data types match (TypeError)
3. Validate input values (ValueError)
4. Check list/dict keys exist (IndexError, KeyError)
5. Ensure files exist before opening (FileNotFoundError)
6. Test with edge cases (empty lists, zero values)
7. Use IDE syntax checking (SyntaxError, IndentationError)

💡 Debugging Tips:
- Read error messages carefully
- Check the line number in the traceback
- Print variables to see their values
- Test small pieces of code separately
- Use type hints to catch type errors early
""")


print("=" * 60)
print("Key Takeaways:")
print("- Most errors have clear messages telling you what's wrong")
print("- Check variable names, types, and values")
print("- Use defensive programming (validate inputs)")
print("- Test with edge cases and invalid data")
print("=" * 60)
