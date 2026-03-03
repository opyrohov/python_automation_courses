"""Exercise 1: Data-Driven Tests from JSON and CSV

Your task:
1. Create JSON and CSV test data files
2. Write helper functions to load the data
3. Write parametrized tests using the data

Requirements:

Data files to create (in test_data/ folder):
- login_scenarios.json with valid and invalid login data
- dropdown_options.csv with value and expected text

Tests to write:
- test_valid_login: Login with valid data from JSON
- test_invalid_login: Parametrized with invalid users from JSON
- test_dropdown_selection: Parametrized with CSV data
- test_page_navigation: Parametrized with JSON array of pages

Run with: pytest exercise_01_data_driven_tests.py -v --headed
"""
import json
import csv
import os
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"
EXERCISE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EXERCISE_DIR, "test_data")


# ============================================
# TODO: Create test data files
# ============================================

# TODO: Create DATA_DIR if it doesn't exist
# os.makedirs(DATA_DIR, exist_ok=True)

# TODO: Create login_scenarios.json
# Structure:
# {
#   "valid": {"username": "tomsmith", "password": "SuperSecretPassword!"},
#   "invalid": [
#     {"username": "wrong", "password": "wrong", "error": "Your username is invalid!"},
#     {"username": "tomsmith", "password": "bad", "error": "Your password is invalid!"}
#   ]
# }

# TODO: Create dropdown_options.csv
# Columns: value, expected_text
# Rows: "1","Option 1" and "2","Option 2"


# ============================================
# TODO: Helper functions
# ============================================

# def load_json(filename):
#     """Load JSON from test_data/ directory."""
#     path = os.path.join(DATA_DIR, filename)
#     with open(path, "r", encoding="utf-8") as f:
#         return json.load(f)

# def load_csv(filename):
#     """Load CSV from test_data/ directory as list of dicts."""
#     path = os.path.join(DATA_DIR, filename)
#     with open(path, "r", encoding="utf-8") as f:
#         return list(csv.DictReader(f))


# ============================================
# TODO: Tests
# ============================================

# def test_valid_login(page: Page):
#     """Login with valid credentials from JSON."""
#     data = load_json("login_scenarios.json")
#     user = data["valid"]
#     page.goto(f"{BASE_URL}/login")
#     page.locator("#username").fill(user["username"])
#     page.locator("#password").fill(user["password"])
#     page.locator("button[type='submit']").click()
#     assert "/secure" in page.url


# @pytest.mark.parametrize("user", ...)
# def test_invalid_login(page: Page, user):
#     """Parametrized invalid login from JSON."""
#     page.goto(f"{BASE_URL}/login")
#     page.locator("#username").fill(user["username"])
#     page.locator("#password").fill(user["password"])
#     page.locator("button[type='submit']").click()
#     assert user["error"] in page.locator("#flash").text_content()


# @pytest.mark.parametrize("row", ...)
# def test_dropdown_selection(page: Page, row):
#     """Parametrized dropdown test from CSV."""
#     page.goto(f"{BASE_URL}/dropdown")
#     page.locator("#dropdown").select_option(value=row["value"])
#     selected = page.locator("#dropdown option:checked")
#     assert row["expected_text"] in selected.text_content()
