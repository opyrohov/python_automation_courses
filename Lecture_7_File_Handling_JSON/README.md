# Lecture 7: File Handling & JSON

Welcome to the seventh lecture of the Python Automation Course! In this lecture, you'll learn how to read and write files, work with JSON data, and handle CSV files - essential skills for managing test data and configurations in automation.

## Table of Contents
1. [Reading Text Files](#reading-text-files)
2. [Writing Text Files](#writing-text-files)
3. [File Modes and Context Managers](#file-modes-and-context-managers)
4. [Working with JSON](#working-with-json)
5. [CSV File Handling](#csv-file-handling)
6. [Working with Paths](#working-with-paths)
7. [Why This Matters for Playwright](#why-this-matters-for-playwright)
8. [Practice Exercises](#practice-exercises)

## Reading Text Files

Learn different ways to read files in Python.

### Key Concepts:
- **open() function**: Opens a file and returns a file object
- **read()**: Read entire file content
- **readline()**: Read one line at a time
- **readlines()**: Read all lines into a list
- **File paths**: Absolute vs relative paths
- **Encoding**: UTF-8 and other encodings
- **Error handling**: What to do when file doesn't exist

See `examples/01_reading_files.py` for code examples.

## Writing Text Files

Create and modify files programmatically.

### Key Concepts:
- **Writing modes**: 'w', 'a', 'x'
- **write()**: Write string to file
- **writelines()**: Write list of strings
- **Overwriting vs appending**: Different modes
- **Creating new files**: When to use 'x' mode
- **Best practices**: Always close files or use context managers

See `examples/02_writing_files.py` for code examples.

## File Modes and Context Managers

Understand file modes and the proper way to handle files.

### Key Concepts:
- **File modes**: 'r', 'w', 'a', 'r+', 'w+', 'a+'
- **Context managers**: Using `with` statement
- **Automatic cleanup**: Why `with` is better
- **Binary mode**: Reading images, PDFs, etc.
- **File object methods**: seek(), tell(), flush()

See `examples/03_file_modes.py` for code examples.

## Working with JSON

JSON is the standard format for configuration and test data.

### Key Concepts:
- **JSON structure**: Objects (dicts) and arrays (lists)
- **json.loads()**: Parse JSON string to Python
- **json.dumps()**: Convert Python to JSON string
- **json.load()**: Read JSON from file
- **json.dump()**: Write JSON to file
- **Pretty printing**: Using indent parameter
- **Handling nested data**: Complex JSON structures

See `examples/04_json_handling.py` for code examples.

## CSV File Handling

CSV files are common for test data and reports.

### Key Concepts:
- **csv module**: Python's built-in CSV handler
- **csv.reader()**: Read CSV files
- **csv.writer()**: Write CSV files
- **DictReader**: Read CSV as dictionaries
- **DictWriter**: Write dictionaries to CSV
- **Headers**: Managing column names
- **Delimiters**: Comma, tab, semicolon, etc.

See `examples/05_csv_handling.py` for code examples.

## Working with Paths

Modern file path handling with pathlib.

### Key Concepts:
- **Path object**: Object-oriented paths
- **Path operations**: join, parts, parent, stem, suffix
- **Existence checks**: exists(), is_file(), is_dir()
- **Creating directories**: mkdir(), makedirs()
- **Listing files**: glob(), iterdir()
- **Cross-platform**: Works on Windows, Mac, Linux

See `examples/06_path_operations.py` for code examples.

## Why This Matters for Playwright

File handling is crucial for managing test data, configurations, and reports in automation.

### Test Data Management:
- **JSON files**: Store user credentials, test scenarios
- **CSV files**: Data-driven testing with multiple test cases
- **Configuration files**: Environment settings, URLs, timeouts
- **Test reports**: Generate custom test result files
- **Screenshots**: Save and organize test artifacts
- **Logs**: Write detailed test execution logs

### Common Automation Patterns:
```python
# Load test users from JSON
with open('test_data/users.json') as f:
    test_users = json.load(f)

# Read test cases from CSV
import csv
with open('test_cases.csv') as f:
    reader = csv.DictReader(f)
    for test_case in reader:
        run_test(test_case)

# Save test results
results = {'passed': 45, 'failed': 3}
with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

### Project Structure with Files:
```
test_project/
├── tests/
│   └── test_login.py
├── test_data/
│   ├── users.json           # Test user credentials
│   ├── test_cases.csv       # Test scenarios
│   └── expected_results.json
├── config/
│   ├── dev_config.json      # Dev environment
│   ├── staging_config.json  # Staging environment
│   └── prod_config.json     # Production environment
├── reports/                 # Generated test reports
│   └── test_report.json
└── logs/                    # Test execution logs
    └── test.log
```

See `examples/07_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_file_basics.py` - Reading and writing files
- `exercise_02_json_csv.py` - Working with JSON and CSV
- `exercise_03_automation_files.py` - File handling for automation

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Quick Reference

### Reading Files
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read lines
with open('file.txt', 'r') as f:
    lines = f.readlines()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### Writing Files
```python
# Write (overwrite)
with open('file.txt', 'w') as f:
    f.write('Hello, World!')

# Append
with open('file.txt', 'a') as f:
    f.write('New line\n')
```

### JSON
```python
import json

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON
data = {'name': 'Alice', 'age': 25}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Parse JSON string
json_str = '{"name": "Bob"}'
data = json.loads(json_str)

# Convert to JSON string
json_str = json.dumps(data, indent=2)
```

### CSV
```python
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['email'])

# Write CSV
data = [
    {'name': 'Alice', 'email': 'alice@example.com'},
    {'name': 'Bob', 'email': 'bob@example.com'}
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'email'])
    writer.writeheader()
    writer.writerows(data)
```

### Paths
```python
from pathlib import Path

# Current file location
current_file = Path(__file__)
project_root = current_file.parent.parent

# Build paths
data_file = project_root / 'test_data' / 'users.json'

# Check existence
if data_file.exists():
    print(f"File exists: {data_file}")

# Create directory
screenshots_dir = Path('screenshots')
screenshots_dir.mkdir(exist_ok=True)
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Reading and writing text files
- Working with JSON data for configuration
- Handling CSV files for test data
- Using pathlib for file operations
- Organizing test data files
- Implementing data-driven testing patterns

Move on to Lecture 8 when you're ready to start hands-on Playwright automation!
