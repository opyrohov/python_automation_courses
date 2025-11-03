"""
Example 1: Basic Navigation
Demonstrates goto(), go_back(), go_forward(), and reload() methods
"""

from playwright.sync_api import sync_playwright
import time


def example_basic_navigation():
    """Navigate between pages using basic navigation methods."""
    with sync_playwright() as p:
        # Launch browser in headed mode
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("=== Basic Navigation Example ===\n")

        # 1. Navigate to first page
        print("1. Navigating to example.com...")
        page.goto("https://example.com")
        print(f"   Current URL: {page.url}")
        print(f"   Page Title: {page.title()}\n")
        time.sleep(1)

        # 2. Navigate to second page
        print("2. Navigating to playwright.dev...")
        page.goto("https://playwright.dev")
        print(f"   Current URL: {page.url}")
        print(f"   Page Title: {page.title()}\n")
        time.sleep(1)

        # 3. Go back
        print("3. Going back...")
        page.go_back()
        print(f"   Current URL: {page.url}")
        print(f"   Page Title: {page.title()}\n")
        time.sleep(1)

        # 4. Go forward
        print("4. Going forward...")
        page.go_forward()
        print(f"   Current URL: {page.url}")
        print(f"   Page Title: {page.title()}\n")
        time.sleep(1)

        # 5. Reload page
        print("5. Reloading page...")
        page.reload()
        print(f"   Current URL: {page.url}")
        print(f"   Page Title: {page.title()}\n")

        print("Navigation complete!")
        time.sleep(2)

        browser.close()


def example_navigation_with_options():
    """Navigate with different wait_until options."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Navigation with Options ===\n")

        # Navigate with different wait options
        print("1. Navigating with 'load' (default)...")
        response = page.goto("https://example.com", wait_until="load")
        print(f"   Status: {response.status}")
        print(f"   OK: {response.ok}\n")

        print("2. Navigating with 'domcontentloaded' (faster)...")
        response = page.goto("https://playwright.dev", wait_until="domcontentloaded")
        print(f"   Status: {response.status}\n")

        print("3. Navigating with 'networkidle' (wait for network)...")
        response = page.goto("https://example.com", wait_until="networkidle")
        print(f"   Status: {response.status}\n")

        browser.close()


def example_navigation_with_error_handling():
    """Navigate with proper error handling."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Navigation with Error Handling ===\n")

        # Try to navigate to valid URL
        try:
            print("1. Navigating to valid URL...")
            response = page.goto("https://example.com", timeout=10000)
            print(f"   Success! Status: {response.status}\n")
        except Exception as e:
            print(f"   Error: {e}\n")

        # Try to navigate to invalid URL
        try:
            print("2. Navigating to invalid URL...")
            response = page.goto("https://this-site-does-not-exist-12345.com", timeout=5000)
            print(f"   Success! Status: {response.status}\n")
        except Exception as e:
            print(f"   Error occurred (expected): {type(e).__name__}\n")

        # Try to navigate with very short timeout
        try:
            print("3. Navigating with very short timeout...")
            response = page.goto("https://playwright.dev", timeout=1)
            print(f"   Success! Status: {response.status}\n")
        except Exception as e:
            print(f"   Timeout error (expected): {type(e).__name__}\n")

        browser.close()


if __name__ == "__main__":
    # Run all examples
    example_basic_navigation()
    example_navigation_with_options()
    example_navigation_with_error_handling()

    print("\n✅ All navigation examples completed!")
