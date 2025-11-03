# Lecture 7: File Handling & JSON - Exercise Solutions

This file contains solutions for all exercises in Lecture 7.

## Exercise 1: File Basics

### Exercise 1.1: Write a Simple Text File
```python
output_file = output_dir / "greeting.txt"

with open(output_file, 'w') as f:
    f.write("Hello, Python!\n")
    f.write("File handling is easy.\n")
    f.write("Let's practice!\n")

print(f"✅ File created: {output_file.name}")
```

### Exercise 1.2: Read the File You Created
```python
with open(output_file, 'r') as f:
    content = f.read()
    print(content)
```

### Exercise 1.3: Append to a File
```python
with open(output_file, 'a') as f:
    f.write("This line was added later!\n")

print("✅ Line appended")
```

### Exercise 1.4: Count Lines in a File
```python
with open(output_file, 'r') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
```

### Exercise 1.5: Write Multiple Lines
```python
languages_file = output_dir / "languages.txt"
languages = ["Python", "JavaScript", "Java", "C++", "Go"]

with open(languages_file, 'w') as f:
    for lang in languages:
        f.write(lang + "\n")

print(f"✅ File created: {languages_file.name}")
```

### Exercise 1.6: Read Specific Lines
```python
with open(languages_file, 'r') as f:
    lines = f.readlines()
    first = lines[0].strip()
    last = lines[-1].strip()
    print(f"First: {first}")
    print(f"Last: {last}")
```

### Exercise 1.7: Create a Log File
```python
from datetime import datetime

def write_log(message):
    """Write a log message with timestamp."""
    log_file = output_dir / "test.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_file, 'a') as f:
        f.write(log_entry)

write_log("Test started")
write_log("Test passed")
write_log("Test completed")

print("✅ Log file created")
```

### BONUS: File Existence Check
```python
def safe_read_file(file_path):
    """Read file only if it exists."""
    if Path(file_path).exists():
        with open(file_path, 'r') as f:
            return f.read()
    else:
        return "File not found"

# Test
print(safe_read_file(output_file))
print(safe_read_file("nonexistent.txt"))
```

---

## Exercise 2: JSON and CSV

### Exercise 2.1: Create JSON File
```python
my_info = {
    "name": "Alice",
    "age": 25,
    "favorite_language": "Python"
}

info_file = output_dir / "my_info.json"
with open(info_file, 'w') as f:
    json.dump(my_info, f, indent=2)

print(f"✅ JSON created: {info_file.name}")
```

### Exercise 2.2: Read and Modify JSON
```python
with open(info_file, 'r') as f:
    data = json.load(f)

data["city"] = "New York"

with open(info_file, 'w') as f:
    json.dump(data, f, indent=2)

print("✅ JSON updated")
```

### Exercise 2.3: Create Test Users JSON
```python
test_users = {
    "users": [
        {
            "username": "testuser1",
            "email": "test1@example.com",
            "password": "Test123!",
            "active": True
        },
        {
            "username": "testuser2",
            "email": "test2@example.com",
            "password": "Test456!",
            "active": False
        },
        {
            "username": "admin",
            "email": "admin@example.com",
            "password": "Admin789!",
            "active": True
        }
    ]
}

users_file = output_dir / "test_users.json"
with open(users_file, 'w') as f:
    json.dump(test_users, f, indent=2)

print(f"✅ Test users created: {len(test_users['users'])} users")
```

### Exercise 2.4: Filter JSON Data
```python
with open(users_file, 'r') as f:
    data = json.load(f)

active_users = [u for u in data['users'] if u['active']]
print("Active users:")
for user in active_users:
    print(f"  - {user['username']}")
```

### Exercise 2.5: Create CSV File
```python
products_file = output_dir / "products.csv"

with open(products_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'price'])
    writer.writerow(['1', 'Laptop', '999.99'])
    writer.writerow(['2', 'Mouse', '29.99'])
    writer.writerow(['3', 'Keyboard', '79.99'])

print(f"✅ CSV created: {products_file.name}")
```

### Exercise 2.6: Read CSV File
```python
with open(products_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: ${row['price']}")
```

### Exercise 2.7: Write Test Results to CSV
```python
results_file = output_dir / "test_results.csv"

with open(results_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['test_name', 'status', 'duration'])
    writer.writerow(['test_login', 'passed', '2.3s'])
    writer.writerow(['test_signup', 'passed', '3.1s'])
    writer.writerow(['test_logout', 'failed', '1.5s'])

print(f"✅ Test results created")
```

### Exercise 2.8: Append to CSV
```python
with open(results_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['test_search', 'passed', '1.8s'])

print("✅ Result appended")
```

### BONUS: JSON to CSV Conversion
```python
with open(users_file, 'r') as f:
    users = json.load(f)['users']

csv_file = output_dir / "users.csv"
with open(csv_file, 'w', newline='') as f:
    fieldnames = ['username', 'email', 'active']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow({
            'username': user['username'],
            'email': user['email'],
            'active': user['active']
        })

print(f"✅ Converted JSON to CSV: {csv_file.name}")
```

---

## Exercise 3: Automation File Handling

### Exercise 3.1: Create Test Configuration
```python
config = {
    "base_url": "https://example.com",
    "browser_type": "chromium",
    "headless": False,
    "timeout": 30000
}

config_file = config_dir / "test_config.json"
with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ Config created: {config_file.name}")
```

### Exercise 3.2: Load and Use Configuration
```python
with open(config_file, 'r') as f:
    config = json.load(f)

print("Configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")
```

### Exercise 3.3: Create Test Data CSV
```python
scenarios_file = output_dir / "test_scenarios.csv"

scenarios = [
    ['scenario', 'username', 'password', 'expected_result'],
    ['valid_login', 'test@example.com', 'Test123!', 'success'],
    ['invalid_password', 'test@example.com', 'wrong', 'failure'],
    ['empty_username', '', 'Test123!', 'failure'],
    ['empty_password', 'test@example.com', '', 'failure']
]

with open(scenarios_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scenarios)

print(f"✅ Test scenarios created")
```

### Exercise 3.4: Run Data-Driven Test
```python
with open(scenarios_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Testing {row['scenario']}: {row['expected_result']}")
```

### Exercise 3.5: Save Test Results
```python
def save_test_results(test_name, passed, failed):
    """Save test results with timestamp."""
    results = {
        "test_name": test_name,
        "timestamp": datetime.now().isoformat(),
        "passed": passed,
        "failed": failed,
        "total": passed + failed,
        "success_rate": f"{(passed/(passed+failed)*100):.1f}%"
    }

    results_file = results_dir / f"{test_name}_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✅ Results saved: {results_file.name}")

save_test_results("LoginTests", 45, 5)
```

### Exercise 3.6: Generate Test Report CSV
```python
def generate_report_csv(test_suite, total, passed, failed):
    """Generate CSV test report."""
    report_file = results_dir / "test_report.csv"

    with open(report_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'test_suite', 'total', 'passed', 'failed', 'success_rate'])
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            test_suite,
            total,
            passed,
            failed,
            f"{(passed/total*100):.1f}%"
        ])

    print(f"✅ Report generated: {report_file.name}")

generate_report_csv("Login Tests", 50, 45, 5)
```

### Exercise 3.7: Create Log Writer
```python
def log_test_step(step, level="INFO"):
    """Log test step with timestamp and level."""
    log_file = results_dir / "test_execution.log"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {step}\n"

    with open(log_file, 'a') as f:
        f.write(log_entry)

log_test_step("Test started")
log_test_step("Login successful", "SUCCESS")
log_test_step("Logout failed", "ERROR")
```

### Exercise 3.8: Load Test Users Helper
```python
def load_test_users(json_file):
    """Load only active users from JSON file."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    return [u for u in data['users'] if u['active']]

# Usage
active_users = load_test_users(users_file)
print(f"Loaded {len(active_users)} active users")
```

### BONUS: Complete Test Suite Helper
```python
class TestDataManager:
    """Manage test data files."""

    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

    def load_config(self, file):
        """Load JSON configuration."""
        with open(self.base_dir / file, 'r') as f:
            return json.load(f)

    def load_test_cases(self, file):
        """Load test cases from CSV."""
        with open(self.base_dir / file, 'r') as f:
            return list(csv.DictReader(f))

    def save_results(self, data, file):
        """Save results to JSON."""
        with open(self.base_dir / file, 'w') as f:
            json.dump(data, f, indent=2)

# Usage
manager = TestDataManager(output_dir)
config = manager.load_config("config/test_config.json")
test_cases = manager.load_test_cases("test_scenarios.csv")
manager.save_results({"status": "complete"}, "final_results.json")
```

---

## Key Takeaways

1. **Always use context managers** (`with` statement) for file operations
2. **JSON is ideal** for configuration and structured data
3. **CSV is perfect** for tabular test data
4. **Organize files** in clear directory structures
5. **Use Path** from pathlib for cross-platform paths
6. **Log everything** for debugging and reporting
7. **Validate data** before using it in tests

## Next Steps

- Practice with your own test data files
- Create a complete test data management system
- Integrate file handling into Playwright tests
- Build reusable helper functions

Good luck with your automation journey!
