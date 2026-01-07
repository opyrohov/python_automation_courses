"""Example 5: Combining UI and API Tests

Demonstrates how to combine API calls with browser UI tests
for faster setup, verification, and cleanup.
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    print("=== Combined UI + API Testing Demo ===\n")

    # Create both API and browser contexts
    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("Created API context and browser")
    print("=" * 50)

    # SCENARIO 1: API Setup -> UI Verification
    print("\n--- Scenario 1: Create via API, Verify in UI ---")

    # Step 1: Create test data via API (fast!)
    print("\n1. Creating test data via API...")
    response = api.post("/posts", data={
        "title": "API Created Post",
        "body": "This post was created via API for UI testing.",
        "userId": 1
    })
    created_post = response.json()
    print(f"   Created post ID: {created_post.get('id')}")

    # Step 2: Verify in UI
    print("\n2. Verifying in UI...")
    # Note: Using the-internet for actual UI verification
    page.goto("https://the-internet.herokuapp.com/")
    print(f"   Navigated to: {page.url}")
    print(f"   Title: {page.title()}")

    # In real scenario:
    # page.goto(f"/posts/{created_post['id']}")
    # expect(page.locator(".post-title")).to_have_text("API Created Post")

    # SCENARIO 2: UI Action -> API Verification
    print("\n--- Scenario 2: UI Action, Verify via API ---")

    # Step 1: Perform UI action
    print("\n1. Performing UI action (login)...")
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")
    print("   Login successful in UI")

    # Step 2: Verify backend state via API
    print("\n2. Verifying state via API...")
    # In real scenario, you'd check:
    # response = api.get(f"/users/{user_id}/session")
    # assert response.json()["active"] == True

    # Demo with available API
    response = api.get("/users/1")
    user = response.json()
    print(f"   User from API: {user['name']}")
    print("   (In real app: verify session/state via API)")

    # SCENARIO 3: API Cleanup after UI Test
    print("\n--- Scenario 3: Cleanup via API ---")

    # Step 1: Create some test data
    print("\n1. Creating test resources...")
    test_ids = []
    for i in range(3):
        response = api.post("/posts", data={
            "title": f"Test Post {i+1}",
            "body": "Will be cleaned up",
            "userId": 1
        })
        test_ids.append(response.json().get("id", 101 + i))
    print(f"   Created posts: {test_ids}")

    # Step 2: Run UI tests (simulated)
    print("\n2. Running UI tests...")
    page.goto("https://the-internet.herokuapp.com/")
    print("   UI tests completed")

    # Step 3: Cleanup via API (fast!)
    print("\n3. Cleaning up via API...")
    for post_id in test_ids:
        response = api.delete(f"/posts/{post_id}")
        print(f"   Deleted post {post_id}: {response.status}")
    print("   Cleanup complete!")

    # SCENARIO 4: API for Test Data, UI for User Flow
    print("\n--- Scenario 4: Complete Test Pattern ---")

    print("""
    Typical test structure:

    def test_user_can_edit_profile():
        # SETUP via API (fast)
        user = api.post("/users", data={...}).json()

        # TEST via UI (what users actually do)
        page.goto(f"/users/{user['id']}/edit")
        page.fill("#name", "New Name")
        page.click("#save")
        expect(page.locator(".success")).to_be_visible()

        # VERIFY via API (reliable)
        updated = api.get(f"/users/{user['id']}").json()
        assert updated["name"] == "New Name"

        # CLEANUP via API (fast)
        api.delete(f"/users/{user['id']}")
    """)

    # SCENARIO 5: Using API Token in Browser
    print("\n--- Scenario 5: API Auth -> Browser Auth ---")

    # Step 1: Get token via API
    print("\n1. Getting auth token via API...")
    # In real app:
    # response = api.post("/auth/login", data={
    #     "email": "test@example.com",
    #     "password": "password"
    # })
    # token = response.json()["token"]

    fake_token = "fake-jwt-token-12345"
    print(f"   Got token: {fake_token[:20]}...")

    # Step 2: Use token in browser context
    print("\n2. Creating authenticated browser context...")
    auth_context = browser.new_context(
        extra_http_headers={
            "Authorization": f"Bearer {fake_token}"
        }
    )
    auth_page = auth_context.new_page()
    print("   Browser context with auth header created")

    # Now all browser requests include the token!
    # auth_page.goto("/dashboard")  # Would be authenticated

    auth_context.close()

    # Cleanup
    api.dispose()
    context.close()
    browser.close()

    print("\n" + "=" * 50)
    print("=== Demo Complete ===")
    print("\nBenefits of combining API + UI:")
    print("  ✓ Fast setup (API) + Real testing (UI)")
    print("  ✓ Reliable verification (API)")
    print("  ✓ Quick cleanup (API)")
    print("  ✓ Share auth between API and browser")
    print("  ✓ Test at the right level")
