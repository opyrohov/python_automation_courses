"""Exercise 2: Multi-User Testing

Your task:
1. Create two separate browser contexts (user1_context, user2_context)
2. Create a page in each context
3. User 1: Go to login page and log in with:
   - username: tomsmith
   - password: SuperSecretPassword!
4. User 2: Go to login page (should see login form, not logged in)
5. Verify User 1 is logged in (sees success message)
6. Verify User 2 is NOT logged in (sees login form)
7. This proves the contexts are isolated!

Hints:
- Use browser.new_context() for each user
- Login URL: https://the-internet.herokuapp.com/login
- Success message has class: .flash.success
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Exercise 2: Multi-User Testing ===\n")

    # TODO: Create two separate contexts
    # user1_context = browser.new_context()
    # user2_context = browser.new_context()

    # TODO: Create pages in each context
    # user1_page = user1_context.new_page()
    # user2_page = user2_context.new_page()

    # TODO: User 1 logs in
    # user1_page.goto("https://the-internet.herokuapp.com/login")
    # user1_page.locator("#username").fill(...)
    # user1_page.locator("#password").fill(...)
    # user1_page.locator("button[type='submit']").click()

    # TODO: Verify User 1 is logged in
    # expect(user1_page.locator(".flash.success")).to_be_visible()
    # print("User 1 is logged in")

    # TODO: User 2 goes to login page
    # user2_page.goto("https://the-internet.herokuapp.com/login")

    # TODO: Verify User 2 sees login form (NOT logged in)
    # expect(user2_page.locator("#username")).to_be_visible()
    # print("User 2 sees login form (not logged in)")

    # TODO: Clean up
    # user1_context.close()
    # user2_context.close()

    print("Exercise completed - contexts are isolated!")
    browser.close()
