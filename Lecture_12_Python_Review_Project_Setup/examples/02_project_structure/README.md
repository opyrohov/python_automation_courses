# Project Structure Template

This folder contains a template structure for a professional Playwright automation project.

## Recommended Structure

```
my_automation_project/
│
├── venv/                      # Virtual environment (DON'T COMMIT)
│   ├── Scripts/               # Windows
│   ├── bin/                   # Mac/Linux
│   └── Lib/                   # Installed packages
│
├── tests/                     # All test files
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_checkout.py
│   ├── test_search.py
│   └── conftest.py            # Pytest fixtures and configuration
│
├── pages/                     # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base class for all pages
│   ├── login_page.py          # Login page object
│   ├── home_page.py           # Home page object
│   └── checkout_page.py       # Checkout page object
│
├── utils/                     # Helper functions and utilities
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── helpers.py             # Helper functions
│   └── logger.py              # Logging setup
│
├── test_data/                 # Test data files
│   ├── users.json             # Test user data
│   ├── products.csv           # Product test data
│   └── test_cases.xlsx        # Test case data
│
├── screenshots/               # Test screenshots (DON'T COMMIT)
├── videos/                    # Test recordings (DON'T COMMIT)
├── test-results/              # Pytest results (DON'T COMMIT)
│
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── .env                       # Environment variables (DON'T COMMIT)
├── .env.example               # Template for .env
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## File Purposes

### tests/
Contains all your test files. Each file should:
- Start with `test_` (e.g., `test_login.py`)
- Contain test functions starting with `test_`
- Follow AAA pattern (Arrange, Act, Assert)

### pages/
Contains Page Object Model classes:
- Each page of the application has its own class
- Encapsulates page elements and actions
- Makes tests more maintainable
- Reduces code duplication

### utils/
Helper code used across the project:
- **config.py**: Application URLs, timeouts, browser settings
- **helpers.py**: Reusable functions (generate test data, screenshots, etc.)
- **logger.py**: Logging configuration

### test_data/
Test data in various formats:
- JSON files for structured data
- CSV files for tabular data
- Excel files for test cases
- Keep separate from code

### requirements.txt
Lists all Python packages needed:
```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
python-dotenv==1.0.0
```

### pytest.ini
Pytest configuration:
```ini
[pytest]
testpaths = tests
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
addopts = -v --tb=short
```

### .env
Environment-specific variables (credentials, URLs):
```
BASE_URL=https://staging.example.com
TEST_USERNAME=test@example.com
TEST_PASSWORD=TestPass123
HEADLESS=False
```

### .gitignore
Files/folders to exclude from Git:
```
venv/
__pycache__/
*.pyc
.pytest_cache/
.env
test-results/
screenshots/
videos/
```

## Creating This Structure

### Option 1: Manually
```bash
# Create project folder
mkdir my_automation_project
cd my_automation_project

# Create folders
mkdir tests pages utils test_data

# Create __init__.py files
touch tests/__init__.py pages/__init__.py utils/__init__.py

# Or on Windows:
type nul > tests\__init__.py
type nul > pages\__init__.py
type nul > utils\__init__.py

# Create configuration files
# (Add content from examples above)
```

### Option 2: Using Script
See `create_project.sh` (Mac/Linux) or `create_project.bat` (Windows) in this folder.

## Next Steps

1. Create this structure for your project
2. Set up virtual environment
3. Create and populate configuration files
4. Write your first test
5. Start building page objects

## Best Practices

✅ **DO:**
- Keep tests separate from application code
- Use Page Object Model for UI tests
- Store test data in separate files
- Use descriptive file and folder names
- Keep configuration in one place

❌ **DON'T:**
- Mix test code with production code
- Hardcode values in tests
- Commit sensitive data (.env, credentials)
- Create deeply nested folder structures
- Store test artifacts in Git
