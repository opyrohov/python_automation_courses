"""Example 5: Real-World Multi-Page Scenarios"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Real-World Scenarios Demo ===\n")

    # Scenario 1: Comparing prices on two stores
    print("1. Scenario: Comparing two pages side by side...")

    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()

    # Open two different sites
    page1.goto("https://the-internet.herokuapp.com/tables")
    page2.goto("https://the-internet.herokuapp.com/challenging_dom")

    # Extract data from both
    table1_rows = page1.locator("table#table1 tbody tr").count()
    buttons_count = page2.locator("a.button").count()

    print(f"   Page 1: {table1_rows} table rows")
    print(f"   Page 2: {buttons_count} buttons")
    print("   ✓ Data extracted from both pages")

    context.close()

    # Scenario 2: Multi-user authentication testing
    print("\n2. Scenario: Two users - Admin and Regular user...")

    admin_context = browser.new_context()
    user_context = browser.new_context()

    admin_page = admin_context.new_page()
    user_page = user_context.new_page()

    # Admin logs in
    admin_page.goto("https://the-internet.herokuapp.com/login")
    admin_page.locator("#username").fill("tomsmith")
    admin_page.locator("#password").fill("SuperSecretPassword!")
    admin_page.locator("button[type='submit']").click()

    expect(admin_page.locator(".flash.success")).to_be_visible()
    print("   ✓ Admin logged in")

    # User tries to access secure page (should fail - not logged in)
    user_page.goto("https://the-internet.herokuapp.com/secure")
    # Will redirect to login
    expect(user_page.locator("#username")).to_be_visible()
    print("   ✓ User redirected to login (not authenticated)")

    # Verify isolation - admin still logged in
    admin_page.reload()
    expect(admin_page.locator(".flash.success")).to_be_visible()
    print("   ✓ Admin session preserved (isolated context)")

    admin_context.close()
    user_context.close()

    # Scenario 3: Testing popup flow
    print("\n3. Scenario: Complete popup workflow...")

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/windows")

    # Step 1: Open popup
    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    popup = popup_info.value
    popup.wait_for_load_state()
    print("   Step 1: Popup opened")

    # Step 2: Interact with popup
    popup_content = popup.locator("h3").text_content()
    print(f"   Step 2: Got content - '{popup_content}'")

    # Step 3: Close popup
    popup.close()
    print("   Step 3: Popup closed")

    # Step 4: Continue on main page
    expect(page.locator("h3")).to_have_text("Opening a new window")
    print("   Step 4: Verified main page")
    print("   ✓ Complete workflow done")

    context.close()

    # Scenario 4: Parallel browsing - different pages same context
    print("\n4. Scenario: Parallel data collection...")

    context = browser.new_context()

    urls = [
        "https://the-internet.herokuapp.com/tables",
        "https://the-internet.herokuapp.com/checkboxes",
        "https://the-internet.herokuapp.com/dropdown"
    ]

    pages = []
    for url in urls:
        p = context.new_page()
        p.goto(url)
        pages.append(p)

    print(f"   ✓ Opened {len(pages)} pages")

    # Collect data from all pages
    for p in pages:
        title = p.locator("h3").text_content()
        print(f"   - {title}")

    # Close all
    for p in pages:
        p.close()

    context.close()

    # Scenario 5: Handle external link that opens in new tab
    print("\n5. Scenario: External link handling...")

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")

    # Find link that might open externally
    link_count = page.locator("a").count()
    print(f"   Found {link_count} links on page")

    # Simulate clicking link that opens new tab
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as new_tab_info:
        page.locator("a[href='/windows/new']").click()

    new_tab = new_tab_info.value
    new_tab.wait_for_load_state()

    print(f"   ✓ New tab opened: {new_tab.url}")

    # Verify and close
    expect(new_tab.locator("h3")).to_have_text("New Window")
    new_tab.close()

    print("   ✓ External link workflow complete")

    context.close()

    print("\n=== Demo Complete ===")
    browser.close()
