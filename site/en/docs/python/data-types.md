# Data Types

A detailed overview of the main data types in Python — strings, numbers, lists, dictionaries, tuples, and sets.

## Strings (str)

```python
# Creating strings
single = 'Hello'
double = "World"
multiline = """Multiline
text for tests"""

# Escaping
path = "C:\\Users\\test"
raw = r"C:\Users\test"  # raw string — no escaping

# Basic operations
name = "Playwright"
print(len(name))          # 10 — length
print(name[0])            # P — first character
print(name[-1])           # t — last character
print(name[0:4])          # Play — slice
print(name.upper())       # PLAYWRIGHT
print(name.lower())       # playwright
```

### String Methods

```python
text = "  Hello, QA World!  "

text.strip()              # "Hello, QA World!" — remove whitespace
text.lstrip()             # "Hello, QA World!  "
text.rstrip()             # "  Hello, QA World!"
text.split(", ")          # ["  Hello", "QA World!  "]
text.replace("QA", "Dev") # "  Hello, Dev World!  "
text.find("QA")           # 9 — substring index
text.count("l")           # 2 — number of occurrences
text.startswith("  H")    # True
text.endswith("!  ")      # True

# Checks
"hello123".isalnum()      # True — letters and digits
"hello".isalpha()         # True — letters only
"12345".isdigit()         # True — digits only
```

::: tip F-strings for Tests
```python
test_name = "login_test"
status = "passed"
duration = 1.234

# Convenient result formatting
log = f"Test [{test_name}] {status} in {duration:.2f}s"
# "Test [login_test] passed in 1.23s"
```
:::

## Numbers

```python
# Integers (int)
count = 42
big = 1_000_000  # separator for readability
binary = 0b1010  # 10 in binary
hex_num = 0xFF   # 255 in hexadecimal

# Floating-point (float)
price = 19.99
scientific = 1.5e3  # 1500.0

# Math operations
import math

math.ceil(4.2)    # 5 — round up
math.floor(4.8)   # 4 — round down
round(4.567, 2)   # 4.57 — round to 2 decimal places
abs(-10)          # 10 — absolute value
max(1, 5, 3)      # 5
min(1, 5, 3)      # 1
```

## Lists (list)

Lists are mutable ordered collections of elements.

```python
# Creation
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
empty = []

# Access
fruits[0]     # "apple"
fruits[-1]    # "cherry"
fruits[1:3]   # ["banana", "cherry"]

# Modification
fruits.append("orange")       # add to end
fruits.insert(0, "mango")     # insert at index
fruits.extend(["kiwi", "grape"])  # add multiple
fruits.remove("banana")       # remove by value
fruits.pop()                  # remove last
fruits.pop(0)                 # remove by index

# Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()                # [1, 1, 3, 4, 5] — in place
numbers.sort(reverse=True)    # [5, 4, 3, 1, 1]
sorted_nums = sorted(numbers) # new copy

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

::: info Example for QA
```python
# Filtering test results
test_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

# Find all failed tests
failed = [t["name"] for t in test_results if t["status"] == "failed"]
# ["test_signup", "test_profile"]

# Total execution time
total_time = sum(t["duration"] for t in test_results)
# 7.6
```
:::

## Dictionaries (dict)

Dictionaries are unordered collections of key-value pairs.

```python
# Creation
user = {
    "name": "John",
    "age": 30,
    "role": "QA Engineer"
}

# Access
user["name"]              # "John"
user.get("email", "N/A")  # "N/A" — with default value

# Modification
user["email"] = "john@test.com"  # add/update
del user["age"]                   # delete
user.pop("role")                  # delete with return

# Iteration
for key in user:
    print(key)

for key, value in user.items():
    print(f"{key}: {value}")

# Useful methods
user.keys()     # dict_keys(["name", "email"])
user.values()   # dict_values(["John", "john@test.com"])
user.items()    # dict_items([("name", "John"), ...])
user.update({"age": 31, "city": "Kyiv"})

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Tuples (tuple)

Tuples are immutable ordered collections.

```python
# Creation
point = (10, 20)
single = (42,)  # single-element tuple (comma required)
rgb = (255, 128, 0)

# Unpacking
x, y = point
r, g, b = rgb

# Using as a dictionary key (because immutable)
coordinates = {
    (0, 0): "origin",
    (1, 1): "diagonal"
}
```

## Sets (set)

Sets are unordered collections of unique elements.

```python
# Creation
unique = {1, 2, 3, 3, 2}  # {1, 2, 3}
from_list = set([1, 1, 2, 3])

# Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # {1, 2, 3, 4, 5, 6} — union
a & b   # {3, 4} — intersection
a - b   # {1, 2} — difference
a ^ b   # {1, 2, 5, 6} — symmetric difference

# Checking
3 in a  # True
7 in a  # False
```

::: tip Sets for Comparison
```python
# Comparing expected and actual elements
expected_items = {"Login", "Profile", "Settings", "Logout"}
actual_items = {"Login", "Profile", "Logout"}

missing = expected_items - actual_items  # {"Settings"}
extra = actual_items - expected_items    # set()
```
:::

## Useful Links

- [Documentation: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
