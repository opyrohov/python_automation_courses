"""Example 5: Multiple User Sessions"""
from playwright.sync_api import sync_playwright, expect
import os

# Note: In a real scenario, you would have different credentials for each user
# For this demo, we'll simulate with the same credentials but show the concept

ADMIN_AUTH = "admin_auth.json"
USER_AUTH = "user_auth.json"


def login_and_save(browser, username, password, auth_file):
    """Login with given credentials and save auth state."""
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/secure")

    context.storage_state(path=auth_file)
    print(f"   Saved auth state to {auth_file}")

    context.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Multiple User Sessions Demo ===\n")

    # Step 1: Create auth states for different "users"
    # (In real scenario, these would be different accounts)
    print("1. Creating auth states for users...")
    login_and_save(browser, "tomsmith", "SuperSecretPassword!", ADMIN_AUTH)
    login_and_save(browser, "tomsmith", "SuperSecretPassword!", USER_AUTH)
    print("   ✓ Auth states created\n")

    # Step 2: Create separate contexts for each user
    print("2. Creating isolated contexts for each user...")
    admin_context = browser.new_context(storage_state=ADMIN_AUTH)
    user_context = browser.new_context(storage_state=USER_AUTH)
    guest_context = browser.new_context()  # No auth - guest user

    admin_page = admin_context.new_page()
    user_page = user_context.new_page()
    guest_page = guest_context.new_page()
    print("   ✓ Three contexts created: admin, user, guest\n")

    # Step 3: Demonstrate all three can work simultaneously
    print("3. Testing all three users simultaneously...")

    # Admin accesses secure page
    admin_page.goto("https://the-internet.herokuapp.com/secure")
    if admin_page.locator("h2").text_content() == "Secure Area":
        print("   Admin: ✓ Has access to Secure Area")
    else:
        print("   Admin: ✗ No access")

    # User accesses secure page
    user_page.goto("https://the-internet.herokuapp.com/secure")
    if user_page.locator("h2").text_content() == "Secure Area":
        print("   User: ✓ Has access to Secure Area")
    else:
        print("   User: ✗ No access")

    # Guest tries to access secure page
    guest_page.goto("https://the-internet.herokuapp.com/secure")
    if "/login" in guest_page.url:
        print("   Guest: ✓ Correctly redirected to login")
    else:
        print("   Guest: ✗ Unexpected access")

    # Step 4: Show isolation - actions in one context don't affect others
    print("\n4. Demonstrating session isolation...")

    # Admin logs out
    admin_page.goto("https://the-internet.herokuapp.com/secure")
    admin_page.locator("a[href='/logout']").click()
    print("   Admin logged out")

    # User should still be logged in (different context)
    user_page.reload()
    expect(user_page.locator("h2")).to_have_text("Secure Area")
    print("   User: ✓ Still logged in (isolated session)")

    # Step 5: Multi-user interaction scenario
    print("\n5. Multi-user interaction scenario...")

    # Both users view the same page (different perspectives)
    admin_page.goto("https://the-internet.herokuapp.com/tables")
    user_page.goto("https://the-internet.herokuapp.com/tables")

    admin_rows = admin_page.locator("table#table1 tbody tr").count()
    user_rows = user_page.locator("table#table1 tbody tr").count()

    print(f"   Admin sees: {admin_rows} rows")
    print(f"   User sees: {user_rows} rows")
    print("   ✓ Both users can interact with the same content")

    # Cleanup
    admin_context.close()
    user_context.close()
    guest_context.close()

    # Clean up auth files
    for f in [ADMIN_AUTH, USER_AUTH]:
        if os.path.exists(f):
            os.remove(f)

    print("\n=== Demo Complete ===")
    print("Key takeaways:")
    print("- Each context has completely isolated session")
    print("- Logout in one context doesn't affect others")
    print("- Perfect for testing multi-user scenarios")

    browser.close()
