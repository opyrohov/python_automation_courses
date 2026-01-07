# Lecture 30: Page Object Model (Part 2)

## Overview
Advanced Page Object Model patterns including BasePage class, inheritance, page transitions, project structure, and best practices.

## Topics Covered

### 1. BasePage Class
- Creating a base class for common functionality
- Inheritance in page objects
- Shared methods (navigation, waits, screenshots)

### 2. Page Transitions
- Methods that return different page objects
- Login returning SecurePage
- Navigation between pages

### 3. Multiple Page Objects
- Working with several page objects
- Page object composition
- Shared components

### 4. Project Structure
- Organizing page objects in folders
- Separating pages, components, tests
- Import strategies

### 5. Best Practices
- What belongs in page objects
- What doesn't belong (assertions)
- Naming conventions
- Documentation

## Examples

1. **01_base_page.py** - Creating and using BasePage class
2. **02_page_inheritance.py** - Inheritance patterns
3. **03_page_transitions.py** - Navigation between page objects
4. **04_project_structure.py** - Organizing POM project
5. **05_best_practices.py** - Correct and incorrect patterns

## Exercises

1. **exercise_01_basepage_implementation.py** - Create BasePage with common methods
2. **exercise_02_multi_page_flow.py** - Implement login flow with multiple pages

## Key Concepts

### BasePage Pattern
```python
class BasePage:
    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.title()

    def take_screenshot(self, name):
        self.page.screenshot(path=f"{name}.png")

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("#username")
```

### Page Transitions
```python
class LoginPage(BasePage):
    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.submit.click()
        return SecurePage(self.page)  # Return new page object
```

### Project Structure
```
project/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── secure_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
└── conftest.py
```

## Resources
- [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)
- [Page Object Model Pattern](https://martinfowler.com/bliki/PageObject.html)

## Next Lecture
Lecture 31: Introduction to Pytest
