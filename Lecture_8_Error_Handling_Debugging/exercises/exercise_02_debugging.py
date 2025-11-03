"""
Lecture 8 - Exercise 2: Debugging Practice
==========================================
Practice debugging techniques and fixing broken code.

Instructions:
1. Find and fix the bugs in each function
2. Add appropriate error handling
3. Test your fixes
4. Check your solutions against SOLUTIONS.md
"""

print("=" * 50)
print("EXERCISE: Debugging Practice")
print("=" * 50)
print()

# Exercise 2.1: Fix the Syntax Error
# ==================================
# TODO: Fix the syntax errors in this function
print("2.1: Fix the Syntax Error")

# BUGGY CODE:
# def calculate_total(items)
#     total = 0
#     for item in items
#         total += item['price']
#     return total

# FIX THE CODE HERE:


# Test your fix:
# test_items = [{'price': 10}, {'price': 20}, {'price': 30}]
# print(f"Total: {calculate_total(test_items)}")

print("-" * 50)


# Exercise 2.2: Fix the NameError
# ===============================
# TODO: Fix the NameError in this function
print("2.2: Fix the NameError")

def greet_user():
    """Greet a user."""
    message = "Hello"
    # BUG: Trying to use undefined variable
    # print(f"{messge}, {user_name}!")  # Typo in variable name
    pass

# FIX THE CODE HERE:


# Test your fix:
# greet_user()

print("-" * 50)


# Exercise 2.3: Fix the IndexError
# ================================
# TODO: Fix the IndexError and add proper error handling
print("2.3: Fix the IndexError")

def get_first_and_last(items):
    """Get first and last items from a list."""
    # BUG: Doesn't check if list is empty
    first = items[0]
    last = items[-1]
    return first, last

# FIX THE CODE HERE (add error handling):


# Test your fix:
# print(get_first_and_last([1, 2, 3, 4, 5]))
# print(get_first_and_last([]))  # Should handle gracefully

print("-" * 50)


# Exercise 2.4: Fix the KeyError
# ==============================
# TODO: Fix the KeyError and add error handling
print("2.4: Fix the KeyError")

def get_user_info(user):
    """Get user information."""
    # BUG: Assumes all keys exist
    name = user['name']
    email = user['email']
    age = user['age']
    return f"{name} ({email}), Age: {age}"

# FIX THE CODE HERE (handle missing keys):


# Test your fix:
# user1 = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
# user2 = {'name': 'Bob', 'email': 'bob@example.com'}  # Missing age
# print(get_user_info(user1))
# print(get_user_info(user2))

print("-" * 50)


# Exercise 2.5: Fix the TypeError
# ===============================
# TODO: Fix the TypeError by validating input types
print("2.5: Fix the TypeError")

def calculate_average(numbers):
    """Calculate average of numbers."""
    # BUG: Doesn't check if numbers is a list or if items are numbers
    total = sum(numbers)
    average = total / len(numbers)
    return average

# FIX THE CODE HERE (add type validation):


# Test your fix:
# print(calculate_average([10, 20, 30, 40]))
# print(calculate_average("not a list"))
# print(calculate_average([]))

print("-" * 50)


# Exercise 2.6: Fix the Logic Error
# =================================
# TODO: Fix the logical bug in this function
print("2.6: Fix the Logic Error")

def is_adult(age):
    """Check if person is an adult (18 or older)."""
    # BUG: Logic is wrong
    if age < 18:
        return True
    else:
        return False

# FIX THE CODE HERE:


# Test your fix:
# print(f"Age 25 is adult: {is_adult(25)}")  # Should be True
# print(f"Age 15 is adult: {is_adult(15)}")  # Should be False

print("-" * 50)


# Exercise 2.7: Debug with Print Statements
# =========================================
# TODO: Add debug print statements to find the bug
print("2.7: Debug with Print Statements")

def find_max_price(products):
    """Find product with maximum price."""
    max_price = 0
    max_product = None

    for product in products:
        # Add debug prints here to see what's happening
        if product['price'] > max_price:
            max_price = product['price']
            max_product = product

    return max_product

# ADD DEBUG PRINTS AND FIX IF NEEDED:


# Test and debug:
# products = [
#     {'name': 'Laptop', 'price': 999},
#     {'name': 'Mouse', 'price': 29},
#     {'name': 'Keyboard', 'price': 79}
# ]
# result = find_max_price(products)
# print(f"Max price product: {result}")

print("-" * 50)


# Exercise 2.8: Fix the Infinite Loop (Be Careful!)
# ================================================
# TODO: Fix the infinite loop (Comment it out first!)
print("2.8: Fix the Infinite Loop")

# DANGEROUS: This will loop forever!
# def count_to_ten():
#     """Count from 1 to 10."""
#     count = 1
#     while count < 10:
#         print(count)
#         # BUG: Forgot to increment count!
#     return count

# FIX THE CODE HERE:


# Test your fix:
# count_to_ten()

print("-" * 50)


# Exercise 2.9: Debug Data Processing
# ===================================
# TODO: Find and fix multiple bugs in this function
print("2.9: Debug Data Processing")

def process_test_results(results):
    """Process test results and calculate statistics."""
    # BUG: Multiple issues in this function
    total = 0
    passed = 0

    for result in results:
        total += 1
        # BUG: Using wrong key name
        if result['status'] == 'pass':
            passed += 1

    # BUG: Division by zero if no results
    success_rate = (passed / total) * 100
    return {
        'total': total,
        'passed': passed,
        'success_rate': success_rate
    }

# FIX THE CODE HERE:


# Test your fix:
# test_results = [
#     {'name': 'test1', 'result': 'pass'},
#     {'name': 'test2', 'result': 'fail'},
#     {'name': 'test3', 'result': 'pass'}
# ]
# print(process_test_results(test_results))
# print(process_test_results([]))  # Empty list

print("-" * 50)


# Exercise 2.10: Debug Complex Function
# =====================================
# TODO: Find all bugs and add error handling
print("2.10: Debug Complex Function")

def calculate_discount(products, discount_code):
    """Calculate total with discount."""
    # Multiple bugs to find!
    total = 0

    for product in products:
        price = product['price']
        quantity = product['quantity']
        total += price * quantity

    # BUG: discount_code might not be in dictionary
    discounts = {
        'SAVE10': 0.10,
        'SAVE20': 0.20,
        'SAVE30': 0.30
    }
    discount = discounts[discount_code]

    # BUG: Wrong calculation
    final_total = total - discount
    return final_total

# FIX THE CODE HERE:


# Test your fix:
# products = [
#     {'name': 'Laptop', 'price': 999, 'quantity': 1},
#     {'name': 'Mouse', 'price': 29, 'quantity': 2}
# ]
# print(calculate_discount(products, 'SAVE10'))
# print(calculate_discount(products, 'INVALID'))  # Handle gracefully

print("-" * 50)


# BONUS: Debug with Logging
# =========================
# TODO: Add logging to debug this function
print("BONUS: Debug with Logging")

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def login_user(username, password, user_database):
    """Login user with debugging."""
    # Add logging statements to debug
    if username in user_database:
        if user_database[username]['password'] == password:
            return True
    return False

# ADD LOGGING STATEMENTS:


# Test your logging:
# users = {
#     'testuser': {'password': 'test123', 'email': 'test@example.com'}
# }
# login_user('testuser', 'test123', users)
# login_user('testuser', 'wrong', users)
# login_user('unknown', 'test123', users)

print("-" * 50)

print("=" * 50)
print("Exercise 2 Complete!")
print("Check SOLUTIONS.md for answers")
print("=" * 50)
