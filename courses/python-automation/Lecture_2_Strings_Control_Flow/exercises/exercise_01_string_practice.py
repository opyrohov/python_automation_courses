"""
Exercise 1: String Manipulation Practice
Complete the exercises below to practice string manipulation skills.
"""

# ============================================
# EXERCISE 1: Email Validation
# ============================================
print("Exercise 1: Email Validation")
print("-" * 40)

# TODO: Create a variable called 'email' with your email address
email = ""  # Replace with your email

# TODO: Check if the email contains '@' and '.'
# Print "Valid email format" if it does, "Invalid email format" if it doesn't


# TODO: Extract and print the domain name (everything after @)
# Example: "user@example.com" should print "example.com"


print()

# ============================================
# EXERCISE 2: Name Formatting
# ============================================
print("Exercise 2: Name Formatting")
print("-" * 40)

# TODO: Create variables for first_name and last_name
first_name = ""  # Replace with a first name
last_name = ""   # Replace with a last name

# TODO: Create a full_name variable by combining first_name and last_name


# TODO: Print the full name in the following formats:
# 1. "John Doe"
# 2. "DOE, John" (last name uppercase, then first name)
# 3. "john.doe" (lowercase with dot separator)


print()

# ============================================
# EXERCISE 3: URL Manipulation
# ============================================
print("Exercise 3: URL Manipulation")
print("-" * 40)

url = "https://www.example.com/products/item-12345"

# TODO: Extract and print the domain name (www.example.com)


# TODO: Extract and print the product ID (12345)


# TODO: Create a new URL by replacing "products" with "items"


print()

# ============================================
# EXERCISE 4: Text Cleaning
# ============================================
print("Exercise 4: Text Cleaning")
print("-" * 40)

messy_text = "   Welcome to Python Programming!   "

# TODO: Remove extra spaces from both ends


# TODO: Convert to lowercase


# TODO: Count how many times the letter 'o' appears


# TODO: Replace "Python" with "JavaScript"


print()

# ============================================
# EXERCISE 5: Password Strength Checker
# ============================================
print("Exercise 5: Password Strength Checker")
print("-" * 40)

password = "MyPassword123"

# TODO: Check and print the password length


# TODO: Check if password contains numbers (use any() with isdigit())
# Hint: any(char.isdigit() for char in password)


# TODO: Check if password contains uppercase letters


# TODO: Check if password contains lowercase letters


# TODO: Based on the checks above, print whether it's a strong password
# Strong password: length >= 8, contains numbers, uppercase, and lowercase


print()

# ============================================
# EXERCISE 6: Log Message Parser
# ============================================
print("Exercise 6: Log Message Parser")
print("-" * 40)

log_message = "[ERROR] 2024-01-15 10:30:45 - Database connection failed"

# TODO: Extract and print the log level (ERROR)


# TODO: Extract and print the timestamp (2024-01-15 10:30:45)


# TODO: Extract and print the actual message (Database connection failed)


# TODO: Check if this is an error message (contains "[ERROR]")


print()

# ============================================
# EXERCISE 7: CSV Data Processing
# ============================================
print("Exercise 7: CSV Data Processing")
print("-" * 40)

csv_line = "John,Doe,30,Engineer,New York"

# TODO: Split the CSV line into a list


# TODO: Create variables for each field: first_name, last_name, age, job, city


# TODO: Print a formatted message using these variables
# Example: "John Doe, 30, works as an Engineer in New York"


print()

# ============================================
# EXERCISE 8: Page Title Verification
# ============================================
print("Exercise 8: Page Title Verification (Automation Scenario)")
print("-" * 40)

page_title = "Shopping Cart - MyStore"
expected_keywords = ["Shopping", "Cart"]

# TODO: Check if both keywords appear in the page_title
# Print "✓ Found: [keyword]" for each keyword found
# Print "✗ Missing: [keyword]" for each keyword not found


print()

# ============================================
# BONUS CHALLENGE: Username Generator
# ============================================
print("BONUS: Username Generator")
print("-" * 40)

full_name = "John Michael Doe"
birth_year = 1995

# TODO: Generate a username using the following format:
# First letter of first name + full last name + last 2 digits of birth year
# Example: "John Michael Doe" + 1995 = "jdoe95"
# Convert to lowercase


print()

print("=" * 40)
print("Great job! Check SOLUTIONS.md for answers.")
print("=" * 40)
