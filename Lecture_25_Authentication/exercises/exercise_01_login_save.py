"""Exercise 1: Login and Save Authentication State

Your task:
1. Navigate to https://the-internet.herokuapp.com/login
2. Login with username: tomsmith, password: SuperSecretPassword!
3. Wait for successful login (check URL or success message)
4. Save the authentication state to a file called "my_auth.json"
5. Print confirmation that auth was saved
6. Verify the file was created

Bonus:
- Check the file size
- Print the number of cookies saved
- Add error handling for failed login

Hints:
- Use context.storage_state(path="filename.json")
- Make sure to wait for login to complete before saving
- Use os.path.exists() to check if file was created
"""
from playwright.sync_api import sync_playwright, expect
import os

AUTH_FILE = "my_auth.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Login and Save Auth State ===\n")

    # TODO: Navigate to login page
    # page.goto(...)

    # TODO: Fill in username
    # page.locator("#username").fill(...)

    # TODO: Fill in password
    # page.locator("#password").fill(...)

    # TODO: Click submit button
    # page.locator("button[type='submit']").click()

    # TODO: Wait for successful login
    # page.wait_for_url("**/secure")
    # expect(page.locator(".flash.success")).to_be_visible()

    # TODO: Save authentication state
    # context.storage_state(path=AUTH_FILE)
    # print(f"Auth state saved to {AUTH_FILE}")

    # TODO: Verify file was created
    # if os.path.exists(AUTH_FILE):
    #     print("File created successfully!")

    print("Exercise completed!")
    context.close()
    browser.close()
