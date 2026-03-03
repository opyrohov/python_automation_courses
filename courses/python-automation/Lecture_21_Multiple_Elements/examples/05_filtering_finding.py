"""Example 5: Filtering and Finding Elements"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Filtering and Finding Demo ===\n")

    # Example 1: Filter by text content
    print("1. Filtering by text content...")
    page.goto("https://the-internet.herokuapp.com/")

    # Find links containing "Dynamic"
    dynamic_links = page.locator("ul li a").filter(has_text="Dynamic")
    count = dynamic_links.count()
    print(f"   Found {count} links containing 'Dynamic'")

    for link in dynamic_links.all():
        print(f"     - {link.text_content()}")

    # Example 2: Filter by child element
    print("\n2. Filtering by child element...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Find form that has checkboxes
    form_with_checkboxes = page.locator("form").filter(
        has=page.locator("input[type='checkbox']")
    )
    print(f"   Found form with checkboxes: {form_with_checkboxes.count()}")

    # Example 3: Chain filters
    print("\n3. Chaining filters...")
    page.goto("https://the-internet.herokuapp.com/")

    # Find links about forms
    form_links = (
        page.locator("ul li a")
        .filter(has_text="Form")
    )
    print(f"   Links about forms: {form_links.count()}")
    for link in form_links.all():
        print(f"     - {link.text_content()}")

    # Example 4: Find first matching element
    print("\n4. Finding first matching element...")
    page.goto("https://the-internet.herokuapp.com/")

    # Find first link containing "Add"
    first_add_link = page.locator("ul li a").filter(has_text="Add").first
    print(f"   First 'Add' link: {first_add_link.text_content()}")

    # Example 5: Find by attribute value
    print("\n5. Finding by attribute value...")
    page.goto("https://the-internet.herokuapp.com/")

    links = page.locator("ul li a").all()
    # Find links with specific href
    checkboxes_link = None
    for link in links:
        if link.get_attribute("href") == "/checkboxes":
            checkboxes_link = link
            break

    if checkboxes_link:
        print(f"   Found link: {checkboxes_link.text_content()}")

    # Example 6: Custom filtering logic
    print("\n6. Custom filtering with list comprehension...")
    page.goto("https://the-internet.herokuapp.com/")

    all_links = page.locator("ul li a").all()

    # Find short links (text length < 15)
    short_links = [
        link for link in all_links
        if len(link.text_content()) < 15
    ]
    print(f"   Found {len(short_links)} short links (first 5):")
    for link in short_links[:5]:
        print(f"     - {link.text_content()}")

    # Example 7: Find elements meeting multiple criteria
    print("\n7. Finding with multiple criteria...")
    page.goto("https://the-internet.herokuapp.com/tables")

    rows = page.locator("#table1 tbody tr").all()

    # Find rows where due amount > $50
    high_due_rows = []
    for row in rows:
        due_cell = row.locator("td").nth(3)
        due_amount = float(due_cell.text_content().replace("$", ""))
        if due_amount > 50:
            high_due_rows.append(row)

    print(f"   Rows with due > $50: {len(high_due_rows)}")
    for row in high_due_rows:
        cells = row.locator("td").all()
        print(f"     {cells[1].text_content()} {cells[0].text_content()}: ${cells[3].text_content()}")

    # Example 8: Find using lambda
    print("\n8. Finding using lambda function...")
    page.goto("https://the-internet.herokuapp.com/")

    links = page.locator("ul li a").all()

    # Find links starting with 'A'
    a_links = list(filter(lambda link: link.text_content().startswith('A'), links))
    print(f"   Links starting with 'A': {len(a_links)}")
    for link in a_links[:3]:
        print(f"     - {link.text_content()}")

    # Example 9: Find and click specific element
    print("\n9. Finding and clicking specific element...")
    page.goto("https://the-internet.herokuapp.com/")

    # Find and click "Checkboxes" link
    links = page.locator("ul li a").all()
    for link in links:
        if link.text_content() == "Checkboxes":
            print(f"   Found and clicking: {link.text_content()}")
            link.click()
            break

    # Verify navigation
    print(f"   Current URL: {page.url}")

    # Example 10: Filter table rows
    print("\n10. Filtering table rows...")
    page.goto("https://the-internet.herokuapp.com/tables")

    # Using built-in filter
    smith_rows = page.locator("#table1 tbody tr").filter(has_text="Smith")
    print(f"   Rows with 'Smith': {smith_rows.count()}")

    for row in smith_rows.all():
        cells = row.locator("td").all()
        print(f"     {cells[1].text_content()} {cells[0].text_content()}")

    # Example 11: Find element by position and content
    print("\n11. Finding by position and content...")
    page.goto("https://the-internet.herokuapp.com/")

    # Get links 5-10
    all_links = page.locator("ul li a").all()
    links_slice = all_links[4:10]  # indices 4-9

    print(f"   Links 5-10:")
    for i, link in enumerate(links_slice, 5):
        print(f"     {i}. {link.text_content()}")

    # Example 12: Complex search scenario
    print("\n12. Complex search scenario...")
    page.goto("https://the-internet.herokuapp.com/tables")

    # Find person with highest due amount
    rows = page.locator("#table1 tbody tr").all()

    max_due = 0
    max_due_person = None

    for row in rows:
        cells = row.locator("td").all()
        due = float(cells[3].text_content().replace("$", ""))

        if due > max_due:
            max_due = due
            max_due_person = {
                'first_name': cells[1].text_content(),
                'last_name': cells[0].text_content(),
                'due': due
            }

    if max_due_person:
        print(f"   Highest due amount:")
        print(f"     {max_due_person['first_name']} {max_due_person['last_name']}: ${max_due_person['due']}")

    print("\n✓ All filtering and finding examples complete!")

    input("\nPress Enter to close...")
    browser.close()
