"""Example 1: Opening and Managing Multiple Pages/Tabs"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    print("=== Multiple Pages Demo ===\n")

    # Example 1: Creating multiple pages
    print("1. Creating multiple pages in same context...")
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://the-internet.herokuapp.com/")
    page2.goto("https://example.com/")

    print(f"   Page 1 URL: {page1.url}")
    print(f"   Page 2 URL: {page2.url}")
    print(f"   ✓ Created 2 pages")

    # Example 2: Count all pages
    print("\n2. Counting pages in context...")
    all_pages = context.pages
    print(f"   ✓ Total pages: {len(all_pages)}")

    # Example 3: Find page by URL
    print("\n3. Finding page by URL...")
    for p in context.pages:
        if "herokuapp" in p.url:
            print(f"   ✓ Found herokuapp page: {p.url}")
        if "example.com" in p.url:
            print(f"   ✓ Found example.com page: {p.url}")

    # Example 4: Find page by title
    print("\n4. Finding page by title...")
    for p in context.pages:
        title = p.title()
        print(f"   Page title: '{title}'")

    # Example 5: Work with specific page
    print("\n5. Working with specific pages...")
    page1.locator("a[href='/login']").click()
    expect(page1).to_have_url("**/login")
    print("   ✓ Navigated page1 to login")

    # Example 6: Create third page
    print("\n6. Creating a third page...")
    page3 = context.new_page()
    page3.goto("https://playwright.dev")
    print(f"   ✓ Page 3 URL: {page3.url}")
    print(f"   ✓ Total pages now: {len(context.pages)}")

    # Example 7: Close specific page
    print("\n7. Closing page2...")
    page2.close()
    print(f"   ✓ Pages after close: {len(context.pages)}")

    # Example 8: List remaining pages
    print("\n8. Remaining pages:")
    for i, p in enumerate(context.pages):
        print(f"   {i}: {p.url}")

    print("\n=== Demo Complete ===")
    browser.close()
