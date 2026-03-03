"""Exercise 1: Capture Login Flow

Your task:
1. Navigate to https://the-internet.herokuapp.com/login
2. Take a screenshot of the initial login page
3. Fill in username: tomsmith
4. Take a screenshot after entering username
5. Fill in password: SuperSecretPassword!
6. Take a screenshot after entering password
7. Click the login button
8. Take a screenshot of the result page
9. All screenshots should be saved in a "screenshots" folder
10. Use descriptive names like "01_login_page.png", "02_username_filled.png", etc.

Bonus:
- Create the screenshots folder if it doesn't exist
- Add full_page screenshot at the end
- Disable animations for consistent results

Hints:
- Use os.makedirs() to create folders
- page.screenshot(path="...", full_page=True)
- page.screenshot(path="...", animations="disabled")
"""
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: Capture Login Flow ===\n")

    # TODO: Create screenshots folder
    # os.makedirs("screenshots", exist_ok=True)

    # TODO: Navigate to login page
    # page.goto(...)

    # TODO: Screenshot 1 - Initial login page
    # page.screenshot(path="screenshots/01_login_page.png")

    # TODO: Fill username
    # page.locator("#username").fill(...)

    # TODO: Screenshot 2 - After username
    # page.screenshot(...)

    # TODO: Fill password
    # page.locator("#password").fill(...)

    # TODO: Screenshot 3 - After password
    # page.screenshot(...)

    # TODO: Click login button
    # page.locator("button[type='submit']").click()
    # page.wait_for_load_state()

    # TODO: Screenshot 4 - Result page
    # page.screenshot(...)

    # TODO: Bonus - Full page screenshot
    # page.screenshot(path="screenshots/05_result_full_page.png", full_page=True)

    print("Exercise completed!")
    browser.close()
