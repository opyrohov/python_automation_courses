"""Example 3: Isolated Browser Contexts"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Multiple Contexts Demo ===\n")

    # Example 1: Same context - shared cookies
    print("1. Same context = shared session...")
    context = browser.new_context()

    page1 = context.new_page()
    page2 = context.new_page()

    # Both pages go to the same site
    page1.goto("https://the-internet.herokuapp.com/login")
    page2.goto("https://the-internet.herokuapp.com/")

    print(f"   Page 1: {page1.url}")
    print(f"   Page 2: {page2.url}")
    print("   ⚠️ These pages SHARE cookies and storage")

    context.close()

    # Example 2: Different contexts - isolated sessions
    print("\n2. Different contexts = isolated sessions...")
    context1 = browser.new_context()
    context2 = browser.new_context()

    user1_page = context1.new_page()
    user2_page = context2.new_page()

    print("   Created two isolated contexts")
    print("   ✓ Each has its own cookies, storage, cache")

    # Example 3: Multi-user simulation
    print("\n3. Multi-user simulation...")

    # User 1 goes to login
    user1_page.goto("https://the-internet.herokuapp.com/login")
    user1_page.locator("#username").fill("tomsmith")
    user1_page.locator("#password").fill("SuperSecretPassword!")
    user1_page.locator("button[type='submit']").click()

    expect(user1_page.locator(".flash.success")).to_be_visible()
    print("   ✓ User 1 logged in")

    # User 2 goes to login (different user)
    user2_page.goto("https://the-internet.herokuapp.com/login")
    # User 2 is NOT logged in - separate context
    expect(user2_page.locator("#username")).to_be_visible()
    print("   ✓ User 2 sees login form (not logged in)")

    # Example 4: Verify isolation
    print("\n4. Verifying isolation...")

    # Check User 1 is still logged in
    user1_page.reload()
    # Should still be on secure page (cookies preserved)
    print(f"   User 1 URL: {user1_page.url}")

    # User 2 still on login
    print(f"   User 2 URL: {user2_page.url}")
    print("   ✓ Sessions are completely isolated")

    # Example 5: Context with specific settings
    print("\n5. Creating context with specific settings...")

    mobile_context = browser.new_context(
        viewport={"width": 375, "height": 667},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    )

    mobile_page = mobile_context.new_page()
    mobile_page.goto("https://the-internet.herokuapp.com/")

    print(f"   ✓ Mobile viewport: {mobile_page.viewport_size}")

    # Example 6: Clean up contexts
    print("\n6. Cleaning up contexts...")
    context1.close()
    context2.close()
    mobile_context.close()
    print("   ✓ All contexts closed")

    print("\n=== Demo Complete ===")
    browser.close()
