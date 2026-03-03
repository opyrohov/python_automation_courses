"""
Lecture 5 - Example 3: Return Values
====================================
Learn how functions can return data back to the caller.
"""

# 1. SIMPLE RETURN
# ================

def get_greeting():
    """Return a greeting message."""
    return "Hello, World!"

# Store the return value
message = get_greeting()
print(message)

# Use return value directly
print(get_greeting())

print("-" * 50)


# 2. RETURN WITH CALCULATION
# ==========================

def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 20)

print(f"5 + 3 = {sum1}")
print(f"10 + 20 = {sum2}")

# Use return value in expression
total = add_numbers(100, 200) + add_numbers(50, 75)
print(f"Total: {total}")

print("-" * 50)


# 3. MULTIPLE RETURN VALUES
# =========================

def get_user_info():
    """Return multiple values as a tuple."""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city

# Unpack return values
user_name, user_age, user_city = get_user_info()
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")

# Or get as tuple
user_data = get_user_info()
print(f"User data: {user_data}")

print("-" * 50)


# 4. RETURN DIFFERENT DATA TYPES
# ==============================

def get_list_of_numbers():
    """Return a list."""
    return [1, 2, 3, 4, 5]

def get_user_dict():
    """Return a dictionary."""
    return {
        "name": "Bob",
        "email": "bob@example.com",
        "age": 30
    }

def is_valid_email(email):
    """Return a boolean."""
    return "@" in email and "." in email

numbers = get_list_of_numbers()
user = get_user_dict()
valid = is_valid_email("test@example.com")

print(f"Numbers: {numbers}")
print(f"User: {user}")
print(f"Valid email: {valid}")

print("-" * 50)


# 5. EARLY RETURN
# ===============

def divide_numbers(a, b):
    """Divide two numbers with error handling."""
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None

    result = a / b
    return result

result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)

print(f"10 / 2 = {result1}")
print(f"10 / 0 = {result2}")

print("-" * 50)


# 6. RETURN NONE (IMPLICIT)
# =========================

def print_message(text):
    """Function that doesn't explicitly return anything."""
    print(text)
    # No return statement = returns None

result = print_message("Hello!")
print(f"Return value: {result}")

print("-" * 50)


# 7. CONDITIONAL RETURNS
# ======================

def check_age_category(age):
    """Return age category based on age."""
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print(f"Age 15: {check_age_category(15)}")
print(f"Age 30: {check_age_category(30)}")
print(f"Age 70: {check_age_category(70)}")

print("-" * 50)


# 8. RETURN FROM LOOPS
# ====================

def find_first_even(numbers):
    """Find and return the first even number."""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None  # If no even number found

numbers = [1, 3, 5, 8, 9, 11]
first_even = find_first_even(numbers)
print(f"First even number: {first_even}")

numbers = [1, 3, 5, 7]
first_even = find_first_even(numbers)
print(f"First even number: {first_even}")

print("-" * 50)


# 9. USING RETURN VALUES IN CONDITIONS
# ====================================

def is_password_strong(password):
    """Check if password meets strength requirements."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

passwords = ["weak", "Strong123", "nodigits", "NOUPPER123", "Perfect1"]

for pwd in passwords:
    if is_password_strong(pwd):
        print(f"✅ '{pwd}' is strong")
    else:
        print(f"❌ '{pwd}' is weak")

print("-" * 50)


# 10. CHAINING FUNCTION CALLS
# ===========================

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

# Chain functions: (2 + 3) * 4 = 20
result = multiply(add(2, 3), 4)
print(f"(2 + 3) * 4 = {result}")

# Complex chaining: ((2 + 3) * 4) ^ 2 = 400
result = power(multiply(add(2, 3), 4), 2)
print(f"((2 + 3) * 4) ^ 2 = {result}")

print("-" * 50)


# 11. AUTOMATION EXAMPLE - HELPER FUNCTIONS WITH RETURNS
# ======================================================

def get_element_text(element_id):
    """Simulate getting text from an element."""
    # In real Playwright, this would get actual element text
    elements = {
        "title": "Welcome to Test Site",
        "status": "Login Successful",
        "error": "Invalid credentials"
    }
    return elements.get(element_id, "Element not found")

def is_element_visible(element_id):
    """Simulate checking if element is visible."""
    visible_elements = ["title", "login_button", "nav_menu"]
    return element_id in visible_elements

def get_all_links():
    """Simulate getting all links from a page."""
    return [
        "https://example.com/home",
        "https://example.com/about",
        "https://example.com/contact"
    ]

def calculate_test_success_rate(passed, failed):
    """Calculate test success rate."""
    total = passed + failed
    if total == 0:
        return 0
    success_rate = (passed / total) * 100
    return round(success_rate, 2)

# Using automation helper functions
print("🧪 Automation Test Results\n")

# Get and verify element text
title = get_element_text("title")
print(f"Page title: {title}")

status = get_element_text("status")
print(f"Status: {status}")

# Check element visibility
if is_element_visible("login_button"):
    print("✅ Login button is visible")
else:
    print("❌ Login button is not visible")

# Get all links
links = get_all_links()
print(f"\nFound {len(links)} links:")
for link in links:
    print(f"  - {link}")

# Calculate success rate
success_rate = calculate_test_success_rate(45, 5)
print(f"\nTest Success Rate: {success_rate}%")

print("\n" + "=" * 50)
print("Example complete! You've mastered return values.")
print("=" * 50)
