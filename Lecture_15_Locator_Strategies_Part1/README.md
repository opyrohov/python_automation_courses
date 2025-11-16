# Lecture 15: Locator Strategies (Part 1)

Welcome to Lecture 15! In this lecture, we'll dive deep into locator strategies - one of the most critical skills for browser automation. Choosing the right locators makes your tests reliable, maintainable, and resilient to changes.

## Table of Contents
1. [Introduction to Locators](#introduction-to-locators)
2. [CSS Selectors](#css-selectors)
3. [XPath Basics](#xpath-basics)
4. [Playwright Modern Locators](#playwright-modern-locators)
5. [Best Practices](#best-practices)
6. [Common Pitfalls](#common-pitfalls)
7. [Practice Exercises](#practice-exercises)

## Introduction to Locators

### What are Locators?

**Locators** are expressions that tell Playwright how to find elements on a web page. They're the foundation of all browser automation - you need them to click buttons, fill forms, read text, and interact with any element on a page.

### Why Do Locators Matter?

The quality of your locators directly impacts:
- **Test Reliability** - Good locators = stable tests
- **Maintainability** - Clear locators = easy updates
- **Resilience** - Smart locators = fewer breaks when UI changes
- **Readability** - Semantic locators = self-documenting tests

### Types of Locators

Playwright supports multiple locator strategies:

1. **Playwright Modern Locators** (Recommended)
   - `get_by_role()`
   - `get_by_label()`
   - `get_by_placeholder()`
   - `get_by_text()`
   - `get_by_test_id()`

2. **CSS Selectors**
   - ID, class, attribute selectors
   - Combinators and pseudo-classes

3. **XPath**
   - Path-based navigation
   - Advanced text matching

## CSS Selectors

CSS selectors are the same selectors used in CSS stylesheets. They're fast, widely supported, and familiar to most developers.

### Basic CSS Selectors

#### 1. ID Selector (#id)

IDs should be unique on a page, making them highly reliable.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    # Select element by ID
    page.locator("#submit-button").click()
    page.locator("#username").fill("john_doe")

    browser.close()
```

**HTML Example:**
```html
<button id="submit-button">Submit</button>
<input id="username" type="text">
```

#### 2. Class Selector (.class)

Classes can appear multiple times, so be specific!

```python
# Single class
page.locator(".btn-primary").click()

# Multiple classes (element must have both)
page.locator(".btn.btn-primary").click()

# Be specific with tag + class
page.locator("button.btn-primary").click()
```

**HTML Example:**
```html
<button class="btn btn-primary">Login</button>
<button class="btn btn-secondary">Cancel</button>
```

⚠️ **Warning:** Using only a common class like `.btn` might match multiple elements!

#### 3. Tag Selector

Select elements by their HTML tag name.

```python
# Select all buttons
page.locator("button")

# Select all inputs
page.locator("input")

# Usually combined with other selectors
page.locator("button.submit")
```

### Attribute Selectors

Attribute selectors allow you to target elements based on their attributes and values.

#### Syntax Variations

```python
# Has attribute (any value)
page.locator("[data-testid]")
page.locator("[disabled]")

# Exact attribute value
page.locator("[type='submit']")
page.locator("[name='email']")

# Attribute contains value (substring)
page.locator("[class*='btn']")  # class contains 'btn'

# Attribute starts with value
page.locator("[href^='https']")  # href starts with 'https'

# Attribute ends with value
page.locator("[src$='.png']")  # src ends with '.png'

# Attribute contains word (space-separated)
page.locator("[class~='primary']")  # class contains word 'primary'
```

#### Real-World Examples

```python
# Select submit buttons
page.locator("[type='submit']").click()

# Select elements by data attribute
page.locator("[data-action='delete']").click()

# Select by name attribute
page.locator("[name='userEmail']").fill("user@example.com")

# Select external links
page.locator("[href^='http']").click()

# Select PNG images
page.locator("img[src$='.png']")

# Combine multiple attributes
page.locator("input[type='text'][name='search']")
```

### Combining Selectors

You can combine multiple selector types for precise targeting.

```python
# Tag + class
page.locator("button.btn-primary")

# Tag + ID
page.locator("input#username")

# Tag + attribute
page.locator("button[type='submit']")

# Multiple classes and attribute
page.locator("button.btn.btn-lg[type='submit']")

# Class + attribute
page.locator(".form-control[placeholder='Email']")
```

### CSS Combinators

Combinators define relationships between selectors.

#### Descendant Selector (space)

Selects all descendants at any level.

```python
# Select all buttons inside .container (at any depth)
page.locator(".container button")

# Select all inputs inside form
page.locator("form input")
```

**HTML Example:**
```html
<div class="container">
  <div class="wrapper">
    <button>Click Me</button> <!-- This is selected -->
  </div>
</div>
```

#### Child Selector (>)

Selects only direct children (immediate descendants).

```python
# Select only direct child buttons of form
page.locator("form > button")

# Select only direct child divs of .container
page.locator(".container > div")
```

**HTML Example:**
```html
<form>
  <button>Direct Child</button> <!-- This is selected -->
  <div>
    <button>Not Direct Child</button> <!-- This is NOT selected -->
  </div>
</form>
```

#### Adjacent Sibling Selector (+)

Selects the element immediately following another element.

```python
# Select input immediately after label
page.locator("label + input")

# Select p immediately after h2
page.locator("h2 + p")
```

**HTML Example:**
```html
<label>Email</label>
<input type="email"> <!-- This is selected -->
<input type="text">  <!-- This is NOT selected -->
```

#### General Sibling Selector (~)

Selects all siblings after an element.

```python
# Select all p elements after h2
page.locator("h2 ~ p")

# Select all inputs after label
page.locator("label ~ input")
```

### CSS Pseudo-classes

```python
# First child
page.locator("li:first-child")

# Last child
page.locator("li:last-child")

# Nth child (1-indexed)
page.locator("li:nth-child(2)")

# Enabled/disabled
page.locator("input:enabled")
page.locator("input:disabled")

# Checked (for checkboxes/radios)
page.locator("input:checked")
```

⚠️ **Note:** While pseudo-classes work, Playwright's modern locators are usually better!

## XPath Basics

XPath (XML Path Language) is a powerful query language for selecting nodes in XML/HTML documents.

### When to Use XPath

Use XPath when:
- ✅ CSS selectors can't express the relationship you need
- ✅ You need to navigate up the DOM tree (to parent elements)
- ✅ You need complex text matching
- ✅ You need to select by position or index in specific contexts

**However:** XPath can be slower than CSS and harder to read. Use it judiciously!

### Absolute vs Relative Paths

```python
# ❌ ABSOLUTE PATH - NEVER USE THIS!
page.locator("xpath=/html/body/div[2]/form/button")
# Breaks with any DOM structure change

# ✅ RELATIVE PATH - ALWAYS USE THIS
page.locator("xpath=//button[@type='submit']")
# Searches anywhere in document
```

### Basic XPath Syntax

```python
# Select by tag
page.locator("xpath=//button")
page.locator("xpath=//input")

# Select by attribute
page.locator("xpath=//button[@type='submit']")
page.locator("xpath=//input[@name='email']")

# Select by ID
page.locator("xpath=//*[@id='submit-btn']")
page.locator("xpath=//button[@id='submit-btn']")

# Select by class (exact match)
page.locator("xpath=//button[@class='btn-primary']")

# Select by class (contains)
page.locator("xpath=//button[contains(@class, 'btn-primary')]")
```

### Text-Based XPath

XPath excels at text matching:

```python
# Exact text match
page.locator("xpath=//button[text()='Login']")
page.locator("xpath=//h1[text()='Welcome']")

# Contains text
page.locator("xpath=//div[contains(text(), 'Welcome')]")
page.locator("xpath=//p[contains(text(), 'Error')]")

# Starts with text
page.locator("xpath=//h2[starts-with(text(), 'Chapter')]")

# Normalize space (handles whitespace)
page.locator("xpath=//button[normalize-space()='Login']")
```

### XPath Axes

Axes allow you to navigate relationships in the DOM tree.

```python
# Parent
page.locator("xpath=//button[@id='submit']/parent::form")

# Ancestor (any level up)
page.locator("xpath=//button[@id='submit']/ancestor::div")

# Child
page.locator("xpath=//form/child::button")

# Following sibling (all siblings after)
page.locator("xpath=//label[text()='Email']/following-sibling::input")

# Preceding sibling (all siblings before)
page.locator("xpath=//input[@name='email']/preceding-sibling::label")

# Descendant (any level down)
page.locator("xpath=//form/descendant::input")
```

### XPath Functions

```python
# Count elements
page.locator("xpath=//button[count(//button) > 5]")

# Position
page.locator("xpath=//button[position()=1]")
page.locator("xpath=//button[last()]")

# String functions
page.locator("xpath=//div[string-length(text()) > 10]")
page.locator("xpath=//button[substring(text(), 1, 3)='Log']")
```

### Real-World XPath Example

**HTML:**
```html
<div class="product-card">
  <h3>Laptop</h3>
  <p class="price">$999</p>
  <button class="add-to-cart">Add to Cart</button>
</div>
```

**Playwright Code:**
```python
# Find the "Add to Cart" button for the product named "Laptop"
page.locator("xpath=//div[.//h3[text()='Laptop']]//button[@class='add-to-cart']").click()

# Get the price of the product named "Laptop"
price = page.locator("xpath=//div[.//h3[text()='Laptop']]//p[@class='price']").text_content()
print(price)  # $999
```

## Playwright Modern Locators

Playwright's modern locators are **user-facing** and **accessible** - they interact with your app the way real users do!

### Why Modern Locators?

**Benefits:**
- ✅ More resilient to DOM changes
- ✅ Improve accessibility testing
- ✅ Self-documenting code
- ✅ Built-in auto-waiting and retrying
- ✅ Better error messages

**Playwright Recommendation:** Always prefer modern locators over CSS/XPath when possible!

### get_by_role() - The Best Locator

`get_by_role()` is Playwright's #1 recommended locator. It selects elements by their ARIA role and accessible name.

```python
# Buttons
page.get_by_role("button", name="Login").click()
page.get_by_role("button", name="Submit").click()

# Links
page.get_by_role("link", name="Contact Us").click()
page.get_by_role("link", name="Documentation").click()

# Textboxes
page.get_by_role("textbox", name="Email").fill("user@example.com")
page.get_by_role("textbox", name="Search").fill("laptop")

# Checkboxes
page.get_by_role("checkbox", name="Accept terms").check()
page.get_by_role("checkbox", name="Remember me").check()

# Radio buttons
page.get_by_role("radio", name="Option A").click()

# Headings
expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
```

#### Common ARIA Roles

```python
# Structural
page.get_by_role("navigation")      # <nav> or role="navigation"
page.get_by_role("main")            # <main> or role="main"
page.get_by_role("banner")          # <header> or role="banner"
page.get_by_role("contentinfo")     # <footer> or role="contentinfo"

# Interactive
page.get_by_role("button")          # <button> or role="button"
page.get_by_role("link")            # <a href> or role="link"
page.get_by_role("textbox")         # <input type="text">
page.get_by_role("combobox")        # <select> or role="combobox"
page.get_by_role("checkbox")        # <input type="checkbox">
page.get_by_role("radio")           # <input type="radio">

# Content
page.get_by_role("heading")         # <h1> to <h6>
page.get_by_role("list")            # <ul>, <ol>
page.get_by_role("listitem")        # <li>
page.get_by_role("table")           # <table>
page.get_by_role("row")             # <tr>
page.get_by_role("cell")            # <td>
```

### get_by_text() - Find by Visible Text

Locate elements by their text content.

```python
# Exact match (default)
page.get_by_text("Login").click()
page.get_by_text("Welcome to our site").is_visible()

# Partial match
page.get_by_text("Welcome", exact=False).is_visible()

# Case-sensitive by default
page.get_by_text("LOGIN")  # Won't match "Login"

# Find within a container
page.locator(".sidebar").get_by_text("Settings").click()
```

**Use Cases:**
- Clicking links or buttons with text
- Verifying text content is visible
- Finding headings or labels

```python
# Click a link
page.get_by_text("Terms of Service").click()

# Verify welcome message
expect(page.get_by_text("Welcome back, John!")).to_be_visible()

# Find specific product
page.get_by_text("Laptop - $999").click()
```

### get_by_label() - Find Form Inputs by Label

Locate form inputs by their associated label text.

```python
# Works with explicit labels (using 'for' attribute)
page.get_by_label("Email Address").fill("user@example.com")
page.get_by_label("Password").fill("secret123")

# Works with implicit labels (wrapping)
page.get_by_label("Remember me").check()

# Partial match
page.get_by_label("Email", exact=False).fill("user@example.com")
```

**HTML Examples:**

```html
<!-- Explicit label with 'for' -->
<label for="email">Email Address</label>
<input id="email" type="email">

<!-- Implicit label (wrapping) -->
<label>
  Password
  <input type="password">
</label>

<!-- aria-label -->
<input type="text" aria-label="Search">
```

**Playwright Code:**
```python
page.get_by_label("Email Address").fill("user@example.com")
page.get_by_label("Password").fill("secret123")
page.get_by_label("Search").fill("laptop")
```

### get_by_placeholder() - Find by Placeholder

Locate inputs by their placeholder text.

```python
# Exact match
page.get_by_placeholder("Search products...").fill("laptop")
page.get_by_placeholder("Enter your email").fill("user@example.com")

# Partial match
page.get_by_placeholder("email", exact=False).fill("user@example.com")
```

**HTML Example:**
```html
<input type="text" placeholder="Search products...">
<input type="email" placeholder="Enter your email">
```

⚠️ **Note:** Prefer `get_by_label()` when possible - it's more accessible!

### get_by_alt_text() - Find Images

Locate images by their alt text.

```python
# Find and click an image
page.get_by_alt_text("Company Logo").click()

# Verify image is visible
expect(page.get_by_alt_text("User profile picture")).to_be_visible()

# Partial match
page.get_by_alt_text("profile", exact=False)
```

**HTML Example:**
```html
<img src="logo.png" alt="Company Logo">
<img src="profile.jpg" alt="User profile picture">
```

### get_by_title() - Find by Title Attribute

Locate elements by their title attribute (tooltip text).

```python
# Click elements by title
page.get_by_title("Close dialog").click()
page.get_by_title("Get help").click()

# Partial match
page.get_by_title("help", exact=False).click()
```

**HTML Example:**
```html
<button title="Close dialog">X</button>
<a href="/help" title="Get help and support">?</a>
```

### get_by_test_id() - Test-Specific IDs

Use test IDs when user-facing attributes aren't stable or available.

```python
# Default attribute is 'data-testid'
page.get_by_test_id("submit-button").click()
page.get_by_test_id("error-message").text_content()

# Verify test ID element
expect(page.get_by_test_id("success-banner")).to_be_visible()
```

**HTML Example:**
```html
<button data-testid="submit-button">Submit</button>
<div data-testid="error-message">Invalid input</div>
```

**When to Use Test IDs:**
- ✅ No stable user-facing attributes exist
- ✅ Text content changes frequently (translations, A/B tests)
- ✅ Multiple similar elements need distinction
- ✅ Complex dynamic components

### Chaining and Filtering Locators

Combine locators for precise targeting.

```python
# Chain modern locators
page.get_by_role("navigation").get_by_role("link", name="Home").click()

# Filter by text
page.get_by_role("listitem").filter(has_text="Product A").click()

# Filter by nested element
page.get_by_role("listitem").filter(
    has=page.get_by_role("button", name="Buy Now")
).click()

# Combine CSS with modern locators
page.locator(".product-card").get_by_role("button", name="Add to Cart").click()

# Chain multiple filters
page.get_by_role("listitem").filter(has_text="Product A").get_by_role("button").click()
```

## Best Practices

### Locator Priority

**Playwright's Recommended Priority (Best to Worst):**

1. **`get_by_role()`** - ARIA roles & accessible names
2. **`get_by_label()`** - Form fields with labels
3. **`get_by_placeholder()`** - Form fields with placeholders
4. **`get_by_text()`** - Text content
5. **`get_by_test_id()`** - Test-specific data attributes
6. **CSS selectors** - When above don't work
7. **XPath** - Last resort for complex cases

### Good vs Bad Locators

#### ❌ Bad Locators

```python
# Absolute XPath - breaks easily
page.locator("xpath=/html/body/div[2]/form/button[1]")

# Position-based - breaks if order changes
page.locator("button:nth-child(3)")

# Generic classes - too broad
page.locator(".btn")

# Generated class names - change on builds
page.locator(".css-1dbjc4n.r-1awozwy")

# Framework-specific attributes - implementation details
page.locator("[ng-click='submit()']")
page.locator("[v-on:click='handleSubmit']")
```

#### ✅ Good Locators

```python
# Role-based - user-facing
page.get_by_role("button", name="Submit")

# Label-based - accessible
page.get_by_label("Email Address")

# Test ID - stable and clear
page.get_by_test_id("checkout-submit")

# Semantic CSS - meaningful attributes
page.locator("#login-form")
page.locator("[name='userEmail']")

# Specific and clear
page.locator("button[type='submit'][form='login']")
```

### Avoid Brittle Selectors

**What makes a selector brittle?**

- ❌ Position-dependent (`nth-child`, `nth-of-type`)
- ❌ Absolute paths
- ❌ Auto-generated class names
- ❌ Too specific (long chains)
- ❌ Implementation details

**Better alternatives:**

```python
# ❌ Brittle
page.locator("div.container > div.row > div.col-md-6 > form > div:nth-child(2) > input")

# ✅ Better - use name attribute
page.locator("[name='email']")

# ✅ Best - use label
page.get_by_label("Email")
```

### Keep Selectors Simple

```python
# ❌ Too complex
page.locator("div.main > section.content > div.form-wrapper > form.login-form > div.input-group:nth-child(1) > input.form-control")

# ✅ Simple and clear
page.get_by_label("Email")
# or
page.locator("#email")
# or
page.locator("[name='email']")
```

**Rule of Thumb:** If you can't explain your selector in one sentence, it's too complex!

### Use Test IDs Wisely

Add test IDs when:
- No stable user-facing attributes exist
- Text changes frequently (i18n, A/B tests)
- Distinguishing similar elements
- Testing complex dynamic components

```python
# Good use of test ID
# HTML: <button data-testid="checkout-submit" class="btn-xyz123">{{ translatedText }}</button>
page.get_by_test_id("checkout-submit").click()
```

## Common Pitfalls

### Pitfall #1: Relying on Order

```python
# ❌ BAD - breaks if order changes
page.locator("button").nth(2).click()

# ✅ GOOD - use identifying attribute
page.get_by_role("button", name="Submit").click()
```

### Pitfall #2: Generated Class Names

```python
# ❌ BAD - generated classes change on build
page.locator(".css-1dbjc4n-x9f619").click()

# ✅ GOOD - use stable identifier
page.get_by_test_id("submit-btn").click()
```

### Pitfall #3: Overly Specific Selectors

```python
# ❌ BAD - too specific, breaks easily
page.locator("div.container > div.wrapper > form.login > div.form-group > input#email")

# ✅ GOOD - just enough specificity
page.locator("#email")
# or
page.get_by_label("Email")
```

### Pitfall #4: Ignoring Accessibility

```python
# ❌ MISSED OPPORTUNITY
page.locator("#submit-btn-xyz").click()

# ✅ BETTER - also improves accessibility
page.get_by_role("button", name="Submit Form").click()
```

## Debugging Locators

### Count Matching Elements

```python
# How many buttons match?
count = page.locator(".btn").count()
print(f"Found {count} buttons")

if count == 0:
    print("No buttons found!")
elif count > 1:
    print(f"Multiple buttons found: {count}")
```

### Get All Text Contents

```python
# Get all button texts
button_texts = page.locator("button").all_text_contents()
print(button_texts)  # ['Login', 'Sign Up', 'Cancel']
```

### Highlight Element

```python
# Visually highlight element (helpful when debugging)
page.locator("#submit").highlight()
```

### Use Playwright Inspector

Run tests with Playwright Inspector to test locators interactively:

```bash
# Windows
set PWDEBUG=1
python my_test.py

# Mac/Linux
PWDEBUG=1 python my_test.py
```

### Browser DevTools

Test selectors in browser console:

```javascript
// CSS selector
document.querySelector("#submit-btn")
document.querySelectorAll(".btn")

// XPath
$x("//button[@type='submit']")
$x("//button[text()='Login']")

// Count
document.querySelectorAll(".btn").length
```

## Practice Exercises

See the `exercises/` folder for hands-on practice with:

1. **CSS Selector Challenges** - Practice different CSS selector types
2. **XPath Exercises** - Master XPath for complex scenarios
3. **Modern Locator Practice** - Use Playwright's recommended locators
4. **Locator Refactoring** - Convert brittle selectors to robust ones
5. **Real-World Scenarios** - Apply locators to realistic web pages

## Summary

**Key Takeaways:**

1. ✅ **Prefer Playwright's modern locators** (`get_by_role`, `get_by_label`) - they're user-facing and resilient
2. ✅ **Use CSS selectors for stable attributes** (ID, name, data-testid)
3. ✅ **Use XPath sparingly** - only when CSS can't express what you need
4. ✅ **Avoid brittle selectors** - no positions, no generated classes
5. ✅ **Keep selectors simple** - readable and maintainable
6. ✅ **Add test IDs when needed** - but prefer user-facing attributes first
7. ✅ **Test your selectors** - use DevTools and Playwright Inspector

## What's Next?

In the next lecture, we'll cover:
- **Locator Strategies Part 2** - Advanced filtering, chaining, and dynamic locators
- **Handling multiple elements** - Working with lists and collections
- **Locator assertions** - Verifying element states

Happy coding! 🎯
