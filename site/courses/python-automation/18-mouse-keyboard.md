# Lecture 18: Mouse & Keyboard Actions

Дії миші та клавіатури.

<div class="lecture-resources">

<a href="/presentations/Lecture_18_Mouse_Keyboard_Actions/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_18_Mouse_Keyboard_Actions/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_18_Mouse_Keyboard_Actions/exercises)

</div>

## Клік

```python
# Звичайний клік
page.get_by_role("button").click()

# Подвійний клік
page.locator(".item").dblclick()

# Правий клік
page.locator(".item").click(button="right")

# Клік з модифікаторами
page.locator("a").click(modifiers=["Control"])  # Ctrl+Click
```

## Hover

```python
# Наведення
page.get_by_text("Menu").hover()

# Hover + Click на підменю
page.get_by_text("Menu").hover()
page.get_by_text("Submenu Item").click()
```

## Drag and Drop

```python
# Простий drag & drop
page.locator("#source").drag_to(page.locator("#target"))

# З координатами
page.mouse.move(100, 200)
page.mouse.down()
page.mouse.move(300, 400)
page.mouse.up()
```

## Клавіатура

```python
# Натискання клавіші
page.keyboard.press("Enter")
page.keyboard.press("Tab")
page.keyboard.press("Escape")

# Комбінації
page.keyboard.press("Control+a")
page.keyboard.press("Control+c")
page.keyboard.press("Control+v")

# На елементі
page.get_by_label("Search").press("Enter")
```

## Введення тексту

```python
# Швидке введення
page.keyboard.type("Hello World")

# Посимвольне
page.keyboard.type("Hello", delay=100)

# Insert text (без подій клавіш)
page.keyboard.insert_text("Hello World")
```
