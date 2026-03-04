# Python Loops

Loops allow you to execute a block of code repeatedly — one of the most important constructs in programming and QA automation. This page covers all loop types, useful built-in functions, and practical examples for testers.

## for Loop

The `for` loop iterates over elements of any iterable object — a list, string, dictionary, range, and more.

### Iterating Over a List

```python
# Iterating over browsers for testing
browsers = ["chrome", "firefox", "safari", "edge"]

for browser in browsers:
    print(f"Running tests in {browser}")
```

### The range() Function

```python
# range(stop) — from 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) — from start to stop-1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) — with a step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Countdown
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

::: info QA Example: generating test data
```python
# Creating test users
test_users = []
for i in range(1, 6):
    user = {
        "username": f"test_user_{i}",
        "email": f"user{i}@test.com",
        "password": f"Pass{i}!secure"
    }
    test_users.append(user)
    print(f"Created user: {user['username']}")
```
:::

### Iterating Over a String

```python
# Each character is a separate iteration
url = "https"
for char in url:
    print(char)  # h, t, t, p, s

# Counting characters
text = "Hello, World!"
count = 0
for char in text:
    if char.isupper():
        count += 1
print(f"Uppercase letters: {count}")  # 2
```

### Iterating Over a Dictionary

```python
# Iterating over keys (default)
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
    "Accept": "text/html"
}

for key in headers:
    print(key)

# Iterating over values
for value in headers.values():
    print(value)

# Iterating over key-value pairs
for key, value in headers.items():
    print(f"{key}: {value}")
```

::: info QA Example: validating response headers
```python
response_headers = {
    "Content-Type": "application/json",
    "X-Request-Id": "abc-123",
    "Cache-Control": "no-cache"
}

required_headers = ["Content-Type", "X-Request-Id"]

for header in required_headers:
    assert header in response_headers, f"Missing header: {header}"
    print(f"OK {header}: {response_headers[header]}")
```
:::

## while Loop

The `while` loop executes as long as the condition remains `True`.

```python
# Basic while
count = 0
while count < 5:
    print(f"Iteration {count}")
    count += 1  # Don't forget the increment!
```

::: warning Infinite Loop
Always make sure the `while` condition will eventually become `False`. Otherwise, you'll get an infinite loop.
```python
# DANGEROUS — infinite loop!
# while True:
#     print("This will never stop")

# SAFE — with an exit condition
attempts = 0
max_attempts = 10
while attempts < max_attempts:
    attempts += 1
    # perform actions
```
:::

::: info QA Example: retry mechanism for flaky tests
```python
import time

def wait_for_element(locator, timeout=10):
    """Waits for an element to appear with retries."""
    elapsed = 0
    interval = 0.5

    while elapsed < timeout:
        element = find_element(locator)  # hypothetical function
        if element is not None:
            print(f"Element found in {elapsed:.1f}s")
            return element
        time.sleep(interval)
        elapsed += interval

    raise TimeoutError(f"Element '{locator}' not found within {timeout}s")
```
:::

::: info QA Example: polling an API for task completion
```python
import time

def poll_task_status(task_id, max_wait=60):
    """Polls the API until a task completes."""
    start_time = time.time()

    while time.time() - start_time < max_wait:
        response = get_task_status(task_id)  # hypothetical function
        status = response.get("status")

        if status == "completed":
            print(f"Task {task_id} completed!")
            return response
        elif status == "failed":
            raise Exception(f"Task {task_id} failed: {response.get('error')}")

        print(f"Status: {status}, waiting...")
        time.sleep(2)

    raise TimeoutError(f"Task {task_id} did not complete within {max_wait}s")
```
:::

## break, continue, else

### break — Exit the Loop

```python
# Stop the loop when the first match is found
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
# First even number: 8
```

### continue — Skip an Iteration

```python
# Skip unwanted elements
test_results = ["PASSED", "FAILED", "SKIPPED", "PASSED", "FAILED"]

for result in test_results:
    if result == "SKIPPED":
        continue  # skip skipped tests
    print(f"Analyzing: {result}")
```

### else in Loops

The `else` block executes only if the loop completed **without** a `break`.

```python
# else runs because break was never triggered
numbers = [1, 3, 5, 7]

for num in numbers:
    if num % 2 == 0:
        print(f"Found even: {num}")
        break
else:
    print("No even numbers found")
# No even numbers found
```

::: info QA Example: searching for a critical failure
```python
test_results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_checkout", "status": "passed"},
    {"name": "test_payment", "status": "passed"},
]

for test in test_results:
    if test["status"] == "failed":
        print(f"CRITICAL: {test['name']} failed!")
        break
else:
    print("All tests passed successfully!")
# All tests passed successfully!
```
:::

::: tip When to use break/continue?
- `break` — when you found the value you need and there is no point searching further
- `continue` — when you need to skip certain elements but continue the loop
- `else` — when you need to run code only if the loop finished normally (without `break`)
:::

## enumerate() — Index + Element

The `enumerate()` function returns (index, element) pairs during iteration.

```python
# Without enumerate — requires an extra variable
browsers = ["chrome", "firefox", "safari"]
index = 0
for browser in browsers:
    print(f"{index}: {browser}")
    index += 1

# With enumerate — clean and convenient
for index, browser in enumerate(browsers):
    print(f"{index}: {browser}")
# 0: chrome
# 1: firefox
# 2: safari

# Start index from 1
for num, browser in enumerate(browsers, start=1):
    print(f"Browser #{num}: {browser}")
# Browser #1: chrome
# Browser #2: firefox
# Browser #3: safari
```

::: info QA Example: numbering test steps
```python
test_steps = [
    "Open the login page",
    "Enter email",
    "Enter password",
    "Click the 'Sign In' button",
    "Verify the dashboard URL"
]

print("=== Test Scenario: Login ===")
for step_num, step in enumerate(test_steps, start=1):
    print(f"Step {step_num}: {step}")
```
:::

## zip() — Parallel Iteration

The `zip()` function combines multiple iterables into pairs.

```python
# Combining two lists
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score} points")
# Alice: 95 points
# Bob: 87 points
# Charlie: 92 points

# Three lists at once
cities = ["Kyiv", "Lviv", "Odesa"]
temperatures = [25, 22, 28]
conditions = ["sunny", "cloudy", "rain"]

for city, temp, cond in zip(cities, temperatures, conditions):
    print(f"{city}: {temp}C, {cond}")
```

::: warning zip() stops at the shortest
If the lists have different lengths, `zip()` stops at the shortest one.
```python
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

result = list(zip(a, b))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')] — 4 and 5 are lost!

# Use itertools.zip_longest to keep everything
from itertools import zip_longest
result = list(zip_longest(a, b, fillvalue=None))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]
```
:::

::: info QA Example: comparing expected vs actual results
```python
expected = [200, 201, 204, 404]
actual = [200, 201, 500, 404]
endpoints = ["/users", "/users/new", "/users/1", "/unknown"]

for endpoint, exp, act in zip(endpoints, expected, actual):
    status = "PASS" if exp == act else "FAIL"
    print(f"[{status}] {endpoint}: expected {exp}, got {act}")
# [PASS] /users: expected 200, got 200
# [PASS] /users/new: expected 201, got 201
# [FAIL] /users/1: expected 204, got 500
# [PASS] /unknown: expected 404, got 404
```
:::

## List Comprehensions

List comprehension is a compact way to create lists in a single line.

```python
# Regular loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension — same thing, one line
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a condition (filtering)
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# With if/else (transformation)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

::: info QA Example: processing test data
```python
# Filtering failed tests
all_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

failed_tests = [t["name"] for t in all_results if t["status"] == "failed"]
print(failed_tests)  # ['test_signup', 'test_profile']

# Extracting durations from all tests
durations = [t["duration"] for t in all_results]
print(f"Average duration: {sum(durations) / len(durations):.2f}s")

# Generating URLs for testing
base_url = "https://example.com/api"
endpoints = ["/users", "/products", "/orders"]
urls = [f"{base_url}{ep}" for ep in endpoints]
print(urls)
# ['https://example.com/api/users', 'https://example.com/api/products', 'https://example.com/api/orders']
```
:::

::: tip When to use list comprehension?
- **Use it** for simple transformations and filtering
- **Don't use it** when the logic is complex — a regular loop is more readable
- If the comprehension doesn't fit on one line (~80 characters), prefer a loop instead
:::

## Dict Comprehensions

Similar to list comprehensions, but creates dictionaries.

```python
# Creating a dictionary from two lists
keys = ["name", "age", "role"]
values = ["Alice", 30, "QA"]
user = {k: v for k, v in zip(keys, values)}
print(user)  # {'name': 'Alice', 'age': 30, 'role': 'QA'}

# Transforming a dictionary
prices = {"apple": 25, "banana": 15, "cherry": 40}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)  # {'apple': 22.5, 'banana': 13.5, 'cherry': 36.0}

# Filtering a dictionary
expensive = {item: price for item, price in prices.items() if price > 20}
print(expensive)  # {'apple': 25, 'cherry': 40}
```

::: info QA Example: processing API responses
```python
# Converting a list of objects to a dict for fast lookup
users_list = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "user"},
]

users_by_id = {user["id"]: user for user in users_list}
print(users_by_id[2])  # {'id': 2, 'name': 'Bob', 'role': 'user'}

# Counting response status codes
status_codes = [200, 200, 404, 200, 500, 404, 200]
status_counts = {code: status_codes.count(code) for code in set(status_codes)}
print(status_counts)  # {200: 4, 404: 2, 500: 1}
```
:::

## Set Comprehensions

```python
# Unique values with transformation
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Unique domains from emails
emails = ["user@gmail.com", "admin@test.com", "qa@gmail.com", "dev@test.com"]
domains = {email.split("@")[1] for email in emails}
print(domains)  # {'gmail.com', 'test.com'}
```

## Nested Loops

Nested loops are useful for working with matrices, combinations, and complex data structures.

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  ")
    print()  # newline

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

::: info QA Example: cross-browser testing
```python
# Generating test combinations
browsers = ["chrome", "firefox", "safari"]
resolutions = ["1920x1080", "1366x768", "375x667"]
os_list = ["Windows", "macOS"]

test_matrix = []
for browser in browsers:
    for resolution in resolutions:
        for os_name in os_list:
            test_matrix.append({
                "browser": browser,
                "resolution": resolution,
                "os": os_name
            })

print(f"Total test combinations: {len(test_matrix)}")
# Total test combinations: 18

# Same thing with list comprehension
test_matrix = [
    {"browser": b, "resolution": r, "os": o}
    for b in browsers
    for r in resolutions
    for o in os_list
]
```
:::

::: info QA Example: validating all fields in an API response
```python
# Validating nested data structure
api_response = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@test.com"},
        {"id": 2, "name": "Bob", "email": "bob@test.com"},
        {"id": 3, "name": "Charlie", "email": None},  # problem!
    ]
}

required_fields = ["id", "name", "email"]

for user in api_response["users"]:
    for field in required_fields:
        assert field in user, f"Field '{field}' missing in user {user.get('id')}"
        if user[field] is None:
            print(f"WARNING: field '{field}' is None in user {user['id']}")
```
:::

::: warning Nested Loop Complexity
Nested loops increase algorithmic complexity. Two levels gives O(n^2), three gives O(n^3). For large datasets, look for alternative approaches.
```python
# O(n^2) — slow for large lists
for i in range(1000):
    for j in range(1000):
        pass  # 1,000,000 iterations

# Better — use sets for lookups
big_list = list(range(10000))
big_set = set(big_list)  # lookup in set is O(1)
```
:::

## Useful Patterns

### Iteration with Unpacking

```python
# List of tuples
coordinates = [(0, 0), (1, 2), (3, 4)]
for x, y in coordinates:
    print(f"x={x}, y={y}")

# Parameterized test data
test_data = [
    ("admin@test.com", "Admin123!", 200),
    ("user@test.com", "User456!", 200),
    ("invalid@test.com", "wrong", 401),
]

for email, password, expected_status in test_data:
    print(f"Login {email} -> expecting {expected_status}")
```

### Walrus Operator (:=) in Loops (Python 3.8+)

```python
# Reading data until a condition is met
import random

# Without walrus
while True:
    value = random.randint(1, 10)
    if value == 7:
        break
    print(f"Got: {value}")

# With walrus operator
while (value := random.randint(1, 10)) != 7:
    print(f"Got: {value}")
print("Found 7!")
```

### Retry with Exponential Backoff

::: info QA Example: retrying flaky requests
```python
import time

def retry_request(url, max_retries=5):
    """Retries a request with exponential backoff."""
    for attempt in range(max_retries):
        try:
            response = make_request(url)  # hypothetical function
            if response.status_code == 200:
                return response
        except ConnectionError as e:
            wait_time = 2 ** attempt  # 1, 2, 4, 8, 16 seconds
            print(f"Attempt {attempt + 1}/{max_retries} failed. "
                  f"Waiting {wait_time}s...")
            time.sleep(wait_time)

    raise Exception(f"All {max_retries} attempts failed for {url}")
```
:::

## Common Mistakes

### Modifying a List While Iterating

```python
# WRONG — modifying the list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Unpredictable behavior!

# CORRECT — create a new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # [1, 3, 5]

# OR — iterate over a copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # [:] creates a copy
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3, 5]
```

### Forgetting the Increment in while

```python
# WRONG — infinite loop
# i = 0
# while i < 5:
#     print(i)  # i never changes!

# CORRECT
i = 0
while i < 5:
    print(i)
    i += 1
```

### Not Using enumerate

```python
# WRONG — manual counter
items = ["a", "b", "c"]
i = 0
for item in items:
    print(f"{i}: {item}")
    i += 1

# CORRECT — enumerate
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

::: tip Rule
If you need the index of an element during iteration, always use `enumerate()` instead of a manual counter.
:::

## Useful Links

- [Official Docs: for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Official Docs: range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Official Docs: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 274 — Dict Comprehensions](https://peps.python.org/pep-0274/)
- [Real Python — Python for Loops](https://realpython.com/python-for-loop/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/collections">← Collections</a>
  <a href="/python_automation_courses/en/docs/python/functions">Functions →</a>
</div>
