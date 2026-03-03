"""Example 1: Finding Multiple Elements"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Finding Multiple Elements Demo ===\n")

    # Example 1: all() - Get all matching elements
    print("1. Using all() to get all elements...")
    page.goto("https://the-internet.herokuapp.com/")

    # Get all links
    links = page.locator("ul li a").all()
    print(f"   Found {len(links)} links")
    print(f"   First 3 links:")
    for i in range(min(3, len(links))):
        print(f"     - {links[i].text_content()}")

    # Example 2: count() - Get count only
    print("\n2. Using count() to get number of elements...")
    count = page.locator("ul li a").count()
    print(f"   Link count: {count}")
    print(f"   (More efficient than len(all()) when you only need count)")

    # Example 3: first - Get first element
    print("\n3. Using first to get first element...")
    first_link = page.locator("ul li a").first
    print(f"   First link: {first_link.text_content()}")

    # Example 4: last - Get last element
    print("\n4. Using last to get last element...")
    last_link = page.locator("ul li a").last
    print(f"   Last link: {last_link.text_content()}")

    # Example 5: nth() - Get element at specific index
    print("\n5. Using nth() to get element by index...")
    third_link = page.locator("ul li a").nth(2)  # 0-indexed
    print(f"   Third link (index 2): {third_link.text_content()}")

    tenth_link = page.locator("ul li a").nth(9)
    print(f"   Tenth link (index 9): {tenth_link.text_content()}")

    # Example 6: Extracting all text content
    print("\n6. Extracting text from all elements...")
    links = page.locator("ul li a").all()
    texts = [link.text_content() for link in links]
    print(f"   All link texts (first 5):")
    for text in texts[:5]:
        print(f"     - {text}")

    # Example 7: Extracting all attributes
    print("\n7. Extracting attributes from all elements...")
    links = page.locator("ul li a").all()
    hrefs = [link.get_attribute("href") for link in links]
    print(f"   All hrefs (first 5):")
    for href in hrefs[:5]:
        print(f"     - {href}")

    # Example 8: Checking if elements exist
    print("\n8. Checking element existence...")
    items = page.locator(".nonexistent-class").all()
    print(f"   Nonexistent elements: {len(items)} (empty list)")

    if page.locator("ul li a").all():
        print("   ✓ Links exist on page")

    # Example 9: Working with dynamic counts
    print("\n9. Dynamic element counting...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    initial_count = page.locator(".added-manually").count()
    print(f"   Initial elements: {initial_count}")

    # Add 3 elements
    for i in range(3):
        page.locator("button").first.click()

    new_count = page.locator(".added-manually").count()
    print(f"   After adding 3: {new_count}")

    # Example 10: Combining methods
    print("\n10. Combining all(), count(), first, last, nth()...")
    elements = page.locator(".added-manually")

    print(f"   Total count: {elements.count()}")
    print(f"   First element text: {elements.first.text_content()}")
    print(f"   Last element text: {elements.last.text_content()}")
    print(f"   Second element text: {elements.nth(1).text_content()}")

    all_elements = elements.all()
    print(f"   All elements: {len(all_elements)} locators in list")

    print("\n✓ All finding elements examples complete!")

    input("\nPress Enter to close...")
    browser.close()
