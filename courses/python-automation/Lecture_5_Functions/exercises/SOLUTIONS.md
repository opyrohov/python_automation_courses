# Lecture 5: Functions - Exercise Solutions

This file contains solutions for all exercises in Lecture 5.

## Exercise 1: Function Basics

### Exercise 1.1: Simple Greeting Function
```python
def greet():
    print("Hello, Python!")

greet()
```

### Exercise 1.2: Personalized Greeting
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
```

### Exercise 1.3: Temperature Converter
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

celsius_to_fahrenheit(0)
celsius_to_fahrenheit(25)
celsius_to_fahrenheit(100)
```

### Exercise 1.4: Age Calculator
```python
def calculate_age(birth_year):
    age = 2024 - birth_year
    print(f"{birth_year} → You are {age} years old")

calculate_age(1990)
calculate_age(2000)
calculate_age(2010)
```

### Exercise 1.5: Box Printer
```python
def print_box(message):
    border = "*" * (len(message) + 6)
    print(border)
    print(f"*  {message}  *")
    print(border)

print_box("Hello")
print_box("Python")
```

### Exercise 1.6: Shopping Cart Function
```python
def add_to_cart(item_name, price):
    print(f"Added {item_name} for ${price} to cart")

add_to_cart("Laptop", 999.99)
add_to_cart("Mouse", 29.99)
add_to_cart("Keyboard", 79.99)
```

### Exercise 1.7: Multiple Functions Working Together
```python
def start_test():
    print("Starting test...")

def run_test():
    print("Running test steps...")

def end_test():
    print("Test completed!")

def run_full_test():
    start_test()
    run_test()
    end_test()

run_full_test()
```

### Exercise 1.8: URL Builder
```python
def build_url(domain, path):
    print(f"https://{domain}/{path}")

build_url("example.com", "login")
build_url("test.com", "dashboard")
```

### BONUS: Test Reporter
```python
def report_test(test_name, passed_count, failed_count):
    total = passed_count + failed_count
    print(f"Test Report: {test_name}")
    print("=" * 24)
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Total: {total}")

report_test("Login Tests", 8, 2)
```

---

## Exercise 2: Parameters and Return Values

### Exercise 2.1: Function with Return Value
```python
def multiply(a, b):
    return a * b

result = multiply(5, 7)
print(f"5 * 7 = {result}")
```

### Exercise 2.2: Function with Default Parameters
```python
def create_user(username, role="user"):
    return f"{username} created with role: {role}"

print(create_user("alice"))
print(create_user("bob", "admin"))
```

### Exercise 2.3: String Manipulation Function
```python
def format_name(first_name, last_name):
    return f"{last_name.upper()}, {first_name.capitalize()}"

full_name = format_name("john", "doe")
print(full_name)
full_name = format_name("alice", "smith")
print(full_name)
```

### Exercise 2.4: Multiple Return Values
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

numbers = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(numbers)
print(f"Min: {minimum}, Max: {maximum}")
```

### Exercise 2.5: Conditional Return
```python
def check_password_strength(password):
    if len(password) >= 8:
        return "Strong"
    else:
        return "Weak"

print(check_password_strength("abc"))
print(check_password_strength("Password123"))
```

### Exercise 2.6: Calculate with Multiple Parameters
```python
def calculate_rectangle_area(width, height=None):
    if height is None:
        height = width  # It's a square
    return width * height

print(f"Area of 5x10 rectangle: {calculate_rectangle_area(5, 10)}")
print(f"Area of 7x7 square: {calculate_rectangle_area(7)}")
```

### Exercise 2.7: Early Return Pattern
```python
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

### Exercise 2.8: Function with Keyword Arguments
```python
def book_flight(passenger, destination, date, class_type="Economy"):
    return f"Flight booked for {passenger} to {destination} on {date} ({class_type} class)"

print(book_flight("Alice", "Paris", "2024-12-01"))
print(book_flight(passenger="Bob", date="2024-12-15", destination="London", class_type="Business"))
```

### Exercise 2.9: List Processing Function
```python
def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Alternative with list comprehension:
# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(numbers)
print(f"Even numbers: {result}")
```

### Exercise 2.10: Dictionary Builder Function
```python
def create_test_user(username, email, age=18):
    return {
        "username": username,
        "email": email,
        "age": age
    }

user1 = create_test_user("alice", "alice@test.com")
user2 = create_test_user("bob", "bob@test.com", 25)
print(user1)
print(user2)
```

### Exercise 2.11: Variable Arguments (*args)
```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Alternative with built-in sum:
# def sum_all(*numbers):
#     return sum(numbers)

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))
```

### Exercise 2.12: Keyword Arguments (**kwargs)
```python
def print_test_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return len(kwargs)

count = print_test_config(browser="Chrome", timeout=30, headless=True)
print(f"Total config items: {count}")
```

### BONUS: Advanced Calculator
```python
def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "subtract":
        if len(args) == 0:
            return 0
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == "divide":
        if len(args) == 0:
            return 0
        if 0 in args[1:]:
            return "Cannot divide by zero"
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    else:
        return "Invalid operation"

print(calculate("add", 1, 2, 3, 4))
print(calculate("multiply", 2, 3, 4))
print(calculate("subtract", 100, 20, 10))
print(calculate("divide", 100, 2, 5))
print(calculate("divide", 100, 0))
```

---

## Exercise 3: Playwright Helper Functions

### Exercise 3.1: Create a Click Helper
```python
def click_element(selector):
    print(f"Clicking element: {selector}")
    return True

click_element("#submit-button")
```

### Exercise 3.2: Create a Fill Field Helper
```python
def fill_input(selector, value):
    print(f"Filling {selector} with: {value}")
    return True

fill_input("#email", "test@example.com")
```

### Exercise 3.3: Create a Navigation Helper
```python
def navigate(url, timeout=30):
    print(f"Navigating to {url} (timeout: {timeout}s)")
    return True

navigate("https://example.com")
navigate("https://test.com", timeout=10)
```

### Exercise 3.4: Create a Login Function
```python
def login_user(username, password, remember_me=False):
    print(f"Logging in as: {username}")
    print(f"Password: {'*' * len(password)}")
    if remember_me:
        print("Checking 'Remember Me'")
    print("Clicking login button")
    print("Login successful!")
    return True

login_user("test@example.com", "SecurePass123")
login_user("admin@test.com", "AdminPass456", remember_me=True)
```

### Exercise 3.5: Create a Verification Helper
```python
def verify_text_on_page(expected_text):
    print(f"Verifying text on page: '{expected_text}'")
    # Simulate check
    found = True  # In real automation, this would check the page
    if found:
        print(f"✅ Text found: '{expected_text}'")
        return True
    else:
        print(f"❌ Text not found: '{expected_text}'")
        return False

verify_text_on_page("Welcome to Dashboard")
```

### Exercise 3.6: Create a Form Fill Helper
```python
def fill_registration_form(first_name, last_name, email, password, phone=None, country="USA"):
    print("Filling registration form:")
    print(f"  First Name: {first_name}")
    print(f"  Last Name: {last_name}")
    print(f"  Email: {email}")
    print(f"  Password: {'*' * len(password)}")
    if phone:
        print(f"  Phone: {phone}")
    print(f"  Country: {country}")

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "country": country
    }

result = fill_registration_form("John", "Doe", "john@test.com", "SecurePass123")
print(f"Filled data: {result}")
```

### Exercise 3.7: Create a Wait Helper
```python
def wait_for_element(selector, timeout=10):
    print(f"Waiting up to {timeout}s for: {selector}")
    print("Element found!")
    return True

wait_for_element("#dashboard")
wait_for_element(".loading-spinner", timeout=5)
```

### Exercise 3.8: Create a Screenshot Helper
```python
def capture_screenshot(screenshot_name, path="screenshots/"):
    full_path = f"{path}{screenshot_name}.png"
    print(f"Saving screenshot: {full_path}")
    return full_path

screenshot_path = capture_screenshot("login_page")
print(f"Screenshot saved at: {screenshot_path}")
```

### Exercise 3.9: Create a Multi-Step Test Function
```python
def test_user_registration():
    print("🧪 Starting User Registration Test\n")

    # Step 1: Navigate
    navigate("https://example.com/register")

    # Step 2: Fill form
    fill_registration_form(
        "Jane",
        "Smith",
        "jane@test.com",
        "SecurePass456",
        phone="555-1234"
    )

    # Step 3: Click submit
    click_element("#submit-button")

    # Step 4: Wait for success
    wait_for_element("#success-message", timeout=5)

    # Step 5: Verify success
    verify_text_on_page("Registration successful")

    # Step 6: Take screenshot
    capture_screenshot("registration_success")

    print("\n✅ Test completed successfully!")
    return True

test_user_registration()
```

### Exercise 3.10: Create a Data-Driven Test Helper
```python
def run_login_tests(test_data):
    results = {"passed": 0, "failed": 0}

    for i, test in enumerate(test_data, 1):
        print(f"\nTest Case {i}:")
        print(f"  Username: {test['username']}")
        print(f"  Password: {test['password']}")
        print(f"  Expected: {test['expected']}")

        # Simulate login
        login_user(test['username'], test['password'])

        # Check result (simplified)
        actual = "success"  # In real test, this would check actual result
        print(f"  Actual: {actual}")

        if actual == test['expected']:
            print("  ✅ PASSED")
            results["passed"] += 1
        else:
            print("  ❌ FAILED")
            results["failed"] += 1

    print(f"\n📊 Summary: {results['passed']} passed, {results['failed']} failed")
    return results

test_data = [
    {"username": "valid@test.com", "password": "Pass123", "expected": "success"},
    {"username": "invalid@test.com", "password": "wrong", "expected": "failure"},
    {"username": "admin@test.com", "password": "Admin456", "expected": "success"}
]

run_login_tests(test_data)
```

### Exercise 3.11: Create a Test Reporter
```python
def generate_test_report(test_name, test_results, timestamp=None):
    total = test_results.get("passed", 0) + test_results.get("failed", 0) + test_results.get("skipped", 0)
    passed = test_results.get("passed", 0)

    if total > 0:
        success_percentage = (passed / total) * 100
    else:
        success_percentage = 0

    print(f"\n{'=' * 50}")
    print(f"Test Report: {test_name}")
    if timestamp:
        print(f"Time: {timestamp}")
    print(f"{'=' * 50}")
    print(f"✅ Passed: {test_results.get('passed', 0)}")
    print(f"❌ Failed: {test_results.get('failed', 0)}")
    if "skipped" in test_results:
        print(f"⏭️  Skipped: {test_results.get('skipped', 0)}")
    print(f"📊 Total: {total}")
    print(f"📈 Success Rate: {success_percentage:.1f}%")
    print(f"{'=' * 50}\n")

    return success_percentage

sample_results = {"passed": 45, "failed": 3, "skipped": 2}
success_rate = generate_test_report("Login Test Suite", sample_results, timestamp="2024-11-01 14:30:00")
```

### Exercise 3.12: Create a Page Object Helper
```python
def create_login_page_helpers():
    return {
        "enter_username": lambda username: print(f"Entering username: {username}"),
        "enter_password": lambda password: print(f"Entering password: {'*' * len(password)}"),
        "click_login": lambda: print("Clicking login button"),
        "get_error_message": lambda: print("Getting error message from page")
    }

login_page = create_login_page_helpers()
login_page["enter_username"]("test@example.com")
login_page["enter_password"]("SecurePass123")
login_page["click_login"]()
```

### BONUS: Create a Test Retry Mechanism
```python
def retry_test(test_function, max_attempts=3, **kwargs):
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}/{max_attempts}")
        result = test_function(**kwargs)
        if result:
            print(f"✅ Test passed on attempt {attempt}")
            return True
        else:
            print(f"❌ Test failed on attempt {attempt}")

    print(f"\n❌ Test failed after {max_attempts} attempts")
    return False

# Sample flaky test
attempt_counter = 0

def flaky_test():
    global attempt_counter
    attempt_counter += 1
    print(f"Running flaky test (internal attempt {attempt_counter})...")
    # Fails first two times, succeeds on third
    if attempt_counter < 3:
        return False
    return True

# Test the retry mechanism
print("🧪 Testing Retry Mechanism:")
retry_test(flaky_test, max_attempts=5)
```

---

## Key Takeaways

1. **Functions organize code**: Break complex tasks into smaller, manageable pieces
2. **Parameters make functions flexible**: Same function can work with different data
3. **Return values enable composition**: Functions can be combined and chained
4. **Default parameters reduce code**: Provide sensible defaults while allowing customization
5. **Helper functions improve tests**: Reusable functions make automation code cleaner and more maintainable

## Next Steps

- Practice creating your own helper functions
- Start building a library of reusable test utilities
- Apply these concepts to real Playwright automation
- Learn about more advanced patterns like decorators and closures

Good luck with your automation journey!
