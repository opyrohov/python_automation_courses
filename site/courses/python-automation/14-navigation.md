# Lecture 14: Navigation & Interactions

Базова навігація та взаємодія з елементами.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_14_Basic_Navigation_Interactions/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/exercises)

</div>

## Теми лекції

- Навігація по сторінках
- Клік та введення тексту
- Базові взаємодії
- Очікування завантаження

## Навігація

```python
# Перехід на URL
page.goto("https://example.com")

# Опції навігації
page.goto("https://example.com", wait_until="load")
page.goto("https://example.com", wait_until="domcontentloaded")
page.goto("https://example.com", wait_until="networkidle")

# Таймаут
page.goto("https://example.com", timeout=30000)
```

## Клік

```python
# Простий клік
page.click("button")
page.click("#submit-btn")
page.click("text=Sign In")

# Подвійний клік
page.dblclick("button")

# Правий клік
page.click("button", button="right")

# Клік з модифікаторами
page.click("button", modifiers=["Shift"])
```

## Введення тексту

```python
# Заповнення поля (очищує перед введенням)
page.fill("input[name='email']", "user@test.com")

# Посимвольне введення
page.type("input[name='email']", "user@test.com", delay=100)

# Очищення
page.fill("input", "")

# Натискання клавіш
page.press("input", "Enter")
page.press("input", "Control+a")
```

## Checkbox та Radio

```python
# Checkbox
page.check("input[type='checkbox']")
page.uncheck("input[type='checkbox']")
is_checked = page.is_checked("input[type='checkbox']")

# Radio
page.check("input[type='radio'][value='option1']")
```

## Select (випадаючі списки)

```python
# По значенню
page.select_option("select#country", "ua")

# По тексту
page.select_option("select#country", label="Ukraine")

# По індексу
page.select_option("select#country", index=2)

# Множинний вибір
page.select_option("select", ["opt1", "opt2"])
```

## Hover

```python
page.hover("button.menu")

# Hover та клік на підменю
page.hover("button.menu")
page.click("a.submenu-item")
```

## Отримання інформації

```python
# Текст елемента
text = page.text_content("h1")
inner_text = page.inner_text("p")

# Атрибут
href = page.get_attribute("a", "href")

# Значення input
value = page.input_value("input[name='email']")

# Видимість
is_visible = page.is_visible("button")
is_enabled = page.is_enabled("button")
```

## Очікування

```python
# Очікування елемента
page.wait_for_selector("button.loaded")
page.wait_for_selector("button", state="visible")
page.wait_for_selector("dialog", state="hidden")

# Очікування навігації
page.wait_for_url("**/dashboard")

# Очікування завантаження
page.wait_for_load_state("networkidle")

# Довільна умова
page.wait_for_function("() => document.title === 'Ready'")
```

## Вправи

::: tip Вправа 1
Напишіть скрипт для автозаповнення форми реєстрації.
:::

::: tip Вправа 2
Створіть скрипт для навігації по меню з підменю.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_14_Basic_Navigation_Interactions/examples)
