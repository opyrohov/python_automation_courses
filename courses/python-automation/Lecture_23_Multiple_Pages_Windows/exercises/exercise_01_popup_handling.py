"""Exercise 1: Popup Handling

Your task:
1. Navigate to https://the-internet.herokuapp.com/windows
2. Click the link that opens a new window
3. Capture the popup using expect_popup()
4. Get the text content from the h3 element in the popup
5. Verify the text is "New Window"
6. Close the popup
7. Verify you're back on the main page

Hints:
- Use 'with page.expect_popup() as popup_info:'
- popup_info.value gives you the popup page
- Don't forget wait_for_load_state()
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Popup Handling ===\n")

    # TODO: Navigate to the windows page
    # page.goto(...)

    # TODO: Click the link and capture popup
    # with page.expect_popup() as popup_info:
    #     page.locator(...).click()
    # popup = popup_info.value

    # TODO: Wait for popup to load
    # popup.wait_for_load_state()

    # TODO: Get text from h3 in popup
    # popup_text = popup.locator(...).text_content()
    # print(f"Popup text: {popup_text}")

    # TODO: Verify the text
    # assert popup_text == "New Window"

    # TODO: Close the popup
    # popup.close()

    # TODO: Verify main page is still accessible
    # expect(page.locator("h3")).to_have_text("Opening a new window")

    print("Exercise completed!")
    browser.close()
