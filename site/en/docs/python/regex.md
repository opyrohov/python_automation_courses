# Regular Expressions

Regular expressions (regex) are a powerful tool for searching, validating, and processing text data. In QA automation, regular expressions are used for form validation, log parsing, API response verification, and much more.

## The `re` Module

Python has a built-in `re` module for working with regular expressions.

```python
import re

# Simple search
result = re.search(r"test", "This is a test string")
if result:
    print(result.group())  # test
```

::: tip Raw Strings
Always use the `r` prefix before a regex pattern. This prevents double interpretation of backslashes.
```python
# Correct — raw string
pattern = r"\d+"

# Incorrect — without r you need double backslash
pattern = "\\d+"
```
:::

## Basic Patterns

### Literal Characters

Literal characters match themselves.

```python
import re

text = "QA Engineer works with automation testing"

# Search for a specific word
result = re.search(r"automation", text)
print(result.group())  # automation
```

### Metacharacters

| Metacharacter | Description | Example |
|:---:|---|---|
| `.` | Any character (except `\n`) | `a.c` -> `abc`, `a1c` |
| `^` | Start of string | `^Hello` |
| `$` | End of string | `world$` |
| `*` | 0 or more repetitions | `ab*c` -> `ac`, `abc`, `abbc` |
| `+` | 1 or more repetitions | `ab+c` -> `abc`, `abbc` |
| `?` | 0 or 1 repetition | `colou?r` -> `color`, `colour` |
| `\|` | Logical OR | `cat\|dog` |
| `()` | Grouping | `(ab)+` -> `ab`, `abab` |
| `[]` | Character set | `[aeiou]` — vowels |
| `{}` | Repetition count | `a{2,4}` -> `aa`, `aaa`, `aaaa` |
| `\` | Escaping | `\.` — literal dot |

```python
import re

# Metacharacter . — any character
print(re.findall(r"t.st", "test tast tost t1st"))  # ['test', 'tast', 'tost', 't1st']

# ^ and $ — start and end of string
print(re.search(r"^Error", "Error: file not found"))   # Match
print(re.search(r"^Error", "No Error here"))            # None

# | — logical OR
print(re.findall(r"pass|fail", "test pass, test fail"))  # ['pass', 'fail']
```

## Character Classes

### Built-in Classes

| Class | Description | Equivalent |
|:---:|---|---|
| `\d` | Digit | `[0-9]` |
| `\D` | Non-digit | `[^0-9]` |
| `\w` | Letter, digit, or `_` | `[a-zA-Z0-9_]` |
| `\W` | Non-letter, non-digit, non-`_` | `[^a-zA-Z0-9_]` |
| `\s` | Whitespace character | `[ \t\n\r\f\v]` |
| `\S` | Non-whitespace character | `[^ \t\n\r\f\v]` |
| `\b` | Word boundary | — |
| `\B` | Non-word boundary | — |

```python
import re

text = "Order #12345 created on 2024-01-15 at 14:30"

# \d — digits
print(re.findall(r"\d+", text))  # ['12345', '2024', '01', '15', '14', '30']

# \w — words and numbers
print(re.findall(r"\w+", text))  # ['Order', '12345', 'created', 'on', '2024', '01', '15', 'at', '14', '30']

# \s — whitespace characters
parts = re.split(r"\s+", "test   data   here")
print(parts)  # ['test', 'data', 'here']

# \b — word boundary
text = "testing test tested"
print(re.findall(r"\btest\b", text))  # ['test'] — exact word only
```

### Custom Character Classes

```python
import re

# [abc] — one of a, b, or c
print(re.findall(r"[aeiou]", "hello world"))  # ['e', 'o', 'o']

# [a-z] — range
print(re.findall(r"[a-zA-Z]+", "test123data"))  # ['test', 'data']

# [^abc] — any character EXCEPT a, b, c
print(re.findall(r"[^0-9]+", "abc123def456"))  # ['abc', 'def']
```

## Functions of the `re` Module

### `re.search()` — Find the First Match

```python
import re

text = "Error 404: Page not found"

match = re.search(r"\d+", text)
if match:
    print(match.group())   # 404
    print(match.start())   # 6
    print(match.end())     # 9
    print(match.span())    # (6, 9)
```

### `re.match()` — Match at the Start of String

```python
import re

# match() checks only the beginning of the string
print(re.match(r"\d+", "123abc"))   # Match — starts with digits
print(re.match(r"\d+", "abc123"))   # None — doesn't start with digits
```

::: warning search() vs match()
`re.match()` looks for a match only at the **beginning** of the string. Use `re.search()` to find a match anywhere in the string.
```python
text = "Status: 200 OK"
re.match(r"\d+", text)    # None — string starts with "Status"
re.search(r"\d+", text)   # Match — finds "200"
```
:::

### `re.findall()` — Find All Matches

```python
import re

text = "Prices: $10.99, $25.50, $7.00"

# Find all prices
prices = re.findall(r"\$[\d.]+", text)
print(prices)  # ['$10.99', '$25.50', '$7.00']

# With groups — returns group contents
prices = re.findall(r"\$([\d.]+)", text)
print(prices)  # ['10.99', '25.50', '7.00']
```

### `re.finditer()` — Match Iterator

```python
import re

text = "Error at line 10, Error at line 25, Error at line 42"

for match in re.finditer(r"line (\d+)", text):
    print(f"Found at position {match.start()}: line {match.group(1)}")
# Found at position 9: line 10
# Found at position 25: line 25
# Found at position 41: line 42
```

### `re.sub()` — Substitution

```python
import re

# Simple replacement
text = "Phone: 123-456-7890"
cleaned = re.sub(r"-", "", text)
print(cleaned)  # Phone: 1234567890

# Replacement with a function
def censor_email(match):
    email = match.group()
    name, domain = email.split("@")
    return f"{name[0]}***@{domain}"

text = "Contacts: john@example.com, admin@test.com"
result = re.sub(r"[\w.]+@[\w.]+", censor_email, text)
print(result)  # Contacts: j***@example.com, a***@test.com
```

### `re.split()` — Split a String

```python
import re

# Split by multiple delimiters
text = "apple;banana,cherry orange|grape"
fruits = re.split(r"[;,\s|]+", text)
print(fruits)  # ['apple', 'banana', 'cherry', 'orange', 'grape']

# Limit the number of splits
text = "one:two:three:four:five"
print(re.split(r":", text, maxsplit=2))  # ['one', 'two', 'three:four:five']
```

### `re.compile()` — Compile a Pattern

```python
import re

# Compile for repeated use
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")

texts = [
    "Contact: user@example.com",
    "No email here",
    "Send to admin@test.org please",
]

for text in texts:
    match = email_pattern.search(text)
    if match:
        print(f"Found: {match.group()}")
```

::: tip When to Use compile()?
Use `re.compile()` when a single pattern is used many times (e.g., in a loop). This improves performance since the pattern is compiled only once.
:::

## Groups and Capturing

### Simple Groups `()`

```python
import re

text = "2024-01-15"

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    print(match.group())    # 2024-01-15 — full match
    print(match.group(1))   # 2024 — first group
    print(match.group(2))   # 01 — second group
    print(match.group(3))   # 15 — third group
    print(match.groups())   # ('2024', '01', '15')
```

### Named Groups `(?P<name>...)`

```python
import re

text = "User: John Doe, Age: 30, Email: john@example.com"

pattern = r"User: (?P<name>[\w ]+), Age: (?P<age>\d+), Email: (?P<email>[\w.]+@[\w.]+)"
match = re.search(pattern, text)

if match:
    print(match.group("name"))    # John Doe
    print(match.group("age"))     # 30
    print(match.group("email"))   # john@example.com
    print(match.groupdict())      # {'name': 'John Doe', 'age': '30', 'email': 'john@example.com'}
```

### Non-Capturing Groups `(?:...)`

```python
import re

# Non-capturing group — for grouping without saving
text = "http://example.com https://example.org"

# (?:...) — won't appear in results
urls = re.findall(r"(?:https?://)(\S+)", text)
print(urls)  # ['example.com', 'example.org']
```

## Quantifiers

| Quantifier | Description |
|:---:|---|
| `*` | 0 or more (greedy) |
| `+` | 1 or more (greedy) |
| `?` | 0 or 1 |
| `{n}` | Exactly n times |
| `{n,}` | n or more times |
| `{n,m}` | From n to m times |
| `*?` | 0 or more (lazy) |
| `+?` | 1 or more (lazy) |

```python
import re

# Greedy vs Lazy
html = "<b>bold</b> and <i>italic</i>"

# Greedy — captures maximum
print(re.findall(r"<.*>", html))    # ['<b>bold</b> and <i>italic</i>']

# Lazy — captures minimum
print(re.findall(r"<.*?>", html))   # ['<b>', '</b>', '<i>', '</i>']
```

::: warning Greedy vs Lazy
By default, quantifiers `*`, `+`, `?` are **greedy** — they capture as many characters as possible. Add `?` after a quantifier to make it **lazy**.
:::

```python
import re

# {n} — exactly n times
print(re.findall(r"\d{3}", "12 123 1234 12345"))  # ['123', '123', '123']

# {n,m} — from n to m
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))  # ['12', '123', '1234', '1234']
```

## Flags

### `re.IGNORECASE` (re.I)

```python
import re

text = "Error: CONNECTION REFUSED, error: timeout, ERROR: denied"

# Without flag — case-sensitive
print(re.findall(r"error", text))               # ['error']

# With re.IGNORECASE — case-insensitive
print(re.findall(r"error", text, re.IGNORECASE)) # ['Error', 'error', 'ERROR']
```

### `re.MULTILINE` (re.M)

```python
import re

log = """ERROR: Connection failed
INFO: Retry attempt 1
ERROR: Timeout exceeded
INFO: Retry attempt 2"""

# Without MULTILINE — ^ matches only the start of the entire text
print(re.findall(r"^ERROR.*", log))               # ['ERROR: Connection failed']

# With MULTILINE — ^ matches the start of each line
print(re.findall(r"^ERROR.*", log, re.MULTILINE))  # ['ERROR: Connection failed', 'ERROR: Timeout exceeded']
```

### `re.DOTALL` (re.S)

```python
import re

html = """<div>
  <p>Hello World</p>
</div>"""

# Without DOTALL — . does not match \n
print(re.search(r"<div>.*</div>", html))             # None

# With DOTALL — . matches \n
print(re.search(r"<div>.*</div>", html, re.DOTALL))  # Match
```

### Combining Flags

```python
import re

text = """name: John
Name: Jane
NAME: Admin"""

# Combine with |
matches = re.findall(r"^name: \w+", text, re.IGNORECASE | re.MULTILINE)
print(matches)  # ['name: John', 'Name: Jane', 'NAME: Admin']
```

## Common Patterns

### Email

```python
import re

email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

emails = [
    "user@example.com",       # Valid
    "admin+tag@test.org",     # Valid
    "invalid@",               # Invalid
    "no-at-sign.com",         # Invalid
    "first.last@company.co",  # Valid
]

for email in emails:
    if email_pattern.fullmatch(email):
        print(f"  Valid: {email}")
    else:
        print(f"  Invalid: {email}")
```

### URL

```python
import re

url_pattern = re.compile(
    r"https?://"
    r"(?:[\w-]+\.)+[\w-]+"
    r"(?:/[\w./?%&=~#-]*)?"
)

text = "Visit https://example.com/page?id=1 or http://test.org"
urls = url_pattern.findall(text)
print(urls)  # ['https://example.com/page?id=1', 'http://test.org']
```

### Phone Number

```python
import re

phone_pattern = re.compile(
    r"(?:\+?\d{1,3}[-.\s]?)?"   # Country code
    r"(?:\(?\d{2,3}\)?[-.\s]?)" # Area code
    r"\d{3}[-.\s]?\d{2}[-.\s]?\d{2}"
)

phones = [
    "+380-67-123-45-67",
    "(067) 123 45 67",
    "+38(067)1234567",
    "067-123-45-67",
]

for phone in phones:
    match = phone_pattern.search(phone)
    if match:
        print(f"Found: {match.group()}")
```

### IP Address

```python
import re

ip_pattern = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}"
    r"(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
)

text = "Server 192.168.1.1 responded, but 10.0.0.255 is unreachable. Invalid: 999.999.999.999"
ips = ip_pattern.findall(text)
print(ips)  # ['192.168.1.1', '10.0.0.255']
```

## QA Examples

### Form Data Validation

```python
import re

def validate_registration_form(data: dict) -> dict:
    """Validate registration form data."""
    errors = {}

    # Email validation
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data.get("email", "")):
        errors["email"] = "Invalid email format"

    # Password validation: minimum 8 characters, upper/lower case, digits
    password = data.get("password", "")
    if len(password) < 8:
        errors["password"] = "Password must be at least 8 characters"
    elif not re.search(r"[A-Z]", password):
        errors["password"] = "Password must contain uppercase letters"
    elif not re.search(r"[a-z]", password):
        errors["password"] = "Password must contain lowercase letters"
    elif not re.search(r"\d", password):
        errors["password"] = "Password must contain digits"

    # Phone validation
    phone = data.get("phone", "")
    if not re.match(r"^\+?\d{10,15}$", re.sub(r"[-.\s()\u2013]", "", phone)):
        errors["phone"] = "Invalid phone number format"

    return errors

# Test
form_data = {
    "email": "user@example.com",
    "password": "SecurePass123",
    "phone": "+380-67-123-45-67",
}

errors = validate_registration_form(form_data)
if not errors:
    print("Form is valid!")
else:
    print(f"Errors: {errors}")
```

### Parsing Log Files

```python
import re
from collections import Counter

log_text = """
2024-01-15 10:23:45 [ERROR] Connection timeout to database server db-01
2024-01-15 10:23:46 [INFO] Retrying connection (attempt 1/3)
2024-01-15 10:23:50 [ERROR] Authentication failed for user admin
2024-01-15 10:24:01 [WARNING] High memory usage: 85%
2024-01-15 10:24:15 [INFO] Connection established to db-02
2024-01-15 10:24:20 [ERROR] Query timeout after 30s: SELECT * FROM users
"""

# Pattern for parsing log lines
log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"\[(?P<level>\w+)\]\s+"
    r"(?P<message>.+)"
)

# Parse each line
entries = []
for match in log_pattern.finditer(log_text):
    entries.append(match.groupdict())

# Count by log level
levels = Counter(entry["level"] for entry in entries)
print(f"Log levels: {dict(levels)}")
# Log levels: {'ERROR': 3, 'INFO': 2, 'WARNING': 1}

# Filter errors only
errors = [e for e in entries if e["level"] == "ERROR"]
for error in errors:
    print(f"[{error['time']}] {error['message']}")
```

### Extracting Data from API Responses

```python
import re

# Parsing HTML response to extract data
html_response = """
<table id="users">
    <tr><td>John Doe</td><td>john@example.com</td><td>Admin</td></tr>
    <tr><td>Jane Smith</td><td>jane@test.org</td><td>User</td></tr>
    <tr><td>Bob Wilson</td><td>bob@company.com</td><td>Moderator</td></tr>
</table>
"""

# Extract table rows
row_pattern = re.compile(r"<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td></tr>")
users = row_pattern.findall(html_response)

for name, email, role in users:
    print(f"Name: {name}, Email: {email}, Role: {role}")
# Name: John Doe, Email: john@example.com, Role: Admin
# Name: Jane Smith, Email: jane@test.org, Role: User
# Name: Bob Wilson, Email: bob@company.com, Role: Moderator
```

::: info QA Example: API Response Validation
```python
import re
import json

def validate_api_response(response_text: str) -> dict:
    """Validate the structure of a JSON API response."""
    results = {"valid": True, "errors": []}

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        results["valid"] = False
        results["errors"].append("Invalid JSON")
        return results

    # Check ID format (UUID v4)
    uuid_pattern = re.compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        re.IGNORECASE,
    )

    if "id" in data and not uuid_pattern.match(str(data["id"])):
        results["valid"] = False
        results["errors"].append(f"Invalid UUID: {data['id']}")

    # Check ISO 8601 date format
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
    for field in ["created_at", "updated_at"]:
        if field in data and not date_pattern.match(str(data[field])):
            results["valid"] = False
            results["errors"].append(f"Invalid date format in {field}")

    return results
```
:::

### Validating Test Data in Pytest

```python
import re
import pytest

class TestDataValidation:
    """Tests for data validation using regular expressions."""

    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("admin+tag@test.org", True),
        ("first.last@company.co.uk", True),
        ("invalid@", False),
        ("@example.com", False),
        ("no-at-sign", False),
        ("spaces in@email.com", False),
    ])
    def test_email_validation(self, email, expected):
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        assert bool(pattern.match(email)) == expected, f"Email '{email}' validation failed"

    @pytest.mark.parametrize("password,is_strong", [
        ("SecurePass1", True),
        ("weakpass", False),      # No uppercase or digits
        ("ALLCAPS123", False),    # No lowercase
        ("Short1A", False),       # Less than 8 characters
        ("GoodPassword99", True),
    ])
    def test_password_strength(self, password, is_strong):
        checks = [
            len(password) >= 8,
            bool(re.search(r"[A-Z]", password)),
            bool(re.search(r"[a-z]", password)),
            bool(re.search(r"\d", password)),
        ]
        assert all(checks) == is_strong
```

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/error-handling">← Error Handling</a>
  <a href="/python_automation_courses/en/docs/python/api-requests">Working with API →</a>
</div>
