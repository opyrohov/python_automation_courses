"""Exercise 2: Combined UI and API Test

Your task:
1. Create both API context and browser
2. Use API to get user data (GET /users/1)
3. Navigate browser to https://the-internet.herokuapp.com/
4. Perform a UI action (navigate to login page)
5. Login with username "tomsmith" and password "SuperSecretPassword!"
6. Verify login success in UI
7. Use API to verify something (get some data)
8. Clean up both contexts

Bonus:
- Create test data via API before UI test
- Verify UI action result via API
- Use API token in browser context headers

Hints:
- Create API context: p.request.new_context()
- Create browser: p.chromium.launch()
- Use page.fill(), page.click() for UI actions
- Use api.get(), api.post() for API calls
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    print("=== Exercise 2: Combined UI + API Test ===\n")

    # TODO: Create API context
    # api = p.request.new_context(base_url="https://jsonplaceholder.typicode.com")

    # TODO: Create browser and page
    # browser = p.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()

    # TODO: Get user data via API
    # response = api.get("/users/1")
    # user = response.json()
    # print(f"User from API: {user['name']}")

    # TODO: Navigate to login page
    # page.goto("https://the-internet.herokuapp.com/login")

    # TODO: Perform login
    # page.fill("#username", "tomsmith")
    # page.fill("#password", "SuperSecretPassword!")
    # page.click("button[type='submit']")

    # TODO: Verify login in UI
    # page.wait_for_url("**/secure")
    # expect(page.locator(".flash.success")).to_be_visible()
    # print("Login successful!")

    # TODO: API verification (get more data)
    # response = api.get("/posts/1")
    # post = response.json()
    # print(f"Post from API: {post['title'][:30]}...")

    # TODO: Cleanup
    # api.dispose()
    # browser.close()

    print("Exercise completed!")
