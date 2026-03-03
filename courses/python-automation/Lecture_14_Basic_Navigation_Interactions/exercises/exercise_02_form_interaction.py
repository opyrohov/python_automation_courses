"""
Exercise 2: Form Interaction Practice
Practice using click(), fill(), and type() methods
"""

from playwright.sync_api import sync_playwright


def exercise_1_simple_click():
    """
    Exercise 1: Simple Click

    Task:
    1. Launch a browser in headed mode
    2. Navigate to https://playwright.dev
    3. Click on the "Get started" link
    4. Print the new URL
    5. Print the page title
    6. Close the browser

    Expected output:
    - URL should contain "docs" or "intro"
    - Page title should be related to documentation
    """
    # TODO: Implement this exercise
    pass


def exercise_2_fill_vs_type():
    """
    Exercise 2: Compare fill() and type()

    Task:
    1. Launch a browser
    2. Create a simple HTML page with two input fields
    3. Use fill() to fill the first input with "Hello from fill()"
    4. Use type() to fill the second input with "Hello from type()" with 50ms delay
    5. Take a screenshot
    6. Close the browser

    HTML to use:
    <input id="input1" /><br><input id="input2" />

    Expected output:
    - Both inputs should be filled
    - You should see type() typing character by character
    - Screenshot should be saved
    """
    # TODO: Implement this exercise
    pass


def exercise_3_complete_form():
    """
    Exercise 3: Complete Form Filling

    Task:
    1. Launch a browser
    2. Create an HTML page with a form containing:
       - Username input (name="username")
       - Email input (name="email")
       - Password input (name="password")
       - Checkbox (id="terms")
       - Submit button
    3. Fill all form fields with appropriate data
    4. Check the checkbox
    5. Click the submit button
    6. Close the browser

    Expected output:
    - All form fields should be filled
    - Checkbox should be checked
    - Form should be submitted
    """
    # TODO: Implement this exercise
    pass


def exercise_4_click_options():
    """
    Exercise 4: Different Click Types

    Task:
    1. Launch a browser
    2. Create an HTML page with a button
    3. Perform these clicks in order:
       - Single click
       - Double click (click_count=2)
       - Right click (button="right")
    4. Add JavaScript to show which type of click was performed
    5. Print the result after each click
    6. Close the browser

    Expected output:
    - Should see different click types being detected
    - Messages showing "single", "double", or "right" click
    """
    # TODO: Implement this exercise
    pass


def exercise_5_type_with_delay():
    """
    Exercise 5: Type with Delay

    Task:
    1. Launch a browser in headed mode with slow_mo=300
    2. Create an HTML page with a search input
    3. Use type() to type "Playwright Automation" with 100ms delay
    4. Print "Typing complete!"
    5. Wait 2 seconds
    6. Close the browser

    Expected output:
    - You should clearly see each character being typed
    - Slow motion should make it easy to observe
    """
    # TODO: Implement this exercise
    pass


# Challenge Exercise
def challenge_interactive_form():
    """
    Challenge: Interactive Form with Validation

    Task:
    Create a complete form automation with:
    1. An HTML form with:
       - Name field (required)
       - Email field (with validation)
       - Message textarea
       - Subscribe checkbox
       - Submit button
    2. JavaScript validation that:
       - Checks if name is not empty
       - Checks if email contains "@"
       - Shows success/error messages
    3. Fill the form correctly and submit
    4. Verify the success message appears
    5. Print the success message

    Expected output:
    - Form should be filled correctly
    - Validation should pass
    - Success message should be displayed
    """
    # TODO: Implement this challenge
    pass


if __name__ == "__main__":
    print("Exercise 1: Simple Click")
    print("=" * 50)
    exercise_1_simple_click()

    print("\n\nExercise 2: Fill vs Type")
    print("=" * 50)
    exercise_2_fill_vs_type()

    print("\n\nExercise 3: Complete Form")
    print("=" * 50)
    exercise_3_complete_form()

    print("\n\nExercise 4: Click Options")
    print("=" * 50)
    exercise_4_click_options()

    print("\n\nExercise 5: Type with Delay")
    print("=" * 50)
    exercise_5_type_with_delay()

    print("\n\nChallenge: Interactive Form")
    print("=" * 50)
    challenge_interactive_form()

    print("\n\n✅ All exercises completed!")
