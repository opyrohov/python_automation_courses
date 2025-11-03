"""
Lecture 5 - Exercise 2: Parameters and Return Values
===================================================
Practice working with parameters, return values, and more advanced function concepts.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_02_parameters_return.py
3. Check your solutions against SOLUTIONS.md
"""

# Exercise 2.1: Function with Return Value
# ========================================
# TODO: Create a function called 'multiply' that:
# - Takes two parameters: a and b
# - Returns their product
# Test it by storing the result and printing it

# Your code here:


# Test
# result = multiply(5, 7)
# print(f"5 * 7 = {result}")

print("-" * 50)


# Exercise 2.2: Function with Default Parameters
# ==============================================
# TODO: Create a function called 'create_user' that:
# - Takes username and role (with default value "user")
# - Returns a string: "[username] created with role: [role]"
# Test with and without providing the role parameter

# Your code here:


print("-" * 50)


# Exercise 2.3: String Manipulation Function
# ==========================================
# TODO: Create a function called 'format_name' that:
# - Takes first_name and last_name
# - Returns them formatted as "LASTNAME, Firstname"
# Example: format_name("john", "doe") → "DOE, John"

# Your code here:


# Test
# full_name = format_name("alice", "smith")
# print(full_name)

print("-" * 50)


# Exercise 2.4: Multiple Return Values
# ====================================
# TODO: Create a function called 'get_min_max' that:
# - Takes a list of numbers
# - Returns both the minimum and maximum values
# Test with: [3, 7, 2, 9, 1, 5]

# Your code here:


print("-" * 50)


# Exercise 2.5: Conditional Return
# ================================
# TODO: Create a function called 'check_password_strength' that:
# - Takes a password string
# - Returns "Strong" if length >= 8, otherwise "Weak"
# Test with: "abc", "Password123"

# Your code here:


print("-" * 50)


# Exercise 2.6: Calculate with Multiple Parameters
# ================================================
# TODO: Create a function called 'calculate_rectangle_area' that:
# - Takes width and height (height defaults to None)
# - If height is None, assume it's a square (height = width)
# - Returns the area
# Test with: (5, 10) and (7)

# Your code here:


print("-" * 50)


# Exercise 2.7: Early Return Pattern
# ==================================
# TODO: Create a function called 'safe_divide' that:
# - Takes two numbers: a and b
# - If b is 0, return "Cannot divide by zero"
# - Otherwise, return the result of a / b
# Test with: (10, 2) and (10, 0)

# Your code here:


print("-" * 50)


# Exercise 2.8: Function with Keyword Arguments
# =============================================
# TODO: Create a function called 'book_flight' that:
# - Takes: passenger, destination, date, class_type (default "Economy")
# - Returns a formatted booking confirmation string
# Test using keyword arguments in different orders

# Your code here:


print("-" * 50)


# Exercise 2.9: List Processing Function
# ======================================
# TODO: Create a function called 'filter_even_numbers' that:
# - Takes a list of numbers
# - Returns a new list containing only even numbers
# Test with: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Your code here:


print("-" * 50)


# Exercise 2.10: Dictionary Builder Function
# ==========================================
# TODO: Create a function called 'create_test_user' that:
# - Takes: username, email, age (default 18)
# - Returns a dictionary with these keys and values
# Test with different parameters

# Your code here:


print("-" * 50)


# Exercise 2.11: Variable Arguments (*args)
# =========================================
# TODO: Create a function called 'sum_all' that:
# - Takes any number of arguments using *args
# - Returns the sum of all numbers
# Test with: (1, 2, 3), (10, 20, 30, 40, 50)

# Your code here:


print("-" * 50)


# Exercise 2.12: Keyword Arguments (**kwargs)
# ===========================================
# TODO: Create a function called 'print_test_config' that:
# - Takes **kwargs for various config options
# - Prints each key-value pair in the format "key: value"
# - Returns the number of config items
# Test with: browser="Chrome", timeout=30, headless=True

# Your code here:


print("-" * 50)


# BONUS Exercise: Advanced Calculator
# ===================================
# TODO: Create a function called 'calculate' that:
# - Takes operation (string): "add", "subtract", "multiply", "divide"
# - Takes *args for numbers to operate on
# - Returns the result based on operation
# - For add: sum all numbers
# - For multiply: multiply all numbers
# - For subtract: subtract all from first
# - For divide: divide first by all others (check for zero!)
# Test with various operations and numbers

# Your code here:


print("=" * 50)
print("Exercise 2 Complete!")
print("Compare your solutions with SOLUTIONS.md")
print("=" * 50)
