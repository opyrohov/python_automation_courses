"""Example 2: Iterating Through Elements"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Iterating Elements Demo ===\n")

    # Example 1: Basic iteration using all()
    print("1. Basic iteration using all()...")
    page.goto("https://the-internet.herokuapp.com/")

    links = page.locator("ul li a").all()
    print(f"   Iterating through {len(links)} links:")
    for i, link in enumerate(links[:5], 1):  # First 5 only
        print(f"     {i}. {link.text_content()}")

    # Example 2: Iteration using count() and nth()
    print("\n2. Iteration using count() and nth()...")
    count = page.locator("ul li a").count()
    print(f"   Iterating through {min(5, count)} links:")
    for i in range(min(5, count)):
        link = page.locator("ul li a").nth(i)
        print(f"     {i}. {link.text_content()}")

    # Example 3: Extract data from all elements
    print("\n3. Extracting data from all elements...")
    links = page.locator("ul li a").all()[:10]

    link_data = []
    for link in links:
        link_data.append({
            'text': link.text_content(),
            'href': link.get_attribute('href')
        })

    print("   Extracted data (first 3):")
    for data in link_data[:3]:
        print(f"     {data['text']} -> {data['href']}")

    # Example 4: List comprehension
    print("\n4. Using list comprehension...")
    links = page.locator("ul li a").all()
    texts = [link.text_content() for link in links]
    print(f"   Extracted {len(texts)} text values (first 5):")
    for text in texts[:5]:
        print(f"     - {text}")

    # Example 5: Filtering while iterating
    print("\n5. Filtering while iterating...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Get all checkboxes
    checkboxes = page.locator("input[type='checkbox']").all()
    print(f"   Total checkboxes: {len(checkboxes)}")

    # Find checked ones
    checked_boxes = [cb for cb in checkboxes if cb.is_checked()]
    print(f"   Checked checkboxes: {len(checked_boxes)}")

    # Example 6: Processing with conditions
    print("\n6. Processing elements with conditions...")
    page.goto("https://the-internet.herokuapp.com/tables")

    # Get all cells from first row
    cells = page.locator("#table1 tbody tr").first.locator("td").all()
    print(f"   First row cells:")
    for i, cell in enumerate(cells):
        text = cell.text_content()
        print(f"     Column {i}: {text}")

    # Example 7: Enumerate for position tracking
    print("\n7. Using enumerate for position tracking...")
    page.goto("https://the-internet.herokuapp.com/")

    for index, link in enumerate(page.locator("ul li a").all()[:5]):
        print(f"   Position {index}: {link.text_content()}")

    # Example 8: Nested iteration (table)
    print("\n8. Nested iteration for table...")
    page.goto("https://the-internet.herokuapp.com/tables")

    rows = page.locator("#table1 tbody tr").all()[:3]  # First 3 rows
    print(f"   Processing {len(rows)} rows:")

    for row_idx, row in enumerate(rows):
        cells = row.locator("td").all()
        row_data = [cell.text_content() for cell in cells]
        print(f"     Row {row_idx}: {', '.join(row_data[:3])}...")  # First 3 cells

    # Example 9: Break and continue in iteration
    print("\n9. Using break and continue...")
    page.goto("https://the-internet.herokuapp.com/")

    links = page.locator("ul li a").all()
    print("   Finding 'Checkboxes' link...")

    for link in links:
        text = link.text_content()
        if text == "Checkboxes":
            print(f"   ✓ Found: {text}")
            break
        elif "Test" in text:
            continue  # Skip test-related links
    else:
        print("   Link not found")

    # Example 10: Collecting specific data
    print("\n10. Collecting specific data...")
    page.goto("https://the-internet.herokuapp.com/tables")

    # Collect all last names from table
    rows = page.locator("#table1 tbody tr").all()
    last_names = []

    for row in rows:
        # Last name is first cell
        last_name = row.locator("td").first.text_content()
        last_names.append(last_name)

    print(f"   Collected last names: {', '.join(last_names)}")

    print("\n✓ All iteration examples complete!")

    input("\nPress Enter to close...")
    browser.close()
