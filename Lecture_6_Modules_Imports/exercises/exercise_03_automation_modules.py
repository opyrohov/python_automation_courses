"""
Lecture 6 - Exercise 3: Automation Modules
=========================================
Practice organizing automation code with modules.

Instructions:
1. Complete each TODO section
2. Create the required module files
3. Test your code by running: python exercise_03_automation_modules.py
4. Check your solutions against SOLUTIONS.md
"""

import sys
from pathlib import Path

# Add parent directory to path
parent_dir = Path(__file__).parent
sys.path.insert(0, str(parent_dir))

print("=" * 50)
print("EXERCISE: Automation Modules")
print("=" * 50)
print()

# Exercise 3.1: Create a Browser Config Module
# ============================================
# TODO: Create 'browser_config.py' with:
#   - BROWSERS = ["chrome", "firefox", "safari"]
#   - DEFAULT_BROWSER = "chrome"
#   - HEADLESS = False
#   - SLOW_MO = 100
#   - get_browser_config(browser_name): Returns config for browser

# Import and use it:

# Your code here:
# from browser_config import BROWSERS, DEFAULT_BROWSER, get_browser_config


print("-" * 50)


# Exercise 3.2: Create a Locators Module
# ======================================
# TODO: Create 'locators.py' with a class for login page locators:
# class LoginPageLocators:
#     USERNAME_INPUT = "#username"
#     PASSWORD_INPUT = "#password"
#     LOGIN_BUTTON = "#login-btn"
#     ERROR_MESSAGE = ".error-message"

# Import and use the locators:

# Your code here:
# from locators import LoginPageLocators


print("-" * 50)


# Exercise 3.3: Create a Wait Helpers Module
# ==========================================
# TODO: Create 'wait_helpers.py' with these functions:
#   - wait_for_element(selector, timeout=10): Simulates waiting
#   - wait_for_text(text, timeout=10): Simulates waiting for text
#   - wait_for_url(url, timeout=10): Simulates waiting for URL

# Import and test:

# Your code here:
# from wait_helpers import wait_for_element, wait_for_text, wait_for_url


print("-" * 50)


# Exercise 3.4: Create a Screenshot Helper Module
# ===============================================
# TODO: Create 'screenshot_helper.py' with:
#   - take_screenshot(name): Returns screenshot path with timestamp
#   - take_full_page_screenshot(name): Returns full page screenshot path
#   - create_screenshots_dir(): Creates screenshots folder if not exists

# Import and test:

# Your code here:
# from screenshot_helper import take_screenshot, create_screenshots_dir


print("-" * 50)


# Exercise 3.5: Create Test Data Module
# =====================================
# TODO: Create 'test_data.py' with:
# TEST_USERS = {
#     "valid": {"username": "testuser", "password": "Test123!"},
#     "invalid": {"username": "bad", "password": "wrong"},
#     "admin": {"username": "admin", "password": "Admin123!"}
# }
#
# TEST_URLS = {
#     "login": "https://example.com/login",
#     "home": "https://example.com/home",
#     "profile": "https://example.com/profile"
# }

# Import and use:

# Your code here:
# from test_data import TEST_USERS, TEST_URLS


print("-" * 50)


# Exercise 3.6: Create an Actions Helper Module
# =============================================
# TODO: Create 'actions.py' with these functions:
#   - click_element(selector): Simulates click
#   - fill_field(selector, value): Simulates fill
#   - select_option(selector, value): Simulates select
#   - clear_field(selector): Simulates clear

# Import and test:

# Your code here:
# from actions import click_element, fill_field, select_option


print("-" * 50)


# Exercise 3.7: Create an Assertions Module
# =========================================
# TODO: Create 'assertions.py' with:
#   - assert_text_present(text): Checks if text exists
#   - assert_element_visible(selector): Checks if element visible
#   - assert_url_contains(expected_url): Checks if URL matches
#   - assert_title(expected_title): Checks page title

# Import and test:

# Your code here:
# from assertions import assert_text_present, assert_element_visible


print("-" * 50)


# Exercise 3.8: Create a Logger Module
# ====================================
# TODO: Create 'test_logger.py' with:
#   - log_info(message): Logs info message with timestamp
#   - log_error(message): Logs error message with timestamp
#   - log_test_start(test_name): Logs test start
#   - log_test_end(test_name, status): Logs test end with status

# Import and test:

# Your code here:
# from test_logger import log_info, log_error, log_test_start, log_test_end


print("-" * 50)


# Exercise 3.9: Create a Complete Test Using Your Modules
# =======================================================
# TODO: Create a function that uses multiple modules you created:
# def test_login_flow():
#     - Use test_logger to log start
#     - Use test_data to get test user
#     - Use browser_config to get config
#     - Use locators for element selectors
#     - Use actions to interact with page
#     - Use assertions to verify results
#     - Use test_logger to log end

# Your code here:


print("-" * 50)


# Exercise 3.10: Understanding Module Organization
# ================================================
# TODO: Describe how you would organize a real test project
# Print your proposed folder structure

print("Proposed test project structure:")
# Your structure here:
structure = """
test_project/
├── tests/
│   ├── test_login.py
│   ├── test_search.py
├── pages/
│   ├── login_page.py
├── utils/
│   ├── helpers.py
├── config/
│   ├── settings.py
└── requirements.txt
"""
print(structure)

print("-" * 50)


# BONUS Exercise: Import Pattern Practice
# =======================================
# TODO: Write examples of different import patterns for Playwright:
# 1. Import sync_playwright
# 2. Import Page, Browser, expect
# 3. Import from pytest_playwright

print("Playwright import patterns:")
examples = """
# Pattern 1: Basic sync API
from playwright.sync_api import sync_playwright

# Pattern 2: Specific classes
from playwright.sync_api import Page, Browser, BrowserContext, expect

# Pattern 3: For pytest
import pytest
from playwright.sync_api import Page

def test_example(page: Page):
    pass
"""
print(examples)

print("=" * 50)
print("Exercise 3 Complete!")
print("You've mastered organizing automation code!")
print("Compare your solutions with SOLUTIONS.md")
print("=" * 50)
