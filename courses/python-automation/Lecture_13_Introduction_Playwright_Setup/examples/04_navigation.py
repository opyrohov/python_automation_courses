"""
Example 4: Page Navigation

Demonstrates various navigation methods in Playwright.

Run: python 04_navigation.py
"""

from playwright.sync_api import sync_playwright


def main():
    """Demonstrate various navigation techniques."""

    print("=" * 60)
    print("Playwright Navigation Examples")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Example 1: Basic navigation
        print("\n1️⃣ Basic Navigation")
        print("Going to example.com...")
        page.goto("https://example.com")
        print(f"   Current URL: {page.url}")
        print(f"   Page title: {page.title()}")

        # Example 2: Navigate to another page
        print("\n2️⃣ Navigate to Another Page")
        print("Going to playwright.dev...")
        page.goto("https://playwright.dev")
        print(f"   Current URL: {page.url}")
        print(f"   Page title: {page.title()}")

        # Example 3: Go back
        print("\n3️⃣ Go Back")
        print("Going back...")
        page.go_back()
        print(f"   Current URL: {page.url}")
        print(f"   Page title: {page.title()}")

        # Example 4: Go forward
        print("\n4️⃣ Go Forward")
        print("Going forward...")
        page.go_forward()
        print(f"   Current URL: {page.url}")
        print(f"   Page title: {page.title()}")

        # Example 5: Reload
        print("\n5️⃣ Reload Page")
        print("Reloading page...")
        page.reload()
        print(f"   Page reloaded: {page.title()}")

        # Example 6: Wait for navigation
        print("\n6️⃣ Wait for Load State")
        page.goto("https://playwright.dev")

        print("   Waiting for network to be idle...")
        page.wait_for_load_state("networkidle")
        print("   ✅ Network is idle")

        print("   Waiting for DOM content loaded...")
        page.wait_for_load_state("domcontentloaded")
        print("   ✅ DOM content loaded")

        # Example 7: Navigate and wait for specific element
        print("\n7️⃣ Wait for Specific Element")
        page.goto("https://playwright.dev")

        print("   Waiting for 'Get started' link...")
        page.wait_for_selector("a:has-text('Get started')")
        print("   ✅ Element is visible")

        # Example 8: Navigate with timeout
        print("\n8️⃣ Navigate with Custom Timeout")
        try:
            print("   Navigating with 30s timeout...")
            page.goto("https://example.com", timeout=30000)
            print("   ✅ Page loaded within timeout")
        except Exception as e:
            print(f"   ❌ Timeout error: {e}")

        # Example 9: Get page info
        print("\n9️⃣ Get Page Information")
        page.goto("https://playwright.dev")

        print(f"   URL: {page.url}")
        print(f"   Title: {page.title()}")
        print(f"   Viewport: {page.viewport_size}")

        # Example 10: Navigation with wait until
        print("\n🔟 Navigate with Wait Until Options")

        # Wait until network idle
        page.goto("https://example.com", wait_until="networkidle")
        print("   ✅ Navigated (waited for network idle)")

        # Wait until DOM content loaded (faster)
        page.goto("https://playwright.dev", wait_until="domcontentloaded")
        print("   ✅ Navigated (waited for DOM content)")

        # Example 11: Check if navigation was successful
        print("\n1️⃣1️⃣ Check Response Status")
        response = page.goto("https://example.com")

        print(f"   Response status: {response.status}")
        print(f"   Response OK: {response.ok}")
        print(f"   Response URL: {response.url}")

        if response.ok:
            print("   ✅ Page loaded successfully")
        else:
            print("   ❌ Page load failed")

        print("\n" + "=" * 60)
        print("✅ All navigation examples completed!")
        print("=" * 60)

        page.wait_for_timeout(2000)
        browser.close()


if __name__ == "__main__":
    main()
