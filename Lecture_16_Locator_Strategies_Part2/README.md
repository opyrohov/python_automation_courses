# Lecture 16: Locator Strategies (Part 2)

Welcome to Lecture 16! Building on Part 1's fundamentals, we'll now explore advanced locator techniques that will make your tests more precise, powerful, and maintainable.

## Video Recording

Watch the lecture recording: [Loom Video](https://www.loom.com/share/3f747309314142629b19a29982e190ba)

## Table of Contents
1. [Introduction](#introduction)
2. [Chaining Locators](#chaining-locators)
3. [Filtering Locators](#filtering-locators)
4. [Selecting Specific Elements](#selecting-specific-elements)
5. [Playwright Inspector](#playwright-inspector)
6. [Practical Examples](#practical-examples)
7. [Best Practices](#best-practices)
8. [Practice Exercises](#practice-exercises)

## Introduction

### What We Covered in Part 1

In Lecture 15, we learned:
- CSS Selectors (ID, class, attributes)
- XPath basics
- Playwright Modern Locators (get_by_role, get_by_label, etc.)
- Basic best practices

### What We'll Cover in Part 2

Today we focus on **advanced techniques** for working with locators:
- **Chaining** - Combining locators for precision
- **Filtering** - Narrowing down multiple matches
- **Selection** - Choosing specific elements from matches
- **Debugging** - Using Playwright Inspector effectively

## Chaining Locators

### What is Locator Chaining?

**Chaining** means combining multiple locators to search progressively from broad to specific. Think of it like giving directions: instead of "find the button" (vague), you say "in the navigation bar, find the login button" (specific).

### Why Chain Locators?

```python
# ❌ Problem: Too vague
page.locator("button").click()  # Which button? Could be any button on the page!

# ✅ Solution: Chain for specificity
page.locator(".navbar").locator("button.login").click()  # Clear and precise!
```

### Basic Chaining Syntax

```python
# Chain with .locator()
page.locator(".container").locator(".sidebar").locator("button")

# Chain modern locators
page.get_by_role("navigation").get_by_role("link", name="Home")

# Mix CSS and modern locators
page.locator("#main-content").get_by_role("button", name="Submit")
```

**Key Concept:** Each chaining step searches **within** the results of the previous step.

### Real-World Chaining Example

**HTML Structure:**
```html
<div class="product-grid">
  <div class="product-card">
    <h3>Laptop</h3>
    <p class="price">$999</p>
    <button class="add-to-cart">Add to Cart</button>
  </div>
  <div class="product-card">
    <h3>Mouse</h3>
    <p class="price">$29</p>
    <button class="add-to-cart">Add to Cart</button>
  </div>
  <div class="product-card">
    <h3>Keyboard</h3>
    <p class="price">$79</p>
    <button class="add-to-cart">Add to Cart</button>
  </div>
</div>
```

**Without Chaining (Wrong!):**
```python
# This clicks the FIRST "Add to Cart" button (Laptop)
# Even if we want the Keyboard!
page.locator(".add-to-cart").click()
```

**With Chaining (Correct!):**
```python
# Find the Keyboard product card, THEN click its "Add to Cart" button
page.locator(".product-card").filter(has_text="Keyboard").locator(".add-to-cart").click()
```

### Chaining Patterns

#### Pattern 1: Container → Element
```python
# Find button inside a specific section
page.locator("#checkout-section").locator("button[type='submit']").click()

# Find input inside a form
page.locator("form#login").locator("input[name='email']").fill("user@example.com")
```

#### Pattern 2: Parent → Child → Grandchild
```python
# Navigate through nested structure
page.locator(".sidebar").locator(".menu").locator("a.active").click()
```

#### Pattern 3: Modern Locator → CSS
```python
# Start with role, then narrow with CSS
page.get_by_role("navigation").locator("a[href='/dashboard']").click()
```

#### Pattern 4: CSS → Modern Locator
```python
# Start with container, then use modern locator
page.locator(".user-panel").get_by_role("button", name="Logout").click()
```

### Chaining Best Practices

#### ✅ DO:
```python
# Keep chains readable (2-3 levels)
page.locator(".content").get_by_role("button", name="Save").click()

# Use semantic containers
page.locator("nav").get_by_role("link", name="Home").click()

# Mix strategies when beneficial
page.get_by_role("main").locator("#product-list").get_by_text("Featured").click()
```

#### ❌ DON'T:
```python
# Too long and fragile
page.locator("div").locator("div").locator("section").locator("div").locator("button")

# Position-based chaining (brittle)
page.locator("div:nth-child(3)").locator("span:nth-child(2)").locator("button:first-child")

# Using brittle selectors in chain
page.locator(".css-xyz123").locator(".generated-class-456").click()
```

## Filtering Locators

### Why Filter?

When a locator matches multiple elements, you need to select the right one:

```python
# This matches ALL buttons on the page!
page.locator("button").count()  # Returns: 23

# How do we click the RIGHT button?
# Answer: Filtering!
```

### filter(has_text="...")

Filter elements containing specific text.

```python
# Find product cards containing "Laptop"
page.locator(".product-card").filter(has_text="Laptop")

# Find list items containing "Active"
page.locator("li").filter(has_text="Active")

# Chain after filtering
page.locator(".product-card").filter(has_text="Laptop").locator("button").click()
```

**Example:**
```python
# HTML: Multiple todo items
# <li>Buy groceries</li>
# <li>Walk the dog</li>
# <li>Read a book</li>

# Find and click the "Walk the dog" todo
page.locator("li").filter(has_text="Walk the dog").click()
```

**Partial Matching:**
```python
# has_text does substring matching by default
page.locator(".message").filter(has_text="Error")  # Matches "Error: Invalid input"
```

### filter(has=locator)

Filter elements that **contain** a specific nested element.

```python
# Find product cards that have a "Sale" badge
page.locator(".product-card").filter(
    has=page.locator(".badge-sale")
)

# Find list items that contain a checkbox
page.locator("li").filter(
    has=page.get_by_role("checkbox")
)

# Find table rows with a "Delete" button
page.locator("tr").filter(
    has=page.get_by_role("button", name="Delete")
)
```

**Real Example:**
```python
# HTML
<div class="product-card">
  <h3>Laptop</h3>
  <span class="badge-sale">On Sale!</span>
  <button>Add to Cart</button>
</div>

# Find products on sale
on_sale_products = page.locator(".product-card").filter(
    has=page.locator(".badge-sale")
)
print(f"Found {on_sale_products.count()} products on sale")
```

### Combining Filters

Stack multiple filters for very precise targeting:

```python
# Find product with BOTH "Laptop" text AND "Sale" badge
page.locator(".product-card")
    .filter(has_text="Laptop")
    .filter(has=page.locator(".badge-sale"))
    .locator("button")
    .click()

# Find active items that also have a checkbox
page.locator("li")
    .filter(has_text="Active")
    .filter(has=page.get_by_role("checkbox"))
```

**Order Matters:**
```python
# More efficient: Start with most selective filter
page.locator(".product-card")
    .filter(has=page.locator(".badge-new"))  # Fewer matches
    .filter(has_text="Electronics")  # Then narrow further
```

### filter(has_not_text=) & filter(has_not=)

Exclude elements you don't want:

```python
# Find all products EXCEPT sold out ones
page.locator(".product-card").filter(has_not_text="Sold Out")

# Find list items WITHOUT a checkbox
page.locator("li").filter(
    has_not=page.get_by_role("checkbox")
)

# Find products without a sale badge
page.locator(".product-card").filter(
    has_not=page.locator(".badge-sale")
)
```

**Use Case:**
```python
# Get all enabled (not disabled) buttons
enabled_buttons = page.locator("button").filter(
    has_not_text="Disabled"
).all()

for button in enabled_buttons:
    print(button.text_content())
```

## Selecting Specific Elements

When a locator matches multiple elements, use these methods to select which one:

### .first - First Element

```python
# Click the first button
page.locator("button").first.click()

# Get text from first list item
first_text = page.locator("li").first.text_content()
print(first_text)

# Chain after .first
page.locator(".product-card").first.get_by_role("button").click()
```

**Use Case:** First search result, first notification, first item in a list.

⚠️ **Warning:** Position-based selection is brittle if order changes! Prefer filtering when possible.

### .last - Last Element

```python
# Click the last button
page.locator("button").last.click()

# Get the most recent notification
recent_notification = page.locator(".notification").last.text_content()

# Get last todo item
last_todo = page.locator("li.todo-item").last.text_content()
```

**Use Case:** Most recent item, latest notification, newest comment.

### .nth(index) - Specific Position

Access elements by index (0-based):

```python
# First item (index 0)
page.locator("li").nth(0).click()

# Second item (index 1)
page.locator("li").nth(1).click()

# Third item (index 2)
page.locator("li").nth(2).click()

# Negative indices work! (-1 = last)
page.locator("li").nth(-1).click()  # Same as .last

# Second to last
page.locator("li").nth(-2).click()
```

⚠️ **Warning:** Only use .nth() when:
- Order is guaranteed
- You can't identify by content
- Testing pagination or ordered lists

**Better Alternative:**
```python
# ❌ Position-based (fragile)
page.locator("button").nth(2).click()

# ✅ Content-based (robust)
page.get_by_role("button", name="Submit").click()
```

### .count() - Count Elements

Get the total number of matching elements:

```python
# How many buttons?
button_count = page.locator("button").count()
print(f"Found {button_count} buttons")

# Check if element exists
if page.locator(".error-message").count() > 0:
    print("Error message is present!")

# Verify exact count
product_count = page.locator(".product-card").count()
assert product_count == 10, f"Expected 10 products, found {product_count}"
```

**Use Cases:**
```python
# Check element presence without error
has_notification = page.locator(".notification").count() > 0

# Verify results
results = page.locator(".search-result").count()
assert results > 0, "No search results found"

# Compare counts
before = page.locator(".cart-item").count()
page.locator(".add-to-cart").first.click()
after = page.locator(".cart-item").count()
assert after == before + 1, "Cart item not added"
```

### .all() - Get All Elements

Returns a list of all matching locators:

```python
# Get all buttons
all_buttons = page.locator("button").all()

# Iterate through elements
for button in all_buttons:
    print(button.text_content())

# Get all product names
products = page.locator(".product-name").all()
product_names = [p.text_content() for p in products]
print(product_names)
```

**Practical Examples:**
```python
# Verify all checkboxes are checked
checkboxes = page.locator("input[type='checkbox']").all()
for checkbox in checkboxes:
    assert checkbox.is_checked(), "All checkboxes should be checked"

# Collect all prices
prices = page.locator(".price").all()
total = sum(float(p.text_content().replace("$", "")) for p in prices)
print(f"Total: ${total}")

# Find specific item in list
items = page.locator(".item").all()
for item in items:
    if "Featured" in item.text_content():
        item.click()
        break
```

### Combining Selection with Filtering

Maximum precision by combining techniques:

```python
# Get first product on sale
page.locator(".product-card")
    .filter(has_text="Sale")
    .first
    .click()

# Get last active todo
page.locator("li")
    .filter(has_text="Active")
    .last
    .text_content()

# Get 3rd Electronics product
page.locator(".product-card")
    .filter(has_text="Electronics")
    .nth(2)
    .click()

# Get all sold-out products
sold_out = page.locator(".product-card")
    .filter(has_text="Sold Out")
    .all()
```

## Playwright Inspector

### What is Playwright Inspector?

Playwright Inspector is a **built-in debugging tool** that helps you:
- 🔍 Test locators in real-time
- ⏸️ Pause test execution
- 👣 Step through code line-by-line
- 📊 View element highlights
- 🎯 Pick elements visually
- 📝 Get locator suggestions

### Launching Inspector

#### Method 1: Environment Variable

```bash
# Windows (CMD)
set PWDEBUG=1
python my_test.py

# Windows (PowerShell)
$env:PWDEBUG=1
python my_test.py

# Mac/Linux
PWDEBUG=1 python my_test.py
```

#### Method 2: page.pause()

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    page.pause()  # Opens Inspector here!

    page.locator("button").click()
    browser.close()
```

### Using Inspector Features

#### 1. Explorer (Pick Elements)
- Click the "Pick locator" button
- Click any element on the page
- Inspector generates multiple locator suggestions
- Choose the best one for your needs

#### 2. Locator Playground
- Type locators in the text box
- See which elements match in real-time
- Shows count of matches
- Highlights matching elements

Example:
```python
# Type in playground:
page.locator("button")
# Shows: "23 elements matched"

# Refine:
page.locator("button").filter(has_text="Login")
# Shows: "1 element matched" ✓
```

#### 3. Step Through Code
- Use Step Over to execute line-by-line
- See exactly what happens at each step
- Inspect state after each action
- Verify locators work as expected

#### 4. Console
- Run Playwright commands interactively
- Test locators before committing to code
- Debug failing assertions

### Debugging Workflow

When a locator isn't working:

1. **Add `page.pause()`** before the failing line
2. **Run with Inspector** (PWDEBUG=1 or page.pause())
3. **Use Explorer** to visually pick the element
4. **Review suggestions** - Inspector shows multiple options
5. **Test in playground** - Verify it matches the right element
6. **Check count** - Ensure only one (or expected number) matches
7. **Copy working locator** to your code
8. **Resume** and verify it works

### Inspector Tips

```python
# Tip 1: Test multiple locator strategies
# Inspector suggests:
# - page.get_by_role("button", name="Submit")
# - page.get_by_text("Submit")
# - page.locator("#submit-btn")
# Try each to find the most reliable!

# Tip 2: Use playground to test filters
page.locator("button").filter(has_text="Login")
# Inspector shows which button matches

# Tip 3: Verify count before using .first
page.locator(".product-card")
# Inspector shows: "12 elements matched"
# Now you know you need to filter more!
```

## Practical Examples

### Example 1: E-commerce Product Selection

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo-store.example.com")

    # Find "Laptop" product and add to cart
    page.locator(".product-card")
        .filter(has_text="Laptop")
        .locator(".add-to-cart")
        .click()

    # Verify cart count increased
    cart_count = page.locator(".cart-count").text_content()
    assert cart_count == "1", "Cart should have 1 item"

    browser.close()
```

### Example 2: Todo List Management

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")

    # Add some todos
    todos = ["Buy groceries", "Walk the dog", "Read a book"]
    for todo in todos:
        page.locator(".new-todo").fill(todo)
        page.locator(".new-todo").press("Enter")

    # Mark first as complete
    page.locator(".todo-list li").first.locator(".toggle").check()

    # Delete last todo
    page.locator(".todo-list li").last.hover()
    page.locator(".todo-list li").last.locator(".destroy").click()

    # Count remaining todos
    remaining = page.locator(".todo-list li").count()
    print(f"Remaining todos: {remaining}")

    browser.close()
```

### Example 3: Table Data Extraction

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/table")

    # Find row containing "John Doe"
    john_row = page.locator("tr").filter(has_text="John Doe")

    # Get email from that row (assuming it's in column 3)
    email = john_row.locator("td").nth(2).text_content()
    print(f"John's email: {email}")

    # Click "Edit" button in John's row
    john_row.locator("button").filter(has_text="Edit").click()

    # Count total rows
    total_rows = page.locator("tr").count()
    print(f"Total rows: {total_rows}")

    browser.close()
```

### Example 4: Complex Filtering

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/products")

    # Find products that are:
    # 1. In "Electronics" category
    # 2. On sale
    # 3. In stock
    electronics_on_sale = (
        page.locator(".product-card")
        .filter(has_text="Electronics")
        .filter(has=page.locator(".badge-sale"))
        .filter(has_not_text="Out of Stock")
    )

    # Get count
    count = electronics_on_sale.count()
    print(f"Found {count} electronics on sale and in stock")

    # Click the first one
    if count > 0:
        electronics_on_sale.first.locator(".add-to-cart").click()

    browser.close()
```

## Best Practices

### ✅ DO

1. **Filter by text when possible**
```python
# Preferred
page.locator(".product-card").filter(has_text="Laptop")

# Instead of
page.locator(".product-card").nth(2)  # Position-based
```

2. **Chain from broad to specific**
```python
# Good
page.locator("nav").get_by_role("link", name="Home")

# Bad
page.locator("nav > div > ul > li:nth-child(1) > a")
```

3. **Use .count() to verify**
```python
# Always verify your assumptions
matching = page.locator("button").filter(has_text="Submit").count()
assert matching == 1, f"Expected 1 submit button, found {matching}"
```

4. **Test with Inspector**
```python
# Before committing:
page.pause()  # Test locator in Inspector
page.locator(".my-locator").click()
```

5. **Combine techniques**
```python
# Mix chaining, filtering, and selection
page.locator(".sidebar")
    .get_by_role("list")
    .filter(has_text="Active")
    .first
    .click()
```

### ❌ AVOID

1. **Position-only selection**
```python
# ❌ Brittle
page.locator("button").nth(3).click()

# ✅ Better
page.get_by_role("button", name="Submit").click()
```

2. **Long, complex chains**
```python
# ❌ Too complex
page.locator("div").locator("div").locator("section").locator("div").locator("button")

# ✅ Simpler
page.locator("#main-section").get_by_role("button", name="Save")
```

3. **Assuming single match**
```python
# ❌ Dangerous
page.locator(".product-card").click()  # Which one?

# ✅ Explicit
page.locator(".product-card").filter(has_text="Laptop").first.click()
```

4. **Skipping verification**
```python
# ❌ No validation
page.locator("button").click()

# ✅ Verify first
assert page.locator("button").count() == 1
page.locator("button").click()
```

## Practice Exercises

See the `exercises/` folder for hands-on practice:

1. **Chaining Challenge** - Practice chaining locators on complex pages
2. **Filtering Exercise** - Use has_text and has filters
3. **Selection Practice** - Work with .first, .last, .nth()
4. **Inspector Workshop** - Debug locators using Playwright Inspector
5. **Real-World Scenarios** - Apply all techniques to realistic websites

## Summary

**Key Takeaways:**

1. ✅ **Chain locators** from broad to specific for precision
2. ✅ **Filter by text** using filter(has_text="...") when possible
3. ✅ **Filter by content** using filter(has=locator) for nested elements
4. ✅ **Select carefully** with .first, .last, .nth() - prefer text when possible
5. ✅ **Count and verify** with .count() before interacting
6. ✅ **Iterate all** with .all() when needed
7. ✅ **Debug effectively** with Playwright Inspector
8. ✅ **Combine techniques** for maximum precision

**Golden Rule:** Make your locators as specific as needed, but as simple as possible!

## What's Next?

In upcoming lectures:
- **Advanced Interactions** - Hover, drag & drop, keyboard actions
- **Waiting Strategies** - Timeouts, auto-waiting, custom waits
- **Assertions** - Verify element states and content
- **Form Handling** - Checkboxes, dropdowns, file uploads

Happy coding! 🎯
