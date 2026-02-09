"""Example 1: JSON Test Data

Demonstrates how to read test data from JSON files
and use it in pytest tests with Playwright.

Run with: pytest 01_json_test_data.py -v --headed
"""
import json
import os
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# LOADING JSON DATA
# ============================================

def load_json(file_path):
    """Load data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================
# CREATE SAMPLE JSON FILES
# ============================================
# In a real project, these files already exist.
# We create them here for demonstration.

EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EXAMPLES_DIR, "test_data")
os.makedirs(DATA_DIR, exist_ok=True)

# login_data.json
login_data = {
    "valid_user": {
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
        "expected_url": "/secure"
    },
    "invalid_users": [
        {
            "username": "wrong",
            "password": "wrong",
            "expected_error": "Your username is invalid!"
        },
        {
            "username": "tomsmith",
            "password": "bad_password",
            "expected_error": "Your password is invalid!"
        },
        {
            "username": "",
            "password": "",
            "expected_error": "Your username is invalid!"
        }
    ]
}

with open(os.path.join(DATA_DIR, "login_data.json"), "w", encoding="utf-8") as f:
    json.dump(login_data, f, indent=2, ensure_ascii=False)

# pages_data.json
pages_data = [
    {"path": "/login", "heading": "Login Page", "tag": "h2"},
    {"path": "/checkboxes", "heading": "Checkboxes", "tag": "h3"},
    {"path": "/dropdown", "heading": "Dropdown List", "tag": "h3"},
    {"path": "/inputs", "heading": "Inputs", "tag": "h3"},
]

with open(os.path.join(DATA_DIR, "pages_data.json"), "w", encoding="utf-8") as f:
    json.dump(pages_data, f, indent=2, ensure_ascii=False)


# ============================================
# TESTS USING JSON DATA
# ============================================

# Load data once
LOGIN_DATA = load_json(os.path.join(DATA_DIR, "login_data.json"))
PAGES_DATA = load_json(os.path.join(DATA_DIR, "pages_data.json"))


def test_valid_login(page: Page):
    """Test login with data from JSON."""
    data = LOGIN_DATA["valid_user"]

    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(data["username"])
    page.locator("#password").fill(data["password"])
    page.locator("button[type='submit']").click()

    assert data["expected_url"] in page.url


@pytest.mark.parametrize("user_data", LOGIN_DATA["invalid_users"],
                         ids=lambda d: d["username"] or "empty")
def test_invalid_login(page: Page, user_data):
    """Test invalid logins from JSON array."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(user_data["username"])
    page.locator("#password").fill(user_data["password"])
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash").text_content()
    assert user_data["expected_error"] in flash


@pytest.mark.parametrize("page_data", PAGES_DATA,
                         ids=lambda d: d["path"])
def test_page_headings(page: Page, page_data):
    """Test page headings from JSON array."""
    page.goto(f"{BASE_URL}{page_data['path']}")
    heading = page.locator(page_data["tag"]).first
    assert page_data["heading"] in heading.text_content()


# ============================================
# HELPER: Load and parametrize in one step
# ============================================

def json_test_data(file_name, key=None):
    """Load JSON and optionally extract a key."""
    data = load_json(os.path.join(DATA_DIR, file_name))
    if key:
        return data[key]
    return data


@pytest.mark.parametrize("user", json_test_data("login_data.json", "invalid_users"),
                         ids=lambda d: d["username"] or "empty")
def test_error_messages(page: Page, user):
    """Using helper function to load parametrized data."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("button[type='submit']").click()
    assert user["expected_error"] in page.locator("#flash").text_content()


# ============================================
# KEY POINTS:
#
# 1. json.load() reads JSON into Python dicts/lists
# 2. Separate data files from test logic
# 3. Use with @pytest.mark.parametrize
# 4. ids= for readable test names
# 5. Helper functions simplify data loading
# 6. Store JSON files in test_data/ directory
#
# Run: pytest 01_json_test_data.py -v --headed
# ============================================
