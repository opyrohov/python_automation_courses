# Lecture 12: Python Review & Project Setup

Welcome to the twelfth lecture of the Python Automation Course! This lecture consolidates everything you've learned in Python and prepares you to start automation testing with Playwright by setting up a professional project structure.

## Table of Contents
1. [Python Fundamentals Review](#python-fundamentals-review)
2. [Virtual Environments](#virtual-environments)
3. [Project Structure Best Practices](#project-structure-best-practices)
4. [Dependency Management](#dependency-management)
5. [Introduction to Testing Mindset](#introduction-to-testing-mindset)
6. [Setting Up Your First Automation Project](#setting-up-your-first-automation-project)
7. [Preparing for Playwright](#preparing-for-playwright)
8. [Practice Exercises](#practice-exercises)

## Python Fundamentals Review

Quick recap of all Python concepts covered in Lectures 1-11.

### Key Topics Covered:
- **Lecture 1-2**: Variables, data types, strings, f-strings, if/elif/else
- **Lecture 3**: For loops, while loops, range(), break, continue
- **Lecture 4**: Lists, dictionaries, indexing, iteration
- **Lecture 5**: Functions, parameters, return values, default arguments
- **Lecture 6**: Modules, imports, pip package installation
- **Lecture 7**: File handling, JSON reading/writing, with statements
- **Lecture 8**: Try/except blocks, error handling, finally
- **Lecture 9**: Classes, __init__, instance variables, methods
- **Lecture 10**: Inheritance, super(), Page Object Model pattern
- **Lecture 11**: Comprehensions, *args/**kwargs, decorators, datetime

See the presentation for a comprehensive review of all concepts.

## Virtual Environments

Virtual environments isolate your project dependencies, preventing conflicts between projects.

### Key Concepts:
- **Why use virtual environments**: Isolate dependencies per project
- **Creating venv**: `python -m venv venv`
- **Activating venv**:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- **Deactivating**: `deactivate`
- **Don't commit venv**: Add to .gitignore
- **Best practice**: Always use venv for projects

See `examples/01_venv_setup.md` for detailed setup instructions.

## Project Structure Best Practices

A well-organized project structure makes your code maintainable and professional.

### Recommended Structure:
```
my_automation_project/
├── venv/                  # Virtual environment (gitignored)
├── tests/                 # All test files (test_*.py)
├── pages/                 # Page Object Model classes
├── utils/                 # Helper functions and configuration
├── test_data/             # JSON, CSV, or other test data
├── requirements.txt       # Project dependencies
├── pytest.ini             # Pytest configuration
├── .env                   # Environment variables (gitignored)
├── .env.example           # Template for .env
└── .gitignore             # Files to exclude from Git
```

### Key Concepts:
- **Naming conventions**: Test files must start with `test_`
- **__init__.py files**: Make folders into Python packages
- **Separation of concerns**: Tests, pages, utilities in separate folders
- **Configuration files**: pytest.ini, .env for settings
- **Documentation**: README.md for project overview

See `examples/02_project_structure/` for a template project.

## Dependency Management

Managing project dependencies ensures everyone can run your tests with the same package versions.

### requirements.txt:
A file listing all Python packages needed for your project.

### Key Concepts:
- **Creating requirements.txt**: `pip freeze > requirements.txt` or manually
- **Installing from requirements.txt**: `pip install -r requirements.txt`
- **Version pinning**: Specify exact versions (e.g., `playwright==1.40.0`)
- **Version ranges**: Allow flexibility (e.g., `pytest>=8.0.0`)
- **Keep it minimal**: Only list packages you actually use
- **Update regularly**: Keep dependencies current for security

See `examples/03_requirements_example.txt` for a sample file.

## Introduction to Testing Mindset

Understanding software testing principles before writing automation code.

### Key Concepts:
- **What is testing**: Verifying software works as expected
- **Manual vs Automated**: Tradeoffs and when to use each
- **Types of tests**:
  - Unit tests: Test individual functions
  - Integration tests: Test multiple components together
  - E2E tests: Test complete user flows (Playwright)
- **Testing pyramid**: More unit tests, fewer E2E tests
- **Good test characteristics**: Fast, Independent, Repeatable, Clear, Focused
- **AAA pattern**: Arrange, Act, Assert - standard test structure

### AAA Pattern Example:
```python
def test_login(page):
    # ARRANGE - Setup
    username = "test@example.com"
    password = "SecurePass123"
    page.goto("/login")

    # ACT - Perform action
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")

    # ASSERT - Verify outcome
    assert page.is_visible(".dashboard")
```

See `examples/04_testing_concepts.md` for detailed explanations.

## Setting Up Your First Automation Project

Step-by-step guide to creating a professional automation project from scratch.

### Setup Steps:
1. **Create project folder** and subdirectories (tests, pages, utils, test_data)
2. **Create virtual environment**: `python -m venv venv`
3. **Activate virtual environment**: Platform-specific activation
4. **Create requirements.txt**: List dependencies (playwright, pytest, etc.)
5. **Install dependencies**: `pip install -r requirements.txt`
6. **Install Playwright browsers**: `playwright install`
7. **Create .gitignore**: Exclude venv, cache, test results
8. **Create pytest.ini**: Configure pytest settings
9. **Create config files**: utils/config.py for settings
10. **Create .env file**: Environment-specific variables (don't commit!)
11. **Write first test**: Simple example to verify setup
12. **Run tests**: `pytest` to verify everything works

See `examples/05_setup_guide.md` for detailed walkthrough.

## Preparing for Playwright

Ensure your environment is ready for Playwright automation.

### Installation Checklist:
- ✓ Python 3.8+ installed
- ✓ Virtual environment created and activated
- ✓ Playwright installed via pip
- ✓ Browser drivers installed (`playwright install`)
- ✓ pytest and pytest-playwright installed
- ✓ First test runs successfully

### Playwright Browsers:
- **Chromium**: Open-source Chrome (default)
- **Firefox**: Mozilla Firefox
- **WebKit**: Safari's engine (cross-platform)

### Verification Commands:
```bash
python --version          # Check Python version
pytest --version          # Verify pytest installed
playwright --version      # Verify Playwright installed
pip list                  # List all installed packages
```

### Common Setup Issues:
- **"playwright: command not found"**: Activate venv
- **"No module named 'playwright'"**: Run `pip install playwright`
- **"Can't find browsers"**: Run `playwright install`
- **Wrong Python version**: Recreate venv with correct Python

See `examples/06_playwright_installation.md` for troubleshooting guide.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_project_setup.md` - Create your first automation project
- `exercise_02_venv_practice.md` - Practice with virtual environments
- `exercise_03_requirements.md` - Manage dependencies
- `exercise_04_first_test.py` - Write and run your first Playwright test

Solutions and detailed explanations are available in `exercises/SOLUTIONS.md`.

## Quick Reference

### Create Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

### Install Playwright
```bash
# Activate venv first!
pip install playwright pytest pytest-playwright

# Install browsers
playwright install

# Verify installation
pytest --version
playwright --version
```

### Run Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run with verbose output
pytest -v

# Run in headed mode (see browser)
pytest --headed

# Run specific browser
pytest --browser firefox
```

### Sample requirements.txt
```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
python-dotenv==1.0.0
```

### Sample .gitignore
```
venv/
__pycache__/
*.pyc
.pytest_cache/
.env
test-results/
screenshots/
```

### Sample pytest.ini
```ini
[pytest]
testpaths = tests
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
addopts = -v --tb=short
```

## Before Next Lecture

Complete these tasks to be ready for Lecture 13:

1. ✓ Create your automation project folder with proper structure
2. ✓ Set up virtual environment successfully
3. ✓ Create and populate requirements.txt
4. ✓ Install all dependencies including Playwright
5. ✓ Create .gitignore, pytest.ini, and .env files
6. ✓ Write and run the example test successfully
7. ✓ Experiment: Try running tests in different browsers

## Next Steps

After completing this lecture, you should be comfortable with:
- All Python fundamentals from Lectures 1-11
- Creating and using virtual environments
- Structuring automation projects professionally
- Managing dependencies with requirements.txt
- Understanding testing principles and the AAA pattern
- Setting up Playwright and running basic tests
- Troubleshooting common setup issues

**You're now ready to dive deep into Playwright automation in Lecture 13!** 🚀

## Additional Resources

- **Python Virtual Environments**: https://docs.python.org/3/library/venv.html
- **Playwright Documentation**: https://playwright.dev/python/
- **Pytest Documentation**: https://docs.pytest.org/
- **Python .gitignore Template**: https://github.com/github/gitignore/blob/main/Python.gitignore
- **pip Documentation**: https://pip.pypa.io/en/stable/

## Questions or Issues?

If you encounter any problems:
1. Check the examples folder for detailed guides
2. Review the SOLUTIONS.md file in exercises
3. Verify your Python and pip versions
4. Ensure virtual environment is activated
5. Check that all dependencies installed correctly

Happy automating! 🎉
