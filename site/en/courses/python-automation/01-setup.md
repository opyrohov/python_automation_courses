# Lecture 1: Installing Python and Basics

The first lecture of the course — installing Python, setting up the development environment, variables, data types, and basic operators.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_1_Python_Basics_Setup/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Installing Python
- Setting up an IDE (VS Code / PyCharm)
- Virtual environment
- First "Hello World" program
- Variables and data types
- Basic operators
- The `print()` function and formatting

## Installing Python

### Downloading and Installing

1. Download Python from [python.org](https://www.python.org/downloads/) (version 3.11+)
2. During installation, make sure to check **"Add Python to PATH"**
3. Verify the installation:

```bash
python --version
# or
python3 --version
```

::: warning Important: Add to PATH
Without this option, Python will not be available from the command line. If you forgot — reinstall Python with this option checked.
:::

### Choosing an IDE

#### VS Code (recommended for beginners)

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension:
   - Open VS Code → Extensions (`Ctrl+Shift+X`)
   - Search for "Python" by Microsoft → Install

#### PyCharm

1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Community Edition — free
3. Built-in Python support

### Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

::: info Why use a virtual environment?
It isolates project dependencies from the system Python. Each project has its own libraries, without conflicts between them.
:::

## Hello World

```python
# First program
print("Hello, World!")

# Variables
name = "Python"
version = 3.12
is_awesome = True

print(f"Welcome to {name} {version}!")
```

### Running the Program

```bash
# Save the code to a file hello.py and run it
python hello.py
```

## Variables and Data Types

Variables in Python do not require type declaration — the interpreter determines the type automatically.

```python
# Creating variables
name = "Alice"          # str — string
age = 25                # int — integer
height = 5.6            # float — floating-point number
is_student = True       # bool — boolean value

# Multiple assignment
x, y, z = 1, 2, 3
```

### Basic Data Types

| Type | Example | Description |
|------|---------|-------------|
| `str` | `"Hello"` | String |
| `int` | `42` | Integer |
| `float` | `3.14` | Floating-point number |
| `bool` | `True` / `False` | Boolean value |
| `None` | `None` | Absence of a value |

### Type Checking and Conversion

```python
# Type checking
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>

# Type conversion
age_string = "30"
age_number = int(age_string)        # str → int
price_string = "29.99"
price_number = float(price_string)  # str → float
count = 100
count_string = str(count)           # int → str
```

::: tip Variable Naming
Use `snake_case` — this is the Python standard (PEP 8):
```python
# Correct ✓
user_name = "Alice"
total_price = 99.99
is_active = True

# Incorrect ✗
userName = "Alice"    # camelCase — this is for JavaScript
TotalPrice = 99.99   # PascalCase — this is for classes
```
:::

## Operators

### Arithmetic Operators

```python
a, b = 10, 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.33 — division (always float)
print(a // b)  # 3   — floor division
print(a % b)   # 1   — modulo (remainder)
print(a ** b)  # 1000 — exponentiation
```

### Comparison Operators

```python
x, y = 5, 10

print(x == y)   # False — equal to
print(x != y)   # True  — not equal to
print(x > y)    # False — greater than
print(x < y)    # True  — less than
print(x >= y)   # False — greater than or equal to
print(x <= y)   # True  — less than or equal to
```

### Logical Operators

```python
is_adult = True
has_ticket = True

# and — both conditions are True
can_enter = is_adult and has_ticket  # True

# or — at least one condition is True
has_cash = False
has_card = True
can_pay = has_cash or has_card  # True

# not — negation
is_raining = False
is_sunny = not is_raining  # True
```

### Compound Assignment Operators

```python
score = 100
score += 10   # score = score + 10 → 110
score -= 5    # score = score - 5  → 105
score *= 2    # score = score * 2  → 210
score /= 3    # score = score / 3  → 70.0
```

## The print() Function

### Basic Usage

```python
# Simple output
print("Hello, World!")

# Multiple values (separated by spaces)
print("Hello", "Python", "Programming")

# Without newline
print("Loading", end="")
print("...", end="")
print(" Done!")  # Loading... Done!

# Custom separator
print("2024", "01", "15", sep="-")  # 2024-01-15
```

### String Formatting (f-strings)

```python
name = "Alice"
age = 25

# f-string — recommended method
print(f"My name is {name} and I'm {age} years old")

# Expressions inside f-strings
print(f"Next year I'll be {age + 1}")
print(f"Name uppercase: {name.upper()}")

# Number formatting
price = 1234.567
print(f"Price: ${price:.2f}")        # Price: $1234.57
print(f"Large: {1234567890:,}")      # Large: 1,234,567,890
print(f"Percent: {0.856:.1%}")       # Percent: 85.6%
```

::: info Other Formatting Methods
```python
# .format() — older method
print("Hello, {}!".format(name))

# % operator — deprecated
print("Hello, %s!" % name)

# f-strings — most convenient, use this one
print(f"Hello, {name}!")
```
:::

### Text Alignment

```python
# Table with alignment
print(f"{'Product':<15} {'Price':>10}")
print(f"{'Laptop':<15} {'$999.99':>10}")
print(f"{'Mouse':<15} {'$29.99':>10}")
print(f"{'Keyboard':<15} {'$79.99':>10}")
```

### Debugging with print

```python
# Python 3.8+ — shows the variable name
username = "john_doe"
user_age = 30
print(f"{username=}")   # username='john_doe'
print(f"{user_age=}")   # user_age=30
```

## Comments

```python
# Single-line comment

"""
Multi-line comment
used for documentation
"""

# Comment explaining code
tax_rate = 0.08  # 8% tax
```

## Exercises

::: tip Exercise 1: Variables and Data Types
Create variables for a city (name, population, area, whether it is a capital). Display the information using f-strings.

[📝 Exercise file](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_01_variables.py)
:::

::: tip Exercise 2: Calculator
Write a restaurant bill calculator program: cost of food + drinks + tax (8%) + tip (18%).

[📝 Exercise file](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_02_calculations.py)
:::

::: tip Exercise 3: Personal Card
Create a program that displays a beautiful business card with your information (name, profession, skills, contacts).

[📝 Exercise file](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_03_personal_info.py)
:::

## What's Next?

After this lecture you should be able to:
- Install Python and set up an IDE
- Create and use variables
- Work with different data types
- Use operators
- Format output using f-strings

::: info Additional Materials
- [Documentation: Python Basics](/en/docs/python/basics) — detailed reference
- [Documentation: Data Types](/en/docs/python/data-types) — complete overview of types
- [Cheatsheet: Python](/en/cheatsheets/python) — quick reference
:::

## Useful Links

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python.org — Downloads](https://www.python.org/downloads/)
- [VS Code — Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
