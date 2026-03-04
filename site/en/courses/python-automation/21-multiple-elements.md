# Lecture 21: Working with Multiple Elements

Working with collections of elements.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_21_Multiple_Elements/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_21_Multiple_Elements/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_21_Multiple_Elements/exercises" target="_blank">📝 Вправи</a>
</div>

## Basic Operations

```python
# Get all elements
items = page.locator(".product-card")

# Count
count = items.count()
print(f"Found {count} items")

# First / Last
items.first.click()
items.last.click()

# By index
items.nth(2).click()
```

## Iteration

```python
items = page.locator(".product-card")

# Loop through elements
for i in range(items.count()):
    item = items.nth(i)
    print(item.text_content())

# all() returns a list
all_items = items.all()
for item in all_items:
    print(item.text_content())
```

## Filtering

```python
# By text
page.locator(".card").filter(has_text="Sale").click()

# By nested element
page.locator(".card").filter(
    has=page.get_by_role("button", name="Buy")
).first.click()

# Combination
page.locator(".product").filter(has_text="iPhone").filter(
    has=page.locator(".in-stock")
).first.click()
```

## Example: Table

```python
# Find row with text
row = page.locator("table tr").filter(has_text="John Doe")

# Click button in that row
row.get_by_role("button", name="Edit").click()

# Get value from a column
cells = row.locator("td")
name = cells.nth(0).text_content()
email = cells.nth(1).text_content()
```

## Example: Product List

```python
def get_all_product_names(page):
    products = page.locator(".product-card")
    names = []
    for i in range(products.count()):
        name = products.nth(i).locator(".product-name").text_content()
        names.append(name)
    return names

def click_product_by_name(page, name):
    page.locator(".product-card").filter(has_text=name).click()
```

## Assertions for Collections

```python
from playwright.sync_api import expect

# Check count
expect(page.locator(".item")).to_have_count(5)

# Check text of all elements
expect(page.locator(".item")).to_have_text([
    "First",
    "Second",
    "Third"
])
```
