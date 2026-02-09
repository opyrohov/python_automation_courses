"""Example 5: Complete Data Management with Fixtures

Demonstrates combining all data management techniques into
a cohesive test project: JSON, CSV, env vars, Faker, fixtures.

Run with: pytest 05_data_fixtures.py -v --headed -s
"""
import json
import csv
import os
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"

EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EXAMPLES_DIR, "test_data")
os.makedirs(DATA_DIR, exist_ok=True)


# ============================================
# DATA FILES SETUP (for this example)
# ============================================

# Create test_users.json
users_json = {
    "valid": {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    },
    "invalid": [
        {"username": "wrong", "password": "wrong", "id": "bad_both"},
        {"username": "tomsmith", "password": "bad", "id": "bad_password"}
    ]
}

with open(os.path.join(DATA_DIR, "test_users.json"), "w") as f:
    json.dump(users_json, f, indent=2)

# Create pages.csv
with open(os.path.join(DATA_DIR, "pages.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["path", "heading_tag", "heading_text"])
    writer.writerow(["/checkboxes", "h3", "Checkboxes"])
    writer.writerow(["/dropdown", "h3", "Dropdown List"])
    writer.writerow(["/inputs", "h3", "Inputs"])


# ============================================
# DATA LOADING UTILITIES
# ============================================

class TestData:
    """Centralized test data loading."""

    _cache = {}

    @classmethod
    def load_json(cls, filename):
        """Load JSON with caching."""
        if filename not in cls._cache:
            path = os.path.join(DATA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                cls._cache[filename] = json.load(f)
        return cls._cache[filename]

    @classmethod
    def load_csv(cls, filename):
        """Load CSV as list of dicts with caching."""
        if filename not in cls._cache:
            path = os.path.join(DATA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                cls._cache[filename] = list(csv.DictReader(f))
        return cls._cache[filename]

    @classmethod
    def get_users(cls):
        return cls.load_json("test_users.json")

    @classmethod
    def get_pages(cls):
        return cls.load_csv("pages.csv")


# ============================================
# FIXTURES
# ============================================

@pytest.fixture(scope="session")
def test_data():
    """Provide TestData class to all tests."""
    return TestData()


@pytest.fixture
def valid_user(test_data):
    """Provide valid user credentials."""
    return test_data.get_users()["valid"]


@pytest.fixture
def login_page(page: Page):
    """Navigate to login page."""
    page.goto(f"{BASE_URL}/login")
    return page


@pytest.fixture
def logged_in_page(page: Page, valid_user):
    """Login with valid credentials from data file."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(valid_user["username"])
    page.locator("#password").fill(valid_user["password"])
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/secure")
    return page


# ============================================
# TESTS: Using fixtures with data
# ============================================

def test_valid_login(login_page, valid_user):
    """Login test using data fixture."""
    login_page.locator("#username").fill(valid_user["username"])
    login_page.locator("#password").fill(valid_user["password"])
    login_page.locator("button[type='submit']").click()
    assert "/secure" in login_page.url


def test_secure_area(logged_in_page):
    """Test using logged_in_page fixture (data-driven)."""
    assert "/secure" in logged_in_page.url
    heading = logged_in_page.locator("h2").text_content().strip()
    assert heading == "Secure Area"


# ============================================
# TESTS: Parametrized with data files
# ============================================

@pytest.mark.parametrize("user", TestData.get_users()["invalid"],
                         ids=lambda u: u["id"])
def test_invalid_logins(page: Page, user):
    """Parametrized test from JSON data."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("button[type='submit']").click()
    assert "/login" in page.url


@pytest.mark.parametrize("page_info", TestData.get_pages(),
                         ids=lambda p: p["path"])
def test_pages_from_csv(page: Page, page_info):
    """Parametrized test from CSV data."""
    page.goto(f"{BASE_URL}{page_info['path']}")
    heading = page.locator(page_info["heading_tag"]).first
    assert page_info["heading_text"] in heading.text_content()


# ============================================
# TESTS: With Faker (if available)
# ============================================

try:
    from faker import Faker
    FAKER_AVAILABLE = True
except ImportError:
    FAKER_AVAILABLE = False


@pytest.fixture
def fake():
    """Provide Faker instance."""
    if not FAKER_AVAILABLE:
        pytest.skip("Faker not installed")
    return Faker()


@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_random_invalid_login(page: Page, fake):
    """Test with random fake credentials."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(fake.user_name())
    page.locator("#password").fill(fake.password())
    page.locator("button[type='submit']").click()
    assert "/login" in page.url


@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_random_number_input(page: Page, fake):
    """Test input with random number."""
    number = str(fake.random_int(min=1, max=9999))
    page.goto(f"{BASE_URL}/inputs")
    page.locator("input[type='number']").fill(number)
    assert page.locator("input[type='number']").input_value() == number
    print(f"\n  Random number: {number}")


# ============================================
# RECOMMENDED PROJECT STRUCTURE
# ============================================
#
# project/
# ├── conftest.py          # Fixtures (data + page)
# ├── pytest.ini           # Config
# ├── .env                 # Secrets (gitignored!)
# ├── .env.example         # Template for .env
# ├── test_data/
# │   ├── users.json       # User credentials
# │   ├── pages.csv        # Page test data
# │   └── products.json    # Product data
# ├── pages/
# │   ├── base_page.py
# │   └── login_page.py
# ├── utils/
# │   └── data_loader.py   # TestData class
# └── tests/
#     ├── test_login.py
#     └── test_products.py
#


# ============================================
# KEY POINTS:
#
# 1. TestData class - centralized data loading
# 2. Caching prevents re-reading files
# 3. Fixtures wrap data for easy access
# 4. Parametrize with data from files
# 5. Faker for random/dynamic data
# 6. .env for sensitive credentials
# 7. Combine all sources in a clean structure
#
# Run: pytest 05_data_fixtures.py -v --headed -s
# ============================================
