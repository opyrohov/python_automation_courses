# Lecture 2: Strings & Control Flow

Welcome to the second lecture of the Python Automation Course! In this lecture, you'll learn how to work with strings and control the flow of your programs using conditional statements.

## Table of Contents
1. [String Manipulation & Formatting](#string-manipulation--formatting)
2. [Control Flow with if/elif/else](#control-flow-with-ifelifelse)
3. [Comparison Operators](#comparison-operators)
4. [Why This Matters for Playwright](#why-this-matters-for-playwright)
5. [Practice Exercises](#practice-exercises)

## String Manipulation & Formatting

Strings are one of the most commonly used data types in automation. You'll frequently work with text from web pages, user inputs, and test data.

### Key Concepts:
- **String methods**: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`
- **String slicing**: Accessing parts of a string
- **String formatting**: f-strings, `.format()`, string concatenation
- **String searching**: `.find()`, `.count()`, `in` operator

See `examples/01_string_manipulation.py` for code examples.

## Control Flow with if/elif/else

Control flow statements allow your program to make decisions and execute different code based on conditions.

### Key Concepts:
- **if statements**: Execute code when a condition is True
- **elif (else if)**: Check multiple conditions
- **else**: Execute code when all conditions are False
- **Nested conditions**: if statements inside other if statements
- **Logical operators**: Combining conditions with `and`, `or`, `not`

See `examples/02_control_flow.py` for code examples.

## Comparison Operators

Comparison operators let you compare values and make decisions in your code.

### Operators:
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

See `examples/03_comparison_operators.py` for code examples.

## Why This Matters for Playwright

Understanding strings and control flow is essential for web automation:

### String Skills in Automation:
- **Checking page text**: Verify that the correct content appears on a page
- **Form inputs**: Manipulate and validate text inputs
- **URL handling**: Extract and modify URLs
- **Data validation**: Check that text matches expected patterns

### Control Flow in Automation:
- **Conditional actions**: Click different buttons based on page state
- **Error handling**: Take different actions if an element is missing
- **Test logic**: Run different test steps based on conditions
- **Dynamic waits**: Wait for elements only when needed

See `examples/04_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_string_practice.py` - String manipulation challenges
- `exercise_02_conditions.py` - Conditional logic practice
- `exercise_03_playwright_scenarios.py` - Automation-focused exercises

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Manipulating and formatting strings
- Using if/elif/else statements to control program flow
- Comparing values with comparison operators
- Understanding how these concepts apply to web automation

Move on to Lecture 3 when you're ready!
