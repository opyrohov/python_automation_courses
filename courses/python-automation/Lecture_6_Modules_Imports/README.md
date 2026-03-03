# Lecture 6: Modules & Imports

Welcome to the sixth lecture of the Python Automation Course! In this lecture, you'll learn how to organize code with modules, import functionality, and use external packages - essential for working with Playwright and other automation libraries.

## Table of Contents
1. [What are Modules?](#what-are-modules)
2. [Importing Modules](#importing-modules)
3. [Creating Your Own Modules](#creating-your-own-modules)
4. [Python Standard Library](#python-standard-library)
5. [Installing External Packages with pip](#installing-external-packages-with-pip)
6. [Working with External Libraries](#working-with-external-libraries)
7. [Why This Matters for Playwright](#why-this-matters-for-playwright)
8. [Practice Exercises](#practice-exercises)

## What are Modules?

Modules are Python files containing functions, classes, and variables that can be imported and used in other programs.

### Key Concepts:
- **Module**: A single Python file (.py)
- **Package**: A directory containing multiple modules with an `__init__.py` file
- **Library**: A collection of packages
- **Why use modules?**: Code organization, reusability, namespace management

## Importing Modules

Learn different ways to import modules and their contents.

### Key Concepts:
- **import statement**: Import entire modules
- **from...import**: Import specific items from modules
- **import...as**: Create aliases for modules
- **from...import ***: Import everything (not recommended)
- **Relative vs absolute imports**: Different import styles
- **Module search path**: Where Python looks for modules

See `examples/01_importing_basics.py` for code examples.

## Creating Your Own Modules

Build your own modules to organize automation helper functions.

### Key Concepts:
- **Creating a module**: Just save a .py file
- **Importing your modules**: Use the file name (without .py)
- **Module variables**: `__name__` and `if __name__ == "__main__"`
- **Organizing test helpers**: Group related functions
- **Module structure**: Best practices for organization

See `examples/02_creating_modules.py` and the `my_modules/` folder for code examples.

## Python Standard Library

Python comes with many built-in modules - no installation needed!

### Key Concepts:
- **datetime**: Working with dates and times
- **random**: Generating random data for tests
- **os**: Operating system operations
- **pathlib**: File path handling
- **json**: Working with JSON data
- **time**: Time-related functions
- **math**: Mathematical operations

See `examples/03_standard_library.py` for code examples.

## Installing External Packages with pip

Learn to install and manage external Python packages.

### Key Concepts:
- **pip**: Python's package installer
- **Installing packages**: `pip install package_name`
- **Uninstalling packages**: `pip uninstall package_name`
- **Listing packages**: `pip list`
- **Requirements file**: `requirements.txt` for project dependencies
- **Virtual environments**: Isolated Python environments (preview)

See `examples/04_pip_packages.py` for code examples.

## Working with External Libraries

Use powerful third-party libraries in your automation.

### Key Concepts:
- **Popular libraries**: requests, pytest, playwright
- **Reading documentation**: How to learn new libraries
- **Import patterns**: Common ways to import libraries
- **Version management**: Specifying package versions
- **Troubleshooting imports**: Common import errors

See `examples/05_external_libraries.py` for code examples.

## Why This Matters for Playwright

Understanding modules and imports is essential for Playwright automation and organizing test code.

### Modules in Automation:
- **Importing Playwright**: `from playwright.sync_api import sync_playwright`
- **Organizing page objects**: Separate modules for each page
- **Helper modules**: Utility functions in separate files
- **Configuration modules**: Test settings and constants
- **Test fixtures**: Reusable setup/teardown in separate modules
- **Custom assertions**: Verification helpers in modules

### Common Playwright Import Patterns:
- **Basic imports**: Sync vs async APIs
- **Specific imports**: Page, Browser, BrowserContext
- **Expect assertions**: `from playwright.sync_api import expect`
- **Test fixtures**: Importing pytest fixtures
- **Page objects**: Importing page classes

### Project Structure:
```
test_project/
├── tests/
│   ├── test_login.py
│   ├── test_checkout.py
├── pages/
│   ├── login_page.py
│   ├── home_page.py
├── utils/
│   ├── helpers.py
│   ├── config.py
├── requirements.txt
```

See `examples/06_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_import_basics.py` - Basic importing practice
- `exercise_02_create_modules.py` - Creating your own modules
- `exercise_03_automation_modules.py` - Building automation utilities

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Install a package
pip install requests

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Show package info
pip show playwright
```

## Quick Reference

### Import Styles
```python
# Import entire module
import math
print(math.sqrt(16))

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import datetime as dt
print(dt.datetime.now())

# Import multiple items
from math import sqrt, pi, ceil
```

### Creating a Module
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module
print(my_module.greet("Alice"))
```

### Using pip
```bash
# Install package
pip install playwright

# Install specific version
pip install playwright==1.40.0

# Install from requirements.txt
pip install -r requirements.txt

# Uninstall package
pip uninstall playwright
```

### Playwright Imports
```python
# Sync API (what we'll use)
from playwright.sync_api import sync_playwright, expect

# Async API (advanced)
from playwright.async_api import async_playwright

# Specific classes
from playwright.sync_api import Page, Browser, BrowserContext
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Importing modules using different syntax
- Creating your own modules to organize code
- Using Python's standard library
- Installing packages with pip
- Working with external libraries
- Setting up Playwright for automation
- Organizing test code with modules

Move on to Lecture 7 when you're ready to start hands-on Playwright automation!
