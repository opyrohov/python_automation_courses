"""Example 5: Artifacts Management"""
from playwright.sync_api import sync_playwright
from datetime import datetime
import os
import shutil


def create_artifact_directory():
    """Create a timestamped directory for test artifacts."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"artifacts/test_run_{timestamp}"

    # Create subdirectories
    os.makedirs(f"{base_dir}/screenshots", exist_ok=True)
    os.makedirs(f"{base_dir}/videos", exist_ok=True)

    return base_dir


def capture_step(page, artifact_dir, step_number, step_name):
    """Capture a screenshot for a test step."""
    filename = f"{step_number:02d}_{step_name}.png"
    path = f"{artifact_dir}/screenshots/{filename}"
    page.screenshot(path=path)
    print(f"   Screenshot: {filename}")
    return path


def capture_on_failure(page, artifact_dir, test_name, error):
    """Capture screenshot and page content on failure."""
    timestamp = datetime.now().strftime("%H%M%S")

    # Screenshot
    screenshot_path = f"{artifact_dir}/screenshots/FAILURE_{test_name}_{timestamp}.png"
    page.screenshot(path=screenshot_path, full_page=True)

    # Page HTML
    html_path = f"{artifact_dir}/screenshots/FAILURE_{test_name}_{timestamp}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page.content())

    print(f"   Failure captured: {screenshot_path}")
    return screenshot_path


with sync_playwright() as p:
    print("=== Artifacts Management Demo ===\n")

    # Create artifact directory for this test run
    artifact_dir = create_artifact_directory()
    print(f"1. Created artifact directory: {artifact_dir}\n")

    browser = p.chromium.launch(headless=False, slow_mo=300)

    # Context with video recording
    context = browser.new_context(
        record_video_dir=f"{artifact_dir}/videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()

    print("2. Running test scenario with step-by-step screenshots...")

    try:
        # Step 1: Navigate to login
        page.goto("https://the-internet.herokuapp.com/login")
        capture_step(page, artifact_dir, 1, "login_page")

        # Step 2: Enter username
        page.locator("#username").fill("tomsmith")
        capture_step(page, artifact_dir, 2, "username_entered")

        # Step 3: Enter password
        page.locator("#password").fill("SuperSecretPassword!")
        capture_step(page, artifact_dir, 3, "password_entered")

        # Step 4: Click login
        page.locator("button[type='submit']").click()
        page.wait_for_load_state()
        capture_step(page, artifact_dir, 4, "after_login")

        # Step 5: Verify success
        success = page.locator(".flash.success")
        if success.is_visible():
            capture_step(page, artifact_dir, 5, "success_verified")
            print("\n3. Test PASSED!")
        else:
            raise Exception("Login failed - no success message")

    except Exception as e:
        print(f"\n3. Test FAILED: {e}")
        capture_on_failure(page, artifact_dir, "login_test", e)

    # Save video with meaningful name
    video_path = f"{artifact_dir}/videos/login_test.webm"
    page.video.save_as(video_path)
    print(f"\n4. Video saved: {video_path}")

    # Close context to finalize video
    context.close()

    # List all artifacts
    print(f"\n5. Artifacts created in {artifact_dir}:")
    for root, dirs, files in os.walk(artifact_dir):
        level = root.replace(artifact_dir, '').count(os.sep)
        indent = '   ' * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = '   ' * (level + 1)
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            print(f"{subindent}{file} ({size:,} bytes)")

    print("\n=== Demo Complete ===")
    browser.close()
