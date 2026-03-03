# Налаштування Playwright

Playwright — це сучасний фреймворк для автоматизації браузерів від Microsoft. У цьому розділі ми розглянемо встановлення, конфігурацію та базове налаштування Playwright для Python.

## Встановлення

Для початку роботи з Playwright необхідно встановити пакет та завантажити браузери.

```python
# Встановлення Playwright через pip
pip install playwright

# Завантаження браузерів (Chromium, Firefox, WebKit)
playwright install

# Встановлення тільки конкретного браузера
playwright install chromium
playwright install firefox
playwright install webkit
```

::: tip Порада
Рекомендується використовувати віртуальне середовище Python для ізоляції залежностей проєкту.
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install playwright
playwright install
```
:::

## Встановлення з pytest-playwright

Для інтеграції з pytest встановіть додатковий пакет:

```python
# Встановлення pytest-playwright для зручної роботи з тестами
pip install pytest-playwright

# Це також автоматично встановить playwright
playwright install
```

## Базова конфігурація

### Запуск браузера

```python
from playwright.sync_api import sync_playwright

def basic_setup():
    with sync_playwright() as p:
        # Запуск Chromium у видимому режимі
        browser = p.chromium.launch(headless=False)

        # Створення нового контексту з налаштуваннями
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="uk-UA",
            timezone_id="Europe/Kyiv",
        )

        # Створення нової сторінки
        page = context.new_page()
        page.goto("https://example.com")

        # Закриття ресурсів
        context.close()
        browser.close()
```

### Параметри запуску браузера

```python
from playwright.sync_api import sync_playwright

def browser_options():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,          # Видимий режим
            slow_mo=500,             # Затримка між діями (мс)
            args=["--start-maximized"],  # Аргументи командного рядка
            devtools=True,           # Відкрити DevTools
        )

        # Контекст з розширеними налаштуваннями
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Custom User Agent",
            locale="uk-UA",
            timezone_id="Europe/Kyiv",
            geolocation={"longitude": 30.5234, "latitude": 50.4501},
            permissions=["geolocation"],
            color_scheme="dark",     # Темна тема
            ignore_https_errors=True,
        )

        page = context.new_page()
        page.goto("https://example.com")

        browser.close()
```

## Конфігурація pytest-playwright

### Файл conftest.py

```python
import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Налаштування контексту браузера для всіх тестів."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "uk-UA",
        "timezone_id": "Europe/Kyiv",
        "ignore_https_errors": True,
    }

@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Створення нової сторінки з базовими налаштуваннями."""
    page = context.new_page()
    # Встановлення таймауту за замовчуванням
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)
    yield page
    page.close()

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Фікстура для автентифікованої сторінки."""
    page.goto("https://example.com/login")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Пароль").fill("password123")
    page.get_by_role("button", name="Увійти").click()
    page.wait_for_url("**/dashboard")
    return page
```

### Файл pytest.ini

```ini
[pytest]
# Налаштування для pytest-playwright
addopts = --browser chromium --headed --slowmo 100
# Інші корисні параметри:
# --browser firefox
# --browser webkit
# --browser-channel chrome
# --headed (видимий режим)
# --slowmo 100 (затримка 100мс)
```

::: warning Увага
Параметр `--headed` увімкне видимий режим браузера. Для CI/CD використовуйте `headless` режим (за замовчуванням).
:::

## Збереження стану автентифікації

```python
from playwright.sync_api import sync_playwright

def save_auth_state():
    """Збереження стану авторизації для повторного використання."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Виконуємо авторизацію
        page.goto("https://example.com/login")
        page.get_by_label("Email").fill("user@test.com")
        page.get_by_label("Пароль").fill("secret123")
        page.get_by_role("button", name="Увійти").click()
        page.wait_for_url("**/dashboard")

        # Зберігаємо стан у файл
        context.storage_state(path="auth_state.json")
        browser.close()

def use_saved_auth():
    """Використання збереженого стану авторизації."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Завантажуємо збережений стан
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()

        # Вже авторизовані — переходимо на захищену сторінку
        page.goto("https://example.com/dashboard")
        browser.close()
```

## Налаштування для CI/CD

```yaml
# Приклад GitHub Actions конфігурації
name: Playwright Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Встановлення залежностей
        run: |
          pip install pytest-playwright
          playwright install --with-deps chromium
      - name: Запуск тестів
        run: pytest tests/ --browser chromium
      - name: Завантаження звітів
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: test-results/
```

::: info Інформація
У CI/CD середовищі використовуйте `playwright install --with-deps` для автоматичного встановлення системних залежностей.
:::

## Корисні посилання

- [Офіційна документація з встановлення](https://playwright.dev/python/docs/intro)
- [Конфігурація pytest-playwright](https://playwright.dev/python/docs/test-runners)
- [Параметри запуску браузера](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch)
- [Збереження стану автентифікації](https://playwright.dev/python/docs/auth)
