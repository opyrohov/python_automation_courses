# Exercise Solutions - Lecture 19: Wait Strategies

## Exercise 1: Waiting for Dynamic Content

```python
from playwright.sync_api import sync_playwright, expect

def dynamic_content_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

        # Solution 1: Click the start button
        page.locator("#start button").click()

        # Solution 2: Wait for loading to be hidden
        page.wait_for_selector("#loading", state="hidden")

        # Solution 3: Wait for finish element to be visible
        page.wait_for_selector("#finish", state="visible")

        # Solution 4: Verify text using expect()
        expect(page.locator("#finish h4")).to_have_text("Hello World!")

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 2: Custom Wait Conditions

```python
from playwright.sync_api import sync_playwright

def custom_wait_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # Solution 1: Add 3 elements
        for i in range(3):
            page.locator("button").first.click()

        # Solution 2: Wait for exactly 3 elements
        page.wait_for_function(
            "() => document.querySelectorAll('.added-manually').length === 3"
        )

        # Solution 3: Verify count
        count = page.locator(".added-manually").count()
        assert count == 3, f"Expected 3 elements, got {count}"

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Key Takeaways

### Auto-Waiting
- Playwright automatically waits for elements to be actionable before actions
- `expect()` assertions auto-wait and retry
- No explicit waits needed for most standard interactions

### wait_for_selector()
- **state="visible"** - Wait for element to appear (default)
- **state="hidden"** - Wait for element to disappear
- **state="attached"** - Wait for element in DOM
- **state="detached"** - Wait for element removal

### wait_for_load_state()
- **"load"** - Page and resources loaded
- **"domcontentloaded"** - DOM ready (faster)
- **"networkidle"** - No network activity (for SPAs)

### Custom Waits
- **wait_for_function()** - Wait for JavaScript conditions
- Can check element counts, text content, attributes, styles
- Pass arguments for dynamic conditions

### Timeout Configuration
- **set_default_timeout()** - Set global timeout
- **timeout parameter** - Per-action timeout
- **Avoid wait_for_timeout()** - Use conditional waits instead

### Best Practices
- ✅ Trust auto-waiting for standard actions
- ✅ Use `expect()` for assertions
- ✅ Wait for specific conditions
- ❌ Avoid `wait_for_timeout()` (anti-pattern)
- ❌ Don't add unnecessary explicit waits
