"""Exercise 1: Comprehensive Login Test Suite with Parametrize

Your task:
1. Create a complete login test suite using various parametrize patterns
2. Use custom IDs, pytest.param with marks, and dict parameters
3. Include valid, invalid, edge cases, and expected failures

Requirements:

Tests to write:
- test_login_scenarios: Parametrize with tuples (username, password, expected_url)
  Include: valid login, wrong username, wrong password, empty fields
  Use custom ids

- test_login_error_messages: Parametrize with dicts containing username, password, error
  Use ids=lambda for dynamic names

- test_login_with_marks: Use pytest.param to mark specific cases
  Include one xfail case and one regular case

- test_login_table: Use the table pattern with comment header

Bonus:
- test_login_class: Class-level parametrize applied to multiple methods

Run with: pytest exercise_01_data_driven_login.py -v --headed
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# TODO: test_login_scenarios (tuple params + ids)
# ============================================

# @pytest.mark.parametrize("username,password,expected_url", [
#     ("tomsmith", "SuperSecretPassword!", "/secure"),
#     ("wrong", "wrong", "/login"),
#     ("tomsmith", "bad_password", "/login"),
#     ("", "", "/login"),
# ], ids=["valid", "bad_user", "bad_pass", "empty"])
# def test_login_scenarios(page: Page, username, password, expected_url):
#     page.goto(f"{BASE_URL}/login")
#     page.locator("#username").fill(username)
#     page.locator("#password").fill(password)
#     page.locator("button[type='submit']").click()
#     assert expected_url in page.url


# ============================================
# TODO: test_login_error_messages (dict params)
# ============================================

# ERROR_CASES = [
#     {"username": "wrong", "password": "SuperSecretPassword!", "error": "Your username is invalid!"},
#     {"username": "tomsmith", "password": "wrong", "error": "Your password is invalid!"},
# ]
#
# @pytest.mark.parametrize("case", ERROR_CASES, ids=lambda c: c["username"])
# def test_login_error_messages(page: Page, case):
#     # Navigate, fill, click, check error message in #flash
#     pass


# ============================================
# TODO: test_login_with_marks (pytest.param)
# ============================================

# @pytest.mark.parametrize("username,password,succeeds", [
#     pytest.param("tomsmith", "SuperSecretPassword!", True, id="valid"),
#     pytest.param("wrong", "wrong", False, id="invalid"),
#     pytest.param("admin", "admin", True, id="admin_guess",
#                  marks=pytest.mark.xfail(reason="admin is not a valid user")),
# ])
# def test_login_with_marks(page: Page, username, password, succeeds):
#     pass


# ============================================
# TODO: test_login_table (table pattern)
# ============================================

# TEST_TABLE = [
#     # username      password                   success  error_fragment
#     ("tomsmith",    "SuperSecretPassword!",     True,    None),
#     ("wrong",       "SuperSecretPassword!",     False,   "username is invalid"),
#     ("tomsmith",    "wrong",                    False,   "password is invalid"),
# ]
#
# @pytest.mark.parametrize("username,password,success,error", TEST_TABLE,
#                          ids=["valid", "bad_user", "bad_pass"])
# def test_login_table(page: Page, username, password, success, error):
#     pass


# ============================================
# BONUS: Class-level parametrize
# ============================================

# @pytest.mark.parametrize("username,password", [
#     ("tomsmith", "SuperSecretPassword!"),
# ])
# class TestLoginFlow:
#     def test_can_login(self, page: Page, username, password):
#         pass
#
#     def test_sees_secure_area(self, page: Page, username, password):
#         pass
