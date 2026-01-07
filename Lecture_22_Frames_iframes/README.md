# Lecture 22: Frames & iframes

## Overview
Master working with frames and iframes in Playwright - a crucial skill for handling embedded content, ads, payment forms, and legacy applications.

## Quick Reference

### Accessing iframes
```python
# Method 1: frame_locator() - Recommended
frame = page.frame_locator("#my-iframe")
frame.locator("button").click()

# Method 2: By name or URL
frame = page.frame_locator("iframe[name='editor']")
frame = page.frame_locator("iframe[src*='payment']")

# Method 3: Using frame() with name
frame = page.frame("frame-name")
```

### Basic iframe Operations
```python
# Click button inside iframe
page.frame_locator("#iframe").locator("button").click()

# Fill form inside iframe
page.frame_locator("#iframe").locator("input").fill("Hello")

# Get text from iframe
text = page.frame_locator("#iframe").locator("h1").text_content()

# Check element in iframe
from playwright.sync_api import expect
expect(page.frame_locator("#iframe").locator(".success")).to_be_visible()
```

### Nested iframes
```python
# Access nested iframe (iframe inside iframe)
outer = page.frame_locator("#outer-frame")
inner = outer.frame_locator("#inner-frame")
inner.locator("button").click()

# Chain multiple levels
page.frame_locator("#level1").frame_locator("#level2").frame_locator("#level3").locator("button").click()
```

### Multiple iframes
```python
# Get all iframes
iframes = page.locator("iframe").all()
print(f"Found {len(iframes)} iframes")

# Work with specific iframe by index
first_frame = page.frame_locator("iframe").first
last_frame = page.frame_locator("iframe").last
second_frame = page.frame_locator("iframe").nth(1)

# Filter iframes
payment_frame = page.frame_locator("iframe[src*='payment']")
```

## Key Concepts

### frame_locator() vs frame()

| Feature | frame_locator() | frame() |
|---------|-----------------|---------|
| Returns | FrameLocator | Frame |
| Chaining | Yes | No |
| Auto-waiting | Yes | No |
| Recommended | Yes | Legacy |

```python
# frame_locator() - Modern, chainable
page.frame_locator("#iframe").locator("button").click()

# frame() - Direct frame access
frame = page.frame("frame-name")
frame.click("button")  # Different syntax
```

### Understanding iframe Structure
```html
<!-- Parent page -->
<html>
  <body>
    <iframe id="my-iframe" src="embedded.html">
      <!-- iframe content (separate document) -->
      <html>
        <body>
          <button>Click Me</button>
        </body>
      </html>
    </iframe>
  </body>
</html>
```

## Common Patterns

### Pattern 1: Payment Form in iframe
```python
# Wait for payment iframe to load
payment = page.frame_locator("iframe[name='payment']")

# Fill card details
payment.locator("#card-number").fill("4111111111111111")
payment.locator("#expiry").fill("12/25")
payment.locator("#cvv").fill("123")
payment.locator("#submit").click()

# Verify success (back in main page)
expect(page.locator(".payment-success")).to_be_visible()
```

### Pattern 2: Rich Text Editor (TinyMCE, CKEditor)
```python
# TinyMCE is typically in an iframe
editor = page.frame_locator("#tinymce_ifr")

# Type in editor
editor.locator("body").fill("Hello World")

# Or use keyboard
editor.locator("body").press_sequentially("Hello World")

# Apply formatting - often in main page
page.locator("#bold-btn").click()
```

### Pattern 3: Handling Ads/Third-party Content
```python
# Check if ad iframe exists
ad_frame = page.frame_locator("iframe[id*='google_ads']")
if ad_frame.locator("body").count() > 0:
    print("Ad loaded")

# Close ad if there's a close button
try:
    ad_frame.locator(".close-btn").click(timeout=2000)
except:
    pass  # No close button or ad not present
```

### Pattern 4: Waiting for iframe Content
```python
# Wait for iframe to be attached
expect(page.locator("#my-iframe")).to_be_attached()

# Wait for content inside iframe
frame = page.frame_locator("#my-iframe")
expect(frame.locator(".content")).to_be_visible()

# Wait for iframe to load specific content
expect(frame.locator("h1")).to_have_text("Welcome")
```

### Pattern 5: Switching Between iframe and Main Page
```python
# Work in iframe
frame = page.frame_locator("#my-iframe")
frame.locator("button").click()

# Work in main page (no need to "switch back")
page.locator("#main-button").click()

# Work in iframe again
frame.locator("input").fill("text")
```

### Pattern 6: Dynamic iframes
```python
# Wait for iframe to appear
page.locator("#load-iframe-btn").click()
expect(page.locator("#dynamic-iframe")).to_be_attached()

# Now access it
frame = page.frame_locator("#dynamic-iframe")
expect(frame.locator(".loaded")).to_be_visible()
```

## Working with frame() API

### Direct Frame Access
```python
# Get all frames
all_frames = page.frames
print(f"Page has {len(all_frames)} frames")

# Get frame by name
frame = page.frame("iframe-name")

# Get frame by URL pattern
frame = page.frame(url=lambda url: "payment" in url)

# Get main frame
main = page.main_frame
```

### Frame Properties
```python
frame = page.frame("my-frame")

# Get frame URL
print(frame.url)

# Get frame name
print(frame.name)

# Get parent frame
parent = frame.parent_frame

# Check if it's main frame
is_main = frame == page.main_frame
```

## iframe Locator Strategies

### By ID
```python
frame = page.frame_locator("#iframe-id")
```

### By Name
```python
frame = page.frame_locator("iframe[name='editor']")
```

### By Source URL
```python
# Exact match
frame = page.frame_locator("iframe[src='https://example.com/embed']")

# Partial match
frame = page.frame_locator("iframe[src*='youtube']")
frame = page.frame_locator("iframe[src*='payment']")
```

### By Title
```python
frame = page.frame_locator("iframe[title='Video Player']")
```

### By Index
```python
# First iframe
frame = page.frame_locator("iframe").first

# Third iframe
frame = page.frame_locator("iframe").nth(2)
```

## Best Practices

### DO
- Use `frame_locator()` for modern, chainable syntax
- Wait for iframe to be attached before accessing
- Use specific selectors (id, name, src) when possible
- Handle iframe load errors gracefully
- Re-query frame after page navigation

### DON'T
- Assume iframe is immediately available
- Use generic `iframe` selector when multiple exist
- Forget that iframe content is a separate document
- Try to directly access elements without frame_locator
- Hardcode iframe indices

## Common Pitfalls

### Cross-Origin iframes
```python
# Cross-origin iframes have limited access
# You can interact but may not read all content
frame = page.frame_locator("iframe[src='https://other-domain.com']")

# This works - interaction
frame.locator("button").click()

# This might fail - reading content from different origin
# text = frame.locator("body").text_content()  # May throw
```

### iframe Not Found
```python
# BAD - no waiting
frame = page.frame_locator("#iframe")
frame.locator("button").click()  # May fail if iframe not loaded

# GOOD - wait for iframe
expect(page.locator("#iframe")).to_be_attached()
frame = page.frame_locator("#iframe")
frame.locator("button").click()
```

### Stale Frame Reference
```python
# BAD - frame reference after navigation
frame = page.frame_locator("#iframe")
page.reload()
frame.locator("button").click()  # Stale!

# GOOD - re-query after navigation
page.reload()
frame = page.frame_locator("#iframe")
frame.locator("button").click()
```

## Examples Included
1. `01_basic_iframe.py` - Basic iframe access and interaction
2. `02_nested_iframes.py` - Working with nested iframes
3. `03_multiple_iframes.py` - Handling multiple iframes on page
4. `04_dynamic_iframes.py` - Dynamic iframe loading and waiting
5. `05_real_world_scenarios.py` - Payment forms, editors, ads

## Resources
- [Playwright Frames Documentation](https://playwright.dev/python/docs/frames)
- [FrameLocator API](https://playwright.dev/python/docs/api/class-framelocator)
- [Frame API](https://playwright.dev/python/docs/api/class-frame)
