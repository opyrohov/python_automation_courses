"""Example 2: Handling Popups and New Windows"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Popup Handling Demo ===\n")

    # Example 1: Handling target="_blank" links
    print("1. Handling link with target='_blank'...")
    page.goto("https://the-internet.herokuapp.com/windows")

    # Click link that opens in new window
    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()

    new_window = popup_info.value
    new_window.wait_for_load_state()

    print(f"   ✓ New window URL: {new_window.url}")
    print(f"   ✓ New window title: {new_window.title()}")

    # Get content from new window
    content = new_window.locator("h3").text_content()
    print(f"   ✓ Content: {content}")

    # Close new window
    new_window.close()
    print("   ✓ Closed new window")

    # Example 2: Multiple windows scenario
    print("\n2. Opening multiple windows...")
    page.goto("https://the-internet.herokuapp.com/windows")

    # Open first window
    with page.expect_popup() as popup1_info:
        page.locator("a[href='/windows/new']").click()
    window1 = popup1_info.value
    window1.wait_for_load_state()
    print(f"   ✓ Window 1 opened")

    # Open second window (go back and click again)
    with page.expect_popup() as popup2_info:
        page.locator("a[href='/windows/new']").click()
    window2 = popup2_info.value
    window2.wait_for_load_state()
    print(f"   ✓ Window 2 opened")

    print(f"   ✓ Total pages: {len(context.pages)}")

    # Close all popup windows
    window1.close()
    window2.close()
    print("   ✓ Closed all popup windows")

    # Example 3: Continue on main page after popup
    print("\n3. Continuing on main page after popup closes...")
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    popup = popup_info.value
    popup.wait_for_load_state()

    # Do something in popup
    popup_text = popup.locator("h3").text_content()
    print(f"   Got from popup: {popup_text}")

    # Close popup
    popup.close()

    # Continue on main page (no need to "switch back")
    expect(page.locator("h3")).to_have_text("Opening a new window")
    print("   ✓ Back on main page, can continue working")

    # Example 4: Using page events to capture popups
    print("\n4. Using event listener for popups...")
    page.goto("https://the-internet.herokuapp.com/windows")

    captured_popups = []

    def capture_popup(popup):
        print(f"   Event: Popup captured - {popup.url}")
        captured_popups.append(popup)

    page.on("popup", capture_popup)

    # Click to open popup
    page.locator("a[href='/windows/new']").click()
    page.wait_for_timeout(1000)  # Wait for popup

    print(f"   ✓ Captured {len(captured_popups)} popup(s)")

    # Clean up
    for pop in captured_popups:
        pop.close()

    print("\n=== Demo Complete ===")
    browser.close()
