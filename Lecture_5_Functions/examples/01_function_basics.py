"""
Lecture 5 - Example 1: Function Basics
======================================
Learn how to define and call basic functions.
"""

# 1. SIMPLE FUNCTION - NO PARAMETERS, NO RETURN
# ==============================================

def say_hello():
    """Prints a simple greeting message."""
    print("Hello, World!")

# Call the function
say_hello()

print("-" * 50)


# 2. FUNCTION WITH DOCUMENTATION
# ==============================

def welcome_message():
    """
    Display a welcome message to the user.

    This function prints a multi-line welcome message
    with information about the Python course.
    """
    print("Welcome to the Python Automation Course!")
    print("In this course, you'll learn Python and Playwright")
    print("Let's master automation testing together!")

welcome_message()

print("-" * 50)


# 3. MULTIPLE FUNCTION CALLS
# ==========================

def print_separator():
    """Prints a decorative separator line."""
    print("=" * 40)

print_separator()
print("Section 1: Introduction")
print_separator()
print("This is the content of section 1")
print_separator()

print("-" * 50)


# 4. FUNCTIONS CAN CALL OTHER FUNCTIONS
# ======================================

def print_header():
    """Prints a formatted header."""
    print("*" * 40)
    print("*   PYTHON AUTOMATION COURSE   *")
    print("*" * 40)

def print_footer():
    """Prints a formatted footer."""
    print("-" * 40)
    print("  End of Section")
    print("-" * 40)

def display_content():
    """Displays formatted content with header and footer."""
    print_header()
    print("\nToday's Topic: Functions")
    print("Functions help us organize code")
    print_footer()

# Call the main function
display_content()

print("-" * 50)


# 5. WHY USE FUNCTIONS?
# =====================

# WITHOUT FUNCTIONS (Repetitive code)
print("=" * 30)
print("Processing Item 1...")
print("Item 1 processed successfully")
print("=" * 30)

print("=" * 30)
print("Processing Item 2...")
print("Item 2 processed successfully")
print("=" * 30)

print("=" * 30)
print("Processing Item 3...")
print("Item 3 processed successfully")
print("=" * 30)

print("\n" + "-" * 50 + "\n")

# WITH FUNCTIONS (DRY - Don't Repeat Yourself)
def process_item(item_number):
    """Process an item and display status."""
    print("=" * 30)
    print(f"Processing Item {item_number}...")
    print(f"Item {item_number} processed successfully")
    print("=" * 30)

# Much cleaner!
process_item(1)
process_item(2)
process_item(3)

print("-" * 50)


# 6. FUNCTION NAMING CONVENTIONS
# ==============================

# Good function names (descriptive, snake_case)
def calculate_total():
    pass

def send_email():
    pass

def validate_user_input():
    pass

def get_current_date():
    pass

# Bad function names (avoid these)
def func1():  # Not descriptive
    pass

def CalculateTotal():  # Should use snake_case, not PascalCase
    pass

def x():  # Too short, not descriptive
    pass

def ThisIsAVeryLongFunctionNameThatIsHardToRead():  # Too long
    pass

print("Function naming examples defined (not called)")

print("-" * 50)


# 7. AUTOMATION EXAMPLE - BASIC TEST STEP FUNCTIONS
# =================================================

def start_browser():
    """Simulates starting a browser."""
    print("Starting browser...")
    print("Browser started successfully")

def navigate_to_login_page():
    """Simulates navigating to login page."""
    print("Navigating to login page...")
    print("Login page loaded")

def close_browser():
    """Simulates closing the browser."""
    print("Closing browser...")
    print("Browser closed")

def run_simple_test():
    """Runs a simple test sequence."""
    print("\n🧪 Running Test: Basic Navigation")
    start_browser()
    navigate_to_login_page()
    close_browser()
    print("✅ Test completed!\n")

# Run the test
run_simple_test()

print("=" * 50)
print("Example complete! You've learned function basics.")
print("=" * 50)
