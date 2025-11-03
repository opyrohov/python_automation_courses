"""
Exercise 3: Datetime and String Methods

Instructions:
1. Complete each task below
2. Run the file to check your results
3. Pay attention to format codes and method usage

Estimated time: 20-25 minutes
"""

from datetime import datetime, date, timedelta

# ============================================
# TASK 1: Format Current Date
# ============================================
# Format the current date as "December 25, 2024"
# YOUR CODE HERE:
now = datetime.now()
formatted_date = ""  # Use strftime to format

# Test your code (don't modify this)
print("=" * 50)
print("TASK 1: Format Current Date")
print("=" * 50)
print(f"Formatted date: {formatted_date}")
print(f"Expected format: 'Month Day, Year'")
print()

# ============================================
# TASK 2: Parse Date String
# ============================================
# Parse this date string into a datetime object
date_string = "2024-12-25 14:30:00"
# YOUR CODE HERE:
parsed_date = None  # Use strptime to parse

# Test your code (don't modify this)
print("=" * 50)
print("TASK 2: Parse Date String")
print("=" * 50)
print(f"Original string: '{date_string}'")
print(f"Parsed datetime: {parsed_date}")
print(f"Type: {type(parsed_date)}")
print()

# ============================================
# TASK 3: Date Arithmetic
# ============================================
# Calculate the date 30 days from today
# YOUR CODE HERE:
today = date.today()
future_date = None  # Add 30 days

# Test your code (don't modify this)
print("=" * 50)
print("TASK 3: Date Arithmetic")
print("=" * 50)
print(f"Today: {today}")
print(f"30 days from now: {future_date}")
print()

# ============================================
# TASK 4: Calculate Age
# ============================================
# Calculate age from birth date (use the provided function structure)
birth_date = date(2000, 6, 15)
# YOUR CODE HERE:
def calculate_age(birth_date):
    # Your implementation here
    pass

age = calculate_age(birth_date)

# Test your code (don't modify this)
print("=" * 50)
print("TASK 4: Calculate Age")
print("=" * 50)
print(f"Birth date: {birth_date}")
print(f"Age: {age}")
print()

# ============================================
# TASK 5: Compare Dates
# ============================================
# Check if event_date is in the future
event_date = datetime(2025, 12, 31)
current = datetime.now()
# YOUR CODE HERE:
is_future = False  # Compare dates

# Test your code (don't modify this)
print("=" * 50)
print("TASK 5: Compare Dates")
print("=" * 50)
print(f"Event date: {event_date.date()}")
print(f"Is in future: {is_future}")
print()

# ============================================
# TASK 6: String Split
# ============================================
# Split this CSV line into a list
csv_line = "Alice,25,NYC,Developer"
# YOUR CODE HERE:
fields = []  # Use split method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 6: String Split")
print("=" * 50)
print(f"CSV line: '{csv_line}'")
print(f"Fields: {fields}")
print(f"Expected: ['Alice', '25', 'NYC', 'Developer']")
print()

# ============================================
# TASK 7: String Join
# ============================================
# Join these words with hyphens
words = ["Python", "Automation", "Testing"]
# YOUR CODE HERE:
joined = ""  # Use join method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 7: String Join")
print("=" * 50)
print(f"Words: {words}")
print(f"Joined: '{joined}'")
print(f"Expected: 'Python-Automation-Testing'")
print()

# ============================================
# TASK 8: String Strip
# ============================================
# Clean this user input (remove whitespace)
user_input = "  test@example.com  \n"
# YOUR CODE HERE:
cleaned = ""  # Use strip method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 8: String Strip")
print("=" * 50)
print(f"Original: '{user_input}'")
print(f"Cleaned: '{cleaned}'")
print(f"Expected: 'test@example.com'")
print()

# ============================================
# TASK 9: String Replace
# ============================================
# Replace all spaces with underscores
text = "Hello World Python"
# YOUR CODE HERE:
replaced = ""  # Use replace method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 9: String Replace")
print("=" * 50)
print(f"Original: '{text}'")
print(f"Replaced: '{replaced}'")
print(f"Expected: 'Hello_World_Python'")
print()

# ============================================
# TASK 10: Check String Prefix/Suffix
# ============================================
# Check if filename starts with "test_" and ends with ".py"
filename = "test_login.py"
# YOUR CODE HERE:
starts_with_test = False  # Use startswith
ends_with_py = False  # Use endswith

# Test your code (don't modify this)
print("=" * 50)
print("TASK 10: Check Prefix/Suffix")
print("=" * 50)
print(f"Filename: '{filename}'")
print(f"Starts with 'test_': {starts_with_test}")
print(f"Ends with '.py': {ends_with_py}")
print(f"Expected: Both True")
print()

# ============================================
# TASK 11: Extract Substring
# ============================================
# Extract the domain from this email address
email = "user@example.com"
# YOUR CODE HERE:
# Hint: Use split to separate by '@', then get the second part
domain = ""

# Test your code (don't modify this)
print("=" * 50)
print("TASK 11: Extract Domain")
print("=" * 50)
print(f"Email: '{email}'")
print(f"Domain: '{domain}'")
print(f"Expected: 'example.com'")
print()

# ============================================
# TASK 12: Case Conversion
# ============================================
# Convert to uppercase and lowercase
text = "Python Automation"
# YOUR CODE HERE:
uppercase = ""  # Use upper method
lowercase = ""  # Use lower method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 12: Case Conversion")
print("=" * 50)
print(f"Original: '{text}'")
print(f"Uppercase: '{uppercase}'")
print(f"Lowercase: '{lowercase}'")
print()

# ============================================
# TASK 13: Count Occurrences
# ============================================
# Count how many times "test" appears in this string
text = "test test test testing tested test"
# YOUR CODE HERE:
count = 0  # Use count method

# Test your code (don't modify this)
print("=" * 50)
print("TASK 13: Count Occurrences")
print("=" * 50)
print(f"Text: '{text}'")
print(f"Count of 'test': {count}")
print(f"Expected: 4")
print()

# ============================================
# TASK 14: Build URL
# ============================================
# Build a URL from these parts
base = "https://api.example.com"
endpoint = "users"
user_id = "123"
# YOUR CODE HERE:
# Use string formatting or join to build: base/endpoint/user_id
url = ""

# Test your code (don't modify this)
print("=" * 50)
print("TASK 14: Build URL")
print("=" * 50)
print(f"Base: '{base}'")
print(f"Endpoint: '{endpoint}'")
print(f"User ID: '{user_id}'")
print(f"Built URL: '{url}'")
print(f"Expected: 'https://api.example.com/users/123'")
print()

# ============================================
# BONUS TASK: Timestamp for Filename
# ============================================
# Create a filename with current timestamp
# Format: "screenshot_20241225_143045.png"
# YOUR CODE HERE:
filename_with_timestamp = ""  # Use datetime.now() and strftime

# Test your code (don't modify this)
print("=" * 50)
print("BONUS: Timestamp Filename")
print("=" * 50)
print(f"Generated filename: '{filename_with_timestamp}'")
print(f"Expected format: 'screenshot_YYYYMMDD_HHMMSS.png'")
print()

print("=" * 50)
print("Congratulations! You completed Exercise 3!")
print("=" * 50)
