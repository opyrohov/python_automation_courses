# Solutions - Lecture 26: Cookies & Local Storage

## Exercise 1: Cookie Management

```python
"""Exercise 1 Solution: Cookie Management"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Cookie Management ===\n")

    # Navigate to the site
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Add "user_id" cookie
    context.add_cookies([{
        "name": "user_id",
        "value": "test_user_123",
        "domain": "the-internet.herokuapp.com",
        "path": "/"
    }])
    print("2. Added 'user_id' cookie")

    # Add "session_token" cookie with httpOnly=True
    context.add_cookies([{
        "name": "session_token",
        "value": "abc123xyz",
        "domain": "the-internet.herokuapp.com",
        "path": "/",
        "httpOnly": True
    }])
    print("3. Added 'session_token' cookie with httpOnly=True")

    # Verify cookies were added
    cookies = context.cookies()
    print(f"\n4. Total cookies: {len(cookies)}")

    # Print all cookie names
    print("5. All cookie names:")
    for cookie in cookies:
        http_only = " (httpOnly)" if cookie.get("httpOnly") else ""
        print(f"   - {cookie['name']}: {cookie['value']}{http_only}")

    # Remove only "user_id" cookie
    all_cookies = context.cookies()
    keep_cookies = [c for c in all_cookies if c["name"] != "user_id"]
    context.clear_cookies()
    context.add_cookies(keep_cookies)
    print("\n6. Removed 'user_id' cookie")

    # Verify results
    remaining = context.cookies()
    user_id_exists = any(c["name"] == "user_id" for c in remaining)
    session_token_exists = any(c["name"] == "session_token" for c in remaining)

    print("\n7. Verification:")
    print(f"   - 'user_id' exists: {user_id_exists} (should be False)")
    print(f"   - 'session_token' exists: {session_token_exists} (should be True)")

    if not user_id_exists and session_token_exists:
        print("\n✓ Exercise completed successfully!")
    else:
        print("\n✗ Something went wrong")

    # BONUS: Cookie with expiration
    print("\n--- BONUS ---")
    one_hour_from_now = time.time() + 3600
    context.add_cookies([{
        "name": "expires_soon",
        "value": "temp_data",
        "domain": "the-internet.herokuapp.com",
        "path": "/",
        "expires": one_hour_from_now
    }])
    print(f"Added cookie expiring at: {one_hour_from_now}")

    # Print full cookie details
    print("\nFull cookie details:")
    for cookie in context.cookies():
        print(f"\n  {cookie['name']}:")
        print(f"    value: {cookie['value']}")
        print(f"    domain: {cookie['domain']}")
        print(f"    path: {cookie['path']}")
        print(f"    httpOnly: {cookie.get('httpOnly', False)}")
        print(f"    secure: {cookie.get('secure', False)}")
        if cookie.get('expires'):
            print(f"    expires: {cookie['expires']}")

    context.close()
    browser.close()
```

### Key Points:
- Use `context.add_cookies([{...}])` with list of cookie dicts
- To remove specific cookies: filter, clear, re-add
- `httpOnly` cookies can't be accessed via JavaScript
- Use `time.time() + seconds` for expiration timestamps

---

## Exercise 2: Storage Manipulation

```python
"""Exercise 2 Solution: Storage Manipulation"""
from playwright.sync_api import sync_playwright
import json
import os

STATE_FILE = "exercise_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 2: Storage Manipulation ===\n")

    # Navigate to the site
    page.goto("https://the-internet.herokuapp.com/")
    print("1. Navigated to the-internet.herokuapp.com")

    # Set localStorage items
    page.evaluate("localStorage.setItem('theme', 'dark')")
    page.evaluate("localStorage.setItem('language', 'en')")

    user_data = {"name": "Test", "level": 5}
    page.evaluate(f"localStorage.setItem('user_data', '{json.dumps(user_data)}')")
    print("2. Set localStorage items")

    # Verify localStorage items
    theme = page.evaluate("localStorage.getItem('theme')")
    language = page.evaluate("localStorage.getItem('language')")
    user_data_str = page.evaluate("localStorage.getItem('user_data')")
    user_data_parsed = json.loads(user_data_str)

    print("\n3. Verification of localStorage:")
    print(f"   - theme: {theme}")
    print(f"   - language: {language}")
    print(f"   - user_data: {user_data_parsed}")

    # Set sessionStorage items
    page.evaluate("sessionStorage.setItem('current_page', 'home')")
    page.evaluate("sessionStorage.setItem('visit_count', '1')")
    print("\n4. Set sessionStorage items")

    # Check sessionStorage before navigation
    session_before = page.evaluate("sessionStorage.length")
    print(f"   sessionStorage items before navigation: {session_before}")

    # Navigate to /login
    page.goto("https://the-internet.herokuapp.com/login")
    print("\n5. Navigated to /login")

    # Check if localStorage persists
    theme_after = page.evaluate("localStorage.getItem('theme')")
    print(f"   localStorage 'theme' after navigation: {theme_after}")
    print("   ✓ localStorage persists across navigation!")

    # Check sessionStorage after navigation
    session_after = page.evaluate("sessionStorage.length")
    print(f"   sessionStorage items after navigation: {session_after}")
    print("   ✓ sessionStorage also persists (same tab)")

    # Get all localStorage as dictionary
    all_local = page.evaluate("""() => {
        const data = {};
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            data[key] = localStorage.getItem(key);
        }
        return data;
    }""")
    print(f"\n6. All localStorage items: {all_local}")

    # Clear only sessionStorage
    page.evaluate("sessionStorage.clear()")
    print("\n7. Cleared sessionStorage")

    # Verify final state
    local_count = page.evaluate("localStorage.length")
    session_count = page.evaluate("sessionStorage.length")
    print(f"\n8. Final state:")
    print(f"   - localStorage items: {local_count} (should be 3)")
    print(f"   - sessionStorage items: {session_count} (should be 0)")

    if local_count == 3 and session_count == 0:
        print("\n✓ Exercise completed successfully!")

    # BONUS: Save and restore storage state
    print("\n--- BONUS: Storage State ---")

    # Save complete state
    context.storage_state(path=STATE_FILE)
    print(f"Saved storage state to {STATE_FILE}")

    # Close current context
    context.close()

    # Create new context with saved state
    new_context = browser.new_context(storage_state=STATE_FILE)
    new_page = new_context.new_page()
    new_page.goto("https://the-internet.herokuapp.com/")

    # Verify state was restored
    restored_theme = new_page.evaluate("localStorage.getItem('theme')")
    restored_language = new_page.evaluate("localStorage.getItem('language')")

    print(f"\nRestored in new context:")
    print(f"   - theme: {restored_theme}")
    print(f"   - language: {restored_language}")

    if restored_theme == "dark" and restored_language == "en":
        print("\n✓ Storage state successfully restored!")

    # Cleanup
    new_context.close()
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
        print(f"\nCleaned up {STATE_FILE}")

    browser.close()
```

### Key Points:
- localStorage persists until explicitly cleared
- sessionStorage persists during navigation within same tab
- Use `page.evaluate()` for all storage operations
- `context.storage_state()` saves both cookies AND localStorage
- JSON.stringify/parse for storing objects

---

## Bonus Challenges

### Challenge 1: Cookie Consent Banner

```python
"""Bonus: Skip cookie consent with pre-set cookie"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Create context with consent cookie already set
    context = browser.new_context()
    context.add_cookies([{
        "name": "cookie_consent",
        "value": "accepted",
        "domain": "example.com",
        "path": "/"
    }])

    page = context.new_page()
    page.goto("https://example.com")

    # Cookie banner should not appear!

    context.close()
    browser.close()
```

### Challenge 2: Multi-User with Separate Storage

```python
"""Bonus: Different users with separate storage"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # User 1 context
    user1_ctx = browser.new_context()
    user1 = user1_ctx.new_page()
    user1.goto("https://the-internet.herokuapp.com/")
    user1.evaluate("localStorage.setItem('user', 'Alice')")

    # User 2 context (completely isolated)
    user2_ctx = browser.new_context()
    user2 = user2_ctx.new_page()
    user2.goto("https://the-internet.herokuapp.com/")
    user2.evaluate("localStorage.setItem('user', 'Bob')")

    # Verify isolation
    alice = user1.evaluate("localStorage.getItem('user')")
    bob = user2.evaluate("localStorage.getItem('user')")

    print(f"User 1 storage: {alice}")  # Alice
    print(f"User 2 storage: {bob}")    # Bob

    user1_ctx.close()
    user2_ctx.close()
    browser.close()
```

### Challenge 3: Pre-populate Storage Before Page Load

```python
"""Bonus: Set storage before first navigation"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Add init script that runs before any page JS
    page.add_init_script("""
        localStorage.setItem('theme', 'dark');
        localStorage.setItem('onboarding_complete', 'true');
        localStorage.setItem('preferred_language', 'en');
    """)

    # Now navigate - localStorage is already set!
    page.goto("https://the-internet.herokuapp.com/")

    # Verify
    theme = page.evaluate("localStorage.getItem('theme')")
    print(f"Theme (set before load): {theme}")

    context.close()
    browser.close()
```

---

## Common Mistakes to Avoid

### Mistake 1: Wrong domain for cookies
```python
# WRONG - cookie won't be sent to the site
context.add_cookies([{
    "name": "test",
    "value": "123",
    "domain": "example.com",  # Wrong domain!
    "path": "/"
}])
page.goto("https://the-internet.herokuapp.com/")

# CORRECT - matching domain
context.add_cookies([{
    "name": "test",
    "value": "123",
    "domain": "the-internet.herokuapp.com",
    "path": "/"
}])
```

### Mistake 2: Forgetting to navigate before evaluate
```python
# WRONG - no page loaded yet
page.evaluate("localStorage.setItem('key', 'value')")  # May fail!

# CORRECT - navigate first
page.goto("https://example.com")
page.evaluate("localStorage.setItem('key', 'value')")
```

### Mistake 3: Not parsing JSON from storage
```python
# WRONG - returns string, not object
data = page.evaluate("localStorage.getItem('user')")
print(data["name"])  # Error!

# CORRECT - parse JSON string
import json
data_str = page.evaluate("localStorage.getItem('user')")
data = json.loads(data_str)
print(data["name"])
```
