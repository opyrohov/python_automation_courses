# Lecture 21: Multiple Elements

Робота з множиною елементів.

<div class="lecture-resources">

<a href="/presentations/Lecture_21_Multiple_Elements/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_21_Multiple_Elements/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_21_Multiple_Elements/exercises)

</div>

## Базові операції

```python
# Отримання всіх елементів
items = page.locator(".product-card")

# Кількість
count = items.count()
print(f"Found {count} items")

# Перший / Останній
items.first.click()
items.last.click()

# По індексу
items.nth(2).click()
```

## Ітерація

```python
items = page.locator(".product-card")

# Цикл по елементах
for i in range(items.count()):
    item = items.nth(i)
    print(item.text_content())

# all() повертає список
all_items = items.all()
for item in all_items:
    print(item.text_content())
```

## Фільтрація

```python
# По тексту
page.locator(".card").filter(has_text="Sale").click()

# По вкладеному елементу
page.locator(".card").filter(
    has=page.get_by_role("button", name="Buy")
).first.click()

# Комбінація
page.locator(".product").filter(has_text="iPhone").filter(
    has=page.locator(".in-stock")
).first.click()
```

## Приклад: Таблиця

```python
# Знайти рядок з текстом
row = page.locator("table tr").filter(has_text="John Doe")

# Клікнути кнопку в цьому рядку
row.get_by_role("button", name="Edit").click()

# Отримати значення з колонки
cells = row.locator("td")
name = cells.nth(0).text_content()
email = cells.nth(1).text_content()
```

## Приклад: Список товарів

```python
def get_all_product_names(page):
    products = page.locator(".product-card")
    names = []
    for i in range(products.count()):
        name = products.nth(i).locator(".product-name").text_content()
        names.append(name)
    return names

def click_product_by_name(page, name):
    page.locator(".product-card").filter(has_text=name).click()
```

## Assertions для колекцій

```python
from playwright.sync_api import expect

# Перевірка кількості
expect(page.locator(".item")).to_have_count(5)

# Перевірка тексту всіх елементів
expect(page.locator(".item")).to_have_text([
    "First",
    "Second",
    "Third"
])
```
