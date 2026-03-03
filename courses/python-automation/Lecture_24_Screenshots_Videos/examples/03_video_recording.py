"""Example 3: Video Recording"""
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# Create videos directory
os.makedirs("videos", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Video Recording Demo ===\n")

    # Create context with video recording enabled
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    print("1. Context created with video recording enabled")

    page = context.new_page()

    # Perform a test scenario - login flow
    page.goto("https://the-internet.herokuapp.com/login")
    print("2. Navigated to login page")

    page.locator("#username").fill("tomsmith")
    print("3. Filled username")

    page.locator("#password").fill("SuperSecretPassword!")
    print("4. Filled password")

    page.locator("button[type='submit']").click()
    print("5. Clicked login button")

    # Wait for navigation
    page.wait_for_load_state()
    print("6. Page loaded after login")

    # Verify login success
    success_message = page.locator(".flash.success")
    if success_message.is_visible():
        print("7. Login successful!")

    # Logout
    page.locator("a[href='/logout']").click()
    page.wait_for_load_state()
    print("8. Logged out")

    # Get video path before closing
    video_path = page.video.path()
    print(f"9. Video path: {video_path}")

    # Save with custom name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    custom_path = f"videos/login_test_{timestamp}.webm"
    page.video.save_as(custom_path)
    print(f"10. Video saved as: {custom_path}")

    # IMPORTANT: Close context to finalize video
    context.close()
    print("11. Context closed - video finalized")

    print("\n=== Demo Complete ===")
    browser.close()
