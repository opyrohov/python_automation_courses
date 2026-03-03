"""
Lecture 7 - Example 5: Playwright File Integration
=================================================
Practical examples of file handling in automation testing.
"""

import json
import csv
from pathlib import Path
from datetime import datetime

print("=" * 60)
print("FILE HANDLING IN PLAYWRIGHT AUTOMATION")
print("=" * 60)
print()

# Paths
sample_data_dir = Path(__file__).parent.parent / "sample_data"
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

# 1. LOAD TEST CONFIGURATION
# ==========================

print("1. Load test configuration from JSON:")
print()

config_file = sample_data_dir / "config.json"
with open(config_file, 'r') as f:
    config = json.load(f)

print(f"Environment: {config['environment']}")
print(f"Base URL: {config['base_url']}")
print(f"Browser: {config['browser']['type']}")
print(f"Default timeout: {config['timeouts']['default']}ms")
print()

# Simulate using config in tests
print("Using config in tests:")
print(f"  page.goto('{config['base_url']}')")
print(f"  page.set_default_timeout({config['timeouts']['default']})")

print()
print("-" * 60)


# 2. LOAD TEST USERS FROM JSON
# ============================

print("2. Load test users from JSON:")
print()

users_file = sample_data_dir / "users.json"
with open(users_file, 'r') as f:
    users_data = json.load(f)

# Get active users only
active_users = [u for u in users_data['users'] if u['active']]
print(f"Loaded {len(active_users)} active test users")

for user in active_users:
    print(f"  - {user['username']} ({user['role']})")

print()
print("-" * 60)


# 3. DATA-DRIVEN TESTS FROM CSV
# =============================

print("3. Run data-driven tests from CSV:")
print()

def simulate_login_test(test_case):
    """Simulate a login test."""
    print(f"  Test: {test_case['test_name']}")
    print(f"    Username: {test_case['username']}")
    print(f"    Expected: {test_case['expected_result']}")

    # In real Playwright test:
    # page.fill('#username', test_case['username'])
    # page.fill('#password', test_case['password'])
    # page.click('#login-button')

    # Simulate result
    result = "passed" if test_case['expected_result'] == 'success' else "failed"
    print(f"    Result: {result}")
    return result

test_cases_file = sample_data_dir / "test_cases.csv"
results = []

with open(test_cases_file, 'r') as f:
    reader = csv.DictReader(f)
    for test_case in reader:
        result = simulate_login_test(test_case)
        results.append({
            'test_id': test_case['test_id'],
            'test_name': test_case['test_name'],
            'result': result
        })
        print()

print("-" * 60)


# 4. SAVE TEST RESULTS TO JSON
# ============================

print("4. Save test results to JSON:")
print()

test_results = {
    "test_run_id": f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "timestamp": datetime.now().isoformat(),
    "environment": config['environment'],
    "total_tests": len(results),
    "passed": sum(1 for r in results if r['result'] == 'passed'),
    "failed": sum(1 for r in results if r['result'] == 'failed'),
    "test_cases": results
}

results_file = output_dir / "test_results.json"
with open(results_file, 'w') as f:
    json.dump(test_results, f, indent=2)

print(f"✅ Results saved to: {results_file.name}")
print(f"   Total: {test_results['total_tests']}")
print(f"   Passed: {test_results['passed']}")
print(f"   Failed: {test_results['failed']}")

print()
print("-" * 60)


# 5. GENERATE CSV REPORT
# ======================

print("5. Generate CSV test report:")
print()

csv_report_file = output_dir / "test_execution_report.csv"

with open(csv_report_file, 'w', newline='') as f:
    fieldnames = ['test_id', 'test_name', 'result', 'timestamp']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        result['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow(result)

print(f"✅ CSV report saved to: {csv_report_file.name}")

print()
print("-" * 60)


# 6. LOG TEST EXECUTION
# =====================

print("6. Write test execution log:")
print()

log_file = output_dir / "test_execution.log"

def log_test_event(message, level="INFO"):
    """Log test event to file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {message}\n"

    with open(log_file, 'a') as f:
        f.write(log_entry)

# Simulate test execution logging
log_test_event("Test suite started", "INFO")
log_test_event("Browser launched", "INFO")
log_test_event("Navigated to login page", "INFO")
log_test_event("Login test passed", "SUCCESS")
log_test_event("Logout test failed", "ERROR")
log_test_event("Test suite completed", "INFO")

print(f"✅ Log file created: {log_file.name}")
print()

with open(log_file, 'r') as f:
    print("Recent log entries:")
    print(f.read())

print("-" * 60)


# 7. ORGANIZE TEST DATA FILES
# ===========================

print("7. Organize test data files:")
print()

project_structure = """
Recommended project structure:

test_project/
├── tests/
│   └── test_login.py
├── test_data/
│   ├── users.json          # Test user credentials
│   ├── test_cases.csv      # Test scenarios
│   └── expected_results.json
├── config/
│   ├── dev_config.json     # Development
│   ├── staging_config.json # Staging
│   └── prod_config.json    # Production
├── output/
│   ├── results/            # Test results
│   ├── screenshots/        # Test screenshots
│   └── logs/               # Execution logs
└── utils/
    └── file_helpers.py     # File handling utilities
"""

print(project_structure)

print("-" * 60)


# 8. HELPER FUNCTIONS FOR FILE OPERATIONS
# =======================================

print("8. Reusable helper functions:")
print()

def load_json_data(file_path):
    """Load JSON data from file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json_data(data, file_path):
    """Save data to JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def load_test_cases(csv_path):
    """Load test cases from CSV."""
    with open(csv_path, 'r') as f:
        return list(csv.DictReader(f))

def append_test_result(result, csv_path):
    """Append test result to CSV."""
    with open(csv_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=result.keys())
        if csv_path.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(result)

print("Helper functions defined:")
print("  - load_json_data(file_path)")
print("  - save_json_data(data, file_path)")
print("  - load_test_cases(csv_path)")
print("  - append_test_result(result, csv_path)")

print()
print("=" * 60)
print("Example complete! File handling patterns for automation.")
print("=" * 60)
print()
print(f"All output files saved to: {output_dir}")
