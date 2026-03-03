# Lecture 33: Test Data Management

## Overview
Learn how to manage test data effectively: read from JSON and CSV files, use environment variables for sensitive data, load configuration from .env files, generate dynamic test data with Faker, and create reusable data fixtures.

## Topics Covered

### 1. Why Manage Test Data?
- Separating data from test logic
- Maintainability and reusability
- Sensitive data protection

### 2. JSON Test Data
- Reading test data from JSON files
- Structuring JSON for test cases
- Using JSON with parametrize

### 3. CSV Test Data
- Reading CSV files with Python
- CSV for large data sets
- CSV with parametrize

### 4. Environment Variables
- os.environ for sensitive data
- Passwords, API keys, URLs
- python-dotenv and .env files

### 5. Config Files
- .env files for project settings
- Loading config per environment (dev, staging, prod)
- Combining config sources

### 6. Faker - Dynamic Test Data
- Installing and using Faker
- Generating names, emails, addresses
- Localized data (Ukrainian, etc.)
- Reproducible data with seeds

### 7. Data Fixtures
- Creating pytest fixtures for test data
- Fixture factories
- Combining data sources with fixtures

## Examples

1. **01_json_test_data.py** - Reading and using JSON test data
2. **02_csv_test_data.py** - Reading and using CSV test data
3. **03_environment_variables.py** - Environment variables and .env files
4. **04_faker_dynamic_data.py** - Generating test data with Faker
5. **05_data_fixtures.py** - Complete data management with fixtures

## Exercises

1. **exercise_01_data_driven_tests.py** - Create data-driven tests from JSON/CSV
2. **exercise_02_config_and_faker.py** - Use .env config and Faker for test data

## Key Concepts

### JSON Test Data
```python
import json

def load_test_data(file_path):
    with open(file_path) as f:
        return json.load(f)

test_data = load_test_data("test_data/login_data.json")
```

### CSV Test Data
```python
import csv

def load_csv_data(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        return list(reader)
```

### Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file
BASE_URL = os.environ.get("BASE_URL", "https://default.com")
PASSWORD = os.environ["SECRET_PASSWORD"]
```

### Faker
```python
from faker import Faker

fake = Faker("uk_UA")
print(fake.name())       # Олександр Петренко
print(fake.email())      # random@example.com
print(fake.address())    # вул. Хрещатик, 1
```

## Resources
- [Faker Documentation](https://faker.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [JSON Module](https://docs.python.org/3/library/json.html)
- [CSV Module](https://docs.python.org/3/library/csv.html)

## Next Lecture
Lecture 34: Parameterized Testing
