# Exercise Solutions - Lecture 20: Assertions in Playwright

## Exercise 1: Visibility and Text Assertions

```python
from playwright.sync_api import sync_playwright, expect

def visibility_text_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

        # Solution 1: Assert start button is visible
        expect(page.locator("#start button")).to_be_visible()

        # Solution 2: Assert finish element is hidden
        expect(page.locator("#finish")).to_be_hidden()

        # Click the start button
        page.locator("#start button").click()

        # Solution 3: Assert finish element becomes visible
        expect(page.locator("#finish")).to_be_visible()

        # Solution 4: Assert text is "Hello World!"
        expect(page.locator("#finish h4")).to_have_text("Hello World!")

        # Solution 5: Assert loading is hidden
        expect(page.locator("#loading")).to_be_hidden()

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 2: Count and URL Assertions

```python
from playwright.sync_api import sync_playwright, expect

def count_url_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # Solution 1: Assert URL pattern
        expect(page).to_have_url("**/add_remove_elements/")

        # Solution 2: Assert initial count is 0
        expect(page.locator(".added-manually")).to_have_count(0)

        # Add 3 elements
        for i in range(3):
            page.locator("button").first.click()

        # Solution 3: Assert count is now 3
        expect(page.locator(".added-manually")).to_have_count(3)

        # Solution 4: Assert each element is visible
        for i in range(3):
            expect(page.locator(".added-manually").nth(i)).to_be_visible()

        # Remove one element
        page.locator(".added-manually").first.click()

        # Solution 5: Assert count is now 2
        expect(page.locator(".added-manually")).to_have_count(2)

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Key Takeaways

### Visibility Assertions
- **to_be_visible()** - Element is visible on the page
- **to_be_hidden()** - Element is not visible
- **to_be_attached()** - Element is in DOM
- **to_be_enabled()** - Element is enabled
- **to_be_disabled()** - Element is disabled

### Text Assertions
- **to_have_text()** - Exact text match
- **to_contain_text()** - Partial text match
- **to_have_value()** - Input field value

### Attribute Assertions
- **to_have_attribute()** - Attribute with specific value
- **to_have_class()** - CSS class
- **to_have_id()** - Element ID
- **to_have_css()** - CSS property value

### Count Assertions
- **to_have_count()** - Exact number of elements
- Works with dynamic content - auto-waits for count to match

### URL & Title Assertions
- **to_have_url()** - Page URL (supports wildcards and regex)
- **to_have_title()** - Page title

### Best Practices
- ✅ Use `expect()` for all assertions (has auto-waiting)
- ✅ Be specific about what you're asserting
- ✅ Use negative assertions (not_to_be_visible) when needed
- ✅ Combine multiple assertions for robust verification
- ❌ Don't use Python's `assert` for element checks
- ❌ Don't over-assert trivial implementation details
