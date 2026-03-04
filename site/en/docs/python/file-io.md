# File I/O

Reading, writing, and processing files in Python is an essential skill for QA automation. This page covers working with text files, CSV, JSON, and file paths.

## Opening Files: open()

The `open()` function is the primary way to work with files in Python.

```python
# Basic file opening
file = open("data.txt", "r")
content = file.read()
file.close()  # Always close the file!
```

::: warning Always close your files!
If you don't close a file, it may lead to memory leaks and file locks. Use `with` for automatic closing.
:::

### Context Manager (with)

The recommended way to work with files is the `with` statement. The file is automatically closed when you exit the block.

```python
# Recommended approach — file closes automatically
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# After exiting the with block, the file is already closed
print(file.closed)  # True
```

::: tip Rule
Always use `with open(...)` instead of `open()` + `close()`. It is safer and cleaner.
:::

## File Modes

| Mode | Description | File exists | File doesn't exist |
|------|-------------|-------------|-------------------|
| `"r"` | Read (default) | Reads | `FileNotFoundError` |
| `"w"` | Write (overwrites) | Overwrites | Creates new |
| `"a"` | Append to end | Appends | Creates new |
| `"r+"` | Read + Write | Reads/writes | `FileNotFoundError` |
| `"x"` | Exclusive creation | `FileExistsError` | Creates new |
| `"b"` | Binary mode (add to others) | — | — |

```python
# Mode combinations
with open("image.png", "rb") as f:    # Read binary file
    data = f.read()

with open("output.bin", "wb") as f:   # Write binary file
    f.write(data)
```

## Reading Files

### read() — entire content

```python
with open("test_data.txt", "r", encoding="utf-8") as file:
    content = file.read()       # Entire content as a single string
    print(content)

# Partial read
with open("large_file.txt", "r") as file:
    chunk = file.read(100)      # First 100 characters
```

### readline() — single line

```python
with open("test_data.txt", "r") as file:
    first_line = file.readline()    # First line
    second_line = file.readline()   # Second line
    print(first_line.strip())       # .strip() removes \n
```

### readlines() — list of lines

```python
with open("test_data.txt", "r") as file:
    lines = file.readlines()        # List of all lines
    print(lines)                    # ['line 1\n', 'line 2\n', ...]

# Removing newline characters
with open("test_data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    print(lines)                    # ['line 1', 'line 2', ...]
```

### Iterating over a file

```python
# Most efficient approach for large files
with open("server.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
```

::: info QA Example: finding errors in logs
```python
def find_errors_in_log(log_path):
    """Find all error lines in a log file."""
    errors = []
    with open(log_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            if "ERROR" in line or "CRITICAL" in line:
                errors.append(f"Line {line_num}: {line.strip()}")
    return errors

# Usage
errors = find_errors_in_log("app.log")
for error in errors:
    print(error)
```
:::

## Writing Files

### write() — write a string

```python
# Write (overwrites the file)
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Test Report\n")
    file.write("=" * 30 + "\n")
    file.write(f"Date: 2024-01-15\n")
```

### writelines() — write a list of strings

```python
lines = ["Test 1: PASSED\n", "Test 2: FAILED\n", "Test 3: PASSED\n"]

with open("results.txt", "w") as file:
    file.writelines(lines)    # Writes all lines without adding \n
```

::: warning writelines() does not add newlines
Unlike `readlines()`, the `writelines()` method does NOT add `\n` automatically. You must include newlines yourself.
:::

### Appending to a file

```python
# Mode "a" — appends to the end, does not overwrite
with open("test.log", "a", encoding="utf-8") as file:
    file.write("[2024-01-15 10:30:00] Test started\n")
    file.write("[2024-01-15 10:30:05] Test passed\n")
```

::: info QA Example: writing a test report
```python
def write_test_report(results, report_path="test_report.txt"):
    """Create a text report with test results."""
    passed = sum(1 for r in results if r["status"] == "PASSED")
    failed = sum(1 for r in results if r["status"] == "FAILED")
    total = len(results)

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write("        TEST REPORT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Total tests:  {total}\n")
        file.write(f"Passed:       {passed}\n")
        file.write(f"Failed:       {failed}\n")
        file.write(f"Pass rate:    {passed/total*100:.1f}%\n\n")

        file.write("-" * 50 + "\n")
        for r in results:
            icon = "+" if r["status"] == "PASSED" else "x"
            file.write(f"  {icon} {r['name']} — {r['status']}\n")

# Usage
results = [
    {"name": "test_login", "status": "PASSED"},
    {"name": "test_logout", "status": "PASSED"},
    {"name": "test_register", "status": "FAILED"},
]
write_test_report(results)
```
:::

## Working with Paths: os.path

The `os.path` module is the classic way to handle file paths.

```python
import os

# Building paths (cross-platform)
path = os.path.join("tests", "data", "users.json")
# Windows: tests\data\users.json
# Linux:   tests/data/users.json

# Useful functions
print(os.path.exists("config.json"))    # True/False — does the file exist
print(os.path.isfile("config.json"))    # True/False — is it a file
print(os.path.isdir("tests"))           # True/False — is it a directory
print(os.path.basename("/home/user/test.py"))  # "test.py"
print(os.path.dirname("/home/user/test.py"))   # "/home/user"
print(os.path.splitext("report.html"))         # ("report", ".html")
print(os.path.abspath("data.txt"))             # Absolute path

# Current directory
print(os.getcwd())                      # Current working directory
```

## Working with Paths: pathlib.Path

The `pathlib` module is the modern and more convenient way to work with paths (Python 3.4+).

```python
from pathlib import Path

# Creating paths
path = Path("tests") / "data" / "users.json"
print(path)  # tests/data/users.json

# Path properties
print(path.name)       # "users.json"
print(path.stem)       # "users"
print(path.suffix)     # ".json"
print(path.parent)     # tests/data
print(path.exists())   # True/False
print(path.is_file())  # True/False
print(path.is_dir())   # False

# Reading and writing via Path
content = Path("data.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("Hello!", encoding="utf-8")

# Finding files
for py_file in Path("tests").glob("*.py"):
    print(py_file)

# Recursive search
for json_file in Path("project").rglob("*.json"):
    print(json_file)
```

::: tip pathlib vs os.path
It is recommended to use `pathlib.Path` in new projects. It is more readable and supports the `/` operator for building paths.
:::

::: info QA Example: finding test files
```python
from pathlib import Path

def find_test_files(test_dir="tests"):
    """Find all test files in a directory."""
    test_path = Path(test_dir)
    if not test_path.exists():
        print(f"Directory {test_dir} not found")
        return []

    test_files = list(test_path.rglob("test_*.py"))
    print(f"Found {len(test_files)} test files:")
    for f in test_files:
        print(f"  - {f}")
    return test_files

find_test_files()
```
:::

## Working with CSV

The `csv` module allows you to read and write CSV files (Comma-Separated Values).

### Reading CSV

```python
import csv

# Reading as a list of rows
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)       # First row — headers
    for row in reader:
        print(row)              # ['John', '25', 'admin']

# Reading as dictionaries
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])  # Access by column name
```

### Writing CSV

```python
import csv

# Writing lists
with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["test_name", "status", "duration"])    # Header
    writer.writerow(["test_login", "PASSED", "1.23"])
    writer.writerow(["test_register", "FAILED", "3.45"])

# Writing dictionaries
with open("results.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["test_name", "status", "duration"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"test_name": "test_login", "status": "PASSED", "duration": "1.23"})
```

::: warning The newline="" parameter
When writing CSV on Windows, always specify `newline=""` to avoid double blank lines.
:::

::: info QA Example: loading test data from CSV
```python
import csv

def load_test_data(csv_path):
    """Load test data from CSV for parameterized tests."""
    test_data = []
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(row)
    return test_data

# File test_users.csv:
# username,password,expected_result
# admin,Admin123!,success
# user,wrong_pass,failure
# ,empty_pass,failure

test_cases = load_test_data("test_users.csv")
for case in test_cases:
    print(f"Login: {case['username']} | Expected: {case['expected_result']}")

# Usage with pytest parametrize
import pytest

def get_login_data():
    return load_test_data("test_users.csv")

@pytest.mark.parametrize("test_data", get_login_data())
def test_login(test_data):
    username = test_data["username"]
    password = test_data["password"]
    expected = test_data["expected_result"]
    # ... execute test
```
:::

## Working with JSON

The `json` module allows you to work with JSON format — the most common data exchange format in APIs.

### Reading JSON from a file

```python
import json

# json.load() — read from a file
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
    print(config["base_url"])
    print(config["timeout"])
```

### Writing JSON to a file

```python
import json

data = {
    "base_url": "https://example.com",
    "timeout": 30,
    "users": [
        {"name": "admin", "role": "admin"},
        {"name": "user1", "role": "viewer"}
    ]
}

# json.dump() — write to a file
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
```

### Working with JSON strings

```python
import json

# json.loads() — parse a string (string → dict/list)
json_string = '{"name": "Test", "passed": true, "score": 95.5}'
data = json.loads(json_string)
print(data["name"])     # "Test"
print(data["passed"])   # True (Python bool)

# json.dumps() — serialize (dict/list → string)
result = {"status": "ok", "count": 42}
json_string = json.dumps(result, indent=2)
print(json_string)
```

::: tip load vs loads, dump vs dumps
- `json.load()` / `json.dump()` — work with **files**
- `json.loads()` / `json.dumps()` — work with **strings** (s = string)
:::

::: info QA Example: loading configuration from JSON
```python
import json
from pathlib import Path

def load_config(config_path="config.json"):
    """Load test environment configuration."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file {config_path} not found")

    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    # Validate required fields
    required_fields = ["base_url", "timeout", "browser"]
    for field in required_fields:
        if field not in config:
            raise KeyError(f"Missing required field: {field}")

    return config

# config.json:
# {
#     "base_url": "https://staging.example.com",
#     "timeout": 30,
#     "browser": "chromium",
#     "headless": true
# }

config = load_config()
print(f"URL: {config['base_url']}")
print(f"Browser: {config['browser']}")
```
:::

::: info QA Example: saving test results to JSON
```python
import json
from datetime import datetime

def save_test_results(results, output_path="test_results.json"):
    """Save test results to a JSON file."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "PASSED"),
        "failed": sum(1 for r in results if r["status"] == "FAILED"),
        "results": results
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"Results saved to {output_path}")

# Usage
results = [
    {"name": "test_login", "status": "PASSED", "duration": 1.23},
    {"name": "test_register", "status": "FAILED", "duration": 3.45,
     "error": "Element not found: #submit-btn"},
    {"name": "test_search", "status": "PASSED", "duration": 2.10},
]
save_test_results(results)
```
:::

## Error Handling with Files

```python
from pathlib import Path

# Check if file exists
path = Path("config.json")
if not path.exists():
    print("File not found!")

# try/except for error handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No access to the file!")
except UnicodeDecodeError:
    print("Encoding error — try a different encoding")
except Exception as e:
    print(f"Unexpected error: {e}")
```

::: warning Encoding
Always specify `encoding="utf-8"` when working with text files. Without it, Python uses the system encoding, which may cause errors across different operating systems.
```python
# Correct
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Risky — encoding depends on the system
with open("data.txt", "r") as f:
    content = f.read()
```
:::

## Useful Links

- [Python Docs: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Docs: csv module](https://docs.python.org/3/library/csv.html)
- [Python Docs: json module](https://docs.python.org/3/library/json.html)
- [Python Docs: pathlib](https://docs.python.org/3/library/pathlib.html)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/modules">← Modules</a>
  <a href="/python_automation_courses/en/docs/python/decorators">Decorators →</a>
</div>
