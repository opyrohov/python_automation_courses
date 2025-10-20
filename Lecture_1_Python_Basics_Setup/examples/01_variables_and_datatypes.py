"""
Lecture 1: Variables and Data Types
This file demonstrates how to create variables and work with different data types in Python.
"""

# ============================================
# VARIABLES
# ============================================
# Variables are containers that store data values
# In Python, you don't need to declare the type - it's automatically determined

# Creating variables
name = "Alice"
age = 25
height = 5.6

print("Basic Variables:")
print(name)
print(age)
print(height)
print()  # Empty line for readability

# ============================================
# STRINGS (str)
# ============================================
# Strings represent text and can use single or double quotes

first_name = "John"
last_name = 'Doe'
full_name = "John Doe"

# Multi-line strings use triple quotes
address = """123 Main Street
Apartment 4B
New York, NY 10001"""

print("String Examples:")
print(first_name)
print(last_name)
print(full_name)
print(address)
print()

# String concatenation (joining strings)
greeting = "Hello, " + first_name + "!"
print(greeting)

# String formatting with f-strings (modern way)
message = f"My name is {first_name} {last_name}"
print(message)
print()

# ============================================
# NUMBERS
# ============================================

# Integers (whole numbers)
student_count = 30
year = 2024
temperature = -5

print("Integer Examples:")
print(f"Students: {student_count}")
print(f"Year: {year}")
print(f"Temperature: {temperature}")
print()

# Floats (decimal numbers)
price = 19.99
pi = 3.14159
distance = 5.0

print("Float Examples:")
print(f"Price: ${price}")
print(f"Pi: {pi}")
print(f"Distance: {distance} km")
print()

# ============================================
# BOOLEANS (bool)
# ============================================
# Booleans represent True or False values

is_student = True
is_employed = False
has_license = True

print("Boolean Examples:")
print(f"Is student: {is_student}")
print(f"Is employed: {is_employed}")
print(f"Has license: {has_license}")
print()

# ============================================
# CHECKING DATA TYPES
# ============================================
# Use the type() function to check what type a variable is

print("Checking Data Types:")
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(height) = {type(height)}")
print(f"type(is_student) = {type(is_student)}")
print()

# ============================================
# TYPE CONVERSION
# ============================================
# Converting between different data types

# String to integer
age_string = "30"
age_number = int(age_string)
print(f"Converted '{age_string}' (string) to {age_number} (int)")

# String to float
price_string = "29.99"
price_number = float(price_string)
print(f"Converted '{price_string}' (string) to {price_number} (float)")

# Number to string
count = 100
count_string = str(count)
print(f"Converted {count} (int) to '{count_string}' (string)")

# Integer to float
whole_number = 5
decimal_number = float(whole_number)
print(f"Converted {whole_number} (int) to {decimal_number} (float)")
print()

# ============================================
# VARIABLE NAMING RULES
# ============================================
"""
Good variable names:
- Use lowercase with underscores: user_name, first_name
- Be descriptive: total_price instead of tp
- Start with letter or underscore: _private, user_id

Bad variable names:
- Don't start with numbers: 1st_name ❌
- Don't use spaces: first name ❌
- Don't use Python keywords: for, if, class ❌
- Avoid single letters (except in loops): x, y ❌
"""

# Good examples
user_name = "Alice"
total_price = 99.99
is_active = True
_internal_value = 42

print("Well-named variables created successfully!")
