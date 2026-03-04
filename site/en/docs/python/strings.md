# Strings

Strings are one of the most important data types in Python. In QA automation, strings are everywhere: URLs, test data, logs, error messages, API responses. This page covers everything you need to know about working with strings.

## Creating Strings

Python supports multiple ways to create strings.

```python
# Single quotes
name = 'QA Engineer'

# Double quotes
title = "Test Automation"

# Single and double are equivalent
print('Hello' == "Hello")  # True

# Quotes inside strings
message = "It's a test"          # double outside, single inside
html = '<div class="header">'    # single outside, double inside

# Triple quotes — multi-line strings
description = """
This is a multi-line string.
It preserves all line breaks
and indentation.
"""

# Triple single quotes also work
sql_query = '''
    SELECT * FROM users
    WHERE status = 'active'
    ORDER BY created_at DESC
'''
```

::: tip Which convention to choose?
In Python, both variants (single and double quotes) are equivalent. The key is to be consistent within your project. PEP 8 does not dictate a specific style, but most QA projects use double quotes.
:::

## Indexing and Slicing

A string is a sequence of characters. Each character has an index, starting from `0`.

```python
text = "Python"
#       P y t h o n
#       0 1 2 3 4 5
#      -6-5-4-3-2-1

# Indexing
print(text[0])    # P — first character
print(text[5])    # n — last character
print(text[-1])   # n — last (negative index)
print(text[-2])   # o — second to last

# Slicing: [start:stop:step]
print(text[0:3])   # Pyt — characters from 0 to 2 (stop is excluded)
print(text[2:])    # thon — from index 2 to the end
print(text[:3])    # Pyt — from the beginning to index 2
print(text[::2])   # Pto — every second character
print(text[::-1])  # nohtyP — reverse the string

# String length
print(len(text))   # 6
```

::: warning IndexError
Attempting to access a non-existent index will raise an error:
```python
text = "Python"
print(text[10])  # IndexError: string index out of range
```
But slices do not raise errors — they simply return what is available:
```python
print(text[2:100])  # thon — no error
```
:::

::: info QA Example: analyzing responses
```python
# Extracting status code from a log line
log_line = "2024-01-15 10:30:45 INFO Response: 200 OK"

# Get the timestamp
timestamp = log_line[:19]  # "2024-01-15 10:30:45"

# Get the status code
status = log_line[-6:-3]   # "200"
```
:::

## String Methods

### Changing Case

```python
text = "Hello, QA World!"

print(text.upper())       # HELLO, QA WORLD!
print(text.lower())       # hello, qa world!
print(text.title())       # Hello, Qa World!
print(text.capitalize())  # Hello, qa world!
print(text.swapcase())    # hELLO, qa wORLD!
```

### Stripping Whitespace — strip()

```python
raw_input = "   test@example.com   "

print(raw_input.strip())   # "test@example.com" — both sides
print(raw_input.lstrip())  # "test@example.com   " — left only
print(raw_input.rstrip())  # "   test@example.com" — right only

# Stripping specific characters
url = "///api/users///"
print(url.strip("/"))  # "api/users"
```

::: tip QA Tip
Always use `.strip()` when processing input data in tests — extra whitespace is a common cause of test failures.
:::

### Splitting and Joining — split(), join()

```python
# split() — breaks a string into a list
csv_line = "John,Doe,QA,Senior"
parts = csv_line.split(",")
print(parts)  # ['John', 'Doe', 'QA', 'Senior']

# Splitting by whitespace (default)
sentence = "Python is awesome"
words = sentence.split()
print(words)  # ['Python', 'is', 'awesome']

# Limiting the number of splits
log = "ERROR: Connection failed: timeout"
parts = log.split(": ", 1)
print(parts)  # ['ERROR', 'Connection failed: timeout']

# join() — joins a list into a string
words = ['Python', 'for', 'QA']
result = " ".join(words)
print(result)  # "Python for QA"

# Building a path
path = "/".join(["api", "v1", "users", "123"])
print(path)  # "api/v1/users/123"

# CSV row
csv = ",".join(["name", "email", "role"])
print(csv)  # "name,email,role"
```

### Replacing — replace()

```python
text = "Hello World"
print(text.replace("World", "QA"))  # "Hello QA"

# Replacing multiple occurrences
url = "http://old-api.com/v1/users"
new_url = url.replace("old-api", "new-api")
print(new_url)  # "http://new-api.com/v1/users"

# Limiting the number of replacements
text = "a-b-c-d"
print(text.replace("-", " ", 2))  # "a b c-d"
```

### Searching — find(), count()

```python
text = "Hello, World! Hello, Python!"

# find() — returns the index of the first occurrence (-1 if not found)
print(text.find("Hello"))    # 0
print(text.find("Python"))   # 21
print(text.find("Java"))     # -1

# rfind() — search from the end
print(text.rfind("Hello"))   # 14

# index() — like find(), but raises ValueError if not found
# print(text.index("Java"))  # ValueError!

# count() — number of occurrences
print(text.count("Hello"))   # 2
print(text.count("l"))       # 4
```

### Checking Start and End — startswith(), endswith()

```python
filename = "test_report_2024.pdf"

print(filename.startswith("test"))   # True
print(filename.endswith(".pdf"))     # True
print(filename.endswith(".csv"))     # False

# Checking multiple options (tuple)
print(filename.endswith((".pdf", ".csv", ".xlsx")))  # True

url = "https://api.example.com/users"
print(url.startswith("https://"))  # True
print(url.startswith("http://"))   # False
```

::: info QA Example: filtering files
```python
# Find all screenshots among files
files = ["report.pdf", "screenshot_01.png", "data.csv", "error.jpg", "log.txt"]

images = [f for f in files if f.endswith((".png", ".jpg", ".jpeg"))]
print(images)  # ['screenshot_01.png', 'error.jpg']

# Find all test files
test_files = [f for f in files if f.startswith("test")]
```
:::

## String Formatting

### f-strings (recommended)

```python
name = "QA Engineer"
experience = 3
salary = 45000.50

# Basic formatting
print(f"I am a {name} with {experience} years of experience")

# Expressions inside f-strings
print(f"Experience in months: {experience * 12}")
print(f"Name uppercased: {name.upper()}")

# Number formatting
print(f"Salary: ${salary:,.2f}")    # Salary: $45,000.50
print(f"Percentage: {0.856:.1%}")   # Percentage: 85.6%
print(f"ID: {42:05d}")              # ID: 00042

# Text alignment
print(f"{'Test':<20} — PASSED")   # left-aligned
print(f"{'Test':>20} — PASSED")   # right-aligned
print(f"{'Test':^20} — PASSED")   # centered
```

### The .format() Method

```python
# Positional arguments
print("I am a {} with {} years of experience".format("QA", 3))

# Named arguments
print("URL: {protocol}://{host}:{port}".format(
    protocol="https",
    host="api.example.com",
    port=8080
))

# Indices
print("{0} vs {1}: {0} wins!".format("Python", "Java"))
# Python vs Java: Python wins!
```

::: info QA Example: generating test data
```python
# Generating test URLs
base_url = "https://api.example.com"
endpoints = ["users", "orders", "products"]

for endpoint in endpoints:
    url = f"{base_url}/api/v1/{endpoint}"
    print(f"Testing: {url}")

# Generating test emails
for i in range(1, 4):
    email = f"test_user_{i:03d}@qa-team.com"
    print(email)
# test_user_001@qa-team.com
# test_user_002@qa-team.com
# test_user_003@qa-team.com
```
:::

## Escape Characters

```python
# Common escape sequences
print("Line 1\nLine 2")             # \n — newline
print("Column1\tColumn2")           # \t — tab
print("Path: C:\\Users\\test")       # \\ — backslash
print("He said: \"Hello\"")         # \" — double quote
print('It\'s a test')               # \' — single quote

# Raw strings — ignore escape sequences
path = r"C:\Users\test\new_folder"
print(path)  # C:\Users\test\new_folder

# Useful for regular expressions
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # SSN pattern
```

::: tip Raw Strings in QA
Use raw strings (`r"..."`) for Windows paths and regular expressions — this saves you from escaping headaches.
:::

## String Immutability

Strings in Python are **immutable**. This means that once a string is created, it cannot be modified.

```python
text = "Hello"

# Cannot modify individual characters
# text[0] = "h"  # TypeError: 'str' object does not support item assignment

# You need to create a new string
text = "h" + text[1:]
print(text)  # "hello"

# All string methods return a NEW string
original = "Hello World"
upper = original.upper()
print(original)  # "Hello World" — original unchanged!
print(upper)     # "HELLO WORLD" — new string
```

::: warning Common Mistake
```python
name = "  John  "
name.strip()     # Returns "John", but name IS NOT CHANGED!
print(name)      # "  John  " — still has spaces

# Correct — save the result
name = name.strip()
print(name)      # "John"
```
:::

## Checking String Content

```python
# Checking character types
print("12345".isdigit())     # True — digits only
print("12.34".isdigit())     # False — dot is not a digit
print("Hello".isalpha())     # True — letters only
print("Hello1".isalpha())    # False — contains a digit
print("Hello1".isalnum())    # True — letters and/or digits
print("hello".islower())     # True — all lowercase
print("HELLO".isupper())     # True — all uppercase
print("   ".isspace())       # True — whitespace only
```

::: info QA Example: validating input data
```python
def validate_username(username):
    """Checks if a username is valid."""
    if not username:
        return False, "Username cannot be empty"
    if not username.isalnum():
        return False, "Only letters and digits are allowed"
    if len(username) < 3 or len(username) > 20:
        return False, "Length must be between 3 and 20 characters"
    return True, "OK"

# Testing
test_cases = ["admin", "user_1", "ab", "a" * 21, "", "validUser123"]
for tc in test_cases:
    is_valid, message = validate_username(tc)
    print(f"'{tc}' -> {is_valid}: {message}")
```
:::

## QA Automation Examples

### Parsing URLs

```python
url = "https://api.example.com:8080/api/v1/users?status=active&page=2"

# Manual URL parsing (for understanding)
protocol = url.split("://")[0]                    # "https"
domain_and_path = url.split("://")[1]             # "api.example.com:8080/api/v1/users?..."
domain = domain_and_path.split("/")[0]            # "api.example.com:8080"
path = "/" + "/".join(domain_and_path.split("/")[1:]).split("?")[0]  # "/api/v1/users"

print(f"Protocol: {protocol}")
print(f"Domain: {domain}")
print(f"Path: {path}")

# Parsing query parameters
query_string = url.split("?")[1]              # "status=active&page=2"
params = dict(p.split("=") for p in query_string.split("&"))
print(params)  # {'status': 'active', 'page': '2'}
```

::: tip In Real Projects
For URL parsing in real projects, use the `urllib.parse` module:
```python
from urllib.parse import urlparse, parse_qs

url = "https://api.example.com/users?status=active&page=2"
parsed = urlparse(url)
params = parse_qs(parsed.query)
print(params)  # {'status': ['active'], 'page': ['2']}
```
:::

### Email Validation (Simplified)

```python
def validate_email_simple(email):
    """Simplified email format validation."""
    email = email.strip()

    # Basic checks
    if "@" not in email:
        return False, "Missing @ symbol"
    if email.count("@") > 1:
        return False, "Too many @ symbols"

    local, domain = email.rsplit("@", 1)

    if not local:
        return False, "Empty local part"
    if not domain:
        return False, "Empty domain"
    if "." not in domain:
        return False, "Domain without dot"
    if domain.startswith(".") or domain.endswith("."):
        return False, "Invalid domain"

    return True, "Valid"

# Testing
test_emails = [
    "user@example.com",
    "invalid-email",
    "@no-local.com",
    "user@",
    "user@@double.com",
    "user@.bad.com",
]

for email in test_emails:
    is_valid, msg = validate_email_simple(email)
    status = "PASS" if is_valid else "FAIL"
    print(f"[{status}] {email:<25} — {msg}")
```

### Processing Log Files

```python
# Parsing log lines
log_lines = [
    "2024-01-15 10:30:45 INFO  Login successful for user: admin",
    "2024-01-15 10:30:46 ERROR Connection timeout after 30s",
    "2024-01-15 10:30:47 WARN  Retry attempt 2/3 for /api/users",
    "2024-01-15 10:30:48 INFO  Response: 200 OK (150ms)",
    "2024-01-15 10:30:49 ERROR AssertionError: Expected 200, got 500",
]

# Filtering errors
errors = [line for line in log_lines if " ERROR " in line]
print(f"Found {len(errors)} errors:")
for error in errors:
    print(f"  {error}")

# Extracting timestamps
timestamps = [line[:19] for line in log_lines]
print(f"\nTimestamps: {timestamps}")

# Searching for a specific pattern
for line in log_lines:
    if "timeout" in line.lower():
        # Extract the timeout value
        parts = line.split()
        for part in parts:
            if part.endswith("s") and part[:-1].isdigit():
                print(f"\nTimeout: {part}")
```

### Building Test Data

```python
# Generating test data for API
def build_test_user(user_id, role="user"):
    """Creates test user data."""
    return {
        "username": f"test_{role}_{user_id:04d}",
        "email": f"test_{role}_{user_id}@qa-automation.com",
        "password": f"Test_{role.capitalize()}_{user_id}!",
        "display_name": f"Test {role.title()} {user_id}",
    }

# Generating a set of test users
for i in range(1, 4):
    user = build_test_user(i, "admin")
    print(f"Username: {user['username']}")
    print(f"Email:    {user['email']}")
    print(f"Password: {user['password']}")
    print("---")

# Building SQL queries for test data
table = "users"
fields = ["name", "email", "status"]
values = ["'John Doe'", "'john@test.com'", "'active'"]

sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(values)});"
print(f"\n{sql}")
```

::: warning Security
Never build SQL queries through string concatenation in real projects — this is a SQL Injection vulnerability. Use parameterized queries instead.
:::

## Useful Tricks

```python
# Checking if a string is empty
text = ""
if not text:
    print("String is empty")

# String multiplication
separator = "-" * 40
print(separator)  # ----------------------------------------

# Membership check (in)
if "error" in "Connection error occurred".lower():
    print("Error found!")

# Removing specific characters
phone = "+38 (050) 123-45-67"
digits_only = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "").replace("+", "")
print(digits_only)  # 380501234567

# Splitting into lines
multiline = "line1\nline2\nline3"
lines = multiline.splitlines()
print(lines)  # ['line1', 'line2', 'line3']

# Padding / alignment
for item in ["PASSED", "FAILED", "SKIPPED"]:
    print(f"| {item:^10} |")
# |  PASSED   |
# |  FAILED   |
# |  SKIPPED  |
```

## Useful Links

- [Python Docs: str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Docs: string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 498 — f-strings](https://peps.python.org/pep-0498/)
- [String formatting — pyformat.info](https://pyformat.info/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/data-types">← Data Types</a>
  <a href="/python_automation_courses/en/docs/python/collections">Collections →</a>
</div>
