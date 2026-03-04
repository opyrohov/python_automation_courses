# Python Basics

Basic Python language syntax — variables, operators, input/output.

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

## Data Types

```python
# Type checking
name = "Test"
print(type(name))  # <class 'str'>

# Basic types
text = "Hello"          # str
number = 42             # int
decimal = 3.14          # float
flag = True             # bool
nothing = None          # NoneType
items = [1, 2, 3]      # list
pair = (1, 2)           # tuple
unique = {1, 2, 3}      # set
data = {"key": "value"} # dict
```

## Operators

### Arithmetic Operators

```python
a, b = 10, 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.33 — division (float)
print(a // b)  # 3   — floor division
print(a % b)   # 1   — modulo
print(a ** b)  # 1000 — exponentiation
```

### Comparison Operators

```python
x, y = 5, 10

print(x == y)   # False — equals
print(x != y)   # True  — not equals
print(x > y)    # False — greater than
print(x < y)    # True  — less than
print(x >= y)   # False — greater than or equal
print(x <= y)   # True  — less than or equal
```

### Logical Operators

```python
a, b = True, False

print(a and b)  # False — logical AND
print(a or b)   # True  — logical OR
print(not a)    # False — logical NOT
```

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

::: warning Indentation
Python uses indentation (4 spaces) instead of curly braces. Incorrect indentation will lead to `IndentationError`.
:::

## Useful Links

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Python for Beginners](https://www.learnpython.org/)
