"""Example 4: Screenshot Options"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Screenshot Options Demo ===\n")

    # Navigate to a page
    page.goto("https://the-internet.herokuapp.com/tables")
    print("1. Navigated to tables page")

    # PNG format (default) - lossless compression
    page.screenshot(path="format_png.png", type="png")
    print("2. PNG screenshot saved: format_png.png")

    # JPEG format with quality setting
    page.screenshot(path="format_jpeg.jpg", type="jpeg", quality=80)
    print("3. JPEG screenshot (quality 80) saved: format_jpeg.jpg")

    # JPEG with lower quality (smaller file)
    page.screenshot(path="format_jpeg_low.jpg", type="jpeg", quality=30)
    print("4. JPEG screenshot (quality 30) saved: format_jpeg_low.jpg")

    # Clipping - capture specific region
    page.screenshot(
        path="clipped_region.png",
        clip={
            "x": 100,
            "y": 100,
            "width": 400,
            "height": 300
        }
    )
    print("5. Clipped region screenshot saved: clipped_region.png")

    # Navigate to page with animations
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Screenshot with animations disabled
    page.screenshot(path="animations_disabled.png", animations="disabled")
    print("6. Screenshot with animations disabled saved: animations_disabled.png")

    # Scale options
    page.goto("https://the-internet.herokuapp.com/")

    # CSS scale (default)
    page.screenshot(path="scale_css.png", scale="css")
    print("7. CSS scale screenshot saved: scale_css.png")

    # Device scale (higher resolution on HiDPI)
    page.screenshot(path="scale_device.png", scale="device")
    print("8. Device scale screenshot saved: scale_device.png")

    # Transparent background (for elements with transparency)
    page.goto("https://the-internet.herokuapp.com/floating_menu")
    page.screenshot(path="transparent_bg.png", omit_background=True)
    print("9. Transparent background screenshot saved: transparent_bg.png")

    # Timeout option
    page.screenshot(path="with_timeout.png", timeout=30000)
    print("10. Screenshot with custom timeout saved: with_timeout.png")

    # Compare file sizes
    import os
    files = ["format_png.png", "format_jpeg.jpg", "format_jpeg_low.jpg"]
    print("\n--- File Size Comparison ---")
    for f in files:
        if os.path.exists(f):
            size = os.path.getsize(f)
            print(f"   {f}: {size:,} bytes")

    print("\n=== Demo Complete ===")
    browser.close()
