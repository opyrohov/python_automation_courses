# Лекція 21: Робота з множинними елементами

**Курс автоматизації Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 21
## Робота з множинними елементами

Курс автоматизації Python + Playwright

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Знаходити та працювати з множинними елементами
- Ефективно використовувати locator.all()
- Ітерувати через колекції елементів
- Динамічно підраховувати елементи
- Обробляти таблиці (рядки, комірки)
- Працювати з динамічними списками
- Фільтрувати та знаходити конкретні елементи

---

## Слайд 3: Чому робота з множинними елементами важлива

Реальні застосунки містять списки, таблиці, сітки — необхідно ефективно працювати з колекціями елементів.

### Типові сценарії використання:

- 📋 Перевірка вмісту списків
- 🔍 Пошук конкретних елементів у колекціях
- 📊 Обробка табличних даних
- ✅ Валідація результатів пошуку
- 🎯 Вибір елементів з випадаючих списків
- 📈 Обробка динамічного контенту

---

## Слайд 4: Частина 1 — Знаходження множинних елементів

# Частина 1
## Знаходження множинних елементів

Отримання колекцій елементів

---

## Слайд 5: locator.all() — Отримання всіх відповідних елементів

Метод **all()** повертає список усіх елементів, що відповідають локатору.

```python
# Отримати всі елементи за локатором
items = page.locator(".item").all()

# Повертає список об'єктів Locator
print(f"Знайдено {len(items)} елементів")

# Кожен елемент є Locator
for item in items:
    print(item.text_content())

# Порожній список, якщо немає збігів
no_items = page.locator(".nonexistent").all()
print(len(no_items))  # 0
```

**Важливо:** all() повертає список — обчислюється негайно (не ліниво)

---

## Слайд 6: count() — Отримання кількості елементів

Метод **count()** повертає кількість знайдених елементів без їх завантаження.

```python
# Підрахувати відповідні елементи
count = page.locator(".product").count()
print(f"Знайдено {count} продуктів")

# Використання з assertions
from playwright.sync_api import expect
expect(page.locator(".product")).to_have_count(10)

# Підрахунок без завантаження всіх елементів
# Ефективніше ніж len(locator.all())
total = page.locator("li").count()
print(f"Всього елементів: {total}")
```

---

## Слайд 7: Порівняння all() та count()

### all() — Повертає список

```python
# Отримати всі елементи
items = page.locator(".item").all()

# Використовувати коли потрібно:
# - Ітерувати через елементи
# - Отримати доступ до властивостей елементів
# - Виконати дії над кожним елементом

for item in items:
    print(item.text_content())
```

### count() — Повертає число

```python
# Отримати тільки кількість
count = page.locator(".item").count()

# Використовувати коли потрібно:
# - Тільки кількість елементів
# - Верифікація
# - Більш ефективний метод

if count > 10:
    print("Багато елементів")
```

---

## Слайд 8: first, last та nth() — Доступ за позицією

```python
# first — перший елемент
first_link = page.locator("ul li a").first
print(f"Перше посилання: {first_link.text_content()}")

# last — останній елемент
last_link = page.locator("ul li a").last
print(f"Останнє посилання: {last_link.text_content()}")

# nth(index) — елемент за індексом (з 0)
third_link = page.locator("ul li a").nth(2)
print(f"Третє посилання: {third_link.text_content()}")

tenth_link = page.locator("ul li a").nth(9)
print(f"Десяте посилання: {tenth_link.text_content()}")
```

---

## Слайд 9: Частина 2 — Ітерація через елементи

# Частина 2
## Ітерація через елементи

Обробка колекцій елементів

---

## Слайд 10: Базова ітерація

```python
# Метод 1: Використання all()
items = page.locator(".item").all()
for item in items:
    text = item.text_content()
    print(f"Елемент: {text}")

# Метод 2: Використання count() та nth()
count = page.locator(".item").count()
for i in range(count):
    item = page.locator(".item").nth(i)
    text = item.text_content()
    print(f"Елемент {i}: {text}")

# Метод 3: Використання enumerate
for i, item in enumerate(page.locator(".item").all()):
    print(f"Позиція {i}: {item.text_content()}")
```

---

## Слайд 11: Екстракція даних з елементів

```python
# Екстракція тексту з усіх елементів
products = page.locator(".product-name").all()
names = [p.text_content() for p in products]
print(names)  # ['Product 1', 'Product 2', ...]

# Екстракція атрибутів
links = page.locator("a").all()
urls = [link.get_attribute("href") for link in links]

# Екстракція кількох властивостей
items = page.locator(".product").all()
data = []
for item in items:
    data.append({
        'name': item.locator(".name").text_content(),
        'price': item.locator(".price").text_content(),
        'id': item.get_attribute("data-id")
    })
print(data)
```

---

## Слайд 12: Фільтрація під час ітерації

```python
# Пошук елементів за умовою
items = page.locator(".product").all()
expensive_items = []

for item in items:
    price_text = item.locator(".price").text_content()
    price = float(price_text.replace("$", ""))
    if price > 100:
        expensive_items.append(item)

print(f"Знайдено {len(expensive_items)} дорогих товарів")

# Використання list comprehension
items = page.locator(".item").all()
visible_items = [item for item in items if item.is_visible()]
print(f"Видимих: {len(visible_items)}")
```

---

## Слайд 13: Частина 3 — Робота з таблицями

# Частина 3
## Робота з таблицями

Обробка рядків та комірок

---

## Слайд 14: Основи роботи з таблицями

```python
# Отримати всі рядки
rows = page.locator("table tbody tr").all()
print(f"Таблиця має {len(rows)} рядків")

# Отримати комірки першого рядка
first_row = page.locator("table tbody tr").first
cells = first_row.locator("td").all()
print(f"Рядок має {len(cells)} комірок")

# Отримати всі комірки таблиці
all_cells = page.locator("table tbody tr td").all()

# Отримати конкретну комірку (рядок 2, колонка 3)
cell = page.locator("table tbody tr").nth(1).locator("td").nth(2)
print(cell.text_content())
```

---

## Слайд 15: Екстракція даних таблиці

```python
# Екстракція таблиці як списку списків
rows = page.locator("table tbody tr").all()
table_data = []

for row in rows:
    cells = row.locator("td").all()
    row_data = [cell.text_content() for cell in cells]
    table_data.append(row_data)

print(table_data)
# [['John', 'Doe', '30'], ['Jane', 'Smith', '25'], ...]

# Екстракція як список словників (з заголовками)
headers = [h.text_content() for h in page.locator("table th").all()]
rows = page.locator("table tbody tr").all()
table_data = []

for row in rows:
    cells = row.locator("td").all()
    row_dict = {headers[i]: cells[i].text_content() for i in range(len(headers))}
    table_data.append(row_dict)

print(table_data)
# [{'Name': 'John', 'Age': '30'}, ...]
```

---

## Слайд 16: Пошук рядків за вмістом

```python
# Пошук рядка, що містить певний текст
rows = page.locator("table tbody tr").all()
for row in rows:
    if "Smith" in row.text_content():
        print("Знайдено рядок зі Smith!")
        # Клік на кнопку в цьому рядку
        row.locator("button").click()
        break

# Пошук рядка за значенням комірки
for row in rows:
    cells = row.locator("td").all()
    if cells[0].text_content() == "John":
        # Отримати інші дані з рядка
        age = cells[2].text_content()
        print(f"Вік John: {age}")

# Використання filter
row = page.locator("table tbody tr").filter(has_text="John")
row.locator(".edit-btn").click()
```

---

## Слайд 17: Сортування та пошук в таблицях

```python
# Екстракція та сортування даних
rows = page.locator("table tbody tr").all()
data = []

for row in rows:
    cells = row.locator("td").all()
    data.append({
        'name': cells[0].text_content(),
        'age': int(cells[1].text_content()),
        'city': cells[2].text_content()
    })

# Сортування за віком
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

# Пошук конкретного запису
result = next((item for item in data if item['name'] == 'John'), None)
if result:
    print(f"Знайдено: {result}")
```

---

## Слайд 18: Частина 4 — Динамічний контент

# Частина 4
## Динамічний контент

Обробка змінюваних списків елементів

---

## Слайд 19: Обробка динамічних списків

```python
# Очікування конкретної кількості
from playwright.sync_api import expect
expect(page.locator(".product")).to_have_count(10)

# Очікування хоча б одного елемента
page.wait_for_selector(".product")
products = page.locator(".product").all()

# Обробка infinite scroll
previous_count = 0
while True:
    current_count = page.locator(".item").count()
    if current_count == previous_count:
        break  # Більше немає елементів для завантаження
    previous_count = current_count
    page.mouse.wheel(0, 1000)  # Прокрутка вниз
    page.wait_for_timeout(1000)  # Очікування завантаження
```

---

## Слайд 20: Додавання та видалення елементів

```python
# Перевірка початкової кількості
initial_count = page.locator(".item").count()

# Додавання нового елемента
page.locator("#add-btn").click()

# Верифікація збільшення кількості
expect(page.locator(".item")).to_have_count(initial_count + 1)

# Отримання нового елемента (останнього)
new_item = page.locator(".item").last

# Видалення елемента
page.locator(".item").first.locator(".delete-btn").click()

# Верифікація зменшення кількості
expect(page.locator(".item")).to_have_count(initial_count)
```

---

## Слайд 21: Оновлення списку елементів

```python
# НЕПРАВИЛЬНО — елементи стають застарілими
items = page.locator(".item").all()
page.locator("#add-btn").click()
# items тепер застарілий!

# ПРАВИЛЬНО — повторний запит після змін
def get_items():
    return page.locator(".item").all()

items = get_items()
print(f"Початкова кількість: {len(items)}")

page.locator("#add-btn").click()
items = get_items()  # Оновлення списку
print(f"Після додавання: {len(items)}")

# Або використання count(), який завжди повертає актуальне значення
print(f"Поточна кількість: {page.locator('.item').count()}")
```

---

## Слайд 22: Частина 5 — Фільтрація елементів

# Частина 5
## Фільтрація елементів

Пошук конкретних елементів у колекціях

---

## Слайд 23: Використання filter() з has_text

```python
# Фільтрація за текстовим вмістом
products = page.locator(".product").filter(has_text="Laptop")
print(f"Ноутбуків: {products.count()}")

# Ланцюжок фільтрів
expensive_laptops = (
    page.locator(".product")
    .filter(has_text="Laptop")
    .filter(has_text="$1000")
)

# Отримання всіх відфільтрованих елементів
items = page.locator(".item").filter(has_text="Active").all()
for item in items:
    print(item.text_content())
```

---

## Слайд 24: Використання filter() з has

```python
# Фільтрація за дочірнім елементом
cards_with_button = page.locator(".card").filter(
    has=page.locator("button")
)

# Фільтрація за конкретним дочірнім елементом
products_on_sale = page.locator(".product").filter(
    has=page.locator(".sale-badge")
)

# Кілька умов
special_products = (
    page.locator(".product")
    .filter(has=page.locator(".sale-badge"))
    .filter(has_text="Featured")
)
```

---

## Слайд 25: Пошук конкретних елементів

```python
# Пошук першого відповідного елемента
first_laptop = page.locator(".product").filter(has_text="Laptop").first
first_laptop.click()

# Пошук останнього елемента
last_item = page.locator(".item").last

# Пошук за позицією
third_product = page.locator(".product").nth(2)

# Пошук та верифікація
items = page.locator(".item").all()
found = None
for item in items:
    if item.get_attribute("data-id") == "123":
        found = item
        break

if found:
    found.click()
```

---

## Слайд 26: Складні приклади фільтрації

```python
# Пошук продуктів у певному ціновому діапазоні
products = page.locator(".product").all()
in_range = []

for product in products:
    price_text = product.locator(".price").text_content()
    price = float(price_text.replace("$", ""))
    if 100 <= price <= 500:
        in_range.append(product)

print(f"Знайдено {len(in_range)} продуктів у діапазоні")

# Пошук елементів за атрибутами
items = page.locator(".item").all()
red_items = [
    item for item in items
    if item.get_attribute("data-color") == "red"
]

# Пошук тільки видимих елементів
all_items = page.locator(".item").all()
visible_items = [item for item in all_items if item.is_visible()]
```

---

## Слайд 27: Частина 6 — Практичні патерни

# Частина 6
## Практичні патерни

Реальні приклади використання

---

## Слайд 28: Патерн 1 — Валідація результатів пошуку

```python
# Пошук продуктів
page.locator("#search").fill("laptop")
page.locator("#search-btn").click()

# Очікування результатів
expect(page.locator(".search-result")).to_have_count(10)

# Верифікація всіх результатів
results = page.locator(".search-result").all()
for result in results:
    text = result.text_content().lower()
    assert "laptop" in text, f"Результат не відповідає: {text}"

print("✓ Всі результати відповідають пошуковому запиту")
```

---

## Слайд 29: Патерн 2 — Операції з кошиком

```python
# Додавання товарів до кошика
products = page.locator(".product").all()[:3]  # Перші 3 продукти
for product in products:
    product.locator(".add-to-cart").click()

# Верифікація кошика
expect(page.locator(".cart-item")).to_have_count(3)

# Розрахунок загальної суми
cart_items = page.locator(".cart-item").all()
total = 0
for item in cart_items:
    price_text = item.locator(".price").text_content()
    price = float(price_text.replace("$", ""))
    total += price

print(f"Загальна сума кошика: ${total}")
```

---

## Слайд 30: Патерн 3 — Валідація форми

```python
# Перевірка всіх обов'язкових полів
required_fields = page.locator("input[required]").all()
print(f"Знайдено {len(required_fields)} обов'язкових полів")

# Верифікація наявності міток
for field in required_fields:
    field_id = field.get_attribute("id")
    label = page.locator(f"label[for='{field_id}']")
    expect(label).to_be_visible()

# Заповнення всіх текстових полів
text_inputs = page.locator("input[type='text']").all()
for i, input_field in enumerate(text_inputs):
    input_field.fill(f"Тестове значення {i}")
```

---

## Слайд 31: Патерн 4 — Верифікація сортування

```python
# Клік на кнопку сортування
page.locator("#sort-by-price").click()

# Екстракція цін
products = page.locator(".product").all()
prices = []
for product in products:
    price_text = product.locator(".price").text_content()
    price = float(price_text.replace("$", ""))
    prices.append(price)

# Верифікація сортування
is_sorted = all(prices[i] <= prices[i+1] for i in range(len(prices)-1))
assert is_sorted, "Продукти не відсортовані за ціною"
print("✓ Продукти правильно відсортовані")
```

---

## Слайд 32: Найкращі практики

### ✅ РОБІТЬ

- Використовуйте count() для перевірки кількості
- Використовуйте all() коли потрібна ітерація
- Повторно запитуйте елементи після змін на сторінці
- Використовуйте filter() для чистішого коду
- Очікуйте потрібну кількість перед обробкою
- Екстрактуйте дані у змінні

### ❌ НЕ РОБІТЬ

- Зберігати посилання на елементи тривалий час
- Використовувати len(all()) замість count()
- Припускати порядок елементів
- Забувати обробляти порожні списки
- Ітерувати без перевірки кількості
- Хардкодити індекси

---

## Слайд 33: Типові помилки

### ⚠️ Застарілі посилання на елементи

```python
# ПОГАНО — елементи застарівають після змін сторінки
items = page.locator(".item").all()
page.locator("#refresh-btn").click()
items[0].click()  # Може не спрацювати!

# ДОБРЕ — повторний запит після змін
page.locator("#refresh-btn").click()
items = page.locator(".item").all()
items[0].click()
```

### ⚠️ Обробка порожніх списків

```python
# ПОГАНО — може викликати IndexError
items = page.locator(".item").all()
items[0].click()  # Помилка якщо немає елементів!

# ДОБРЕ — перевірка наявності
items = page.locator(".item").all()
if items:
    items[0].click()
```

---

## Слайд 34: Оптимізація продуктивності

```python
# НЕЕФЕКТИВНО — завантажує всі елементи для підрахунку
if len(page.locator(".item").all()) > 10:
    print("Багато елементів")

# ЕФЕКТИВНО — тільки отримує кількість
if page.locator(".item").count() > 10:
    print("Багато елементів")

# Швидка екстракція всіх текстів
# Замість:
texts = [el.text_content() for el in page.locator(".item").all()]

# Використовуйте:
texts = page.locator(".item").all_text_contents()
```

---

## Слайд 35: Швидка екстракція тексту — all_text_contents() та all_inner_texts()

```python
# all_text_contents() — повертає список всіх текстів (включаючи приховані)
texts = page.locator(".product-name").all_text_contents()
print(texts)  # ['Laptop', 'Phone', 'Tablet', ...]

# all_inner_texts() — повертає тільки видимий текст
visible_texts = page.locator(".product-name").all_inner_texts()

# Порівняння продуктивності
# ПОВІЛЬНО — створює список локаторів, потім ітерує
names = [el.text_content() for el in page.locator(".item").all()]

# ШВИДКО — один виклик до браузера
names = page.locator(".item").all_text_contents()

# Практичний приклад — перевірка наявності тексту
all_names = page.locator(".user-name").all_text_contents()
assert "John" in all_names, "John не знайдено у списку"
```

---

## Слайд 36: Негативна фільтрація — has_not та has_not_text

```python
# has_not — елементи БЕЗ певного дочірнього елемента
# Знайти картки без кнопки "Delete"
editable_cards = page.locator(".card").filter(
    has_not=page.locator(".delete-btn")
)

# Знайти продукти без badge "Sold Out"
available_products = page.locator(".product").filter(
    has_not=page.locator(".sold-out-badge")
)

# has_not_text — елементи БЕЗ певного тексту
# Знайти елементи без слова "Archived"
active_items = page.locator(".item").filter(has_not_text="Archived")

# Знайти рядки таблиці без статусу "Deleted"
active_rows = page.locator("table tr").filter(has_not_text="Deleted")

# Комбінування позитивної та негативної фільтрації
special_items = (
    page.locator(".product")
    .filter(has_text="Premium")           # З текстом "Premium"
    .filter(has_not_text="Discontinued")  # Без "Discontinued"
    .filter(has=page.locator(".in-stock")) # З елементом in-stock
)
```

---

## Слайд 37: Робота з пагінацією — Load More

```python
# Патерн 1: Кнопка "Load More"
all_items = []

while True:
    # Зберегти поточні елементи
    current_items = page.locator(".item").all_text_contents()
    all_items.extend(current_items)

    # Перевірити наявність кнопки "Load More"
    load_more = page.locator("#load-more")
    if load_more.is_visible():
        load_more.click()
        # Почекати завантаження нових елементів
        page.wait_for_timeout(1000)
    else:
        break

print(f"Завантажено {len(all_items)} елементів")

# Патерн 2: Числова пагінація
total_pages = int(page.locator(".pagination .total").text_content())

for page_num in range(1, total_pages + 1):
    # Клік на номер сторінки
    page.locator(f".pagination [data-page='{page_num}']").click()
    page.wait_for_load_state("networkidle")

    # Обробка елементів поточної сторінки
    items = page.locator(".item").all()
    for item in items:
        print(item.text_content())
```

---

## Слайд 38: Функція-хелпер для екстракції таблиці

```python
def extract_table(page, selector="table"):
    """
    Екстрактує таблицю як список словників.

    Args:
        page: Playwright page object
        selector: CSS селектор таблиці

    Returns:
        List[Dict]: Список рядків як словників
    """
    # Отримати заголовки
    headers = page.locator(f"{selector} th").all_text_contents()

    # Отримати всі рядки
    rows = page.locator(f"{selector} tbody tr").all()

    # Побудувати дані
    data = []
    for row in rows:
        cells = row.locator("td").all_text_contents()
        row_dict = {
            headers[i]: cells[i].strip()
            for i in range(min(len(headers), len(cells)))
        }
        data.append(row_dict)

    return data

# Використання
table_data = extract_table(page, "#users-table")
print(f"Знайдено {len(table_data)} записів")

# Фільтрація даних
active_users = [row for row in table_data if row['Status'] == 'Active']
```

---

## Слайд 39: Підсумок

### Ключові методи:

- ✅ **all()** — Отримати список усіх відповідних елементів
- ✅ **count()** — Отримати кількість елементів (ефективніше)
- ✅ **nth(i)** — Отримати елемент за індексом
- ✅ **first/last** — Отримати перший/останній елемент
- ✅ **filter()** — Фільтрувати елементи за критеріями
- ✅ **has_not/has_not_text** — Негативна фільтрація
- ✅ **all_text_contents()** — Швидка екстракція тексту
- ✅ **Таблиці** — Екстрактувати дані з рядків та комірок
- ✅ **Динамічний контент** — Обробляти змінювані списки

---

## Слайд 40: Що далі?

### Наступні теми:

- Скріншоти та відео
- Перехоплення мережевих запитів
- API тестування
- Організація тестів з Pytest

### Практика:

- Виконайте вправи в папці `exercises/`
- Перегляньте приклади в папці `examples/`
- Працюйте з реальними таблицями та списками

---

## Слайд 41: Фінальний слайд

# Відмінна робота!

## Ви опанували роботу з множинними елементами!

Колекції елементів — потужний інструмент автоматизації
