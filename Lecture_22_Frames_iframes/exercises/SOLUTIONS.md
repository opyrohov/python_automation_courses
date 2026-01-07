# Solutions - Lecture 22: Frames & iframes

## Exercise 1: Basic iframe Interaction

```python
"""Exercise 1 Solution: Basic iframe Interaction"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: Basic iframe Interaction ===\n")

    # Navigate to the page
    page.goto("https://the-internet.herokuapp.com/iframe")
    print("1. Navigated to iframe page")

    # Wait for the iframe to be visible
    expect(page.locator("#mce_0_ifr")).to_be_visible()
    print("2. iframe is visible")

    # Get the frame locator
    frame = page.frame_locator("#mce_0_ifr")
    print("3. Got frame locator")

    # Get the editor body element inside iframe
    editor = frame.locator("#tinymce")
    expect(editor).to_be_visible()
    print("4. Editor body is visible")

    # Clear existing content
    editor.clear()
    print("5. Cleared existing content")

    # Fill with new text
    editor.fill("Hello, I am learning Playwright iframes!")
    print("6. Filled with new text")

    # Verify the text
    expect(editor).to_have_text("Hello, I am learning Playwright iframes!")
    print("7. Text verified successfully!")

    print("\n✓ Exercise 1 completed!")
    browser.close()
```

### Key Points:
- Use `page.frame_locator("#mce_0_ifr")` to access the iframe
- Chain `.locator("#tinymce")` to find elements inside
- Use `expect()` for waiting and verification
- No need to "switch back" - just use `page.locator()` for main page elements

---

## Exercise 2: Nested Frames Navigation

```python
"""Exercise 2 Solution: Nested Frames Navigation"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 2: Nested Frames Navigation ===\n")

    # Navigate to the nested frames page
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    print("1. Navigated to nested frames page")

    # Access the top frame
    top_frame = page.frame_locator("frame[name='frame-top']")
    print("2. Accessed top frame")

    # Access the middle frame (nested inside top)
    middle_frame = top_frame.frame_locator("frame[name='frame-middle']")
    print("3. Accessed middle frame (nested)")

    # Get the content element and its text
    content = middle_frame.locator("#content")
    middle_text = content.text_content()
    print(f"4. Middle frame content: '{middle_text}'")

    # Verify it contains "MIDDLE"
    assert "MIDDLE" in middle_text, f"Expected 'MIDDLE' in text, got: {middle_text}"
    print("5. Verified content contains 'MIDDLE'")

    # Access the bottom frame and get its content
    bottom_frame = page.frame_locator("frame[name='frame-bottom']")
    bottom_text = bottom_frame.locator("body").text_content().strip()
    print(f"6. Bottom frame content: '{bottom_text}'")

    # Bonus: Access left and right frames too
    left_frame = top_frame.frame_locator("frame[name='frame-left']")
    left_text = left_frame.locator("body").text_content().strip()
    print(f"7. Left frame content: '{left_text}'")

    right_frame = top_frame.frame_locator("frame[name='frame-right']")
    right_text = right_frame.locator("body").text_content().strip()
    print(f"8. Right frame content: '{right_text}'")

    print("\n✓ Exercise 2 completed!")
    browser.close()
```

### Key Points:
- Chain `frame_locator()` calls for nested frames
- `top_frame.frame_locator("frame[name='frame-middle']")` accesses nested frame
- Use `frame[name='...']` selector for frames with name attribute
- The structure is: page → top_frame → left/middle/right frames

---

## Bonus Challenge Solutions

### Challenge 1: Count and List All Frames

```python
"""Bonus: List all frames on nested frames page"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # Get all frames using frame() API
    all_frames = page.frames
    print(f"Total frames: {len(all_frames)}")

    for frame in all_frames:
        name = frame.name or "(main)"
        parent = frame.parent_frame
        parent_name = parent.name if parent else "(none)"
        print(f"  Frame: {name}, Parent: {parent_name}")

    browser.close()
```

### Challenge 2: Extract All Text from All Frames

```python
"""Bonus: Extract text from all frames"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    frame_contents = {}

    # Top frame children
    top = page.frame_locator("frame[name='frame-top']")
    for name in ["frame-left", "frame-middle", "frame-right"]:
        frame = top.frame_locator(f"frame[name='{name}']")
        text = frame.locator("body").text_content().strip()
        frame_contents[name] = text

    # Bottom frame
    bottom = page.frame_locator("frame[name='frame-bottom']")
    frame_contents["frame-bottom"] = bottom.locator("body").text_content().strip()

    # Print all contents
    for name, content in frame_contents.items():
        print(f"{name}: {content}")

    browser.close()
```

---

## Common Mistakes to Avoid

### Mistake 1: Accessing iframe content directly
```python
# ❌ WRONG - This won't find elements inside iframe
page.locator("#tinymce").click()

# ✅ CORRECT - Use frame_locator first
page.frame_locator("#mce_0_ifr").locator("#tinymce").click()
```

### Mistake 2: Not waiting for iframe
```python
# ❌ WRONG - May fail if iframe not loaded yet
frame = page.frame_locator("#dynamic-iframe")
frame.locator("button").click()

# ✅ CORRECT - Wait first
expect(page.locator("#dynamic-iframe")).to_be_attached()
frame = page.frame_locator("#dynamic-iframe")
expect(frame.locator("button")).to_be_visible()
frame.locator("button").click()
```

### Mistake 3: Using stale frame reference after navigation
```python
# ❌ WRONG - Frame reference is stale after navigation
frame = page.frame_locator("#iframe")
page.reload()
frame.locator("button").click()  # May fail!

# ✅ CORRECT - Re-query after navigation
page.reload()
frame = page.frame_locator("#iframe")
frame.locator("button").click()
```
