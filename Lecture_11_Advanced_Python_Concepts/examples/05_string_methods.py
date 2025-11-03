"""
Lecture 11: String Methods Deep Dive
This file demonstrates essential string methods used in automation testing.
"""

# ============================================
# SPLIT - BREAKING STRINGS INTO LISTS
# ============================================
print("=" * 60)
print("SPLIT - BREAKING STRINGS INTO LISTS")
print("=" * 60)

# Basic split (splits on whitespace by default)
text = "Hello World Python"
words = text.split()
print(f"Text: '{text}'")
print(f"Split result: {words}")
print()

# Split on specific delimiter
csv_data = "Alice,25,NYC,Developer"
fields = csv_data.split(',')
print(f"CSV data: '{csv_data}'")
print(f"Split by comma: {fields}")
print()

# Split with maxsplit parameter
path = "home/user/documents/file.txt"
parts = path.split('/', maxsplit=2)
print(f"Path: '{path}'")
print(f"Split with maxsplit=2: {parts}")
print()

# Split lines
multiline = """Line 1
Line 2
Line 3"""
lines = multiline.split('\n')
print(f"Multiline text split by newline: {lines}")
print()

# Splitlines method (better for lines)
lines2 = multiline.splitlines()
print(f"Using splitlines(): {lines2}")
print()

# ============================================
# JOIN - COMBINING LISTS INTO STRINGS
# ============================================
print("=" * 60)
print("JOIN - COMBINING LISTS INTO STRINGS")
print("=" * 60)

# Basic join
words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"Words: {words}")
print(f"Joined with space: '{joined}'")
print()

# Join with different separator
csv = ",".join(["Alice", "25", "NYC"])
print(f"Joined with comma: '{csv}'")

path = "/".join(["home", "user", "documents"])
print(f"Joined with slash: '{path}'")

hyphenated = "-".join(["2024", "12", "25"])
print(f"Joined with hyphen: '{hyphenated}'")
print()

# Join with no separator
chars = ["H", "e", "l", "l", "o"]
word = "".join(chars)
print(f"Characters: {chars}")
print(f"Joined with no separator: '{word}'")
print()

# ============================================
# STRIP - REMOVING WHITESPACE
# ============================================
print("=" * 60)
print("STRIP - REMOVING WHITESPACE")
print("=" * 60)

# Remove whitespace from both ends
text = "   Hello World   "
stripped = text.strip()
print(f"Original: '{text}'")
print(f"Stripped: '{stripped}'")
print()

# Remove from left only
left_stripped = text.lstrip()
print(f"Left stripped: '{left_stripped}'")

# Remove from right only
right_stripped = text.rstrip()
print(f"Right stripped: '{right_stripped}'")
print()

# Strip specific characters
text = "***Hello World***"
cleaned = text.strip('*')
print(f"Original: '{text}'")
print(f"Strip asterisks: '{cleaned}'")
print()

# Common use case: clean user input
user_input = "  alice@example.com  \n"
cleaned_email = user_input.strip()
print(f"User input: '{user_input}'")
print(f"Cleaned: '{cleaned_email}'")
print()

# ============================================
# REPLACE - SUBSTITUTING SUBSTRINGS
# ============================================
print("=" * 60)
print("REPLACE - SUBSTITUTING SUBSTRINGS")
print("=" * 60)

# Basic replace
text = "Hello World"
replaced = text.replace("World", "Python")
print(f"Original: '{text}'")
print(f"Replaced: '{replaced}'")
print()

# Replace multiple occurrences
text = "apple banana apple orange apple"
replaced = text.replace("apple", "fruit")
print(f"Original: '{text}'")
print(f"Replaced all: '{replaced}'")
print()

# Replace with count parameter
replaced_once = text.replace("apple", "fruit", 1)
print(f"Replaced first only: '{replaced_once}'")
print()

# Remove substring (replace with empty string)
text = "Hello, World!"
no_comma = text.replace(",", "")
print(f"Original: '{text}'")
print(f"Without comma: '{no_comma}'")
print()

# ============================================
# CASE METHODS
# ============================================
print("=" * 60)
print("CASE METHODS")
print("=" * 60)

text = "Hello World Python"

print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"swapcase(): '{text.swapcase()}'")
print()

# Case-insensitive comparison
name1 = "Alice"
name2 = "ALICE"
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"Case-insensitive comparison: {name1.lower() == name2.lower()}")
print()

# ============================================
# STARTSWITH AND ENDSWITH
# ============================================
print("=" * 60)
print("STARTSWITH AND ENDSWITH")
print("=" * 60)

# Check prefix
filename = "report.pdf"
print(f"Filename: '{filename}'")
print(f"Starts with 'report': {filename.startswith('report')}")
print(f"Starts with 'data': {filename.startswith('data')}")
print()

# Check suffix
print(f"Ends with '.pdf': {filename.endswith('.pdf')}")
print(f"Ends with '.txt': {filename.endswith('.txt')}")
print()

# Multiple options (tuple)
file_list = ["data.csv", "report.pdf", "image.jpg", "script.py"]
for f in file_list:
    if f.endswith(('.pdf', '.jpg', '.png')):
        print(f"{f} is a document or image")
print()

# ============================================
# FIND AND INDEX
# ============================================
print("=" * 60)
print("FIND AND INDEX")
print("=" * 60)

text = "Hello World Python"

# find() returns -1 if not found
position = text.find("World")
print(f"Text: '{text}'")
print(f"Position of 'World': {position}")

position = text.find("Java")
print(f"Position of 'Java': {position} (not found)")
print()

# index() raises exception if not found
try:
    position = text.index("Python")
    print(f"Position of 'Python': {position}")
except ValueError as e:
    print(f"Error: {e}")

# rfind() - find from right
text = "apple banana apple orange apple"
print(f"\nText: '{text}'")
print(f"First 'apple': {text.find('apple')}")
print(f"Last 'apple': {text.rfind('apple')}")
print()

# ============================================
# COUNT
# ============================================
print("=" * 60)
print("COUNT")
print("=" * 60)

text = "apple banana apple orange apple"
count = text.count("apple")
print(f"Text: '{text}'")
print(f"Count of 'apple': {count}")

text = "Hello World"
count = text.count("l")
print(f"\nText: '{text}'")
print(f"Count of 'l': {count}")
print()

# ============================================
# VALIDATION METHODS
# ============================================
print("=" * 60)
print("VALIDATION METHODS")
print("=" * 60)

# isdigit() - check if all characters are digits
test_strings = ["12345", "123abc", ""]
print("Testing isdigit():")
for s in test_strings:
    print(f"  '{s}'.isdigit() = {s.isdigit()}")
print()

# isalpha() - check if all characters are alphabetic
test_strings = ["Hello", "Hello123", "Hello World"]
print("Testing isalpha():")
for s in test_strings:
    print(f"  '{s}'.isalpha() = {s.isalpha()}")
print()

# isalnum() - check if all characters are alphanumeric
test_strings = ["Hello123", "Hello 123", "Hello!"]
print("Testing isalnum():")
for s in test_strings:
    print(f"  '{s}'.isalnum() = {s.isalnum()}")
print()

# isspace() - check if all characters are whitespace
test_strings = ["   ", "Hello", ""]
print("Testing isspace():")
for s in test_strings:
    print(f"  '{s}'.isspace() = {s.isspace()}")
print()

# ============================================
# FORMATTING METHODS
# ============================================
print("=" * 60)
print("FORMATTING METHODS")
print("=" * 60)

# center()
text = "Python"
centered = text.center(20, '-')
print(f"Centered: '{centered}'")

# ljust() and rjust()
text = "Name"
print(f"Left justified: '{text.ljust(20, '.')}'")
print(f"Right justified: '{text.rjust(20, '.')}'")
print()

# zfill() - pad with zeros
number = "42"
padded = number.zfill(5)
print(f"Number: '{number}'")
print(f"Zero-padded to 5 digits: '{padded}'")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Parse log line
log_line = "2024-12-25 10:30:45 ERROR Database connection failed"
parts = log_line.split(' ', 3)  # Split into 4 parts max
timestamp = f"{parts[0]} {parts[1]}"
level = parts[2]
message = parts[3]
print("Log parsing:")
print(f"  Timestamp: {timestamp}")
print(f"  Level: {level}")
print(f"  Message: {message}")
print()

# Example 2: Clean and validate email
def clean_email(email):
    """Clean and validate email address"""
    cleaned = email.strip().lower()
    if '@' in cleaned and '.' in cleaned.split('@')[1]:
        return cleaned
    return None

emails = ["  Alice@Example.COM  ", "invalid.email", "bob@test.com"]
print("Email cleaning:")
for email in emails:
    cleaned = clean_email(email)
    print(f"  '{email}' -> {cleaned}")
print()

# Example 3: Build URL from parts
def build_url(base, *paths, **params):
    """Build URL from base, paths, and query parameters"""
    # Join paths
    url = base.rstrip('/')
    if paths:
        url += '/' + '/'.join(str(p).strip('/') for p in paths)

    # Add query parameters
    if params:
        query = '&'.join(f"{k}={v}" for k, v in params.items())
        url += '?' + query

    return url

url = build_url("https://api.example.com", "users", 123, "posts", page=1, limit=10)
print(f"Built URL: {url}")
print()

# Example 4: Extract file information
def parse_filename(filename):
    """Extract name and extension from filename"""
    if '.' in filename:
        parts = filename.rsplit('.', 1)  # Split from right, once
        return {"name": parts[0], "extension": parts[1]}
    return {"name": filename, "extension": None}

files = ["document.pdf", "archive.tar.gz", "README"]
print("File parsing:")
for f in files:
    info = parse_filename(f)
    print(f"  {f} -> {info}")
print()

# Example 5: Format table output
def format_table(rows):
    """Format data as table"""
    # Calculate column widths
    if not rows:
        return ""

    # Get max width for each column
    col_widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]

    # Format rows
    lines = []
    for row in rows:
        formatted_row = " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths))
        lines.append(formatted_row)

    # Add separator after header
    separator = "-+-".join("-" * width for width in col_widths)
    lines.insert(1, separator)

    return "\n".join(lines)

data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"],
    ["Charlie", "35", "Chicago"]
]

print("Formatted table:")
print(format_table(data))
print()

# ============================================
# CHEAT SHEET
# ============================================
print("=" * 60)
print("STRING METHODS CHEAT SHEET")
print("=" * 60)
print("""
Splitting & Joining:
  .split(sep, maxsplit)  - Split string into list
  .join(iterable)        - Join list into string
  .splitlines()          - Split on line breaks

Whitespace:
  .strip()               - Remove whitespace from both ends
  .lstrip()              - Remove whitespace from left
  .rstrip()              - Remove whitespace from right

Modification:
  .replace(old, new, count) - Replace substring
  .upper()               - Convert to uppercase
  .lower()               - Convert to lowercase
  .title()               - Title Case Each Word
  .capitalize()          - Capitalize first letter only

Searching:
  .find(sub)             - Find substring (-1 if not found)
  .index(sub)            - Find substring (raises exception)
  .count(sub)            - Count occurrences
  .startswith(prefix)    - Check if starts with
  .endswith(suffix)      - Check if ends with

Validation:
  .isdigit()             - All characters are digits
  .isalpha()             - All characters are letters
  .isalnum()             - All characters are alphanumeric
  .isspace()             - All characters are whitespace

Formatting:
  .center(width, fill)   - Center string with padding
  .ljust(width, fill)    - Left justify
  .rjust(width, fill)    - Right justify
  .zfill(width)          - Pad with zeros
""")
