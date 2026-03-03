"""Exercise 1: Set Up Complete Project Configuration

Your task:
1. Create pytest.ini with proper settings
2. Create conftest.py with browser and context configuration
3. Write tests that use the configuration

Requirements:

pytest.ini should include:
- addopts: -v --tb=short
- base_url: https://the-internet.herokuapp.com
- markers: smoke, regression

conftest.py should include:
- browser_type_launch_args: headless=False, slow_mo=300
- browser_context_args: viewport 1280x720, ignore_https_errors=True
- base_url fixture returning the-internet URL
- login_page fixture that navigates to /login
- logged_in_page fixture that logs in with valid credentials
- A fixture that sets default timeouts (10s actions, 15s navigation)

Tests to write:
- test_homepage_loads: Verify homepage loads (use base_url)
- test_login_page_elements: Verify login page elements (use login_page fixture)
- test_secure_area: Verify access after login (use logged_in_page fixture)
- test_viewport_configured: Verify viewport is 1280x720

Run with: pytest exercise_01_project_config.py -v --headed
"""
import pytest
from playwright.sync_api import Page


# ============================================
# CONFIGURATION FIXTURES
# ============================================
# In a real project, these go in conftest.py
# They are here for exercise purposes

# TODO: Create browser_type_launch_args fixture
# @pytest.fixture(scope="session")
# def browser_type_launch_args():
#     return {
#         # headless, slow_mo
#     }


# TODO: Create browser_context_args fixture
# @pytest.fixture(scope="session")
# def browser_context_args():
#     return {
#         # viewport, ignore_https_errors
#     }


# TODO: Create base_url fixture
# @pytest.fixture(scope="session")
# def base_url():
#     return "..."


# TODO: Create timeout setup fixture (autouse=True)
# @pytest.fixture(autouse=True)
# def setup_timeouts(page):
#     # set_default_timeout
#     # set_default_navigation_timeout
#     yield page


# ============================================
# PAGE FIXTURES
# ============================================

# TODO: Create login_page fixture
# @pytest.fixture
# def login_page(page, base_url):
#     # Navigate to login page using base_url
#     # Return page
#     pass


# TODO: Create logged_in_page fixture
# @pytest.fixture
# def logged_in_page(page, base_url):
#     # Navigate to login, fill credentials, click login
#     # Wait for /secure URL
#     # Return page
#     pass


# ============================================
# TESTS
# ============================================

# TODO: test_homepage_loads
# @pytest.mark.smoke
# def test_homepage_loads(page, base_url):
#     # goto base_url
#     # assert title == "The Internet"
#     pass


# TODO: test_login_page_elements
# @pytest.mark.smoke
# def test_login_page_elements(login_page):
#     # assert username input visible
#     # assert password input visible
#     # assert login button visible
#     pass


# TODO: test_secure_area
# @pytest.mark.regression
# def test_secure_area(logged_in_page):
#     # assert URL contains /secure
#     # assert heading text
#     pass


# TODO: test_viewport_configured
# def test_viewport_configured(page, base_url):
#     # goto base_url
#     # get viewport_size
#     # assert width == 1280 and height == 720
#     pass
