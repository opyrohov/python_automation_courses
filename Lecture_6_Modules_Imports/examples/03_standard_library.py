"""
Lecture 6 - Example 3: Python Standard Library
=============================================
Learn to use Python's built-in modules (no installation needed!).
"""

# 1. DATETIME MODULE - Working with Dates and Times
# =================================================

from datetime import datetime, timedelta, date

print("1. datetime module:")
print()

# Current date and time
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Today's date
today = date.today()
print(f"Today's date: {today}")

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Time differences
future_date = datetime(2025, 12, 31)
days_until = (future_date - now).days
print(f"Days until 2025-12-31: {days_until}")
print()

print("-" * 50)


# 2. RANDOM MODULE - Generating Random Data
# =========================================

import random

print("2. random module (perfect for test data!):")
print()

# Random integers
print(f"Random number 1-100: {random.randint(1, 100)}")
print(f"Random number 1-10: {random.randint(1, 10)}")

# Random choice from list
browsers = ["Chrome", "Firefox", "Safari", "Edge"]
print(f"Random browser: {random.choice(browsers)}")

# Random sample (multiple items)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample = random.sample(numbers, 3)
print(f"Random sample of 3: {sample}")

# Shuffle a list
test_data = ["test1", "test2", "test3", "test4"]
random.shuffle(test_data)
print(f"Shuffled tests: {test_data}")

# Random float
print(f"Random float 0-1: {random.random()}")
print(f"Random float 1-10: {random.uniform(1, 10)}")
print()

print("-" * 50)


# 3. OS MODULE - Operating System Operations
# ==========================================

import os

print("3. os module:")
print()

# Current working directory
print(f"Current directory: {os.getcwd()}")

# Environment variables
print(f"PATH exists: {os.environ.get('PATH') is not None}")
print(f"USER/USERNAME: {os.environ.get('USER') or os.environ.get('USERNAME')}")

# Check if path exists
print(f"Current dir exists: {os.path.exists('.')}")
print(f"File exists: {os.path.exists(__file__)}")

# Path operations
full_path = os.path.abspath(__file__)
directory = os.path.dirname(full_path)
filename = os.path.basename(full_path)
print(f"Full path: {full_path}")
print(f"Directory: {directory}")
print(f"Filename: {filename}")
print()

print("-" * 50)


# 4. PATHLIB MODULE - Modern Path Handling
# ========================================

from pathlib import Path

print("4. pathlib module (modern way!):")
print()

# Current file path
current_file = Path(__file__)
print(f"Current file: {current_file}")
print(f"File name: {current_file.name}")
print(f"File stem: {current_file.stem}")
print(f"File suffix: {current_file.suffix}")
print(f"Parent directory: {current_file.parent}")

# Check properties
print(f"Is file: {current_file.is_file()}")
print(f"Is directory: {current_file.is_dir()}")
print(f"Exists: {current_file.exists()}")

# Build paths
project_root = current_file.parent.parent
tests_dir = project_root / "tests"
config_file = project_root / "config" / "settings.py"
print(f"Project root: {project_root}")
print(f"Tests dir path: {tests_dir}")
print(f"Config file path: {config_file}")
print()

print("-" * 50)


# 5. JSON MODULE - Working with JSON Data
# =======================================

import json

print("5. json module:")
print()

# Python dict to JSON string
user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "age": 25,
    "active": True,
    "roles": ["user", "tester"]
}

json_string = json.dumps(user_data, indent=2)
print("Python dict to JSON:")
print(json_string)
print()

# JSON string to Python dict
json_data = '{"name": "Alice", "score": 95, "passed": true}'
parsed_data = json.loads(json_data)
print(f"JSON to Python dict: {parsed_data}")
print(f"Name: {parsed_data['name']}")
print(f"Score: {parsed_data['score']}")
print()

print("-" * 50)


# 6. TIME MODULE - Time-Related Functions
# =======================================

import time

print("6. time module:")
print()

# Current timestamp
timestamp = time.time()
print(f"Current timestamp: {timestamp}")

# Formatted time
formatted = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time: {formatted}")

# Sleep (useful for tests)
print("Sleeping for 1 second...")
time.sleep(1)
print("Done!")
print()

print("-" * 50)


# 7. MATH MODULE - Mathematical Operations
# ========================================

import math

print("7. math module:")
print()

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.2: {math.ceil(4.2)}")
print(f"Floor of 4.8: {math.floor(4.8)}")
print(f"Round 4.5: {round(4.5)}")
print(f"Absolute value of -10: {abs(-10)}")
print(f"Power: 2^8 = {math.pow(2, 8)}")
print()

print("-" * 50)


# 8. COLLECTIONS MODULE - Specialized Data Structures
# ==================================================

from collections import Counter, defaultdict

print("8. collections module:")
print()

# Counter - count occurrences
test_results = ["pass", "pass", "fail", "pass", "skip", "fail", "pass"]
result_counts = Counter(test_results)
print(f"Test results: {result_counts}")
print(f"Passed tests: {result_counts['pass']}")
print(f"Failed tests: {result_counts['fail']}")
print()

# defaultdict - dict with default values
test_scores = defaultdict(list)
test_scores["user1"].append(85)
test_scores["user1"].append(90)
test_scores["user2"].append(75)
print(f"Test scores: {dict(test_scores)}")
print()

print("-" * 50)


# 9. PRACTICAL TEST AUTOMATION EXAMPLE
# ====================================

print("9. Practical automation example:")
print()

# Generate test data
test_user = {
    "id": random.randint(1000, 9999),
    "username": f"testuser_{random.randint(100, 999)}",
    "email": f"test{random.randint(1, 100)}@example.com",
    "password": "Test123!",
    "created_at": datetime.now().isoformat(),
    "active": True
}

print("Generated test user:")
print(json.dumps(test_user, indent=2))
print()

# Create test report file path
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_dir = Path("reports")
report_file = report_dir / f"test_report_{timestamp}.json"
print(f"Report would be saved to: {report_file}")
print()

# Measure test execution time
start_time = time.time()
time.sleep(0.5)  # Simulate test
end_time = time.time()
duration = end_time - start_time
print(f"Test duration: {duration:.2f} seconds")
print()

print("-" * 50)


# 10. COMMONLY USED STANDARD LIBRARY MODULES
# ==========================================

print("10. Other useful standard library modules:")
print()

modules_info = """
✅ string - String operations and constants
✅ re - Regular expressions
✅ urllib - URL handling
✅ csv - CSV file reading/writing
✅ logging - Logging framework
✅ argparse - Command-line argument parsing
✅ subprocess - Running external commands
✅ threading - Threading operations
✅ unittest - Unit testing framework
✅ copy - Deep and shallow copy operations
"""

print(modules_info)

print("=" * 50)
print("Example complete! You've learned the standard library.")
print("=" * 50)
