# Collections

Collections in Python are data structures for storing and organizing multiple elements. They are the foundation of any test automation: from storing test data to managing configurations.

## Lists

A list is an ordered, mutable collection of elements. It is the most commonly used data structure in Python.

### Creating Lists

```python
# Empty list
empty = []
empty2 = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", True, 3.14, None]

# List from another list (copy)
original = [1, 2, 3]
copy = list(original)

# List from range
numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Indexing and Slicing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing (starts at 0)
fruits[0]      # "apple"
fruits[2]      # "cherry"
fruits[-1]     # "elderberry" — last element
fruits[-2]     # "date" — second to last

# Slicing [start:stop:step]
fruits[1:3]    # ["banana", "cherry"] — from 1 to 3 (excluding 3)
fruits[:3]     # ["apple", "banana", "cherry"] — first 3
fruits[2:]     # ["cherry", "date", "elderberry"] — from 2 to end
fruits[::2]    # ["apple", "cherry", "elderberry"] — every other
fruits[::-1]   # ["elderberry", "date", "cherry", "banana", "apple"] — reversed
```

::: tip Remember
Indexing starts at `0`. Negative indices count from the end: `-1` is the last element, `-2` is the second to last.
:::

### List Methods

```python
# Adding elements
items = [1, 2, 3]
items.append(4)          # [1, 2, 3, 4] — adds to the end
items.insert(0, 0)       # [0, 1, 2, 3, 4] — inserts at position
items.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6] — adds multiple elements

# Removing elements
items.remove(0)          # [1, 2, 3, 4, 5, 6] — removes first occurrence
last = items.pop()       # last = 6, items = [1, 2, 3, 4, 5]
second = items.pop(1)    # second = 2, items = [1, 3, 4, 5]
del items[0]             # items = [3, 4, 5]

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()           # [1, 1, 2, 3, 4, 5, 6, 9] — in place
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1] — descending
sorted_nums = sorted(numbers)  # Returns new list, original unchanged

# Reversing
numbers.reverse()        # Reverses list in place

# Searching and counting
numbers = [1, 2, 3, 2, 1]
numbers.index(2)         # 1 — index of first occurrence
numbers.count(2)         # 2 — number of occurrences
3 in numbers             # True — membership check
len(numbers)             # 5 — length of the list
```

::: warning Pay Attention
`sort()` modifies the list in place and returns `None`. `sorted()` returns a new sorted list. Do not write `items = items.sort()` — it will assign `None`!
:::

### List Comprehensions

```python
# Basic syntax: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# With condition (filtering)
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]  # ["ALICE", "BOB", "CHARLIE"]

# With conditional expression
labels = ["pass" if x >= 50 else "fail" for x in [80, 30, 65, 45, 90]]
# ["pass", "fail", "pass", "fail", "pass"]
```

::: info QA Example: filtering test results
```python
# Test results
test_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

# Only failed tests
failed = [t["name"] for t in test_results if t["status"] == "failed"]
# ["test_signup", "test_profile"]

# Slow tests (> 2 seconds)
slow_tests = [t for t in test_results if t["duration"] > 2.0]
```
:::

## Tuples

A tuple is an ordered, **immutable** collection. Once created, elements cannot be added, removed, or changed.

### Creating Tuples

```python
# Creating a tuple
coordinates = (10, 20)
single = (42,)           # Single-element tuple — comma is required!
not_tuple = (42)          # This is just a number in parentheses, not a tuple!
from_list = tuple([1, 2, 3])

# Without parentheses (packing)
point = 10, 20, 30        # Also a tuple: (10, 20, 30)
```

### Tuple Unpacking

```python
# Basic unpacking
x, y = (10, 20)
print(x)  # 10
print(y)  # 20

# Unpacking with * (star)
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

head, *middle, tail = (1, 2, 3, 4, 5)
# head = 1, middle = [2, 3, 4], tail = 5

# Swapping variables
a, b = 1, 2
a, b = b, a  # a = 2, b = 1
```

### When to Use Tuples vs Lists?

| Tuple | List |
|-------|------|
| Data will not change | Data may change |
| Coordinates, RGB colors | Collection of tests, results |
| Dictionary keys | Buffer, queue, stack |
| Returning multiple values from a function | Dataset for processing |
| Slightly faster and uses less memory | More methods available |

::: info QA Example: returning multiple values
```python
def run_test(test_name):
    """Runs a test and returns the result."""
    # ... test execution logic ...
    status = "passed"
    duration = 2.35
    error_message = None
    return status, duration, error_message  # Returns a tuple

# Unpacking the result
status, duration, error = run_test("test_login")
print(f"[{status}] {duration:.2f}s")
```
:::

## Dictionaries

A dictionary is a collection of "key: value" pairs. Keys must be immutable (str, int, tuple) and unique.

### Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty2 = dict()

# Dictionary with data
user = {
    "name": "John",
    "age": 30,
    "is_active": True
}

# Creating from pairs
pairs = dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}

# Creating from keyword arguments
config = dict(timeout=30, retries=3, base_url="https://example.com")
```

### Accessing Elements

```python
user = {"name": "Alice", "age": 25, "role": "QA"}

# Access by key
user["name"]         # "Alice"
# user["email"]      # KeyError! — key does not exist

# Safe access with get()
user.get("name")           # "Alice"
user.get("email")          # None — key missing, no error
user.get("email", "N/A")   # "N/A" — default value

# Checking if key exists
"name" in user       # True
"email" in user      # False
```

::: tip Recommendation
Always use `.get()` when you are not sure the key exists. This prevents `KeyError` in tests.
:::

### Dictionary Methods

```python
user = {"name": "Alice", "age": 25}

# Getting keys, values, pairs
user.keys()      # dict_keys(["name", "age"])
user.values()    # dict_values(["Alice", 25])
user.items()     # dict_items([("name", "Alice"), ("age", 25)])

# Adding and updating
user["email"] = "alice@test.com"    # Adds a new pair
user["age"] = 26                    # Updates existing value
user.update({"role": "QA", "age": 27})  # Updates multiple pairs

# Removing
email = user.pop("email")           # Removes and returns value
user.pop("phone", None)             # Safe removal (no KeyError)
del user["role"]                     # Removes pair

# Iteration
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions

```python
# Basic syntax: {key: value for item in iterable}
squares = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Inverting a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

::: info QA Example: test environment configuration
```python
# Configuration as a dictionary
config = {
    "base_url": "https://staging.example.com",
    "timeout": 30,
    "browser": "chromium",
    "headless": True,
    "retries": 3,
}

# Accessing configuration
base_url = config.get("base_url")
timeout = config.get("timeout", 10)  # 10 as default value

# Updating configuration for different environments
production_overrides = {"base_url": "https://example.com", "headless": False}
config.update(production_overrides)

# HTTP headers as a dictionary
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
    "X-Request-ID": "test-001",
}
```
:::

## Sets

A set is an unordered collection of **unique** elements. Sets do not support indexing.

### Creating Sets

```python
# Creating a set
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 2, 1}    # {1, 2, 3} — duplicates are removed
empty_set = set()              # Empty set (not {}!)
from_list = set([1, 2, 2, 3]) # {1, 2, 3}
```

::: warning Caution
`{}` creates an empty **dictionary**, not a set! Use `set()` for an empty set.
:::

### Set Methods

```python
colors = {"red", "green", "blue"}

# Adding
colors.add("yellow")        # {"red", "green", "blue", "yellow"}
colors.add("red")           # No change — element already exists

# Removing
colors.remove("yellow")     # Removes element (KeyError if missing)
colors.discard("purple")    # Removes element (no error if missing)
removed = colors.pop()      # Removes and returns an arbitrary element
```

### Set Operations

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — all elements from both sets
a | b              # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)         # same

# Intersection — common elements
a & b              # {4, 5}
a.intersection(b)  # same

# Difference — elements in a that are not in b
a - b              # {1, 2, 3}
a.difference(b)    # same

# Symmetric difference — elements in only one of the sets
a ^ b              # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)  # same

# Subset and superset
{1, 2}.issubset({1, 2, 3})      # True — {1,2} is a subset
{1, 2, 3}.issuperset({1, 2})    # True — {1,2,3} is a superset
```

::: info QA Example: comparing test coverage
```python
# Tests covering different modules
smoke_tests = {"test_login", "test_home", "test_search"}
regression_tests = {"test_login", "test_home", "test_search", "test_cart", "test_checkout"}
flaky_tests = {"test_search", "test_cart"}

# Which tests are in regression but not in smoke?
new_in_regression = regression_tests - smoke_tests
# {"test_cart", "test_checkout"}

# Stable regression tests (excluding flaky)
stable_tests = regression_tests - flaky_tests
# {"test_login", "test_home", "test_checkout"}

# Unique test case IDs (no duplicates)
all_test_ids = [1, 2, 3, 2, 4, 3, 5]
unique_ids = list(set(all_test_ids))  # [1, 2, 3, 4, 5]
```
:::

## Nested Collections

Collections can be nested inside each other to create complex data structures.

```python
# List of dictionaries
users = [
    {"name": "Alice", "role": "QA"},
    {"name": "Bob", "role": "Dev"},
    {"name": "Charlie", "role": "QA"},
]

# Accessing nested data
users[0]["name"]  # "Alice"

# Dictionary with lists
test_suite = {
    "smoke": ["test_login", "test_home"],
    "regression": ["test_login", "test_home", "test_cart", "test_checkout"],
    "performance": ["test_load", "test_stress"],
}

# Dictionary of dictionaries
environments = {
    "dev": {"url": "https://dev.example.com", "db": "dev_db"},
    "staging": {"url": "https://staging.example.com", "db": "staging_db"},
    "prod": {"url": "https://example.com", "db": "prod_db"},
}

# Access
staging_url = environments["staging"]["url"]
# "https://staging.example.com"
```

::: info QA Example: storing and analyzing test results
```python
# Complete test report structure
test_report = {
    "suite": "Regression",
    "total": 4,
    "results": [
        {
            "name": "test_login_valid",
            "status": "passed",
            "duration": 1.2,
            "tags": ["smoke", "auth"],
        },
        {
            "name": "test_login_invalid",
            "status": "passed",
            "duration": 0.9,
            "tags": ["auth"],
        },
        {
            "name": "test_add_to_cart",
            "status": "failed",
            "duration": 3.1,
            "tags": ["cart", "regression"],
            "error": "Element not found: #add-btn",
        },
        {
            "name": "test_checkout",
            "status": "skipped",
            "duration": 0,
            "tags": ["cart", "checkout"],
        },
    ],
}

# Analyzing results
results = test_report["results"]

passed = [r["name"] for r in results if r["status"] == "passed"]
failed = [r["name"] for r in results if r["status"] == "failed"]

total_duration = sum(r["duration"] for r in results)
pass_rate = len(passed) / test_report["total"] * 100

print(f"Pass rate: {pass_rate:.1f}%")          # Pass rate: 50.0%
print(f"Total duration: {total_duration:.1f}s") # Total duration: 5.2s
print(f"Failed: {failed}")                      # Failed: ["test_add_to_cart"]

# Find all unique tags
all_tags = set()
for r in results:
    all_tags.update(r["tags"])
# {"smoke", "auth", "cart", "regression", "checkout"}
```
:::

## Useful Functions for Collections

```python
numbers = [5, 2, 8, 1, 9, 3]

len(numbers)      # 6 — number of elements
min(numbers)      # 1 — minimum value
max(numbers)      # 9 — maximum value
sum(numbers)      # 28 — sum of elements
sorted(numbers)   # [1, 2, 3, 5, 8, 9] — new sorted list

# enumerate — iteration with index
for i, num in enumerate(numbers):
    print(f"{i}: {num}")

# zip — combining multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# any / all — condition checks
numbers = [2, 4, 6, 8]
all(x % 2 == 0 for x in numbers)  # True — all are even
any(x > 5 for x in numbers)       # True — at least one > 5
```

## Useful Links

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Collections Module](https://docs.python.org/3/library/collections.html)
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/strings">← Strings</a>
  <a href="/python_automation_courses/en/docs/python/loops">Loops →</a>
</div>
