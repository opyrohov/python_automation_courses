# Playwright

Документація з Playwright для Python — потужний інструмент для E2E тестування веб-застосунків.

## Розділи

- [Налаштування](/docs/playwright/setup) - Встановлення та конфігурація
- [Locators](/docs/playwright/locators) - Стратегії пошуку елементів
- [Actions](/docs/playwright/actions) - Взаємодія з елементами
- [Assertions](/docs/playwright/assertions) - Перевірки та очікування
- [Waits](/docs/playwright/waits) - Стратегії очікування
- [Page Object Model](/docs/playwright/page-object) - Патерн організації тестів
- [API Testing](/docs/playwright/api-testing) - Тестування API
- [Screenshots & Video](/docs/playwright/screenshots-video) - Документування тестів

## Швидкий старт

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Навігація
    page.goto("https://example.com")

    # Локатори
    page.get_by_role("button", name="Sign In").click()
    page.get_by_placeholder("Email").fill("user@test.com")

    # Assertions
    expect(page.get_by_text("Welcome")).to_be_visible()

    browser.close()
```

## Корисні посилання

- [Офіційна документація Playwright](https://playwright.dev/python/)
- [Playwright GitHub](https://github.com/microsoft/playwright-python)
