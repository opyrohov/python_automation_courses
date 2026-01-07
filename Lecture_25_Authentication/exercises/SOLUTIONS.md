# Solutions - Lecture 25: Authentication

## Exercise 1: Login and Save Authentication State

```python
"""Exercise 1 Solution: Login and Save Authentication State"""
from playwright.sync_api import sync_playwright, expect
import os
import json

AUTH_FILE = "my_auth.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("=== Exercise 1: Login and Save Auth State ===\n")

    # Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print("1. Navigated to login page")

    # Fill in username
    page.locator("#username").fill("tomsmith")
    print("2. Entered username")

    # Fill in password
    page.locator("#password").fill("SuperSecretPassword!")
    print("3. Entered password")

    # Click submit button
    page.locator("button[type='submit']").click()
    print("4. Clicked login button")

    # Wait for successful login
    page.wait_for_url("**/secure")
    expect(page.locator(".flash.success")).to_be_visible()
    print("5. ✓ Login successful")

    # Save authentication state
    context.storage_state(path=AUTH_FILE)
    print(f"6. ✓ Auth state saved to {AUTH_FILE}")

    # Verify file was created
    if os.path.exists(AUTH_FILE):
        file_size = os.path.getsize(AUTH_FILE)
        print(f"7. ✓ File created successfully ({file_size} bytes)")

        # Bonus: Print number of cookies
        with open(AUTH_FILE, "r") as f:
            state = json.load(f)
        cookie_count = len(state.get("cookies", []))
        print(f"8. Cookies saved: {cookie_count}")
    else:
        print("7. ✗ File was not created!")

    print("\n✓ Exercise 1 completed!")
    context.close()
    browser.close()
```

### Key Points:
- Always wait for login to complete before saving state
- Use `page.wait_for_url()` or `expect()` to verify login success
- The auth file contains cookies and localStorage
- Check file exists to confirm save was successful

---

## Exercise 2: Reuse Saved Session

```python
"""Exercise 2 Solution: Reuse Saved Session"""
from playwright.sync_api import sync_playwright, expect
import os

AUTH_FILE = "my_auth.json"

# Check if auth file exists
if not os.path.exists(AUTH_FILE):
    print(f"ERROR: {AUTH_FILE} not found!")
    print("Please run exercise_01_login_save.py first.")
    exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    print("=== Exercise 2: Reuse Saved Session ===\n")

    # Create context with saved auth state
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()
    print("1. Created context with saved auth state")

    # Navigate directly to secure page
    page.goto("https://the-internet.herokuapp.com/secure")
    print("2. Navigated to secure page")

    # Verify we're authenticated
    expect(page.locator("h2")).to_have_text("Secure Area")
    expect(page.locator(".flash.success")).to_be_visible()
    print("3. ✓ Successfully accessed secure page - we're authenticated!")

    # Navigate to another page to prove session works
    page.goto("https://the-internet.herokuapp.com/")
    print("4. Navigated to home page")

    page.goto("https://the-internet.herokuapp.com/secure")
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("5. ✓ Still authenticated on secure page")

    context.close()

    # Compare with fresh context (no auth)
    print("\n--- Testing Fresh Context (No Auth) ---")
    fresh_context = browser.new_context()
    fresh_page = fresh_context.new_page()

    fresh_page.goto("https://the-internet.herokuapp.com/secure")

    if "/login" in fresh_page.url:
        print("6. ✓ Fresh context correctly redirected to login")
    else:
        print("6. Fresh context unexpectedly accessed secure page")

    fresh_context.close()

    # Bonus: Clean up auth file
    # os.remove(AUTH_FILE)
    # print("7. Cleaned up auth file")

    print("\n✓ Exercise 2 completed!")
    browser.close()
```

### Key Points:
- Use `storage_state` parameter when creating context
- No login needed - session is restored automatically
- Fresh context (without storage_state) has no auth
- This proves the saved state is being used correctly

---

## Bonus Challenges

### Challenge 1: Auto-Refresh Expired Sessions

```python
"""Bonus: Auto-refresh expired sessions"""
from playwright.sync_api import sync_playwright, expect
import os
import time

AUTH_FILE = "auth_state.json"
MAX_AGE_HOURS = 24

def is_auth_valid():
    """Check if auth file exists and is not too old."""
    if not os.path.exists(AUTH_FILE):
        return False

    file_age = time.time() - os.path.getmtime(AUTH_FILE)
    max_age_seconds = MAX_AGE_HOURS * 3600

    return file_age < max_age_seconds

def perform_login(browser):
    """Login and save auth state."""
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    page.wait_for_url("**/secure")

    context.storage_state(path=AUTH_FILE)
    print("Fresh login performed and saved")

    context.close()

def get_authenticated_context(browser):
    """Get context with valid auth, refreshing if needed."""
    if is_auth_valid():
        print("Using cached auth state")
        return browser.new_context(storage_state=AUTH_FILE)
    else:
        print("Auth expired or missing - performing fresh login")
        perform_login(browser)
        return browser.new_context(storage_state=AUTH_FILE)

# Usage
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = get_authenticated_context(browser)
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/secure")
    expect(page.locator("h2")).to_have_text("Secure Area")
    print("Successfully accessed secure page!")

    context.close()
    browser.close()
```

### Challenge 2: Environment Variables for Credentials

```python
"""Bonus: Using environment variables for credentials"""
from playwright.sync_api import sync_playwright, expect
import os

# Get credentials from environment (with defaults for development)
USERNAME = os.environ.get("TEST_USERNAME", "tomsmith")
PASSWORD = os.environ.get("TEST_PASSWORD", "SuperSecretPassword!")

def login_with_env_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        # Use environment variables
        page.fill("#username", USERNAME)
        page.fill("#password", PASSWORD)
        page.click("button[type='submit']")

        # Check for login errors
        if page.locator(".flash.error").is_visible():
            error = page.locator(".flash.error").text_content()
            raise Exception(f"Login failed: {error}")

        page.wait_for_url("**/secure")
        print(f"Successfully logged in as: {USERNAME}")

        browser.close()

# Run with:
# TEST_USERNAME=admin TEST_PASSWORD=secret python script.py
login_with_env_credentials()
```

### Challenge 3: Multi-Role Testing

```python
"""Bonus: Testing with different user roles"""
from playwright.sync_api import sync_playwright, expect
import os

# Define user roles
USERS = {
    "admin": {
        "username": "tomsmith",
        "password": "SuperSecretPassword!",
        "auth_file": "admin_auth.json"
    },
    "user": {
        "username": "tomsmith",  # Same for demo
        "password": "SuperSecretPassword!",
        "auth_file": "user_auth.json"
    }
}

def setup_all_users(browser):
    """Create auth files for all users."""
    for role, creds in USERS.items():
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("#username", creds["username"])
        page.fill("#password", creds["password"])
        page.click("button[type='submit']")
        page.wait_for_url("**/secure")

        context.storage_state(path=creds["auth_file"])
        print(f"Created auth for: {role}")

        context.close()

def get_user_context(browser, role):
    """Get context for specific user role."""
    if role not in USERS:
        raise ValueError(f"Unknown role: {role}")

    auth_file = USERS[role]["auth_file"]

    if not os.path.exists(auth_file):
        raise FileNotFoundError(f"Auth file not found: {auth_file}")

    return browser.new_context(storage_state=auth_file)

# Usage
with sync_playwright() as p:
    browser = p.chromium.launch()

    # Setup (run once)
    setup_all_users(browser)

    # Tests with different roles
    admin_ctx = get_user_context(browser, "admin")
    admin_page = admin_ctx.new_page()
    admin_page.goto("https://the-internet.herokuapp.com/secure")
    print(f"Admin title: {admin_page.title()}")
    admin_ctx.close()

    user_ctx = get_user_context(browser, "user")
    user_page = user_ctx.new_page()
    user_page.goto("https://the-internet.herokuapp.com/secure")
    print(f"User title: {user_page.title()}")
    user_ctx.close()

    # Cleanup
    for role in USERS:
        auth_file = USERS[role]["auth_file"]
        if os.path.exists(auth_file):
            os.remove(auth_file)

    browser.close()
```

---

## Common Mistakes to Avoid

### Mistake 1: Saving state before login completes
```python
# WRONG - may save incomplete state
page.click("button[type='submit']")
context.storage_state(path="auth.json")  # Too early!

# CORRECT - wait for login to complete
page.click("button[type='submit']")
page.wait_for_url("**/dashboard")  # Wait for redirect
context.storage_state(path="auth.json")  # Now it's safe
```

### Mistake 2: Hardcoding credentials
```python
# WRONG - credentials in code
page.fill("#password", "MySecretPassword123!")

# CORRECT - use environment variables
password = os.environ.get("TEST_PASSWORD")
page.fill("#password", password)
```

### Mistake 3: Sharing auth file between different accounts
```python
# WRONG - overwrites admin auth with user auth
login_as_admin()
context.storage_state(path="auth.json")
login_as_user()
context.storage_state(path="auth.json")  # Overwrites!

# CORRECT - separate files
login_as_admin()
context.storage_state(path="admin_auth.json")
login_as_user()
context.storage_state(path="user_auth.json")
```

### Mistake 4: Not handling expired sessions
```python
# WRONG - assumes auth is always valid
context = browser.new_context(storage_state="auth.json")
page.goto("/dashboard")  # May fail if expired!

# CORRECT - check and refresh if needed
context = browser.new_context(storage_state="auth.json")
page = context.new_page()
page.goto("/dashboard")
if "/login" in page.url:
    # Session expired - re-authenticate
    perform_fresh_login()
```
