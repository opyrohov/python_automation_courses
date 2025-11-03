"""
Example 1: Your First Playwright Script

This is the simplest Playwright script using the sync API.
It opens a browser, navigates to a website, and prints the title.

Run: python 01_first_script.py
"""

from playwright.sync_api import sync_playwright


def main():
    """Open browser and navigate to Playwright homepage."""

    # Create Playwright instance
    with sync_playwright() as p:
        # Launch browser (headless=False to see the browser window)
        print("🚀 Launching browser...")
        browser = p.chromium.launch(headless=False)

        # Create new page (tab)
        print("📄 Creating new page...")
        page = browser.new_page()

        # Navigate to URL
        url = "https://playwright.dev"
        print(f"🌐 Navigating to {url}...")
        page.goto(url)

        # Get and print page title
        title = page.title()
        print(f"📰 Page title: {title}")

        # Get and print current URL
        current_url = page.url
        print(f"🔗 Current URL: {current_url}")

        # Take a screenshot
        screenshot_path = "playwright_homepage.png"
        page.screenshot(path=screenshot_path)
        print(f"📸 Screenshot saved to: {screenshot_path}")

        # Wait a moment so you can see the browser
        print("⏳ Waiting 3 seconds before closing...")
        page.wait_for_timeout(3000)

        # Close browser
        print("👋 Closing browser...")
        browser.close()

        print("✅ Script completed successfully!")


if __name__ == "__main__":
    main()
