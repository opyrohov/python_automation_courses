"""Exercise 2: Record Video of Test Scenario

Your task:
1. Create a browser context with video recording enabled
2. Set video size to 1280x720
3. Navigate to https://the-internet.herokuapp.com/
4. Click on "Form Authentication" link
5. Perform login with username: tomsmith, password: SuperSecretPassword!
6. Verify login was successful (check for success message)
7. Click logout
8. Save video with a descriptive name including timestamp
9. Close context properly to save the video

Bonus:
- Add try/except to capture failure screenshot if something goes wrong
- Print the final video file size

Hints:
- browser.new_context(record_video_dir="videos/", record_video_size={...})
- page.video.save_as("custom_name.webm")
- Don't forget context.close() at the end!
"""
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Exercise 2: Record Video of Test ===\n")

    # TODO: Create videos folder
    # os.makedirs("videos", exist_ok=True)

    # TODO: Create context with video recording
    # context = browser.new_context(
    #     record_video_dir="videos/",
    #     record_video_size={"width": 1280, "height": 720}
    # )

    # TODO: Create page
    # page = context.new_page()

    # TODO: Navigate to main page
    # page.goto("https://the-internet.herokuapp.com/")

    # TODO: Click on Form Authentication link
    # page.locator("a[href='/login']").click()

    # TODO: Fill login form
    # page.locator("#username").fill(...)
    # page.locator("#password").fill(...)

    # TODO: Submit form
    # page.locator("button[type='submit']").click()
    # page.wait_for_load_state()

    # TODO: Verify success
    # assert page.locator(".flash.success").is_visible()
    # print("Login successful!")

    # TODO: Logout
    # page.locator("a[href='/logout']").click()
    # page.wait_for_load_state()

    # TODO: Save video with timestamp
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # video_path = f"videos/login_test_{timestamp}.webm"
    # page.video.save_as(video_path)

    # TODO: Close context to finalize video
    # context.close()

    # TODO: Print video size
    # if os.path.exists(video_path):
    #     size = os.path.getsize(video_path)
    #     print(f"Video saved: {video_path} ({size:,} bytes)")

    print("Exercise completed!")
    browser.close()
