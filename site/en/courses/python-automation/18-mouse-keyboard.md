# Lecture 18: Mouse and Keyboard Actions

Mouse and keyboard actions.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_18_Mouse_Keyboard_Actions/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_18_Mouse_Keyboard_Actions/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_18_Mouse_Keyboard_Actions/exercises" target="_blank">📝 Вправи</a>
</div>

## Click

```python
# Regular click
page.get_by_role("button").click()

# Double click
page.locator(".item").dblclick()

# Right click
page.locator(".item").click(button="right")

# Click with modifiers
page.locator("a").click(modifiers=["Control"])  # Ctrl+Click
```

## Hover

```python
# Hover
page.get_by_text("Menu").hover()

# Hover + Click on submenu
page.get_by_text("Menu").hover()
page.get_by_text("Submenu Item").click()
```

## Drag and Drop

```python
# Simple drag & drop
page.locator("#source").drag_to(page.locator("#target"))

# With coordinates
page.mouse.move(100, 200)
page.mouse.down()
page.mouse.move(300, 400)
page.mouse.up()
```

## Keyboard

```python
# Key press
page.keyboard.press("Enter")
page.keyboard.press("Tab")
page.keyboard.press("Escape")

# Combinations
page.keyboard.press("Control+a")
page.keyboard.press("Control+c")
page.keyboard.press("Control+v")

# On an element
page.get_by_label("Search").press("Enter")
```

## Text Input

```python
# Fast input
page.keyboard.type("Hello World")

# Character-by-character
page.keyboard.type("Hello", delay=100)

# Insert text (without key events)
page.keyboard.insert_text("Hello World")
```
