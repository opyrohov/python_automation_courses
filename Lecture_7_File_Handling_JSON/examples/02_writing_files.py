"""
Lecture 7 - Example 2: Writing Files
===================================
Learn how to create and write to files.
"""

from pathlib import Path

# Create output directory for examples
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

print("=" * 60)
print("WRITING FILES IN PYTHON")
print("=" * 60)
print()

# 1. WRITE TO A FILE (OVERWRITE)
# ===============================

print("1. Write to file (overwrite mode 'w'):")
print()

output_file = output_dir / "example_output.txt"

with open(output_file, 'w') as f:
    f.write("Hello, Python File Handling!\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")

print(f"✅ File created: {output_file.name}")
print("   Mode 'w' overwrites existing content")
print()

# Read back to verify
with open(output_file, 'r') as f:
    print("File content:")
    print(f.read())

print("-" * 60)


# 2. APPEND TO A FILE
# ===================

print("2. Append to file (mode 'a'):")
print()

with open(output_file, 'a') as f:
    f.write("This line was appended!\n")
    f.write("And so was this one!\n")

print(f"✅ Content appended to: {output_file.name}")
print()

with open(output_file, 'r') as f:
    print("Updated file content:")
    print(f.read())

print("-" * 60)


# 3. WRITE MULTIPLE LINES AT ONCE
# ================================

print("3. Write multiple lines with writelines():")
print()

lines = [
    "Line 1: Test automation\n",
    "Line 2: File handling\n",
    "Line 3: Data management\n"
]

multiline_file = output_dir / "multiple_lines.txt"
with open(multiline_file, 'w') as f:
    f.writelines(lines)

print(f"✅ File created: {multiline_file.name}")
print()

print("-" * 60)


# 4. WRITE WITH f-strings
# =======================

print("4. Write with formatted strings:")
print()

test_results_file = output_dir / "test_results.txt"

test_name = "Login Test"
passed = 45
failed = 3
total = passed + failed

with open(test_results_file, 'w') as f:
    f.write(f"Test Report: {test_name}\n")
    f.write("=" * 40 + "\n")
    f.write(f"Passed: {passed}\n")
    f.write(f"Failed: {failed}\n")
    f.write(f"Total: {total}\n")
    f.write(f"Success Rate: {(passed/total)*100:.1f}%\n")

print(f"✅ Report created: {test_results_file.name}")
print()

with open(test_results_file, 'r') as f:
    print(f.read())

print("-" * 60)


# 5. CREATE FILE ONLY IF IT DOESN'T EXIST (mode 'x')
# ==================================================

print("5. Exclusive creation with mode 'x':")
print()

new_file = output_dir / "new_file.txt"

try:
    with open(new_file, 'x') as f:
        f.write("This file was created with mode 'x'\n")
    print(f"✅ New file created: {new_file.name}")
except FileExistsError:
    print(f"⚠️  File already exists: {new_file.name}")
    print("   Mode 'x' prevents overwriting")

print()
print("-" * 60)


# 6. WRITE LOG FILE
# =================

print("6. Write log file example:")
print()

from datetime import datetime

log_file = output_dir / "test_log.txt"

def log_message(message, level="INFO"):
    """Write a log message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"

    with open(log_file, 'a') as f:
        f.write(log_entry)

# Write some log messages
log_message("Test execution started", "INFO")
log_message("Browser launched successfully", "INFO")
log_message("Login test passed", "SUCCESS")
log_message("Screenshot saved", "INFO")

print(f"✅ Log file created: {log_file.name}")
print()

with open(log_file, 'r') as f:
    print("Log contents:")
    print(f.read())

print("-" * 60)


# 7. WRITE TEST REPORT
# ====================

print("7. Generate test report:")
print()

report_file = output_dir / "detailed_report.txt"

test_results = [
    {"name": "test_login", "status": "PASSED", "duration": "2.3s"},
    {"name": "test_signup", "status": "PASSED", "duration": "3.1s"},
    {"name": "test_logout", "status": "FAILED", "duration": "1.5s"},
]

with open(report_file, 'w') as f:
    f.write("=" * 50 + "\n")
    f.write("TEST EXECUTION REPORT\n")
    f.write("=" * 50 + "\n\n")

    for test in test_results:
        f.write(f"Test: {test['name']}\n")
        f.write(f"  Status: {test['status']}\n")
        f.write(f"  Duration: {test['duration']}\n")
        f.write("-" * 50 + "\n")

    passed = sum(1 for t in test_results if t['status'] == 'PASSED')
    f.write(f"\nSummary: {passed}/{len(test_results)} tests passed\n")

print(f"✅ Report generated: {report_file.name}")
print()

print("-" * 60)


# 8. SAVE TEST DATA
# =================

print("8. Save test data to file:")
print()

test_data_file = output_dir / "test_users.txt"

test_users = [
    "testuser1@example.com:Test123!",
    "testuser2@example.com:Test456!",
    "admin@example.com:Admin789!"
]

with open(test_data_file, 'w') as f:
    for user in test_users:
        f.write(user + "\n")

print(f"✅ Test data saved: {test_data_file.name}")
print(f"   Total users: {len(test_users)}")
print()

print("=" * 60)
print("Example complete! You've learned how to write files.")
print("=" * 60)
print()
print(f"All output files saved to: {output_dir}")
