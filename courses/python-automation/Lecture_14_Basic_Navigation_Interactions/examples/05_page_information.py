"""
Example 5: Getting Page Information
Demonstrates extracting information from pages: title, URL, content
"""

from playwright.sync_api import sync_playwright
import time


def example_basic_page_info():
    """Get basic information from a page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("=== Basic Page Information Example ===\n")

        # Navigate to page
        page.goto("https://example.com")

        # Get page title
        title = page.title()
        print(f"Page Title: {title}")

        # Get current URL
        url = page.url
        print(f"Current URL: {url}")

        # Get page content (HTML)
        html = page.content()
        print(f"HTML Length: {len(html)} characters")
        print(f"HTML Preview: {html[:100]}...\n")

        time.sleep(2)

        browser.close()


def example_page_info_across_navigation():
    """Track page information across navigation."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== Page Info Across Navigation Example ===\n")

        urls = [
            "https://example.com",
            "https://playwright.dev",
            "https://github.com"
        ]

        for i, url in enumerate(urls, 1):
            print(f"Navigation {i}:")
            page.goto(url)

            print(f"  URL: {page.url}")
            print(f"  Title: {page.title()}")
            print(f"  Content size: {len(page.content())} chars\n")

            time.sleep(1)

        browser.close()


def example_response_information():
    """Get response information from navigation."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Response Information Example ===\n")

        # Navigate and get response
        response = page.goto("https://example.com")

        print(f"URL: {response.url}")
        print(f"Status Code: {response.status}")
        print(f"Status Text: {response.status_text}")
        print(f"OK (2xx): {response.ok}")
        print(f"Headers: {dict(list(response.headers.items())[:5])}...")  # First 5 headers

        time.sleep(2)

        browser.close()


def example_viewport_information():
    """Get viewport and window information."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        print("\n=== Viewport Information Example ===\n")

        # Create page with specific viewport
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto("https://example.com")

        # Get viewport size
        viewport = page.viewport_size
        print(f"Viewport Size: {viewport}")
        print(f"Width: {viewport['width']}px")
        print(f"Height: {viewport['height']}px")

        time.sleep(2)

        browser.close()


def example_extracting_page_content():
    """Extract and analyze page content."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Extracting Page Content Example ===\n")

        page.goto("https://example.com")

        # Get full HTML
        html = page.content()
        print(f"Full HTML length: {len(html)} chars")

        # Check for specific content
        if "Example Domain" in html:
            print("✓ Found 'Example Domain' in HTML")

        if "illustrative examples" in html:
            print("✓ Found 'illustrative examples' in HTML")

        # Get page text content
        body_text = page.locator("body").inner_text()
        print(f"\nPage Text Content:\n{body_text}\n")

        time.sleep(2)

        browser.close()


def example_page_info_utility():
    """Create a utility function to get comprehensive page info."""
    def get_comprehensive_page_info(page):
        """Get all available information about a page."""
        return {
            'url': page.url,
            'title': page.title(),
            'content_length': len(page.content()),
            'viewport': page.viewport_size
        }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Comprehensive Page Info Utility Example ===\n")

        # Test with multiple pages
        test_urls = [
            "https://example.com",
            "https://playwright.dev"
        ]

        for url in test_urls:
            page.goto(url)
            info = get_comprehensive_page_info(page)

            print(f"Page: {url}")
            print(f"  Title: {info['title']}")
            print(f"  URL: {info['url']}")
            print(f"  Content: {info['content_length']} chars")
            print(f"  Viewport: {info['viewport']}\n")

            time.sleep(1)

        browser.close()


def example_saving_page_info():
    """Save page information to file."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Saving Page Info Example ===\n")

        page.goto("https://example.com")

        # Save HTML to file
        html_filename = "page_content.html"
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(page.content())
        print(f"✓ HTML saved to {html_filename}")

        # Save page info to text file
        info_filename = "page_info.txt"
        with open(info_filename, "w", encoding="utf-8") as f:
            f.write(f"Page Title: {page.title()}\n")
            f.write(f"URL: {page.url}\n")
            f.write(f"Content Length: {len(page.content())} chars\n")
            f.write(f"Viewport: {page.viewport_size}\n")
        print(f"✓ Page info saved to {info_filename}")

        print("\nFiles created successfully!")

        time.sleep(2)

        browser.close()


def example_page_info_comparison():
    """Compare page information before and after actions."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== Page Info Comparison Example ===\n")

        # Get info before
        page.goto("https://example.com")
        title_before = page.title()
        url_before = page.url
        content_before = len(page.content())

        print("BEFORE NAVIGATION:")
        print(f"  Title: {title_before}")
        print(f"  URL: {url_before}")
        print(f"  Content: {content_before} chars\n")

        time.sleep(1)

        # Navigate to different page
        page.goto("https://playwright.dev")

        # Get info after
        title_after = page.title()
        url_after = page.url
        content_after = len(page.content())

        print("AFTER NAVIGATION:")
        print(f"  Title: {title_after}")
        print(f"  URL: {url_after}")
        print(f"  Content: {content_after} chars\n")

        # Compare
        print("COMPARISON:")
        print(f"  Title changed: {title_before != title_after}")
        print(f"  URL changed: {url_before != url_after}")
        print(f"  Content changed: {content_before != content_after}")

        time.sleep(2)

        browser.close()


if __name__ == "__main__":
    # Run all examples
    example_basic_page_info()
    example_page_info_across_navigation()
    example_response_information()
    example_viewport_information()
    example_extracting_page_content()
    example_page_info_utility()
    example_saving_page_info()
    example_page_info_comparison()

    print("\n✅ All page information examples completed!")
