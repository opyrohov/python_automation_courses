"""Exercise 1: Write Basic Pytest Tests

Your task:
1. Write test functions for the Checkboxes page
2. Write test functions for the Dropdown page
3. All tests should use the 'page' fixture
4. Use proper assertions

Target pages:
- Checkboxes: https://the-internet.herokuapp.com/checkboxes
- Dropdown: https://the-internet.herokuapp.com/dropdown

Requirements:
- test_checkboxes_page_loads: Verify page loads with heading "Checkboxes"
- test_two_checkboxes_present: Verify exactly 2 checkboxes exist
- test_check_first_checkbox: Check first checkbox and verify it's checked
- test_uncheck_second_checkbox: Uncheck second checkbox and verify
- test_dropdown_page_loads: Verify dropdown page loads
- test_select_option_1: Select "Option 1" and verify selection
- test_select_option_2: Select "Option 2" and verify selection

Run with: pytest exercise_01_write_basic_tests.py -v --headed
"""
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# CHECKBOX TESTS
# ============================================

# TODO: Write test_checkboxes_page_loads
# def test_checkboxes_page_loads(page: Page):
#     # Navigate to checkboxes page
#     # Assert heading text is "Checkboxes"
#     pass


# TODO: Write test_two_checkboxes_present
# def test_two_checkboxes_present(page: Page):
#     # Navigate to checkboxes page
#     # Assert there are exactly 2 checkboxes
#     pass


# TODO: Write test_check_first_checkbox
# def test_check_first_checkbox(page: Page):
#     # Navigate to checkboxes page
#     # Check the first checkbox using .check()
#     # Assert it is checked using .is_checked()
#     pass


# TODO: Write test_uncheck_second_checkbox
# def test_uncheck_second_checkbox(page: Page):
#     # Navigate to checkboxes page
#     # Uncheck the second checkbox using .uncheck()
#     # Assert it is NOT checked
#     pass


# ============================================
# DROPDOWN TESTS
# ============================================

# TODO: Write test_dropdown_page_loads
# def test_dropdown_page_loads(page: Page):
#     # Navigate to dropdown page
#     # Assert heading is "Dropdown List"
#     pass


# TODO: Write test_select_option_1
# def test_select_option_1(page: Page):
#     # Navigate to dropdown page
#     # Select "Option 1" using select_option(value="1")
#     # Assert selected value
#     pass


# TODO: Write test_select_option_2
# def test_select_option_2(page: Page):
#     # Navigate to dropdown page
#     # Select "Option 2" using select_option(value="2")
#     # Assert selected value
#     pass
