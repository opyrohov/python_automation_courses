"""Example 4: Dynamic Test Generation

Demonstrates how to generate test cases programmatically
using pytest_generate_tests hook and data files.

Run with: pytest 04_dynamic_generation.py -v --headed -s
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
# CREATE SAMPLE DATA FILES
# ============================================

# pages.json
pages_data = [
    {"path": "/login", "heading": "Login Page", "tag": "h2"},
    {"path": "/checkboxes", "heading": "Checkboxes", "tag": "h3"},
    {"path": "/dropdown", "heading": "Dropdown List", "tag": "h3"},
    {"path": "/inputs", "heading": "Inputs", "tag": "h3"},
]

with open(os.path.join(DATA_DIR, "pages.json"), "w") as f:
    json.dump(pages_data, f, indent=2)

# login_cases.csv
with open(os.path.join(DATA_DIR, "login_cases.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["username", "password", "expected_url"])
    writer.writerow(["tomsmith", "SuperSecretPassword!", "/secure"])
    writer.writerow(["wrong", "wrong", "/login"])
    writer.writerow(["tomsmith", "bad", "/login"])


# ============================================
# pytest_generate_tests HOOK
# ============================================
# This hook is called for each test function
# and allows dynamic parametrization.

def pytest_generate_tests(metafunc):
    """Dynamically generate test parameters."""

    # If test uses 'page_data' fixture, load from JSON
    if "page_data" in metafunc.fixturenames:
        path = os.path.join(DATA_DIR, "pages.json")
        with open(path) as f:
            data = json.load(f)
        metafunc.parametrize(
            "page_data",
            data,
            ids=[d["path"] for d in data],
        )

    # If test uses 'login_case' fixture, load from CSV
    if "login_case" in metafunc.fixturenames:
        path = os.path.join(DATA_DIR, "login_cases.csv")
        with open(path) as f:
            rows = list(csv.DictReader(f))
        metafunc.parametrize(
            "login_case",
            rows,
            ids=[r["username"] or "empty" for r in rows],
        )


# ============================================
# TESTS USING DYNAMIC PARAMETERS
# ============================================

def test_page_heading(page: Page, page_data):
    """Test parametrized dynamically from JSON."""
    page.goto(f"{BASE_URL}{page_data['path']}")
    heading = page.locator(page_data["tag"]).first
    assert page_data["heading"] in heading.text_content()


def test_login_case(page: Page, login_case):
    """Test parametrized dynamically from CSV."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(login_case["username"])
    page.locator("#password").fill(login_case["password"])
    page.locator("button[type='submit']").click()
    assert login_case["expected_url"] in page.url


# ============================================
# GENERATING FROM A FUNCTION
# ============================================

def generate_number_cases():
    """Generate test cases programmatically."""
    cases = []
    for i in range(1, 6):
        cases.append(pytest.param(
            str(i * 10),
            id=f"number_{i*10}",
        ))
    return cases


@pytest.mark.parametrize("number", generate_number_cases())
def test_number_input(page: Page, number):
    """Test with programmatically generated numbers."""
    page.goto(f"{BASE_URL}/inputs")
    input_field = page.locator("input[type='number']")
    input_field.fill(number)
    assert input_field.input_value() == number
    print(f"\n  Entered: {number}")


# ============================================
# CONDITIONAL GENERATION
# ============================================

def get_test_data_for_env():
    """Return different data based on environment."""
    env = os.environ.get("TEST_ENV", "dev")

    if env == "prod":
        # Fewer tests in production
        return ["/login", "/checkboxes"]
    else:
        # Full tests in dev
        return ["/login", "/checkboxes", "/dropdown", "/inputs"]


@pytest.mark.parametrize("path", get_test_data_for_env())
def test_environment_specific(page: Page, path):
    """Different test sets for different environments."""
    page.goto(f"{BASE_URL}{path}")
    assert page.title() == "The Internet"


# ============================================
# KEY POINTS:
#
# 1. pytest_generate_tests hook for dynamic params
# 2. metafunc.parametrize() in the hook
# 3. Check metafunc.fixturenames for which tests need data
# 4. Generator functions for computed parameters
# 5. Environment-based test data selection
# 6. Load from any source: JSON, CSV, DB, API
# 7. Most flexible approach for complex scenarios
#
# Run: pytest 04_dynamic_generation.py -v --headed -s
# ============================================
