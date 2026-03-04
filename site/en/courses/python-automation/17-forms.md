# Lecture 17: Working with Forms

Working with forms.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_17_Form_Handling/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_17_Form_Handling/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_17_Form_Handling/exercises" target="_blank">📝 Вправи</a>
</div>

## Input Fields

```python
# Fill (clears before typing)
page.get_by_label("Email").fill("user@test.com")

# Character-by-character typing
page.get_by_label("Search").type("query", delay=100)

# Clear
page.get_by_label("Email").clear()
```

## Checkbox and Radio

```python
# Checkbox
page.get_by_label("Remember me").check()
page.get_by_label("Remember me").uncheck()

# Check state
is_checked = page.get_by_label("Remember me").is_checked()

# Radio
page.get_by_label("Option A").check()
```

## Select (Dropdown)

```python
# By value
page.get_by_label("Country").select_option("ua")

# By text
page.get_by_label("Country").select_option(label="Ukraine")

# By index
page.get_by_label("Country").select_option(index=2)

# Multiple selection
page.locator("select").select_option(["opt1", "opt2"])
```

## File Upload

```python
# Single file
page.get_by_label("Upload").set_input_files("file.pdf")

# Multiple files
page.get_by_label("Upload").set_input_files(["file1.pdf", "file2.pdf"])

# Clear
page.get_by_label("Upload").set_input_files([])
```

## Complete Form

```python
def fill_registration_form(page):
    page.get_by_label("Name").fill("John Doe")
    page.get_by_label("Email").fill("john@example.com")
    page.get_by_label("Password").fill("SecurePass123")
    page.get_by_label("Country").select_option("ua")
    page.get_by_label("I agree").check()
    page.get_by_role("button", name="Register").click()
```
