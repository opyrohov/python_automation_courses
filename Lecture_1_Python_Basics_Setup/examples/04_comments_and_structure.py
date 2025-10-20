"""
Lecture 1: Comments and Code Structure
This file demonstrates how to write clean, well-documented Python code using comments
and following Python's style conventions.
"""

# ============================================
# SINGLE-LINE COMMENTS
# ============================================

# This is a single-line comment
# Comments start with the hash symbol (#)
# Python ignores everything after # on that line

# Use comments to explain WHY, not WHAT
# Bad comment:
x = 10  # Set x to 10 (obvious from code)

# Good comment:
max_retries = 3  # Limit retries to prevent infinite loops and API rate limiting

# Comments can be on their own line or at the end of a line
print("Hello")  # This prints a greeting

# ============================================
# MULTI-LINE COMMENTS / DOCSTRINGS
# ============================================

"""
This is a multi-line comment (also called a docstring).
It uses triple quotes (either ''' or """).
You can write multiple lines of text.
These are often used for documentation.
"""

'''
You can also use triple single quotes
for multi-line comments.
Both work the same way.
'''

# Docstrings at the beginning of a file, class, or function
# serve as documentation and can be accessed programmatically

def calculate_total(price, tax_rate):
    """
    Calculate the total price including tax.

    Args:
        price (float): The base price of the item
        tax_rate (float): Tax rate as a decimal (e.g., 0.08 for 8%)

    Returns:
        float: The total price including tax
    """
    return price + (price * tax_rate)

# ============================================
# WHEN TO USE COMMENTS
# ============================================

# 1. Explain complex logic
# Calculate compound interest: A = P(1 + r/n)^(nt)
principal = 1000
rate = 0.05
time = 10
amount = principal * (1 + rate) ** time

# 2. Explain business rules or requirements
minimum_age = 18  # Legal driving age in most states

# 3. Mark TODO items or future improvements
# TODO: Add error handling for negative numbers
# FIXME: This calculation doesn't account for leap years
# NOTE: This API endpoint will be deprecated in v2.0

# 4. Explain non-obvious decisions
# Using floor division because we need whole items, not fractional
items_per_box = 47 // 6

# ============================================
# WHEN NOT TO USE COMMENTS
# ============================================

# Don't comment on obvious code
# Bad:
# counter = 0  # Initialize counter to 0
# counter += 1  # Increment counter by 1

# Instead, write clear code that doesn't need comments
counter = 0
counter += 1

# Bad: Commenting what the code does (code is self-explanatory)
# total = price + tax  # Add price and tax

# Good: Use descriptive variable names instead
total_with_tax = base_price + sales_tax

# ============================================
# CODE STRUCTURE AND SPACING
# ============================================

# Use blank lines to separate logical sections
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"

# Blank line between different concepts
age = 30
birth_year = 2024 - age

# Use 4 spaces for indentation (not tabs)
# Indentation is required in Python for code blocks
age = 20
if age >= 18:
    print("You are an adult")  # 4 spaces
    print("You can vote")      # 4 spaces

# ============================================
# NAMING CONVENTIONS (PEP 8)
# ============================================

# Variables and functions: lowercase with underscores (snake_case)
user_name = "Alice"
total_price = 99.99
item_count = 5

# Constants: uppercase with underscores
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159

# Classes: CapitalizedWords (PascalCase) - you'll learn this later
# class UserAccount:
#     pass

# Private variables: start with underscore
_internal_value = 42
_private_data = "secret"

# ============================================
# LINE LENGTH AND READABILITY
# ============================================

# Keep lines under 79-100 characters for readability
# Bad: Too long
# very_long_variable_name = some_function(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6)

# Good: Break into multiple lines
very_long_variable_name = some_function(
    parameter1,
    parameter2,
    parameter3,
    parameter4
)

# Long strings can be broken up
long_message = (
    "This is a very long message that we want to break up "
    "into multiple lines for better readability and to stay "
    "within the recommended line length limit."
)

# ============================================
# WHITESPACE IN EXPRESSIONS
# ============================================

# Good: Use spaces around operators
total = price + tax
average = (a + b + c) / 3
is_valid = (x > 0) and (y < 100)

# Bad: No spaces (harder to read)
# total=price+tax
# average=(a+b+c)/3

# Good: No space before comma, space after
numbers = [1, 2, 3, 4, 5]
print("Hello", "World", "!")

# Function calls: no space before parentheses
print("Hello")
len("Python")

# ============================================
# ORGANIZING CODE INTO SECTIONS
# ============================================

# Section 1: Imports (if any)
# import math
# import datetime

# Section 2: Constants
SALES_TAX_RATE = 0.08
SHIPPING_COST = 5.99

# Section 3: Variables
product_name = "Laptop"
base_price = 999.99

# Section 4: Calculations
tax_amount = base_price * SALES_TAX_RATE
subtotal = base_price + tax_amount
total = subtotal + SHIPPING_COST

# Section 5: Output
print(f"Product: {product_name}")
print(f"Base Price: ${base_price:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Shipping: ${SHIPPING_COST:.2f}")
print(f"Total: ${total:.2f}")

# ============================================
# PRACTICAL EXAMPLE: WELL-STRUCTURED CODE
# ============================================

"""
Student Grade Calculator
This script calculates a student's final grade based on multiple assignments.
"""

# Constants
PASSING_GRADE = 60
TOTAL_ASSIGNMENTS = 5

# Student information
student_name = "Alice Johnson"
student_id = "STU12345"

# Assignment scores (out of 100)
assignment1 = 85
assignment2 = 92
assignment3 = 78
assignment4 = 88
assignment5 = 95

# Calculate average
total_score = assignment1 + assignment2 + assignment3 + assignment4 + assignment5
average_score = total_score / TOTAL_ASSIGNMENTS

# Determine pass/fail status
is_passing = average_score >= PASSING_GRADE

# Display results
print("\n" + "=" * 40)
print("STUDENT GRADE REPORT")
print("=" * 40)
print(f"Student: {student_name}")
print(f"ID: {student_id}")
print("-" * 40)
print(f"Assignment 1: {assignment1}")
print(f"Assignment 2: {assignment2}")
print(f"Assignment 3: {assignment3}")
print(f"Assignment 4: {assignment4}")
print(f"Assignment 5: {assignment5}")
print("-" * 40)
print(f"Average Score: {average_score:.2f}")
print(f"Status: {'PASSING' if is_passing else 'FAILING'}")
print("=" * 40 + "\n")

# ============================================
# INLINE DOCUMENTATION TIPS
# ============================================

"""
Tips for writing good comments:
1. Write comments as you code, not after
2. Keep comments up-to-date when code changes
3. Use complete sentences with proper grammar
4. Explain WHY, not WHAT (code shows what)
5. Comment complex algorithms or business logic
6. Don't comment bad code - rewrite it
7. Use TODO, FIXME, NOTE for markers
8. Be concise but clear
"""

# Example of explaining WHY
# We multiply by 1.5 for overtime because company policy pays time-and-a-half
overtime_rate = regular_rate * 1.5

# Not this (explains WHAT, which is obvious):
# overtime_rate = regular_rate * 1.5  # Multiply regular rate by 1.5

# ============================================
# COMMENTED OUT CODE
# ============================================

# Sometimes you temporarily comment out code during development
# price = 100
# discount = 0.1
# final_price = price - (price * discount)

# But don't leave commented code in production!
# Either use it or delete it

# For version control, use git instead of commenting
# Bad:
# old_calculation = value * 2  # Old way
# new_calculation = value * 3  # New way (2024-10-20)

# Good: Just use the new way, git history preserves the old

print("\nThis file demonstrates proper Python code structure and commenting!")
