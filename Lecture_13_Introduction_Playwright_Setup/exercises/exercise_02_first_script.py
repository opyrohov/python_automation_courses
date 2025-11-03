"""
Exercise 2: Write Your First Playwright Script

Complete the functions below to practice basic Playwright operations.

Run: python exercise_02_first_script.py
"""

from playwright.sync_api import sync_playwright


def exercise_1_open_browser():
    """
    Exercise 1: Open a browser and navigate to a website.

    TODO:
    1. Launch Chromium browser in headed mode
    2. Create a new page
    3. Navigate to https://example.com
    4. Print the page title
    5. Close the browser
    """

    with sync_playwright() as p:
        # TODO: Launch browser (headless=False to see it)
        # browser = ???

        # TODO: Create new page
        # page = ???

        # TODO: Navigate to https://example.com
        # page.goto(???)

        # TODO: Print page title
        # title = page.title()
        # print(f"Page title: {title}")

        # TODO: Close browser
        # browser.close()

        pass  # Remove this when you complete the exercise


def exercise_2_multiple_pages():
    """
    Exercise 2: Open multiple pages (tabs).

    TODO:
    1. Launch browser
    2. Create page 1 and navigate to https://example.com
    3. Create page 2 and navigate to https://playwright.dev
    4. Print titles of both pages
    5. Close browser
    """

    with sync_playwright() as p:
        # TODO: Your code here

        pass  # Remove this when you complete the exercise


def exercise_3_take_screenshot():
    """
    Exercise 3: Take a screenshot.

    TODO:
    1. Launch browser
    2. Navigate to https://playwright.dev
    3. Take a screenshot and save it as "my_screenshot.png"
    4. Print confirmation message
    5. Close browser
    """

    with sync_playwright() as p:
        # TODO: Your code here

        pass  # Remove this when you complete the exercise


def exercise_4_get_page_info():
    """
    Exercise 4: Get and print page information.

    TODO:
    1. Navigate to https://playwright.dev
    2. Print:
       - Page title
       - Current URL
       - Page content length (len(page.content()))
    3. Close browser
    """

    with sync_playwright() as p:
        # TODO: Your code here

        pass  # Remove this when you complete the exercise


def exercise_5_different_browsers():
    """
    Exercise 5: Open the same page in different browsers.

    TODO:
    1. Open https://example.com in Chromium
    2. Open https://example.com in Firefox
    3. Open https://example.com in WebKit
    4. Print title from each browser
    5. Close all browsers
    """

    with sync_playwright() as p:
        # TODO: Launch Chromium
        # browser1 = p.chromium.launch(headless=False)
        # ...

        # TODO: Launch Firefox
        # browser2 = p.firefox.launch(headless=False)
        # ...

        # TODO: Launch WebKit
        # browser3 = p.webkit.launch(headless=False)
        # ...

        # TODO: Close all browsers

        pass  # Remove this when you complete the exercise


def exercise_6_navigation():
    """
    Exercise 6: Practice navigation.

    TODO:
    1. Navigate to https://example.com
    2. Navigate to https://playwright.dev
    3. Go back to example.com
    4. Go forward to playwright.dev
    5. Reload the page
    6. Print title after each navigation
    """

    with sync_playwright() as p:
        # TODO: Your code here

        pass  # Remove this when you complete the exercise


def exercise_7_slow_motion():
    """
    Exercise 7: Use slow motion to see what's happening.

    TODO:
    1. Launch browser with slow_mo=1000 (1 second delay)
    2. Navigate to https://playwright.dev
    3. Click on "Get started" link
    4. Wait 2 seconds
    5. Close browser

    Watch how each action is slowed down!
    """

    with sync_playwright() as p:
        # TODO: Launch with slow motion
        # browser = p.chromium.launch(headless=False, slow_mo=1000)

        # TODO: Rest of your code

        pass  # Remove this when you complete the exercise


def exercise_8_your_favorite_website():
    """
    Exercise 8: Automate your favorite website!

    TODO:
    Create your own automation script that:
    1. Navigates to your favorite website
    2. Prints the title
    3. Takes a screenshot
    4. Prints the URL
    5. Shows the browser for 5 seconds (so you can see it)

    Be creative! Choose any website you like.
    """

    with sync_playwright() as p:
        # TODO: Your creative automation here!

        pass  # Remove this when you complete the exercise


# ============================================================================
# Run all exercises
# ============================================================================

def main():
    """Run all exercises."""

    print("=" * 60)
    print("Playwright First Script Exercises")
    print("=" * 60)

    # Uncomment each exercise as you complete it

    # print("\n📝 Exercise 1: Open Browser")
    # exercise_1_open_browser()

    # print("\n📝 Exercise 2: Multiple Pages")
    # exercise_2_multiple_pages()

    # print("\n📝 Exercise 3: Take Screenshot")
    # exercise_3_take_screenshot()

    # print("\n📝 Exercise 4: Get Page Info")
    # exercise_4_get_page_info()

    # print("\n📝 Exercise 5: Different Browsers")
    # exercise_5_different_browsers()

    # print("\n📝 Exercise 6: Navigation")
    # exercise_6_navigation()

    # print("\n📝 Exercise 7: Slow Motion")
    # exercise_7_slow_motion()

    # print("\n📝 Exercise 8: Your Favorite Website")
    # exercise_8_your_favorite_website()

    print("\n" + "=" * 60)
    print("✅ All exercises completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================================
# Hints and Tips
# ============================================================================
"""
Useful Playwright Methods:

Browser:
- p.chromium.launch(headless=False)
- p.firefox.launch()
- p.webkit.launch()
- browser.new_page()
- browser.close()

Page:
- page.goto(url)
- page.title()
- page.url
- page.content()
- page.screenshot(path="file.png")
- page.go_back()
- page.go_forward()
- page.reload()
- page.wait_for_timeout(milliseconds)
- page.click(selector)

Remember:
- headless=False shows the browser window
- headless=True runs in background (faster)
- slow_mo=1000 slows down actions by 1 second (for debugging)
"""
