# Lecture 16: Locator Strategies Part 2

CSS та XPath селектори.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_16_Locator_Strategies_Part2/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_16_Locator_Strategies_Part2/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_16_Locator_Strategies_Part2/exercises)

</div>

## CSS Селектори

```python
# По ID
page.locator("#login-btn")

# По класу
page.locator(".submit-button")

# По атрибуту
page.locator("[data-testid='submit']")
page.locator("input[type='email']")

# Комбінації
page.locator("form.login input[name='email']")

# Псевдо-селектори
page.locator("li:first-child")
page.locator("li:nth-child(2)")
```

## XPath Селектори

```python
# Базовий XPath
page.locator("//button[@type='submit']")

# По тексту
page.locator("//span[text()='Submit']")
page.locator("//button[contains(text(), 'Sign')]")

# По атрибуту
page.locator("//input[@placeholder='Email']")

# Навігація по DOM
page.locator("//div[@class='card']//button")
page.locator("//table//tr[2]/td[1]")
```

## Коли що використовувати

| Ситуація | Рекомендація |
|----------|--------------|
| Є data-testid | `get_by_test_id()` |
| Кнопка/посилання | `get_by_role()` |
| Поле форми | `get_by_label()` |
| Складна структура | CSS селектор |
| Текст в середині | XPath з contains() |
