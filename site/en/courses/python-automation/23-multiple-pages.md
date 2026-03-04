# Lecture 23: Multiple Pages and Windows

Working with multiple pages and windows.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_23_Multiple_Pages_Windows/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_23_Multiple_Pages_Windows/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_23_Multiple_Pages_Windows/exercises" target="_blank">📝 Вправи</a>
</div>

## New Window/Tab

```python
# Wait for a new page
with context.expect_page() as new_page_info:
    page.get_by_text("Open in new tab").click()

new_page = new_page_info.value
new_page.wait_for_load_state()
print(new_page.title())
```

## Multiple Pages in a Context

```python
# Creating multiple pages
page1 = context.new_page()
page2 = context.new_page()

page1.goto("https://example.com/login")
page2.goto("https://example.com/register")

# All pages
for p in context.pages:
    print(p.url)
```

## Popup Windows

```python
# Wait for popup
with page.expect_popup() as popup_info:
    page.get_by_text("Open popup").click()

popup = popup_info.value
popup.wait_for_load_state()

# Interact with popup
popup.get_by_label("Email").fill("test@example.com")
popup.close()
```

## Dialogs (alert, confirm, prompt)

```python
# Handling dialogs
def handle_dialog(dialog):
    print(f"Dialog: {dialog.message}")
    dialog.accept()  # or dialog.dismiss()

page.on("dialog", handle_dialog)
page.get_by_role("button", name="Show Alert").click()

# For prompt
def handle_prompt(dialog):
    dialog.accept("My input")

page.on("dialog", handle_prompt)
```

## Example: OAuth Popup

```python
with page.expect_popup() as popup_info:
    page.get_by_role("button", name="Login with Google").click()

oauth_popup = popup_info.value
oauth_popup.get_by_label("Email").fill("user@gmail.com")
oauth_popup.get_by_role("button", name="Next").click()
# ... popup will close automatically after authorization

# Return to the main page
expect(page.get_by_text("Welcome")).to_be_visible()
```
