"""Exercise 1: Block Resources and Mock APIs

Your task:
1. Navigate to https://the-internet.herokuapp.com/
2. Block all image requests (png, jpg, gif, svg, ico)
3. Count how many images were blocked
4. Set up a mock for an imaginary "/api/user" endpoint
5. Mock should return: {"id": 1, "name": "Test User", "premium": true}
6. Verify your mock is correctly configured by checking the route

Bonus:
- Block all requests to external domains (not herokuapp.com)
- Create a mock that returns different data based on query parameters
- Simulate a 500 error for a specific endpoint

Hints:
- Use page.route(pattern, handler) to intercept requests
- Use route.abort() to block requests
- Use route.fulfill(status=200, body="...", content_type="...") to mock
- resource_type can be: image, stylesheet, script, font, xhr, fetch, etc.
"""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Block and Mock ===\n")

    blocked_images = 0

    # TODO: Create handler to block images
    # def block_images(route):
    #     global blocked_images
    #     blocked_images += 1
    #     print(f"Blocked: {route.request.url}")
    #     route.abort()

    # TODO: Register route to block images
    # page.route("**/*.{png,jpg,jpeg,gif,svg,ico}", block_images)

    # TODO: Navigate to page
    # page.goto("https://the-internet.herokuapp.com/")

    # TODO: Print blocked count
    # print(f"Images blocked: {blocked_images}")

    # TODO: Create mock for /api/user
    # mock_user = {"id": 1, "name": "Test User", "premium": True}
    # def mock_user_api(route):
    #     route.fulfill(
    #         status=200,
    #         content_type="application/json",
    #         body=json.dumps(mock_user)
    #     )
    # page.route("**/api/user", mock_user_api)

    # TODO: Verify mock is configured
    # print(f"Mock configured for /api/user: {mock_user}")

    print("Exercise completed!")
    context.close()
    browser.close()
