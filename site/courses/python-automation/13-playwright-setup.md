# Lecture 13: Playwright Setup

Вступ до Playwright та налаштування середовища.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_13_Introduction_Playwright_Setup/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/exercises)

</div>

## Теми лекції

- Що таке Playwright
- Встановлення
- Перший скрипт
- Браузери та контексти

## Що таке Playwright?

Playwright — це бібліотека для автоматизації браузерів від Microsoft.

**Переваги:**
- Підтримка Chromium, Firefox, WebKit
- Автоматичне очікування елементів
- Мобільна емуляція
- Запис відео та скріншотів
- Network interception

## Встановлення

```bash
# Встановлення бібліотеки
pip install playwright

# Встановлення браузерів
playwright install
```

## Перший скрипт

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запуск браузера
    browser = p.chromium.launch(headless=False)

    # Створення сторінки
    page = browser.new_page()

    # Навігація
    page.goto("https://example.com")

    # Отримання заголовка
    print(page.title())

    # Закриття браузера
    browser.close()
```

## Опції запуску браузера

```python
browser = p.chromium.launch(
    headless=False,      # Показувати вікно браузера
    slow_mo=500,         # Затримка між діями (мс)
    devtools=True,       # Відкрити DevTools
)

# Різні браузери
browser = p.chromium.launch()
browser = p.firefox.launch()
browser = p.webkit.launch()
```

## Browser Context

```python
# Context = ізольована сесія (як incognito)
context = browser.new_context(
    viewport={"width": 1920, "height": 1080},
    locale="uk-UA",
    timezone_id="Europe/Kiev",
)

page = context.new_page()

# Кілька сторінок в одному контексті
page1 = context.new_page()
page2 = context.new_page()
```

## Навігація

```python
# Перехід на сторінку
page.goto("https://example.com")
page.goto("https://example.com", wait_until="networkidle")

# Навігація браузера
page.go_back()
page.go_forward()
page.reload()

# URL та title
current_url = page.url
current_title = page.title()
```

## Async версія

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()

asyncio.run(main())
```

## Вправи

::: tip Вправа 1
Напишіть скрипт, що відкриває Google, робить пошук та виводить URL результатів.
:::

::: tip Вправа 2
Створіть скрипт для відкриття сайту в трьох різних браузерах одночасно.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/examples)
