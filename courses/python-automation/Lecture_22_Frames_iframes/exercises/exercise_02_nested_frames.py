"""Exercise 2: Nested Frames Navigation

Your task:
1. Navigate to https://the-internet.herokuapp.com/nested_frames
2. Access the top frame
3. Inside the top frame, access the middle frame
4. Get the text content from the middle frame
5. Print the text and verify it contains "MIDDLE"
6. Also get and print the content from the bottom frame

Hints:
- Top frame: frame[name='frame-top']
- Middle frame (inside top): frame[name='frame-middle']
- Content element: #content
- Bottom frame: frame[name='frame-bottom']
"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 2: Nested Frames Navigation ===\n")

    # TODO: Navigate to the nested frames page
    # page.goto(...)

    # TODO: Access the top frame
    # top_frame = page.frame_locator(...)

    # TODO: Access the middle frame (nested inside top)
    # middle_frame = top_frame.frame_locator(...)

    # TODO: Get the content element and its text
    # content = middle_frame.locator(...)
    # middle_text = content.text_content()
    # print(f"Middle frame content: {middle_text}")

    # TODO: Verify it contains "MIDDLE"
    # assert "MIDDLE" in middle_text

    # TODO: Access the bottom frame and get its content
    # bottom_frame = page.frame_locator(...)
    # bottom_text = bottom_frame.locator("body").text_content()
    # print(f"Bottom frame content: {bottom_text}")

    print("\nExercise completed!")
    browser.close()
