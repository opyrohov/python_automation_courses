"""
Lecture 7 - Example 4: CSV Handling
==================================
Learn how to work with CSV files in Python.
"""

import csv
from pathlib import Path

# Paths
sample_data_dir = Path(__file__).parent.parent / "sample_data"
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

print("=" * 60)
print("WORKING WITH CSV FILES IN PYTHON")
print("=" * 60)
print()

# 1. READING CSV FILE
# ===================

print("1. Read CSV file:")
print()

test_cases_file = sample_data_dir / "test_cases.csv"

with open(test_cases_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    print(f"Columns: {', '.join(header)}")
    print()

    for row in reader:
        print(f"  Test {row[0]}: {row[1]} - Expected: {row[4]}")

print()
print("-" * 60)


# 2. READING CSV AS DICTIONARIES
# ==============================

print("2. Read CSV as dictionaries (DictReader):")
print()

with open(test_cases_file, 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"Test: {row['test_name']}")
        print(f"  Username: {row['username']}")
        print(f"  Expected: {row['expected_result']}")
        print()

print("-" * 60)


# 3. WRITING CSV FILE
# ===================

print("3. Write CSV file:")
print()

output_file = output_dir / "test_results.csv"

results = [
    ['test_id', 'test_name', 'status', 'duration'],
    ['1', 'test_login', 'passed', '2.3s'],
    ['2', 'test_signup', 'passed', '3.1s'],
    ['3', 'test_logout', 'failed', '1.5s']
]

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results)

print(f"✅ CSV file created: {output_file.name}")

print()
print("-" * 60)


# 4. WRITING WITH DICTWRITER
# ==========================

print("4. Write CSV with DictWriter:")
print()

test_users = [
    {'username': 'alice', 'email': 'alice@test.com', 'role': 'user'},
    {'username': 'bob', 'email': 'bob@test.com', 'role': 'admin'},
    {'username': 'charlie', 'email': 'charlie@test.com', 'role': 'user'}
]

users_file = output_dir / "test_users.csv"

with open(users_file, 'w', newline='') as f:
    fieldnames = ['username', 'email', 'role']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(test_users)

print(f"✅ Users CSV created: {users_file.name}")
print(f"   Total users: {len(test_users)}")

print()
print("-" * 60)


# 5. DATA-DRIVEN TESTING PATTERN
# ==============================

print("5. Data-driven testing pattern:")
print()

def run_login_test(username, password, expected):
    """Simulate running a login test."""
    print(f"  Testing: {username}")
    print(f"  Expected: {expected}")
    # In real test: page.fill('#username', username), etc.
    print(f"  ✅ Test executed")

print("Running tests from CSV:")
with open(test_cases_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        run_login_test(
            row['username'],
            row['password'],
            row['expected_result']
        )
        print()

print("-" * 60)


# 6. APPEND TO CSV
# ================

print("6. Append new results to CSV:")
print()

new_result = ['4', 'test_search', 'passed', '1.8s']

with open(output_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_result)

print(f"✅ New result appended to: {output_file.name}")

print()
print("-" * 60)


# 7. GENERATE TEST REPORT CSV
# ===========================

print("7. Generate test report CSV:")
print()

from datetime import datetime

report_data = [
    {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'test_suite': 'Login Tests',
        'total': 10,
        'passed': 8,
        'failed': 2,
        'success_rate': '80%'
    }
]

report_file = output_dir / "test_report.csv"

with open(report_file, 'w', newline='') as f:
    fieldnames = ['timestamp', 'test_suite', 'total', 'passed', 'failed', 'success_rate']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(report_data)

print(f"✅ Report generated: {report_file.name}")

print()
print("=" * 60)
print("Example complete! You've mastered CSV handling.")
print("=" * 60)
