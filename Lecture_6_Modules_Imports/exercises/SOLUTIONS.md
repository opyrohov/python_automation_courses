# Lecture 6: Modules & Imports - Exercise Solutions

This file contains solutions for all exercises in Lecture 6.

## Exercise 1: Import Basics

### Exercise 1.1: Import Entire Module
```python
import math

result = math.sqrt(144)
print(f"Square root of 144: {result}")
```

### Exercise 1.2: Import Specific Function
```python
from math import sqrt

result = sqrt(225)
print(f"Square root of 225: {result}")
```

### Exercise 1.3: Import Multiple Items
```python
from math import pi, ceil, floor

print(f"Pi: {pi}")
print(f"Ceiling of 7.3: {ceil(7.3)}")
print(f"Floor of 7.8: {floor(7.8)}")
```

### Exercise 1.4: Import with Alias
```python
import datetime as dt

print(f"Current date and time: {dt.datetime.now()}")
```

### Exercise 1.5: Import from Random Module
```python
from random import randint, choice, shuffle

print(f"Random number 1-100: {randint(1, 100)}")

languages = ["Python", "JavaScript", "Java", "C++"]
print(f"Random language: {choice(languages)}")

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(f"Shuffled: {numbers}")
```

### Exercise 1.6: Working with Time Module
```python
import time

print(f"Current timestamp: {time.time()}")
print(f"Formatted time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
```

### Exercise 1.7: Using datetime for Calculations
```python
from datetime import datetime, timedelta

today = datetime.now().date()
print(f"Today: {today}")

future = today + timedelta(days=7)
print(f"7 days from now: {future}")

past = today - timedelta(days=30)
print(f"30 days ago: {past}")
```

### Exercise 1.8: JSON Module Practice
```python
import json

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(person, indent=2)
print(f"JSON string:\n{json_string}")
```

### BONUS: Exploring Module Contents
```python
import random

print(f"Module name: {random.__name__}")

items = [item for item in dir(random) if not item.startswith('_')]
print(f"Available functions (first 10): {items[:10]}")
```

---

## Exercise 2: Creating Your Own Modules

### Exercise 2.1: Create string_utils.py

**File: string_utils.py**
```python
"""String utility functions."""

def reverse_string(text):
    """Return reversed string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize each word."""
    return text.title()

def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    print("Testing string_utils module")
    print(reverse_string("hello"))
```

**Usage:**
```python
from string_utils import reverse_string, capitalize_words, count_vowels

print(reverse_string("Python"))  # nohtyP
print(capitalize_words("hello world"))  # Hello World
print(count_vowels("automation"))  # 5
```

### Exercise 2.2: Create math_utils.py

**File: math_utils.py**
```python
"""Math utility functions."""

def is_even(num):
    """Check if number is even."""
    return num % 2 == 0

def is_prime(num):
    """Check if number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    """Calculate factorial."""
    if num <= 1:
        return 1
    return num * factorial(num - 1)

if __name__ == "__main__":
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 7 prime? {is_prime(7)}")
    print(f"Factorial of 5: {factorial(5)}")
```

**Usage:**
```python
from math_utils import is_even, is_prime, factorial

print(is_even(10))  # True
print(is_prime(17))  # True
print(factorial(5))  # 120
```

### Exercise 2.3: Create test_data_gen.py

**File: test_data_gen.py**
```python
"""Test data generator functions."""
import random

def generate_email():
    """Generate random test email."""
    num = random.randint(100, 999)
    return f"testuser{num}@example.com"

def generate_username():
    """Generate random username."""
    num = random.randint(1000, 9999)
    return f"user_{num}"

def generate_password():
    """Generate random password."""
    chars = "abcdefghijklmnopqrstuvwxyz"
    pwd = ''.join(random.choice(chars) for _ in range(8))
    return f"{pwd.capitalize()}123!"

if __name__ == "__main__":
    print(generate_email())
    print(generate_username())
    print(generate_password())
```

**Usage:**
```python
from test_data_gen import generate_email, generate_username, generate_password

print(generate_email())  # testuser742@example.com
print(generate_username())  # user_3847
print(generate_password())  # Abcdefgh123!
```

### Exercise 2.5: Create config.py

**File: config.py**
```python
"""Configuration constants for tests."""

BASE_URL = "https://example.com"
DEFAULT_TIMEOUT = 30
TEST_BROWSER = "chrome"
ADMIN_USER = {
    "username": "admin",
    "password": "admin123"
}

if __name__ == "__main__":
    print(f"Base URL: {BASE_URL}")
    print(f"Timeout: {DEFAULT_TIMEOUT}")
```

**Usage:**
```python
from config import BASE_URL, DEFAULT_TIMEOUT, TEST_BROWSER, ADMIN_USER

print(f"Navigating to: {BASE_URL}")
print(f"Timeout: {DEFAULT_TIMEOUT}s")
print(f"Browser: {TEST_BROWSER}")
print(f"Admin: {ADMIN_USER['username']}")
```

### Exercise 2.6: Import with Alias
```python
import string_utils as su

result = su.reverse_string("Playwright")
print(f"Reversed: {result}")
```

### Exercise 2.7: Create test_helpers.py

**File: test_helpers.py**
```python
"""Test helper functions."""
import random

def log_test_step(step_name):
    """Log a test step."""
    print(f"[TEST] {step_name}")

def create_test_user(name, email):
    """Create a test user dictionary."""
    return {
        "id": random.randint(1000, 9999),
        "name": name,
        "email": email
    }

def verify_status_code(actual, expected):
    """Verify status code."""
    if actual == expected:
        print(f"✅ Status code {actual} matches expected {expected}")
    else:
        print(f"❌ Status code {actual} does not match expected {expected}")
```

**Usage:**
```python
from test_helpers import log_test_step, create_test_user, verify_status_code

log_test_step("Starting login test")
user = create_test_user("Alice", "alice@test.com")
print(f"Created user: {user}")
verify_status_code(200, 200)
```

### Exercise 2.8: Create validators.py

**File: validators.py**
```python
"""Validation functions."""

def is_valid_email(email):
    """Check if email is valid."""
    return "@" in email and "." in email

def is_strong_password(password):
    """Check if password is strong."""
    return len(password) >= 8

def is_valid_phone(phone):
    """Check if phone is valid."""
    digits = ''.join(c for c in phone if c.isdigit())
    return len(digits) >= 10
```

**Usage:**
```python
from validators import is_valid_email, is_strong_password, is_valid_phone

print(is_valid_email("test@example.com"))  # True
print(is_strong_password("Pass123!"))  # True
print(is_valid_phone("555-123-4567"))  # True
```

---

## Exercise 3: Automation Modules

### Exercise 3.1: Create browser_config.py

**File: browser_config.py**
```python
"""Browser configuration."""

BROWSERS = ["chrome", "firefox", "safari"]
DEFAULT_BROWSER = "chrome"
HEADLESS = False
SLOW_MO = 100

def get_browser_config(browser_name):
    """Get configuration for a browser."""
    return {
        "browser": browser_name,
        "headless": HEADLESS,
        "slow_mo": SLOW_MO
    }
```

**Usage:**
```python
from browser_config import BROWSERS, DEFAULT_BROWSER, get_browser_config

print(f"Available browsers: {BROWSERS}")
print(f"Default: {DEFAULT_BROWSER}")
config = get_browser_config("chrome")
print(f"Config: {config}")
```

### Exercise 3.2: Create locators.py

**File: locators.py**
```python
"""Page locators."""

class LoginPageLocators:
    """Login page locators."""
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-btn"
    ERROR_MESSAGE = ".error-message"

class HomePageLocators:
    """Home page locators."""
    USER_MENU = "#user-menu"
    LOGOUT_BUTTON = "#logout"
    WELCOME_TEXT = ".welcome"
```

**Usage:**
```python
from locators import LoginPageLocators

print(f"Username field: {LoginPageLocators.USERNAME_INPUT}")
print(f"Password field: {LoginPageLocators.PASSWORD_INPUT}")
print(f"Login button: {LoginPageLocators.LOGIN_BUTTON}")
```

### Exercise 3.3: Create wait_helpers.py

**File: wait_helpers.py**
```python
"""Wait helper functions."""

def wait_for_element(selector, timeout=10):
    """Wait for element to appear."""
    print(f"Waiting for element: {selector} (timeout: {timeout}s)")
    return True

def wait_for_text(text, timeout=10):
    """Wait for text to appear."""
    print(f"Waiting for text: '{text}' (timeout: {timeout}s)")
    return True

def wait_for_url(url, timeout=10):
    """Wait for URL to match."""
    print(f"Waiting for URL: {url} (timeout: {timeout}s)")
    return True
```

**Usage:**
```python
from wait_helpers import wait_for_element, wait_for_text, wait_for_url

wait_for_element("#submit-button")
wait_for_text("Welcome")
wait_for_url("/dashboard")
```

### Exercise 3.4: Create screenshot_helper.py

**File: screenshot_helper.py**
```python
"""Screenshot helper functions."""
from datetime import datetime
from pathlib import Path

def create_screenshots_dir():
    """Create screenshots directory."""
    Path("screenshots").mkdir(exist_ok=True)

def take_screenshot(name):
    """Take a screenshot."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    print(f"Taking screenshot: {filename}")
    return filename

def take_full_page_screenshot(name):
    """Take full page screenshot."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_fullpage_{timestamp}.png"
    print(f"Taking full page screenshot: {filename}")
    return filename
```

**Usage:**
```python
from screenshot_helper import take_screenshot, create_screenshots_dir

create_screenshots_dir()
screenshot_path = take_screenshot("login_page")
print(f"Screenshot saved: {screenshot_path}")
```

### Exercise 3.5: Create test_data.py

**File: test_data.py**
```python
"""Test data constants."""

TEST_USERS = {
    "valid": {
        "username": "testuser",
        "password": "Test123!"
    },
    "invalid": {
        "username": "bad",
        "password": "wrong"
    },
    "admin": {
        "username": "admin",
        "password": "Admin123!"
    }
}

TEST_URLS = {
    "login": "https://example.com/login",
    "home": "https://example.com/home",
    "profile": "https://example.com/profile"
}
```

**Usage:**
```python
from test_data import TEST_USERS, TEST_URLS

user = TEST_USERS["valid"]
print(f"Test user: {user['username']}")
print(f"Login URL: {TEST_URLS['login']}")
```

### Exercise 3.9: Complete Test Using Modules

```python
def test_login_flow():
    """Complete login test using all modules."""
    from test_logger import log_test_start, log_test_end, log_info
    from test_data import TEST_USERS, TEST_URLS
    from browser_config import get_browser_config
    from locators import LoginPageLocators
    from actions import click_element, fill_field
    from assertions import assert_text_present, assert_element_visible

    # Start test
    log_test_start("Login Flow Test")

    # Get test data
    user = TEST_USERS["valid"]
    log_info(f"Using test user: {user['username']}")

    # Get config
    config = get_browser_config("chrome")
    log_info(f"Browser config: {config}")

    # Navigate
    log_info(f"Navigating to: {TEST_URLS['login']}")

    # Login
    fill_field(LoginPageLocators.USERNAME_INPUT, user["username"])
    fill_field(LoginPageLocators.PASSWORD_INPUT, user["password"])
    click_element(LoginPageLocators.LOGIN_BUTTON)

    # Verify
    assert_text_present("Welcome")
    assert_element_visible("#user-menu")

    # End test
    log_test_end("Login Flow Test", "PASSED")

test_login_flow()
```

---

## Key Takeaways

1. **Import Patterns**: Multiple ways to import (entire module, specific items, with alias)
2. **Module Creation**: Any .py file can be a module
3. **Organization**: Group related functions in modules
4. **Reusability**: Modules promote code reuse
5. **Maintenance**: Easier to maintain organized code
6. **Testing**: Modules can be tested independently

## Next Steps

- Practice creating your own utility modules
- Organize your test code with modules
- Learn about packages (folders with __init__.py)
- Explore the Python Standard Library
- Install and use Playwright with proper imports

Good luck with your automation journey!
