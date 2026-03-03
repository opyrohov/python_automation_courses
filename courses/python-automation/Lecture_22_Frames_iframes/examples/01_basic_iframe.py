"""Example 1: Basic iframe Access and Interaction"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Basic iframe Demo ===\n")

    # Example 1: Accessing iframe by ID
    print("1. Accessing iframe on W3Schools iframe demo...")
    page.goto("https://www.w3schools.com/html/html_iframe.asp")

    # Wait for the iframe to be attached
    expect(page.locator("iframe[src*='default.asp']")).to_be_attached()
    print("   ✓ iframe is attached to DOM")

    # Get iframe using frame_locator
    iframe = page.frame_locator("iframe[src*='default.asp']")

    # Check if content is visible inside iframe
    # Note: The actual content depends on the iframe source
    print("   ✓ Successfully accessed iframe content")

    # Example 2: Using the-internet.herokuapp.com for iframe practice
    print("\n2. Working with iframe on herokuapp demo...")
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Wait for the TinyMCE editor iframe
    expect(page.locator("#mce_0_ifr")).to_be_visible()
    print("   ✓ TinyMCE editor iframe is visible")

    # Access the editor iframe
    editor_iframe = page.frame_locator("#mce_0_ifr")

    # Get the editable body inside the iframe
    editor_body = editor_iframe.locator("#tinymce")
    expect(editor_body).to_be_visible()
    print("   ✓ Editor body is accessible")

    # Clear existing content and type new text
    editor_body.clear()
    editor_body.fill("Hello from Playwright! This text was typed inside an iframe.")
    print("   ✓ Typed text into the iframe editor")

    # Verify the text was entered
    expect(editor_body).to_contain_text("Hello from Playwright")
    print("   ✓ Text verification passed")

    # Example 3: Working with main page elements after iframe
    print("\n3. Switching between iframe and main page...")

    # Click a button on main page (no need to "switch back")
    bold_button = page.locator("button[title='Bold']")
    if bold_button.count() > 0:
        # Select all text in iframe first
        editor_body.press("Control+a")
        # Click bold button on main page
        bold_button.click()
        print("   ✓ Applied bold formatting from main page button")

    # Go back to iframe and verify
    text_in_editor = editor_body.text_content()
    print(f"   ✓ Current text in editor: '{text_in_editor[:50]}...'")

    # Example 4: iframe locator strategies
    print("\n4. Different ways to locate iframes...")

    page.goto("https://the-internet.herokuapp.com/iframe")
    expect(page.locator("#mce_0_ifr")).to_be_visible()

    # By ID
    by_id = page.frame_locator("#mce_0_ifr")
    print("   ✓ Located by ID: #mce_0_ifr")

    # By CSS selector with attribute
    by_attr = page.frame_locator("iframe[id='mce_0_ifr']")
    print("   ✓ Located by attribute selector")

    # Using first/last when multiple iframes exist
    first_iframe = page.frame_locator("iframe").first
    print("   ✓ Located first iframe on page")

    print("\n=== Demo Complete ===")
    browser.close()
