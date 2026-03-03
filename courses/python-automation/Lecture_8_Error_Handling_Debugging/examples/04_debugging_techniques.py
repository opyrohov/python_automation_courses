"""
Lecture 8 - Example 4: Debugging Techniques
===========================================
Learn practical debugging techniques for Python and test automation.
"""

print("=" * 60)
print("EXAMPLE 4: DEBUGGING TECHNIQUES")
print("=" * 60)
print()


# 1. Print Debugging (Quick and Simple)
# =====================================
print("1. Print Debugging")
print("-" * 40)

def calculate_total(items):
    """Calculate total price of items."""
    print(f"DEBUG: calculate_total called with {len(items)} items")

    total = 0
    for i, item in enumerate(items):
        print(f"DEBUG: Processing item {i}: {item}")
        price = item.get('price', 0)
        quantity = item.get('quantity', 1)

        print(f"DEBUG: price={price}, quantity={quantity}")

        item_total = price * quantity
        print(f"DEBUG: item_total={item_total}")

        total += item_total

    print(f"DEBUG: Final total={total}")
    return total

items = [
    {'name': 'Laptop', 'price': 999, 'quantity': 1},
    {'name': 'Mouse', 'price': 29, 'quantity': 2}
]

result = calculate_total(items)
print(f"✅ Total: ${result}")
print()


# 2. Using repr() for Better Debugging
# ====================================
print("2. Using repr() for Better Debugging")
print("-" * 40)

def debug_variable(var_name, value):
    """Print variable with type and representation."""
    print(f"{var_name} = {repr(value)}")
    print(f"  Type: {type(value).__name__}")
    print(f"  Str: {str(value)}")

# Debug different types
debug_variable("text", "hello")
debug_variable("number", 42)
debug_variable("empty_string", "")
debug_variable("none_value", None)
debug_variable("list", [1, 2, 3])
print()


# 3. Assertion for Sanity Checks
# ==============================
print("3. Assertion for Sanity Checks")
print("-" * 40)

def process_order(order_id, items):
    """Process an order with sanity checks."""
    # Sanity checks during development
    assert isinstance(order_id, int), "Order ID must be integer"
    assert order_id > 0, "Order ID must be positive"
    assert len(items) > 0, "Order must have at least one item"

    print(f"✅ Processing order #{order_id} with {len(items)} items")

try:
    process_order(123, [{'item': 'test'}])
    process_order("123", [])  # Will fail assertion
except AssertionError as e:
    print(f"❌ Assertion failed: {e}")
print()


# 4. Stack Trace Analysis
# =======================
print("4. Stack Trace Analysis")
print("-" * 40)

def level_1():
    """First level function."""
    print("  Level 1: Calling level_2()")
    level_2()

def level_2():
    """Second level function."""
    print("  Level 2: Calling level_3()")
    level_3()

def level_3():
    """Third level function with error."""
    print("  Level 3: Attempting division")
    result = 10 / 0  # Error here

try:
    level_1()
except ZeroDivisionError:
    print("\n❌ Error occurred! Stack trace shows:")
    print("   level_1() called level_2()")
    print("   level_2() called level_3()")
    print("   level_3() had the error (division by zero)")
    print("\n💡 Read stack traces from bottom to top to find the error source!")
print()


# 5. Debugging with Try/Except and Traceback
# ==========================================
print("5. Debugging with Traceback")
print("-" * 40)

import traceback

def buggy_function():
    """Function with a bug."""
    data = {'users': [{'name': 'Alice'}, {'name': 'Bob'}]}
    # Bug: trying to access index that doesn't exist
    return data['users'][5]['name']

try:
    buggy_function()
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
    print("\nFull traceback:")
    print(traceback.format_exc())
print()


# 6. Defensive Programming
# ========================
print("6. Defensive Programming")
print("-" * 40)

def safe_get_user_email(users, user_id):
    """Safely get user email with defensive checks."""

    # Check 1: Valid input
    if not isinstance(users, dict):
        print("❌ ERROR: users must be a dictionary")
        return None

    # Check 2: User exists
    if user_id not in users:
        print(f"❌ ERROR: User {user_id} not found")
        print(f"   Available users: {list(users.keys())}")
        return None

    user = users[user_id]

    # Check 3: User has email
    if not isinstance(user, dict):
        print(f"❌ ERROR: User data is invalid")
        return None

    if 'email' not in user:
        print(f"❌ ERROR: User {user_id} has no email")
        return None

    email = user['email']

    # Check 4: Email is valid
    if not email or '@' not in email:
        print(f"❌ ERROR: Invalid email format: {email}")
        return None

    print(f"✅ Email found: {email}")
    return email

# Test with different scenarios
users = {
    'user1': {'name': 'Alice', 'email': 'alice@example.com'},
    'user2': {'name': 'Bob', 'email': 'invalid-email'},
    'user3': {'name': 'Charlie'}
}

safe_get_user_email(users, 'user1')
safe_get_user_email(users, 'user999')
safe_get_user_email(users, 'user2')
safe_get_user_email(users, 'user3')
print()


# 7. Debugging Helper Functions
# =============================
print("7. Debugging Helper Functions")
print("-" * 40)

def debug_function_call(func):
    """Decorator to debug function calls."""
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling {func.__name__}")
        print(f"   Args: {args}")
        print(f"   Kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
            print(f"   ✅ Returned: {result}")
            return result
        except Exception as e:
            print(f"   ❌ Error: {type(e).__name__}: {e}")
            raise

    return wrapper

@debug_function_call
def add_numbers(a, b):
    """Add two numbers."""
    return a + b

@debug_function_call
def divide_numbers(a, b):
    """Divide two numbers."""
    return a / b

add_numbers(5, 3)
try:
    divide_numbers(10, 0)
except ZeroDivisionError:
    pass
print()


# 8. State Inspection
# ==================
print("8. State Inspection")
print("-" * 40)

class TestRunner:
    """Simulate a test runner with state."""

    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.current_test = None

    def run_test(self, test_name, should_pass=True):
        """Run a test and track results."""
        self.current_test = test_name
        self.tests_run += 1

        print(f"Running: {test_name}")
        self.print_state()

        if should_pass:
            self.tests_passed += 1
            print("  ✅ Passed")
        else:
            self.tests_failed += 1
            print("  ❌ Failed")

        self.current_test = None

    def print_state(self):
        """Debug: Print current state."""
        print(f"  DEBUG STATE:")
        print(f"    Current test: {self.current_test}")
        print(f"    Tests run: {self.tests_run}")
        print(f"    Passed: {self.tests_passed}")
        print(f"    Failed: {self.tests_failed}")

runner = TestRunner()
runner.run_test("test_login", True)
runner.run_test("test_signup", False)
print()


# 9. Debugging Automation Tests
# =============================
print("9. Debugging Automation Tests")
print("-" * 40)

def debug_page_state(page_data):
    """Debug current page state."""
    print("📄 PAGE STATE DEBUG:")
    print(f"  URL: {page_data.get('url', 'Unknown')}")
    print(f"  Title: {page_data.get('title', 'Unknown')}")
    print(f"  Loaded: {page_data.get('loaded', False)}")

    elements = page_data.get('elements', {})
    print(f"  Elements found: {len(elements)}")
    for selector, found in elements.items():
        status = "✅" if found else "❌"
        print(f"    {status} {selector}")

# Simulate page state
page_state = {
    'url': 'https://example.com/login',
    'title': 'Login Page',
    'loaded': True,
    'elements': {
        '#username': True,
        '#password': True,
        '#submit': True,
        '#error-message': False
    }
}

debug_page_state(page_state)
print()


# 10. Debugging Checklist
# =======================
print("10. Debugging Checklist")
print("-" * 40)
print("""
🔍 When you encounter a bug:

1. READ THE ERROR MESSAGE
   - What type of error is it?
   - What line number?
   - What is the error message saying?

2. LOCATE THE PROBLEM
   - Check the stack trace
   - Identify which function failed
   - Find the exact line with the error

3. UNDERSTAND THE CONTEXT
   - Print variable values before the error
   - Check data types
   - Verify assumptions about the data

4. FORM A HYPOTHESIS
   - What do you think caused the error?
   - What should the code be doing?
   - What is it actually doing?

5. TEST YOUR HYPOTHESIS
   - Add print statements
   - Use the debugger
   - Try with different inputs
   - Isolate the problem

6. FIX THE BUG
   - Make the smallest change possible
   - Test the fix works
   - Test it doesn't break other things

7. PREVENT IT HAPPENING AGAIN
   - Add validation
   - Add error handling
   - Add tests
   - Document the fix
""")

# Example of the debugging process
def example_debugging_process():
    """Example: Debugging a list comprehension."""
    print("\n📝 Example Debugging Process:")
    print("-" * 40)

    # Original buggy code (commented out):
    # numbers = [1, 2, '3', 4, '5']
    # doubled = [n * 2 for n in numbers]  # TypeError!

    # Step 1: Identify the problem
    print("Step 1: Error - TypeError: can't multiply string by int")

    # Step 2: Add debugging
    numbers = [1, 2, '3', 4, '5']
    print(f"Step 2: numbers = {numbers}")
    print(f"        Types: {[type(n).__name__ for n in numbers]}")

    # Step 3: Fix the issue
    print("\nStep 3: Filter to only integers")
    doubled = [n * 2 for n in numbers if isinstance(n, int)]
    print(f"        Doubled (integers only): {doubled}")

    # Step 4: Better solution - convert strings
    print("\nStep 4: Better - convert all to integers")
    try:
        doubled = [int(n) * 2 for n in numbers]
        print(f"        Doubled (all converted): {doubled}")
    except ValueError as e:
        print(f"        ❌ Conversion failed: {e}")

example_debugging_process()
print()


print("=" * 60)
print("Key Takeaways:")
print("- Start with simple print debugging")
print("- Read error messages and stack traces carefully")
print("- Use defensive programming to catch errors early")
print("- Break down complex problems into smaller parts")
print("- Add logging and debugging helpers to your code")
print("=" * 60)
