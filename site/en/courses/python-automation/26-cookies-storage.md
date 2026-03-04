# Lecture 26: Cookies and Local Storage

Cookies and local storage.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_26_Cookies_Local_Storage/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_26_Cookies_Local_Storage/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_26_Cookies_Local_Storage/exercises" target="_blank">📝 Вправи</a>
</div>

## Cookies

```python
# Get all cookies
cookies = context.cookies()
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")

# Get cookies for URL
cookies = context.cookies(["https://example.com"])

# Add cookie
context.add_cookies([{
    "name": "session_id",
    "value": "abc123",
    "domain": "example.com",
    "path": "/"
}])

# Clear cookies
context.clear_cookies()
```

## Local Storage

```python
# Get value
value = page.evaluate("() => localStorage.getItem('key')")

# Set value
page.evaluate("() => localStorage.setItem('key', 'value')")

# Remove
page.evaluate("() => localStorage.removeItem('key')")

# Clear all
page.evaluate("() => localStorage.clear()")

# Get all keys
keys = page.evaluate("""() => {
    const keys = [];
    for (let i = 0; i < localStorage.length; i++) {
        keys.push(localStorage.key(i));
    }
    return keys;
}""")
```

## Session Storage

```python
# Similar to localStorage
value = page.evaluate("() => sessionStorage.getItem('key')")
page.evaluate("() => sessionStorage.setItem('key', 'value')")
```

## Storage State

```python
# Save entire state (cookies + localStorage)
storage = context.storage_state()

# Save to file
context.storage_state(path="state.json")

# Load state
context = browser.new_context(storage_state="state.json")
```

## Example: Skipping cookie banner

```python
# Set cookie that user accepted cookies
context.add_cookies([{
    "name": "cookie_consent",
    "value": "accepted",
    "domain": "example.com",
    "path": "/"
}])

page.goto("https://example.com")
# Cookie banner won't appear
```
