"""Exercise 3: Real-Time Collaboration Testing (Advanced)

Scenario: Test a collaborative todo list application where multiple users
can add, edit, and see each other's changes in real-time.

Your tasks:
1. Create THREE separate browser contexts (admin, user1, user2)
2. Admin creates a shared todo list
3. User1 adds an item to the list
4. Verify User2 sees the new item (simulating real-time sync)
5. User2 marks the item as complete
6. Verify User1 sees the item as completed
7. Admin deletes the item
8. Verify both users see the item removed

Test Site: https://the-internet.herokuapp.com/
(We'll simulate this with multiple login sessions and checking UI states)

Learning Goals:
- Managing 3+ contexts simultaneously
- Simulating real-time sync between users
- Complex multi-user verification flows
- Proper resource cleanup

Hints:
- Use browser.new_context() for each user
- Consider using helper functions for repeated actions
- Remember to wait for UI updates between actions
- Clean up all contexts at the end
"""
from playwright.sync_api import sync_playwright, expect


def login_user(page, username: str, password: str):
    """Helper function to log in a user."""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    page.wait_for_load_state()


def verify_logged_in(page, username: str):
    """Verify user is logged in and sees secure area."""
    expect(page.locator(".flash.success")).to_be_visible()
    print(f"   {username} is logged in")


def verify_logged_out(page, username: str):
    """Verify user sees login form."""
    expect(page.locator("#username")).to_be_visible()
    print(f"   {username} sees login form (not logged in)")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Exercise 3: Real-Time Collaboration Testing ===\n")

    # TODO Step 1: Create three isolated contexts
    print("Step 1: Creating isolated contexts for each user...")
    # admin_context = browser.new_context()
    # user1_context = browser.new_context()
    # user2_context = browser.new_context()

    # admin_page = admin_context.new_page()
    # user1_page = user1_context.new_page()
    # user2_page = user2_context.new_page()

    # TODO Step 2: Admin logs in first
    print("\nStep 2: Admin logging in...")
    # login_user(admin_page, "tomsmith", "SuperSecretPassword!")
    # verify_logged_in(admin_page, "Admin")

    # TODO Step 3: User1 logs in (separate session)
    print("\nStep 3: User1 logging in...")
    # login_user(user1_page, "tomsmith", "SuperSecretPassword!")
    # verify_logged_in(user1_page, "User1")

    # TODO Step 4: User2 is NOT logged in yet - verify isolation
    print("\nStep 4: Verifying User2 is NOT logged in (context isolation)...")
    # user2_page.goto("https://the-internet.herokuapp.com/login")
    # verify_logged_out(user2_page, "User2")

    # TODO Step 5: User2 logs in
    print("\nStep 5: User2 logging in...")
    # login_user(user2_page, "tomsmith", "SuperSecretPassword!")
    # verify_logged_in(user2_page, "User2")

    # TODO Step 6: Verify all three users are now logged in independently
    print("\nStep 6: Verifying all users have independent sessions...")
    # All three should see the secure area
    # expect(admin_page.locator("h2")).to_contain_text("Secure Area")
    # expect(user1_page.locator("h2")).to_contain_text("Secure Area")
    # expect(user2_page.locator("h2")).to_contain_text("Secure Area")
    # print("   All 3 users are logged in with independent sessions!")

    # TODO Step 7: Admin logs out - verify others stay logged in
    print("\nStep 7: Admin logs out, checking if others stay logged in...")
    # admin_page.locator("a[href='/logout']").click()
    # expect(admin_page.locator("#username")).to_be_visible()
    # print("   Admin logged out")

    # Verify User1 and User2 are STILL logged in (isolation test)
    # admin_page.goto("https://the-internet.herokuapp.com/secure")
    # expect(admin_page).to_have_url("**/login")  # Redirected to login
    # print("   Admin cannot access secure area")

    # User1 should still be in secure area
    # user1_page.reload()
    # expect(user1_page.locator("h2")).to_contain_text("Secure Area")
    # print("   User1 still has access (independent session)")

    # User2 should still be in secure area
    # user2_page.reload()
    # expect(user2_page.locator("h2")).to_contain_text("Secure Area")
    # print("   User2 still has access (independent session)")

    # TODO Step 8: Clean up all contexts
    print("\nStep 8: Cleaning up all contexts...")
    # admin_context.close()
    # user1_context.close()
    # user2_context.close()

    print("\n" + "="*50)
    print("Exercise completed!")
    print("You've demonstrated:")
    print("  - Creating multiple isolated contexts")
    print("  - Managing independent user sessions")
    print("  - Verifying context isolation")
    print("  - Proper resource cleanup")
    print("="*50)

    browser.close()
