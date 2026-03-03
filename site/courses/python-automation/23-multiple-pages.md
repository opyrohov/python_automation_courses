# Lecture 23: Multiple Pages & Windows

Робота з кількома сторінками та вікнами.

<div class="lecture-resources">

<a href="/presentations/Lecture_23_Multiple_Pages_Windows/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_23_Multiple_Pages_Windows/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_23_Multiple_Pages_Windows/exercises)

</div>

## Нове вікно/вкладка

```python
# Очікування нової сторінки
with context.expect_page() as new_page_info:
    page.get_by_text("Open in new tab").click()

new_page = new_page_info.value
new_page.wait_for_load_state()
print(new_page.title())
```

## Кілька сторінок в контексті

```python
# Створення кількох сторінок
page1 = context.new_page()
page2 = context.new_page()

page1.goto("https://example.com/login")
page2.goto("https://example.com/register")

# Всі сторінки
for p in context.pages:
    print(p.url)
```

## Popup вікна

```python
# Очікування popup
with page.expect_popup() as popup_info:
    page.get_by_text("Open popup").click()

popup = popup_info.value
popup.wait_for_load_state()

# Взаємодія з popup
popup.get_by_label("Email").fill("test@example.com")
popup.close()
```

## Діалоги (alert, confirm, prompt)

```python
# Обробка діалогів
def handle_dialog(dialog):
    print(f"Dialog: {dialog.message}")
    dialog.accept()  # або dialog.dismiss()

page.on("dialog", handle_dialog)
page.get_by_role("button", name="Show Alert").click()

# Для prompt
def handle_prompt(dialog):
    dialog.accept("My input")

page.on("dialog", handle_prompt)
```

## Приклад: OAuth popup

```python
with page.expect_popup() as popup_info:
    page.get_by_role("button", name="Login with Google").click()

oauth_popup = popup_info.value
oauth_popup.get_by_label("Email").fill("user@gmail.com")
oauth_popup.get_by_role("button", name="Next").click()
# ... popup закриється автоматично після авторизації

# Повернення до основної сторінки
expect(page.get_by_text("Welcome")).to_be_visible()
```
