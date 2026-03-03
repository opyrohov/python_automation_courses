"""
Lecture 1: Print Statements
This file demonstrates various ways to use the print() function in Python.
"""

# ============================================
# BASIC PRINT STATEMENTS
# ============================================

print("=" * 50)
print("BASIC PRINT STATEMENTS")
print("=" * 50)

# Simple print
print("Hello, World!")

# Print multiple items (separated by space automatically)
print("Hello", "Python", "Programming")

# Print numbers
print(42)
print(3.14159)

# Print without adding a new line (use end parameter)
print("Hello", end=" ")
print("World")  # Continues on same line
print()  # Empty print to move to next line

# ============================================
# STRING FORMATTING
# ============================================

print("=" * 50)
print("STRING FORMATTING")
print("=" * 50)

name = "Alice"
age = 25
height = 5.6

# Method 1: String concatenation (joining strings)
print("My name is " + name + " and I am " + str(age) + " years old.")

# Method 2: Using commas (automatic space between items)
print("My name is", name, "and I am", age, "years old.")

# Method 3: Using .format() method
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old. {0} is my first name.".format(name, age))
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# Method 4: f-strings (recommended - Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
print(f"My height is {height} feet.")
print()

# ============================================
# FORMATTING NUMBERS
# ============================================

print("=" * 50)
print("FORMATTING NUMBERS")
print("=" * 50)

# Formatting decimal places
pi = 3.14159265359
print(f"Pi with 2 decimals: {pi:.2f}")
print(f"Pi with 4 decimals: {pi:.4f}")

# Formatting currency
price = 1234.567
print(f"Price: ${price:.2f}")

# Formatting with comma separators
large_number = 1234567890
print(f"Large number: {large_number:,}")
print(f"With decimals: ${large_number:,.2f}")

# Percentage formatting
score = 0.8567
print(f"Score: {score:.1%}")
print()

# ============================================
# ALIGNMENT AND PADDING
# ============================================

print("=" * 50)
print("ALIGNMENT AND PADDING")
print("=" * 50)

# Left alignment
print(f"{'Left':<20}|")

# Right alignment
print(f"{'Right':>20}|")

# Center alignment
print(f"{'Center':^20}|")

# With numbers
print(f"{'Product':<15} {'Price':>10}")
print(f"{'Apple':<15} {'$2.99':>10}")
print(f"{'Banana':<15} {'$1.50':>10}")
print(f"{'Orange':<15} {'$3.25':>10}")
print()

# ============================================
# SPECIAL CHARACTERS
# ============================================

print("=" * 50)
print("SPECIAL CHARACTERS")
print("=" * 50)

# New line (\n)
print("First line\nSecond line\nThird line")

# Tab (\t)
print("Name:\tAlice")
print("Age:\t25")
print("City:\tNew York")

# Backslash (\\)
print("This is a backslash: \\")

# Quotes inside strings
print("She said, \"Hello!\"")
print('He said, "Python is great!"')
print("It's a beautiful day")
print()

# ============================================
# PRINT SEPARATOR
# ============================================

print("=" * 50)
print("CUSTOM SEPARATORS")
print("=" * 50)

# Default separator is space
print("Apple", "Banana", "Orange")

# Custom separator
print("Apple", "Banana", "Orange", sep=", ")
print("2024", "10", "20", sep="-")
print("Python", "is", "awesome", sep=" *** ")

# No separator
print("A", "B", "C", sep="")
print()

# ============================================
# PRINT END PARAMETER
# ============================================

print("=" * 50)
print("CUSTOM END CHARACTERS")
print("=" * 50)

# Default end is new line
print("First")
print("Second")

# Custom end
print("First", end=" | ")
print("Second", end=" | ")
print("Third")

# Printing on same line in a loop
for i in range(1, 6):
    print(i, end=" ")
print()  # New line after loop
print()

# ============================================
# PRINTING MULTIPLE LINES
# ============================================

print("=" * 50)
print("MULTI-LINE STRINGS")
print("=" * 50)

# Using triple quotes
message = """
Dear Student,

Welcome to Python Programming!
We hope you enjoy the course.

Best regards,
The Python Team
"""
print(message)

# ============================================
# PRINTING VARIABLES WITH EXPRESSIONS
# ============================================

print("=" * 50)
print("EXPRESSIONS IN F-STRINGS")
print("=" * 50)

x = 10
y = 20

# Calculations in f-strings
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")

# Calling functions in f-strings
name = "alice"
print(f"Uppercase: {name.upper()}")
print(f"Capitalized: {name.capitalize()}")

# Conditional in f-strings
score = 85
print(f"Result: {'Pass' if score >= 60 else 'Fail'}")
print()

# ============================================
# DEBUGGING WITH PRINT
# ============================================

print("=" * 50)
print("DEBUGGING WITH PRINT")
print("=" * 50)

# Print variable name and value (Python 3.8+)
username = "john_doe"
user_age = 30
print(f"{username=}")
print(f"{user_age=}")

# Print type information
print(f"Type of username: {type(username)}")
print(f"Type of user_age: {type(user_age)}")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Receipt example
item1 = "Laptop"
price1 = 999.99

item2 = "Mouse"
price2 = 29.99

item3 = "Keyboard"
price3 = 79.99

subtotal = price1 + price2 + price3
tax = subtotal * 0.08
total = subtotal + tax

print("\n" + "=" * 40)
print(" " * 15 + "RECEIPT")
print("=" * 40)
print(f"{item1:<20} ${price1:>10.2f}")
print(f"{item2:<20} ${price2:>10.2f}")
print(f"{item3:<20} ${price3:>10.2f}")
print("-" * 40)
print(f"{'Subtotal:':<20} ${subtotal:>10.2f}")
print(f"{'Tax (8%):':<20} ${tax:>10.2f}")
print("=" * 40)
print(f"{'TOTAL:':<20} ${total:>10.2f}")
print("=" * 40 + "\n")

# Progress indicator
print("Loading", end="")
for i in range(5):
    print(".", end="", flush=True)
print(" Done!")
