# Solutions - Lecture 24: Screenshots & Videos

## Exercise 1: Capture Login Flow

```python
"""Exercise 1 Solution: Capture Login Flow"""
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: Capture Login Flow ===\n")

    # Create screenshots folder
    os.makedirs("screenshots", exist_ok=True)
    print("1. Screenshots folder created")

    # Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print("2. Navigated to login page")

    # Screenshot 1 - Initial login page
    page.screenshot(
        path="screenshots/01_login_page.png",
        animations="disabled"
    )
    print("3. Screenshot: 01_login_page.png")

    # Fill username
    page.locator("#username").fill("tomsmith")
    print("4. Username filled")

    # Screenshot 2 - After username
    page.screenshot(
        path="screenshots/02_username_filled.png",
        animations="disabled"
    )
    print("5. Screenshot: 02_username_filled.png")

    # Fill password
    page.locator("#password").fill("SuperSecretPassword!")
    print("6. Password filled")

    # Screenshot 3 - After password
    page.screenshot(
        path="screenshots/03_password_filled.png",
        animations="disabled"
    )
    print("7. Screenshot: 03_password_filled.png")

    # Click login button
    page.locator("button[type='submit']").click()
    page.wait_for_load_state()
    print("8. Login button clicked")

    # Screenshot 4 - Result page
    page.screenshot(
        path="screenshots/04_result_page.png",
        animations="disabled"
    )
    print("9. Screenshot: 04_result_page.png")

    # Full page screenshot
    page.screenshot(
        path="screenshots/05_result_full_page.png",
        full_page=True,
        animations="disabled"
    )
    print("10. Screenshot: 05_result_full_page.png (full page)")

    # List all screenshots
    print("\nScreenshots created:")
    for f in sorted(os.listdir("screenshots")):
        size = os.path.getsize(f"screenshots/{f}")
        print(f"   - {f} ({size:,} bytes)")

    print("\nExercise 1 completed!")
    browser.close()
```

### Key Points:
- Use `os.makedirs(..., exist_ok=True)` to create folder if not exists
- Use descriptive, numbered filenames for proper ordering
- `animations="disabled"` ensures consistent screenshots
- `full_page=True` captures entire scrollable content
- Always `wait_for_load_state()` after navigation

---

## Exercise 2: Record Video of Test Scenario

```python
"""Exercise 2 Solution: Record Video of Test Scenario"""
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Exercise 2: Record Video of Test ===\n")

    # Create videos folder
    os.makedirs("videos", exist_ok=True)
    print("1. Videos folder created")

    # Create context with video recording
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    print("2. Context created with video recording")

    page = context.new_page()
    video_path = None

    try:
        # Navigate to main page
        page.goto("https://the-internet.herokuapp.com/")
        print("3. Navigated to main page")

        # Click on Form Authentication link
        page.locator("a[href='/login']").click()
        page.wait_for_load_state()
        print("4. Clicked Form Authentication link")

        # Fill login form
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        print("5. Login form filled")

        # Submit form
        page.locator("button[type='submit']").click()
        page.wait_for_load_state()
        print("6. Form submitted")

        # Verify success
        success_message = page.locator(".flash.success")
        assert success_message.is_visible(), "Success message not visible!"
        print("7. Login verified - success message visible")

        # Logout
        page.locator("a[href='/logout']").click()
        page.wait_for_load_state()
        print("8. Logged out")

        # Save video with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        video_path = f"videos/login_test_{timestamp}.webm"
        page.video.save_as(video_path)
        print(f"9. Video saved: {video_path}")

    except Exception as e:
        # Capture failure screenshot
        print(f"\nTest FAILED: {e}")
        page.screenshot(path="videos/FAILURE_screenshot.png", full_page=True)
        print("Failure screenshot saved: videos/FAILURE_screenshot.png")
        raise

    finally:
        # Close context to finalize video
        context.close()
        print("10. Context closed - video finalized")

    # Print video size
    if video_path and os.path.exists(video_path):
        size = os.path.getsize(video_path)
        print(f"\nVideo file size: {size:,} bytes ({size / 1024 / 1024:.2f} MB)")

    print("\nExercise 2 completed!")
    browser.close()
```

### Key Points:
- Video recording is set at context level, not page level
- Always close context to save the video properly
- Use try/except/finally to handle errors and still save video
- `page.video.save_as()` copies video to a custom path
- Video format is WebM

---

## Bonus Challenges

### Challenge 1: Element Screenshot Gallery

```python
"""Bonus: Create a gallery of element screenshots"""
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    os.makedirs("gallery", exist_ok=True)

    page.goto("https://the-internet.herokuapp.com/")

    # Screenshot each link as a separate image
    links = page.locator("ul li a")
    count = links.count()

    for i in range(min(count, 10)):  # Limit to 10
        link = links.nth(i)
        text = link.text_content().strip()
        safe_name = "".join(c if c.isalnum() else "_" for c in text)
        link.screenshot(path=f"gallery/{i+1:02d}_{safe_name}.png")
        print(f"Captured: {text}")

    browser.close()
```

### Challenge 2: Compare Before/After Screenshots

```python
"""Bonus: Before/After comparison"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Before screenshot
    before = page.screenshot()
    print(f"Before: {len(before)} bytes")

    # Toggle checkboxes
    page.locator("input[type='checkbox']").first.click()
    page.locator("input[type='checkbox']").last.click()

    # After screenshot
    after = page.screenshot()
    print(f"After: {len(after)} bytes")

    # Simple comparison
    if before == after:
        print("Screenshots are identical")
    else:
        print("Screenshots differ!")
        # Save both for manual comparison
        with open("before.png", "wb") as f:
            f.write(before)
        with open("after.png", "wb") as f:
            f.write(after)

    browser.close()
```

### Challenge 3: Video with Automatic Cleanup

```python
"""Bonus: Video recording with cleanup for passed tests"""
from playwright.sync_api import sync_playwright
import os
import shutil

def run_test_with_video(test_name, test_func):
    """Run a test with video, keep video only if test fails."""
    video_dir = f"temp_videos/{test_name}"
    os.makedirs(video_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir=video_dir,
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        test_passed = False
        try:
            test_func(page)
            test_passed = True
            print(f"Test '{test_name}' PASSED")
        except Exception as e:
            print(f"Test '{test_name}' FAILED: {e}")
            # Save failure video
            os.makedirs("failed_videos", exist_ok=True)
            page.video.save_as(f"failed_videos/{test_name}.webm")
        finally:
            context.close()
            browser.close()

        # Cleanup temp videos
        shutil.rmtree(video_dir, ignore_errors=True)
        if not os.listdir("temp_videos"):
            os.rmdir("temp_videos")

        return test_passed


# Example test function
def login_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    assert page.locator(".flash.success").is_visible()


# Run test
run_test_with_video("login_flow", login_test)
```

---

## Common Mistakes to Avoid

### Mistake 1: Not waiting before screenshot
```python
# WRONG - page may not be loaded
page.goto("https://example.com")
page.screenshot(path="screenshot.png")  # May capture loading state!

# CORRECT - wait for load
page.goto("https://example.com")
page.wait_for_load_state("networkidle")  # Wait for page to settle
page.screenshot(path="screenshot.png")
```

### Mistake 2: Forgetting to close context for video
```python
# WRONG - video won't be saved
context = browser.new_context(record_video_dir="videos/")
page = context.new_page()
page.goto("https://example.com")
browser.close()  # Video may be incomplete!

# CORRECT - close context first
context = browser.new_context(record_video_dir="videos/")
page = context.new_page()
page.goto("https://example.com")
context.close()  # This saves the video
browser.close()
```

### Mistake 3: Using quality with PNG
```python
# WRONG - quality only works with JPEG
page.screenshot(path="image.png", quality=80)  # Error or ignored

# CORRECT - use with JPEG
page.screenshot(path="image.jpg", type="jpeg", quality=80)
```

### Mistake 4: Element not visible
```python
# WRONG - element may not be visible yet
page.locator("#dynamic-element").screenshot(path="element.png")

# CORRECT - wait for visibility
element = page.locator("#dynamic-element")
element.wait_for(state="visible")
element.screenshot(path="element.png")
```
