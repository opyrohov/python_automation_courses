"""
Example 5: Screenshots and Visual Testing

Demonstrates how to take screenshots in Playwright.

Run: python 05_screenshots.py
"""

from playwright.sync_api import sync_playwright
from pathlib import Path


def main():
    """Demonstrate various screenshot techniques."""

    # Create screenshots folder
    screenshots_dir = Path("screenshots_output")
    screenshots_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("Playwright Screenshots Examples")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to a page
        page.goto("https://playwright.dev")

        # Example 1: Basic screenshot
        print("\n1️⃣ Basic Screenshot")
        path1 = screenshots_dir / "01_basic.png"
        page.screenshot(path=path1)
        print(f"   ✅ Saved to: {path1}")

        # Example 2: Full page screenshot
        print("\n2️⃣ Full Page Screenshot")
        path2 = screenshots_dir / "02_full_page.png"
        page.screenshot(path=path2, full_page=True)
        print(f"   ✅ Saved full page to: {path2}")

        # Example 3: Screenshot of specific element
        print("\n3️⃣ Element Screenshot")
        path3 = screenshots_dir / "03_element.png"
        header = page.locator("header")
        header.screenshot(path=path3)
        print(f"   ✅ Saved header element to: {path3}")

        # Example 4: Screenshot with custom quality (JPEG)
        print("\n4️⃣ JPEG Screenshot with Quality")
        path4 = screenshots_dir / "04_quality.jpeg"
        page.screenshot(
            path=path4,
            type="jpeg",
            quality=80  # 0-100, only for JPEG
        )
        print(f"   ✅ Saved JPEG to: {path4}")

        # Example 5: Screenshot with clip (specific area)
        print("\n5️⃣ Clipped Screenshot")
        path5 = screenshots_dir / "05_clip.png"
        page.screenshot(
            path=path5,
            clip={
                'x': 0,
                'y': 0,
                'width': 800,
                'height': 600
            }
        )
        print(f"   ✅ Saved clipped area to: {path5}")

        # Example 6: Screenshot as bytes (for comparison)
        print("\n6️⃣ Screenshot as Bytes")
        screenshot_bytes = page.screenshot()
        print(f"   ✅ Screenshot size: {len(screenshot_bytes)} bytes")

        # Example 7: Multiple screenshots for comparison
        print("\n7️⃣ Before/After Screenshots")

        # Before
        path7a = screenshots_dir / "07a_before.png"
        page.screenshot(path=path7a)
        print(f"   ✅ Before screenshot: {path7a}")

        # Scroll down
        page.evaluate("window.scrollBy(0, 500)")
        page.wait_for_timeout(500)

        # After
        path7b = screenshots_dir / "07b_after_scroll.png"
        page.screenshot(path=path7b)
        print(f"   ✅ After screenshot: {path7b}")

        # Example 8: Screenshot with custom viewport
        print("\n8️⃣ Custom Viewport Screenshot")
        page2 = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page2.goto("https://playwright.dev")

        path8 = screenshots_dir / "08_1920x1080.png"
        page2.screenshot(path=path8)
        print(f"   ✅ 1920x1080 screenshot: {path8}")

        page2.close()

        # Example 9: Mobile screenshot
        print("\n9️⃣ Mobile Screenshot")
        iphone = p.devices['iPhone 12']
        page3 = browser.new_page(**iphone)
        page3.goto("https://playwright.dev")

        path9 = screenshots_dir / "09_mobile.png"
        page3.screenshot(path=path9)
        print(f"   ✅ Mobile screenshot: {path9}")

        page3.close()

        # Example 10: Screenshot with omit background
        print("\n🔟 Screenshot with Transparent Background")
        path10 = screenshots_dir / "10_transparent.png"
        page.screenshot(
            path=path10,
            omit_background=True  # Transparent background instead of white
        )
        print(f"   ✅ Transparent background: {path10}")

        print("\n" + "=" * 60)
        print(f"✅ All screenshots saved to: {screenshots_dir}/")
        print("=" * 60)

        browser.close()


if __name__ == "__main__":
    main()
