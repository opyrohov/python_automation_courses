"""Example 3: Handling Multiple iframes on a Page"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Multiple iframes Demo ===\n")

    # Example 1: Counting iframes on page
    print("1. Counting iframes on W3Schools...")
    page.goto("https://www.w3schools.com/html/html_iframe.asp")

    # Count all iframe elements
    iframe_count = page.locator("iframe").count()
    print(f"   ✓ Found {iframe_count} iframes on page")

    # Example 2: Accessing iframes by index
    print("\n2. Accessing iframes by index...")

    if iframe_count > 0:
        # First iframe
        first_iframe = page.frame_locator("iframe").first
        print("   ✓ Accessed first iframe")

        # Last iframe
        last_iframe = page.frame_locator("iframe").last
        print("   ✓ Accessed last iframe")

        # Specific index (if multiple exist)
        if iframe_count > 1:
            second_iframe = page.frame_locator("iframe").nth(1)
            print("   ✓ Accessed second iframe")

    # Example 3: Iterating through all iframes
    print("\n3. Iterating through all iframes...")

    iframes = page.locator("iframe").all()
    for i, iframe in enumerate(iframes):
        src = iframe.get_attribute("src") or "(no src)"
        title = iframe.get_attribute("title") or "(no title)"
        width = iframe.get_attribute("width") or "auto"
        height = iframe.get_attribute("height") or "auto"
        print(f"   iframe {i}: {title[:30]}... | size: {width}x{height}")

    # Example 4: Finding specific iframe by content
    print("\n4. Finding iframe by content...")
    page.goto("https://the-internet.herokuapp.com/iframe")

    # We know we're looking for TinyMCE editor
    # Check if specific content exists in each iframe
    iframes_on_page = page.locator("iframe").all()
    print(f"   Checking {len(iframes_on_page)} iframes for TinyMCE editor...")

    for i in range(len(iframes_on_page)):
        frame = page.frame_locator("iframe").nth(i)
        # Try to find TinyMCE specific element
        tinymce = frame.locator("#tinymce")
        if tinymce.count() > 0:
            print(f"   ✓ Found TinyMCE editor in iframe {i}")
            # Interact with it
            tinymce.fill("Found and filled via iteration!")
            break
    else:
        print("   TinyMCE not found in any iframe")

    # Example 5: Filtering iframes by attribute
    print("\n5. Filtering iframes by attributes...")
    page.goto("https://www.w3schools.com/html/html_iframe.asp")

    # Find iframe with specific attribute pattern
    demo_iframes = page.locator("iframe[src*='default']")
    demo_count = demo_iframes.count()
    print(f"   ✓ Found {demo_count} iframes with 'default' in src")

    # Find iframes with specific dimensions
    sized_iframes = page.locator("iframe[width]")
    sized_count = sized_iframes.count()
    print(f"   ✓ Found {sized_count} iframes with width attribute")

    # Example 6: Working with specific iframe types
    print("\n6. Targeting specific iframe types...")

    # Different ways to target iframes
    selectors = [
        ("iframe[src*='w3schools']", "W3Schools iframes"),
        ("iframe[title]", "iframes with title"),
        ("iframe:not([src=''])", "iframes with non-empty src"),
    ]

    for selector, description in selectors:
        count = page.locator(selector).count()
        print(f"   - {description}: {count}")

    print("\n=== Demo Complete ===")
    browser.close()
