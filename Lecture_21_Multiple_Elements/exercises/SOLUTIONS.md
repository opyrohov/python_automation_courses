# Exercise Solutions - Lecture 21: Working with Multiple Elements

## Exercise 1: List Operations

```python
from playwright.sync_api import sync_playwright, expect

def list_operations_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # Solution 1: Get all links
        links = page.locator("ul li a").all()
        print(f"Total links: {len(links)}")

        # Solution 2: Get count
        count = page.locator("ul li a").count()
        print(f"Count: {count}")

        # Solution 3: Get first link
        first_link = page.locator("ul li a").first
        print(f"First link: {first_link.text_content()}")

        # Solution 4: Get first 5 link texts
        texts = [link.text_content() for link in page.locator("ul li a").all()[:5]]
        print(f"First 5 link texts: {texts}")

        # Solution 5: Find and click Checkboxes link
        links = page.locator("ul li a").all()
        for link in links:
            if link.text_content() == "Checkboxes":
                link.click()
                break

        # Verify
        expect(page).to_have_url("**/checkboxes")

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 2: Table Data Extraction

```python
from playwright.sync_api import sync_playwright

def table_data_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/tables")

        # Solution 1: Get row count
        row_count = page.locator("#table1 tbody tr").count()
        print(f"Total rows: {row_count}")

        # Solution 2: Extract headers
        headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
        print(f"Headers: {headers}")

        # Solution 3: Get first row data
        first_row = page.locator("#table1 tbody tr").first
        cells = first_row.locator("td").all()
        row_data = [cell.text_content() for cell in cells]
        print(f"First row: {row_data}")

        # Solution 4: Extract entire table
        table_data = []
        for row in page.locator("#table1 tbody tr").all():
            cells = row.locator("td").all()
            row_dict = {headers[i]: cells[i].text_content() for i in range(len(cells))}
            table_data.append(row_dict)
        print(f"Table data (first entry): {table_data[0]}")

        # Solution 5: Find Smith's first name
        smith_row = page.locator("#table1 tbody tr").filter(has_text="Smith")
        first_name = smith_row.locator("td").nth(1).text_content()
        print(f"Smith's first name: {first_name}")

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 3: Dynamic Elements Operations

```python
from playwright.sync_api import sync_playwright, expect

def dynamic_elements_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # Solution 1: Verify initial state
        expect(page.locator(".added-manually")).to_have_count(0)

        # Solution 2: Add 5 elements
        for i in range(5):
            page.locator("button").first.click()

        # Solution 3: Verify 5 elements added
        expect(page.locator(".added-manually")).to_have_count(5)

        # Solution 4: Verify each element is visible
        elements = page.locator(".added-manually").all()
        for element in elements:
            expect(element).to_be_visible()

        # Solution 5: Remove first and last
        page.locator(".added-manually").first.click()
        page.locator(".added-manually").last.click()

        # Solution 6: Verify 3 remain
        expect(page.locator(".added-manually")).to_have_count(3)

        # Solution 7: Remove all remaining
        while page.locator(".added-manually").count() > 0:
            page.locator(".added-manually").first.click()

        # Solution 8: Verify none remain
        expect(page.locator(".added-manually")).to_have_count(0)

        print("✓ Exercise 3 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 4: Filtering and Searching Elements

```python
from playwright.sync_api import sync_playwright

def filtering_search_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # Solution 1: Get all links and count
        all_links = page.locator("ul li a").all()
        print(f"Total links: {len(all_links)}")

        # Solution 2: Find links with "Dynamic"
        dynamic_links = page.locator("ul li a").filter(has_text="Dynamic")
        print(f"Links with 'Dynamic': {dynamic_links.count()}")

        # Solution 3: Extract text from Dynamic links
        texts = [link.text_content() for link in dynamic_links.all()]
        print(f"Dynamic link texts: {texts}")

        # Solution 4: Find links starting with "A"
        a_links = [link for link in all_links if link.text_content().startswith('A')]
        print(f"Links starting with 'A': {len(a_links)}")
        for link in a_links:
            print(f"  - {link.text_content()}")

        # Solution 5: Find and click "Form Authentication"
        for link in all_links:
            if link.text_content() == "Form Authentication":
                link.click()
                break

        # Solution 6: Verify URL
        print(f"Current URL: {page.url}")
        assert "/login" in page.url

        print("✓ Exercise 4 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 5: Advanced Table Operations

```python
from playwright.sync_api import sync_playwright

def table_advanced_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/tables")

        # Solution 1: Extract table as list of dicts
        headers = [h.text_content() for h in page.locator("#table1 thead th").all()]
        rows = page.locator("#table1 tbody tr").all()
        table_data = []
        for row in rows:
            cells = row.locator("td").all()
            row_dict = {headers[i]: cells[i].text_content() for i in range(len(cells))}
            table_data.append(row_dict)
        print(f"Extracted {len(table_data)} rows")

        # Solution 2: Find all Smiths
        smiths = [row for row in table_data if row['Last Name'] == 'Smith']
        print(f"People named Smith: {len(smiths)}")
        for smith in smiths:
            print(f"  - {smith}")

        # Solution 3: Calculate total due
        total_due = 0
        for row in table_data:
            due_amount = float(row['Due'].replace('$', ''))
            total_due += due_amount
        print(f"Total due: ${total_due:.2f}")

        # Solution 4: Find highest due
        max_due_person = max(table_data, key=lambda x: float(x['Due'].replace('$', '')))
        print(f"Highest due: {max_due_person}")

        # Solution 5: Extract Last Name column
        last_names = [row['Last Name'] for row in table_data]
        print(f"All last names: {last_names}")

        # Solution 6: Find Bach's row
        bach_row = page.locator("#table1 tbody tr").filter(has_text="Bach")
        print(f"Found Bach's row")

        # Solution 7: Sort by due amount
        sorted_data = sorted(table_data, key=lambda x: float(x['Due'].replace('$', '')), reverse=True)
        print("Sorted by due amount (highest first):")
        for i, row in enumerate(sorted_data[:3], 1):
            print(f"  {i}. {row}")

        print("✓ Exercise 5 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Key Takeaways

### Finding Multiple Elements
- **all()** - Returns list of Locator objects, use for iteration
- **count()** - Returns number only, more efficient for counting
- **first/last** - Convenience methods for boundary elements
- **nth(i)** - Get element at specific index (0-based)

### Iteration Patterns
```python
# Pattern 1: Using all()
for item in page.locator(".item").all():
    print(item.text_content())

# Pattern 2: Using count() and nth()
for i in range(page.locator(".item").count()):
    item = page.locator(".item").nth(i)
    print(item.text_content())

# Pattern 3: List comprehension
texts = [item.text_content() for item in page.locator(".item").all()]
```

### Table Handling
- Extract headers first for column mapping
- Use dictionaries for structured table data
- Use filter() to find specific rows
- Iterate rows and cells for complete extraction

### Best Practices
- ✅ Use count() when you only need the number
- ✅ Use all() when you need to iterate or access properties
- ✅ Re-query after page changes (don't store stale references)
- ✅ Use filter() for cleaner code
- ✅ Handle empty lists before accessing indices
- ❌ Don't use len(all()) instead of count()
- ❌ Don't store element references across page changes
- ❌ Don't hardcode indices without checking count

### Dynamic Content
```python
# Wait for expected count
expect(page.locator(".item")).to_have_count(10)

# Re-query after changes
page.locator("#add-btn").click()
items = page.locator(".item").all()  # Refresh
```

### Filtering
```python
# By text
items = page.locator(".product").filter(has_text="Laptop")

# By child element
cards = page.locator(".card").filter(has=page.locator("button"))

# Chain filters
results = (page.locator(".product")
    .filter(has_text="Laptop")
    .filter(has=page.locator(".sale")))
```
