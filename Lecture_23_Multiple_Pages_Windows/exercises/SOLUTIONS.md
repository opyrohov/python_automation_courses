# Solutions - Lecture 23: Multiple Pages & Windows

## Exercise 1: Popup Handling

```python
"""Exercise 1 Solution: Popup Handling"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Popup Handling ===\n")

    # Navigate to the windows page
    page.goto("https://the-internet.herokuapp.com/windows")
    print("1. Navigated to windows page")

    # Click the link and capture popup
    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    popup = popup_info.value
    print("2. Popup captured")

    # Wait for popup to load
    popup.wait_for_load_state()
    print("3. Popup loaded")

    # Get text from h3 in popup
    popup_text = popup.locator("h3").text_content()
    print(f"4. Popup text: '{popup_text}'")

    # Verify the text
    assert popup_text == "New Window", f"Expected 'New Window', got '{popup_text}'"
    print("5. Text verified!")

    # Close the popup
    popup.close()
    print("6. Popup closed")

    # Verify main page is still accessible
    expect(page.locator("h3")).to_have_text("Opening a new window")
    print("7. Main page verified")

    print("\n✓ Exercise 1 completed!")
    browser.close()
```

### Key Points:
- Use `with page.expect_popup() as popup_info:` to capture new windows
- `popup_info.value` gives you the Page object for the popup
- Always call `wait_for_load_state()` after capturing a popup
- After closing popup, you're automatically back on the main page

---

## Exercise 2: Multi-User Testing

```python
"""Exercise 2 Solution: Multi-User Testing"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Exercise 2: Multi-User Testing ===\n")

    # Create two separate contexts
    user1_context = browser.new_context()
    user2_context = browser.new_context()
    print("1. Created two isolated contexts")

    # Create pages in each context
    user1_page = user1_context.new_page()
    user2_page = user2_context.new_page()
    print("2. Created pages in each context")

    # User 1 logs in
    user1_page.goto("https://the-internet.herokuapp.com/login")
    user1_page.locator("#username").fill("tomsmith")
    user1_page.locator("#password").fill("SuperSecretPassword!")
    user1_page.locator("button[type='submit']").click()
    print("3. User 1 submitted login form")

    # Verify User 1 is logged in
    expect(user1_page.locator(".flash.success")).to_be_visible()
    print("4. ✓ User 1 is logged in (sees success message)")

    # User 2 goes to login page
    user2_page.goto("https://the-internet.herokuapp.com/login")
    print("5. User 2 navigated to login page")

    # Verify User 2 sees login form (NOT logged in)
    expect(user2_page.locator("#username")).to_be_visible()
    expect(user2_page.locator("#password")).to_be_visible()
    print("6. ✓ User 2 sees login form (not logged in)")

    # Bonus: Verify User 1 is still logged in after User 2 visited
    user1_page.reload()
    expect(user1_page.locator(".flash.success")).to_be_visible()
    print("7. ✓ User 1 still logged in (session isolated)")

    # Clean up
    user1_context.close()
    user2_context.close()
    print("8. Contexts closed")

    print("\n✓ Exercise 2 completed - contexts are isolated!")
    browser.close()
```

### Key Points:
- Use `browser.new_context()` for each user/session
- Different contexts have separate cookies, storage, cache
- Pages in the same context share session (like tabs in same browser window)
- Pages in different contexts are completely isolated
- Always close contexts when done to free resources

---

## Bonus Challenges

### Challenge 1: Multiple Popups

```python
"""Bonus: Handle multiple popups"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/windows")

    popups = []

    def capture_popup(popup):
        popups.append(popup)
        print(f"Captured popup: {popup.url}")

    page.on("popup", capture_popup)

    # Open multiple popups
    for _ in range(3):
        page.locator("a[href='/windows/new']").click()
        page.wait_for_timeout(500)

    print(f"Total popups: {len(popups)}")

    # Close all popups
    for popup in popups:
        popup.close()

    browser.close()
```

### Challenge 2: Page Event Logging

```python
"""Bonus: Log all page events"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    def on_page(page):
        print(f"[EVENT] New page: {page.url or 'blank'}")

        def on_load():
            print(f"[EVENT] Page loaded: {page.url}")

        def on_close():
            print(f"[EVENT] Page closed: {page.url}")

        page.on("load", on_load)
        page.on("close", on_close)

    context.on("page", on_page)

    page1 = context.new_page()
    page1.goto("https://example.com")

    page2 = context.new_page()
    page2.goto("https://the-internet.herokuapp.com")

    page2.close()
    page1.close()

    browser.close()
```

---

## Common Mistakes to Avoid

### Mistake 1: Not waiting for popup
```python
# ❌ WRONG - popup may not be loaded
with page.expect_popup() as popup_info:
    page.click("#popup-btn")
popup = popup_info.value
popup.locator("#element").click()  # May fail!

# ✅ CORRECT - wait for load
with page.expect_popup() as popup_info:
    page.click("#popup-btn")
popup = popup_info.value
popup.wait_for_load_state()  # Wait!
popup.locator("#element").click()  # Safe
```

### Mistake 2: Same context for different users
```python
# ❌ WRONG - users share session
context = browser.new_context()
user1 = context.new_page()
user2 = context.new_page()
# If user1 logs in, user2 is also logged in!

# ✅ CORRECT - separate contexts
ctx1 = browser.new_context()
ctx2 = browser.new_context()
user1 = ctx1.new_page()
user2 = ctx2.new_page()
# Completely isolated sessions
```

### Mistake 3: Using closed page
```python
# ❌ WRONG - popup is closed
popup.locator("#submit").click()  # This closes popup
popup.locator("#next").click()  # Error! Popup is gone

# ✅ CORRECT - continue on main page
popup.locator("#submit").click()  # Closes popup
page.locator("#next").click()  # Use main page
```
