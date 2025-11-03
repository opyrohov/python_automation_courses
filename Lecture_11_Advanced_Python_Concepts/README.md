# Lecture 11: Advanced Python Concepts

Welcome to the eleventh lecture of the Python Automation Course! In this lecture, you'll learn advanced Python techniques that will make your automation code more elegant, efficient, and professional.

## Table of Contents
1. [List and Dictionary Comprehensions](#list-and-dictionary-comprehensions)
2. [Args and Kwargs](#args-and-kwargs)
3. [Decorators Basics](#decorators-basics)
4. [Working with Datetime](#working-with-datetime)
5. [String Methods Deep Dive](#string-methods-deep-dive)
6. [Why This Matters for Playwright](#why-this-matters-for-playwright)
7. [Practice Exercises](#practice-exercises)

## List and Dictionary Comprehensions

Comprehensions provide a concise way to create lists, dictionaries, and sets from existing iterables. They make your code more Pythonic and readable.

### Key Concepts:
- **List comprehensions**: Create lists in a single line
- **Dictionary comprehensions**: Build dictionaries efficiently
- **Set comprehensions**: Generate unique value sets
- **Conditional comprehensions**: Filter data while creating collections
- **Nested comprehensions**: Handle multi-dimensional data
- **Performance benefits**: Often faster than traditional loops

See `examples/01_comprehensions.py` for code examples.

## Args and Kwargs

Special syntax for handling variable numbers of arguments in functions, enabling flexible function signatures.

### Key Concepts:
- **\*args**: Accept any number of positional arguments
- **\*\*kwargs**: Accept any number of keyword arguments
- **Unpacking**: Use * and ** to unpack iterables and dictionaries
- **Combining with regular parameters**: Order matters
- **Use cases**: Wrapper functions, flexible APIs, forwarding arguments
- **Best practices**: When to use and when to avoid

See `examples/02_args_kwargs.py` for code examples.

## Decorators Basics

Decorators are a powerful feature that allows you to modify or enhance functions without changing their code directly.

### Key Concepts:
- **What are decorators?**: Functions that wrap other functions
- **@syntax**: Clean decorator application
- **Use cases**: Logging, timing, authentication, retry logic
- **Built-in decorators**: @property, @staticmethod, @classmethod
- **Creating custom decorators**: Step-by-step guide
- **Practical applications**: Test automation scenarios

See `examples/03_decorators.py` for code examples.

## Working with Datetime

Python's datetime module is essential for handling dates, times, and time-based operations in your automation scripts.

### Key Concepts:
- **datetime objects**: Representing specific moments in time
- **date and time objects**: Working with dates and times separately
- **timedelta**: Calculating time differences
- **Formatting**: strftime and strptime for string conversion
- **Time zones**: Handling different time zones
- **Common operations**: Current time, date arithmetic, comparisons

See `examples/04_datetime_module.py` for code examples.

## String Methods Deep Dive

Master essential string methods that you'll use constantly in automation testing for data manipulation and validation.

### Key Concepts:
- **split()**: Breaking strings into lists
- **join()**: Combining lists into strings
- **strip(), lstrip(), rstrip()**: Removing whitespace
- **replace()**: Substituting substrings
- **Advanced methods**: startswith, endswith, find, count
- **Case methods**: upper, lower, title, capitalize
- **Validation methods**: isdigit, isalpha, isalnum

See `examples/05_string_methods.py` for code examples.

## Why This Matters for Playwright

These advanced concepts are crucial for writing professional, maintainable test automation code and handling complex test scenarios.

### Comprehensions in Testing:
- **Filter test data**: Extract specific test cases from large datasets
- **Transform locators**: Generate multiple selectors from patterns
- **Process results**: Aggregate test outcomes efficiently
- **Clean data**: Remove invalid entries before tests
- **Generate test inputs**: Create test data combinations

### Args/Kwargs in Testing:
- **Flexible test helpers**: Functions that work with varying parameters
- **Custom assertions**: Variable number of conditions to check
- **Page object methods**: Handle optional parameters elegantly
- **Test fixtures**: Create reusable setup with flexible configuration
- **API testing**: Pass dynamic headers and parameters

### Decorators in Testing:
- **Retry failed tests**: Automatically retry flaky tests
- **Performance monitoring**: Time test execution
- **Screenshot on failure**: Capture state when tests fail
- **Logging**: Automatic test step logging
- **Authentication**: Login before test execution
- **Test data cleanup**: Ensure cleanup after tests

### Datetime in Testing:
- **Time-based testing**: Test scheduling features
- **Wait calculations**: Dynamic waits based on time
- **Test reports**: Timestamp test results
- **Date input testing**: Fill date fields with various formats
- **Expiration testing**: Test with dates in past/future
- **Performance tracking**: Measure execution times

### String Methods in Testing:
- **Data validation**: Verify text formats and patterns
- **Log parsing**: Extract information from logs
- **URL manipulation**: Build and modify test URLs
- **CSV/JSON processing**: Parse test data files
- **Text assertions**: Clean and compare expected vs actual text
- **Dynamic locators**: Build selectors from strings

See `examples/06_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_comprehensions.py` - Master list and dictionary comprehensions
- `exercise_02_args_kwargs_decorators.py` - Work with flexible functions and decorators
- `exercise_03_datetime_strings.py` - Handle dates and string manipulation
- `exercise_04_automation_helpers.py` - Build advanced test automation utilities

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Quick Reference

### List Comprehension
```python
# Basic list comprehension
numbers = [x * 2 for x in range(5)]  # [0, 2, 4, 6, 8]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Dictionary Comprehension
```python
# Create dictionary from lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = {k: v for k, v in zip(keys, values)}
```

### Args and Kwargs
```python
def flexible_function(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)
```

### Simple Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
```

### Datetime Basics
```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
```

### String Methods
```python
text = "  Hello, World!  "
text.strip()           # "Hello, World!"
text.split(',')        # ["  Hello", " World!  "]
'-'.join(['a', 'b'])   # "a-b"
text.replace('!', '?') # "  Hello, World?  "
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Using comprehensions for efficient data transformation
- Creating flexible functions with *args and **kwargs
- Understanding and creating basic decorators
- Working with dates and times in Python
- Using advanced string methods for text processing
- Applying these concepts in test automation scenarios

Move on to Lecture 12 when you're ready!
