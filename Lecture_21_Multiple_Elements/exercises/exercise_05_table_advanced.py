"""Exercise 5: Advanced Table Operations"""
from playwright.sync_api import sync_playwright

def table_advanced_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/tables")

        # TODO 1: Extract all data from table #table1 as list of dictionaries
        # Hint: 1. Get headers: headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
        #       2. Get rows: rows = page.locator("#table1 tbody tr").all()
        #       3. Build dict for each row using headers as keys
        # headers = YOUR_CODE_HERE
        # rows = YOUR_CODE_HERE
        # table_data = []
        # for row in rows:
        #     cells = YOUR_CODE_HERE
        #     row_dict = YOUR_CODE_HERE
        #     table_data.append(row_dict)
        # print(f"Extracted {len(table_data)} rows")

        # TODO 2: Find all people with last name "Smith"
        # Hint: Use list comprehension to filter table_data
        # smiths = [row for row in table_data if YOUR_CONDITION_HERE]
        # print(f"People named Smith: {len(smiths)}")
        # for smith in smiths:
        #     print(f"  - {smith}")

        # TODO 3: Calculate total "Due" amount from all rows
        # Hint: Extract "Due" column, remove "$", convert to float, sum
        # total_due = 0
        # for row in table_data:
        #     due_amount = YOUR_CODE_HERE  # Get "Due", remove "$", convert to float
        #     total_due += due_amount
        # print(f"Total due: ${total_due:.2f}")

        # TODO 4: Find the person with the highest due amount
        # Hint: Use max() with key parameter
        # max_due_person = max(table_data, key=lambda x: YOUR_CODE_HERE)
        # print(f"Highest due: {max_due_person}")

        # TODO 5: Extract just the "Last Name" column as a list
        # Hint: Use list comprehension to get "Last Name" from each row
        # last_names = YOUR_CODE_HERE
        # print(f"All last names: {last_names}")

        # TODO 6: Find and click a row containing "Bach" using filter()
        # Hint: bach_row = page.locator("#table1 tbody tr").filter(has_text="Bach")
        # bach_row = page.YOUR_CODE_HERE
        # print(f"Found Bach's row")
        # # Could interact with row here: bach_row.locator("a.edit").click()

        # TODO 7: Sort table data by "Due" amount (highest first)
        # Hint: Use sorted() with key parameter
        # sorted_data = sorted(table_data, key=lambda x: YOUR_CODE_HERE, reverse=True)
        # print("Sorted by due amount (highest first):")
        # for i, row in enumerate(sorted_data[:3], 1):  # Top 3
        #     print(f"  {i}. {row}")

        print("✓ Exercise 5 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    table_advanced_exercise()
