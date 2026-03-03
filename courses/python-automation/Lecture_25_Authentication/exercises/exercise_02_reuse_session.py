"""Exercise 2: Reuse Saved Session

Your task:
1. Check if auth file exists (from Exercise 1)
2. Create a new context with the saved storage_state
3. Navigate directly to the secure page (without logging in)
4. Verify you're authenticated (check for success message)
5. Navigate to another protected page to prove session works
6. Compare with a fresh context that has no auth

Bonus:
- Handle case when auth file doesn't exist
- Check if session is expired (try to detect login redirect)
- Clean up the auth file at the end

Hints:
- Use browser.new_context(storage_state="filename.json")
- Protected pages should show content, not redirect to login
- Use page.url to check current URL
"""
from playwright.sync_api import sync_playwright, expect
import os

AUTH_FILE = "my_auth.json"

# Check if auth file exists
if not os.path.exists(AUTH_FILE):
    print(f"ERROR: {AUTH_FILE} not found!")
    print("Please run exercise_01_login_save.py first.")
    exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Exercise 2: Reuse Saved Session ===\n")

    # TODO: Create context with saved auth state
    # context = browser.new_context(storage_state=AUTH_FILE)
    # page = context.new_page()

    # TODO: Navigate directly to secure page
    # page.goto("https://the-internet.herokuapp.com/secure")

    # TODO: Verify we're authenticated
    # expect(page.locator("h2")).to_have_text("Secure Area")
    # print("Successfully accessed secure page!")

    # TODO: Navigate to another page to prove session works
    # page.goto("https://the-internet.herokuapp.com/")
    # page.goto("https://the-internet.herokuapp.com/secure")
    # Check still authenticated

    # TODO: Compare with fresh context (no auth)
    # fresh_context = browser.new_context()
    # fresh_page = fresh_context.new_page()
    # fresh_page.goto("https://the-internet.herokuapp.com/secure")
    # Check if redirected to login

    print("Exercise completed!")
    browser.close()
