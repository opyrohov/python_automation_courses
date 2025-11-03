# Lecture 8: Error Handling & Debugging

Learn how to handle errors gracefully and debug Python code effectively, with a focus on test automation scenarios.

## 🎯 Learning Objectives

By the end of this lecture, you will be able to:
- Use try/except blocks to handle errors
- Understand common Python errors and how to fix them
- Apply debugging techniques to find and fix issues
- Handle Playwright-specific errors (timeouts, element not found)
- Write robust automation code with proper error handling

## 📚 Topics Covered

### 1. Try/Except Blocks
- Understanding exceptions
- Basic try/except syntax
- Catching specific exceptions
- Using else and finally
- Raising exceptions
- Custom exceptions

### 2. Common Python Errors
- SyntaxError: Invalid Python syntax
- NameError: Variable not defined
- TypeError: Wrong data type
- ValueError: Invalid value
- IndexError: List index out of range
- KeyError: Dictionary key not found
- FileNotFoundError: File doesn't exist
- AttributeError: Attribute doesn't exist

### 3. Debugging Techniques
- Print debugging
- Using Python debugger (pdb)
- IDE debugging features
- Logging for debugging
- Stack traces and how to read them
- Common debugging strategies

### 4. Playwright Error Handling
- TimeoutError: Element not found in time
- Selector errors
- Navigation errors
- Context and browser errors
- Best practices for robust tests

## 🔧 Why This Matters for Test Automation

Error handling is crucial for automation:
- **Reliability**: Tests don't crash on unexpected issues
- **Debugging**: Quick identification of problems
- **Reporting**: Better error messages for failures
- **Resilience**: Tests handle edge cases gracefully
- **Maintenance**: Easier to fix broken tests

## 📂 Lecture Structure

```
Lecture_8_Error_Handling_Debugging/
├── README.md                          # This file
├── examples/
│   ├── 01_try_except_basics.py       # Basic exception handling
│   ├── 02_common_errors.py           # Common Python errors
│   ├── 03_exception_types.py         # Different exception types
│   ├── 04_debugging_techniques.py    # Debugging methods
│   ├── 05_logging_debugging.py       # Using logging
│   └── 06_playwright_error_handling.py # Playwright errors
├── exercises/
│   ├── exercise_01_basic_errors.py   # Practice error handling
│   ├── exercise_02_debugging.py      # Debug broken code
│   ├── exercise_03_playwright_errors.py # Handle test errors
│   └── SOLUTIONS.md                   # Exercise solutions
├── sample_code/
│   ├── buggy_code.py                 # Code with bugs to fix
│   └── broken_test.py                # Broken test to debug
└── presentation.html                  # Lecture slides
```

## 🚀 Getting Started

### Run Examples
```bash
# Navigate to examples directory
cd Lecture_8_Error_Handling_Debugging/examples

# Run any example
python 01_try_except_basics.py
python 02_common_errors.py
# ... and so on
```

### Complete Exercises
```bash
# Navigate to exercises directory
cd Lecture_8_Error_Handling_Debugging/exercises

# Work on exercises
python exercise_01_basic_errors.py
python exercise_02_debugging.py
python exercise_03_playwright_errors.py

# Check solutions
cat SOLUTIONS.md
```

## 💡 Key Concepts

### Basic Try/Except
```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # Handle the error
    print("Cannot divide by zero!")
```

### Multiple Exceptions
```python
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Finally Block
```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # Always runs, even if error occurs
    file.close()
```

### Playwright Error Handling
```python
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

try:
    page.click("#submit-button", timeout=5000)
except PlaywrightTimeoutError:
    print("Button not found within 5 seconds")
    # Take screenshot for debugging
    page.screenshot(path="error.png")
```

## 🐛 Debugging Best Practices

1. **Read the Error Message**: Python tells you exactly what went wrong
2. **Check the Stack Trace**: Shows where the error occurred
3. **Use Print Statements**: Quick way to see variable values
4. **Use Logging**: Better than print for production code
5. **Use Debugger**: Step through code line by line
6. **Isolate the Problem**: Test small parts of code separately
7. **Check Assumptions**: Verify your data is what you expect

## 🎯 Automation-Specific Tips

### Make Tests Resilient
```python
def safe_click(page, selector, timeout=5000):
    """Safely click an element with error handling."""
    try:
        page.click(selector, timeout=timeout)
        return True
    except PlaywrightTimeoutError:
        print(f"Could not find element: {selector}")
        page.screenshot(path=f"error_{selector.replace('#', '')}.png")
        return False
```

### Better Error Messages
```python
try:
    assert page.title() == "Expected Title"
except AssertionError:
    actual = page.title()
    raise AssertionError(
        f"Title mismatch!\n"
        f"Expected: 'Expected Title'\n"
        f"Actual: '{actual}'"
    )
```

## 📖 Additional Resources

- [Python Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html)
- [Playwright Error Handling](https://playwright.dev/python/docs/errors)
- [Python Logging Module](https://docs.python.org/3/library/logging.html)

## ✅ Practice Checklist

- [ ] Complete all examples
- [ ] Solve all exercises
- [ ] Debug the sample buggy code
- [ ] Fix the broken test
- [ ] Practice using pdb debugger
- [ ] Add error handling to previous lecture code
- [ ] Create custom exception classes
- [ ] Implement logging in automation scripts

## 🎓 Next Steps

After mastering error handling:
1. Add robust error handling to all your test scripts
2. Create a library of helper functions with error handling
3. Set up logging for your test suite
4. Practice debugging real automation issues
5. Move on to **Lecture 9** for more advanced topics!

---

**Remember**: Good error handling makes the difference between fragile tests that break easily and robust tests that provide valuable feedback!
