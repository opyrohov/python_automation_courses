"""
Exercise 4: Complete Workflow Practice
Build complete automation workflows combining all concepts
"""

from playwright.sync_api import sync_playwright


def exercise_1_simple_workflow():
    """
    Exercise 1: Simple Login Workflow

    Task:
    Build a workflow that:
    1. Creates a simple login page with HTML
    2. Navigates to the page
    3. Fills username and password
    4. Clicks submit
    5. Verifies success message
    6. Prints confirmation

    HTML structure:
    - Username input (name="username")
    - Password input (name="password")
    - Submit button
    - Result div to show success/error

    Expected output:
    - Form should be filled
    - Submit should be clicked
    - Success message should be verified
    """
    # TODO: Implement this exercise
    pass


def exercise_2_multi_page_workflow():
    """
    Exercise 2: Multi-Page Data Extraction

    Task:
    1. Navigate to 3 different websites
    2. For each website, extract:
       - Page title
       - Current URL
       - Response status
       - Content length
    3. Store data in a list
    4. Print a formatted summary table

    Websites to use:
    - https://example.com
    - https://playwright.dev
    - https://python.org

    Expected output:
    - Formatted table with all data
    - All 3 websites processed
    """
    # TODO: Implement this exercise
    pass


def exercise_3_shopping_flow():
    """
    Exercise 3: E-commerce Shopping Flow

    Task:
    Create an HTML page simulating shopping and automate:
    1. Product page - click "Add to Cart"
    2. Cart page - click "Checkout"
    3. Checkout page - fill shipping info
    4. Confirmation page - verify order

    Include:
    - Navigation between pages
    - Form filling
    - Click interactions
    - Verification steps

    Expected output:
    - Complete shopping flow
    - All steps verified
    - Confirmation message printed
    """
    # TODO: Implement this exercise
    pass


def exercise_4_error_handling_workflow():
    """
    Exercise 4: Workflow with Error Handling

    Task:
    Build a workflow with proper error handling:
    1. Try to navigate to a URL (may fail)
    2. Try to click an element (may not exist)
    3. Try to fill a form (may timeout)
    4. Take screenshot on any error
    5. Log all errors
    6. Ensure browser closes even on error

    Use try/except/finally blocks properly.

    Expected output:
    - Proper error messages
    - Screenshot on error
    - Browser always closes
    """
    # TODO: Implement this exercise
    pass


def exercise_5_page_info_collector():
    """
    Exercise 5: Page Information Collector

    Task:
    Create a utility that:
    1. Accepts a list of URLs
    2. Visits each URL
    3. Collects comprehensive info:
       - URL
       - Title
       - Status code
       - Content length
       - Viewport size
    4. Saves data to a text file
    5. Returns the data

    URLs to test:
    - https://example.com
    - https://playwright.dev
    - https://github.com

    Expected output:
    - Data file created
    - Console output with summary
    - All URLs processed
    """
    # TODO: Implement this exercise
    pass


# Challenge Exercise
def challenge_complete_test_suite():
    """
    Challenge: Complete Test Suite

    Task:
    Build a complete test suite that:
    1. Creates a web application (HTML) with:
       - Login page
       - Dashboard (after login)
       - Profile page
       - Logout functionality

    2. Automate these scenarios:
       - Valid login → verify dashboard
       - Invalid login → verify error
       - Navigate to profile → verify data
       - Logout → verify back to login

    3. Include:
       - Error handling
       - Assertions
       - Logging
       - Screenshots on failure

    This combines everything you've learned!

    Expected output:
    - All test scenarios pass
    - Proper logging
    - Error handling works
    """
    # TODO: Implement this challenge
    pass


if __name__ == "__main__":
    print("Exercise 1: Simple Workflow")
    print("=" * 50)
    exercise_1_simple_workflow()

    print("\n\nExercise 2: Multi-Page Workflow")
    print("=" * 50)
    exercise_2_multi_page_workflow()

    print("\n\nExercise 3: Shopping Flow")
    print("=" * 50)
    exercise_3_shopping_flow()

    print("\n\nExercise 4: Error Handling Workflow")
    print("=" * 50)
    exercise_4_error_handling_workflow()

    print("\n\nExercise 5: Page Info Collector")
    print("=" * 50)
    exercise_5_page_info_collector()

    print("\n\nChallenge: Complete Test Suite")
    print("=" * 50)
    challenge_complete_test_suite()

    print("\n\n✅ All exercises completed!")
