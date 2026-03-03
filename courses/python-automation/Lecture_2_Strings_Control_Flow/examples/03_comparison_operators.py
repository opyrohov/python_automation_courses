"""
Lecture 2: Comparison Operators
This file demonstrates how to compare values in Python.
"""

# ============================================
# EQUAL TO (==)
# ============================================
print("=== Equal To (==) ===")

x = 10
y = 10
z = 5

print(f"x = {x}, y = {y}, z = {z}")
print(f"x == y: {x == y}")  # True
print(f"x == z: {x == z}")  # False
print()

# String comparison
name1 = "Python"
name2 = "Python"
name3 = "python"

print(f"'{name1}' == '{name2}': {name1 == name2}")  # True
print(f"'{name1}' == '{name3}': {name1 == name3}")  # False (case-sensitive)
print()

# ============================================
# NOT EQUAL TO (!=)
# ============================================
print("=== Not Equal To (!=) ===")

status_code = 404
expected_code = 200

print(f"status_code = {status_code}, expected_code = {expected_code}")
print(f"status_code != expected_code: {status_code != expected_code}")  # True
print()

# ============================================
# GREATER THAN (>)
# ============================================
print("=== Greater Than (>) ===")

score = 85
passing_score = 60

print(f"score = {score}, passing_score = {passing_score}")
print(f"score > passing_score: {score > passing_score}")  # True
print()

age = 16
min_age = 18

print(f"age = {age}, min_age = {min_age}")
print(f"age > min_age: {age > min_age}")  # False
print()

# ============================================
# LESS THAN (<)
# ============================================
print("=== Less Than (<) ===")

temperature = 15
freezing_point = 0

print(f"temperature = {temperature}, freezing_point = {freezing_point}")
print(f"temperature < freezing_point: {temperature < freezing_point}")  # False
print()

price = 29.99
budget = 50.00

print(f"price = ${price}, budget = ${budget}")
print(f"price < budget: {price < budget}")  # True
print()

# ============================================
# GREATER THAN OR EQUAL TO (>=)
# ============================================
print("=== Greater Than or Equal To (>=) ===")

items_in_cart = 5
min_items_for_discount = 5

print(f"items_in_cart = {items_in_cart}, min_items_for_discount = {min_items_for_discount}")
print(f"items_in_cart >= min_items_for_discount: {items_in_cart >= min_items_for_discount}")  # True
print()

# ============================================
# LESS THAN OR EQUAL TO (<=)
# ============================================
print("=== Less Than or Equal To (<=) ===")

file_size = 2.5  # MB
max_file_size = 5.0  # MB

print(f"file_size = {file_size}MB, max_file_size = {max_file_size}MB")
print(f"file_size <= max_file_size: {file_size <= max_file_size}")  # True
print()

# ============================================
# CHAINING COMPARISONS
# ============================================
print("=== Chaining Comparisons ===")

age = 25
min_age = 18
max_age = 65

print(f"age = {age}, range = {min_age} to {max_age}")
print(f"{min_age} <= age <= {max_age}: {min_age <= age <= max_age}")  # True
print()

score = 85
print(f"score = {score}")
print(f"80 <= score < 90: {80 <= score < 90}")  # True
print(f"90 <= score <= 100: {90 <= score <= 100}")  # False
print()

# ============================================
# COMPARING STRINGS
# ============================================
print("=== Comparing Strings ===")

# Alphabetical comparison
word1 = "apple"
word2 = "banana"

print(f"'{word1}' < '{word2}': {word1 < word2}")  # True (alphabetically)
print(f"'{word1}' > '{word2}': {word1 > word2}")  # False
print()

# Case matters!
name_lower = "alice"
name_upper = "ALICE"

print(f"'{name_lower}' == '{name_upper}': {name_lower == name_upper}")  # False
print(f"'{name_lower}'.upper() == '{name_upper}': {name_lower.upper() == name_upper}")  # True
print()

# ============================================
# COMPARING WITH BOOLEAN VALUES
# ============================================
print("=== Comparing Boolean Values ===")

is_logged_in = True
is_admin = False

print(f"is_logged_in = {is_logged_in}")
print(f"is_admin = {is_admin}")
print(f"is_logged_in == True: {is_logged_in == True}")
print(f"is_admin == False: {is_admin == False}")
print()

# Better way: use the boolean directly
print("Better way (without == True/False):")
print(f"is_logged_in: {is_logged_in}")
print(f"not is_admin: {not is_admin}")
print()

# ============================================
# PRACTICAL EXAMPLE: FORM VALIDATION
# ============================================
print("=== Practical Example: Form Validation ===")

username_length = 8
password_length = 12
age = 25

print("Form Validation Results:")

# Username length check
if username_length >= 6:
    print("✓ Username length is valid")
else:
    print("✗ Username must be at least 6 characters")

# Password length check
if password_length >= 8:
    print("✓ Password length is valid")
else:
    print("✗ Password must be at least 8 characters")

# Age check
if age >= 18:
    print("✓ Age requirement met")
else:
    print("✗ Must be 18 or older")

print()

# ============================================
# PRACTICAL EXAMPLE: PRICE COMPARISON
# ============================================
print("=== Practical Example: Price Comparison ===")

original_price = 99.99
sale_price = 79.99
discount_threshold = 20.00

discount = original_price - sale_price

print(f"Original price: ${original_price}")
print(f"Sale price: ${sale_price}")
print(f"Discount: ${discount}")

if discount >= discount_threshold:
    print("✓ Good deal! Discount is significant.")
else:
    print("⚠ Discount is minimal.")

print()

# ============================================
# PRACTICAL EXAMPLE: TEST SCORE EVALUATION
# ============================================
print("=== Practical Example: Test Score Evaluation ===")

test_score = 87
max_score = 100
passing_score = 70

print(f"Test Score: {test_score}/{max_score}")

if test_score >= passing_score:
    print("✓ PASSED")

    if test_score >= 90:
        print("Grade: A - Excellent!")
    elif test_score >= 80:
        print("Grade: B - Very Good!")
    elif test_score >= 70:
        print("Grade: C - Good")
else:
    print("✗ FAILED")
    print(f"Need {passing_score - test_score} more points to pass")

print()

# ============================================
# PRACTICAL EXAMPLE: PAGE LOAD TIME CHECK
# ============================================
print("=== Practical Example: Page Load Time ===")

page_load_time = 2.5  # seconds
acceptable_time = 3.0
excellent_time = 1.0

print(f"Page load time: {page_load_time}s")

if page_load_time <= excellent_time:
    print("✓ Excellent performance!")
elif page_load_time <= acceptable_time:
    print("✓ Acceptable performance")
else:
    print("✗ Page is loading too slowly")

print()

# ============================================
# PRACTICAL EXAMPLE: STOCK LEVEL CHECK
# ============================================
print("=== Practical Example: Stock Level Check ===")

stock_level = 5
reorder_point = 10
out_of_stock = 0

print(f"Current stock: {stock_level} units")

if stock_level == out_of_stock:
    print("✗ OUT OF STOCK - Cannot fulfill orders")
elif stock_level < reorder_point:
    print("⚠ LOW STOCK - Reorder needed")
elif stock_level >= reorder_point:
    print("✓ Stock level is adequate")

print()

# ============================================
# PRACTICAL EXAMPLE: ELEMENT COUNT VALIDATION
# ============================================
print("=== Practical Example: Element Count Validation ===")

expected_buttons = 5
actual_buttons = 5
expected_links = 10
actual_links = 8

print("Validating page elements...")
print(f"Buttons - Expected: {expected_buttons}, Actual: {actual_buttons}")
print(f"Links - Expected: {expected_links}, Actual: {actual_links}")

if actual_buttons == expected_buttons:
    print("✓ Button count is correct")
else:
    print("✗ Button count mismatch")

if actual_links == expected_links:
    print("✓ Link count is correct")
elif actual_links < expected_links:
    print(f"✗ Missing {expected_links - actual_links} links")
else:
    print(f"⚠ Found {actual_links - expected_links} extra links")
