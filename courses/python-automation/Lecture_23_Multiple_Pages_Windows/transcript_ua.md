# Лекція 23: Множинні сторінки та вікна

**Курс автоматизації Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 23
## Множинні сторінки та вікна

Курс автоматизації Python + Playwright

---

## Слайд 2: Що розглядається в цій лекції

- Відкриття та керування множинними сторінками/вкладками
- Обробка popup-вікон з expect_popup()
- Одночасна робота з кількома сторінками
- Використання подій сторінок (on load, on close)
- Ізоляція контекстів браузера
- Тестування багатокористувацьких сценаріїв

---

## Слайд 3: Важливість роботи з множинними сторінками

Сучасні веб-застосунки часто відкривають нові вкладки, popup-вікна або потребують тестування взаємодії кількох користувачів одночасно.

### Типові сценарії:

- **OAuth popup-вікна** — Google, Facebook, GitHub авторизація
- **Документи в нових вкладках** — PDF, звіти
- **Багатокористувацьке тестування** — чати, системи спільної роботи
- **Зовнішні посилання** — target="_blank"
- **Порівняння даних** — паралельний перегляд інформації

---

## Слайд 4: Частина 1 — Ієрархія браузера

# Частина 1
## Ієрархія браузера

Browser → Context → Page

---

## Слайд 5: Розуміння ієрархії

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Рівень 1: Browser (Chromium, Firefox, WebKit)
    browser = p.chromium.launch()

    # Рівень 2: Context (як інкогніто-вікно)
    context = browser.new_context()

    # Рівень 3: Page (окрема вкладка)
    page = context.new_page()
```

| Рівень | Опис | Ізоляція |
|--------|------|----------|
| Browser | Екземпляр браузера | Повна |
| Context | Контейнер сесії | Cookies, storage |
| Page | Окрема вкладка/вікно | Тільки DOM |

---

## Слайд 6: Ізоляція контекстів

### Однаковий контекст — спільна сесія

```python
# Сторінки ділять cookies!
page1 = context.new_page()
page2 = context.new_page()

# Вхід на page1...
page1.goto("/login")
page1.fill("#user", "alice")

# page2 теж авторизована!
```

### Різні контексти — ізоляція

```python
# Окремі сесії
ctx1 = browser.new_context()
ctx2 = browser.new_context()

page1 = ctx1.new_page()
page2 = ctx2.new_page()

# Повністю незалежні!
```

---

## Слайд 7: Частина 2 — Відкриття нових сторінок

# Частина 2
## Відкриття нових сторінок

Створення та керування вкладками

---

## Слайд 8: Створення нових сторінок

```python
# Метод 1: Створення нової сторінки в контексті
page1 = context.new_page()
page2 = context.new_page()

# Навігація кожної сторінки
page1.goto("https://example.com/page1")
page2.goto("https://example.com/page2")

# Робота з обома сторінками
page1.locator("#btn1").click()
page2.locator("#btn2").click()

# Отримання всіх сторінок контексту
all_pages = context.pages
print(f"Всього сторінок: {len(all_pages)}")
```

---

## Слайд 9: Керування множинними сторінками

```python
# Отримати всі сторінки
all_pages = context.pages

# Пошук сторінки за URL
for p in context.pages:
    if "dashboard" in p.url:
        dashboard = p
        break

# Пошук сторінки за заголовком
for p in context.pages:
    if p.title() == "Settings":
        settings = p
        break

# Закриття конкретної сторінки
page2.close()

# Закриття всіх сторінок окрім головної
for p in context.pages[1:]:
    p.close()
```

---

## Слайд 10: Частина 3 — Обробка popup-вікон

# Частина 3
## Обробка popup-вікон

Метод expect_popup()

---

## Слайд 11: Метод expect_popup()

```python
# Клік відкриває popup-вікно
with page.expect_popup() as popup_info:
    page.locator("#open-popup").click()

# Отримання об'єкта popup
popup = popup_info.value

# Очікування завантаження
popup.wait_for_load_state()

# Робота з popup
print(popup.title())
popup.locator("#popup-btn").click()

# Закриття popup
popup.close()
```

**Важливо:** expect_popup() очікує та захоплює посилання на нове вікно.

---

## Слайд 12: Обробка посилань target="_blank"

```python
# Посилання відкривається в новій вкладці
# <a href="/docs" target="_blank">Documentation</a>

with page.expect_popup() as new_tab_info:
    page.locator("a[target='_blank']").click()

new_tab = new_tab_info.value
new_tab.wait_for_load_state()

# Перевірка URL нової вкладки
expect(new_tab).to_have_url("**/docs")

# Робота з новою вкладкою
content = new_tab.locator("#content").text_content()

# Закриття та повернення до головної сторінки
new_tab.close()
page.locator("#continue").click()
```

---

## Слайд 13: Приклад OAuth Login Popup

```python
# Клік "Login with Google"
with page.expect_popup() as popup_info:
    page.locator("#google-login").click()

popup = popup_info.value
popup.wait_for_load_state()

# Заповнення форми Google у popup
popup.locator("#email").fill("user@gmail.com")
popup.locator("#next").click()

popup.locator("#password").fill("password123")
popup.locator("#submit").click()

# Popup закривається автоматично після авторизації
# Очікування оновлення головної сторінки
page.wait_for_load_state()
expect(page.locator(".user-profile")).to_be_visible()
```

---

## Слайд 14: Обробка множинних popup-вікон

```python
# Коли дія відкриває кілька popup-вікон
popups = []

def capture_popup(popup):
    popups.append(popup)

# Реєстрація обробника події
page.on("popup", capture_popup)

# Виконання дії, що відкриває popup-вікна
page.locator("#multi-popup").click()

# Очікування появи popup-вікон
page.wait_for_timeout(1000)

# Обробка всіх захоплених popup-вікон
for popup in popups:
    popup.wait_for_load_state()
    print(f"Popup: {popup.url}")
    popup.close()
```

---

## Слайд 15: Частина 4 — Події сторінок

# Частина 4
## Події сторінок

Слухачі та обробники подій

---

## Слайд 16: Слухачі подій сторінок

```python
# Слухач нових сторінок у контексті
def on_new_page(page):
    print(f"Нова сторінка: {page.url}")

context.on("page", on_new_page)

# Слухач закриття сторінки
def on_page_close():
    print("Сторінку закрито!")

page.on("close", on_page_close)

# Слухач консольних повідомлень
def on_console(msg):
    print(f"Console [{msg.type}]: {msg.text}")

page.on("console", on_console)
```

---

## Слайд 17: Очікування подій сторінок

```python
# Очікування відкриття нової сторінки
with context.expect_page() as new_page_info:
    page.locator("#open-new").click()
new_page = new_page_info.value

# Очікування завантаження файлу
with page.expect_download() as download_info:
    page.locator("#download-btn").click()
download = download_info.value
download.save_as("file.pdf")

# Очікування самозакриття сторінки
with page.expect_close():
    page.locator("#self-close-btn").click()
```

---

## Слайд 18: expect_popup() з таймаутом

```python
# Встановлення власного таймауту (5 секунд)
try:
    with page.expect_popup(timeout=5000) as popup_info:
        page.locator("#slow-popup-btn").click()

    popup = popup_info.value
    popup.wait_for_load_state()
    print(f"Popup захоплено: {popup.url}")
    popup.close()

except Exception as e:
    print(f"Таймаут очікування popup: {e}")
```

---

## Слайд 19: context.expect_page()

```python
# context.expect_page() захоплює БУДЬ-ЯКУ нову сторінку в контексті
with context.expect_page() as new_page_info:
    page.locator("#open-new").click()

new_page = new_page_info.value
new_page.wait_for_load_state()

print(f"Нова сторінка: {new_page.url}")
print(f"Всього сторінок: {len(context.pages)}")

# З таймаутом
with context.expect_page(timeout=3000) as page_info:
    page.locator("#create-tab").click()
```

---

## Слайд 20: Частина 5 — Багатокористувацьке тестування

# Частина 5
## Багатокористувацьке тестування

Реальні сценарії

---

## Слайд 21: Тестування чат-застосунку

```python
# Створення окремих контекстів для кожного користувача
user1_ctx = browser.new_context()
user2_ctx = browser.new_context()

user1 = user1_ctx.new_page()
user2 = user2_ctx.new_page()

# Обидва користувачі приєднуються до чату
user1.goto("https://chat.example.com")
user1.locator("#name").fill("Alice")
user1.locator("#join").click()

user2.goto("https://chat.example.com")
user2.locator("#name").fill("Bob")
user2.locator("#join").click()

# Alice надсилає повідомлення
user1.locator("#message").fill("Hello Bob!")
user1.locator("#send").click()

# Перевірка отримання повідомлення Bob
expect(user2.locator(".message")).to_contain_text("Hello Bob!")
```

---

## Слайд 22: Порівняння двох сторінок

```python
# Порівняння цін продукту на двох сайтах
page1 = context.new_page()
page2 = context.new_page()

page1.goto("https://store1.com/product/123")
page2.goto("https://store2.com/product/123")

# Екстракція цін
price1 = page1.locator(".price").text_content()
price2 = page2.locator(".price").text_content()

print(f"Магазин 1: {price1}")
print(f"Магазин 2: {price2}")

# Порівняння наявності
avail1 = page1.locator(".stock").text_content()
avail2 = page2.locator(".stock").text_content()

print(f"Наявність: {avail1} vs {avail2}")
```

---

## Слайд 23: Тестування Admin + User

```python
# Тест: дія адміністратора відображається для користувача
admin_ctx = browser.new_context()
user_ctx = browser.new_context()

admin = admin_ctx.new_page()
user = user_ctx.new_page()

# Адміністратор створює оголошення
admin.goto("https://app.com/admin")
admin.locator("#new-announcement").fill("Технічні роботи сьогодні")
admin.locator("#publish").click()

# Користувач бачить оголошення
user.goto("https://app.com")
expect(user.locator(".announcement")).to_contain_text("Технічні роботи")
```

---

## Слайд 24: Найкращі практики

### Рекомендовано

- Використання expect_popup() для popup-вікон
- Очікування wait_for_load_state() для нових сторінок
- Закриття сторінок після завершення роботи
- Використання окремих контекстів для ізоляції
- Обробка popup-блокувальників
- Очищення ресурсів

### Не рекомендовано

- Припускати миттєве відкриття popup
- Залишати відкриті невикористані сторінки
- Змішувати користувачів в одному контексті
- Забувати про закриті сторінки
- Ігнорувати посилання на сторінки після закриття
- Пропускати wait_for_load_state()

---

## Слайд 25: Типові помилки

```python
# НЕПРАВИЛЬНО — Popup не захоплено
page.locator("#popup-btn").click()
# Як отримати доступ до popup?

# ПРАВИЛЬНО — Використання expect_popup()
with page.expect_popup() as popup_info:
    page.locator("#popup-btn").click()
popup = popup_info.value


# НЕПРАВИЛЬНО — Робота із закритою сторінкою
popup.locator("#submit").click()  # закриває popup
popup.locator("#next").click()  # Помилка!

# ПРАВИЛЬНО — Перехід до головної сторінки
popup.locator("#submit").click()  # закриває popup
page.locator("#next").click()  # продовження на головній
```

---

## Слайд 26: Async API для паралельних операцій

```python
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Створення контекстів паралельно
        ctx1, ctx2 = await asyncio.gather(
            browser.new_context(),
            browser.new_context()
        )

        user1, user2 = await asyncio.gather(
            ctx1.new_page(),
            ctx2.new_page()
        )

        # Навігація обох сторінок паралельно (швидше!)
        await asyncio.gather(
            user1.goto("https://example.com"),
            user2.goto("https://example.com")
        )

        await browser.close()

asyncio.run(main())
```

---

## Слайд 27: Підсумок

**Ієрархія:** Browser → Context → Page

**Нові сторінки:** context.new_page() створює вкладки

**Popup-вікна:** expect_popup() захоплює нові вікна

**Події:** page.on() / context.on() для слухачів

**Ізоляція:** Різні контексти = окремі сесії

**Багатокористувацькі тести:** Окремий контекст для кожного користувача

**Таймаут:** expect_popup(timeout=5000) для контролю очікування

**Async API:** asyncio.gather() для паралельних операцій

---

## Слайд 28: Наступні теми

### Що далі:

- Скріншоти та відео
- Автентифікація та Storage State
- Перехоплення мережевих запитів

### Практика:

- Виконання вправ у папці exercises/
- Перегляд прикладів у папці examples/
- Експерименти з багатокористувацькими сценаріями

---

## Слайд 29: Фінальний слайд

# Множинні сторінки та вікна

## Опановано роботу з множинними сторінками

Тепер можна тестувати складні багатосторінкові сценарії
