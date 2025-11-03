"""
Exercise 1: Navigation Practice
Practice using goto(), go_back(), go_forward(), and reload()
"""

from playwright.sync_api import sync_playwright


def exercise_1_basic_navigation():
    """
    Exercise 1: Basic Navigation

    Task:
    1. Launch a browser in headed mode
    2. Navigate to https://example.com
    3. Print the page title
    4. Navigate to https://playwright.dev
    5. Print the page title
    6. Go back to the previous page
    7. Print the current URL
    8. Go forward
    9. Print the current URL
    10. Reload the page
    11. Print "Navigation complete!"
    12. Close the browser

    Expected output:
    - Should see browser navigating between pages
    - Should print titles and URLs at each step
    """
    # TODO: Implement this exercise
    pass


def exercise_2_navigation_with_wait():
    """
    Exercise 2: Navigation with Wait Options

    Task:
    1. Launch a browser
    2. Navigate to https://playwright.dev with wait_until="networkidle"
    3. Get the response object and print the status code
    4. Print whether the response is OK (status 200-299)
    5. Print the page title
    6. Close the browser

    Expected output:
    - Status code: 200
    - OK: True
    - Page title should be printed
    """
    # TODO: Implement this exercise
    pass


def exercise_3_navigation_history():
    """
    Exercise 3: Browser History Navigation

    Task:
    1. Launch a browser
    2. Visit these URLs in order:
       - https://example.com
       - https://playwright.dev
       - https://github.com
    3. Print the title after each navigation
    4. Go back twice
    5. Print the current URL (should be example.com)
    6. Go forward once
    7. Print the current URL (should be playwright.dev)
    8. Close the browser

    Expected output:
    - Titles of all three pages
    - URLs after going back and forward
    """
    # TODO: Implement this exercise
    pass


def exercise_4_reload_page():
    """
    Exercise 4: Page Reload

    Task:
    1. Launch a browser
    2. Navigate to https://example.com
    3. Get the page content length
    4. Reload the page
    5. Get the page content length again
    6. Compare the lengths (should be the same)
    7. Print both lengths
    8. Close the browser

    Expected output:
    - Content length before reload
    - Content length after reload
    - They should match
    """
    # TODO: Implement this exercise
    pass


def exercise_5_navigation_with_error_handling():
    """
    Exercise 5: Navigation with Error Handling

    Task:
    1. Launch a browser
    2. Try to navigate to a valid URL (https://example.com) with try/except
    3. Print "Success!" if navigation works
    4. Try to navigate to an invalid URL with a 2-second timeout
    5. Catch the exception and print the error type
    6. Close the browser

    Expected output:
    - "Success!" for valid URL
    - Error type for invalid URL (TimeoutError or similar)
    """
    # TODO: Implement this exercise
    pass


# Challenge Exercise
def challenge_navigation_tracker():
    """
    Challenge: Navigation Tracker

    Task:
    Create a script that:
    1. Navigates to 5 different websites
    2. For each site, collect:
       - URL
       - Title
       - Response status code
       - Content length
    3. Store all data in a list of dictionaries
    4. At the end, print a summary table of all collected data

    Hint: Use a loop and store data in a list
    """
    # TODO: Implement this challenge
    pass


if __name__ == "__main__":
    print("Exercise 1: Basic Navigation")
    print("=" * 50)
    exercise_1_basic_navigation()

    print("\n\nExercise 2: Navigation with Wait")
    print("=" * 50)
    exercise_2_navigation_with_wait()

    print("\n\nExercise 3: Navigation History")
    print("=" * 50)
    exercise_3_navigation_history()

    print("\n\nExercise 4: Reload Page")
    print("=" * 50)
    exercise_4_reload_page()

    print("\n\nExercise 5: Navigation with Error Handling")
    print("=" * 50)
    exercise_5_navigation_with_error_handling()

    print("\n\nChallenge: Navigation Tracker")
    print("=" * 50)
    challenge_navigation_tracker()

    print("\n\n✅ All exercises completed!")
