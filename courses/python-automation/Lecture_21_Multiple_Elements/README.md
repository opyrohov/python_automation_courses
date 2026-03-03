# Lecture 21: Working with Multiple Elements

## Overview
Master working with collections of elements - lists, tables, search results, and dynamic content.

## Quick Reference

### Getting Multiple Elements
```python
# Get all matching elements (returns list)
items = page.locator(".item").all()

# Get count only (more efficient)
count = page.locator(".item").count()

# Get specific element by index
first = page.locator(".item").first
last = page.locator(".item").last
third = page.locator(".item").nth(2)
```

### Iterating Elements
```python
# Method 1: Using all()
items = page.locator(".product").all()
for item in items:
    print(item.text_content())

# Method 2: Using count() and nth()
count = page.locator(".product").count()
for i in range(count):
    item = page.locator(".product").nth(i)
    print(item.text_content())

# Method 3: Enumerate
for i, item in enumerate(page.locator(".product").all()):
    print(f"{i}: {item.text_content()}")
```

### Extracting Data
```python
# Extract text from all elements
products = page.locator(".product-name").all()
names = [p.text_content() for p in products]

# Extract attributes
links = page.locator("a").all()
urls = [link.get_attribute("href") for link in links]

# Extract complex data
items = page.locator(".product").all()
data = [{
    'name': item.locator(".name").text_content(),
    'price': item.locator(".price").text_content()
} for item in items]
```

### Working with Tables
```python
# Get all rows
rows = page.locator("table tbody tr").all()

# Get cells in first row
cells = page.locator("table tbody tr").first.locator("td").all()

# Extract entire table
table_data = []
for row in page.locator("table tbody tr").all():
    cells = row.locator("td").all()
    row_data = [cell.text_content() for cell in cells]
    table_data.append(row_data)

# Find row by content
row = page.locator("table tbody tr").filter(has_text="John")
```

### Filtering Elements
```python
# Filter by text
laptops = page.locator(".product").filter(has_text="Laptop")

# Filter by child element
cards_with_button = page.locator(".card").filter(
    has=page.locator("button")
)

# Chain filters
results = (page.locator(".product")
    .filter(has_text="Laptop")
    .filter(has=page.locator(".sale-badge")))
```

## Key Methods

### all()
- Returns: `List[Locator]`
- Use when: You need to iterate or access individual elements
- Note: Evaluates immediately, returns snapshot

```python
items = page.locator(".item").all()  # List of Locator objects
print(len(items))
```

### count()
- Returns: `int`
- Use when: You only need the count
- More efficient than `len(all())`

```python
count = page.locator(".item").count()  # Just the number
```

### nth(index)
- Returns: `Locator`
- Get element at specific position (0-indexed)

```python
third_item = page.locator(".item").nth(2)
```

### first / last
- Returns: `Locator`
- Convenience methods for first/last element

```python
first = page.locator(".item").first
last = page.locator(".item").last
```

## Common Patterns

### Pattern 1: Validate List Contents
```python
# Verify all products shown
products = page.locator(".product").all()
assert len(products) == 12, f"Expected 12 products, got {len(products)}"

# Verify all contain specific text
for product in products:
    assert product.is_visible(), "Product not visible"
```

### Pattern 2: Extract and Process Data
```python
# Get all product data
products = page.locator(".product").all()
data = []

for product in products:
    data.append({
        'name': product.locator(".name").text_content(),
        'price': float(product.locator(".price").text_content().replace("$", "")),
        'rating': product.locator(".rating").get_attribute("data-rating")
    })

# Find expensive products
expensive = [p for p in data if p['price'] > 100]
```

### Pattern 3: Table Data Extraction
```python
# Extract table with headers
headers = [h.text_content() for h in page.locator("table th").all()]
rows = page.locator("table tbody tr").all()

table_data = []
for row in rows:
    cells = row.locator("td").all()
    row_dict = {headers[i]: cells[i].text_content() for i in range(len(cells))}
    table_data.append(row_dict)

# Result: [{'Name': 'John', 'Age': '30'}, ...]
```

### Pattern 4: Dynamic Content
```python
from playwright.sync_api import expect

# Wait for specific count
expect(page.locator(".result")).to_have_count(10)

# Handle adding items
initial_count = page.locator(".item").count()
page.locator("#add-btn").click()
expect(page.locator(".item")).to_have_count(initial_count + 1)

# Get new item
new_item = page.locator(".item").last
```

### Pattern 5: Finding Specific Element
```python
# Find by text content
items = page.locator(".item").all()
for item in items:
    if "Laptop" in item.text_content():
        item.click()
        break

# Find by attribute
for item in items:
    if item.get_attribute("data-id") == "123":
        item.click()
        break

# Using filter (better)
item = page.locator(".item").filter(has_text="Laptop").first
item.click()
```

### Pattern 6: Verify Sorting
```python
# Extract values
items = page.locator(".product").all()
prices = [
    float(item.locator(".price").text_content().replace("$", ""))
    for item in items
]

# Check if sorted
is_sorted = all(prices[i] <= prices[i+1] for i in range(len(prices)-1))
assert is_sorted, "Products not sorted correctly"
```

## Working with Tables

### Basic Table Operations
```python
# Count rows
row_count = page.locator("table tbody tr").count()

# Get specific cell (row 2, column 3)
cell = page.locator("table tbody tr").nth(1).locator("td").nth(2)

# Get all data in column
column_data = [
    row.locator("td").first.text_content()
    for row in page.locator("table tbody tr").all()
]
```

### Finding Rows
```python
# Find row containing text
row = page.locator("table tbody tr").filter(has_text="John")

# Find row by cell value
rows = page.locator("table tbody tr").all()
for row in rows:
    first_cell = row.locator("td").first
    if first_cell.text_content() == "John":
        # Found it!
        row.locator("button").click()
        break
```

### Table to Data Structure
```python
def extract_table(page, selector="table"):
    """Extract table as list of dictionaries"""
    # Get headers
    headers = [
        h.text_content().strip()
        for h in page.locator(f"{selector} th").all()
    ]

    # Get rows
    rows = page.locator(f"{selector} tbody tr").all()

    # Build data
    data = []
    for row in rows:
        cells = row.locator("td").all()
        row_data = {
            headers[i]: cells[i].text_content().strip()
            for i in range(len(cells))
        }
        data.append(row_data)

    return data

# Usage
table_data = extract_table(page)
```

## Best Practices

### ✅ DO
- Use `count()` instead of `len(all())` for efficiency
- Re-query elements after page changes
- Use `filter()` for cleaner, more readable code
- Wait for expected count before processing
- Handle empty lists gracefully
- Extract data to variables for processing

### ❌ DON'T
- Store element references long-term (they become stale)
- Assume specific element order unless explicitly sorted
- Use `all()` when you only need the count
- Forget to check if list is empty before accessing
- Hardcode element indices
- Iterate without verifying count first

## Common Pitfalls

### Stale Element References
```python
# ❌ BAD - elements become stale
items = page.locator(".item").all()
page.locator("#refresh").click()
items[0].click()  # May fail - stale reference!

# ✅ GOOD - re-query after page changes
page.locator("#refresh").click()
items = page.locator(".item").all()
items[0].click()
```

### Empty List Handling
```python
# ❌ BAD - IndexError if no items
items = page.locator(".item").all()
items[0].click()

# ✅ GOOD - check first
items = page.locator(".item").all()
if items:
    items[0].click()
else:
    print("No items found")
```

### Using all() vs count()
```python
# ❌ INEFFICIENT - loads all elements just to count
if len(page.locator(".item").all()) > 10:
    print("Many items")

# ✅ EFFICIENT - just gets the count
if page.locator(".item").count() > 10:
    print("Many items")
```

## Examples

| File | Description |
|------|-------------|
| `01_finding_elements.py` | all(), count(), nth(), first, last |
| `02_iterating_elements.py` | Different iteration patterns |
| `03_table_handling.py` | Working with table data |
| `04_dynamic_lists.py` | Dynamic content handling |
| `05_filtering_finding.py` | Filter and find specific elements |

## Exercises

| Exercise | Topic | Difficulty |
|----------|-------|------------|
| `exercise_01_list_operations.py` | all(), count(), first, iteration | Easy |
| `exercise_02_table_data.py` | Table extraction, headers, cells | Easy |
| `exercise_03_dynamic_elements.py` | Add/remove elements, verification | Medium |
| `exercise_04_filtering_search.py` | filter(), text search, navigation | Medium |
| `exercise_05_table_advanced.py` | Complex table operations, sorting | Hard |

Solutions are available in `exercises/SOLUTIONS.md`.

## Resources
- [Locator.all() API](https://playwright.dev/python/docs/api/class-locator#locator-all)
- [Locator.count() API](https://playwright.dev/python/docs/api/class-locator#locator-count)
- [Filtering](https://playwright.dev/python/docs/locators#filtering-locators)
