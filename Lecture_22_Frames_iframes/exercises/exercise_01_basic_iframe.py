"""Exercise 1: Basic iframe Interaction

Your task:
1. Navigate to https://the-internet.herokuapp.com/iframe
2. Wait for the TinyMCE editor iframe to be visible
3. Access the editor inside the iframe
4. Clear any existing content
5. Type: "Hello, I am learning Playwright iframes!"
6. Verify the text was entered correctly

Hints:
- The iframe has id="mce_0_ifr"
- The editable area inside has id="tinymce"
- Use expect() to wait and verify
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: Basic iframe Interaction ===\n")

    # TODO: Navigate to the page
    # page.goto(...)

    # TODO: Wait for the iframe to be visible
    # expect(page.locator(...)).to_be_visible()

    # TODO: Get the frame locator
    # frame = page.frame_locator(...)

    # TODO: Get the editor body element inside iframe
    # editor = frame.locator(...)

    # TODO: Clear existing content
    # editor.clear()

    # TODO: Fill with new text
    # editor.fill("Hello, I am learning Playwright iframes!")

    # TODO: Verify the text
    # expect(editor).to_have_text(...)

    print("Exercise completed!")
    browser.close()
