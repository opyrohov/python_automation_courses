"""
Lecture 8 - Example 3: Exception Types and Custom Exceptions
============================================================
Learn about different exception types and creating custom exceptions.
"""

print("=" * 60)
print("EXAMPLE 3: EXCEPTION TYPES")
print("=" * 60)
print()


# 1. Exception Hierarchy
# ======================
print("1. Exception Hierarchy")
print("-" * 40)
print("""
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception (Most exceptions inherit from this)
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── AttributeError
    ├── FileNotFoundError
    └── ... (many more)
""")
print()


# 2. Catching Multiple Exceptions
# ===============================
print("2. Catching Multiple Exceptions")
print("-" * 40)

def process_data(data, index):
    """Process data with multiple error handling."""
    try:
        value = data[index]
        number = int(value)
        result = 100 / number
        print(f"✅ Result: {result}")
        return result

    except (IndexError, KeyError) as e:
        print(f"❌ Data access error: {e}")
        return None

    except ValueError as e:
        print(f"❌ Invalid value: {e}")
        return None

    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
        return None

    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}: {e}")
        return None

# Test different scenarios
print("Test 1: Valid data")
process_data([1, 2, 3], 1)

print("\nTest 2: Index error")
process_data([1, 2, 3], 10)

print("\nTest 3: Value error")
process_data(['a', 'b', 'c'], 0)

print("\nTest 4: Zero division")
process_data([0, 1, 2], 0)
print()


# 3. Raising Exceptions
# =====================
print("3. Raising Exceptions")
print("-" * 40)

def validate_age(age):
    """Validate user age."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 150:
        raise ValueError("Age seems unrealistic")

    print(f"✅ Valid age: {age}")
    return age

try:
    validate_age(25)
    validate_age("25")
except (TypeError, ValueError) as e:
    print(f"❌ {type(e).__name__}: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"❌ {e}")
print()


# 4. Custom Exception Classes
# ===========================
print("4. Custom Exception Classes")
print("-" * 40)

class TestAutomationError(Exception):
    """Base exception for test automation errors."""
    pass

class ElementNotFoundError(TestAutomationError):
    """Raised when an element is not found."""
    def __init__(self, selector, timeout=None):
        self.selector = selector
        self.timeout = timeout
        message = f"Element '{selector}' not found"
        if timeout:
            message += f" within {timeout}ms"
        super().__init__(message)

class PageLoadError(TestAutomationError):
    """Raised when page fails to load."""
    def __init__(self, url, status_code=None):
        self.url = url
        self.status_code = status_code
        message = f"Failed to load page: {url}"
        if status_code:
            message += f" (Status: {status_code})"
        super().__init__(message)

class TestDataError(TestAutomationError):
    """Raised when test data is invalid."""
    pass

# Using custom exceptions
def click_element(selector, timeout=5000):
    """Simulate clicking an element."""
    # Simulate element not found
    if selector == "#missing":
        raise ElementNotFoundError(selector, timeout)

    print(f"✅ Clicked element: {selector}")

try:
    click_element("#submit")
    click_element("#missing")
except ElementNotFoundError as e:
    print(f"❌ {type(e).__name__}: {e}")
    print(f"   Selector: {e.selector}")
    print(f"   Timeout: {e.timeout}")
print()


# 5. Exception Context and Chaining
# =================================
print("5. Exception Context and Chaining")
print("-" * 40)

def load_user_data(user_id):
    """Load user data with context."""
    try:
        # Simulate database query
        if user_id not in ['user1', 'user2']:
            raise KeyError(f"User {user_id} not found in database")

        user = {'id': user_id, 'name': 'Test User'}
        return user

    except KeyError as e:
        # Chain the exception with more context
        raise TestDataError(f"Failed to load test user: {user_id}") from e

try:
    load_user_data('user1')
    print("✅ User loaded successfully")

    load_user_data('user999')
except TestDataError as e:
    print(f"❌ {type(e).__name__}: {e}")
    print(f"   Caused by: {type(e.__cause__).__name__}: {e.__cause__}")
print()


# 6. Context Managers and Exceptions
# ==================================
print("6. Context Managers and Exceptions")
print("-" * 40)

class TestContext:
    """Custom context manager for tests."""

    def __init__(self, test_name):
        self.test_name = test_name

    def __enter__(self):
        print(f"🚀 Starting test: {self.test_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"✅ Test passed: {self.test_name}")
        else:
            print(f"❌ Test failed: {self.test_name}")
            print(f"   Error: {exc_type.__name__}: {exc_val}")

        # Return False to propagate exception, True to suppress it
        return False

# Using the context manager
with TestContext("Login Test"):
    print("   Executing login test...")
    # Test passes

print()

try:
    with TestContext("Broken Test"):
        print("   Executing broken test...")
        raise ValueError("Something went wrong")
except ValueError:
    print("   Exception was propagated")
print()


# 7. Validation with Custom Exceptions
# ====================================
print("7. Validation with Custom Exceptions")
print("-" * 40)

class ValidationError(Exception):
    """Raised when validation fails."""
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

def validate_login_data(username, password):
    """Validate login credentials."""
    if not username:
        raise ValidationError("username", "Username cannot be empty")

    if len(username) < 3:
        raise ValidationError("username", "Username must be at least 3 characters")

    if not password:
        raise ValidationError("password", "Password cannot be empty")

    if len(password) < 6:
        raise ValidationError("password", "Password must be at least 6 characters")

    print(f"✅ Validation passed for user: {username}")

# Test validation
test_cases = [
    ("validuser", "password123"),
    ("", "password123"),
    ("ab", "password123"),
    ("validuser", "pass")
]

for username, password in test_cases:
    try:
        print(f"\nValidating: username='{username}', password='{password}'")
        validate_login_data(username, password)
    except ValidationError as e:
        print(f"❌ Validation failed - {e}")
print()


# 8. Retry Logic with Exceptions
# ==============================
print("8. Retry Logic with Exceptions")
print("-" * 40)

import time

class RetryableError(Exception):
    """Exception that can be retried."""
    pass

def unreliable_operation(attempt_number):
    """Simulate an unreliable operation."""
    if attempt_number < 3:
        raise RetryableError(f"Temporary failure (attempt {attempt_number})")
    return "Success!"

def retry_operation(func, max_retries=3, delay=1):
    """Retry an operation multiple times."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}/{max_retries}...")
            result = func(attempt)
            print(f"✅ Operation succeeded: {result}")
            return result

        except RetryableError as e:
            print(f"❌ {e}")
            if attempt < max_retries:
                print(f"   Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"   Max retries reached")
                raise

retry_operation(unreliable_operation, max_retries=5, delay=0.5)
print()


# 9. Automation-Specific Exceptions
# =================================
print("9. Automation-Specific Exceptions")
print("-" * 40)

class AutomationException(Exception):
    """Base class for automation exceptions."""
    pass

class BrowserError(AutomationException):
    """Browser-related errors."""
    pass

class TimeoutException(AutomationException):
    """Timeout errors."""
    pass

class AssertionFailure(AutomationException):
    """Test assertion failures."""
    pass

def wait_for_element(selector, timeout=5000):
    """Wait for element to appear."""
    # Simulate timeout
    if selector == "#slow-element":
        raise TimeoutException(
            f"Element '{selector}' did not appear within {timeout}ms"
        )

    print(f"✅ Element found: {selector}")

def verify_element_text(actual, expected):
    """Verify element text."""
    if actual != expected:
        raise AssertionFailure(
            f"Text mismatch:\n"
            f"  Expected: '{expected}'\n"
            f"  Actual: '{actual}'"
        )

    print(f"✅ Text matches: {expected}")

# Test automation exceptions
try:
    wait_for_element("#button")
    verify_element_text("Home", "Home")

    wait_for_element("#slow-element")
except (TimeoutException, AssertionFailure) as e:
    print(f"❌ Test failed: {type(e).__name__}")
    print(f"   {e}")
print()


# 10. Exception Best Practices
# ============================
print("10. Exception Best Practices")
print("-" * 40)
print("""
✅ Creating Custom Exceptions:
1. Inherit from Exception (or a more specific built-in exception)
2. Add custom attributes for context
3. Use descriptive names ending in 'Error' or 'Exception'
4. Group related exceptions under a base exception
5. Include helpful error messages

✅ Using Exceptions:
1. Catch specific exceptions, not broad 'Exception'
2. Only catch exceptions you can handle
3. Re-raise if you can't handle it
4. Add context when re-raising
5. Clean up resources in finally blocks

❌ Common Mistakes:
1. Catching exceptions and doing nothing (silent failures)
2. Using exceptions for control flow
3. Creating too many custom exception classes
4. Not including enough information in error messages
5. Catching BaseException (too broad)
""")


print("=" * 60)
print("Key Takeaways:")
print("- Custom exceptions make code more maintainable")
print("- Include context in exception messages")
print("- Use exception hierarchies for related errors")
print("- Handle exceptions at the appropriate level")
print("=" * 60)
