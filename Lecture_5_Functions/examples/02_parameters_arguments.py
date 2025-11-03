"""
Lecture 5 - Example 2: Parameters and Arguments
==============================================
Learn how to make functions flexible with parameters.
"""

# 1. SINGLE PARAMETER
# ===================

def greet_user(name):
    """Greet a user by name."""
    print(f"Hello, {name}!")
    print(f"Welcome to the course, {name}!")

greet_user("Alice")
greet_user("Bob")

print("-" * 50)


# 2. MULTIPLE PARAMETERS
# ======================

def introduce_person(name, age, city):
    """Introduce a person with their details."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print()

introduce_person("Alice", 25, "New York")
introduce_person("Bob", 30, "San Francisco")

print("-" * 50)


# 3. DEFAULT PARAMETERS
# =====================

def greet_with_time(name, time_of_day="morning"):
    """Greet user with time of day (defaults to morning)."""
    print(f"Good {time_of_day}, {name}!")

greet_with_time("Alice")  # Uses default "morning"
greet_with_time("Bob", "evening")  # Overrides default
greet_with_time("Charlie", "afternoon")

print("-" * 50)


# 4. KEYWORD ARGUMENTS
# ====================

def create_user_profile(name, age, email, is_admin=False):
    """Create a user profile with details."""
    print("Creating user profile:")
    print(f"  Name: {name}")
    print(f"  Age: {age}")
    print(f"  Email: {email}")
    print(f"  Admin: {is_admin}")
    print()

# Positional arguments
create_user_profile("Alice", 25, "alice@example.com")

# Keyword arguments (order doesn't matter)
create_user_profile(email="bob@example.com", name="Bob", age=30)

# Mix of positional and keyword
create_user_profile("Charlie", 35, email="charlie@example.com", is_admin=True)

print("-" * 50)


# 5. COMMON MISTAKE - POSITIONAL ORDER MATTERS
# ============================================

def book_flight(passenger, destination, date):
    """Book a flight for a passenger."""
    print(f"Booking flight:")
    print(f"  Passenger: {passenger}")
    print(f"  Destination: {destination}")
    print(f"  Date: {date}")
    print()

# Correct order
book_flight("Alice", "Paris", "2024-12-01")

# Wrong order - confusing output!
book_flight("Paris", "Alice", "2024-12-01")  # Oops!

# Use keyword arguments to avoid mistakes
book_flight(passenger="Bob", destination="London", date="2024-12-15")

print("-" * 50)


# 6. MULTIPLE DEFAULT PARAMETERS
# ==============================

def send_notification(message, email=None, sms=None, push=True):
    """Send notification through various channels."""
    print(f"Message: {message}")
    if email:
        print(f"  Sending email to: {email}")
    if sms:
        print(f"  Sending SMS to: {sms}")
    if push:
        print(f"  Sending push notification")
    print()

send_notification("Test completed!")
send_notification("Test failed!", email="admin@test.com")
send_notification("Server down!", email="admin@test.com", sms="+1234567890")
send_notification("Info message", push=False)

print("-" * 50)


# 7. VARIABLE NUMBER OF ARGUMENTS - *args
# =======================================

def calculate_sum(*numbers):
    """Calculate sum of any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print()

calculate_sum(1, 2, 3)
calculate_sum(10, 20, 30, 40, 50)
calculate_sum(5)

print("-" * 50)


# 8. VARIABLE KEYWORD ARGUMENTS - **kwargs
# ========================================

def print_user_info(**user_data):
    """Print user information from keyword arguments."""
    print("User Information:")
    for key, value in user_data.items():
        print(f"  {key}: {value}")
    print()

print_user_info(name="Alice", age=25, city="NYC")
print_user_info(name="Bob", email="bob@test.com", role="Admin", active=True)

print("-" * 50)


# 9. COMBINING *args AND **kwargs
# ================================

def log_test_result(test_name, *messages, **details):
    """Log test results with messages and details."""
    print(f"Test: {test_name}")

    if messages:
        print("Messages:")
        for msg in messages:
            print(f"  - {msg}")

    if details:
        print("Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    print()

log_test_result("Login Test")
log_test_result("Form Test", "Form filled", "Submit clicked")
log_test_result("API Test", status="passed", duration="2.5s", assertions=5)
log_test_result(
    "Complex Test",
    "Step 1 completed",
    "Step 2 completed",
    status="passed",
    browser="Chrome",
    duration="10s"
)

print("-" * 50)


# 10. AUTOMATION EXAMPLE - PLAYWRIGHT TEST FUNCTIONS
# ==================================================

def login(username, password, remember_me=False):
    """Simulate login function."""
    print(f"Logging in as: {username}")
    print(f"Password: {'*' * len(password)}")
    if remember_me:
        print("Remember me: Yes")
    print("Login successful!")
    print()

def navigate_to(url, timeout=30, wait_for_load=True):
    """Simulate navigation with options."""
    print(f"Navigating to: {url}")
    print(f"Timeout: {timeout}s")
    if wait_for_load:
        print("Waiting for page load...")
    print("Navigation complete!")
    print()

def fill_form(**fields):
    """Simulate filling a form with multiple fields."""
    print("Filling form:")
    for field_name, field_value in fields.items():
        print(f"  {field_name}: {field_value}")
    print("Form filled successfully!")
    print()

# Using the automation functions
print("🧪 Running Automation Test\n")

login("testuser@example.com", "SecurePass123", remember_me=True)
navigate_to("https://example.com/dashboard", timeout=10)
fill_form(
    first_name="John",
    last_name="Doe",
    email="john@example.com",
    phone="555-1234",
    country="USA"
)

print("=" * 50)
print("Example complete! You've mastered parameters and arguments.")
print("=" * 50)
