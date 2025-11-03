# Lecture 10: Classes & Objects (Part 2)

## Overview
Building on Lecture 9, this lecture dives deeper into Object-Oriented Programming with a focus on **inheritance**, organizing test automation code, and building reusable page classes using the Page Object Model pattern with Playwright.

## Learning Objectives
By the end of this lecture, you will be able to:
- Understand and implement class inheritance in Python
- Use the `super()` function to call parent methods
- Create base classes for code reuse
- Organize test automation code effectively
- Build reusable page classes with inheritance
- Apply OOP best practices in test automation
- Implement method overriding
- Work with multi-level inheritance

## Topics Covered

### 1. Inheritance Basics
- What is inheritance and why use it?
- Creating parent (base) classes
- Creating child (derived) classes
- The `super()` function
- Accessing parent methods and attributes

### 2. Method Overriding
- Overriding parent methods
- Extending parent functionality
- When to override vs when to extend

### 3. Building Reusable Page Classes
- Creating a BasePage class
- Implementing common page actions
- Inheriting from BasePage
- Organizing page object hierarchy

### 4. Organizing Test Code
- Structuring test projects
- Base test classes
- Test fixtures and setup
- Utility classes and helpers

### 5. Best Practices
- When to use inheritance
- Composition vs inheritance
- DRY (Don't Repeat Yourself) principle
- Single Responsibility Principle
- Naming conventions

## File Structure

```
Lecture_10_Classes_Objects_Part2/
├── README.md (this file)
├── examples/
│   ├── 01_inheritance_basics.py
│   ├── 02_super_function.py
│   ├── 03_method_overriding.py
│   ├── 04_basepage_pattern.py
│   ├── 05_organizing_tests.py
│   └── 06_best_practices.py
├── exercises/
│   ├── exercise_01_inheritance.py
│   ├── exercise_02_page_objects.py
│   ├── exercise_03_test_organization.py
│   └── SOLUTIONS.md
└── presentation.html
```

## Key Concepts

### Inheritance
Inheritance allows a class to inherit attributes and methods from another class:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.speak()  # Buddy says Woof!
```

### BasePage Pattern
A common pattern in test automation using inheritance:

```python
class BasePage:
    """Base class for all page objects."""

    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        """Navigate to URL."""
        self.page.goto(url)

    def get_title(self):
        """Get page title."""
        return self.page.title()

    def click_element(self, selector):
        """Click an element."""
        self.page.click(selector)

class LoginPage(BasePage):
    """Login page inherits common functionality."""

    def __init__(self, page):
        super().__init__(page)  # Call parent constructor
        self.username_input = "#username"
        self.password_input = "#password"

    def login(self, username, password):
        """Perform login."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.click_element("#submit")  # Use parent method

# Now LoginPage has all BasePage methods!
login_page = LoginPage(page)
login_page.navigate_to("https://example.com/login")
login_page.login("user", "pass")
```

### The super() Function
`super()` is used to call methods from the parent class:

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent __init__
        self.age = age
```

## Practice Checklist

- [ ] Understand inheritance concepts
- [ ] Create classes with inheritance
- [ ] Use `super()` function correctly
- [ ] Override parent methods
- [ ] Create a BasePage class
- [ ] Build page objects using inheritance
- [ ] Organize test code with base classes
- [ ] Apply OOP best practices

## Common Pitfalls

1. **Forgetting to call super().__init__()**: Always initialize parent class
2. **Deep inheritance hierarchies**: Keep it simple (2-3 levels max)
3. **Overusing inheritance**: Consider composition when inheritance doesn't fit
4. **Not following naming conventions**: Use clear, descriptive names

## Real-World Applications

### Test Automation
- BasePage for common page actions
- BaseTest for test setup/teardown
- Reusable utility classes

### Code Organization
- Shared functionality in base classes
- Specific implementations in child classes
- Maintainable test suites

## Next Steps

After completing this lecture:
1. Complete all examples
2. Work through all exercises
3. Build your own page object hierarchy
4. Apply these patterns to real test projects
5. Practice organizing test code

## Resources

- [Python Inheritance Documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [Page Object Model Best Practices](https://martinfowler.com/bliki/PageObject.html)

## Summary

Inheritance is a powerful feature that promotes code reuse and organization. In test automation, the BasePage pattern using inheritance is an industry-standard approach for building maintainable test suites. By mastering these concepts, you'll write cleaner, more maintainable automation code.

Happy coding!
