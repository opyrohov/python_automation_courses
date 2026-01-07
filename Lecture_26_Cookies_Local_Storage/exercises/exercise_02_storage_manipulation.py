"""Exercise 2: Storage Manipulation

Your task:
1. Navigate to https://the-internet.herokuapp.com/
2. Set localStorage items:
   - "theme" = "dark"
   - "language" = "en"
   - "user_data" = JSON string with {name: "Test", level: 5}
3. Verify all items were stored correctly
4. Set sessionStorage items:
   - "current_page" = "home"
   - "visit_count" = "1"
5. Navigate to another page (/login)
6. Verify localStorage persists but check sessionStorage behavior
7. Get all localStorage items as a dictionary
8. Clear only sessionStorage, keep localStorage
9. Verify final state

Bonus:
- Save complete storage state to a file
- Create new context with saved state
- Verify state was restored

Hints:
- Use page.evaluate() for localStorage/sessionStorage operations
- JSON.stringify() and JSON.parse() for objects
- Use context.storage_state(path="file.json") to save
- Use browser.new_context(storage_state="file.json") to load
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 2: Storage Manipulation ===\n")

    # TODO: Navigate to the site
    # page.goto("https://the-internet.herokuapp.com/")

    # TODO: Set localStorage items
    # page.evaluate("localStorage.setItem('theme', 'dark')")
    # page.evaluate("localStorage.setItem('language', 'en')")
    # user_data = {"name": "Test", "level": 5}
    # page.evaluate(f"localStorage.setItem('user_data', '{json.dumps(user_data)}')")

    # TODO: Verify localStorage items
    # theme = page.evaluate("localStorage.getItem('theme')")
    # print(f"Theme: {theme}")

    # TODO: Set sessionStorage items
    # page.evaluate("sessionStorage.setItem('current_page', 'home')")
    # page.evaluate("sessionStorage.setItem('visit_count', '1')")

    # TODO: Navigate to /login
    # page.goto("https://the-internet.herokuapp.com/login")

    # TODO: Check if localStorage persists
    # theme_after = page.evaluate("localStorage.getItem('theme')")
    # print(f"Theme after navigation: {theme_after}")

    # TODO: Get all localStorage as dictionary
    # all_local = page.evaluate("""() => {
    #     const data = {};
    #     for (let i = 0; i < localStorage.length; i++) {
    #         const key = localStorage.key(i);
    #         data[key] = localStorage.getItem(key);
    #     }
    #     return data;
    # }""")
    # print(f"All localStorage: {all_local}")

    # TODO: Clear only sessionStorage
    # page.evaluate("sessionStorage.clear()")

    # TODO: Verify localStorage still exists
    # local_count = page.evaluate("localStorage.length")
    # session_count = page.evaluate("sessionStorage.length")
    # print(f"localStorage items: {local_count}")
    # print(f"sessionStorage items: {session_count}")

    print("Exercise completed!")
    context.close()
    browser.close()
