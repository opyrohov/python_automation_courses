"""
Example 3: Browser Launch Options

Demonstrates various browser configuration options.

Run: python 03_browser_options.py
"""

from playwright.sync_api import sync_playwright
import time


def example_headed_mode():
    """Launch browser in headed mode (visible window)."""

    print("\n=== Example 1: Headed Mode ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        print("✅ Browser window is visible")
        time.sleep(2)

        browser.close()


def example_headless_mode():
    """Launch browser in headless mode (no window, faster)."""

    print("\n=== Example 2: Headless Mode ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")

        print("✅ Browser running in background (no window)")
        print(f"📰 Page title: {page.title()}")

        browser.close()


def example_slow_motion():
    """Launch browser with slow motion (for debugging)."""

    print("\n=== Example 3: Slow Motion ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000  # Slow down by 1000ms (1 second) between actions
        )
        page = browser.new_page()

        print("🐌 Browser will move slowly - watch each action")

        page.goto("https://playwright.dev")
        page.click("a:has-text('Get started')")

        print("✅ Notice how each action was slowed down")

        browser.close()


def example_custom_viewport():
    """Launch browser with custom window size."""

    print("\n=== Example 4: Custom Viewport ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create page with specific viewport size
        page = browser.new_page(
            viewport={'width': 1920, 'height': 1080}
        )

        page.goto("https://example.com")

        print(f"✅ Browser opened with 1920x1080 viewport")

        time.sleep(2)
        browser.close()


def example_mobile_emulation():
    """Emulate mobile device."""

    print("\n=== Example 5: Mobile Emulation ===")

    with sync_playwright() as p:
        # Get device descriptor for iPhone 12
        iphone_12 = p.devices['iPhone 12']

        browser = p.chromium.launch(headless=False)
        page = browser.new_page(**iphone_12)

        page.goto("https://playwright.dev")

        print(f"✅ Emulating iPhone 12")
        print(f"📱 Viewport: {iphone_12['viewport']}")

        time.sleep(3)
        browser.close()


def example_devtools_open():
    """Launch browser with DevTools open."""

    print("\n=== Example 6: DevTools Open ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            devtools=True  # Opens DevTools automatically
        )
        page = browser.new_page()
        page.goto("https://example.com")

        print("✅ Browser opened with DevTools")

        time.sleep(3)
        browser.close()


def example_different_browsers():
    """Launch different browsers."""

    print("\n=== Example 7: Different Browsers ===")

    with sync_playwright() as p:
        # Chromium
        print("🌐 Launching Chromium...")
        browser1 = p.chromium.launch(headless=False)
        page1 = browser1.new_page()
        page1.goto("https://example.com")
        print(f"  Title: {page1.title()}")

        # Firefox
        print("🦊 Launching Firefox...")
        browser2 = p.firefox.launch(headless=False)
        page2 = browser2.new_page()
        page2.goto("https://example.com")
        print(f"  Title: {page2.title()}")

        # WebKit
        print("🧭 Launching WebKit...")
        browser3 = p.webkit.launch(headless=False)
        page3 = browser3.new_page()
        page3.goto("https://example.com")
        print(f"  Title: {page3.title()}")

        print("✅ All three browsers launched!")

        time.sleep(3)

        # Close all
        browser1.close()
        browser2.close()
        browser3.close()


def main():
    """Run all examples."""

    print("=" * 60)
    print("Playwright Browser Options Examples")
    print("=" * 60)

    # Run each example
    example_headed_mode()
    example_headless_mode()
    example_slow_motion()
    example_custom_viewport()
    example_mobile_emulation()
    example_devtools_open()
    example_different_browsers()

    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
