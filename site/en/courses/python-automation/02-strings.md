# Lecture 2: Strings and Control Flow

Working with strings and controlling the flow of execution.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_2_Strings_Control_Flow/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Strings and their methods
- String formatting (f-strings)
- Conditional operators (if/elif/else)
- Comparison and logical operators

## Strings

```python
# Creating strings
single = 'Hello'
double = "World"
multiline = """
Multi-line
text
"""

# Concatenation
full = single + " " + double  # "Hello World"

# Repetition
repeat = "Ha" * 3  # "HaHaHa"
```

## String Methods

```python
text = "  Hello World  "

text.strip()       # "Hello World"
text.lower()       # "  hello world  "
text.upper()       # "  HELLO WORLD  "
text.replace("o", "0")  # "  Hell0 W0rld  "
text.split()       # ["Hello", "World"]

# Checks
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True
"Hello".isalpha()         # True
"123".isdigit()           # True
```

## F-strings (Formatting)

```python
name = "Alice"
age = 25

# F-string
message = f"My name is {name} and I'm {age} years old"

# With expressions
result = f"Next year I'll be {age + 1}"

# Number formatting
price = 19.99
formatted = f"Price: ${price:.2f}"  # "Price: $19.99"
```

## Conditional Operators

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade: {grade}")
```

## Logical Operators

```python
age = 25
has_license = True

# and - both conditions are True
can_drive = age >= 18 and has_license

# or - at least one condition is True
is_minor_or_senior = age < 18 or age > 65

# not - negation
is_adult = not (age < 18)
```

## Ternary Operator

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

## Exercises

::: tip Exercise 1
Write a program that checks whether a number is even or odd.
:::

::: tip Exercise 2
Create a program to determine the largest of three numbers.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/examples)
