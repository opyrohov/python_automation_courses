"""
Exercise 3: Multiple Pages Practice
Practice working with multiple pages, contexts, and tabs
"""

from playwright.sync_api import sync_playwright


def exercise_1_create_multiple_pages():
    """
    Exercise 1: Create Multiple Pages

    Task:
    1. Launch a browser
    2. Create a context
    3. Create 3 pages in the same context
    4. Navigate each page to a different URL:
       - Page 1: https://example.com
       - Page 2: https://playwright.dev
       - Page 3: https://github.com
    5. Print the title of each page
    6. Print the total number of pages
    7. Close the browser

    Expected output:
    - Titles of all 3 pages
    - Total pages: 3
    """
    # TODO: Implement this exercise
    pass


def exercise_2_switch_between_pages():
    """
    Exercise 2: Switch Between Pages

    Task:
    1. Launch a browser in headed mode with slow_mo=1000
    2. Create 3 pages with different URLs
    3. Bring each page to front in order:
       - First page
       - Second page
       - Third page
       - Back to first page
    4. Print the URL each time you switch
    5. Close the browser

    Expected output:
    - Should see browser switching between tabs
    - URLs should be printed in order
    """
    # TODO: Implement this exercise
    pass


def exercise_3_close_specific_pages():
    """
    Exercise 3: Close Specific Pages

    Task:
    1. Launch a browser
    2. Create 4 pages
    3. Navigate all pages to different URLs
    4. Print total pages
    5. Close the 2nd page
    6. Print total pages
    7. Close the 4th page
    8. Print total pages
    9. Print URLs of remaining pages
    10. Close the browser

    Expected output:
    - Total pages: 4 → 3 → 2
    - URLs of remaining pages (1st and 3rd)
    """
    # TODO: Implement this exercise
    pass


def exercise_4_multiple_contexts():
    """
    Exercise 4: Multiple Contexts

    Task:
    1. Launch a browser
    2. Create 2 separate contexts
    3. In context 1:
       - Create a page
       - Navigate to https://example.com
       - Set localStorage item: "user" = "Alice"
    4. In context 2:
       - Create a page
       - Navigate to https://example.com
       - Try to read localStorage "user"
    5. Print the localStorage value from both contexts
    6. Verify they are isolated (context 2 should get null)
    7. Close the browser

    Expected output:
    - Context 1: "Alice"
    - Context 2: null (isolated)
    """
    # TODO: Implement this exercise
    pass


def exercise_5_iterate_pages():
    """
    Exercise 5: Iterate Through Pages

    Task:
    1. Launch a browser
    2. Create 5 pages with these URLs:
       - https://example.com
       - https://playwright.dev
       - https://github.com
       - https://python.org
       - https://npmjs.com
    3. Use a loop to iterate through context.pages
    4. For each page, print:
       - Page number
       - URL
       - Title
    5. Close the browser

    Expected output:
    - Information for all 5 pages
    - Formatted as a list
    """
    # TODO: Implement this exercise
    pass


# Challenge Exercise
def challenge_page_manager():
    """
    Challenge: Page Manager

    Task:
    Create a page manager that:
    1. Opens 3 pages with different URLs
    2. Provides a menu to:
       - List all pages
       - Switch to a specific page (by number)
       - Close a specific page (by number)
       - Get info about a page
       - Exit
    3. Implement simple menu-driven interaction
    4. Handle edge cases (invalid page numbers, etc.)

    This is a more advanced exercise combining multiple concepts.

    Expected output:
    - Interactive menu
    - Ability to manage pages
    - Proper error handling
    """
    # TODO: Implement this challenge
    pass


if __name__ == "__main__":
    print("Exercise 1: Create Multiple Pages")
    print("=" * 50)
    exercise_1_create_multiple_pages()

    print("\n\nExercise 2: Switch Between Pages")
    print("=" * 50)
    exercise_2_switch_between_pages()

    print("\n\nExercise 3: Close Specific Pages")
    print("=" * 50)
    exercise_3_close_specific_pages()

    print("\n\nExercise 4: Multiple Contexts")
    print("=" * 50)
    exercise_4_multiple_contexts()

    print("\n\nExercise 5: Iterate Pages")
    print("=" * 50)
    exercise_5_iterate_pages()

    print("\n\nChallenge: Page Manager")
    print("=" * 50)
    challenge_page_manager()

    print("\n\n✅ All exercises completed!")
