# Lecture 20: Assertions in Playwright

## Overview
Master Playwright's powerful expect() assertions to create robust, self-verifying tests with auto-waiting and retry logic.

## Quick Reference

### Visibility Assertions
```python
from playwright.sync_api import expect

# Visibility
expect(page.locator("#element")).to_be_visible()
expect(page.locator("#element")).to_be_hidden()
expect(page.locator("#element")).not_to_be_visible()

# State
expect(page.locator("#button")).to_be_enabled()
expect(page.locator("#button")).to_be_disabled()
expect(page.locator("#checkbox")).to_be_checked()
expect(page.locator("#input")).to_be_editable()

# Attachment
expect(page.locator("#element")).to_be_attached()
expect(page.locator("#element")).to_be_in_viewport()
```

### Text Assertions
```python
# Exact text match
expect(page.locator("h1")).to_have_text("Welcome")

# Contains text
expect(page.locator(".message")).to_contain_text("Success")

# Input value
expect(page.locator("#username")).to_have_value("john.doe")

# Multiple elements
expect(page.locator("li")).to_have_text(["Item 1", "Item 2", "Item 3"])

# Regex pattern
import re
expect(page.locator("#price")).to_have_text(re.compile(r"\$\d+\.\d{2}"))
```

### Attribute Assertions
```python
# Attribute value
expect(page.locator("#link")).to_have_attribute("href", "/dashboard")

# Class
expect(page.locator("#button")).to_have_class("btn-primary")

# ID
expect(page.locator("div").first).to_have_id("main-container")

# CSS property
expect(page.locator("#button")).to_have_css("background-color", "rgb(0, 123, 255)")
```

### Count Assertions
```python
# Exact count
expect(page.locator(".product")).to_have_count(12)

# No elements
expect(page.locator(".error")).to_have_count(0)

# With timeout
expect(page.locator(".result")).to_have_count(10, timeout=10000)
```

### URL & Title Assertions
```python
# URL - exact
expect(page).to_have_url("https://example.com/dashboard")

# URL - pattern
expect(page).to_have_url("**/dashboard")

# URL - regex
import re
expect(page).to_have_url(re.compile(r".*/user/\d+"))

# Title
expect(page).to_have_title("Dashboard - My App")
expect(page).to_have_title(re.compile(r".*Dashboard.*"))
```

## All Assertion Methods

### Element State
| Assertion | Description |
|-----------|-------------|
| `to_be_visible()` | Element is visible |
| `to_be_hidden()` | Element is not visible |
| `to_be_attached()` | Element is in DOM |
| `to_be_enabled()` | Element is enabled |
| `to_be_disabled()` | Element is disabled |
| `to_be_editable()` | Element can be edited |
| `to_be_checked()` | Checkbox/radio is checked |
| `to_be_in_viewport()` | Element is in viewport |

### Text & Value
| Assertion | Description |
|-----------|-------------|
| `to_have_text()` | Exact text match |
| `to_contain_text()` | Contains text |
| `to_have_value()` | Input field value |

### Attributes
| Assertion | Description |
|-----------|-------------|
| `to_have_attribute()` | Has attribute with value |
| `to_have_class()` | Has CSS class |
| `to_have_id()` | Has specific ID |
| `to_have_css()` | Has CSS property value |

### Count
| Assertion | Description |
|-----------|-------------|
| `to_have_count()` | Number of matched elements |

### Page Properties
| Assertion | Description |
|-----------|-------------|
| `to_have_url()` | Page URL matches |
| `to_have_title()` | Page title matches |

## Key Features

### 1. Auto-Waiting & Retry
```python
# Automatically waits up to 5 seconds (default)
expect(page.locator("#element")).to_be_visible()

# Custom timeout
expect(page.locator("#slow")).to_be_visible(timeout=10000)
```

### 2. Negative Assertions
```python
# Positive
expect(page.locator("#element")).to_be_visible()

# Negative - use not_ prefix
expect(page.locator("#element")).not_to_be_visible()
```

### 3. Regex Support
```python
import re

# Text pattern
expect(page.locator("#email")).to_have_value(re.compile(r".*@example\.com"))

# URL pattern
expect(page).to_have_url(re.compile(r".*/dashboard"))

# Case-insensitive
expect(page.locator(".status")).to_contain_text(re.compile(r"complete", re.IGNORECASE))
```

## Common Patterns

### Pattern 1: Verify Action Result
```python
# Perform action
page.locator("#submit-btn").click()

# Verify result
expect(page.locator(".success-message")).to_be_visible()
expect(page.locator(".success-message")).to_contain_text("Saved successfully")
```

### Pattern 2: Verify Navigation
```python
# Click link
page.locator("#dashboard-link").click()

# Verify navigation
expect(page).to_have_url("**/dashboard")
expect(page).to_have_title(re.compile(r".*Dashboard.*"))
```

### Pattern 3: Verify Form Validation
```python
# Submit empty form
page.locator("#submit").click()

# Verify error message
expect(page.locator(".error")).to_be_visible()
expect(page.locator(".error")).to_contain_text("Email is required")
expect(page.locator("#email")).to_have_class("is-invalid")
```

### Pattern 4: Verify List Changes
```python
# Initial state
expect(page.locator(".item")).to_have_count(5)

# Add item
page.locator("#add-btn").click()

# Verify count increased
expect(page.locator(".item")).to_have_count(6)
```

### Pattern 5: Verify Element State
```python
# Button should be disabled initially
expect(page.locator("#submit")).to_be_disabled()

# Fill required field
page.locator("#email").fill("test@example.com")

# Button should be enabled now
expect(page.locator("#submit")).to_be_enabled()
```

## Best Practices

### ✅ DO
- Use `expect()` for all assertions
- Be specific about what you're asserting
- Use regex for flexible text matching
- Combine related assertions
- Set appropriate timeouts for slow operations
- Use negative assertions to verify absence

### ❌ DON'T
- Use Python's `assert` for element checks
- Over-assert implementation details
- Use very long timeouts (> 30 seconds)
- Ignore assertion failures
- Assert too many things at once
- Skip error case assertions

## Assertion vs Python assert

```python
# ❌ BAD - No auto-waiting, immediate failure
assert page.locator("#element").is_visible()

# ✅ GOOD - Auto-waits and retries
expect(page.locator("#element")).to_be_visible()
```

## Examples Included
1. `01_visibility_assertions.py` - Visibility and state checks
2. `02_text_assertions.py` - Text and value verification
3. `03_attribute_assertions.py` - Attribute and CSS checks
4. `04_count_assertions.py` - Counting elements
5. `05_url_title_assertions.py` - URL and title verification
6. `06_combined_assertions.py` - Complete test examples

## Resources
- [Playwright Assertions](https://playwright.dev/python/docs/test-assertions)
- [expect() API](https://playwright.dev/python/docs/api/class-locatorassertions)
- [Auto-waiting](https://playwright.dev/python/docs/actionability)
