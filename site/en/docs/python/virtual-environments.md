# Virtual Environments

Virtual environments are isolated spaces for Python projects where each project has its own set of dependencies. This is critically important for QA automation, where different projects may require different library versions.

## Why Virtual Environments?

Imagine this situation: you are working on two test automation projects at the same time.

```python
# Project A — requires Selenium 4.10
# pip install selenium==4.10.0

# Project B — requires Selenium 4.20
# pip install selenium==4.20.0

# Without virtual environments — conflict!
# You can only install one version globally
```

::: warning Problems Without Isolation
- **Version conflicts** — different projects require different versions of the same library
- **Global Python pollution** — dozens of unnecessary packages in the system
- **Reproducibility issues** — impossible to guarantee the same environment in CI/CD
- **Maintenance difficulty** — removing one package may break another project
:::

::: tip Golden Rule
Always create a separate virtual environment for each project. Never install packages globally for production projects.
:::

## Creating a Virtual Environment

Python has a built-in `venv` module for creating virtual environments.

```bash
# Navigate to the project directory
cd my-qa-project

# Create a virtual environment
python -m venv venv
```

```
my-qa-project/
├── venv/                  # Virtual environment
│   ├── bin/               # (Linux/macOS) or Scripts/ (Windows)
│   ├── include/
│   ├── lib/               # Installed packages
│   └── pyvenv.cfg         # Environment configuration
├── tests/
└── requirements.txt
```

::: info Naming Convention
The most common names are: `venv`, `.venv`, `env`. It is recommended to use `venv` or `.venv` — they are easy to recognize and add to `.gitignore`.
:::

## Activation and Deactivation

### Windows

```bash
# Activation (Command Prompt)
venv\Scripts\activate

# Activation (PowerShell)
venv\Scripts\Activate.ps1

# Activation (Git Bash)
source venv/Scripts/activate
```

### macOS / Linux

```bash
# Activation
source venv/bin/activate
```

### Verification and Deactivation

```bash
# After activation, a prefix appears in the terminal:
(venv) $ python --version
Python 3.12.0

# Verify that Python points to the venv
(venv) $ which python
/home/user/my-qa-project/venv/bin/python

# Deactivation (same for all OS)
(venv) $ deactivate
```

::: warning PowerShell Execution Policy
If you get an error in Windows PowerShell during activation, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
:::

## pip Basics

`pip` is the Python package manager that installs libraries from PyPI (Python Package Index).

### Installing Packages

```bash
# Install the latest version
pip install pytest

# Install a specific version
pip install selenium==4.20.0

# Install a minimum version
pip install playwright>=1.40.0

# Install multiple packages at once
pip install pytest selenium allure-pytest
```

### Upgrading and Uninstalling

```bash
# Upgrade a package to the latest version
pip install --upgrade pytest

# Upgrade pip itself
pip install --upgrade pip

# Uninstall a package
pip uninstall selenium

# Uninstall without confirmation
pip uninstall -y selenium
```

### Viewing Installed Packages

```bash
# List all installed packages
pip list

# List in requirements format
pip freeze

# Information about a specific package
pip show pytest
```

::: tip pip freeze vs pip list
- `pip list` — displays packages in a user-friendly table format
- `pip freeze` — outputs in `package==version` format, ready for `requirements.txt`
:::

## requirements.txt

The `requirements.txt` file locks project dependencies for environment reproducibility.

### Creating

```bash
# Save all dependencies to a file
pip freeze > requirements.txt
```

```txt
# requirements.txt
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0
allure-pytest==2.13.5
requests==2.31.0
python-dotenv==1.0.1
```

### Installing from File

```bash
# Install all dependencies from file
pip install -r requirements.txt
```

::: info Version Specifiers
```txt
pytest==8.1.1        # Exact version (recommended)
selenium>=4.20.0     # Minimum version
requests>=2.28,<3.0  # Version range
playwright~=1.43.0   # Compatible version (>=1.43.0, <1.44.0)
```
:::

### Separating Dependencies

```txt
# requirements.txt — core dependencies
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0

# requirements-dev.txt — for development
-r requirements.txt
black==24.3.0
flake8==7.0.0
mypy==1.9.0
pre-commit==3.7.0
```

```bash
# For development — installs both files
pip install -r requirements-dev.txt
```

## pyproject.toml

The modern standard for Python project configuration, replacing `setup.py` and `setup.cfg`.

```toml
[project]
name = "qa-automation-project"
version = "1.0.0"
description = "Test automation project"
requires-python = ">=3.10"

dependencies = [
    "pytest>=8.0.0",
    "selenium>=4.20.0",
    "playwright>=1.43.0",
    "allure-pytest>=2.13.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "black>=24.0.0",
    "flake8>=7.0.0",
    "mypy>=1.9.0",
    "pre-commit>=3.7.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "smoke: Smoke tests",
    "regression: Regression tests",
    "api: API tests",
    "ui: UI tests",
]
addopts = "-v --tb=short"

[tool.black]
line-length = 120

[tool.mypy]
python_version = "3.12"
strict = true
```

```bash
# Install project from pyproject.toml
pip install .

# Install with dev dependencies
pip install ".[dev]"

# Install in development (editable) mode
pip install -e ".[dev]"
```

::: tip pyproject.toml vs requirements.txt
- **`pyproject.toml`** — for defining the project and its dependencies (recommended approach)
- **`requirements.txt`** — for locking exact versions (lock file), convenient for CI/CD
- You can use both: `pyproject.toml` for configuration + `requirements.txt` as a lock file
:::

## QA Project Structure

A typical test automation project structure:

```
qa-automation-project/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI/CD pipeline
├── config/
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   └── .env                    # Environment variables (NOT in git!)
├── pages/                      # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # pytest fixtures
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── api/
│       ├── __init__.py
│       └── test_users_api.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── api_client.py
├── .gitignore
├── .env.example                # Environment variable template
├── pyproject.toml
├── requirements.txt
└── README.md
```

### .gitignore for a Python Project

```gitignore
# Virtual environment
venv/
.venv/
env/

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Environment
.env

# IDE
.idea/
.vscode/
*.code-workspace

# Test artifacts
allure-results/
allure-report/
.pytest_cache/
htmlcov/
*.log
screenshots/
```

## QA Automation Examples

### Setting Up a New Project

```bash
# 1. Create the project directory
mkdir qa-automation && cd qa-automation

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install testing dependencies
pip install pytest selenium playwright allure-pytest requests python-dotenv

# 6. Install Playwright browsers
playwright install

# 7. Save dependencies
pip freeze > requirements.txt

# 8. Create the project structure
mkdir -p tests pages config utils
touch tests/__init__.py tests/conftest.py
touch pages/__init__.py pages/base_page.py
touch config/__init__.py config/settings.py
touch utils/__init__.py
```

### Test Project Configuration

```python
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Test environment configuration."""

    BASE_URL = os.getenv("BASE_URL", "https://staging.example.com")
    API_URL = os.getenv("API_URL", "https://api.staging.example.com")

    # Credentials
    ADMIN_USER = os.getenv("ADMIN_USER", "admin@test.com")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Test123!")

    # Timeouts
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30"))

    # Browser
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

settings = Settings()
```

```bash
# .env.example
BASE_URL=https://staging.example.com
API_URL=https://api.staging.example.com
ADMIN_USER=admin@test.com
ADMIN_PASSWORD=Test123!
DEFAULT_TIMEOUT=30
BROWSER=chromium
HEADLESS=true
```

### Managing Dependencies for Different Environments

```txt
# requirements.txt — base dependencies
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0
allure-pytest==2.13.5
requests==2.31.0
python-dotenv==1.0.1

# requirements-ci.txt — additional for CI/CD
-r requirements.txt
pytest-xdist==3.5.0        # Parallel test execution
pytest-rerunfailures==14.0  # Rerun flaky tests
pytest-timeout==2.3.1       # Test timeouts
```

### CI/CD — GitHub Actions

```yaml
# .github/workflows/tests.yml
name: Run Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Create virtual environment
        run: python -m venv venv

      - name: Install dependencies
        run: |
          source venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements-ci.txt

      - name: Install Playwright browsers
        run: |
          source venv/bin/activate
          playwright install --with-deps chromium

      - name: Run tests
        run: |
          source venv/bin/activate
          pytest tests/ -v --alluredir=allure-results
        env:
          BASE_URL: ${{ secrets.BASE_URL }}
          ADMIN_USER: ${{ secrets.ADMIN_USER }}
          ADMIN_PASSWORD: ${{ secrets.ADMIN_PASSWORD }}
          HEADLESS: "true"

      - name: Upload Allure results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: allure-results
          path: allure-results/
```

::: warning Security in CI/CD
- **Never** store passwords and tokens in code or `requirements.txt`
- Use **GitHub Secrets** for sensitive data
- The `.env` file must be in `.gitignore`
- Create `.env.example` as a template without real values
:::

### conftest.py with Fixtures

```python
# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from config.settings import settings


@pytest.fixture(scope="session")
def browser():
    """Launches a browser for the entire test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=settings.HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Creates a new page for each test."""
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(settings.DEFAULT_TIMEOUT * 1000)
    yield page
    context.close()


@pytest.fixture
def authenticated_page(page):
    """Page with an authenticated user."""
    page.goto(f"{settings.BASE_URL}/login")
    page.fill("[data-testid='email']", settings.ADMIN_USER)
    page.fill("[data-testid='password']", settings.ADMIN_PASSWORD)
    page.click("[data-testid='login-button']")
    page.wait_for_url(f"{settings.BASE_URL}/dashboard")
    return page
```

## Useful Links

- [Official venv Documentation](https://docs.python.org/3/library/venv.html)
- [pip — User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [PEP 621 — pyproject.toml](https://peps.python.org/pep-0621/)
- [Python Packaging Guide](https://packaging.python.org/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/api-requests">← Working with API</a>
  <a href="/python_automation_courses/en/docs/python/best-practices">Best Practices →</a>
</div>
