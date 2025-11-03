# Complete Project Setup Guide

Step-by-step guide to creating your first Playwright automation project from scratch.

## Prerequisites

Before starting, ensure you have:
- [ ] Python 3.8 or higher installed
- [ ] pip package manager installed
- [ ] Git installed (optional but recommended)
- [ ] Code editor (VS Code, PyCharm, etc.)

Verify:
```bash
python --version    # Should be 3.8+
pip --version       # Should show pip version
git --version       # Should show git version
```

## Step-by-Step Setup

### Step 1: Create Project Folder

```bash
# Create and navigate to project folder
mkdir my_automation_project
cd my_automation_project
```

### Step 2: Create Folder Structure

**Windows:**
```cmd
mkdir tests pages utils test_data
type nul > tests\__init__.py
type nul > pages\__init__.py
type nul > utils\__init__.py
```

**Mac/Linux:**
```bash
mkdir tests pages utils test_data
touch tests/__init__.py pages/__init__.py utils/__init__.py
```

Your structure should now look like:
```
my_automation_project/
├── tests/
│   └── __init__.py
├── pages/
│   └── __init__.py
├── utils/
│   └── __init__.py
└── test_data/
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# If you have multiple Python versions:
# python3.11 -m venv venv
```

### Step 4: Activate Virtual Environment

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your prompt:
```
(venv) C:\my_automation_project>
```

### Step 5: Create requirements.txt

Create `requirements.txt` file with this content:

```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
python-dotenv==1.0.0
```

### Step 6: Install Dependencies

```bash
# Make sure venv is activated!
pip install -r requirements.txt

# This will install:
# - playwright (browser automation)
# - pytest (testing framework)
# - pytest-playwright (pytest + playwright integration)
# - python-dotenv (environment variable management)
```

### Step 7: Install Playwright Browsers

```bash
# Install browser drivers (Chrome, Firefox, Safari)
playwright install

# Or install specific browser:
# playwright install chromium
```

This downloads and installs browser binaries that Playwright will use for testing.

### Step 8: Verify Installation

```bash
# Check Python (should be from venv)
where python  # Windows
which python  # Mac/Linux

# Check pytest
pytest --version

# Check playwright
playwright --version

# List installed packages
pip list
```

### Step 9: Create .gitignore

Create `.gitignore` file:

```
# Virtual environment
venv/
env/
ENV/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Pytest
.pytest_cache/

# Test artifacts
test-results/
screenshots/
videos/
playwright-report/

# Environment variables
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### Step 10: Create pytest.ini

Create `pytest.ini` file:

```ini
[pytest]
# Where to look for tests
testpaths = tests

# Custom markers for test organization
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    login: Login-related tests
    checkout: Checkout flow tests
    critical: Business-critical tests

# Command line options applied by default
addopts = -v --tb=short --strict-markers

# Minimum Python version
minversion = 3.8
```

### Step 11: Create Configuration File

Create `utils/config.py`:

```python
"""
Configuration settings for the test automation project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
TEST_DATA_DIR = PROJECT_ROOT / "test_data"

# Ensure directories exist
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Application settings
BASE_URL = os.getenv("BASE_URL", "https://example.com")

# Browser settings
BROWSER = os.getenv("BROWSER", "chromium")  # chromium, firefox, webkit
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))  # Slow down operations (ms)

# Timeouts (milliseconds)
DEFAULT_TIMEOUT = 30000  # 30 seconds
NAVIGATION_TIMEOUT = 60000  # 60 seconds

# Test user credentials (from .env)
TEST_USERNAME = os.getenv("TEST_USERNAME", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")

# Viewport size
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080

# Screenshot settings
SCREENSHOT_ON_FAILURE = True
FULL_PAGE_SCREENSHOT = True

# Video recording
RECORD_VIDEO = os.getenv("RECORD_VIDEO", "False").lower() == "true"
```

### Step 12: Create .env File

Create `.env` file (this will NOT be committed to Git):

```env
# Application URLs
BASE_URL=https://staging.example.com

# Browser configuration
BROWSER=chromium
HEADLESS=False
SLOW_MO=0

# Test credentials (NEVER use real credentials!)
TEST_USERNAME=test@example.com
TEST_PASSWORD=TestPassword123

# Video recording
RECORD_VIDEO=False
```

### Step 13: Create .env.example

Create `.env.example` (template for other developers):

```env
# Copy this file to .env and fill in your values
# DO NOT commit .env to Git!

# Application URLs
BASE_URL=https://example.com

# Browser configuration
BROWSER=chromium
HEADLESS=False
SLOW_MO=0

# Test credentials
TEST_USERNAME=your_test_username
TEST_PASSWORD=your_test_password

# Video recording
RECORD_VIDEO=False
```

### Step 14: Create Your First Test

Create `tests/test_example.py`:

```python
"""
Example test to verify setup is working correctly.
"""

import pytest
from playwright.sync_api import Page, expect


def test_google_homepage(page: Page):
    """
    Test that Google homepage loads successfully.
    This is a simple test to verify Playwright is working.
    """
    # ARRANGE
    url = "https://www.google.com"

    # ACT
    page.goto(url)

    # ASSERT
    expect(page).to_have_title("Google")
    assert page.is_visible("textarea[name='q']")


def test_google_search(page: Page):
    """
    Test that search functionality works on Google.
    """
    # ARRANGE
    search_term = "Playwright Python"
    page.goto("https://www.google.com")

    # ACT
    page.fill("textarea[name='q']", search_term)
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")

    # ASSERT
    expect(page).to_have_url("**/search?**")
    assert page.is_visible("#search")
```

### Step 15: Create conftest.py

Create `tests/conftest.py` for pytest fixtures:

```python
"""
Pytest configuration and fixtures.
"""

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def configure_page(page: Page):
    """
    Configure page settings before each test.
    """
    # Set default timeout
    page.set_default_timeout(30000)

    # Set viewport size
    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page

    # Teardown: Could add cleanup code here if needed
```

### Step 16: Run Your First Test

```bash
# Make sure venv is activated!
(venv) $ pytest

# Run with more details
pytest -v

# Run in headed mode (see browser)
pytest --headed

# Run specific test
pytest tests/test_example.py::test_google_homepage

# Run with specific browser
pytest --browser firefox
```

Expected output:
```
========================= test session starts =========================
platform win32 -- Python 3.11.0, pytest-8.0.0, pluggy-1.3.0
rootdir: C:\my_automation_project
plugins: playwright-0.4.4
collected 2 items

tests/test_example.py::test_google_homepage PASSED          [ 50%]
tests/test_example.py::test_google_search PASSED            [100%]

========================== 2 passed in 8.23s ==========================
```

### Step 17: Create Project README

Create `README.md`:

```markdown
# My Automation Project

Playwright + Pytest automation testing project.

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate venv:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Install browsers: `playwright install`
6. Copy `.env.example` to `.env` and configure

## Running Tests

```bash
# All tests
pytest

# Specific file
pytest tests/test_login.py

# Headed mode (see browser)
pytest --headed

# Specific browser
pytest --browser firefox

# Run smoke tests only
pytest -m smoke
```

## Project Structure

```
├── tests/         # Test files
├── pages/         # Page Object Model classes
├── utils/         # Helper functions and config
├── test_data/     # Test data files
└── requirements.txt
```

## Contributing

1. Create feature branch
2. Write tests
3. Run tests locally
4. Submit pull request
```

## Final Project Structure

Your complete project should now look like:

```
my_automation_project/
│
├── venv/                      # ✓ Created and activated
├── tests/                     # ✓ Created
│   ├── __init__.py
│   ├── conftest.py           # ✓ Pytest fixtures
│   └── test_example.py       # ✓ First test
│
├── pages/                     # ✓ Created (empty for now)
│   └── __init__.py
│
├── utils/                     # ✓ Created
│   ├── __init__.py
│   └── config.py             # ✓ Configuration
│
├── test_data/                 # ✓ Created (empty for now)
│
├── requirements.txt           # ✓ Dependencies listed
├── pytest.ini                 # ✓ Pytest config
├── .env                       # ✓ Environment variables
├── .env.example               # ✓ Template
├── .gitignore                 # ✓ Git exclusions
└── README.md                  # ✓ Documentation
```

## Verification Checklist

- [ ] Virtual environment created and activated
- [ ] All dependencies installed (check with `pip list`)
- [ ] Playwright browsers installed
- [ ] Configuration files created (.env, pytest.ini)
- [ ] First test written
- [ ] Tests run successfully (`pytest`)
- [ ] .gitignore created
- [ ] Project documented (README.md)

## Next Steps

1. ✅ Setup complete!
2. Learn Playwright basics (Lecture 13)
3. Write Page Object Model classes
4. Create more tests for your application
5. Set up CI/CD pipeline (future lectures)

## Troubleshooting

### Tests not found
- Ensure test files start with `test_`
- Ensure test functions start with `test_`
- Check `pytest.ini` testpaths setting

### Import errors
- Verify venv is activated
- Check all dependencies installed: `pip install -r requirements.txt`

### Browser not found
- Run `playwright install`
- Check Playwright version: `playwright --version`

### Permission errors (PowerShell)
- Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Daily Workflow

```bash
# 1. Navigate to project
cd my_automation_project

# 2. Activate venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Run tests
pytest

# 4. Deactivate when done
deactivate
```

Congratulations! Your automation project is ready! 🎉
