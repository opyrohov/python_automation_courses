"""
Lecture 7 - Example 3: JSON Handling
===================================
Learn how to work with JSON data in Python.
"""

import json
from pathlib import Path

# Paths
sample_data_dir = Path(__file__).parent.parent / "sample_data"
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

print("=" * 60)
print("WORKING WITH JSON IN PYTHON")
print("=" * 60)
print()

# 1. READING JSON FROM FILE
# =========================

print("1. Read JSON from file:")
print()

users_file = sample_data_dir / "users.json"

with open(users_file, 'r') as f:
    data = json.load(f)

print(f"Loaded {len(data['users'])} users")
print("\nFirst user:")
print(f"  Username: {data['users'][0]['username']}")
print(f"  Email: {data['users'][0]['email']}")
print(f"  Role: {data['users'][0]['role']}")

print()
print("-" * 60)


# 2. WRITING JSON TO FILE
# =======================

print("2. Write JSON to file:")
print()

new_user = {
    "id": 4,
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "NewPass123!",
    "role": "user",
    "active": True
}

# Add new user
data['users'].append(new_user)

output_file = output_dir / "updated_users.json"
with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Updated JSON saved to: {output_file.name}")
print(f"   Total users: {len(data['users'])}")

print()
print("-" * 60)


# 3. PARSE JSON STRING
# ====================

print("3. Parse JSON string:")
print()

json_string = '{"name": "Alice", "age": 25, "city": "NYC"}'
user_data = json.loads(json_string)

print(f"Name: {user_data['name']}")
print(f"Age: {user_data['age']}")
print(f"City: {user_data['city']}")

print()
print("-" * 60)


# 4. CONVERT PYTHON TO JSON STRING
# ================================

print("4. Convert Python dict to JSON string:")
print()

test_result = {
    "test_name": "Login Test",
    "passed": True,
    "duration": 2.5,
    "assertions": ["title_correct", "url_correct"]
}

json_str = json.dumps(test_result, indent=2)
print("JSON output:")
print(json_str)

print()
print("-" * 60)


# 5. WORKING WITH NESTED JSON
# ===========================

print("5. Working with nested JSON:")
print()

config_file = sample_data_dir / "config.json"
with open(config_file, 'r') as f:
    config = json.load(f)

print(f"Environment: {config['environment']}")
print(f"Base URL: {config['base_url']}")
print(f"Browser type: {config['browser']['type']}")
print(f"Headless mode: {config['browser']['headless']}")
print(f"Default timeout: {config['timeouts']['default']}ms")

print()
print("-" * 60)


# 6. CREATE TEST DATA JSON
# ========================

print("6. Create test data JSON:")
print()

test_data = {
    "test_suite": "Login Tests",
    "test_cases": [
        {
            "id": 1,
            "name": "valid_login",
            "username": "testuser@example.com",
            "password": "Test123!",
            "expected": "success"
        },
        {
            "id": 2,
            "name": "invalid_password",
            "username": "testuser@example.com",
            "password": "wrong",
            "expected": "failure"
        }
    ]
}

test_data_file = output_dir / "test_data.json"
with open(test_data_file, 'w') as f:
    json.dump(test_data, f, indent=2)

print(f"✅ Test data created: {test_data_file.name}")
print(f"   Test cases: {len(test_data['test_cases'])}")

print()
print("-" * 60)


# 7. FILTER JSON DATA
# ===================

print("7. Filter JSON data:")
print()

# Get only active users
with open(users_file, 'r') as f:
    all_users = json.load(f)

active_users = [u for u in all_users['users'] if u['active']]
print(f"Active users: {len(active_users)}")
for user in active_users:
    print(f"  - {user['username']} ({user['email']})")

print()
print("-" * 60)


# 8. UPDATE JSON DATA
# ===================

print("8. Update JSON data:")
print()

# Update configuration
with open(config_file, 'r') as f:
    config = json.load(f)

# Change to production settings
config['environment'] = 'production'
config['base_url'] = 'https://example.com'
config['browser']['headless'] = True

prod_config_file = output_dir / "prod_config.json"
with open(prod_config_file, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ Production config created: {prod_config_file.name}")
print(f"   Environment: {config['environment']}")
print(f"   Headless: {config['browser']['headless']}")

print()
print("-" * 60)


# 9. PRETTY PRINT JSON
# ====================

print("9. Pretty print JSON:")
print()

compact_json = json.dumps(new_user)
pretty_json = json.dumps(new_user, indent=2)

print("Compact JSON:")
print(compact_json)
print()
print("Pretty JSON:")
print(pretty_json)

print()
print("=" * 60)
print("Example complete! You've mastered JSON handling.")
print("=" * 60)
