# Actions — Взаємодія з елементами

Playwright надає широкий набір методів для взаємодії з елементами на сторінці — від простих кліків до складних операцій перетягування. У цьому розділі розглянемо основні дії та їх практичне застосування в QA автоматизації.

## Кліки

### Базові кліки

```python
from playwright.sync_api import Page

def test_click_actions(page: Page):
    """Різні варіанти кліків по елементах."""
    page.goto("https://example.com")

    # Звичайний клік
    page.get_by_role("button", name="Зберегти").click()

    # Подвійний клік
    page.get_by_text("Редагувати назву").dblclick()

    # Клік правою кнопкою миші (контекстне меню)
    page.get_by_role("row").first.click(button="right")

    # Клік з модифікаторами клавіш
    page.get_by_role("link", name="Документ").click(modifiers=["Control"])  # Ctrl+Click

    # Клік з затримкою (імітація довгого натискання)
    page.get_by_role("button", name="Меню").click(delay=1000)

    # Клік у конкретну позицію елемента
    page.locator(".canvas").click(position={"x": 100, "y": 200})

    # Примусовий клік (ігнорує перевірку видимості)
    page.locator(".hidden-trigger").click(force=True)
```

### Hover (наведення курсора)

```python
def test_hover_actions(page: Page):
    """Наведення курсора на елемент."""
    page.goto("https://example.com")

    # Наведення для показу підменю
    page.get_by_role("menuitem", name="Продукти").hover()
    page.get_by_role("menuitem", name="Ноутбуки").click()

    # Наведення для відображення підказки (tooltip)
    page.get_by_role("button", name="Інфо").hover()
    tooltip = page.get_by_role("tooltip")
    assert tooltip.is_visible()
```

## Введення тексту

### fill та type

```python
def test_input_actions(page: Page):
    """Введення тексту в поля форми."""
    page.goto("https://example.com/form")

    # fill — миттєве заповнення поля (очищає попередній вміст)
    page.get_by_label("Ім'я").fill("Тарас Шевченко")

    # clear — очищення поля
    page.get_by_label("Ім'я").clear()

    # press_sequentially — посимвольне введення (імітує реальний набір)
    page.get_by_label("Пошук").press_sequentially("Playwright", delay=100)

    # Заповнення кількох полів форми
    page.get_by_label("Email").fill("taras@example.com")
    page.get_by_label("Пароль").fill("SecurePassword123!")
    page.get_by_label("Підтвердження").fill("SecurePassword123!")
```

::: tip Порада
Використовуйте `fill()` для звичайного заповнення полів. `press_sequentially()` корисний, коли потрібно емулювати посимвольний ввід, наприклад, для полів з автозаповненням.
:::

### Натискання клавіш

```python
def test_keyboard_actions(page: Page):
    """Робота з клавіатурою."""
    page.goto("https://example.com")

    # Натискання окремих клавіш
    page.get_by_label("Пошук").press("Enter")

    # Комбінації клавіш
    page.get_by_role("textbox").press("Control+a")    # Виділити все
    page.get_by_role("textbox").press("Control+c")    # Копіювати
    page.get_by_role("textbox").press("Control+v")    # Вставити

    # Спеціальні клавіші
    page.get_by_label("Коментар").press("Tab")        # Перехід до наступного поля
    page.keyboard.press("Escape")                      # Закриття модального вікна

    # Введення тексту через keyboard (глобально)
    page.keyboard.type("Привіт, світ!")
    page.keyboard.press("Shift+Enter")                 # Новий рядок
```

## Робота з випадаючими списками

```python
def test_select_actions(page: Page):
    """Взаємодія з елементами select."""
    page.goto("https://example.com/form")

    # Вибір за значенням (value)
    page.get_by_label("Країна").select_option("UA")

    # Вибір за текстом
    page.get_by_label("Місто").select_option(label="Київ")

    # Вибір за індексом
    page.get_by_label("Місяць").select_option(index=5)

    # Множинний вибір
    page.get_by_label("Навички").select_option(["python", "javascript", "sql"])
```

## Чекбокси та радіокнопки

```python
from playwright.sync_api import expect

def test_checkbox_radio_actions(page: Page):
    """Взаємодія з чекбоксами та радіокнопками."""
    page.goto("https://example.com/settings")

    # Чекбокси
    page.get_by_role("checkbox", name="Отримувати сповіщення").check()
    page.get_by_role("checkbox", name="Темна тема").uncheck()

    # Перевірка стану чекбокса
    expect(page.get_by_role("checkbox", name="Отримувати сповіщення")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Темна тема")).not_to_be_checked()

    # Перемикання стану (toggle)
    checkbox = page.get_by_role("checkbox", name="Режим розробника")
    checkbox.set_checked(True)
    checkbox.set_checked(False)

    # Радіокнопки
    page.get_by_role("radio", name="Українська").check()
    expect(page.get_by_role("radio", name="Українська")).to_be_checked()
```

## Завантаження файлів

```python
def test_file_upload(page: Page):
    """Завантаження файлів на сторінку."""
    page.goto("https://example.com/upload")

    # Завантаження одного файлу
    page.get_by_label("Оберіть файл").set_input_files("tests/data/document.pdf")

    # Завантаження кількох файлів
    page.get_by_label("Оберіть файли").set_input_files([
        "tests/data/photo1.jpg",
        "tests/data/photo2.jpg",
    ])

    # Очищення вибору файлів
    page.get_by_label("Оберіть файл").set_input_files([])

    # Завантаження через діалог вибору файлу
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Завантажити").click()
    file_chooser = fc_info.value
    file_chooser.set_files("tests/data/report.xlsx")
```

## Завантаження файлів (Download)

```python
def test_file_download(page: Page):
    """Завантаження файлів зі сторінки."""
    page.goto("https://example.com/reports")

    # Очікування завантаження файлу
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Завантажити звіт").click()
    download = download_info.value

    # Збереження файлу
    download.save_as("downloads/" + download.suggested_filename)

    # Перевірка завантаженого файлу
    assert download.suggested_filename == "report_2024.pdf"
    assert download.failure() is None  # Перевірка відсутності помилок
```

## Drag and Drop (Перетягування)

```python
def test_drag_and_drop(page: Page):
    """Перетягування елементів."""
    page.goto("https://example.com/kanban")

    # Простий drag and drop
    page.locator("#task-1").drag_to(page.locator("#column-done"))

    # Drag and drop з ручним керуванням
    source = page.locator(".draggable-item").first
    target = page.locator(".drop-zone")

    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()
```

## Діалогові вікна

```python
def test_dialog_handling(page: Page):
    """Обробка діалогових вікон (alert, confirm, prompt)."""
    page.goto("https://example.com")

    # Обробка alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Показати alert").click()

    # Обробка confirm — натиснути "OK"
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Підтвердити видалення").click()

    # Обробка confirm — натиснути "Скасувати"
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Підтвердити видалення").click()

    # Обробка prompt — ввести текст
    page.on("dialog", lambda dialog: dialog.accept("Нова назва"))
    page.get_by_role("button", name="Перейменувати").click()
```

::: warning Увага
Обробник діалогових вікон потрібно встановити **до** дії, яка викликає діалог. Інакше Playwright автоматично закриє діалог.
:::

## Навігація

```python
def test_navigation_actions(page: Page):
    """Навігація по сторінках."""
    # Перехід на URL
    page.goto("https://example.com")

    # Перехід з очікуванням стану
    page.goto("https://example.com/dashboard", wait_until="networkidle")

    # Навігація кнопками браузера
    page.go_back()
    page.go_forward()

    # Перезавантаження сторінки
    page.reload()

    # Очікування навігації після кліку
    with page.expect_navigation():
        page.get_by_role("link", name="Каталог").click()
```

## Практичний приклад: оформлення замовлення

```python
from playwright.sync_api import Page, expect

def test_checkout_flow(page: Page):
    """Тест оформлення замовлення в інтернет-магазині."""
    page.goto("https://example-shop.com")

    # Пошук товару
    page.get_by_placeholder("Пошук товарів...").fill("Навушники")
    page.get_by_placeholder("Пошук товарів...").press("Enter")

    # Вибір товару
    page.get_by_role("link", name="Бездротові навушники Pro").click()

    # Вибір кольору
    page.get_by_role("radio", name="Чорний").check()

    # Вибір кількості
    page.get_by_label("Кількість").select_option("2")

    # Додавання до кошика
    page.get_by_role("button", name="Додати до кошика").click()
    expect(page.get_by_text("Товар додано до кошика")).to_be_visible()

    # Перехід до кошика
    page.get_by_role("link", name="Кошик").click()

    # Заповнення форми доставки
    page.get_by_label("Ім'я").fill("Олександр")
    page.get_by_label("Прізвище").fill("Бондаренко")
    page.get_by_label("Телефон").fill("+380501234567")
    page.get_by_label("Місто").select_option(label="Київ")
    page.get_by_label("Відділення Нової Пошти").fill("Відділення №25")

    # Вибір способу оплати
    page.get_by_role("radio", name="Оплата при отриманні").check()

    # Підтвердження замовлення
    page.get_by_role("button", name="Оформити замовлення").click()

    # Перевірка успішного оформлення
    expect(page.get_by_role("heading", name="Замовлення оформлено")).to_be_visible()
    expect(page.get_by_text("Номер замовлення")).to_be_visible()
```

## Корисні посилання

- [Офіційна документація Actions](https://playwright.dev/python/docs/input)
- [Робота з подіями сторінки](https://playwright.dev/python/docs/events)
- [Робота з файлами](https://playwright.dev/python/docs/downloads)
- [Навігація](https://playwright.dev/python/docs/navigations)
