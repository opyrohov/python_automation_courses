"""
Lecture 6 - Example 5: Working with External Libraries
=====================================================
Learn how to work with external packages installed via pip.

NOTE: These examples show import patterns and usage concepts.
Some packages may need to be installed first:
pip install requests pytest faker
"""

print("=" * 60)
print("WORKING WITH EXTERNAL LIBRARIES")
print("=" * 60)
print()

# 1. REQUESTS LIBRARY - HTTP Requests
# ===================================

print("1. requests library (HTTP requests):")
print()

try:
    import requests

    print("Making HTTP request...")

    # GET request
    response = requests.get("https://api.github.com")
    print(f"Status code: {response.status_code}")
    print(f"Response time: {response.elapsed.total_seconds()}s")

    # Parse JSON
    data = response.json()
    print(f"Response keys: {list(data.keys())[:5]}")

    print()
    print("Common requests operations:")
    example_code = """
    # GET request
    response = requests.get("https://api.example.com/users")

    # POST request
    data = {"username": "test", "email": "test@example.com"}
    response = requests.post("https://api.example.com/users", json=data)

    # With headers
    headers = {"Authorization": "Bearer token123"}
    response = requests.get("https://api.example.com/profile", headers=headers)

    # Check response
    if response.status_code == 200:
        data = response.json()
    """
    print(example_code)

except ImportError:
    print("❌ requests not installed")
    print("Install with: pip install requests")

print()
print("-" * 60)


# 2. PYTEST - Testing Framework
# =============================

print("2. pytest (testing framework):")
print()

try:
    import pytest

    print(f"✅ pytest version: {pytest.__version__}")
    print()

    print("Example pytest test:")
    test_example = """
    # test_example.py
    import pytest

    def test_addition():
        assert 2 + 2 == 4

    def test_string():
        assert "hello".upper() == "HELLO"

    @pytest.mark.parametrize("input,expected", [
        (2, 4),
        (3, 9),
        (4, 16),
    ])
    def test_square(input, expected):
        assert input ** 2 == expected

    # Run with: pytest test_example.py
    """
    print(test_example)

except ImportError:
    print("❌ pytest not installed")
    print("Install with: pip install pytest")

print()
print("-" * 60)


# 3. FAKER - Generate Fake Test Data
# ==================================

print("3. faker (generate test data):")
print()

try:
    from faker import Faker

    fake = Faker()

    print("Generated test data:")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Address: {fake.address()}")
    print(f"Phone: {fake.phone_number()}")
    print(f"Company: {fake.company()}")
    print(f"Text: {fake.text(max_nb_chars=50)}")
    print()

    print("Generate multiple test users:")
    for i in range(3):
        user = {
            "name": fake.name(),
            "email": fake.email(),
            "username": fake.user_name(),
            "password": fake.password()
        }
        print(f"User {i+1}: {user}")
    print()

    print("Other faker capabilities:")
    print(f"Date: {fake.date()}")
    print(f"URL: {fake.url()}")
    print(f"IPv4: {fake.ipv4()}")
    print(f"Credit Card: {fake.credit_card_number()}")

except ImportError:
    print("❌ faker not installed")
    print("Install with: pip install faker")

print()
print("-" * 60)


# 4. CHECKING IF PACKAGE IS INSTALLED
# ===================================

print("4. Checking if packages are installed:")
print()


def is_package_installed(package_name):
    """Check if a package is installed."""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False


packages_to_check = [
    ("playwright", "pip install playwright"),
    ("pytest", "pip install pytest"),
    ("requests", "pip install requests"),
    ("selenium", "pip install selenium"),
    ("faker", "pip install faker"),
]

print("Package status:")
for package, install_cmd in packages_to_check:
    status = "✅ Installed" if is_package_installed(package) else f"❌ Not installed ({install_cmd})"
    print(f"{package:15} - {status}")

print()
print("-" * 60)


# 5. READING PACKAGE DOCUMENTATION
# ================================

print("5. Finding package information:")
print()

try:
    import requests

    print(f"Package: {requests.__name__}")
    print(f"Version: {requests.__version__}")
    print(f"File location: {requests.__file__}")
    print()

    # List some available attributes
    attrs = [attr for attr in dir(requests) if not attr.startswith('_')]
    print(f"Main functions/classes: {attrs[:10]}")
    print()

except ImportError:
    pass

print("Where to find documentation:")
docs = """
1. Official package website
   - playwright: playwright.dev/python
   - pytest: pytest.org
   - requests: requests.readthedocs.io

2. PyPI package page
   - https://pypi.org/project/package-name/

3. GitHub repository
   - Usually linked from PyPI

4. Using help() in Python
   - help(package_name)
   - help(package_name.function_name)
"""
print(docs)

print()
print("-" * 60)


# 6. IMPORT PATTERNS FOR POPULAR LIBRARIES
# ========================================

print("6. Common import patterns:")
print()

patterns = """
# Requests
import requests
response = requests.get(url)

# Pytest
import pytest
@pytest.fixture
def setup():
    pass

# Faker
from faker import Faker
fake = Faker()

# Datetime
from datetime import datetime, timedelta
now = datetime.now()

# JSON
import json
data = json.loads(json_string)

# Pathlib
from pathlib import Path
path = Path(__file__)

# Random
import random
num = random.randint(1, 10)

# Playwright (we'll cover this next!)
from playwright.sync_api import sync_playwright, expect
"""

print(patterns)

print()
print("-" * 60)


# 7. VERSION COMPATIBILITY
# ========================

print("7. Checking versions and compatibility:")
print()

import sys

print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print()

# Check if Python version is compatible
if sys.version_info >= (3, 8):
    print("✅ Python 3.8+ (compatible with Playwright)")
else:
    print("❌ Please upgrade to Python 3.8 or higher")

print()
print("-" * 60)


# 8. HANDLING IMPORT ERRORS GRACEFULLY
# ====================================

print("8. Handling import errors:")
print()

# Try to import optional dependency
try:
    from faker import Faker
    fake = Faker()
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False
    print("⚠️  faker not available, using default values")


def generate_test_email():
    """Generate test email (with or without faker)."""
    if HAS_FAKER:
        return fake.email()
    else:
        import random
        return f"test{random.randint(1, 1000)}@example.com"


print(f"Generated email: {generate_test_email()}")

print()
print("-" * 60)


# 9. PRACTICAL EXAMPLE - API TEST HELPER
# ======================================

print("9. Practical example - API test helper:")
print()


def api_test_helper():
    """Example of using multiple libraries together."""

    # Check if requests is available
    if not is_package_installed("requests"):
        print("Please install requests: pip install requests")
        return

    import requests
    from datetime import datetime

    print("API Test Helper")
    print(f"Test started at: {datetime.now()}")
    print()

    try:
        # Make API request
        print("Testing GitHub API...")
        response = requests.get("https://api.github.com")

        # Log results
        print(f"Status: {response.status_code}")
        print(f"Response time: {response.elapsed.total_seconds():.2f}s")

        if response.status_code == 200:
            print("✅ API is responding")
        else:
            print(f"❌ API returned status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

    print(f"\nTest ended at: {datetime.now()}")


api_test_helper()

print()
print("-" * 60)


# 10. NEXT STEPS - PLAYWRIGHT
# ===========================

print("10. Next up: Playwright!")
print()

playwright_info = """
In the next example (06_playwright_examples.py), we'll cover:

✅ Installing Playwright
✅ Importing Playwright modules
✅ Understanding sync vs async API
✅ Common Playwright imports for tests
✅ Organizing Playwright test projects

To install Playwright:
1. pip install playwright
2. playwright install

Then you'll be ready for browser automation!
"""

print(playwright_info)

print("=" * 60)
print("Example complete! You understand external libraries.")
print("=" * 60)
