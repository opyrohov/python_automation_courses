"""Example 3: Table Handling"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Table Handling Demo ===\n")

    page.goto("https://the-internet.herokuapp.com/tables")

    # Example 1: Count rows and columns
    print("1. Counting table rows and columns...")
    row_count = page.locator("#table1 tbody tr").count()
    header_count = page.locator("#table1 thead th").count()
    print(f"   Table has {row_count} data rows")
    print(f"   Table has {header_count} columns")

    # Example 2: Get all headers
    print("\n2. Extracting table headers...")
    headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
    print(f"   Headers: {headers}")

    # Example 3: Get specific cell
    print("\n3. Getting specific cell (row 1, column 2)...")
    cell = page.locator("#table1 tbody tr").first.locator("td").nth(1)
    print(f"   Cell value: {cell.text_content()}")

    # Example 4: Get entire row
    print("\n4. Getting entire first row...")
    first_row = page.locator("#table1 tbody tr").first
    cells = first_row.locator("td").all()
    row_data = [cell.text_content() for cell in cells]
    print(f"   First row: {row_data}")

    # Example 5: Extract entire table as list of lists
    print("\n5. Extracting entire table as list of lists...")
    rows = page.locator("#table1 tbody tr").all()
    table_data = []

    for row in rows:
        cells = row.locator("td").all()
        row_data = [cell.text_content() for cell in cells]
        table_data.append(row_data)

    print(f"   Extracted {len(table_data)} rows")
    print(f"   First row: {table_data[0]}")
    print(f"   Second row: {table_data[1]}")

    # Example 6: Extract table as list of dictionaries
    print("\n6. Extracting table as list of dictionaries...")
    headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
    rows = page.locator("#table1 tbody tr").all()

    table_dict = []
    for row in rows:
        cells = row.locator("td").all()
        row_dict = {
            headers[i]: cells[i].text_content()
            for i in range(len(cells))
        }
        table_dict.append(row_dict)

    print(f"   Extracted {len(table_dict)} row dictionaries")
    print(f"   First row: {table_dict[0]}")

    # Example 7: Find row by content
    print("\n7. Finding row containing 'Smith'...")
    rows = page.locator("#table1 tbody tr").all()

    for row_idx, row in enumerate(rows):
        if "Smith" in row.text_content():
            cells = row.locator("td").all()
            print(f"   Found at row {row_idx}:")
            print(f"   Last Name: {cells[0].text_content()}")
            print(f"   First Name: {cells[1].text_content()}")
            break

    # Example 8: Find row by specific cell value
    print("\n8. Finding row where first name is 'John'...")
    rows = page.locator("#table1 tbody tr").all()

    for row in rows:
        cells = row.locator("td").all()
        if cells[1].text_content() == "John":  # First name column
            print(f"   Found John:")
            print(f"   Last Name: {cells[0].text_content()}")
            print(f"   Due: ${cells[3].text_content()}")

    # Example 9: Extract specific column
    print("\n9. Extracting 'Last Name' column...")
    rows = page.locator("#table1 tbody tr").all()
    last_names = [row.locator("td").first.text_content() for row in rows]
    print(f"   Last names: {last_names}")

    # Example 10: Find and interact with table row
    print("\n10. Finding and clicking action in table row...")

    # Use filter to find row
    smith_row = page.locator("#table1 tbody tr").filter(has_text="Smith")
    print(f"   Found row with 'Smith'")

    # Get data from that row
    cells = smith_row.locator("td").all()
    print(f"   Data: {cells[0].text_content()} {cells[1].text_content()}")

    # Could click button/link in this row
    # smith_row.locator("a.edit").click()

    # Example 11: Sort table data
    print("\n11. Extracting and sorting table data...")
    rows = page.locator("#table1 tbody tr").all()

    # Extract with due amount
    data_with_due = []
    for row in rows:
        cells = row.locator("td").all()
        data_with_due.append({
            'name': f"{cells[1].text_content()} {cells[0].text_content()}",
            'due': float(cells[3].text_content().replace('$', ''))
        })

    # Sort by due amount
    sorted_data = sorted(data_with_due, key=lambda x: x['due'], reverse=True)
    print("   Sorted by due amount (highest first):")
    for item in sorted_data[:3]:
        print(f"     {item['name']}: ${item['due']}")

    # Example 12: Table statistics
    print("\n12. Calculating table statistics...")
    rows = page.locator("#table1 tbody tr").all()

    total_due = 0
    for row in rows:
        due_cell = row.locator("td").nth(3)  # Due column
        amount = float(due_cell.text_content().replace('$', ''))
        total_due += amount

    average_due = total_due / len(rows)
    print(f"   Total due: ${total_due:.2f}")
    print(f"   Average due: ${average_due:.2f}")

    print("\n✓ All table handling examples complete!")

    input("\nPress Enter to close...")
    browser.close()
