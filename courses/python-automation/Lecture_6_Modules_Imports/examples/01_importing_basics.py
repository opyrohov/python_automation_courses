"""
Lecture 6 - Example 1: Importing Basics
======================================
Learn different ways to import modules in Python.
"""

# 1. IMPORT ENTIRE MODULE
# =======================

import math

print("1. Import entire module:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print()

print("-" * 50)


# 2. IMPORT SPECIFIC FUNCTION
# ============================

from math import sqrt

print("2. Import specific function:")
print(f"Square root of 25: {sqrt(25)}")
# Note: We can use sqrt() directly without math. prefix
print()

print("-" * 50)


# 3. IMPORT MULTIPLE ITEMS
# ========================

from math import sqrt, pi, ceil, floor

print("3. Import multiple items:")
print(f"Square root: {sqrt(36)}")
print(f"Pi: {pi}")
print(f"Ceiling of 4.7: {ceil(4.7)}")
print(f"Floor of 4.7: {floor(4.7)}")
print()

print("-" * 50)


# 4. IMPORT WITH ALIAS
# ====================

import datetime as dt

print("4. Import with alias:")
current_time = dt.datetime.now()
print(f"Current time: {current_time}")
print(f"Today's date: {dt.date.today()}")
print()

print("-" * 50)


# 5. IMPORT SPECIFIC ITEM WITH ALIAS
# ==================================

from datetime import datetime as dt_now

print("5. Import item with alias:")
print(f"Now: {dt_now.now()}")
print()

print("-" * 50)


# 6. COMMON IMPORT PATTERNS
# =========================

# Pattern 1: Import commonly used items
from random import randint, choice, shuffle

print("6. Common patterns:")
print(f"Random number 1-10: {randint(1, 10)}")
print(f"Random choice: {choice(['apple', 'banana', 'cherry'])}")

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(f"Shuffled list: {numbers}")
print()

print("-" * 50)


# 7. IMPORT FROM SUBMODULES
# =========================

from os import path
from datetime import datetime, timedelta

print("7. Import from submodules:")
print(f"Current working directory exists: {path.exists('.')}")

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(f"Today: {today.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print()

print("-" * 50)


# 8. VIEWING MODULE CONTENTS
# ==========================

import random

print("8. Viewing module contents:")
print(f"Module name: {random.__name__}")
print(f"Module file location: {random.__file__}")

# List some available functions (first 10)
available_items = [item for item in dir(random) if not item.startswith('_')]
print(f"Some available functions: {available_items[:10]}")
print()

print("-" * 50)


# 9. CHECKING WHAT'S IMPORTED
# ===========================

import sys

print("9. Checking imported modules:")
# Show first 5 imported modules
imported_modules = list(sys.modules.keys())[:5]
print(f"First 5 imported modules: {imported_modules}")
print()

print("-" * 50)


# 10. IMPORTING FROM PARENT DIRECTORY (PREVIEW)
# =============================================

# This is a preview - we'll use this pattern in real projects
# from ..utils import helpers
# from ..pages import login_page

print("10. Import patterns for test projects:")
print("# For page objects:")
print("from pages.login_page import LoginPage")
print()
print("# For utilities:")
print("from utils.helpers import wait_for_element")
print()
print("# For config:")
print("from config.settings import BASE_URL, TIMEOUT")
print()

print("-" * 50)


# 11. AUTOMATION EXAMPLE - COMMON TEST IMPORTS
# ============================================

print("11. Common imports for automation testing:")
print()

# These are the imports you'd typically see at the top of test files
example_imports = """
# Standard library imports
import time
import json
from datetime import datetime
from pathlib import Path

# Testing framework
import pytest

# Playwright imports
from playwright.sync_api import Page, expect, sync_playwright

# Your custom modules
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.test_helpers import take_screenshot, log_test_step
from config.test_data import TEST_USERS, BASE_URL
"""

print(example_imports)

print("-" * 50)


# 12. IMPORT BEST PRACTICES
# =========================

print("12. Import best practices:")
print()
print("✅ DO:")
print("  - Import standard library first")
print("  - Then third-party libraries")
print("  - Then your own modules")
print("  - Use specific imports when possible")
print("  - Use aliases for long module names")
print()
print("❌ DON'T:")
print("  - Use 'from module import *' (imports everything)")
print("  - Create circular imports")
print("  - Import in the middle of code")
print("  - Use confusing aliases")
print()

print("=" * 50)
print("Example complete! You've learned the basics of importing.")
print("=" * 50)
