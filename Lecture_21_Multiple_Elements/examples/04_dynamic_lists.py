"""Example 4: Dynamic Lists"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Dynamic Lists Demo ===\n")

    # Example 1: Adding elements dynamically
    print("1. Adding elements to dynamic list...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Initial state
    initial_count = page.locator(".added-manually").count()
    print(f"   Initial count: {initial_count}")

    # Add 5 elements
    for i in range(5):
        page.locator("button").first.click()
        current_count = page.locator(".added-manually").count()
        print(f"   After adding {i+1}: {current_count} elements")

    # Verify final count
    expect(page.locator(".added-manually")).to_have_count(5)
    print("   ✓ Successfully added 5 elements")

    # Example 2: Removing elements
    print("\n2. Removing elements from list...")
    elements = page.locator(".added-manually")

    # Remove first element
    elements.first.click()
    print(f"   After removing first: {elements.count()} elements")

    # Remove last element
    elements.last.click()
    print(f"   After removing last: {elements.count()} elements")

    # Example 3: Re-querying after changes
    print("\n3. Demonstrating re-querying after changes...")

    # Get initial list
    items_before = page.locator(".added-manually").all()
    count_before = len(items_before)
    print(f"   Elements before: {count_before}")

    # Add more elements
    page.locator("button").first.click()
    page.locator("button").first.click()

    # Must re-query to get updated list!
    items_after = page.locator(".added-manually").all()
    count_after = len(items_after)
    print(f"   Elements after: {count_after}")
    print(f"   Difference: +{count_after - count_before}")

    # Example 4: Waiting for specific count
    print("\n4. Waiting for specific element count...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Add elements in background (simulate async loading)
    for i in range(3):
        page.locator("button").first.click()

    # Wait for count
    expect(page.locator(".added-manually")).to_have_count(3)
    print("   ✓ Count reached 3")

    # Example 5: Handling empty lists
    print("\n5. Handling empty lists...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    items = page.locator(".added-manually").all()
    if items:
        print(f"   Found {len(items)} items")
    else:
        print("   ✓ No items found (empty list)")

    # Safe way to access first element
    items = page.locator(".added-manually").all()
    if items:
        items[0].click()
    else:
        print("   ✓ Skipped action - no items to click")

    # Example 6: Monitoring list changes
    print("\n6. Monitoring list changes...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    previous_count = 0
    for i in range(5):
        page.locator("button").first.click()
        current_count = page.locator(".added-manually").count()
        added = current_count - previous_count
        print(f"   Iteration {i+1}: Added {added}, Total: {current_count}")
        previous_count = current_count

    # Example 7: Progressive operations
    print("\n7. Progressive operations on list...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Add 10 elements
    for _ in range(10):
        page.locator("button").first.click()

    # Process every other element
    elements = page.locator(".added-manually")
    count = elements.count()
    print(f"   Total elements: {count}")

    # Click every other delete button
    for i in range(0, count, 2):
        if i < elements.count():  # Re-check count
            elements.nth(i).click()
            print(f"   Removed element at index {i}")

    final_count = page.locator(".added-manually").count()
    print(f"   Final count: {final_count}")

    # Example 8: Collecting data during changes
    print("\n8. Collecting data during list changes...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    counts = []
    for i in range(5):
        page.locator("button").first.click()
        count = page.locator(".added-manually").count()
        counts.append(count)

    print(f"   Count history: {counts}")
    print(f"   Total added: {sum(counts)}")

    # Example 9: Verifying list consistency
    print("\n9. Verifying list consistency...")
    elements = page.locator(".added-manually")
    count = elements.count()
    all_elements = elements.all()

    print(f"   count() returned: {count}")
    print(f"   all() returned: {len(all_elements)} elements")
    print(f"   ✓ Consistent: {count == len(all_elements)}")

    # Example 10: Handling rapid changes
    print("\n10. Handling rapid list changes...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Rapid additions
    add_button = page.locator("button").first
    for _ in range(10):
        add_button.click()

    # Wait for final count
    expect(page.locator(".added-manually")).to_have_count(10)
    print("   ✓ All 10 elements added successfully")

    # Rapid deletions
    for _ in range(5):
        page.locator(".added-manually").first.click()

    # Verify final state
    expect(page.locator(".added-manually")).to_have_count(5)
    print("   ✓ 5 elements remain after deletions")

    print("\n✓ All dynamic list examples complete!")

    input("\nPress Enter to close...")
    browser.close()
