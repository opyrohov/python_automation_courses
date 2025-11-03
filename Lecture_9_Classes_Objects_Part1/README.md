# Lecture 9: Classes & Objects (Part 1)

Learn Object-Oriented Programming (OOP) fundamentals in Python and apply them to test automation with the Page Object Model pattern.

## 🎯 Learning Objectives

By the end of this lecture, you will be able to:
- Understand what classes and objects are
- Create custom classes with the `__init__` method
- Work with instance variables and methods
- Understand the difference between classes and instances
- Implement the Page Object Model pattern for Playwright
- Organize test code using OOP principles

## 📚 Topics Covered

### 1. Introduction to Classes
- What are classes and objects?
- Why use classes in automation?
- Class vs instance concepts
- Creating your first class

### 2. The `__init__` Method
- Constructor basics
- Initializing instance variables
- Parameters in `__init__`
- Setting up object state

### 3. Instance Variables
- What are instance variables?
- Using `self`
- Accessing and modifying attributes
- Instance vs class variables

### 4. Instance Methods
- Defining methods in a class
- The `self` parameter
- Calling methods
- Methods with parameters and return values

### 5. Page Object Model (POM)
- What is Page Object Model?
- Benefits for test automation
- Creating page classes
- Organizing selectors and actions
- Writing cleaner tests with POM

## 🔧 Why This Matters for Test Automation

Object-Oriented Programming is essential for:
- **Organization**: Group related functionality together
- **Reusability**: Write code once, use it many times
- **Maintainability**: Easier to update and fix
- **Scalability**: Build large test suites effectively
- **Page Object Model**: Industry standard for UI automation
- **Clean Code**: More readable and professional tests

## 📂 Lecture Structure

```
Lecture_9_Classes_Objects_Part1/
├── README.md                          # This file
├── examples/
│   ├── 01_class_basics.py            # Introduction to classes
│   ├── 02_init_method.py             # The __init__ constructor
│   ├── 03_instance_variables.py      # Working with attributes
│   ├── 04_instance_methods.py        # Defining and using methods
│   ├── 05_practical_examples.py      # Real-world class examples
│   └── 06_page_object_model.py       # POM for Playwright
├── exercises/
│   ├── exercise_01_basic_classes.py  # Practice creating classes
│   ├── exercise_02_methods.py        # Practice with methods
│   ├── exercise_03_page_objects.py   # Build page objects
│   └── SOLUTIONS.md                   # Exercise solutions
├── sample_code/
│   ├── login_page.py                 # Example: Login page object
│   └── test_with_pom.py              # Example: Test using POM
└── presentation.html                  # Lecture slides
```

## 🚀 Getting Started

### Run Examples
```bash
# Navigate to examples directory
cd Lecture_9_Classes_Objects_Part1/examples

# Run any example
python 01_class_basics.py
python 02_init_method.py
# ... and so on
```

### Complete Exercises
```bash
# Navigate to exercises directory
cd Lecture_9_Classes_Objects_Part1/exercises

# Work on exercises
python exercise_01_basic_classes.py
python exercise_02_methods.py
python exercise_03_page_objects.py

# Check solutions
cat SOLUTIONS.md
```

## 💡 Key Concepts

### Basic Class Structure
```python
class Dog:
    """A simple Dog class."""

    def __init__(self, name, age):
        """Initialize a new dog."""
        self.name = name
        self.age = age

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")

# Create an instance (object)
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Buddy says Woof!
```

### Page Object Model Example
```python
class LoginPage:
    """Page object for login page."""

    def __init__(self, page):
        """Initialize with Playwright page."""
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def login(self, username, password):
        """Perform login action."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.submit_button)

# Usage in test
login_page = LoginPage(page)
login_page.login("testuser", "password123")
```

## 🎓 Class Terminology

- **Class**: Blueprint or template for creating objects
- **Object**: Instance of a class (actual thing created from blueprint)
- **Instance**: Same as object (one specific example of a class)
- **Instance Variable**: Data that belongs to a specific object
- **Instance Method**: Function that belongs to a class
- **`self`**: Reference to the current instance
- **`__init__`**: Special method called when creating a new object
- **Constructor**: Another name for `__init__` method

## 🏗️ Page Object Model Benefits

### Without POM (Bad):
```python
def test_login():
    page.fill("#username", "testuser")
    page.fill("#password", "password")
    page.click("#submit")
    # Selectors scattered everywhere
    # Hard to maintain if UI changes
```

### With POM (Good):
```python
def test_login():
    login_page = LoginPage(page)
    login_page.login("testuser", "password")
    # Clean, readable, easy to maintain
    # All selectors in one place
```

## 📖 Additional Resources

- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)
- [Selenium Page Objects](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

## ✅ Practice Checklist

- [ ] Complete all examples
- [ ] Understand class vs instance
- [ ] Master `__init__` method
- [ ] Practice creating classes
- [ ] Implement instance methods
- [ ] Build your first page object
- [ ] Write tests using POM
- [ ] Refactor old tests to use POM

## 🎓 Next Steps

After mastering Classes & Objects Part 1:
1. Practice creating different types of classes
2. Build page objects for common pages (login, signup, etc.)
3. Refactor existing tests to use Page Object Model
4. Prepare for **Lecture 10: Classes & Objects (Part 2)** covering:
   - Class methods and static methods
   - Inheritance
   - Encapsulation
   - Advanced POM patterns

---

**Remember**: Classes are blueprints, objects are the actual things you create from those blueprints. Just like a blueprint for a house (class) vs the actual house you build (object)!
