"""
Lecture 7 - Exercise 3: Automation File Handling
===============================================
Practice file handling patterns for test automation.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_03_automation_files.py
3. Check your solutions against SOLUTIONS.md
"""

import json
import csv
from pathlib import Path
from datetime import datetime

# Create necessary directories
output_dir = Path(__file__).parent / "my_output"
config_dir = output_dir / "config"
results_dir = output_dir / "results"

output_dir.mkdir(exist_ok=True)
config_dir.mkdir(exist_ok=True)
results_dir.mkdir(exist_ok=True)

print("=" * 50)
print("EXERCISE: Automation File Handling")
print("=" * 50)
print()

# Exercise 3.1: Create Test Configuration
# =======================================
# TODO: Create a JSON configuration file with:
# - base_url
# - browser_type
# - headless (boolean)
# - timeout (number)
# Save to config/test_config.json

# Your code here:


print("-" * 50)


# Exercise 3.2: Load and Use Configuration
# ========================================
# TODO: Read the configuration file and print all settings

# Your code here:


print("-" * 50)


# Exercise 3.3: Create Test Data CSV
# ==================================
# TODO: Create a CSV file with test login scenarios:
# Columns: scenario, username, password, expected_result
# Add at least 4 scenarios (valid, invalid password, empty fields, etc.)

# Your code here:


print("-" * 50)


# Exercise 3.4: Run Data-Driven Test
# ==================================
# TODO: Read the test scenarios CSV and simulate running each test
# Print: "Testing [scenario]: [expected_result]"

# Your code here:


print("-" * 50)


# Exercise 3.5: Save Test Results
# ===============================
# TODO: Create a function save_test_results(test_name, passed, failed)
# that saves results to a JSON file with timestamp

# Your code here:


print("-" * 50)


# Exercise 3.6: Generate Test Report CSV
# ======================================
# TODO: Create a function that generates a CSV report with:
# timestamp, test_suite, total, passed, failed, success_rate

# Your code here:


print("-" * 50)


# Exercise 3.7: Create Log Writer
# ===============================
# TODO: Create a function log_test_step(step, level="INFO")
# that writes to test_execution.log with timestamp and level

# Your code here:


print("-" * 50)


# Exercise 3.8: Load Test Users Helper
# ====================================
# TODO: Create a function load_test_users(json_file)
# that returns only active users from a JSON file

# Your code here:


print("-" * 50)


# BONUS: Complete Test Suite Helper
# =================================
# TODO: Create a class TestDataManager with methods:
# - load_config(file)
# - load_test_cases(file)
# - save_results(data, file)

# Your code here:


print("=" * 50)
print("Exercise 3 Complete!")
print("You've mastered file handling for automation!")
print("=" * 50)
