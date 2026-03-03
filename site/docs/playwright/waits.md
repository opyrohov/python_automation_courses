# Waits — Стратегії очікування

Коректна обробка очікувань — одна з найважливіших частин стабільної автоматизації. Playwright має потужний механізм автоматичного очікування (auto-wait), але іноді потрібні додаткові стратегії. У цьому розділі розглянемо всі підходи до очікувань.

## Auto-wait — автоматичне очікування

Playwright автоматично чекає, поки елемент стане готовим до взаємодії перед виконанням дії. Це значно зменшує потребу в явних очікуваннях.

```python
from playwright.sync_api import Page, expect

def test_auto_wait(page: Page):
    """Playwright автоматично чекає перед виконанням дій."""
    page.goto("https://example.com")

    # Playwright сам дочекається, поки кнопка стане:
    # - прикріпленою до DOM
    # - видимою
    # - стабільною (не анімується)
    # - доступною для подій (не перекрита іншим елементом)
    # - активною (enabled)
    page.get_by_role("button", name="Зберегти").click()

    # Те саме для fill — чекає, поки поле стане доступним
    page.get_by_label("Ім'я").fill("Іван")
```

::: tip Порада
У більшості випадків auto-wait достатньо. Не додавайте зайвих явних очікувань — це уповільнює тести та може маскувати справжні проблеми.
:::

## wait_for_selector

```python
def test_wait_for_selector(page: Page):
    """Очікування появи або зникнення елемента."""
    page.goto("https://example.com")

    # Очікування появи елемента в DOM
    page.wait_for_selector(".loading-complete")

    # Очікування видимості елемента
    page.wait_for_selector("#results-table", state="visible")

    # Очікування зникнення елемента
    page.wait_for_selector(".spinner", state="hidden")

    # Очікування видалення елемента з DOM
    page.wait_for_selector(".temp-notification", state="detached")

    # Очікування з власним таймаутом
    page.wait_for_selector("#slow-content", state="visible", timeout=30000)
```

## wait_for_load_state

```python
def test_wait_for_load_state(page: Page):
    """Очікування станів завантаження сторінки."""
    page.goto("https://example.com")

    # Очікування завершення початкового завантаження DOM
    page.wait_for_load_state("domcontentloaded")

    # Очікування повного завантаження сторінки (всі ресурси)
    page.wait_for_load_state("load")

    # Очікування завершення мережевої активності
    # (жодного запиту протягом 500мс)
    page.wait_for_load_state("networkidle")
```

::: warning Увага
`networkidle` може бути ненадійним на сторінках з постійними запитами (вебсокети, polling). Використовуйте його обережно та надавайте перевагу очікуванню конкретних елементів.
:::

## wait_for_url

```python
import re

def test_wait_for_url(page: Page):
    """Очікування зміни URL."""
    page.goto("https://example.com/login")

    # Виконуємо авторизацію
    page.get_by_label("Email").fill("user@test.com")
    page.get_by_label("Пароль").fill("password")
    page.get_by_role("button", name="Увійти").click()

    # Очікування переходу на конкретний URL
    page.wait_for_url("**/dashboard")

    # Очікування URL за регулярним виразом
    page.wait_for_url(re.compile(r".*/dashboard\?.*"))

    # Очікування з таймаутом
    page.wait_for_url("**/dashboard", timeout=15000)
```

## Очікування locator

```python
def test_locator_wait_for(page: Page):
    """Використання wait_for на локаторах."""
    page.goto("https://example.com")

    # Очікування появи елемента через локатор
    page.get_by_test_id("data-loaded").wait_for(state="visible")

    # Очікування зникнення індикатора завантаження
    page.locator(".loading-overlay").wait_for(state="hidden")

    # Очікування появи в DOM (навіть якщо прихований)
    page.locator("#lazy-component").wait_for(state="attached")

    # Очікування зникнення з DOM
    page.get_by_text("Тимчасове повідомлення").wait_for(state="detached")
```

## Очікування мережевих запитів

```python
def test_wait_for_request_response(page: Page):
    """Очікування конкретних мережевих запитів та відповідей."""
    page.goto("https://example.com")

    # Очікування відповіді API
    with page.expect_response("**/api/products") as response_info:
        page.get_by_role("button", name="Завантажити товари").click()
    response = response_info.value
    assert response.status == 200

    # Очікування відповіді з умовою
    with page.expect_response(
        lambda response: response.url.endswith("/api/search") and response.status == 200
    ) as response_info:
        page.get_by_label("Пошук").fill("Ноутбук")
        page.get_by_label("Пошук").press("Enter")
    data = response_info.value.json()
    assert len(data["results"]) > 0

    # Очікування запиту
    with page.expect_request("**/api/orders") as request_info:
        page.get_by_role("button", name="Оформити").click()
    request = request_info.value
    assert request.method == "POST"
```

## Очікування подій сторінки

```python
def test_wait_for_events(page: Page):
    """Очікування різних подій сторінки."""
    page.goto("https://example.com")

    # Очікування нового вікна (popup)
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Відкрити у новому вікні").click()
    popup = popup_info.value
    popup.wait_for_load_state()
    assert "Нова сторінка" in popup.title()

    # Очікування console повідомлення
    with page.expect_console_message() as msg_info:
        page.get_by_role("button", name="Виконати").click()
    message = msg_info.value
    assert "Операція завершена" in message.text

    # Очікування WebSocket з'єднання
    with page.expect_websocket() as ws_info:
        page.get_by_role("button", name="Підключитись").click()
    ws = ws_info.value
    assert ws.url.endswith("/ws")
```

## Очікування з expect (retry assertions)

```python
def test_expect_with_retry(page: Page):
    """Перевірки expect автоматично повторюються до успіху."""
    page.goto("https://example.com/async-page")

    # expect автоматично повторює перевірку протягом таймауту
    expect(page.get_by_test_id("status")).to_have_text("Завершено")

    # Очікування зміни тексту
    page.get_by_role("button", name="Почати обробку").click()
    expect(page.get_by_test_id("progress")).to_have_text("100%", timeout=30000)

    # Очікування появи елемента
    expect(page.get_by_text("Результати готові")).to_be_visible(timeout=15000)

    # Очікування зміни кількості елементів
    expect(page.get_by_role("listitem")).to_have_count(5, timeout=10000)

    # Очікування зміни URL
    expect(page).to_have_url(re.compile(r".*/results"))
```

::: info Інформація
`expect` — рекомендований спосіб очікування в тестах. Він одночасно і чекає, і перевіряє, що зменшує кількість коду та робить тести читабельнішими.
:::

## Кастомні очікування

```python
def test_custom_wait(page: Page):
    """Створення власних умов очікування."""
    page.goto("https://example.com")

    # Очікування через evaluate (JavaScript в браузері)
    page.wait_for_function("document.querySelectorAll('.item').length >= 10")

    # Очікування з умовою на значення
    page.wait_for_function(
        "() => document.querySelector('#counter').textContent === '100'"
    )

    # Очікування з параметрами
    page.wait_for_function(
        "selector => document.querySelector(selector).classList.contains('loaded')",
        arg="#main-content"
    )

    # Очікування завершення анімації
    page.wait_for_function(
        "() => getComputedStyle(document.querySelector('.modal')).opacity === '1'"
    )
```

## Таймаути та їх налаштування

```python
from playwright.sync_api import sync_playwright

def configure_timeouts():
    """Налаштування різних рівнів таймаутів."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Таймаут за замовчуванням для всіх дій (click, fill тощо)
        page.set_default_timeout(15000)  # 15 секунд

        # Таймаут для навігації (goto, reload)
        page.set_default_navigation_timeout(30000)  # 30 секунд

        # Глобальний таймаут для expect
        expect.set_options(timeout=10000)  # 10 секунд

        page.goto("https://example.com")
        browser.close()
```

## Практичний приклад: тестування динамічного контенту

```python
import re
from playwright.sync_api import Page, expect

def test_dynamic_content_loading(page: Page):
    """Тест сторінки з динамічним завантаженням контенту."""
    page.goto("https://example.com/products")

    # Очікування зникнення скелетону завантаження
    page.locator(".skeleton-loader").wait_for(state="hidden")

    # Перевірка завантаження товарів
    expect(page.get_by_role("listitem")).to_have_count(12, timeout=10000)

    # Фільтрація з очікуванням API відповіді
    with page.expect_response("**/api/products?category=electronics") as resp:
        page.get_by_role("combobox", name="Категорія").select_option("electronics")
    assert resp.value.status == 200

    # Очікування оновлення списку
    expect(page.get_by_role("listitem")).to_have_count(5)

    # Нескінченний скрол — завантаження нових елементів
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    with page.expect_response("**/api/products?page=2"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Перевірка, що з'явились нові елементи
    expect(page.get_by_role("listitem")).not_to_have_count(5)

    # Пошук з автодоповненням
    page.get_by_placeholder("Пошук товарів...").press_sequentially("Ноут", delay=200)
    expect(page.locator(".autocomplete-item")).to_have_count(3, timeout=5000)
    page.locator(".autocomplete-item").first.click()

    # Перевірка завантаження сторінки товару
    expect(page).to_have_url(re.compile(r".*/products/\d+"))
    expect(page.get_by_role("heading", level=1)).to_be_visible()
```

## Антипатерни — чого уникати

```python
import time

def test_bad_waits_example(page: Page):
    """ПОГАНИЙ приклад — так робити НЕ треба."""
    page.goto("https://example.com")

    # ПОГАНО: жорстка затримка
    # time.sleep(5)  # Не використовуйте!

    # ПОГАНО: занадто довгий таймаут для простих операцій
    # page.wait_for_selector("#button", timeout=60000)

    # ДОБРЕ: використовуйте auto-wait та expect
    page.get_by_role("button", name="Зберегти").click()
    expect(page.get_by_text("Збережено")).to_be_visible()
```

::: warning Увага
Ніколи не використовуйте `time.sleep()` в тестах Playwright. Це робить тести повільними та ненадійними. Використовуйте auto-wait, `expect` або конкретні методи очікування.
:::

## Корисні посилання

- [Офіційна документація Auto-waiting](https://playwright.dev/python/docs/actionability)
- [Навігація та очікування](https://playwright.dev/python/docs/navigations)
- [Мережеві події](https://playwright.dev/python/docs/network)
- [Рекомендації щодо очікувань](https://playwright.dev/python/docs/best-practices)
