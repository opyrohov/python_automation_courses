# Lecture 1: Python Basics & Setup

Welcome to the first lecture of the Python Automation Course! In this lecture, you'll learn the fundamentals of Python programming and set up your development environment.

## 📊 Interactive Presentation

**New!** Open `presentation.html` in your web browser for an interactive slide presentation of this lecture!

- **Navigate:** Use arrow keys (← →) or click the navigation buttons
- **Jump:** Press Home/End to go to first/last slide
- **Features:** Syntax-highlighted code examples, visual formatting, and organized content

Simply double-click `presentation.html` or open it in any modern web browser to get started.

## Table of Contents
1. [Installation & Setup](#installation--setup)
2. [Variables & Data Types](#variables--data-types)
3. [Basic Operators](#basic-operators)
4. [Print Statements](#print-statements)
5. [Comments & Code Structure](#comments--code-structure)
6. [Practice Exercises](#practice-exercises)

## Installation & Setup

### Installing Python

1. **Download Python**
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.11 or later
   - During installation, check "Add Python to PATH"

2. **Verify Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

### Choosing Your IDE

#### Option 1: Visual Studio Code (Recommended for Beginners)

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension:
   - Open VS Code
   - Click Extensions (Ctrl+Shift+X)
   - Search "Python" by Microsoft
   - Click Install

#### Option 2: PyCharm

1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Choose Community Edition (free) or Professional
3. Python support is built-in

### Setting Up a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

## Variables & Data Types

Variables store data that your program can use and manipulate.

### Key Concepts:
- **Variables** don't need type declaration in Python
- **Strings**: Text data enclosed in quotes
- **Numbers**: Integers (int) and floating-point numbers (float)
- **Booleans**: True or False values

See `examples/01_variables_and_datatypes.py` for code examples.

## Basic Operators

Python supports various operators for calculations and comparisons:
- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`

See `examples/02_operators.py` for code examples.

## Print Statements

The `print()` function displays output to the console.

See `examples/03_print_statements.py` for code examples.

## Comments & Code Structure

Comments help document your code:
- **Single-line comments**: Start with `#`
- **Multi-line comments**: Use triple quotes `"""` or `'''`

See `examples/04_comments_and_structure.py` for code examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_variables.py`
- `exercise_02_calculations.py`
- `exercise_03_personal_info.py`

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Setting up Python and your IDE
- Creating and using variables
- Working with different data types
- Using basic operators
- Writing print statements
- Documenting code with comments

Move on to Lecture 2 when you're ready!
