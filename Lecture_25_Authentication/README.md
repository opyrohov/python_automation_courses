# Lecture 25: Authentication

## Overview
Master authentication handling in Playwright - from basic HTTP auth to advanced session management. Learn how to efficiently handle login flows and reuse authentication state across tests.

## Topics Covered

### 1. Basic HTTP Authentication
- HTTP Basic Auth with credentials in URL
- Using `http_credentials` context option
- Handling auth dialogs

### 2. Login Automation Best Practices
- Form-based login automation
- Waiting for successful login
- Error handling for failed logins
- Avoiding common pitfalls

### 3. Saving Authentication State
- `storage_state()` method
- Saving cookies and localStorage
- JSON file storage
- When to save vs when to login fresh

### 4. Reusing Authentication Across Tests
- Loading saved state
- `storage_state` context option
- Sharing auth between tests
- Test isolation considerations

### 5. Session Management
- Understanding cookies and sessions
- Session expiration handling
- Refreshing authentication
- Multiple user sessions

### 6. Handling Different Auth Methods
- OAuth flows
- Token-based authentication
- Multi-factor authentication considerations
- SSO (Single Sign-On) basics

## Quick Reference

### HTTP Basic Auth
```python
# Method 1: Credentials in URL
page.goto("https://user:password@example.com/protected")

# Method 2: http_credentials option (recommended)
context = browser.new_context(
    http_credentials={
        "username": "user",
        "password": "password"
    }
)
```

### Form-Based Login
```python
# Standard login flow
page.goto("https://example.com/login")
page.locator("#username").fill("user")
page.locator("#password").fill("password")
page.locator("button[type='submit']").click()

# Wait for successful login
page.wait_for_url("**/dashboard")
# or
expect(page.locator(".welcome-message")).to_be_visible()
```

### Saving Authentication State
```python
# After logging in, save state
page.goto("https://example.com/login")
page.locator("#username").fill("user")
page.locator("#password").fill("password")
page.locator("button[type='submit']").click()
page.wait_for_url("**/dashboard")

# Save cookies and localStorage to file
context.storage_state(path="auth_state.json")
```

### Reusing Authentication State
```python
# Create context with saved state
context = browser.new_context(
    storage_state="auth_state.json"
)
page = context.new_page()

# Already logged in!
page.goto("https://example.com/dashboard")
```

### Multiple Users
```python
# User 1 context
user1_context = browser.new_context(
    storage_state="user1_auth.json"
)

# User 2 context
user2_context = browser.new_context(
    storage_state="user2_auth.json"
)

# Both users logged in with different accounts
```

## Examples

| File | Description |
|------|-------------|
| `01_http_basic_auth.py` | HTTP Basic Authentication methods |
| `02_form_login.py` | Form-based login automation |
| `03_save_auth_state.py` | Saving authentication state |
| `04_reuse_auth_state.py` | Reusing saved authentication |
| `05_multi_user_auth.py` | Multiple user sessions |

## Exercises

| File | Description |
|------|-------------|
| `exercise_01_login_save.py` | Login and save authentication state |
| `exercise_02_reuse_session.py` | Reuse saved session for multiple tests |

## Key Concepts

1. **HTTP Basic Auth**
   - Built into HTTP protocol
   - Credentials sent with every request
   - Use `http_credentials` context option

2. **Storage State**
   - Includes cookies and localStorage
   - Saved as JSON file
   - Can be shared between test runs

3. **Session Isolation**
   - Each context has separate session
   - Contexts don't share cookies
   - Use for multi-user testing

4. **Best Practices**
   - Save auth state once, reuse many times
   - Refresh state when it expires
   - Don't commit auth files to git

## Common Issues

| Issue | Solution |
|-------|----------|
| Login state not persisting | Ensure context.storage_state() is called after full login |
| Auth state expired | Re-run login and save new state |
| Wrong user logged in | Check you're loading correct state file |
| HTTP auth not working | Use http_credentials, not URL credentials |
| Session lost between tests | Load storage_state when creating context |

## Auth State File Structure

```json
{
  "cookies": [
    {
      "name": "session_id",
      "value": "abc123...",
      "domain": "example.com",
      "path": "/",
      "expires": 1735689600,
      "httpOnly": true,
      "secure": true,
      "sameSite": "Lax"
    }
  ],
  "origins": [
    {
      "origin": "https://example.com",
      "localStorage": [
        {
          "name": "auth_token",
          "value": "xyz789..."
        }
      ]
    }
  ]
}
```

## Security Considerations

1. **Never commit auth files** - Add to .gitignore
2. **Use environment variables** for credentials
3. **Rotate test credentials** regularly
4. **Use dedicated test accounts** - not real user accounts
5. **Clear state after tests** in CI/CD pipelines

## Resources

- [Playwright Authentication Documentation](https://playwright.dev/python/docs/auth)
- [HTTP Authentication](https://playwright.dev/python/docs/network#http-authentication)
- [Browser Contexts](https://playwright.dev/python/docs/browser-contexts)
