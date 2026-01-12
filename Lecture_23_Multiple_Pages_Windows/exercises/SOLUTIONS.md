# Solutions - Lecture 23: Multiple Pages & Windows

## Exercise 1: Popup Handling

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as popup_info:
        page.locator("a[href='/windows/new']").click()
    popup = popup_info.value

    popup.wait_for_load_state()
    popup_text = popup.locator("h3").text_content()
    assert popup_text == "New Window"

    popup.close()
    expect(page.locator("h3")).to_have_text("Opening a new window")
    browser.close()
```

### Key Points:
- Use `with page.expect_popup() as popup_info:` to capture new windows
- `popup_info.value` gives you the Page object for the popup
- Always call `wait_for_load_state()` after capturing a popup

---

## Exercise 2: Multi-User Testing

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    user1_context = browser.new_context()
    user2_context = browser.new_context()

    user1_page = user1_context.new_page()
    user2_page = user2_context.new_page()

    # User 1 logs in
    user1_page.goto("https://the-internet.herokuapp.com/login")
    user1_page.locator("#username").fill("tomsmith")
    user1_page.locator("#password").fill("SuperSecretPassword!")
    user1_page.locator("button[type='submit']").click()

    expect(user1_page.locator(".flash.success")).to_be_visible()

    # User 2 is NOT logged in
    user2_page.goto("https://the-internet.herokuapp.com/login")
    expect(user2_page.locator("#username")).to_be_visible()

    user1_context.close()
    user2_context.close()
    browser.close()
```

### Key Points:
- Use `browser.new_context()` for each user
- Different contexts = completely isolated sessions

---

## Exercise 3: Real-Time Collaboration (Advanced)

```python
from playwright.sync_api import sync_playwright, expect

def login_user(page, username, password):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    page.wait_for_load_state()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    admin_ctx = browser.new_context()
    user1_ctx = browser.new_context()
    user2_ctx = browser.new_context()

    admin = admin_ctx.new_page()
    user1 = user1_ctx.new_page()
    user2 = user2_ctx.new_page()

    login_user(admin, "tomsmith", "SuperSecretPassword!")
    login_user(user1, "tomsmith", "SuperSecretPassword!")
    login_user(user2, "tomsmith", "SuperSecretPassword!")

    # All have independent sessions
    expect(admin.locator("h2")).to_contain_text("Secure Area")
    expect(user1.locator("h2")).to_contain_text("Secure Area")
    expect(user2.locator("h2")).to_contain_text("Secure Area")

    # Admin logs out - others stay logged in
    admin.locator("a[href='/logout']").click()
    user1.reload()
    user2.reload()
    expect(user1.locator("h2")).to_contain_text("Secure Area")
    expect(user2.locator("h2")).to_contain_text("Secure Area")

    admin_ctx.close()
    user1_ctx.close()
    user2_ctx.close()
    browser.close()
```

---

## Bonus: expect_popup with Timeout

```python
# Custom timeout (5 seconds)
try:
    with page.expect_popup(timeout=5000) as popup_info:
        page.locator("#popup-btn").click()
    popup = popup_info.value
    popup.wait_for_load_state()
except Exception as e:
    print(f"Timeout: {e}")
```

## Bonus: context.expect_page()

```python
# Captures ANY new page in context
with context.expect_page() as new_page_info:
    page.locator("#open-new").click()

new_page = new_page_info.value
new_page.wait_for_load_state()
print(f"Total pages: {len(context.pages)}")
```

## Bonus: Async Multi-User

```python
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # Create contexts in parallel
        ctx1, ctx2 = await asyncio.gather(
            browser.new_context(),
            browser.new_context()
        )

        user1, user2 = await asyncio.gather(
            ctx1.new_page(),
            ctx2.new_page()
        )

        # Navigate in parallel (faster!)
        await asyncio.gather(
            user1.goto("https://example.com"),
            user2.goto("https://example.com")
        )

        await browser.close()

asyncio.run(main())
```

---

## Common Mistakes

### Not waiting for popup
```python
# WRONG
popup = popup_info.value
popup.click("#btn")  # May fail!

# CORRECT
popup = popup_info.value
popup.wait_for_load_state()
popup.click("#btn")
```

### Same context for different users
```python
# WRONG - shared session
user1 = context.new_page()
user2 = context.new_page()

# CORRECT - isolated
user1 = ctx1.new_page()
user2 = ctx2.new_page()
```
