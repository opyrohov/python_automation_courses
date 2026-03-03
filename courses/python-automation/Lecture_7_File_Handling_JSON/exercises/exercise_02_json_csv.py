"""
Lecture 7 - Exercise 2: JSON and CSV
===================================
Practice working with JSON and CSV files.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_02_json_csv.py
3. Check your solutions against SOLUTIONS.md
"""

import json
import csv
from pathlib import Path

# Create output directory
output_dir = Path(__file__).parent / "my_output"
output_dir.mkdir(exist_ok=True)

print("=" * 50)
print("EXERCISE: JSON and CSV")
print("=" * 50)
print()

# Exercise 2.1: Create JSON File
# ==============================
# TODO: Create a dictionary with your name, age, and favorite language
# Save it to "my_info.json" with proper indentation

# Your code here:


print("-" * 50)


# Exercise 2.2: Read and Modify JSON
# ==================================
# TODO: Read my_info.json, add a new field "city" with your city
# Save the updated data back to the file

# Your code here:


print("-" * 50)


# Exercise 2.3: Create Test Users JSON
# ====================================
# TODO: Create a JSON file "test_users.json" with a list of 3 test users
# Each user should have: username, email, password, active (boolean)

# Your code here:


print("-" * 50)


# Exercise 2.4: Filter JSON Data
# ==============================
# TODO: Read test_users.json and print only the active users

# Your code here:


print("-" * 50)


# Exercise 2.5: Create CSV File
# =============================
# TODO: Create a CSV file "products.csv" with columns: id, name, price
# Add at least 3 products

# Your code here:


print("-" * 50)


# Exercise 2.6: Read CSV File
# ===========================
# TODO: Read products.csv and print each product's name and price

# Your code here:


print("-" * 50)


# Exercise 2.7: Write Test Results to CSV
# =======================================
# TODO: Create a CSV file "test_results.csv" with columns:
# test_name, status, duration
# Write 3 test results

# Your code here:


print("-" * 50)


# Exercise 2.8: Append to CSV
# ===========================
# TODO: Append a new test result to test_results.csv

# Your code here:


print("-" * 50)


# BONUS: JSON to CSV Conversion
# =============================
# TODO: Read test_users.json and convert it to users.csv

# Your code here:


print("=" * 50)
print("Exercise 2 Complete!")
print("=" * 50)
