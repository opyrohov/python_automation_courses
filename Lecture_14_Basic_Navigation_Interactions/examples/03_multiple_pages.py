"""
Example 3: Multiple Pages (Tabs)
Demonstrates working with multiple pages/tabs in a browser
"""

from playwright.sync_api import sync_playwright
import time


def example_creating_multiple_pages():
    """Create and work with multiple pages."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()

        print("=== Creating Multiple Pages Example ===\n")

        # Create first page
        print("Creating page 1...")
        page1 = context.new_page()
        page1.goto("https://example.com")
        print(f"Page 1: {page1.title()}\n")
        time.sleep(1)

        # Create second page
        print("Creating page 2...")
        page2 = context.new_page()
        page2.goto("https://playwright.dev")
        print(f"Page 2: {page2.title()}\n")
        time.sleep(1)

        # Create third page
        print("Creating page 3...")
        page3 = context.new_page()
        page3.goto("https://github.com")
        print(f"Page 3: {page3.title()}\n")

        print(f"Total pages: {len(context.pages)}")

        time.sleep(2)

        browser.close()


def example_iterating_pages():
    """Iterate through all pages in a context."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        print("\n=== Iterating Through Pages Example ===\n")

        # Create multiple pages
        urls = [
            "https://example.com",
            "https://playwright.dev",
            "https://github.com"
        ]

        for url in urls:
            page = context.new_page()
            page.goto(url)

        # Iterate through all pages
        print(f"Total pages created: {len(context.pages)}\n")

        for i, page in enumerate(context.pages, 1):
            print(f"Page {i}:")
            print(f"  URL: {page.url}")
            print(f"  Title: {page.title()}\n")

        time.sleep(2)

        browser.close()


def example_switching_between_pages():
    """Switch between different pages."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()

        print("\n=== Switching Between Pages Example ===\n")

        # Create pages
        page1 = context.new_page()
        page1.goto("https://example.com")

        page2 = context.new_page()
        page2.goto("https://playwright.dev")

        page3 = context.new_page()
        page3.goto("https://github.com")

        # Switch focus between pages
        print("Switching to page 1...")
        page1.bring_to_front()
        print(f"Current: {page1.title()}\n")
        time.sleep(1)

        print("Switching to page 2...")
        page2.bring_to_front()
        print(f"Current: {page2.title()}\n")
        time.sleep(1)

        print("Switching to page 3...")
        page3.bring_to_front()
        print(f"Current: {page3.title()}\n")
        time.sleep(1)

        browser.close()


def example_closing_specific_pages():
    """Close specific pages while keeping others open."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()

        print("\n=== Closing Specific Pages Example ===\n")

        # Create pages
        page1 = context.new_page()
        page1.goto("https://example.com")

        page2 = context.new_page()
        page2.goto("https://playwright.dev")

        page3 = context.new_page()
        page3.goto("https://github.com")

        print(f"Total pages: {len(context.pages)}\n")

        # Close page 2
        print("Closing page 2...")
        page2.close()
        print(f"Total pages: {len(context.pages)}\n")
        time.sleep(1)

        # Close page 1
        print("Closing page 1...")
        page1.close()
        print(f"Total pages: {len(context.pages)}\n")
        time.sleep(1)

        # Only page 3 remains
        print(f"Remaining page: {page3.title()}")

        time.sleep(2)

        browser.close()


def example_new_tab_simulation():
    """Simulate opening links in new tabs."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()

        print("\n=== New Tab Simulation Example ===\n")

        # Create main page
        main_page = context.new_page()
        main_page.goto("https://example.com")
        print(f"Main page: {main_page.title()}\n")

        # Simulate opening link in new tab
        print("Opening link in new tab...")
        new_tab = context.new_page()
        new_tab.goto("https://playwright.dev")
        print(f"New tab: {new_tab.title()}\n")

        # Switch back to main page
        print("Switching back to main page...")
        main_page.bring_to_front()
        time.sleep(1)

        # Switch to new tab again
        print("Switching to new tab...")
        new_tab.bring_to_front()
        time.sleep(1)

        browser.close()


def example_managing_page_lifecycle():
    """Complete lifecycle of managing multiple pages."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        print("\n=== Page Lifecycle Management Example ===\n")

        pages = []

        # Create and track pages
        print("Creating 3 pages...")
        for i in range(1, 4):
            page = context.new_page()
            page.goto(f"https://example.com")
            pages.append(page)
            print(f"Created page {i}")

        print(f"\nTotal pages: {len(context.pages)}\n")

        # Do work with each page
        print("Processing pages...")
        for i, page in enumerate(pages, 1):
            print(f"Processing page {i}: {page.title()}")
            # Do something with the page
            time.sleep(0.5)

        print()

        # Close all pages
        print("Closing all pages...")
        for i, page in enumerate(pages, 1):
            page.close()
            print(f"Closed page {i}")
            print(f"Remaining pages: {len(context.pages)}")

        print("\nAll pages closed!")

        time.sleep(1)

        browser.close()


def example_page_events():
    """Listen to page events."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        print("\n=== Page Events Example ===\n")

        # Listen for new pages
        def handle_page(page):
            print(f"New page created: {page.url}")
            page.on("load", lambda: print(f"Page loaded: {page.url}"))

        context.on("page", handle_page)

        # Create pages
        print("Creating pages (events will be logged)...\n")

        page1 = context.new_page()
        page1.goto("https://example.com")
        time.sleep(1)

        page2 = context.new_page()
        page2.goto("https://playwright.dev")
        time.sleep(1)

        print(f"\nTotal pages: {len(context.pages)}")

        time.sleep(2)

        browser.close()


if __name__ == "__main__":
    # Run all examples
    example_creating_multiple_pages()
    example_iterating_pages()
    example_switching_between_pages()
    example_closing_specific_pages()
    example_new_tab_simulation()
    example_managing_page_lifecycle()
    example_page_events()

    print("\n✅ All multiple pages examples completed!")
