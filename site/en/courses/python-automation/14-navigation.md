# Lecture 14: Navigation and Interaction

Basic navigation and interaction with elements.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_14_Basic_Navigation_Interactions/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/exercises" target="_blank">📝 Вправи</a>
</div>

## Lecture Topics

- Page navigation
- Click and text input
- Basic interactions
- Waiting for page load

## Navigation

```python
# Go to URL
page.goto("https://example.com")

# Navigation options
page.goto("https://example.com", wait_until="load")
page.goto("https://example.com", wait_until="domcontentloaded")
page.goto("https://example.com", wait_until="networkidle")

# Timeout
page.goto("https://example.com", timeout=30000)
```

## Click

```python
# Simple click
page.click("button")
page.click("#submit-btn")
page.click("text=Sign In")

# Double click
page.dblclick("button")

# Right click
page.click("button", button="right")

# Click with modifiers
page.click("button", modifiers=["Shift"])
```

## Text Input

```python
# Fill field (clears before typing)
page.fill("input[name='email']", "user@test.com")

# Character-by-character typing
page.type("input[name='email']", "user@test.com", delay=100)

# Clear
page.fill("input", "")

# Key presses
page.press("input", "Enter")
page.press("input", "Control+a")
```

## Checkbox and Radio

```python
# Checkbox
page.check("input[type='checkbox']")
page.uncheck("input[type='checkbox']")
is_checked = page.is_checked("input[type='checkbox']")

# Radio
page.check("input[type='radio'][value='option1']")
```

## Select (Dropdowns)

```python
# By value
page.select_option("select#country", "ua")

# By text
page.select_option("select#country", label="Ukraine")

# By index
page.select_option("select#country", index=2)

# Multiple selection
page.select_option("select", ["opt1", "opt2"])
```

## Hover

```python
page.hover("button.menu")

# Hover and click on submenu
page.hover("button.menu")
page.click("a.submenu-item")
```

## Getting Information

```python
# Element text
text = page.text_content("h1")
inner_text = page.inner_text("p")

# Attribute
href = page.get_attribute("a", "href")

# Input value
value = page.input_value("input[name='email']")

# Visibility
is_visible = page.is_visible("button")
is_enabled = page.is_enabled("button")
```

## Waiting

```python
# Wait for element
page.wait_for_selector("button.loaded")
page.wait_for_selector("button", state="visible")
page.wait_for_selector("dialog", state="hidden")

# Wait for navigation
page.wait_for_url("**/dashboard")

# Wait for page load
page.wait_for_load_state("networkidle")

# Custom condition
page.wait_for_function("() => document.title === 'Ready'")
```

## Exercises

::: tip Exercise 1
Write a script to auto-fill a registration form.
:::

::: tip Exercise 2
Create a script to navigate through a menu with submenus.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/examples)
