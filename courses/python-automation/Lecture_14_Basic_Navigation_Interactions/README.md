# Lecture 14: Basic Navigation & Interactions

Welcome to Lecture 14! Now that you have Playwright installed and set up, it's time to learn the fundamentals of browser navigation and user interactions.

## Table of Contents
1. [Navigation Basics](#navigation-basics)
2. [Pages & Browser Contexts](#pages--browser-contexts)
3. [Basic Actions](#basic-actions)
4. [Getting Page Information](#getting-page-information)
5. [Closing Browsers Properly](#closing-browsers-properly)
6. [Practice Exercises](#practice-exercises)

## Navigation Basics

### The Four Core Navigation Methods

#### 1. page.goto() - Navigate to URL

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Basic navigation
    page.goto("https://example.com")

    # With options
    page.goto("https://example.com",
              wait_until="networkidle",  # Wait for network to be idle
              timeout=30000)              # 30 seconds timeout

    browser.close()
```

**wait_until Options:**
- `load` - Wait for 'load' event (default)
- `domcontentloaded` - Wait for DOM to be loaded
- `networkidle` - Wait until no network activity for 500ms
- `commit` - Wait for navigation to commit

**Getting Response:**
```python
response = page.goto("https://example.com")
print(f"Status: {response.status}")  # 200
print(f"OK: {response.ok}")          # True if 200-299
```

#### 2. page.go_back() - Navigate Back

```python
page.goto("https://example.com")
page.goto("https://playwright.dev")

# Go back to example.com
page.go_back()
print(page.url)  # https://example.com/
```

#### 3. page.go_forward() - Navigate Forward

```python
# After going back, go forward
page.go_forward()
print(page.url)  # https://playwright.dev/
```

#### 4. page.reload() - Reload Page

```python
# Reload current page
page.reload()

# With options
page.reload(wait_until="networkidle", timeout=30000)
```

### Complete Navigation Example

```python
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # Navigate to first page
    page.goto("https://example.com")
    print(f"1. Current: {page.url}")
    time.sleep(1)

    # Navigate to second page
    page.goto("https://playwright.dev")
    print(f"2. Current: {page.url}")
    time.sleep(1)

    # Go back
    page.go_back()
    print(f"3. After back: {page.url}")
    time.sleep(1)

    # Go forward
    page.go_forward()
    print(f"4. After forward: {page.url}")
    time.sleep(1)

    # Reload
    page.reload()
    print(f"5. After reload: {page.url}")

    browser.close()
```

## Pages & Browser Contexts

### Understanding the Hierarchy

```
Browser (Chrome/Firefox/WebKit)
└── Context 1 (Isolated session)
    ├── Page 1 (Tab 1)
    ├── Page 2 (Tab 2)
    └── Page 3 (Tab 3)
└── Context 2 (Different session)
    └── Page 4 (Tab 1)
```

**Key Concepts:**
- **Browser**: The browser process (heavy to create)
- **Context**: Isolated incognito-like session (lightweight)
- **Page**: A single tab/window

### Creating Browser Contexts

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Create first context (User A)
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://example.com")

    # Create second context (User B)
    context2 = browser.new_context()
    page2 = context2.new_page()
    page2.goto("https://example.com")

    # Each context has isolated cookies/storage!

    context1.close()
    context2.close()
    browser.close()
```

### Multiple Pages in One Context

```python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Create multiple pages (tabs)
    page1 = context.new_page()
    page1.goto("https://example.com")

    page2 = context.new_page()
    page2.goto("https://playwright.dev")

    page3 = context.new_page()
    page3.goto("https://github.com")

    # All pages share same context (cookies, storage)
    print(f"Total pages: {len(context.pages)}")  # 3

    browser.close()
```

### Context Options

```python
context = browser.new_context(
    viewport={'width': 1920, 'height': 1080},
    user_agent='Custom User Agent',
    locale='en-US',
    timezone_id='America/New_York',
    permissions=['geolocation'],
    geolocation={'latitude': 40.7128, 'longitude': -74.0060},
    ignore_https_errors=True
)
```

**Common Options:**
- `viewport` - Browser window size
- `user_agent` - Custom user agent string
- `locale` - Language/region (en-US, fr-FR, etc.)
- `timezone_id` - Timezone
- `permissions` - Grant permissions (notifications, geolocation)
- `ignore_https_errors` - Ignore SSL errors

## Basic Actions

### Three Core Actions

| Action | Purpose | When to Use |
|--------|---------|-------------|
| **click()** | Click an element | Buttons, links, checkboxes |
| **fill()** | Fill input fast | Forms (fast, no events) |
| **type()** | Type character by character | When you need keyboard events |

### 1. page.click() - Click Elements

```python
# Basic click
page.click("button")

# Click with different selectors
page.click("#submit-btn")              # ID
page.click(".login-button")            # Class
page.click("text=Sign In")             # Text content
page.click("button:has-text('Save')")  # Contains text

# Click with options
page.click("button",
          button="right",     # Right-click
          click_count=2,      # Double-click
          timeout=5000)       # 5 second timeout
```

**Click Options:**
- `button` - "left" (default), "right", "middle"
- `click_count` - Number of clicks (1=single, 2=double)
- `delay` - Delay between mousedown and mouseup (ms)
- `force` - Skip actionability checks (use carefully!)
- `timeout` - Maximum wait time

**Examples:**

```python
# Single click
page.click("button#submit")

# Double-click
page.click("button", click_count=2)

# Right-click
page.click("button", button="right")
```

### 2. page.fill() - Fill Input Fields

```python
# Fill form fields
page.fill("input[name='username']", "john_doe")
page.fill("#email", "john@example.com")
page.fill(".password-input", "SecurePass123")
```

**How fill() works:**
1. Focuses the input element
2. Clears existing value
3. Sets the new value instantly
4. Does NOT trigger keyboard events

**Use fill() when:**
- Filling forms quickly
- No need for keyboard events
- Default choice for most inputs

### 3. page.type() - Type Text

```python
# Type character by character
page.type("input[name='search']", "Playwright")

# Type with delay
page.type("input", "Hello World", delay=100)  # 100ms between chars
```

**How type() works:**
1. Focuses the input element
2. Types each character one by one
3. Triggers keyboard events (keydown, keypress, keyup)
4. Slower but more realistic

**Use type() when:**
- Your application listens to keyboard events
- Testing autocomplete functionality
- Simulating human typing behavior

### fill() vs type() - Key Differences

| Feature | fill() | type() |
|---------|--------|--------|
| **Speed** | ⚡ Very Fast | 🐢 Slower |
| **Clears First** | ✅ Yes | ❌ No (appends) |
| **Keyboard Events** | ❌ No | ✅ Yes |
| **Use Case** | Forms, inputs | Search boxes, autocomplete |
| **Recommended** | ✅ Default choice | ⚠️ Special cases |

**Example:**

```python
# Choose fill() for most cases
page.fill("input[name='email']", "user@example.com")  # Fast ✓

# Use type() for autocomplete/search
page.type("input[name='search']", "Python", delay=50)  # Triggers events ✓
```

### Complete Form Example

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://example.com/login")

    # Fill form fields
    page.fill("input[name='username']", "john_doe")
    page.fill("input[name='password']", "SecurePass123")
    page.fill("input[name='email']", "john@example.com")

    # Check checkbox
    page.check("input[type='checkbox']")

    # Click submit button
    page.click("button[type='submit']")

    # Wait for navigation
    page.wait_for_url("**/dashboard")

    print("Login successful!")

    browser.close()
```

## Getting Page Information

### page.title() - Get Page Title

```python
# Get page title
title = page.title()
print(title)  # "Example Domain"

# Use in assertions
assert page.title() == "Example Domain"
assert "Example" in page.title()
```

### page.url - Get Current URL

```python
# Get current URL
current_url = page.url
print(current_url)  # "https://example.com/"

# Check URL after navigation
assert "login" in page.url
assert page.url.startswith("https://")
```

### page.content() - Get Page HTML

```python
# Get full page HTML
html = page.content()
print(html[:100])  # Print first 100 chars

# Check if text exists in HTML
if "Welcome" in html:
    print("Welcome message found!")

# Save HTML to file
with open("page.html", "w", encoding="utf-8") as f:
    f.write(page.content())
```

### Complete Example

```python
from playwright.sync_api import sync_playwright

def get_page_info(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate
        response = page.goto(url)

        # Collect info
        info = {
            'url': page.url,
            'title': page.title(),
            'status': response.status,
            'ok': response.ok,
            'content_length': len(page.content()),
            'viewport': page.viewport_size
        }

        browser.close()
        return info

# Usage
page_info = get_page_info("https://playwright.dev")
print(f"Title: {page_info['title']}")
print(f"URL: {page_info['url']}")
print(f"Status: {page_info['status']}")
print(f"Content: {page_info['content_length']} chars")
```

## Closing Browsers Properly

### Closing Hierarchy

```python
# Close page only
page.close()

# Close context (closes all its pages)
context.close()

# Close browser (closes all contexts and pages)
browser.close()
```

**Remember:**
- `browser.close()` → Closes everything
- `context.close()` → Closes all pages in that context
- `page.close()` → Closes only that specific page

### Closing Examples

```python
# Example 1: Close individual pages
page1 = browser.new_page()
page2 = browser.new_page()

page1.close()  # Close only page1
page2.close()  # Close only page2
browser.close()  # Close browser

# Example 2: Close context (closes all pages)
context = browser.new_context()
page1 = context.new_page()
page2 = context.new_page()

context.close()  # Closes both page1 and page2
browser.close()

# Example 3: Close browser (closes everything)
browser = p.chromium.launch()
page1 = browser.new_page()
page2 = browser.new_page()

browser.close()  # Closes all contexts and pages
```

### Using Context Managers (Recommended)

```python
# Recommended: Use 'with' statement
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://example.com")
    print(page.title())

    # browser.close() called automatically!
```

**Why use 'with'?**
- ✅ Automatic cleanup even if errors occur
- ✅ Cleaner code
- ✅ Prevents resource leaks
- ✅ Best practice for production code

### Error Handling with Cleanup

```python
# Best: Context manager handles everything
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    try:
        page.goto("https://invalid-url")
    except Exception as e:
        print(f"Error: {e}")
    # Automatic cleanup!
```

## Best Practices

### ✅ DO:

- Use `with sync_playwright()` for automatic cleanup
- Use fill() for forms (faster)
- Use type() only when keyboard events are needed
- Check page.url or page.title() after navigation
- Close pages/contexts when done
- Use meaningful timeouts
- Handle navigation errors with try/except

### ❌ DON'T:

- Forget to close browsers (memory leaks!)
- Use type() everywhere (slower)
- Ignore navigation failures
- Use force=True unless necessary
- Create too many contexts (resource intensive)

## Common Patterns

### Pattern 1: Login Flow

```python
def login(page, username, password):
    page.goto("https://example.com/login")
    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard")
    return page.title() == "Dashboard"
```

### Pattern 2: Search and Verify

```python
def search(page, query):
    page.goto("https://example.com")
    page.type("input[name='search']", query)
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    return page.url
```

### Pattern 3: Multi-page Workflow

```python
def checkout(page):
    page.goto("https://example.com/cart")
    page.click("text=Proceed to Checkout")
    page.fill("input[name='address']", "123 Main St")
    page.click("text=Continue")
    page.click("text=Place Order")
    return "order" in page.url
```

## Debugging Tips

```python
# 1. Use headed mode
browser = p.chromium.launch(headless=False)

# 2. Add slow motion
browser = p.chromium.launch(headless=False, slow_mo=1000)

# 3. Use page.pause() for inspection
page.goto("https://example.com")
page.pause()  # Opens Playwright Inspector

# 4. Print page info
print(f"Current URL: {page.url}")
print(f"Title: {page.title()}")

# 5. Take screenshots
page.screenshot(path="debug.png")

# 6. Check response status
response = page.goto("https://example.com")
print(f"Status: {response.status}")

# 7. Wait for specific state
page.wait_for_load_state("networkidle")
```

## Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| TimeoutError | Element not found/visible | Check selector, increase timeout |
| Navigation failed | Invalid URL or network issue | Verify URL, check network |
| Element not clickable | Element covered or disabled | Wait for visibility, check CSS |
| fill() doesn't work | Not an input element | Use correct selector, verify element type |
| Browser not closing | Exception before close() | Use context manager or try/finally |

**Error Handling Example:**

```python
try:
    page.goto("https://example.com", timeout=5000)
    page.click("button", timeout=3000)
except TimeoutError:
    print("Element took too long to appear")
    page.screenshot(path="error.png")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Tips

**Speed Up Your Tests:**
- ✅ Use fill() instead of type() when possible
- ✅ Use "domcontentloaded" instead of "load" for faster navigation
- ✅ Reuse browser contexts when possible
- ✅ Run in headless mode for CI/CD
- ✅ Don't use unnecessary waits

```python
# Fast navigation
page.goto("https://example.com", wait_until="domcontentloaded")

# Fast form filling
page.fill("input", "value")  # Not type()

# Reuse context
context = browser.new_context()
page1 = context.new_page()
page2 = context.new_page()  # Share context

# Headless for speed
browser = p.chromium.launch(headless=True)
```

## pytest Integration

```python
# test_navigation.py
import pytest
from playwright.sync_api import Page, expect

def test_basic_navigation(page: Page):
    """Test basic navigation functionality."""
    page.goto("https://example.com")

    expect(page).to_have_title("Example Domain")
    expect(page).to_have_url("https://example.com/")

def test_form_interaction(page: Page):
    """Test form filling and submission."""
    page.goto("https://example.com/form")

    page.fill("input[name='name']", "John Doe")
    page.fill("input[name='email']", "john@example.com")
    page.click("button[type='submit']")

    expect(page).to_have_url("**/success")
    expect(page.locator("text=Thank you")).to_be_visible()

def test_navigation_history(page: Page):
    """Test browser history navigation."""
    page.goto("https://example.com")
    page.goto("https://playwright.dev")

    page.go_back()
    expect(page).to_have_url("https://example.com/")

    page.go_forward()
    expect(page).to_have_url("https://playwright.dev/")
```

## Practice Exercises

Complete the exercises in the `exercises/` folder:
- `exercise_01_navigation.py` - Practice navigation methods
- `exercise_02_form_interaction.py` - Form filling practice
- `exercise_03_multiple_pages.py` - Working with multiple pages
- `exercise_04_complete_workflow.py` - Build complete automation

Solutions available in `exercises/SOLUTIONS.md`.

## Quick Reference

### Navigation
```python
page.goto(url)                    # Navigate to URL
page.go_back()                    # Go back in history
page.go_forward()                 # Go forward in history
page.reload()                     # Reload current page
```

### Actions
```python
page.click(selector)              # Click element
page.fill(selector, value)        # Fill input (fast)
page.type(selector, text)         # Type text (with events)
```

### Page Info
```python
page.title()                      # Get page title
page.url                          # Get current URL
page.content()                    # Get page HTML
```

### Context & Pages
```python
context = browser.new_context()   # Create context
page = context.new_page()         # Create new page
context.pages                     # List all pages
page.close()                      # Close page
context.close()                   # Close context
browser.close()                   # Close browser
```

## Resources

- **Playwright Docs**: https://playwright.dev/python/docs/api/class-page
- **Navigation API**: https://playwright.dev/python/docs/api/class-page#page-goto
- **Actions API**: https://playwright.dev/python/docs/api/class-page#page-click
- **Context API**: https://playwright.dev/python/docs/api/class-browsercontext
- **Examples**: See `examples/` folder

## Next Steps

After completing this lecture:
1. ✅ Understand navigation methods (goto, go_back, go_forward, reload)
2. ✅ Know the Browser → Context → Page hierarchy
3. ✅ Can perform basic actions (click, fill, type)
4. ✅ Extract page information (title, URL, content)
5. ✅ Close browsers properly

**Ready for Lecture 15: Locators & Element Selection!** 🚀
