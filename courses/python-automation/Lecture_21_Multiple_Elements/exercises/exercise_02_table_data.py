"""Exercise 2: Table Data Extraction"""
from playwright.sync_api import sync_playwright

def table_data_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/tables")

        # TODO 1: Get the count of rows in table #table1
        # Hint: row_count = page.locator("#table1 tbody tr").count()
        # row_count = page.YOUR_CODE_HERE
        # print(f"Total rows: {row_count}")

        # TODO 2: Extract all headers from the table
        # Hint: headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
        # headers = YOUR_CODE_HERE
        # print(f"Headers: {headers}")

        # TODO 3: Get the first row and extract all cell values
        # Hint: first_row = page.locator("#table1 tbody tr").first
        #       cells = first_row.locator("td").all()
        #       row_data = [cell.text_content() for cell in cells]
        # first_row = page.YOUR_CODE_HERE
        # cells = YOUR_CODE_HERE
        # row_data = YOUR_CODE_HERE
        # print(f"First row: {row_data}")

        # TODO 4: Extract the entire table as a list of dictionaries
        # Hint: Use headers from TODO 2 and iterate through all rows
        # table_data = []
        # for row in page.YOUR_CODE_HERE:
        #     cells = YOUR_CODE_HERE
        #     row_dict = {headers[i]: cells[i].text_content() for i in range(len(cells))}
        #     table_data.append(row_dict)
        # print(f"Table data (first entry): {table_data[0]}")

        # TODO 5: Find the row containing "Smith" and print the first name
        # Hint: Use filter() or iterate through rows checking text_content()
        # smith_row = page.YOUR_CODE_HERE
        # first_name = YOUR_CODE_HERE
        # print(f"Smith's first name: {first_name}")

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    table_data_exercise()
