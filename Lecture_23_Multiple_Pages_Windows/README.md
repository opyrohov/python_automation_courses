# Lecture 23: Multiple Pages & Windows

## Overview
Master working with multiple browser pages, tabs, popups, and windows in Playwright - essential skills for testing modern web applications.

## Quick Reference

### Opening New Pages
```python
# Open a new page in same context
new_page = context.new_page()
new_page.goto("https://example.com")

# Work with multiple pages
page1 = context.new_page()
page2 = context.new_page()

page1.goto("https://site1.com")
page2.goto("https://site2.com")
```

### Handling Popups
```python
# Wait for popup and get reference
with page.expect_popup() as popup_info:
    page.locator("#open-popup").click()
popup = popup_info.value

# Work with popup
popup.wait_for_load_state()
print(popup.title())
popup.locator("#popup-button").click()
popup.close()
```

### Handling New Tabs (target="_blank")
```python
# Link opens in new tab
with page.expect_popup() as new_tab_info:
    page.locator("a[target='_blank']").click()
new_tab = new_tab_info.value

# Work with new tab
new_tab.wait_for_load_state()
expect(new_tab).to_have_url("**/new-page")
```

### Multiple Contexts (Isolated Sessions)
```python
# Create isolated contexts (like incognito)
context1 = browser.new_context()
context2 = browser.new_context()

# Each context has separate cookies, storage
page1 = context1.new_page()
page2 = context2.new_page()

# Login as different users
page1.goto("https://example.com/login")
page1.locator("#user").fill("user1")

page2.goto("https://example.com/login")
page2.locator("#user").fill("user2")
```

## Key Concepts

### Page vs Context vs Browser

| Level | Description | Isolation |
|-------|-------------|-----------|
| Browser | Browser instance (Chromium, Firefox) | Complete |
| Context | Session container (like incognito window) | Cookies, storage, cache |
| Page | Single tab/window | DOM only |

```python
browser = playwright.chromium.launch()

# Context = isolated session
context = browser.new_context()

# Page = tab within context
page = context.new_page()
```

### expect_popup() vs expect_page()

```python
# expect_popup() - for window.open() popups
with page.expect_popup() as popup_info:
    page.locator("#popup-btn").click()
popup = popup_info.value

# For programmatic page creation, use context.pages
initial_pages = len(context.pages)
page.locator("#create-tab").click()
# New page appears in context.pages
```

## Common Patterns

### Pattern 1: OAuth/Social Login Popup
```python
# Click "Login with Google" opens popup
with page.expect_popup() as popup_info:
    page.locator("#google-login").click()

popup = popup_info.value
popup.wait_for_load_state()

# Fill credentials in popup
popup.locator("#email").fill("user@gmail.com")
popup.locator("#next").click()
popup.locator("#password").fill("password")
popup.locator("#submit").click()

# Popup closes, back to main page
page.wait_for_load_state()
expect(page.locator(".user-profile")).to_be_visible()
```

### Pattern 2: PDF/Document in New Tab
```python
# Download link opens PDF in new tab
with page.expect_popup() as pdf_tab_info:
    page.locator("#view-pdf").click()

pdf_tab = pdf_tab_info.value
expect(pdf_tab).to_have_url(re.compile(r".*\.pdf"))

# Close PDF tab
pdf_tab.close()

# Continue on main page
page.locator("#next-step").click()
```

### Pattern 3: Multi-User Testing
```python
# Test chat between two users
context1 = browser.new_context()
context2 = browser.new_context()

user1_page = context1.new_page()
user2_page = context2.new_page()

# Both login to chat
user1_page.goto("https://chat.example.com")
user1_page.locator("#username").fill("Alice")
user1_page.locator("#join").click()

user2_page.goto("https://chat.example.com")
user2_page.locator("#username").fill("Bob")
user2_page.locator("#join").click()

# User1 sends message
user1_page.locator("#message").fill("Hello Bob!")
user1_page.locator("#send").click()

# User2 receives it
expect(user2_page.locator(".message")).to_contain_text("Hello Bob!")
```

### Pattern 4: Comparing Two Pages
```python
# Compare product on two different sites
page1 = context.new_page()
page2 = context.new_page()

page1.goto("https://store1.com/product/123")
page2.goto("https://store2.com/product/123")

price1 = page1.locator(".price").text_content()
price2 = page2.locator(".price").text_content()

print(f"Store 1: {price1}")
print(f"Store 2: {price2}")
```

### Pattern 5: Handling Multiple Popups
```python
# Click triggers multiple popups
popups = []

def handle_popup(popup):
    popups.append(popup)

page.on("popup", handle_popup)

page.locator("#multi-popup-btn").click()

# Wait for popups to load
for popup in popups:
    popup.wait_for_load_state()
    print(f"Popup URL: {popup.url}")
```

## Page Events

### Listening to Page Events
```python
# New page created in context
def on_page(page):
    print(f"New page: {page.url}")

context.on("page", on_page)

# Page closed
def on_close():
    print("Page was closed")

page.on("close", on_close)

# Console messages
def on_console(msg):
    print(f"Console: {msg.text}")

page.on("console", on_console)
```

### Waiting for Page Events
```python
# Wait for new page event
with context.expect_page() as new_page_info:
    page.locator("#open-new").click()
new_page = new_page_info.value

# Wait for page to close
with page.expect_close() as close_info:
    page.locator("#self-close").click()
```

## Working with context.pages

```python
# Get all pages in context
all_pages = context.pages
print(f"Total pages: {len(all_pages)}")

# Find page by URL
for p in context.pages:
    if "dashboard" in p.url:
        dashboard_page = p
        break

# Find page by title
for p in context.pages:
    if p.title() == "Settings":
        settings_page = p
        break
```

## Best Practices

### DO
- Use `expect_popup()` for window.open() popups
- Wait for load state on new pages
- Close popups when done to free resources
- Use separate contexts for isolated sessions
- Handle popup events for multiple popups

### DON'T
- Assume popup opens instantly
- Forget to close unused pages
- Mix users in same context (cookies shared)
- Ignore popup blockers in browser settings
- Leave orphaned pages open

## Common Pitfalls

### Popup Blocked
```python
# ❌ Popup might be blocked
page.locator("#popup-btn").click()
# Nothing happens...

# ✅ Use expect_popup to wait and capture
with page.expect_popup() as popup_info:
    page.locator("#popup-btn").click()
popup = popup_info.value
```

### Wrong Page Reference
```python
# ❌ Working on wrong page after popup
popup = ...  # got popup
popup.locator("#submit").click()  # popup closes
popup.locator("#next").click()  # Error! Popup is closed

# ✅ Switch to correct page
popup.locator("#submit").click()  # popup closes
page.locator("#next").click()  # back to main page
```

### Context vs Page Isolation
```python
# ❌ Same context = shared cookies
page1 = context.new_page()
page2 = context.new_page()
# Login on page1 affects page2!

# ✅ Different contexts = isolated
context1 = browser.new_context()
context2 = browser.new_context()
page1 = context1.new_page()
page2 = context2.new_page()
# Completely separate sessions
```

## Examples Included
1. `01_new_pages_tabs.py` - Opening and managing multiple pages
2. `02_popup_handling.py` - Handling popups and new windows
3. `03_multiple_contexts.py` - Isolated browser contexts
4. `04_page_events.py` - Page event listeners
5. `05_real_world_scenarios.py` - OAuth, multi-user testing

## Resources
- [Multiple Pages Documentation](https://playwright.dev/python/docs/pages)
- [Browser Contexts](https://playwright.dev/python/docs/browser-contexts)
- [Page Events](https://playwright.dev/python/docs/api/class-page#events)
