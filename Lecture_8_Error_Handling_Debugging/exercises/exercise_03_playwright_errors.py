"""
Lecture 8 - Exercise 3: Playwright Error Handling
=================================================
Practice handling Playwright-specific errors in automation tests.

Instructions:
1. Complete each TODO section
2. These are patterns - actual Playwright code is commented
3. Focus on error handling logic
4. Check your solutions against SOLUTIONS.md
"""

print("=" * 50)
print("EXERCISE: Playwright Error Handling")
print("=" * 50)
print()

from pathlib import Path
from datetime import datetime
import time

# Exercise 3.1: Safe Click Function
# =================================
# TODO: Create a function safe_click(page, selector, timeout=5000) that:
# - Tries to click the element
# - Handles TimeoutError
# - Takes a screenshot on error
# - Returns True/False for success

# Your code here:


# Test pattern:
# safe_click(page, "#submit")
# safe_click(page, "#missing-element")

print("-" * 50)


# Exercise 3.2: Retry Click Function
# ==================================
# TODO: Create a function retry_click(page, selector, retries=3) that:
# - Attempts to click with retries
# - Waits 1 second between retries
# - Returns True if successful, False if all retries fail
# - Logs each attempt

# Your code here:


# Test pattern:
# retry_click(page, "#flaky-button", retries=3)

print("-" * 50)


# Exercise 3.3: Safe Navigation
# =============================
# TODO: Create a function safe_goto(page, url, timeout=30000) that:
# - Navigates to the URL
# - Handles TimeoutError
# - Checks response status code
# - Returns True/False for success

# Your code here:


# Test pattern:
# safe_goto(page, "https://example.com")
# safe_goto(page, "https://invalid-url-12345.com")

print("-" * 50)


# Exercise 3.4: Wait for Element
# ==============================
# TODO: Create a function wait_for_element(page, selector, timeout=10000) that:
# - Waits for element to be visible
# - Handles TimeoutError
# - Returns True if found, False otherwise
# - Takes screenshot on timeout

# Your code here:


# Test pattern:
# wait_for_element(page, "#submit-button")
# wait_for_element(page, "#slow-loading-element", timeout=20000)

print("-" * 50)


# Exercise 3.5: Safe Text Extraction
# ==================================
# TODO: Create a function safe_get_text(page, selector) that:
# - Gets text content from element
# - Handles element not found
# - Returns text or None
# - Logs warning if element not found

# Your code here:


# Test pattern:
# text = safe_get_text(page, "h1")
# text = safe_get_text(page, "#missing-element")

print("-" * 50)


# Exercise 3.6: Safe Form Fill
# ============================
# TODO: Create a function safe_fill(page, selector, value) that:
# - Fills input field with value
# - Checks if element is enabled
# - Handles TimeoutError
# - Returns True/False for success

# Your code here:


# Test pattern:
# safe_fill(page, "#username", "testuser")
# safe_fill(page, "#disabled-input", "value")

print("-" * 50)


# Exercise 3.7: Screenshot on Error Decorator
# ===========================================
# TODO: Create a decorator screenshot_on_error(page) that:
# - Wraps test functions
# - Takes screenshot if exception occurs
# - Saves with timestamp and test name
# - Re-raises the exception

# Your code here:


# Test pattern:
# @screenshot_on_error(page)
# def test_login(page):
#     page.click("#submit")

print("-" * 50)


# Exercise 3.8: Page State Validator
# ==================================
# TODO: Create a function validate_page_loaded(page, expected_title) that:
# - Checks page title matches expected
# - Checks page is not loading
# - Raises custom PageNotLoadedError if issues
# - Takes screenshot on error

# Your code here:


# Test pattern:
# validate_page_loaded(page, "Home Page")
# validate_page_loaded(page, "Wrong Title")  # Should raise error

print("-" * 50)


# Exercise 3.9: Test Context Manager
# ==================================
# TODO: Create a class TestContext that:
# - Accepts test_name in __init__
# - Sets up browser in __enter__
# - Takes screenshot on failure in __exit__
# - Closes browser in __exit__
# - Logs test start/end

# Your code here:


# Usage pattern:
# with TestContext("test_login") as ctx:
#     # Test code here
#     pass

print("-" * 50)


# Exercise 3.10: Comprehensive Error Handler
# ==========================================
# TODO: Create a function handle_playwright_error(error, page, context) that:
# - Checks error type (Timeout, Navigation, etc.)
# - Provides specific suggestions based on error type
# - Takes screenshot
# - Logs error details with context
# - Returns error report dictionary

# Your code here:


# Test pattern:
# try:
#     page.click("#missing", timeout=5000)
# except Exception as e:
#     report = handle_playwright_error(e, page, "Clicking submit button")
#     print(report)

print("-" * 50)


# BONUS 1: Element Presence Checker
# =================================
# TODO: Create a function check_elements_exist(page, selectors) that:
# - Takes a list of selectors
# - Checks each element exists
# - Returns dict with selector: exists status
# - Logs missing elements

# Your code here:


# Test pattern:
# selectors = ["#username", "#password", "#submit", "#missing"]
# results = check_elements_exist(page, selectors)
# print(results)

print("-" * 50)


# BONUS 2: Robust Test Runner
# ===========================
# TODO: Create a class RobustTestRunner that:
# - Runs multiple test functions
# - Handles errors in each test
# - Takes screenshots on failures
# - Collects results (passed/failed)
# - Generates summary report

# Your code here:


# Usage pattern:
# def test_1(page):
#     page.click("#button1")
#
# def test_2(page):
#     page.click("#button2")
#
# runner = RobustTestRunner(page)
# runner.add_test("Test 1", test_1)
# runner.add_test("Test 2", test_2)
# report = runner.run_all()
# print(report)

print("-" * 50)


# BONUS 3: Smart Retry with Exponential Backoff
# =============================================
# TODO: Create a function retry_with_backoff(func, max_retries=3) that:
# - Retries function with exponential backoff
# - Wait times: 1s, 2s, 4s, 8s...
# - Logs each attempt and wait time
# - Returns result or raises last exception

# Your code here:


# Test pattern:
# def flaky_operation():
#     # Simulated flaky operation
#     import random
#     if random.random() < 0.7:
#         raise Exception("Temporary failure")
#     return "Success"
#
# result = retry_with_backoff(flaky_operation, max_retries=5)

print("-" * 50)

print("=" * 50)
print("Exercise 3 Complete!")
print("Check SOLUTIONS.md for answers")
print("=" * 50)


# Notes for Actual Playwright Implementation
# ==========================================
print("\n" + "=" * 50)
print("ACTUAL PLAYWRIGHT USAGE")
print("=" * 50)
print("""
To use these patterns with real Playwright:

1. Install Playwright:
   pip install playwright
   playwright install

2. Import Playwright:
   from playwright.sync_api import sync_playwright, TimeoutError

3. Basic structure:
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()

       try:
           # Your test code with error handling
           safe_click(page, "#button")
       except Exception as e:
           handle_playwright_error(e, page, "test context")
       finally:
           browser.close()

4. Error types to handle:
   - TimeoutError: Element not found in time
   - Error: Generic Playwright errors
   - Exception: Catch-all for unexpected issues

5. Best practices:
   - Always use try/except for Playwright operations
   - Take screenshots on errors
   - Use reasonable timeouts
   - Clean up resources in finally block
   - Log all errors with context
""")
