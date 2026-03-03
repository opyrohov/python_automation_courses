# Lecture 8: Error Handling & Debugging - Exercise Solutions

This file contains solutions for all exercises in Lecture 8.

## Exercise 1: Basic Error Handling

### Exercise 1.1: Basic Try/Except
```python
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

# Test
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None
```

### Exercise 1.2: Multiple Exceptions
```python
def get_list_item(lst, index):
    """Safely get item from list."""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid type"

# Test
print(get_list_item([1, 2, 3], 1))  # 2
print(get_list_item([1, 2, 3], 10))  # "Index out of range"
print(get_list_item("not a list", 0))  # "Invalid type"
```

### Exercise 1.3: Try/Except/Else
```python
def convert_to_int(value):
    """Convert value to integer."""
    try:
        result = int(value)
    except ValueError:
        print("Cannot convert to integer")
        return None
    else:
        print(f"Conversion successful: {result}")
        return result

# Test
convert_to_int("42")  # Prints success message
convert_to_int("abc")  # Prints error message
```

### Exercise 1.4: Try/Except/Finally
```python
def read_file_lines(filename):
    """Read and count lines in file."""
    file = None
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        print(f"File has {len(lines)} lines")
        return len(lines)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0
    finally:
        if file:
            file.close()
        print("File operation complete")
```

### Exercise 1.5: Dictionary Access
```python
def get_user_email(users, user_id):
    """Get user email from dictionary."""
    try:
        return users[user_id]['email']
    except KeyError:
        return "User not found"

# Test
users = {
    "user1": {"email": "user1@example.com"},
    "user2": {"email": "user2@example.com"}
}
print(get_user_email(users, "user1"))  # user1@example.com
print(get_user_email(users, "user999"))  # User not found
```

### Exercise 1.6: String to Number Validation
```python
def validate_age(age_str):
    """Validate age string."""
    try:
        age = int(age_str)
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        print(f"Valid age: {age}")
        return True
    except ValueError as e:
        print(f"Invalid age: {e}")
        return False

# Test
validate_age("25")  # Valid
validate_age("abc")  # Invalid
validate_age("-5")  # Invalid
validate_age("200")  # Invalid
```

### Exercise 1.7: List Operations
```python
def safe_pop(lst, index=None):
    """Safely remove item from list."""
    try:
        if index is None:
            return lst.pop()
        else:
            return lst.pop(index)
    except IndexError:
        print("Index out of range")
        return None

# Test
numbers = [1, 2, 3, 4, 5]
print(safe_pop(numbers))  # 5
print(safe_pop(numbers, 0))  # 1
print(safe_pop(numbers, 100))  # None
```

### Exercise 1.8: Nested Try/Except
```python
def process_user_age(data):
    """Process user age from nested dictionary."""
    try:
        user = data['user']
        age_str = user['age']

        try:
            age = int(age_str)
            print(f"User age: {age}")
            return age
        except ValueError:
            print("Invalid age format")
            return None

    except KeyError as e:
        print(f"Missing key: {e}")
        return None

# Test
test_data = [
    {"user": {"age": "25"}},
    {"user": {"name": "Bob"}},
    {"user": {"age": "twenty"}},
    {"name": "Charlie"}
]
for data in test_data:
    print(process_user_age(data))
```

### BONUS: Custom Exception
```python
class InvalidCredentialsError(Exception):
    """Raised when credentials are invalid."""
    pass

def validate_login(username, password):
    """Validate login credentials."""
    if not username or not password:
        raise InvalidCredentialsError("Username and password required")

    if len(password) < 6:
        raise InvalidCredentialsError("Password must be at least 6 characters")

    print(f"Valid credentials for: {username}")
    return True

# Test
try:
    validate_login("testuser", "password123")  # Valid
    validate_login("", "password")  # Raises error
except InvalidCredentialsError as e:
    print(f"Login validation failed: {e}")
```

---

## Exercise 2: Debugging Practice

### Exercise 2.1: Fix the Syntax Error
```python
def calculate_total(items):
    """Calculate total price."""
    total = 0
    for item in items:
        total += item['price']
    return total

# Test
test_items = [{'price': 10}, {'price': 20}, {'price': 30}]
print(f"Total: {calculate_total(test_items)}")  # 60
```

### Exercise 2.2: Fix the NameError
```python
def greet_user():
    """Greet a user."""
    message = "Hello"
    user_name = "User"  # Fixed: Define variable
    print(f"{message}, {user_name}!")  # Fixed: Correct spelling

greet_user()
```

### Exercise 2.3: Fix the IndexError
```python
def get_first_and_last(items):
    """Get first and last items from a list."""
    if not items:  # Fixed: Check if list is empty
        print("List is empty")
        return None, None

    first = items[0]
    last = items[-1]
    return first, last

# Test
print(get_first_and_last([1, 2, 3, 4, 5]))  # (1, 5)
print(get_first_and_last([]))  # (None, None)
```

### Exercise 2.4: Fix the KeyError
```python
def get_user_info(user):
    """Get user information."""
    name = user.get('name', 'Unknown')
    email = user.get('email', 'No email')
    age = user.get('age', 'Not specified')
    return f"{name} ({email}), Age: {age}"

# Test
user1 = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
user2 = {'name': 'Bob', 'email': 'bob@example.com'}
print(get_user_info(user1))
print(get_user_info(user2))
```

### Exercise 2.5: Fix the TypeError
```python
def calculate_average(numbers):
    """Calculate average of numbers."""
    if not isinstance(numbers, list):
        print("Error: Input must be a list")
        return None

    if len(numbers) == 0:
        print("Error: Cannot calculate average of empty list")
        return None

    # Check all items are numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            print(f"Error: {num} is not a number")
            return None

    total = sum(numbers)
    average = total / len(numbers)
    return average

# Test
print(calculate_average([10, 20, 30, 40]))  # 25.0
print(calculate_average("not a list"))  # None
print(calculate_average([]))  # None
```

### Exercise 2.6: Fix the Logic Error
```python
def is_adult(age):
    """Check if person is an adult (18 or older)."""
    if age >= 18:  # Fixed: >= not <
        return True
    else:
        return False

# Or more concise:
def is_adult(age):
    return age >= 18

# Test
print(f"Age 25 is adult: {is_adult(25)}")  # True
print(f"Age 15 is adult: {is_adult(15)}")  # False
```

### Exercise 2.7: Debug with Print Statements
```python
def find_max_price(products):
    """Find product with maximum price."""
    if not products:
        print("DEBUG: Empty products list")
        return None

    max_price = 0
    max_product = None

    for product in products:
        print(f"DEBUG: Checking product: {product['name']}, price: {product['price']}")

        if product['price'] > max_price:
            max_price = product['price']
            max_product = product
            print(f"DEBUG: New max found: {max_product['name']}")

    print(f"DEBUG: Final max price: {max_price}")
    return max_product

# Test
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 29},
    {'name': 'Keyboard', 'price': 79}
]
result = find_max_price(products)
print(f"Max price product: {result}")
```

### Exercise 2.8: Fix the Infinite Loop
```python
def count_to_ten():
    """Count from 1 to 10."""
    count = 1
    while count <= 10:  # Fixed: <= instead of <
        print(count)
        count += 1  # Fixed: Added increment
    return count

count_to_ten()
```

### Exercise 2.9: Debug Data Processing
```python
def process_test_results(results):
    """Process test results and calculate statistics."""
    if not results:  # Fixed: Check for empty list
        return {
            'total': 0,
            'passed': 0,
            'success_rate': 0
        }

    total = 0
    passed = 0

    for result in results:
        total += 1
        # Fixed: Use 'result' key instead of 'status'
        if result['result'] == 'pass':
            passed += 1

    success_rate = (passed / total) * 100
    return {
        'total': total,
        'passed': passed,
        'success_rate': success_rate
    }

# Test
test_results = [
    {'name': 'test1', 'result': 'pass'},
    {'name': 'test2', 'result': 'fail'},
    {'name': 'test3', 'result': 'pass'}
]
print(process_test_results(test_results))
print(process_test_results([]))
```

### Exercise 2.10: Debug Complex Function
```python
def calculate_discount(products, discount_code):
    """Calculate total with discount."""
    total = 0

    for product in products:
        price = product['price']
        quantity = product['quantity']
        total += price * quantity

    discounts = {
        'SAVE10': 0.10,
        'SAVE20': 0.20,
        'SAVE30': 0.30
    }

    # Fixed: Check if discount code exists
    if discount_code not in discounts:
        print(f"Invalid discount code: {discount_code}")
        return total

    discount = discounts[discount_code]

    # Fixed: Calculate discount amount, then subtract
    discount_amount = total * discount
    final_total = total - discount_amount

    print(f"Subtotal: ${total:.2f}")
    print(f"Discount ({discount_code}): -${discount_amount:.2f}")
    print(f"Final total: ${final_total:.2f}")

    return final_total

# Test
products = [
    {'name': 'Laptop', 'price': 999, 'quantity': 1},
    {'name': 'Mouse', 'price': 29, 'quantity': 2}
]
print(calculate_discount(products, 'SAVE10'))
print(calculate_discount(products, 'INVALID'))
```

### BONUS: Debug with Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def login_user(username, password, user_database):
    """Login user with debugging."""
    logging.info(f"Login attempt for username: {username}")
    logging.debug(f"Checking if user exists in database...")

    if username in user_database:
        logging.debug(f"User found: {username}")
        logging.debug("Checking password...")

        if user_database[username]['password'] == password:
            logging.info(f"Login successful for: {username}")
            return True
        else:
            logging.warning(f"Invalid password for: {username}")
            return False
    else:
        logging.warning(f"User not found: {username}")
        return False

# Test
users = {
    'testuser': {'password': 'test123', 'email': 'test@example.com'}
}
login_user('testuser', 'test123', users)
login_user('testuser', 'wrong', users)
login_user('unknown', 'test123', users)
```

---

## Exercise 3: Playwright Error Handling

### Exercise 3.1: Safe Click Function
```python
from pathlib import Path

def safe_click(page, selector, timeout=5000):
    """Safely click an element."""
    try:
        page.click(selector, timeout=timeout)
        print(f"✅ Clicked: {selector}")
        return True
    except Exception as e:  # TimeoutError in real Playwright
        print(f"❌ Could not click {selector}: {e}")

        # Take screenshot
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        page.screenshot(path=str(screenshots_dir / f"click_error_{selector.replace('#', '')}.png"))

        return False
```

### Exercise 3.2: Retry Click Function
```python
import time

def retry_click(page, selector, retries=3):
    """Click element with retries."""
    for attempt in range(1, retries + 1):
        try:
            print(f"Attempt {attempt}/{retries}: Clicking {selector}")
            page.click(selector, timeout=5000)
            print(f"✅ Successfully clicked: {selector}")
            return True
        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt < retries:
                print("   Retrying in 1s...")
                time.sleep(1)

    print(f"❌ Failed to click {selector} after {retries} attempts")
    return False
```

### Exercise 3.3: Safe Navigation
```python
def safe_goto(page, url, timeout=30000):
    """Safely navigate to URL."""
    try:
        print(f"🌐 Navigating to: {url}")
        response = page.goto(url, timeout=timeout)

        if response and response.status >= 400:
            print(f"❌ HTTP error: {response.status}")
            return False

        print(f"✅ Successfully loaded: {url}")
        return True

    except Exception as e:
        print(f"❌ Navigation failed: {e}")
        return False
```

### Exercise 3.4: Wait for Element
```python
from pathlib import Path

def wait_for_element(page, selector, timeout=10000):
    """Wait for element to be visible."""
    try:
        page.wait_for_selector(selector, state="visible", timeout=timeout)
        print(f"✅ Element found: {selector}")
        return True
    except Exception as e:
        print(f"❌ Element not found: {selector}")
        print(f"   Timeout: {timeout}ms")

        # Take screenshot
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        page.screenshot(path=str(screenshots_dir / f"wait_error_{selector.replace('#', '')}.png"))

        return False
```

### Exercise 3.5: Safe Text Extraction
```python
def safe_get_text(page, selector):
    """Safely get text from element."""
    try:
        text = page.locator(selector).text_content(timeout=5000)
        print(f"✅ Text from {selector}: {text}")
        return text
    except Exception as e:
        print(f"⚠️  Could not get text from {selector}: {e}")
        return None
```

### Exercise 3.6: Safe Form Fill
```python
def safe_fill(page, selector, value):
    """Safely fill input field."""
    try:
        # Check if element is enabled
        if not page.locator(selector).is_enabled(timeout=5000):
            print(f"❌ Element is disabled: {selector}")
            return False

        page.fill(selector, value, timeout=5000)
        print(f"✅ Filled {selector} with: {value}")
        return True

    except Exception as e:
        print(f"❌ Could not fill {selector}: {e}")
        return False
```

### Exercise 3.7: Screenshot on Error Decorator
```python
from pathlib import Path
from datetime import datetime
from functools import wraps

def screenshot_on_error(page):
    """Decorator to take screenshot on error."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Take screenshot
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{func.__name__}_{timestamp}.png"
                filepath = screenshots_dir / filename

                page.screenshot(path=str(filepath))
                print(f"📸 Screenshot saved: {filepath}")

                # Re-raise exception
                raise
        return wrapper
    return decorator

# Usage:
# @screenshot_on_error(page)
# def test_login(page):
#     page.click("#submit")
```

### Exercise 3.8: Page State Validator
```python
from pathlib import Path

class PageNotLoadedError(Exception):
    """Raised when page is not loaded properly."""
    pass

def validate_page_loaded(page, expected_title):
    """Validate page is properly loaded."""
    try:
        actual_title = page.title()

        if actual_title != expected_title:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshots_dir / "page_validation_error.png"))

            raise PageNotLoadedError(
                f"Page title mismatch:\n"
                f"  Expected: '{expected_title}'\n"
                f"  Actual: '{actual_title}'"
            )

        print(f"✅ Page loaded correctly: {expected_title}")

    except PageNotLoadedError:
        raise
    except Exception as e:
        raise PageNotLoadedError(f"Page validation failed: {e}")
```

### Exercise 3.9: Test Context Manager
```python
import logging

class TestContext:
    """Context manager for Playwright tests."""

    def __init__(self, test_name):
        self.test_name = test_name
        self.page = None
        self.browser = None

    def __enter__(self):
        logging.info(f"🚀 Starting test: {self.test_name}")
        # Setup browser (simplified)
        # self.browser = playwright.chromium.launch()
        # self.page = self.browser.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f"❌ Test failed: {self.test_name}")
            logging.error(f"   Error: {exc_val}")

            # Take screenshot on failure
            if self.page:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)
                self.page.screenshot(
                    path=str(screenshots_dir / f"{self.test_name}_error.png")
                )
        else:
            logging.info(f"✅ Test passed: {self.test_name}")

        # Cleanup
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()

        return False  # Don't suppress exceptions
```

### Exercise 3.10: Comprehensive Error Handler
```python
import logging
from pathlib import Path

def handle_playwright_error(error, page, context):
    """Handle Playwright errors comprehensively."""
    error_type = type(error).__name__
    error_msg = str(error)

    report = {
        'error_type': error_type,
        'error_message': error_msg,
        'context': context,
        'suggestions': []
    }

    logging.error(f"❌ {error_type}: {error_msg}")
    logging.error(f"   Context: {context}")

    # Timeout errors
    if "Timeout" in error_type or "timeout" in error_msg.lower():
        suggestions = [
            "Increase timeout value",
            "Check if element selector is correct",
            "Verify element actually appears on page",
            "Check network conditions"
        ]
        report['suggestions'] = suggestions

    # Selector errors
    elif "selector" in error_msg.lower() or "locator" in error_msg.lower():
        suggestions = [
            "Verify selector is correct",
            "Check element has loaded",
            "Try waiting for element first",
            "Use more specific selector"
        ]
        report['suggestions'] = suggestions

    # Navigation errors
    elif "navigation" in error_msg.lower():
        suggestions = [
            "Check URL is accessible",
            "Verify network connectivity",
            "Check page loads in regular browser"
        ]
        report['suggestions'] = suggestions

    # Generic errors
    else:
        suggestions = [
            "Review error message carefully",
            "Check Playwright documentation",
            "Enable debug logging"
        ]
        report['suggestions'] = suggestions

    # Print suggestions
    for suggestion in report['suggestions']:
        logging.info(f"   💡 {suggestion}")

    # Take screenshot
    if page:
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        screenshot_path = screenshots_dir / "error.png"
        page.screenshot(path=str(screenshot_path))
        report['screenshot'] = str(screenshot_path)
        logging.info(f"   📸 Screenshot: {screenshot_path}")

    return report
```

### BONUS 1: Element Presence Checker
```python
import logging

def check_elements_exist(page, selectors):
    """Check if multiple elements exist."""
    results = {}
    missing = []

    for selector in selectors:
        try:
            count = page.locator(selector).count()
            exists = count > 0
            results[selector] = exists

            if not exists:
                missing.append(selector)
                logging.warning(f"❌ Element not found: {selector}")
            else:
                logging.info(f"✅ Element found: {selector}")

        except Exception as e:
            results[selector] = False
            missing.append(selector)
            logging.error(f"❌ Error checking {selector}: {e}")

    if missing:
        logging.warning(f"Missing elements: {missing}")

    return results
```

### BONUS 2: Robust Test Runner
```python
import logging
from pathlib import Path
from datetime import datetime

class RobustTestRunner:
    """Robust test runner with error handling."""

    def __init__(self, page):
        self.page = page
        self.tests = []
        self.results = {
            'passed': [],
            'failed': [],
            'total': 0
        }

    def add_test(self, test_name, test_func):
        """Add test to runner."""
        self.tests.append((test_name, test_func))

    def run_all(self):
        """Run all tests."""
        logging.info(f"🚀 Running {len(self.tests)} tests...")

        for test_name, test_func in self.tests:
            self.results['total'] += 1

            try:
                logging.info(f"\n▶ Running: {test_name}")
                test_func(self.page)
                logging.info(f"✅ PASSED: {test_name}")
                self.results['passed'].append(test_name)

            except Exception as e:
                logging.error(f"❌ FAILED: {test_name}")
                logging.error(f"   Error: {e}")
                self.results['failed'].append({
                    'name': test_name,
                    'error': str(e)
                })

                # Take screenshot
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = screenshots_dir / f"{test_name}_{timestamp}.png"
                self.page.screenshot(path=str(screenshot_path))
                logging.info(f"   📸 Screenshot: {screenshot_path}")

        # Generate report
        self._print_summary()
        return self.results

    def _print_summary(self):
        """Print test summary."""
        total = self.results['total']
        passed = len(self.results['passed'])
        failed = len(self.results['failed'])
        success_rate = (passed / total * 100) if total > 0 else 0

        logging.info("\n" + "=" * 50)
        logging.info("TEST SUMMARY")
        logging.info("=" * 50)
        logging.info(f"Total tests: {total}")
        logging.info(f"Passed: {passed}")
        logging.info(f"Failed: {failed}")
        logging.info(f"Success rate: {success_rate:.1f}%")
        logging.info("=" * 50)

        if self.results['failed']:
            logging.info("\nFailed tests:")
            for failure in self.results['failed']:
                logging.info(f"  - {failure['name']}: {failure['error']}")
```

### BONUS 3: Smart Retry with Exponential Backoff
```python
import time
import logging

def retry_with_backoff(func, max_retries=3):
    """Retry function with exponential backoff."""
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Attempt {attempt}/{max_retries}")
            result = func()
            logging.info(f"✅ Success on attempt {attempt}")
            return result

        except Exception as e:
            last_exception = e
            logging.warning(f"❌ Attempt {attempt} failed: {e}")

            if attempt < max_retries:
                # Exponential backoff: 1s, 2s, 4s, 8s...
                wait_time = 2 ** (attempt - 1)
                logging.info(f"   Retrying in {wait_time}s...")
                time.sleep(wait_time)

    # All retries failed
    logging.error(f"❌ All {max_retries} attempts failed")
    raise last_exception
```

---

## Key Takeaways

1. **Always handle exceptions**: Never let unexpected errors crash your tests
2. **Take screenshots on errors**: Visual context is invaluable for debugging
3. **Log everything**: Detailed logs help track down issues
4. **Use specific exception types**: Catch specific errors when possible
5. **Retry flaky operations**: Network and timing issues benefit from retries
6. **Clean up resources**: Always close browsers/pages in finally blocks
7. **Provide context**: Error messages should explain what was happening
8. **Validate inputs**: Check data types and values before using them

## Next Steps

- Apply error handling to all your test scripts
- Create a library of helper functions with robust error handling
- Set up logging for your test suite
- Practice debugging real automation issues
- Move on to **Lecture 9** for more advanced topics!

---

Good luck with your automation journey!
