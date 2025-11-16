"""Example 4: Count Assertions"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Count Assertions Demo ===\n")

    # Example 1: Basic count assertion
    print("1. Testing to_have_count() - basic usage...")
    page.goto("https://the-internet.herokuapp.com/")

    # Count all list items on homepage
    list_items = page.locator("ul li")
    count = list_items.count()
    expect(list_items).to_have_count(count)
    print(f"   ✓ Found {count} list items on homepage")

    # Example 2: Zero count
    print("\n2. Testing zero count...")
    page.goto("https://the-internet.herokuapp.com/")

    # Should have no error messages
    expect(page.locator(".error-message")).to_have_count(0)
    print("   ✓ No error messages (count = 0)")

    # Example 3: Adding elements dynamically
    print("\n3. Testing count after adding elements...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Initially no elements
    expect(page.locator(".added-manually")).to_have_count(0)
    print("   ✓ Initially 0 elements")

    # Add 3 elements
    for i in range(3):
        page.locator("button").first.click()

    # Should have 3 elements
    expect(page.locator(".added-manually")).to_have_count(3)
    print("   ✓ After adding: 3 elements")

    # Remove one
    page.locator(".added-manually").first.click()

    # Should have 2 elements
    expect(page.locator(".added-manually")).to_have_count(2)
    print("   ✓ After removing: 2 elements")

    # Example 4: Counting table rows
    print("\n4. Testing table row count...")
    page.goto("https://the-internet.herokuapp.com/tables")

    # Count rows in first table (excluding header)
    rows = page.locator("#table1 tbody tr")
    expect(rows).to_have_count(4)
    print("   ✓ Table has 4 data rows")

    # Example 5: Counting specific elements
    print("\n5. Testing count of specific filtered elements...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Count all checkboxes
    checkboxes = page.locator("input[type='checkbox']")
    expect(checkboxes).to_have_count(2)
    print("   ✓ Page has 2 checkboxes")

    # Example 6: Count with timeout
    print("\n6. Testing count with custom timeout...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Initially 1 button
    expect(page.locator("button")).to_have_count(1)

    # Click to load
    page.locator("button").click()

    # Wait for finish element with timeout
    expect(page.locator("#finish")).to_have_count(1, timeout=10000)
    print("   ✓ Finish element appeared (with 10s timeout)")

    # Example 7: Not equal to count
    print("\n7. Testing negative count assertion...")
    page.goto("https://the-internet.herokuapp.com/")

    # Should have more than 0 links
    links = page.locator("ul li a")
    expect(links).not_to_have_count(0)
    print(f"   ✓ Has {links.count()} links (not 0)")

    # Example 8: Verifying list consistency
    print("\n8. Testing list consistency...")
    page.goto("https://the-internet.herokuapp.com/")

    # All list items should have links
    list_items = page.locator("ul li")
    links_in_items = page.locator("ul li a")

    # Count should match
    expect(list_items).to_have_count(links_in_items.count())
    print("   ✓ Each list item has a link")

    # Example 9: Progressive counting
    print("\n9. Testing progressive element addition...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    for i in range(1, 6):
        page.locator("button").first.click()
        expect(page.locator(".added-manually")).to_have_count(i)
        print(f"   ✓ Step {i}: {i} elements")

    print("\n✓ All count assertion examples complete!")

    input("\nPress Enter to close...")
    browser.close()
