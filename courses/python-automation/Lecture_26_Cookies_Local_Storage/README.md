# Lecture 26: Cookies & Local Storage

## Overview
Learn how to work with browser storage mechanisms in Playwright - cookies, local storage, and session storage. Essential for managing state, authentication, and user preferences in automated tests.

## Topics Covered

### 1. Working with Cookies
```python
# Get all cookies
cookies = context.cookies()

# Get cookies for specific URL
cookies = context.cookies(["https://example.com"])

# Add cookies
context.add_cookies([
    {
        "name": "session_id",
        "value": "abc123",
        "domain": "example.com",
        "path": "/"
    }
])

# Clear cookies
context.clear_cookies()
```

### 2. Cookie Properties
```python
# Full cookie structure
cookie = {
    "name": "user_token",           # Required
    "value": "xyz789",              # Required
    "domain": ".example.com",       # Required (or url)
    "path": "/",                    # Default: "/"
    "expires": 1735689600,          # Unix timestamp (optional)
    "httpOnly": True,               # JS cannot access
    "secure": True,                 # HTTPS only
    "sameSite": "Strict"            # Strict, Lax, or None
}
```

### 3. Local Storage
```python
# Set local storage item
page.evaluate("localStorage.setItem('theme', 'dark')")

# Get local storage item
theme = page.evaluate("localStorage.getItem('theme')")

# Remove item
page.evaluate("localStorage.removeItem('theme')")

# Clear all local storage
page.evaluate("localStorage.clear()")

# Get all local storage
all_data = page.evaluate("""() => {
    const data = {};
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        data[key] = localStorage.getItem(key);
    }
    return data;
}""")
```

### 4. Session Storage
```python
# Set session storage item
page.evaluate("sessionStorage.setItem('cart_id', '12345')")

# Get session storage item
cart_id = page.evaluate("sessionStorage.getItem('cart_id')")

# Clear session storage
page.evaluate("sessionStorage.clear()")

# Get all session storage
session_data = page.evaluate("""() => {
    const data = {};
    for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        data[key] = sessionStorage.getItem(key);
    }
    return data;
}""")
```

### 5. Storage State (Save & Load)
```python
# Save complete storage state (cookies + localStorage)
context.storage_state(path="state.json")

# Load storage state when creating context
context = browser.new_context(storage_state="state.json")

# Get storage state as dict (without saving)
state = context.storage_state()
print(state["cookies"])
print(state["origins"])  # localStorage per origin
```

### 6. Clearing Browser Data
```python
# Clear cookies only
context.clear_cookies()

# Clear all storage for page
page.evaluate("""() => {
    localStorage.clear();
    sessionStorage.clear();
}""")

# Fresh context (no data)
fresh_context = browser.new_context()

# Clear specific domain cookies
cookies = context.cookies()
other_cookies = [c for c in cookies if c["domain"] != "example.com"]
context.clear_cookies()
context.add_cookies(other_cookies)
```

## Key Differences

| Storage Type | Persistence | Scope | Size Limit | Sent to Server |
|-------------|-------------|-------|------------|----------------|
| Cookies | Configurable (expires) | Domain + Path | ~4KB | Yes (every request) |
| Local Storage | Permanent | Origin | ~5-10MB | No |
| Session Storage | Tab session | Origin + Tab | ~5-10MB | No |

## Common Use Cases

### 1. Skip Login with Cookies
```python
# First: Login and save
context.storage_state(path="auth.json")

# Later: Skip login
context = browser.new_context(storage_state="auth.json")
page.goto("/dashboard")  # Already logged in!
```

### 2. Set User Preferences
```python
# Set dark mode before page loads
page.add_init_script("""
    localStorage.setItem('theme', 'dark');
    localStorage.setItem('language', 'en');
""")
page.goto("https://example.com")
```

### 3. Inject Test Data
```python
# Prepare cart data
page.evaluate("""
    localStorage.setItem('cart', JSON.stringify([
        {id: 1, name: 'Product A', qty: 2},
        {id: 2, name: 'Product B', qty: 1}
    ]));
""")
page.reload()  # App reads cart from storage
```

### 4. Test Cookie Consent
```python
# Accept cookies
context.add_cookies([{
    "name": "cookie_consent",
    "value": "accepted",
    "domain": "example.com",
    "path": "/"
}])
page.goto("https://example.com")
# Cookie banner should not appear
```

## Best Practices

1. **Use storage_state for auth** - More reliable than just cookies
2. **Clear storage between tests** - Avoid test pollution
3. **Set expiry for test cookies** - Avoid stale cookies
4. **Use add_init_script for localStorage** - Set before page loads
5. **Check domain matches** - Cookies need exact domain match
6. **Handle secure cookies** - May need HTTPS context

## Files in This Lecture

### Examples
- `01_cookie_basics.py` - Getting and setting cookies
- `02_local_storage.py` - Working with localStorage
- `03_session_storage.py` - Working with sessionStorage
- `04_storage_state.py` - Saving and loading complete state
- `05_clearing_data.py` - Clearing browser storage

### Exercises
- `exercise_01_cookie_management.py` - Manage cookies for login
- `exercise_02_storage_manipulation.py` - Work with localStorage
- `SOLUTIONS.md` - Complete solutions

## Quick Reference

```python
# Cookies
context.cookies()                    # Get all cookies
context.cookies(["https://..."])     # Get for URL
context.add_cookies([{...}])         # Add cookies
context.clear_cookies()              # Clear all cookies

# Local Storage (via evaluate)
page.evaluate("localStorage.setItem('key', 'value')")
page.evaluate("localStorage.getItem('key')")
page.evaluate("localStorage.removeItem('key')")
page.evaluate("localStorage.clear()")

# Session Storage (via evaluate)
page.evaluate("sessionStorage.setItem('key', 'value')")
page.evaluate("sessionStorage.getItem('key')")
page.evaluate("sessionStorage.clear()")

# Storage State
context.storage_state(path="state.json")          # Save
browser.new_context(storage_state="state.json")   # Load
```
