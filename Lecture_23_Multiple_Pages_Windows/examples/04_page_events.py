"""Example 4: Page Event Listeners"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    print("=== Page Events Demo ===\n")

    # Example 1: Listen for new pages in context
    print("1. Listening for new pages in context...")

    def on_new_page(page):
        print(f"   EVENT: New page created - {page.url or '(blank)'}")

    context.on("page", on_new_page)

    # Create pages - events will fire
    page1 = context.new_page()
    page1.goto("https://example.com")

    page2 = context.new_page()
    page2.goto("https://the-internet.herokuapp.com/")

    print("   ✓ Event listener captured page creations")

    # Example 2: Listen for page close
    print("\n2. Listening for page close...")

    close_count = 0

    def on_page_close():
        nonlocal close_count
        close_count += 1
        print(f"   EVENT: Page closed (total: {close_count})")

    page2.on("close", on_page_close)
    page2.close()

    print("   ✓ Close event captured")

    # Example 3: Console message listener
    print("\n3. Listening for console messages...")

    page = context.new_page()

    console_messages = []

    def on_console(msg):
        console_messages.append(f"[{msg.type}] {msg.text}")
        print(f"   CONSOLE: [{msg.type}] {msg.text[:50]}...")

    page.on("console", on_console)

    # Navigate to page with console output
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # Trigger some JavaScript
    page.evaluate("console.log('Hello from Playwright!')")
    page.evaluate("console.warn('This is a warning')")

    print(f"   ✓ Captured {len(console_messages)} console messages")

    # Example 4: Dialog (alert/confirm/prompt) handling
    print("\n4. Handling JavaScript dialogs...")

    def handle_dialog(dialog):
        print(f"   DIALOG: {dialog.type} - {dialog.message}")
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Trigger an alert
    page.locator("button[onclick='jsAlert()']").click()
    page.wait_for_timeout(500)
    print("   ✓ Alert handled")

    # Trigger a confirm
    page.locator("button[onclick='jsConfirm()']").click()
    page.wait_for_timeout(500)
    print("   ✓ Confirm handled")

    # Example 5: Wait for popup event
    print("\n5. Waiting for popup with expect_popup()...")

    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()

    popup = popup_info.value
    popup.wait_for_load_state()
    print(f"   ✓ Popup captured: {popup.url}")
    popup.close()

    # Example 6: Request/Response events
    print("\n6. Listening for network events...")

    request_count = 0

    def on_request(request):
        nonlocal request_count
        request_count += 1

    page.on("request", on_request)

    page.goto("https://example.com")
    print(f"   ✓ Captured {request_count} network requests")

    print("\n=== Demo Complete ===")
    browser.close()
