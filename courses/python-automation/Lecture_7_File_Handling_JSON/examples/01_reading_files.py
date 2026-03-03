"""
Lecture 7 - Example 1: Reading Files
===================================
Learn different ways to read files in Python.
"""

from pathlib import Path

# Get the path to sample data
sample_data_dir = Path(__file__).parent.parent / "sample_data"
sample_file = sample_data_dir / "sample.txt"

print("=" * 60)
print("READING FILES IN PYTHON")
print("=" * 60)
print()

# 1. READ ENTIRE FILE AT ONCE
# ===========================

print("1. Read entire file:")
print()

with open(sample_file, 'r') as f:
    content = f.read()
    print(content)

print("-" * 60)


# 2. READ LINE BY LINE
# ====================

print("2. Read line by line:")
print()

with open(sample_file, 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"Line {line_num}: {line.strip()}")

print()
print("-" * 60)


# 3. READ ALL LINES INTO A LIST
# =============================

print("3. Read all lines into a list:")
print()

with open(sample_file, 'r') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")
    print(f"Last line: {lines[-1].strip()}")

print()
print("-" * 60)


# 4. READ SPECIFIC NUMBER OF CHARACTERS
# =====================================

print("4. Read specific number of characters:")
print()

with open(sample_file, 'r') as f:
    first_50_chars = f.read(50)
    print(f"First 50 characters:")
    print(first_50_chars)

print()
print("-" * 60)


# 5. READ ONE LINE AT A TIME
# ===========================

print("5. Read one line at a time with readline():")
print()

with open(sample_file, 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")
    print(f"Line 3: {line3.strip()}")

print()
print("-" * 60)


# 6. CHECK IF FILE EXISTS BEFORE READING
# ======================================

print("6. Check if file exists:")
print()

if sample_file.exists():
    print(f"✅ File exists: {sample_file.name}")
    with open(sample_file, 'r') as f:
        line_count = len(f.readlines())
        print(f"   Lines in file: {line_count}")
else:
    print(f"❌ File not found: {sample_file}")

print()
print("-" * 60)


# 7. HANDLING FILE NOT FOUND
# ===========================

print("7. Handling file not found:")
print()

try:
    with open("nonexistent_file.txt", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("❌ Error: File does not exist!")
    print("   Always check if file exists before reading")

print()
print("-" * 60)


# 8. READING WITH DIFFERENT ENCODINGS
# ===================================

print("8. Specifying encoding:")
print()

# UTF-8 is the default and recommended encoding
with open(sample_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Read {len(content)} characters with UTF-8 encoding")

print()
print("-" * 60)


# 9. STRIP WHITESPACE FROM LINES
# ===============================

print("9. Strip whitespace from lines:")
print()

with open(sample_file, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
    print("Non-empty lines:")
    for i, line in enumerate(lines, 1):
        print(f"  {i}. {line}")

print()
print("-" * 60)


# 10. PRACTICAL AUTOMATION EXAMPLE
# =================================

print("10. Automation example - Read test data:")
print()

# Simulate reading test URLs from a file
test_urls_file = sample_data_dir.parent / "examples" / "test_urls.txt"

# Create a sample URLs file for demonstration
test_urls_content = """https://example.com/login
https://example.com/dashboard
https://example.com/profile
https://example.com/settings
"""

# For this example, we'll just demonstrate the pattern
print("Reading test URLs from file:")
print("```python")
print("with open('test_urls.txt', 'r') as f:")
print("    urls = [line.strip() for line in f if line.strip()]")
print("    for url in urls:")
print("        page.goto(url)")
print("        # Run tests on this URL")
print("```")

print()
print("=" * 60)
print("Example complete! You've learned how to read files.")
print("=" * 60)
