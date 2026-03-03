# Assertions — Перевірки та очікування

Assertions (перевірки) — це ключовий компонент будь-якого тесту. Playwright надає бібліотеку `expect` з автоматичним повторенням (auto-retry), що робить тести стабільними та надійними. У цьому розділі розглянемо всі типи перевірок.

## Основи expect

Playwright assertions автоматично повторюють перевірку протягом заданого таймауту (за замовчуванням 5 секунд), що усуває потребу в явних очікуваннях.

```python
from playwright.sync_api import Page, expect

def test_basic_assertions(page: Page):
    """Базові перевірки з expect."""
    page.goto("https://example.com")

    # Перевірка видимості елемента
    expect(page.get_by_role("heading", name="Головна")).to_be_visible()

    # Негативна перевірка (елемент НЕ видимий)
    expect(page.get_by_text("Помилка")).not_to_be_visible()

    # Власний таймаут для конкретної перевірки
    expect(page.get_by_text("Дані завантажено")).to_be_visible(timeout=15000)
```

::: tip Порада
Завжди використовуйте `expect` з Playwright замість звичайного `assert`. Playwright assertions мають вбудований механізм повторних спроб, що робить тести стабільнішими.
:::

## Перевірки видимості та стану

```python
def test_visibility_state_assertions(page: Page):
    """Перевірки видимості, доступності та стану елементів."""
    page.goto("https://example.com/form")

    # Видимість
    expect(page.get_by_role("dialog")).to_be_visible()
    expect(page.get_by_role("dialog")).not_to_be_visible()

    # Приховані елементи
    expect(page.locator(".loading-spinner")).to_be_hidden()

    # Доступність елемента (enabled/disabled)
    expect(page.get_by_role("button", name="Зберегти")).to_be_enabled()
    expect(page.get_by_role("button", name="Видалити")).to_be_disabled()

    # Редагованість поля
    expect(page.get_by_label("Ім'я")).to_be_editable()
    expect(page.get_by_label("ID користувача")).not_to_be_editable()

    # Наявність елемента в DOM (навіть якщо прихований)
    expect(page.locator("#hidden-data")).to_be_attached()

    # Фокус на елементі
    page.get_by_label("Email").click()
    expect(page.get_by_label("Email")).to_be_focused()

    # Порожність елемента
    expect(page.get_by_label("Нотатки")).to_be_empty()
```

## Перевірки тексту

```python
import re

def test_text_assertions(page: Page):
    """Перевірки текстового вмісту елементів."""
    page.goto("https://example.com/dashboard")

    # Точний збіг тексту
    expect(page.get_by_test_id("welcome-msg")).to_have_text("Ласкаво просимо, Іване!")

    # Частковий збіг тексту
    expect(page.get_by_test_id("welcome-msg")).to_contain_text("Ласкаво просимо")

    # Перевірка з регулярним виразом
    expect(page.get_by_test_id("order-id")).to_have_text(re.compile(r"Замовлення #\d{6}"))
    expect(page.get_by_test_id("price")).to_contain_text(re.compile(r"\d+\.\d{2} грн"))

    # Перевірка тексту списку елементів
    items = page.get_by_role("listitem")
    expect(items).to_have_text([
        "Головна",
        "Продукти",
        "Контакти",
        "Про нас",
    ])

    # Ігнорування регістру
    expect(page.get_by_test_id("status")).to_have_text(
        re.compile(r"активний", re.IGNORECASE)
    )
```

## Перевірки атрибутів та CSS

```python
def test_attribute_css_assertions(page: Page):
    """Перевірки HTML-атрибутів та CSS властивостей."""
    page.goto("https://example.com")

    # Перевірка атрибуту
    expect(page.get_by_role("link", name="Документація")).to_have_attribute("href", "/docs")
    expect(page.get_by_role("img").first).to_have_attribute("alt", "Логотип")

    # Перевірка атрибуту з регулярним виразом
    expect(page.get_by_role("link", name="API")).to_have_attribute(
        "href", re.compile(r"/api/v\d+")
    )

    # Перевірка CSS класу
    expect(page.get_by_role("button", name="Активна")).to_have_class(re.compile(r"active"))
    expect(page.locator(".nav-item").first).to_have_class("nav-item selected")

    # Перевірка CSS властивості
    expect(page.get_by_role("alert")).to_have_css("background-color", "rgb(255, 0, 0)")
    expect(page.locator(".modal")).to_have_css("display", "none")

    # Перевірка id
    expect(page.get_by_role("main")).to_have_id("content")
```

## Перевірки значень форми

```python
def test_form_value_assertions(page: Page):
    """Перевірки значень полів форми."""
    page.goto("https://example.com/profile")

    # Перевірка значення текстового поля
    expect(page.get_by_label("Ім'я")).to_have_value("Іван")

    # Перевірка з регулярним виразом
    expect(page.get_by_label("Телефон")).to_have_value(re.compile(r"\+380\d{9}"))

    # Перевірка значень множинного вибору
    expect(page.get_by_label("Навички")).to_have_values([
        re.compile(r"python"),
        re.compile(r"javascript"),
    ])

    # Перевірка стану чекбоксів
    expect(page.get_by_role("checkbox", name="Підписка")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Рекламні листи")).not_to_be_checked()
```

## Перевірки кількості елементів

```python
def test_count_assertions(page: Page):
    """Перевірки кількості знайдених елементів."""
    page.goto("https://example.com/products")

    # Точна кількість
    expect(page.get_by_role("listitem")).to_have_count(10)

    # Перевірка наявності елементів (більше нуля)
    items = page.get_by_role("listitem")
    count = items.count()
    assert count > 0, f"Очікувалось більше 0 елементів, отримано {count}"
```

## Перевірки сторінки (Page assertions)

```python
def test_page_assertions(page: Page):
    """Перевірки на рівні сторінки."""
    page.goto("https://example.com/dashboard")

    # Перевірка заголовку сторінки
    expect(page).to_have_title("Панель керування — Example")
    expect(page).to_have_title(re.compile(r"Панель керування"))

    # Перевірка URL
    expect(page).to_have_url("https://example.com/dashboard")
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    # Після навігації
    page.get_by_role("link", name="Профіль").click()
    expect(page).to_have_url(re.compile(r".*/profile"))
```

## Перевірки API відповідей

```python
def test_api_response_assertions(page: Page):
    """Перевірки відповідей API запитів."""
    page.goto("https://example.com")

    # Перехоплення та перевірка API відповіді
    with page.expect_response("**/api/users") as response_info:
        page.get_by_role("button", name="Завантажити користувачів").click()
    response = response_info.value

    # Перевірка статус-коду
    assert response.status == 200

    # Перевірка тіла відповіді
    data = response.json()
    assert len(data["users"]) > 0
    assert data["users"][0]["name"] is not None

    # Перевірка заголовків відповіді
    assert response.headers["content-type"] == "application/json"
```

## Soft Assertions (м'які перевірки)

```python
def test_soft_assertions(page: Page):
    """М'які перевірки — продовжують виконання після невдачі."""
    page.goto("https://example.com/profile")

    # Всі перевірки виконаються, навіть якщо деякі впадуть
    expect(page.get_by_label("Ім'я"), "Перевірка імені").to_have_value("Іван")
    expect(page.get_by_label("Email"), "Перевірка email").to_have_value("ivan@example.com")
    expect(page.get_by_label("Місто"), "Перевірка міста").to_have_value("Київ")
    expect(page.get_by_role("heading"), "Заголовок профілю").to_have_text("Мій профіль")
```

::: info Інформація
Другий параметр `expect` — це повідомлення, яке буде показано в разі невдалої перевірки. Це допомагає швидше зрозуміти причину помилки.
:::

## Налаштування таймаутів

```python
def test_custom_timeouts(page: Page):
    """Налаштування таймаутів для перевірок."""
    page.goto("https://example.com")

    # Конкретний таймаут для однієї перевірки
    expect(page.get_by_text("Дані оброблено")).to_be_visible(timeout=30000)

    # Глобальне налаштування таймауту в conftest.py
    # expect.set_options(timeout=10000)
```

::: warning Увага
Не використовуйте занадто великі таймаути без потреби. Якщо елемент потребує 30 секунд для появи, можливо, є проблема з продуктивністю додатку.
:::

## Практичний приклад: тестування панелі користувача

```python
import re
from playwright.sync_api import Page, expect

def test_user_dashboard(page: Page):
    """Комплексна перевірка панелі користувача."""
    page.goto("https://example.com/login")

    # Авторизація
    page.get_by_label("Email").fill("admin@example.com")
    page.get_by_label("Пароль").fill("admin123")
    page.get_by_role("button", name="Увійти").click()

    # Перевірка URL після авторизації
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    # Перевірка заголовку сторінки
    expect(page).to_have_title(re.compile(r"Dashboard"))

    # Перевірка вітального повідомлення
    expect(page.get_by_test_id("greeting")).to_contain_text("Вітаємо, Адміністратор")

    # Перевірка навігаційного меню
    nav_items = page.locator("nav").get_by_role("link")
    expect(nav_items).to_have_count(5)

    # Перевірка статистики
    expect(page.get_by_test_id("active-users")).to_have_text(re.compile(r"\d+"))
    expect(page.get_by_test_id("total-orders")).to_contain_text("замовлень")

    # Перевірка таблиці останніх замовлень
    rows = page.get_by_role("table").get_by_role("row")
    expect(rows).to_have_count(11)  # 10 рядків + заголовок

    # Перевірка стану кнопок
    expect(page.get_by_role("button", name="Експорт")).to_be_enabled()
    expect(page.get_by_role("button", name="Видалити все")).to_be_disabled()

    # Перевірка іконки профілю
    expect(page.get_by_alt_text("Аватар")).to_be_visible()
    expect(page.get_by_alt_text("Аватар")).to_have_attribute("src", re.compile(r"/avatars/"))
```

## Корисні посилання

- [Офіційна документація Assertions](https://playwright.dev/python/docs/test-assertions)
- [Список всіх assertions](https://playwright.dev/python/docs/api/class-locatorassertions)
- [Page assertions](https://playwright.dev/python/docs/api/class-pageassertions)
- [API Response assertions](https://playwright.dev/python/docs/api/class-apiresponseassertions)
