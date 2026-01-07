"""Exercise 2: Test Error Handling

Your task:
1. Navigate to https://the-internet.herokuapp.com/
2. Set up mocks for different error scenarios:
   - /api/not-found should return 404
   - /api/server-error should return 500
   - /api/unauthorized should return 401
3. Each mock should return appropriate JSON error response
4. Navigate to a page and verify your mocks work
5. Use expect_response to capture and verify response status

Bonus:
- Test that your app shows correct error messages for each status
- Create a slow response mock (2+ seconds delay)
- Mock a network failure (route.abort("failed"))

Hints:
- Use route.fulfill(status=404, body="...") for errors
- Use time.sleep() inside handler for delay
- Use route.abort("failed") for network failure
- Use page.expect_response() to verify responses
"""
from playwright.sync_api import sync_playwright
import json
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 2: Test Error Handling ===\n")

    # TODO: Create 404 mock
    # def mock_404(route):
    #     route.fulfill(
    #         status=404,
    #         content_type="application/json",
    #         body=json.dumps({"error": "Not Found", "code": 404})
    #     )
    # page.route("**/api/not-found", mock_404)

    # TODO: Create 500 mock
    # def mock_500(route):
    #     route.fulfill(
    #         status=500,
    #         content_type="application/json",
    #         body=json.dumps({"error": "Internal Server Error", "code": 500})
    #     )
    # page.route("**/api/server-error", mock_500)

    # TODO: Create 401 mock
    # def mock_401(route):
    #     route.fulfill(
    #         status=401,
    #         content_type="application/json",
    #         body=json.dumps({"error": "Unauthorized", "code": 401})
    #     )
    # page.route("**/api/unauthorized", mock_401)

    # TODO: Navigate to page
    # page.goto("https://the-internet.herokuapp.com/")

    # TODO: Verify mocks are configured
    # print("Error mocks configured:")
    # print("  - /api/not-found -> 404")
    # print("  - /api/server-error -> 500")
    # print("  - /api/unauthorized -> 401")

    # BONUS: Slow response
    # def slow_response(route):
    #     print("Delaying response...")
    #     time.sleep(2)
    #     route.fulfill(status=200, body='{"slow": true}')
    # page.route("**/api/slow", slow_response)

    # BONUS: Network failure
    # def network_failure(route):
    #     route.abort("failed")
    # page.route("**/api/offline", network_failure)

    print("Exercise completed!")
    context.close()
    browser.close()
