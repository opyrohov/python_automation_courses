# Lecture 29: Page Object Model (Part 1)

## Overview
Learn the Page Object Model (POM) design pattern - a best practice for organizing test automation code. POM improves maintainability, reusability, and readability of your tests.

## Topics Covered

### 1. What is Page Object Model?
POM is a design pattern where:
- Each web page has a corresponding Python class
- Page elements (locators) are defined as class attributes
- Page interactions are defined as class methods
- Tests use page objects instead of raw Playwright commands

### 2. Why Use POM?

| Without POM | With POM |
|-------------|----------|
| Locators scattered in tests | Locators in one place |
| Duplicate code | Reusable methods |
| Hard to maintain | Easy to update |
| Tests are verbose | Tests are readable |

### 3. Basic POM Structure
```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-btn")

    # Actions
    def navigate(self):
        self.page.goto("/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

### 4. Using Page Objects in Tests
```python
# tests/test_login.py
from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")

    # Assertions
    expect(page).to_have_url("**/secure")
```

### 5. Organizing Locators
```python
class LoginPage:
    def __init__(self, page):
        self.page = page

        # Group related locators
        # Form inputs
        self.username = page.locator("#username")
        self.password = page.locator("#password")

        # Buttons
        self.submit_btn = page.locator("button[type='submit']")

        # Messages
        self.error_message = page.locator(".flash.error")
        self.success_message = page.locator(".flash.success")
```

### 6. Creating Page Methods
```python
class LoginPage:
    # Navigation
    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
        return self

    # Actions
    def enter_username(self, username):
        self.username.fill(username)
        return self

    def enter_password(self, password):
        self.password.fill(password)
        return self

    def click_login(self):
        self.submit_btn.click()
        return self

    # Combined action
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    # Getters
    def get_error_message(self):
        return self.error_message.text_content()

    def is_error_visible(self):
        return self.error_message.is_visible()
```

### 7. Method Chaining
```python
class LoginPage:
    def navigate(self):
        self.page.goto("/login")
        return self  # Return self for chaining

    def enter_username(self, username):
        self.username.fill(username)
        return self

    def enter_password(self, password):
        self.password.fill(password)
        return self

# Usage with chaining
login_page.navigate().enter_username("user").enter_password("pass")
```

### 8. Project Structure
```
project/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── secure_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_secure_area.py
└── conftest.py
```

## Benefits of POM

1. **Maintainability**: Change locator once, affects all tests
2. **Reusability**: Same page object used by multiple tests
3. **Readability**: Tests read like user stories
4. **Separation**: Tests focus on WHAT, pages focus on HOW
5. **Scalability**: Easy to add new pages and tests

## Common Patterns

### Pattern 1: Wait in Methods
```python
def click_login(self):
    self.submit_btn.click()
    self.page.wait_for_url("**/secure")
    return self
```

### Pattern 2: Return New Page
```python
def login(self, username, password):
    self.username.fill(username)
    self.password.fill(password)
    self.submit_btn.click()
    return SecurePage(self.page)  # Return next page
```

### Pattern 3: Validation Methods
```python
def is_loaded(self):
    return self.login_button.is_visible()

def has_error(self):
    return self.error_message.is_visible()
```

## Files in This Lecture

### Examples
- `01_without_pom.py` - Test without POM (messy)
- `02_basic_page_object.py` - Basic page object class
- `03_page_with_methods.py` - Page with action methods
- `04_method_chaining.py` - Fluent interface pattern
- `05_complete_example.py` - Full POM implementation

### Exercises
- `exercise_01_create_page_object.py` - Create your first page object
- `exercise_02_refactor_test.py` - Refactor test to use POM
- `SOLUTIONS.md` - Complete solutions

## Quick Reference

```python
# Basic Page Object Structure
class PageName:
    def __init__(self, page):
        self.page = page
        # Define locators
        self.element = page.locator("selector")

    def action_method(self):
        # Perform action
        self.element.click()
        return self  # For chaining

    def getter_method(self):
        # Return data
        return self.element.text_content()

    def validation_method(self):
        # Return boolean
        return self.element.is_visible()
```
