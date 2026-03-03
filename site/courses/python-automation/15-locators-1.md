# Лекція 15: Стратегії пошуку елементів. Частина 1

Стратегії пошуку елементів — рекомендовані локатори.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_15_Locator_Strategies_Part1/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Що таке локатори
- Рекомендовані локатори
- get_by_role
- get_by_text
- get_by_label

## Що таке локатори?

Локатор — це спосіб знайти елемент на сторінці для взаємодії з ним.

**Пріоритет локаторів (від найкращого):**
1. `get_by_role` — по ролі елемента
2. `get_by_text` — по тексту
3. `get_by_label` — по label форми
4. `get_by_placeholder` — по placeholder
5. `get_by_test_id` — по data-testid
6. CSS/XPath — як останній варіант

## get_by_role

```python
# Кнопки
page.get_by_role("button", name="Submit")
page.get_by_role("button", name="Sign In")

# Посилання
page.get_by_role("link", name="Home")
page.get_by_role("link", name="About Us")

# Текстові поля
page.get_by_role("textbox", name="Email")

# Checkbox
page.get_by_role("checkbox", name="Remember me")

# Заголовки
page.get_by_role("heading", name="Welcome")
page.get_by_role("heading", level=1)

# Список
page.get_by_role("list")
page.get_by_role("listitem")
```

## Ролі елементів

| HTML елемент | Роль |
|-------------|------|
| `<button>` | button |
| `<a>` | link |
| `<input type="text">` | textbox |
| `<input type="checkbox">` | checkbox |
| `<input type="radio">` | radio |
| `<select>` | combobox |
| `<h1>-<h6>` | heading |
| `<ul>`, `<ol>` | list |
| `<li>` | listitem |
| `<table>` | table |
| `<tr>` | row |
| `<img>` | img |

## get_by_text

```python
# Точне співпадіння
page.get_by_text("Welcome", exact=True)

# Часткове співпадіння (default)
page.get_by_text("Welcome")  # знайде "Welcome to our site"

# Регулярний вираз
import re
page.get_by_text(re.compile(r"Welcome.*"))
```

## get_by_label

```python
# <label for="email">Email</label>
# <input id="email">
page.get_by_label("Email")

# <label>
#   Password
#   <input type="password">
# </label>
page.get_by_label("Password")
```

## get_by_placeholder

```python
# <input placeholder="Enter your email">
page.get_by_placeholder("Enter your email")

# Часткове співпадіння
page.get_by_placeholder("email")
```

## get_by_alt_text

```python
# <img alt="Company Logo">
page.get_by_alt_text("Company Logo")

# Для картинок
page.get_by_alt_text("Profile picture")
```

## get_by_title

```python
# <button title="Close dialog">×</button>
page.get_by_title("Close dialog")
```

## get_by_test_id

```python
# <button data-testid="submit-btn">Submit</button>
page.get_by_test_id("submit-btn")

# Найстабільніший локатор для критичних елементів
page.get_by_test_id("login-button")
page.get_by_test_id("user-profile")
```

## Комбінування локаторів

```python
# Фільтрація
page.get_by_role("listitem").filter(has_text="Product A")

# Вкладені локатори
card = page.get_by_test_id("product-card")
card.get_by_role("button", name="Buy")

# Ланцюжок
page.get_by_role("list").get_by_role("listitem").first
```

## Вправи

::: tip Вправа 1
Знайдіть всі кнопки на сторінці та виведіть їх текст.
:::

::: tip Вправа 2
Напишіть тест, що заповнює форму використовуючи тільки рекомендовані локатори.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/examples)
