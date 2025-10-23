"""
Lecture 2: Control Flow with if/elif/else
This file demonstrates conditional statements and decision-making in Python.
"""

# ============================================
# BASIC IF STATEMENT
# ============================================
print("=== Basic if Statement ===")

age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print()

# ============================================
# IF-ELSE STATEMENT
# ============================================
print("=== if-else Statement ===")

temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

print()

# ============================================
# IF-ELIF-ELSE STATEMENT
# ============================================
print("=== if-elif-else Statement ===")

score = 85

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Satisfactory")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - Failed")

print()

# ============================================
# MULTIPLE CONDITIONS WITH AND
# ============================================
print("=== Multiple Conditions with AND ===")

username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid credentials!")

print()

# Example 2: Age and license check
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

print()

# ============================================
# MULTIPLE CONDITIONS WITH OR
# ============================================
print("=== Multiple Conditions with OR ===")

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend! Time to relax.")
else:
    print("It's a weekday. Time to work.")

print()

# Example 2: Payment method check
payment_method = "PayPal"

if payment_method == "Credit Card" or payment_method == "PayPal" or payment_method == "Debit Card":
    print("Payment method accepted.")
else:
    print("Payment method not supported.")

print()

# ============================================
# NOT OPERATOR
# ============================================
print("=== NOT Operator ===")

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")
else:
    print("Take an umbrella!")

print()

# ============================================
# COMBINING AND, OR, NOT
# ============================================
print("=== Combining Logical Operators ===")

age = 25
is_student = True
has_id = True

if (age >= 18 and age < 65) and (is_student or has_id):
    print("You qualify for the discount.")
else:
    print("No discount available.")

print()

# ============================================
# NESTED IF STATEMENTS
# ============================================
print("=== Nested if Statements ===")

account_balance = 500
withdrawal_amount = 200
is_account_active = True

if is_account_active:
    print("Account is active.")
    if account_balance >= withdrawal_amount:
        print(f"Withdrawal of ${withdrawal_amount} approved.")
        print(f"Remaining balance: ${account_balance - withdrawal_amount}")
    else:
        print("Insufficient funds.")
else:
    print("Account is not active. Cannot withdraw.")

print()

# ============================================
# CHECKING MULTIPLE VALUES WITH IN
# ============================================
print("=== Checking Multiple Values with 'in' ===")

user_role = "admin"
allowed_roles = ["admin", "moderator", "editor"]

if user_role in allowed_roles:
    print(f"Access granted for role: {user_role}")
else:
    print("Access denied.")

print()

# ============================================
# CHECKING STRING CONTENT
# ============================================
print("=== Checking String Content ===")

email = "user@example.com"

if "@" in email and "." in email:
    print("Email format looks valid.")
else:
    print("Invalid email format.")

print()

# ============================================
# TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ============================================
print("=== Ternary Operator ===")

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Another example
score = 75
result = "Pass" if score >= 60 else "Fail"
print(f"Result: {result}")

print()

# ============================================
# PRACTICAL EXAMPLE: USER INPUT VALIDATION
# ============================================
print("=== Practical Example: Input Validation ===")

username = "john_doe"
password = "Pass123!"
email = "john@example.com"

print("Validating user registration...")

# Username validation
if len(username) < 3:
    print("✗ Username must be at least 3 characters long.")
elif len(username) > 20:
    print("✗ Username must be at most 20 characters long.")
else:
    print("✓ Username is valid.")

# Password validation
if len(password) < 8:
    print("✗ Password must be at least 8 characters long.")
else:
    print("✓ Password is valid.")

# Email validation
if "@" not in email or "." not in email:
    print("✗ Email format is invalid.")
else:
    print("✓ Email is valid.")

print()

# ============================================
# PRACTICAL EXAMPLE: STATUS CODE HANDLING
# ============================================
print("=== Practical Example: HTTP Status Codes ===")

status_code = 200

if status_code == 200:
    print("Success! Request completed.")
elif status_code == 404:
    print("Error: Page not found.")
elif status_code == 500:
    print("Error: Server error.")
elif status_code >= 400 and status_code < 500:
    print("Client error occurred.")
elif status_code >= 500:
    print("Server error occurred.")
else:
    print(f"Status code: {status_code}")

print()

# ============================================
# PRACTICAL EXAMPLE: ELEMENT STATE CHECK
# ============================================
print("=== Practical Example: Element State ===")

is_visible = True
is_enabled = True
is_clickable = is_visible and is_enabled

if is_clickable:
    print("Element is ready to be clicked.")
else:
    if not is_visible:
        print("Element is not visible.")
    if not is_enabled:
        print("Element is not enabled.")

print()

# ============================================
# PRACTICAL EXAMPLE: TEST RESULT EVALUATION
# ============================================
print("=== Practical Example: Test Results ===")

tests_passed = 8
tests_failed = 2
total_tests = tests_passed + tests_failed
pass_rate = (tests_passed / total_tests) * 100

print(f"Tests passed: {tests_passed}/{total_tests}")
print(f"Pass rate: {pass_rate}%")

if tests_failed == 0:
    print("✓ All tests passed! Excellent!")
elif pass_rate >= 80:
    print("⚠ Most tests passed, but some failed.")
elif pass_rate >= 50:
    print("⚠ Many tests failed. Needs attention.")
else:
    print("✗ Critical: Majority of tests failed!")
