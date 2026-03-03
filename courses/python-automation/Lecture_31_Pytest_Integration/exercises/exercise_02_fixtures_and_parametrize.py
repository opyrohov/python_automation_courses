"""Exercise 2: Fixtures and Parametrize

Your task:
1. Create custom fixtures for reusable setup
2. Write parameterized tests
3. Add markers to categorize tests

Requirements:

Fixtures (use @pytest.fixture):
- checkbox_page: Navigate to checkboxes page, return page
- dropdown_page: Navigate to dropdown page, return page
- input_page: Navigate to inputs page, return page

Parameterized tests:
- test_dropdown_options: Test selecting different options (parametrize with values "1" and "2")
- test_login_credentials: Test different login credentials (valid and invalid)

Markers:
- Add @pytest.mark.smoke to critical tests
- Add @pytest.mark.regression to detailed tests

Run with:
    pytest exercise_02_fixtures_and_parametrize.py -v --headed
    pytest exercise_02_fixtures_and_parametrize.py -v -m smoke --headed
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# FIXTURES
# ============================================

# TODO: Create checkbox_page fixture
# @pytest.fixture
# def checkbox_page(page: Page):
#     # Navigate to checkboxes page
#     # Return page
#     pass


# TODO: Create dropdown_page fixture
# @pytest.fixture
# def dropdown_page(page: Page):
#     # Navigate to dropdown page
#     # Return page
#     pass


# TODO: Create input_page fixture
# @pytest.fixture
# def input_page(page: Page):
#     # Navigate to inputs page
#     # Return page
#     pass


# ============================================
# TESTS USING FIXTURES
# ============================================

# TODO: Write test using checkbox_page fixture
# @pytest.mark.smoke
# def test_checkboxes_visible(checkbox_page):
#     # Assert checkboxes are visible
#     pass


# TODO: Write test using dropdown_page fixture
# @pytest.mark.smoke
# def test_dropdown_visible(dropdown_page):
#     # Assert dropdown is visible
#     pass


# TODO: Write test using input_page fixture
# @pytest.mark.regression
# def test_input_accepts_numbers(input_page):
#     # Find the input field
#     # Fill with a number
#     # Assert the value
#     pass


# ============================================
# PARAMETERIZED TESTS
# ============================================

# TODO: Parametrize dropdown options test
# @pytest.mark.regression
# @pytest.mark.parametrize("value,expected_text", [
#     ("1", "Option 1"),
#     ("2", "Option 2"),
# ])
# def test_dropdown_options(dropdown_page, value, expected_text):
#     # Select the option by value
#     # Assert the selected option text matches expected_text
#     pass


# TODO: Parametrize login test
# @pytest.mark.parametrize("username,password,should_succeed", [
#     ("tomsmith", "SuperSecretPassword!", True),
#     ("wrong", "wrong", False),
#     ("tomsmith", "bad_password", False),
# ])
# def test_login_credentials(page: Page, username, password, should_succeed):
#     # Navigate to login page
#     # Fill username and password
#     # Click login button
#     # Assert based on should_succeed:
#     #   True: URL contains "/secure"
#     #   False: URL contains "/login"
#     pass


# ============================================
# BONUS: FIXTURE WITH YIELD
# ============================================

# TODO: Create a fixture with setup and teardown
# @pytest.fixture
# def add_remove_page(page: Page):
#     # SETUP: Navigate to add/remove elements page
#     page.goto(f"{BASE_URL}/add_remove_elements/")
#
#     yield page
#
#     # TEARDOWN: Print how many elements were added
#     count = page.locator(".added-manually").count()
#     print(f"\n[Teardown] {count} elements remaining")


# TODO: Write test using add_remove_page fixture
# @pytest.mark.regression
# def test_add_elements(add_remove_page):
#     # Click "Add Element" button 3 times
#     # Assert 3 "Delete" buttons appear
#     pass
