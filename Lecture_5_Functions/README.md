# Lecture 5: Functions

Welcome to the fifth lecture of the Python Automation Course! In this lecture, you'll learn how to create reusable blocks of code with functions - essential for writing clean, maintainable automation tests.

## Table of Contents
1. [Introduction to Functions](#introduction-to-functions)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Parameters and Arguments](#parameters-and-arguments)
4. [Return Values](#return-values)
5. [Advanced Function Concepts](#advanced-function-concepts)
6. [Why This Matters for Playwright](#why-this-matters-for-playwright)
7. [Practice Exercises](#practice-exercises)

## Introduction to Functions

Functions are reusable blocks of code that perform specific tasks. They help you organize code, avoid repetition, and make your automation tests more maintainable.

### Key Concepts:
- **What is a function?**: A named block of code that performs a specific task
- **Why use functions?**: DRY (Don't Repeat Yourself) principle, code organization, easier testing
- **Built-in vs custom**: Python has built-in functions (print, len, etc.), but you can create your own

## Defining and Calling Functions

Learn how to create and use your own functions.

### Key Concepts:
- **def keyword**: Used to define a function
- **Function name**: Should be descriptive and use snake_case
- **Indentation**: Function body must be indented
- **Calling functions**: Use function name followed by parentheses
- **Docstrings**: Document what your function does

See `examples/01_function_basics.py` for code examples.

## Parameters and Arguments

Functions can accept input data to make them more flexible and reusable.

### Key Concepts:
- **Parameters**: Variables defined in function definition
- **Arguments**: Actual values passed when calling the function
- **Positional arguments**: Order matters
- **Keyword arguments**: Name matters, order doesn't
- **Default parameters**: Provide default values
- **Multiple parameters**: Functions can accept many inputs
- ***args and **kwargs**: Variable number of arguments

See `examples/02_parameters_arguments.py` for code examples.

## Return Values

Functions can send data back to the caller using return statements.

### Key Concepts:
- **return keyword**: Sends value back to caller
- **Multiple return values**: Return tuples or multiple values
- **None return**: Functions without return statement return None
- **Early returns**: Exit function early based on conditions
- **Using return values**: Store in variables or use directly

See `examples/03_return_values.py` for code examples.

## Advanced Function Concepts

More sophisticated function techniques for better code organization.

### Key Concepts:
- **Function scope**: Variables inside functions are local
- **Global vs local variables**: Understanding variable visibility
- **Lambda functions**: Short, anonymous functions
- **Functions as arguments**: Pass functions to other functions
- **Nested functions**: Functions inside functions
- **Recursion**: Functions that call themselves

See `examples/04_advanced_functions.py` for code examples.

## Why This Matters for Playwright

Functions are fundamental to writing clean, maintainable automation code and enable code reuse across your test suite.

### Functions in Automation:
- **Reusable test steps**: Login, navigation, form filling
- **Helper functions**: Wait for elements, take screenshots, verify text
- **Page objects**: Organize locators and actions by page
- **Data setup/teardown**: Create test data, clean up after tests
- **Custom assertions**: Verify multiple conditions
- **Configuration**: Load and parse test settings

### Common Automation Patterns:
- **login(username, password)**: Reusable login function
- **navigate_to(page_name)**: Navigate to different pages
- **fill_form(form_data)**: Fill forms with dictionary data
- **wait_and_click(locator)**: Combine wait and click operations
- **verify_text_present(expected_texts)**: Check multiple text strings
- **take_screenshot(name)**: Capture and name screenshots

### Benefits for Test Automation:
- **DRY principle**: Write once, use everywhere
- **Easier maintenance**: Update in one place
- **Better readability**: Test code reads like documentation
- **Faster development**: Build on existing functions
- **Easier debugging**: Isolate issues to specific functions
- **Team collaboration**: Share utility functions

See `examples/05_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_function_basics.py` - Creating and calling functions
- `exercise_02_parameters_return.py` - Working with parameters and return values
- `exercise_03_playwright_helpers.py` - Building automation helper functions

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Quick Reference

### Basic Function
```python
def greet():
    print("Hello, World!")

greet()  # Call the function
```

### Function with Parameters
```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
```

### Function with Return Value
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # result = 8
```

### Function with Default Parameters
```python
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()        # Hello, Guest!
greet_user("Bob")   # Hello, Bob!
```

### Multiple Return Values
```python
def get_user_info():
    name = "Alice"
    age = 25
    return name, age

user_name, user_age = get_user_info()
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Creating and calling functions
- Using parameters and arguments effectively
- Returning values from functions
- Organizing automation code with helper functions
- Understanding when to create new functions
- Writing reusable test utilities

Move on to Lecture 6 when you're ready!
