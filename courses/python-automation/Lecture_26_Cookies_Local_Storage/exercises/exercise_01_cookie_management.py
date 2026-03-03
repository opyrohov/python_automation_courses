"""Exercise 1: Cookie Management

Your task:
1. Navigate to https://the-internet.herokuapp.com/
2. Add a cookie named "user_id" with value "test_user_123"
3. Add a cookie named "session_token" with value "abc123xyz" and httpOnly=True
4. Verify both cookies were added
5. Get all cookies and print their names
6. Remove only the "user_id" cookie (keep "session_token")
7. Verify "user_id" is gone but "session_token" remains

Bonus:
- Add a cookie with an expiration date (1 hour from now)
- Check if a cookie is httpOnly
- Print the full details of each cookie

Hints:
- Use context.add_cookies([{...}]) to add
- Use context.cookies() to get all
- To remove specific cookie: get all, filter, clear_cookies(), add_cookies(filtered)
- Use time.time() + 3600 for 1 hour expiration
"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Cookie Management ===\n")

    # TODO: Navigate to the site
    # page.goto("https://the-internet.herokuapp.com/")

    # TODO: Add "user_id" cookie
    # context.add_cookies([{...}])

    # TODO: Add "session_token" cookie with httpOnly=True
    # context.add_cookies([{...}])

    # TODO: Verify cookies were added
    # cookies = context.cookies()
    # print(f"Total cookies: {len(cookies)}")

    # TODO: Print all cookie names
    # for cookie in cookies:
    #     print(f"  - {cookie['name']}")

    # TODO: Remove only "user_id" cookie
    # Hint: Filter cookies to keep only those != "user_id"
    # all_cookies = context.cookies()
    # keep_cookies = [c for c in all_cookies if c["name"] != "user_id"]
    # context.clear_cookies()
    # context.add_cookies(keep_cookies)

    # TODO: Verify "user_id" is gone, "session_token" remains
    # remaining = context.cookies()
    # Check that "session_token" is in remaining
    # Check that "user_id" is NOT in remaining

    print("Exercise completed!")
    context.close()
    browser.close()
