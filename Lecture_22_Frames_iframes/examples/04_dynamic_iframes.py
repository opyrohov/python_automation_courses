"""Example 4: Dynamic iframe Loading and Waiting"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Dynamic iframes Demo ===\n")

    # Example 1: Waiting for iframe to be attached
    print("1. Waiting for iframe to be attached to DOM...")
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Wait for iframe element to exist in DOM
    iframe_locator = page.locator("#mce_0_ifr")
    expect(iframe_locator).to_be_attached()
    print("   ✓ iframe is attached to DOM")

    # Wait for iframe to be visible
    expect(iframe_locator).to_be_visible()
    print("   ✓ iframe is visible")

    # Example 2: Waiting for content inside iframe
    print("\n2. Waiting for content inside iframe...")

    frame = page.frame_locator("#mce_0_ifr")

    # Wait for specific element inside iframe
    editor_body = frame.locator("#tinymce")
    expect(editor_body).to_be_visible()
    print("   ✓ Editor body is visible inside iframe")

    # Wait for element to have specific text
    expect(editor_body).to_contain_text("")  # Ensure it's ready
    print("   ✓ Editor is ready for input")

    # Example 3: Waiting with custom timeout
    print("\n3. Using custom timeouts for slow-loading iframes...")

    # Clear and fill the editor
    editor_body.clear()
    editor_body.fill("Testing dynamic content")

    # Wait with extended timeout (useful for slow connections)
    expect(editor_body).to_have_text("Testing dynamic content", timeout=10000)
    print("   ✓ Content verified with 10s timeout")

    # Example 4: Polling for iframe appearance
    print("\n4. Checking for iframe before accessing...")

    page.goto("https://the-internet.herokuapp.com/iframe")

    # Good practice: always verify iframe exists first
    iframe_element = page.locator("#mce_0_ifr")

    # Check count before accessing
    if iframe_element.count() > 0:
        print("   ✓ iframe exists, proceeding to access...")
        frame = page.frame_locator("#mce_0_ifr")
        expect(frame.locator("#tinymce")).to_be_visible()
        print("   ✓ Successfully accessed iframe content")
    else:
        print("   ✗ iframe not found on page")

    # Example 5: Handling iframe that may or may not exist
    print("\n5. Gracefully handling optional iframes...")

    # Try to find an ad iframe that may not exist
    ad_iframe = page.locator("iframe[id*='google_ads']")

    if ad_iframe.count() > 0:
        print("   Ad iframe found - attempting to close")
        try:
            ad_frame = page.frame_locator("iframe[id*='google_ads']")
            close_btn = ad_frame.locator(".close, .dismiss, [aria-label='Close']")
            if close_btn.count() > 0 and close_btn.is_visible():
                close_btn.click()
                print("   ✓ Closed ad iframe")
        except Exception as e:
            print(f"   Could not close ad: {e}")
    else:
        print("   ✓ No ad iframe present - continuing with test")

    # Example 6: Waiting for iframe after page action
    print("\n6. Waiting for iframe after triggering action...")

    # Navigate to a page where iframe appears after action
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Simulate scenario: clear editor and wait for it to update
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")

    # Type something
    editor.clear()
    editor.fill("Before refresh")
    expect(editor).to_have_text("Before refresh")
    print("   ✓ Initial content set")

    # Clear and type new content
    editor.clear()
    editor.fill("After update")

    # Wait for the change
    expect(editor).to_have_text("After update")
    print("   ✓ Content updated and verified")

    # Example 7: Re-accessing iframe after page navigation
    print("\n7. Re-accessing iframe after navigation...")

    # Navigate away and back
    page.goto("https://the-internet.herokuapp.com/")
    print("   Navigated away from iframe page")

    page.goto("https://the-internet.herokuapp.com/iframe")
    print("   Navigated back to iframe page")

    # Must re-query the iframe (old reference is stale)
    new_frame = page.frame_locator("#mce_0_ifr")
    expect(new_frame.locator("#tinymce")).to_be_visible()
    print("   ✓ Re-accessed iframe after navigation")

    print("\n=== Demo Complete ===")
    browser.close()
