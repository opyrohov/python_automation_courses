# Python Basics

Basic Python language syntax — variables, operators, input/output. This page covers everything you need to get started with Python in QA automation.

## Comments

Comments help explain code to other developers (and to yourself a month later).

```python
# Single-line comment — starts with #

# Multiple single-line comments in a row
# describe complex logic
# step by step

"""
Multi-line comment (docstring).
Used for documenting modules,
classes, and functions.
"""

def login(username, password):
    """Authenticates a user in the system.

    Args:
        username: User name
        password: Password

    Returns:
        True if authentication is successful
    """
    pass
```

::: tip When to comment?
- Explain **why**, not **what** — the code already shows what happens
- Document functions with docstrings
- Don't comment obvious code: `x = x + 1  # increment x by 1` — unnecessary
:::

## Variables

Variables in Python do not require type declaration — the interpreter determines the type automatically.

```python
# Creating variables
name = "QA Engineer"
age = 25
salary = 5500.50
is_active = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0
```

::: tip Variable Naming
Use `snake_case` for variables and functions — this is the PEP 8 standard.
```python
# Correct
user_name = "John"
max_retry_count = 3

# Incorrect
userName = "John"
MaxRetryCount = 3
```
:::

::: info QA Example: test data in variables
```python
# Storing test data
base_url = "https://example.com"
api_endpoint = f"{base_url}/api/v1/users"
admin_login = "admin@test.com"
admin_password = "Test123!"
timeout_seconds = 30
max_retries = 3

# Expected values for assertions
expected_status = 200
expected_title = "Dashboard"
```
:::

## Data Types

| Type | Example | Description | Mutable |
|------|---------|-------------|---------|
| `str` | `"Hello"` | Text string | No |
| `int` | `42` | Integer | No |
| `float` | `3.14` | Floating-point number | No |
| `bool` | `True` / `False` | Boolean | No |
| `NoneType` | `None` | Absence of value | No |
| `list` | `[1, 2, 3]` | List (ordered) | **Yes** |
| `tuple` | `(1, 2, 3)` | Tuple (ordered) | No |
| `set` | `{1, 2, 3}` | Set (unique values) | **Yes** |
| `dict` | `{"key": "val"}` | Dictionary (key-value) | **Yes** |

```python
# Type checking
name = "Test"
print(type(name))  # <class 'str'>
```

::: warning Mutable vs Immutable
**Mutable** objects can be changed in place. **Immutable** — cannot; any modification creates a new object.
```python
# Mutable — list is modified in place
items = [1, 2, 3]
items.append(4)      # items = [1, 2, 3, 4] — same object

# Immutable — str creates a new object
name = "Hello"
name_upper = name.upper()  # "HELLO" — new string, name unchanged
```
:::

## Operators

### Arithmetic Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division (float) | `10 / 3` | `3.33...` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Exponentiation | `10 ** 3` | `1000` |

### Comparison Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equals | `5 == 10` | `False` |
| `!=` | Not equals | `5 != 10` | `True` |
| `>` | Greater than | `5 > 10` | `False` |
| `<` | Less than | `5 < 10` | `True` |
| `>=` | Greater or equal | `5 >= 10` | `False` |
| `<=` | Less or equal | `5 <= 10` | `True` |

### Logical Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Logical AND — both True | `True and False` | `False` |
| `or` | Logical OR — at least one True | `True or False` | `True` |
| `not` | Logical NOT — inverts | `not True` | `False` |

::: info Practical Example for QA
```python
# Checking conditions in tests
is_visible = True
is_enabled = True
has_text = False

# Is the element ready to click?
can_click = is_visible and is_enabled  # True

# Is there at least one issue?
has_issue = not is_visible or not is_enabled or not has_text  # True
```
:::

## Input and Output

```python
# Output
print("Hello, World!")
print("Name:", "QA", "Engineer")  # Name: QA Engineer
print(f"Age: {age}")              # f-string formatting

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # conversion to number
```

## Type Conversion

```python
# Type conversion
num_str = "42"
num_int = int(num_str)      # str → int
num_float = float(num_str)  # str → float
back_str = str(num_int)     # int → str
is_true = bool(1)           # int → bool (True)
is_false = bool(0)          # int → bool (False)

# Type checking
isinstance(42, int)         # True
isinstance("hello", str)    # True
isinstance(True, bool)      # True
```

::: details What converts to False?
These values are considered "falsy" when converted to `bool`:
```python
bool(0)        # False — zero
bool(0.0)      # False — zero float
bool("")       # False — empty string
bool([])       # False — empty list
bool({})       # False — empty dict
bool(None)     # False — None

# Everything else is True
bool(1)        # True
bool("text")   # True
bool([1, 2])   # True
```
:::

## String Formatting

```python
name = "QA Engineer"
experience = 3

# f-string (recommended)
print(f"I am a {name} with {experience} years of experience")

# format()
print("I am a {} with {} years of experience".format(name, experience))

# % operator (legacy)
print("I am a %s with %d years of experience" % (name, experience))

# Number formatting
price = 1234.5678
print(f"Price: {price:.2f}")     # Price: 1234.57
print(f"Percentage: {0.856:.1%}") # Percentage: 85.6%
print(f"Number: {42:05d}")       # Number: 00042
```

::: info QA Example: generating messages
```python
# Logging in tests
test_name = "test_login_valid_user"
status = "PASSED"
duration = 2.347
print(f"[{status}] {test_name} — {duration:.2f}s")
# [PASSED] test_login_valid_user — 2.35s

# Generating test data
for i in range(3):
    email = f"user_{i}@test.com"
    print(f"Created test user: {email}")
```
:::

## Conditional Statements

```python
# if / elif / else
status_code = 200

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code >= 500:
    print("Server Error")
else:
    print(f"Other code: {status_code}")

# Ternary operator
result = "Pass" if status_code == 200 else "Fail"
```

::: info QA Example: validating API responses
```python
# Status code validation
status_code = 201
assert 200 <= status_code < 300, f"Expected 2xx, got {status_code}"

# Response body validation
response_body = {"id": 1, "name": "Test User"}

if "id" in response_body:
    print(f"User created with ID: {response_body['id']}")
else:
    print("ERROR: 'id' not found in response")

# Checking multiple conditions
is_success = status_code == 200
has_data = response_body is not None
is_valid = is_success and has_data
```
:::

::: warning Indentation
Python uses indentation (4 spaces) instead of curly braces. Incorrect indentation will lead to `IndentationError`.
:::

## Common Beginner Mistakes

### `=` vs `==`

```python
# = is assignment
x = 10

# == is comparison
if x == 10:    # Correct
    print("yes")

if x = 10:     # SyntaxError!
    print("yes")
```

### Indentation (IndentationError)

```python
# Wrong — mixed indentation
if True:
    print("ok")
      print("error")  # IndentationError!

# Correct — consistent indentation (4 spaces)
if True:
    print("ok")
    print("also ok")
```

### Changing variable type

```python
# Python allows it, but it's risky
count = 10
count = "ten"   # Now it's a string — easy to get errors later

# Better: use different names
count = 10
count_text = "ten"
```

### `is None` vs `== None`

```python
result = None

# Correct — is checks identity
if result is None:
    print("No result")

if result is not None:
    print(f"Got: {result}")

# Not recommended — == checks equality (can be overridden)
if result == None:  # Works, but not recommended
    print("No result")
```

::: tip Rule
Always use `is None` and `is not None` when checking for `None`. The `is` operator compares object identity, not its value.
:::

## Test Yourself

<script setup>
const quizQuestions = [
  {
    question: 'What does type(42) return?',
    options: ['str', 'int', 'float', 'number'],
    correct: 1,
    explanation: 'type(42) returns <class int> because 42 is an integer.'
  },
  {
    question: 'Which character starts a single-line comment in Python?',
    options: ['//', '#', '--', '/*'],
    correct: 1,
    explanation: 'In Python, single-line comments start with #. The // syntax is used in JavaScript/C++.'
  },
  {
    question: 'Which of these data types is mutable?',
    options: ['str', 'tuple', 'int', 'dict'],
    correct: 3,
    explanation: 'dict (dictionary) is mutable — you can add, modify, and delete keys. str, tuple, and int are immutable.'
  },
  {
    question: 'What does the expression 10 // 3 return?',
    options: ['3.33', '3', '1', '3.0'],
    correct: 1,
    explanation: 'The // operator performs floor division. 10 // 3 = 3 (discards the fractional part).'
  },
  {
    question: 'What does the expression 10 % 3 return?',
    options: ['3', '0', '1', '10'],
    correct: 2,
    explanation: 'The % operator returns the remainder of division. 10 % 3 = 1, because 10 = 3 * 3 + 1.'
  },
  {
    question: 'Which naming style does PEP 8 recommend for variables?',
    options: ['camelCase', 'PascalCase', 'snake_case', 'UPPER_CASE'],
    correct: 2,
    explanation: 'PEP 8 recommends snake_case for variables and functions: user_name, max_retry_count.'
  },
  {
    question: 'What does bool("") return?',
    options: ['True', 'False', 'None', 'Error'],
    correct: 1,
    explanation: 'An empty string is a falsy value — bool("") returns False. Non-empty strings return True.'
  },
  {
    question: 'How should you check if a variable is None?',
    options: ['if x == None', 'if x is None', 'if x = None', 'if x.isNone()'],
    correct: 1,
    explanation: 'Use is None — the is operator checks object identity. == checks equality and can be overridden.'
  },
  {
    question: 'What is the difference between = and ==?',
    options: ['No difference', '= compares, == assigns', '= assigns a value, == compares', '== only works with numbers'],
    correct: 2,
    explanation: '= is the assignment operator (x = 10). == is the comparison operator (if x == 10). Confusing them is a common mistake.'
  },
  {
    question: 'What does True and False evaluate to?',
    options: ['True', 'False', 'None', 'Error'],
    correct: 1,
    explanation: 'The and operator returns True only when both operands are True. True and False = False.'
  },
  {
    question: 'What is the recommended way to format strings in modern Python?',
    options: ['% operator', '.format()', 'f-string', 'concat (+)'],
    correct: 2,
    explanation: 'f-strings are the recommended approach since Python 3.6+. They are the most readable and fastest.'
  },
  {
    question: 'What happens when you run: x, y, z = 1, 2, 3?',
    options: ['SyntaxError', 'x=1, y=2, z=3', 'All become [1,2,3]', 'x=3, y=2, z=1'],
    correct: 1,
    explanation: 'This is multiple assignment — each variable gets the corresponding value: x=1, y=2, z=3.'
  },
  {
    question: 'What is used to document functions in Python?',
    options: ['// comment', '# comment', 'docstring (triple quotes)', '/* ... */'],
    correct: 2,
    explanation: 'A docstring is a string in triple quotes right after the function definition. It is accessible via func.__doc__.'
  },
  {
    question: 'What error do incorrect indentations cause in Python?',
    options: ['SyntaxError', 'IndentationError', 'TypeError', 'ValueError'],
    correct: 1,
    explanation: 'Python uses indentation to define code blocks. Incorrect indentation raises IndentationError.'
  },
  {
    question: 'What does isinstance(True, bool) return?',
    options: ['True', 'False', 'None', 'TypeError'],
    correct: 0,
    explanation: 'isinstance checks if an object is an instance of a given type. True is a bool value, so the result is True.'
  }
]
</script>

<Quiz :questions="quizQuestions" />

## Useful Links

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Python for Beginners](https://www.learnpython.org/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/">← Introduction</a>
  <a href="/python_automation_courses/en/docs/python/data-types">Data Types →</a>
</div>
