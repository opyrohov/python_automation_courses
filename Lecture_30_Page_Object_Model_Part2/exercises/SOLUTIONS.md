# Solutions - Lecture 30: Page Object Model (Part 2)

## Exercise 1: BasePage Implementation

```python
"""Exercise 1 Solution: BasePage with Common Methods"""
from playwright.sync_api import sync_playwright
import os


class BasePage:
    """Base class with common functionality."""

    def __init__(self, page):
        self.page = page

    def get_url(self):
        """Return current URL."""
        return self.page.url

    def get_title(self):
        """Return page title."""
        return self.page.title()

    def wait_for_load(self):
        """Wait for page to load completely."""
        self.page.wait_for_load_state("networkidle")
        return self

    def take_screenshot(self, name):
        """Save screenshot to screenshots folder."""
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{name}.png"
        self.page.screenshot(path=path)
        print(f"Screenshot saved: {path}")
        return self

    def scroll_to_top(self):
        """Scroll to top of page."""
        self.page.evaluate("window.scrollTo(0, 0)")
        return self

    def scroll_to_bottom(self):
        """Scroll to bottom of page."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        return self


class DynamicLoadingPage(BasePage):
    """Dynamic Loading page object."""

    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def __init__(self, page):
        super().__init__(page)
        self.start_button = page.locator("#start button")
        self.loading = page.locator("#loading")
        self.result = page.locator("#finish h4")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def click_start(self):
        self.start_button.click()
        return self

    def wait_for_result(self):
        self.loading.wait_for(state="hidden")
        self.result.wait_for(state="visible")
        return self

    def get_result_text(self):
        return self.result.text_content()


class InfiniteScrollPage(BasePage):
    """Infinite Scroll page object."""

    URL = "https://the-internet.herokuapp.com/infinite_scroll"

    def __init__(self, page):
        super().__init__(page)
        self.paragraphs = page.locator(".jscroll-added")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def get_paragraph_count(self):
        return self.paragraphs.count()

    def scroll_and_load_more(self):
        initial_count = self.get_paragraph_count()
        self.scroll_to_bottom()
        # Wait for new content
        self.page.wait_for_function(
            f"document.querySelectorAll('.jscroll-added').length > {initial_count}"
        )
        return self


# Test the implementation
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1 Solution ===\n")

    # Test DynamicLoadingPage
    print("--- DynamicLoadingPage ---")
    dynamic = DynamicLoadingPage(page)
    dynamic.navigate()

    print(f"1. Title (inherited): {dynamic.get_title()}")
    print(f"2. URL (inherited): {dynamic.get_url()}")

    dynamic.click_start()
    dynamic.wait_for_result()
    print(f"3. Result: {dynamic.get_result_text()}")

    dynamic.take_screenshot("dynamic_result")
    print("4. Screenshot taken (inherited)")

    # Test InfiniteScrollPage
    print("\n--- InfiniteScrollPage ---")
    infinite = InfiniteScrollPage(page)
    infinite.navigate()

    print(f"5. Title (inherited): {infinite.get_title()}")

    initial_count = infinite.get_paragraph_count()
    print(f"6. Initial paragraphs: {initial_count}")

    infinite.scroll_and_load_more()
    new_count = infinite.get_paragraph_count()
    print(f"7. After scroll: {new_count}")

    assert new_count > initial_count
    print(f"\n✓ Exercise 1 completed!")

    browser.close()
```

### Key Points:
- BasePage contains reusable methods
- Child classes call `super().__init__(page)`
- Methods return `self` for chaining
- Screenshots folder created automatically

---

## Exercise 2: Multi-Page Flow with Page Transitions

```python
"""Exercise 2 Solution: Multi-Page Flow"""
from playwright.sync_api import sync_playwright


class BasePage:
    """Base class for all pages."""

    def __init__(self, page):
        self.page = page

    def get_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()


class LoginPage(BasePage):
    """Login page with transitions."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def enter_username(self, username):
        self.username_input.fill(username)
        return self

    def enter_password(self, password):
        self.password_input.fill(password)
        return self

    def click_login(self):
        self.login_button.click()
        # Return appropriate page based on result
        if "/secure" in self.page.url:
            return SecurePage(self.page)
        return self

    def login(self, username, password):
        """Complete login - returns SecurePage on success."""
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()

    def login_expecting_error(self, username, password):
        """Login expecting failure - always returns self."""
        self.enter_username(username)
        self.enter_password(password)
        self.login_button.click()
        return self

    def get_error_message(self):
        return self.flash.text_content().strip()

    def has_error(self):
        return "error" in (self.flash.get_attribute("class") or "")


class SecurePage(BasePage):
    """Secure area page after login."""

    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h2")
        self.flash = page.locator("#flash")
        self.logout_button = page.locator("a[href='/logout']")

    def get_heading(self):
        return self.heading.text_content()

    def get_welcome_message(self):
        return self.flash.text_content().strip()

    def is_logged_in(self):
        return self.logout_button.is_visible()

    def logout(self):
        """Logout and return LoginPage."""
        self.logout_button.click()
        return LoginPage(self.page)


# Test all scenarios
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 2 Solution ===\n")

    # Scenario 1: Successful Login
    print("--- Scenario 1: Successful Login ---")
    login_page = LoginPage(page)
    login_page.navigate()
    print(f"1. On: {login_page.__class__.__name__}")

    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
    print(f"2. After login: {secure_page.__class__.__name__}")
    print(f"   Is logged in: {secure_page.is_logged_in()}")
    assert isinstance(secure_page, SecurePage)

    # Scenario 2: Logout
    print("\n--- Scenario 2: Logout ---")
    login_page = secure_page.logout()
    print(f"3. After logout: {login_page.__class__.__name__}")
    assert isinstance(login_page, LoginPage)

    # Scenario 3: Failed Login
    print("\n--- Scenario 3: Failed Login ---")
    login_page.navigate()
    result = login_page.login("wrong", "wrong")
    print(f"4. After bad login: {result.__class__.__name__}")
    print(f"   Has error: {result.has_error()}")
    assert isinstance(result, LoginPage)
    assert result.has_error()

    # Scenario 4: Full User Journey
    print("\n--- Scenario 4: Full User Journey ---")

    # Start fresh
    journey = LoginPage(page)
    journey.navigate()
    print("Step 1: On login page")

    # Try invalid credentials
    journey = journey.login_expecting_error("bad", "credentials")
    assert journey.has_error()
    print("Step 2: Invalid login rejected")

    # Valid login
    secure = journey.login("tomsmith", "SuperSecretPassword!")
    assert isinstance(secure, SecurePage)
    print(f"Step 3: Logged in - {secure.get_heading()}")

    # Access secure area
    assert secure.is_logged_in()
    welcome = secure.get_welcome_message()
    print(f"Step 4: Welcome message: {welcome[:30]}...")

    # Logout
    final = secure.logout()
    assert isinstance(final, LoginPage)
    print("Step 5: Logged out successfully")

    # Verify back on login
    assert "/login" in final.get_url()
    print("Step 6: Back on login page")

    print("\n✓ Exercise 2 completed!")

    browser.close()
```

### Key Points:
- `login()` returns `SecurePage` on success, `LoginPage` on failure
- `logout()` always returns `LoginPage`
- Use `isinstance()` to verify page type in tests
- Full journey tests multiple transitions

---

## Summary: Page Transitions Pattern

```python
# Pattern for actions that change pages:

def login(self, user, pwd):
    # Perform action
    self.fill_username(user)
    self.fill_password(pwd)
    self.click_submit()

    # Check result and return appropriate page
    if "/success" in self.page.url:
        return SuccessPage(self.page)
    return self  # Stay on current page

# Pattern for actions that always go to specific page:

def logout(self):
    self.logout_button.click()
    return LoginPage(self.page)  # Always returns LoginPage

# Pattern for expected errors:

def login_expecting_error(self, user, pwd):
    self.fill_form(user, pwd)
    self.click_submit()
    return self  # Explicitly stay on login page
```

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting super().__init__()
```python
# WRONG
class MyPage(BasePage):
    def __init__(self, page):
        self.page = page  # Missing super()!

# CORRECT
class MyPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Call parent!
```

### Mistake 2: Returning wrong page type
```python
# WRONG - always returns self
def login(self, user, pwd):
    self.fill_form(user, pwd)
    self.click_submit()
    return self  # Even on success!

# CORRECT - checks result
def login(self, user, pwd):
    self.fill_form(user, pwd)
    self.click_submit()
    if "/secure" in self.page.url:
        return SecurePage(self.page)
    return self
```

### Mistake 3: Not sharing page object
```python
# WRONG - creating new page
def logout(self):
    self.logout_button.click()
    new_page = browser.new_page()  # Wrong!
    return LoginPage(new_page)

# CORRECT - using same page
def logout(self):
    self.logout_button.click()
    return LoginPage(self.page)  # Same page object!
```
