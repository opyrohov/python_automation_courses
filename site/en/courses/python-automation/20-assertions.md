# Lecture 20: Assertions

Checks and assertions.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_20_Assertions/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_20_Assertions/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_20_Assertions/exercises" target="_blank">📝 Вправи</a>
</div>

## Playwright Assertions

```python
from playwright.sync_api import expect

# Visibility
expect(page.get_by_text("Welcome")).to_be_visible()
expect(page.locator(".error")).not_to_be_visible()

# Text
expect(page.locator("h1")).to_have_text("Dashboard")
expect(page.locator("p")).to_contain_text("success")

# Attributes
expect(page.locator("input")).to_have_attribute("type", "email")
expect(page.locator("input")).to_have_value("test@example.com")
```

## Page Assertions

```python
# URL
expect(page).to_have_url("https://example.com/dashboard")
expect(page).to_have_url(re.compile(r".*/dashboard"))

# Title
expect(page).to_have_title("Dashboard - App")
expect(page).to_have_title(re.compile(r"Dashboard.*"))
```

## Element State

```python
# Enabled/Disabled
expect(page.get_by_role("button")).to_be_enabled()
expect(page.get_by_role("button")).to_be_disabled()

# Checked
expect(page.get_by_role("checkbox")).to_be_checked()
expect(page.get_by_role("checkbox")).not_to_be_checked()

# Focused
expect(page.get_by_label("Email")).to_be_focused()

# Editable
expect(page.locator("input")).to_be_editable()
```

## Collections

```python
# Number of elements
expect(page.locator(".item")).to_have_count(5)

# Text in a list
expect(page.locator(".item")).to_have_text([
    "Item 1",
    "Item 2",
    "Item 3"
])
```

## Soft Assertions

```python
# Continue the test even if an assertion fails
expect(page.get_by_text("Welcome")).to_be_visible()  # Hard
# Soft assertions in pytest-playwright via plugins
```

## Timeout for Assertions

```python
# Default: 5 seconds
expect(page.get_by_text("Loaded")).to_be_visible()

# Custom timeout
expect(page.get_by_text("Loaded")).to_be_visible(timeout=10000)
```
