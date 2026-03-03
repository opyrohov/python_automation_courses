"""
Lecture 2: String Manipulation
This file demonstrates various string manipulation techniques in Python.
"""

# ============================================
# STRING BASICS
# ============================================
# Strings can be created with single or double quotes

text = "Hello, World!"
name = 'Python Automation'

print("Basic Strings:")
print(text)
print(name)
print()

# ============================================
# STRING METHODS - CASE MANIPULATION
# ============================================

message = "Welcome to Python Automation"

print("Case Manipulation:")
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Title Case: {message.title()}")
print(f"Swap Case: {message.swapcase()}")
print()

# ============================================
# STRING METHODS - WHITESPACE
# ============================================

messy_text = "   extra spaces   "
print("Whitespace Handling:")
print(f"Original: '{messy_text}'")
print(f"Strip (both ends): '{messy_text.strip()}'")
print(f"Left strip: '{messy_text.lstrip()}'")
print(f"Right strip: '{messy_text.rstrip()}'")
print()

# ============================================
# STRING METHODS - REPLACE
# ============================================

url = "https://example.com/old-page"
print("String Replacement:")
print(f"Original URL: {url}")
print(f"Updated URL: {url.replace('old-page', 'new-page')}")
print()

# Replace multiple occurrences
text_with_repeats = "Python is great. Python is powerful. Python is fun."
print(f"Original: {text_with_repeats}")
print(f"Replace Python with JavaScript: {text_with_repeats.replace('Python', 'JavaScript')}")
print()

# ============================================
# STRING METHODS - SPLIT & JOIN
# ============================================

# Split strings into lists
csv_data = "John,Doe,30,Engineer"
print("Splitting Strings:")
print(f"CSV data: {csv_data}")
print(f"Split by comma: {csv_data.split(',')}")
print()

sentence = "This is a test sentence"
words = sentence.split()  # Split by whitespace (default)
print(f"Sentence: {sentence}")
print(f"Words: {words}")
print()

# Join lists into strings
word_list = ["Python", "is", "awesome"]
print("Joining Strings:")
print(f"Word list: {word_list}")
print(f"Joined with spaces: {' '.join(word_list)}")
print(f"Joined with dashes: {'-'.join(word_list)}")
print()

# ============================================
# STRING SLICING
# ============================================

text = "Python Programming"
print("String Slicing:")
print(f"Original: {text}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[0:6]}")
print(f"Characters 7 to end: {text[7:]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse string: {text[::-1]}")
print()

# ============================================
# STRING SEARCHING
# ============================================

page_text = "Welcome to our website. Please login to continue."

print("String Searching:")
print(f"Text: {page_text}")
print(f"Contains 'login': {'login' in page_text}")
print(f"Contains 'signup': {'signup' in page_text}")
print(f"Find 'login' position: {page_text.find('login')}")
print(f"Find 'signup' position: {page_text.find('signup')}")  # Returns -1 if not found
print(f"Count 'e': {page_text.count('e')}")
print()

# ============================================
# STRING CHECKING METHODS
# ============================================

email = "user@example.com"
username = "admin123"
number_str = "12345"
alpha_str = "Python"

print("String Checking Methods:")
print(f"'{email}' contains '@': {'@' in email}")
print(f"'{email}' starts with 'user': {email.startswith('user')}")
print(f"'{email}' ends with '.com': {email.endswith('.com')}")
print(f"'{username}' is alphanumeric: {username.isalnum()}")
print(f"'{number_str}' is numeric: {number_str.isdigit()}")
print(f"'{alpha_str}' is alphabetic: {alpha_str.isalpha()}")
print()

# ============================================
# STRING FORMATTING
# ============================================

# Method 1: f-strings (recommended - modern and readable)
name = "Alice"
age = 25
city = "New York"

print("String Formatting with f-strings:")
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city}.")
print()

# Expressions in f-strings
price = 19.99
quantity = 3
print(f"Total cost: ${price * quantity:.2f}")
print()

# Method 2: .format() method
print("String Formatting with .format():")
print("My name is {} and I am {} years old.".format(name, age))
print("Hello, {0}! You are {1} years old.".format(name, age))
print()

# Method 3: % formatting (old style)
print("String Formatting with % operator:")
print("My name is %s and I am %d years old." % (name, age))
print()

# ============================================
# MULTILINE STRINGS
# ============================================

multi_line = """This is a multi-line string.
It can span multiple lines.
Very useful for templates and long text."""

print("Multiline String:")
print(multi_line)
print()

# ============================================
# STRING CONCATENATION
# ============================================

first_name = "John"
last_name = "Doe"

# Method 1: + operator
full_name = first_name + " " + last_name
print(f"Concatenation with +: {full_name}")

# Method 2: f-strings (better)
full_name = f"{first_name} {last_name}"
print(f"Concatenation with f-string: {full_name}")

# Method 3: join (best for multiple strings)
parts = [first_name, last_name]
full_name = " ".join(parts)
print(f"Concatenation with join: {full_name}")
print()

# ============================================
# PRACTICAL EXAMPLE: URL MANIPULATION
# ============================================

base_url = "https://example.com"
endpoint = "/api/users"
user_id = "12345"

# Build complete URL
full_url = f"{base_url}{endpoint}/{user_id}"
print("URL Building:")
print(f"Full URL: {full_url}")

# Extract domain
domain = base_url.replace("https://", "").replace("http://", "")
print(f"Domain: {domain}")

# Extract path
path = full_url.split(domain)[1] if domain in full_url else ""
print(f"Path: {path}")
print()

# ============================================
# PRACTICAL EXAMPLE: TEXT VALIDATION
# ============================================

page_title = "Login - My Application"
expected_keywords = ["Login", "Application"]

print("Text Validation:")
print(f"Page title: {page_title}")
for keyword in expected_keywords:
    if keyword in page_title:
        print(f"✓ Found keyword: {keyword}")
    else:
        print(f"✗ Missing keyword: {keyword}")
