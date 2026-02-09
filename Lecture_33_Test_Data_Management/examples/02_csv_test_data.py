"""Example 2: CSV Test Data

Demonstrates how to read test data from CSV files
and use it with pytest parametrize.

Run with: pytest 02_csv_test_data.py -v --headed
"""
import csv
import os
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"

EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EXAMPLES_DIR, "test_data")
os.makedirs(DATA_DIR, exist_ok=True)


# ============================================
# CREATE SAMPLE CSV FILES
# ============================================

# login_data.csv
csv_login_data = [
    ["username", "password", "should_succeed", "expected_message"],
    ["tomsmith", "SuperSecretPassword!", "true", "You logged into a secure area!"],
    ["wrong", "wrong", "false", "Your username is invalid!"],
    ["tomsmith", "bad_password", "false", "Your password is invalid!"],
]

with open(os.path.join(DATA_DIR, "login_data.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(csv_login_data)

# dropdown_data.csv
csv_dropdown_data = [
    ["value", "expected_text"],
    ["1", "Option 1"],
    ["2", "Option 2"],
]

with open(os.path.join(DATA_DIR, "dropdown_data.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(csv_dropdown_data)


# ============================================
# LOADING CSV DATA
# ============================================

def load_csv(file_path):
    """Load CSV file as list of dictionaries."""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_csv_tuples(file_path):
    """Load CSV file as list of tuples (skip header)."""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        return [tuple(row) for row in reader]


# ============================================
# TESTS WITH CSV DATA (DictReader)
# ============================================

LOGIN_DATA = load_csv(os.path.join(DATA_DIR, "login_data.csv"))


@pytest.mark.parametrize("row", LOGIN_DATA,
                         ids=lambda r: r["username"] or "empty")
def test_login_from_csv(page: Page, row):
    """Test login scenarios from CSV file."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(row["username"])
    page.locator("#password").fill(row["password"])
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash").text_content()
    assert row["expected_message"] in flash

    # CSV values are always strings - convert to bool
    should_succeed = row["should_succeed"].lower() == "true"
    if should_succeed:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# TESTS WITH CSV DATA (Tuples)
# ============================================

DROPDOWN_DATA = load_csv_tuples(os.path.join(DATA_DIR, "dropdown_data.csv"))


@pytest.mark.parametrize("value,expected_text", DROPDOWN_DATA)
def test_dropdown_from_csv(page: Page, value, expected_text):
    """Test dropdown options from CSV file."""
    page.goto(f"{BASE_URL}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(value=value)

    selected = dropdown.locator("option:checked")
    assert selected.text_content().strip() == expected_text


# ============================================
# CSV vs JSON COMPARISON
# ============================================
#
# CSV Advantages:
#   + Easy to edit in Excel/Google Sheets
#   + Great for tabular data
#   + Non-technical people can edit
#   + Smaller file size
#
# CSV Disadvantages:
#   - All values are strings (need conversion)
#   - No nested data
#   - No comments
#
# JSON Advantages:
#   + Supports types (int, bool, null)
#   + Nested structures
#   + More flexible
#
# JSON Disadvantages:
#   - Harder to edit without IDE
#   - More verbose
#
# RECOMMENDATION:
#   - CSV for simple tabular test data
#   - JSON for complex/nested data
#


# ============================================
# HELPER: Generic CSV parametrize
# ============================================

def csv_data(file_name):
    """Load CSV data for parametrize from test_data/ directory."""
    return load_csv(os.path.join(DATA_DIR, file_name))


@pytest.mark.parametrize("row", csv_data("dropdown_data.csv"))
def test_dropdown_with_helper(page: Page, row):
    """Using helper to load CSV data."""
    page.goto(f"{BASE_URL}/dropdown")
    page.locator("#dropdown").select_option(value=row["value"])
    selected = page.locator("#dropdown option:checked")
    assert row["expected_text"] in selected.text_content()


# ============================================
# KEY POINTS:
#
# 1. csv.DictReader - rows as dictionaries
# 2. csv.reader - rows as lists/tuples
# 3. CSV values are ALWAYS strings
# 4. Convert types manually (bool, int)
# 5. Good for tabular, simple data
# 6. Use JSON for complex/nested data
# 7. Helper functions simplify loading
#
# Run: pytest 02_csv_test_data.py -v --headed
# ============================================
