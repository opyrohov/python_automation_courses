"""
Lecture 5 - Example 4: Advanced Function Concepts
================================================
Learn more sophisticated function techniques.
"""

# 1. FUNCTION SCOPE - LOCAL VS GLOBAL
# ====================================

# Global variable
global_counter = 0

def increment_local():
    """Function with local variable."""
    local_counter = 0
    local_counter += 1
    print(f"Local counter: {local_counter}")

def increment_global():
    """Function that modifies global variable."""
    global global_counter
    global_counter += 1
    print(f"Global counter: {global_counter}")

print("Testing scope:")
increment_local()
increment_local()  # Still prints 1
print(f"Global counter before: {global_counter}")
increment_global()
increment_global()
print(f"Global counter after: {global_counter}")

print("-" * 50)


# 2. NESTED FUNCTIONS
# ===================

def outer_function(text):
    """Function containing another function."""

    def inner_function():
        """Inner function can access outer function's variables."""
        print(f"Inner function says: {text}")

    print(f"Outer function says: {text}")
    inner_function()

outer_function("Hello!")

print("-" * 50)


# 3. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# =========================================

# Regular function
def add(a, b):
    return a + b

# Lambda function (one-liner)
add_lambda = lambda a, b: a + b

print(f"Regular function: 5 + 3 = {add(5, 3)}")
print(f"Lambda function: 5 + 3 = {add_lambda(5, 3)}")

# Lambda with single parameter
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with no parameters
get_pi = lambda: 3.14159
print(f"Pi: {get_pi()}")

print("-" * 50)


# 4. LAMBDA IN SORTING
# ====================

users = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 30}
]

# Sort by age using lambda
sorted_by_age = sorted(users, key=lambda user: user["age"])
print("Sorted by age:")
for user in sorted_by_age:
    print(f"  {user['name']}: {user['age']}")

# Sort by name using lambda
sorted_by_name = sorted(users, key=lambda user: user["name"])
print("\nSorted by name:")
for user in sorted_by_name:
    print(f"  {user['name']}: {user['age']}")

print("-" * 50)


# 5. LAMBDA IN FILTERING
# ======================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greater_than_5}")

print("-" * 50)


# 6. LAMBDA IN MAPPING
# ====================

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

print("-" * 50)


# 7. FUNCTION AS ARGUMENT
# =======================

def execute_operation(a, b, operation):
    """Execute a given operation on two numbers."""
    result = operation(a, b)
    return result

# Define operations
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Pass functions as arguments
result1 = execute_operation(5, 3, add)
result2 = execute_operation(5, 3, multiply)
result3 = execute_operation(5, 3, lambda a, b: a - b)

print(f"5 + 3 = {result1}")
print(f"5 * 3 = {result2}")
print(f"5 - 3 = {result3}")

print("-" * 50)


# 8. CLOSURES
# ===========

def create_multiplier(factor):
    """Create a function that multiplies by a given factor."""

    def multiplier(number):
        return number * factor

    return multiplier

# Create specific multipliers
double = create_multiplier(2)
triple = create_multiplier(3)
times_10 = create_multiplier(10)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Times 10: {times_10(5)}")

print("-" * 50)


# 9. DECORATORS (INTRODUCTION)
# ============================

def logger_decorator(func):
    """Decorator that logs function calls."""

    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result

    return wrapper

@logger_decorator
def greet(name):
    """Greet a user."""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

result = greet("Alice")
print(f"Result: {result}")

print("-" * 50)


# 10. RECURSION
# =============

def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    """Countdown from n to 1 using recursion."""
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

print("Factorial examples:")
print(f"5! = {factorial(5)}")
print(f"3! = {factorial(3)}")

print("\nCountdown:")
countdown(5)

print("-" * 50)


# 11. AUTOMATION EXAMPLE - ADVANCED PATTERNS
# ==========================================

def create_test_runner(browser_type):
    """Create a test runner for a specific browser."""

    def run_test(test_name):
        print(f"Running '{test_name}' on {browser_type}")
        print(f"  Browser: {browser_type}")
        print(f"  Test: {test_name}")
        print(f"  Status: ✅ Passed")
        return True

    return run_test

# Create browser-specific test runners
chrome_runner = create_test_runner("Chrome")
firefox_runner = create_test_runner("Firefox")

print("🧪 Running Tests\n")
chrome_runner("Login Test")
print()
firefox_runner("Form Test")

print("\n" + "-" * 50)


# Test retry decorator
def retry_on_failure(max_attempts=3):
    """Decorator to retry failed tests."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                print(f"Attempt {attempt}/{max_attempts}")
                try:
                    result = func(*args, **kwargs)
                    print("✅ Success!")
                    return result
                except Exception as e:
                    print(f"❌ Failed: {e}")
                    if attempt == max_attempts:
                        print("Max attempts reached")
                        raise
            return None
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3)
def flaky_test(should_pass):
    """Simulate a flaky test."""
    if not should_pass:
        raise Exception("Test failed")
    return "Test passed"

print("\nTesting retry decorator:")
try:
    flaky_test(True)
except:
    pass

print("\n" + "-" * 50)


# Dynamic test data generator
def generate_test_data(data_type):
    """Generate test data based on type."""

    generators = {
        "email": lambda: ["user1@test.com", "user2@test.com", "user3@test.com"],
        "password": lambda: ["Pass123!", "Secure456!", "Strong789!"],
        "username": lambda: ["alice", "bob", "charlie"]
    }

    if data_type in generators:
        return generators[data_type]()
    return []

print("\n🔧 Test Data Generation:")
emails = generate_test_data("email")
passwords = generate_test_data("password")

print(f"Test emails: {emails}")
print(f"Test passwords: {passwords}")

print("\n" + "=" * 50)
print("Example complete! You've learned advanced function concepts.")
print("=" * 50)
