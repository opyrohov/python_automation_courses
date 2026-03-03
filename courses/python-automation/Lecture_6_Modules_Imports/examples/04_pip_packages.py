"""
Lecture 6 - Example 4: Working with pip and Packages
===================================================
Learn how to install and manage Python packages with pip.
"""

# This file demonstrates pip concepts - the actual commands
# are run in the terminal, not in Python code

print("=" * 60)
print("WORKING WITH PIP - Python Package Manager")
print("=" * 60)
print()

# 1. WHAT IS PIP?
# ==============

print("1. What is pip?")
print()
print("pip is Python's package installer")
print("It downloads and installs packages from PyPI (Python Package Index)")
print("PyPI has over 400,000 packages available!")
print()

print("-" * 60)


# 2. BASIC PIP COMMANDS
# =====================

print("2. Basic pip commands (run these in terminal):")
print()

commands = """
# Check pip version
pip --version

# Install a package
pip install requests

# Install specific version
pip install playwright==1.40.0

# Install minimum version
pip install pytest>=7.0.0

# Install multiple packages
pip install requests pytest playwright

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests

# List installed packages
pip list

# Show package details
pip show playwright

# Search for packages (deprecated, use PyPI website)
pip search selenium  # No longer works, use pypi.org
"""

print(commands)
print()

print("-" * 60)


# 3. REQUIREMENTS.TXT FILE
# =======================

print("3. Using requirements.txt:")
print()

requirements_example = """
# requirements.txt - list all project dependencies

# Testing framework
pytest==7.4.3
pytest-playwright==0.4.3

# Playwright for browser automation
playwright==1.40.0

# HTTP requests
requests==2.31.0

# Data handling
pandas>=2.0.0

# Environment variables
python-dotenv==1.0.0

# Reporting
pytest-html==4.1.1

# You can also add comments and organize by category
# Development dependencies
black==23.12.0  # Code formatter
flake8==6.1.0   # Linter
"""

print(requirements_example)
print()

print("To install all packages from requirements.txt:")
print("pip install -r requirements.txt")
print()

print("To create requirements.txt from current environment:")
print("pip freeze > requirements.txt")
print()

print("-" * 60)


# 4. CHECKING INSTALLED PACKAGES
# ==============================

print("4. Checking what's installed:")
print()

# You can check installed packages programmatically
import sys
import subprocess

try:
    # Get pip list
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list"],
        capture_output=True,
        text=True
    )
    print("Installed packages (first 10):")
    lines = result.stdout.split('\n')
    for line in lines[:12]:  # Header + 10 packages
        print(line)
    print("...")
except Exception as e:
    print(f"Could not list packages: {e}")
print()

print("-" * 60)


# 5. VIRTUAL ENVIRONMENTS (PREVIEW)
# =================================

print("5. Virtual environments (important!):")
print()

venv_commands = """
Virtual environments create isolated Python installations
for each project, preventing package conflicts.

# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\\Scripts\\activate

# Mac/Linux:
source venv/bin/activate

# Now install packages - they go only in this environment
pip install playwright

# Deactivate when done
deactivate

# Your project structure:
my_project/
├── venv/              # Virtual environment (don't commit!)
├── tests/
├── pages/
├── requirements.txt
└── .gitignore         # Add venv/ to this
"""

print(venv_commands)
print()

print("-" * 60)


# 6. PLAYWRIGHT INSTALLATION
# ==========================

print("6. Installing Playwright specifically:")
print()

playwright_install = """
# Step 1: Install the Python package
pip install playwright

# Step 2: Install browser binaries
playwright install

# Install specific browsers
playwright install chromium
playwright install firefox
playwright install webkit

# Install with dependencies (for Linux)
playwright install --with-deps

# Check installation
playwright --version
"""

print(playwright_install)
print()

print("-" * 60)


# 7. COMMON PIP ISSUES AND SOLUTIONS
# ==================================

print("7. Common pip issues and solutions:")
print()

issues = """
❌ ISSUE: "pip not found" or "command not found"
✅ SOLUTION:
   - Use: python -m pip install package_name
   - Or ensure Python is in PATH

❌ ISSUE: Permission denied
✅ SOLUTION:
   - Use: pip install --user package_name
   - Or use virtual environment (recommended)

❌ ISSUE: Package conflicts
✅ SOLUTION:
   - Use virtual environments
   - Check versions with pip show package_name

❌ ISSUE: SSL certificate error
✅ SOLUTION:
   - Use: pip install --trusted-host pypi.org package_name
   - Or fix certificate installation

❌ ISSUE: Package not found
✅ SOLUTION:
   - Check spelling
   - Check if package exists on PyPI
   - Ensure pip is updated: python -m pip install --upgrade pip
"""

print(issues)
print()

print("-" * 60)


# 8. USEFUL PIP PACKAGES FOR AUTOMATION
# =====================================

print("8. Popular packages for test automation:")
print()

packages = """
🔧 Testing Frameworks:
   - pytest: Modern testing framework
   - unittest: Built-in testing framework
   - nose2: Alternative testing framework

🌐 Web Automation:
   - playwright: Modern browser automation
   - selenium: Traditional web automation
   - requests: HTTP requests library

📊 Reporting:
   - pytest-html: HTML test reports
   - allure-pytest: Beautiful test reports
   - pytest-cov: Code coverage

🛠️ Utilities:
   - python-dotenv: Environment variable management
   - pyyaml: YAML file handling
   - openpyxl: Excel file handling
   - pillow: Image processing
   - faker: Generate fake test data

📈 Data & API:
   - requests: HTTP requests
   - httpx: Async HTTP client
   - jsonschema: JSON validation
   - pydantic: Data validation
"""

print(packages)
print()

print("-" * 60)


# 9. BEST PRACTICES
# =================

print("9. pip best practices:")
print()

best_practices = """
✅ DO:
   - Always use virtual environments
   - Pin versions in requirements.txt
   - Keep requirements.txt up to date
   - Separate dev and prod requirements
   - Document installation steps in README

❌ DON'T:
   - Install packages globally (except pip, virtualenv)
   - Use 'pip install' with sudo
   - Commit virtual environment to git
   - Forget to update requirements.txt
   - Mix pip and conda in same environment
"""

print(best_practices)
print()

print("-" * 60)


# 10. QUICK REFERENCE
# ===================

print("10. Quick reference:")
print()

quick_ref = """
# Install package
pip install package_name

# Install from requirements
pip install -r requirements.txt

# Update package
pip install --upgrade package_name

# Uninstall package
pip uninstall package_name

# List packages
pip list

# Show package info
pip show package_name

# Freeze current packages
pip freeze > requirements.txt

# Check outdated packages
pip list --outdated

# Install specific version
pip install package_name==1.2.3
"""

print(quick_ref)
print()

print("=" * 60)
print("Example complete! You understand pip package management.")
print("=" * 60)
