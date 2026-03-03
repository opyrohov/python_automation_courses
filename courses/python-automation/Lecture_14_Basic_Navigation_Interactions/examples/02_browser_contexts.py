"""
Example 2: Browser Contexts
Demonstrates creating and working with isolated browser contexts
"""

from playwright.sync_api import sync_playwright
import time


def example_single_context():
    """Basic example with a single context."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("=== Single Context Example ===\n")

        # Create context and page
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://example.com")
        print(f"Page title: {page.title()}")
        print(f"Context has {len(context.pages)} page(s)\n")

        time.sleep(2)

        context.close()
        browser.close()


def example_multiple_contexts():
    """Create multiple isolated contexts (like different users)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Multiple Contexts Example ===\n")

        # Context 1: User A
        print("Creating Context 1 (User A)...")
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://example.com")
        print(f"Context 1 - Page: {page1.title()}\n")

        # Context 2: User B
        print("Creating Context 2 (User B)...")
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://playwright.dev")
        print(f"Context 2 - Page: {page2.title()}\n")

        print("Both contexts are isolated - separate cookies/storage!")

        time.sleep(3)

        # Close contexts
        context1.close()
        context2.close()
        browser.close()


def example_context_with_options():
    """Create context with custom options."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Context with Options Example ===\n")

        # Create context with custom viewport and user agent
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Custom User Agent)',
            locale='en-US',
            timezone_id='America/New_York',
            geolocation={'latitude': 40.7128, 'longitude': -74.0060},
            permissions=['geolocation']
        )

        page = context.new_page()
        page.goto("https://example.com")

        print(f"Viewport size: {page.viewport_size}")
        print(f"Page loaded: {page.title()}\n")

        time.sleep(2)

        context.close()
        browser.close()


def example_mobile_context():
    """Emulate mobile device using context options."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Mobile Emulation Example ===\n")

        # Emulate iPhone 13
        iphone_13 = p.devices['iPhone 13']
        context = browser.new_context(**iphone_13)

        page = context.new_page()
        page.goto("https://example.com")

        print(f"Emulating: iPhone 13")
        print(f"Viewport: {page.viewport_size}")
        print(f"User Agent: {context.user_agent}\n")

        time.sleep(3)

        context.close()
        browser.close()


def example_context_isolation():
    """Demonstrate context isolation with cookies/storage."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Context Isolation Example ===\n")

        # Context 1: Set some storage
        print("Context 1: Setting localStorage...")
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://example.com")

        # Set localStorage in context 1
        page1.evaluate("localStorage.setItem('user', 'Alice')")
        stored_value = page1.evaluate("localStorage.getItem('user')")
        print(f"Context 1 stored: {stored_value}\n")

        # Context 2: Try to read storage (should be isolated)
        print("Context 2: Trying to read localStorage...")
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://example.com")

        stored_value = page2.evaluate("localStorage.getItem('user')")
        print(f"Context 2 reads: {stored_value} (null = isolated!)\n")

        print("Contexts are properly isolated!")

        time.sleep(2)

        context1.close()
        context2.close()
        browser.close()


def example_reusing_context():
    """Create multiple pages within the same context."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Reusing Context Example ===\n")

        # Create one context
        context = browser.new_context()

        # Create multiple pages in same context
        print("Creating 3 pages in same context...")

        page1 = context.new_page()
        page1.goto("https://example.com")
        print(f"Page 1: {page1.title()}")

        page2 = context.new_page()
        page2.goto("https://playwright.dev")
        print(f"Page 2: {page2.title()}")

        page3 = context.new_page()
        page3.goto("https://github.com")
        print(f"Page 3: {page3.title()}")

        print(f"\nTotal pages in context: {len(context.pages)}")
        print("All pages share same context (cookies/storage)!\n")

        time.sleep(3)

        # Closing context closes all pages
        print("Closing context (will close all pages)...")
        context.close()

        browser.close()


if __name__ == "__main__":
    # Run all examples
    example_single_context()
    example_multiple_contexts()
    example_context_with_options()
    example_mobile_context()
    example_context_isolation()
    example_reusing_context()

    print("\n✅ All context examples completed!")
