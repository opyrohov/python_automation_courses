# Screenshots & Video — Документування тестів

Playwright надає потужні інструменти для візуальної документації тестів: знімки екрану, запис відео та трейсинг. Ці можливості критично важливі для діагностики помилок та аналізу поведінки тестів. У цьому розділі розглянемо всі способи візуальної документації.

## Screenshots — Знімки екрану

### Базові знімки

```python
from playwright.sync_api import Page

def test_basic_screenshots(page: Page):
    """Створення знімків екрану сторінки."""
    page.goto("https://example.com")

    # Знімок усієї видимої частини сторінки
    page.screenshot(path="screenshots/homepage.png")

    # Повний знімок сторінки (з прокруткою)
    page.screenshot(path="screenshots/full_page.png", full_page=True)

    # Знімок у форматі JPEG з якістю
    page.screenshot(path="screenshots/homepage.jpg", type="jpeg", quality=80)

    # Отримання знімку як байтів (без збереження у файл)
    screenshot_bytes = page.screenshot()
    # Можна прикріпити до звіту або відправити на сервер
```

### Знімки елементів

```python
def test_element_screenshots(page: Page):
    """Знімки окремих елементів на сторінці."""
    page.goto("https://example.com/dashboard")

    # Знімок конкретного елемента
    page.get_by_test_id("stats-chart").screenshot(path="screenshots/chart.png")

    # Знімок таблиці
    page.get_by_role("table").screenshot(path="screenshots/data_table.png")

    # Знімок форми
    page.locator("form#registration").screenshot(path="screenshots/form.png")

    # Знімок навігаційного меню
    page.locator("nav.sidebar").screenshot(path="screenshots/sidebar.png")
```

### Параметри знімків

```python
def test_screenshot_options(page: Page):
    """Додаткові параметри для знімків екрану."""
    page.goto("https://example.com")

    # Приховання певних елементів на знімку
    page.screenshot(
        path="screenshots/no_ads.png",
        mask=[
            page.locator(".advertisement"),
            page.locator(".cookie-banner"),
        ],
    )

    # Колір маски (за замовчуванням — рожевий)
    page.screenshot(
        path="screenshots/masked.png",
        mask=[page.locator(".dynamic-content")],
        mask_color="#000000",  # Чорна маска
    )

    # Знімок з анімаціями зупиненими
    page.screenshot(
        path="screenshots/no_animation.png",
        animations="disabled",
    )

    # Знімок з певним масштабом (для Retina)
    page.screenshot(
        path="screenshots/retina.png",
        scale="css",  # або "device"
    )
```

## Знімки при помилках тесту

### Автоматичні знімки через conftest.py

```python
# conftest.py
import pytest
from datetime import datetime
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page: Page):
    """Автоматичний знімок екрану при невдалому тесті."""
    yield
    # Виконується після кожного тесту
    if request.node.rep_call and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        page.screenshot(
            path=f"screenshots/failures/{test_name}_{timestamp}.png",
            full_page=True,
        )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для збереження результату тесту у request.node."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
```

### Знімки на кроках тесту

```python
def test_checkout_with_screenshots(page: Page):
    """Тест з документуванням кожного кроку."""
    page.goto("https://example.com/cart")
    page.screenshot(path="screenshots/steps/01_cart.png")

    # Заповнення форми доставки
    page.get_by_label("Адреса").fill("вул. Хрещатик, 1")
    page.get_by_label("Місто").select_option("Київ")
    page.screenshot(path="screenshots/steps/02_delivery_form.png")

    # Вибір оплати
    page.get_by_role("radio", name="Карткою онлайн").check()
    page.screenshot(path="screenshots/steps/03_payment.png")

    # Підтвердження замовлення
    page.get_by_role("button", name="Оформити").click()
    page.screenshot(path="screenshots/steps/04_confirmation.png")
```

## Video — Запис відео

### Налаштування запису відео

```python
from playwright.sync_api import sync_playwright

def test_video_recording():
    """Запис відео виконання тесту."""
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # Увімкнення запису відео через контекст
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720},
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.get_by_role("link", name="Продукти").click()
        page.get_by_text("Ноутбук Pro").click()

        # Відео зберігається при закритті контексту
        context.close()
        browser.close()

        # Шлях до відео доступний через page.video
        # video_path = page.video.path()
```

### Відео через pytest-playwright

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Налаштування запису відео для всіх тестів."""
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720},
    }
```

```bash
# Або через командний рядок
pytest --video on                    # Завжди записувати відео
pytest --video retain-on-failure     # Зберігати тільки при помилці
```

::: tip Порада
Використовуйте `--video retain-on-failure` для CI/CD — це зберігає відео тільки для невдалих тестів, економлячи місце на диску.
:::

## Tracing — Детальне трасування

Tracing — найпотужніший інструмент діагностики в Playwright. Він записує повну інформацію про виконання тесту: знімки, мережеві запити, console логи, DOM-снапшоти.

### Запис трейсу

```python
from playwright.sync_api import sync_playwright

def test_with_tracing():
    """Запис детального трейсу виконання тесту."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Початок запису трейсу
        context.tracing.start(
            screenshots=True,     # Знімки на кожному кроці
            snapshots=True,       # DOM-снапшоти
            sources=True,         # Вихідний код тестів
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.get_by_role("link", name="Каталог").click()
        page.get_by_placeholder("Пошук").fill("Ноутбук")
        page.get_by_placeholder("Пошук").press("Enter")

        # Зупинка та збереження трейсу
        context.tracing.stop(path="traces/test_trace.zip")

        context.close()
        browser.close()
```

### Перегляд трейсу

```bash
# Відкриття трейсу в Trace Viewer
playwright show-trace traces/test_trace.zip

# Або через вебінтерфейс
# Перейдіть на https://trace.playwright.dev та завантажте .zip файл
```

### Трейсинг через pytest-playwright

```python
# conftest.py
import pytest
from playwright.sync_api import BrowserContext

@pytest.fixture
def context(context: BrowserContext):
    """Фікстура з трейсингом для кожного тесту."""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="traces/trace.zip")
```

```bash
# Або через командний рядок pytest-playwright
pytest --tracing on                   # Завжди записувати трейс
pytest --tracing retain-on-failure    # Тільки при помилці
```

::: info Інформація
Trace Viewer показує: таймлайн дій, знімки до/після кожної дії, мережеві запити, console логи, та вихідний код тесту. Це найкращий інструмент для дебагу.
:::

## Групові налаштування для pytest

```python
# conftest.py — повна конфігурація документування тестів
import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page, BrowserContext

# Директорії для артефактів
SCREENSHOTS_DIR = Path("test-results/screenshots")
VIDEOS_DIR = Path("test-results/videos")
TRACES_DIR = Path("test-results/traces")

@pytest.fixture(scope="session", autouse=True)
def create_artifact_dirs():
    """Створення директорій для артефактів тестів."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    TRACES_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Глобальні налаштування контексту з відео."""
    return {
        **browser_context_args,
        "record_video_dir": str(VIDEOS_DIR),
        "record_video_size": {"width": 1280, "height": 720},
    }

@pytest.fixture
def context(context: BrowserContext):
    """Контекст з трейсингом."""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context

@pytest.fixture(autouse=True)
def test_artifacts(request, page: Page, context: BrowserContext):
    """Збереження артефактів після кожного тесту."""
    yield
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Завжди зберігаємо знімок фінального стану
    page.screenshot(path=str(SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"))

    # Зберігаємо трейс
    trace_path = str(TRACES_DIR / f"{test_name}_{timestamp}.zip")
    context.tracing.stop(path=trace_path)
```

## Візуальне тестування (Visual Comparison)

```python
from playwright.sync_api import Page, expect

def test_visual_comparison(page: Page):
    """Порівняння знімків для виявлення візуальних регресій."""
    page.goto("https://example.com")

    # Порівняння з еталонним знімком
    # При першому запуску створюється еталон
    expect(page).to_have_screenshot("homepage.png")

    # Порівняння з допуском відхилення
    expect(page).to_have_screenshot(
        "homepage_tolerant.png",
        max_diff_pixels=100,         # Максимум 100 пікселів різниці
    )

    # Порівняння з порогом відхилення
    expect(page).to_have_screenshot(
        "homepage_threshold.png",
        threshold=0.2,               # Допуск кольору 20%
    )

    # Порівняння окремого елемента
    expect(page.locator("header")).to_have_screenshot("header.png")

    # Маскування динамічних елементів
    expect(page).to_have_screenshot(
        "static_content.png",
        mask=[
            page.locator(".timestamp"),
            page.locator(".random-banner"),
        ],
    )
```

::: warning Увага
Візуальне тестування чутливе до середовища: різні ОС, шрифти та роздільна здатність можуть впливати на результати. Рекомендується запускати візуальні тести в Docker для консистентності.
:::

## Налаштування для CI/CD

```yaml
# GitHub Actions з артефактами тестів
name: Playwright Tests
on: [push]

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
      - name: Запуск тестів з артефактами
        run: |
          pytest tests/ \
            --browser chromium \
            --video retain-on-failure \
            --tracing retain-on-failure \
            --screenshot on
      - name: Завантаження артефактів тестів
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-artifacts
          path: |
            test-results/
            screenshots/
            videos/
            traces/
          retention-days: 14
```

## Практичний приклад: звіт про помилку

```python
from playwright.sync_api import Page, BrowserContext, expect
from datetime import datetime
import json

def test_with_full_reporting(page: Page, context: BrowserContext):
    """Тест з повною документацією для аналізу помилок."""
    # Старт трейсингу
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://example.com/checkout")
    page.screenshot(path="reports/step_01_checkout_page.png")

    # Заповнення форми
    page.get_by_label("Ім'я").fill("Олена Коваленко")
    page.get_by_label("Email").fill("olena@test.com")
    page.get_by_label("Телефон").fill("+380991234567")
    page.screenshot(path="reports/step_02_form_filled.png")

    # Оформлення замовлення
    page.get_by_role("button", name="Оформити").click()
    page.screenshot(path="reports/step_03_after_submit.png")

    # Перевірка результату
    try:
        expect(page.get_by_text("Замовлення прийнято")).to_be_visible(timeout=10000)
        page.screenshot(path="reports/step_04_success.png")
    except Exception:
        # У разі помилки — збираємо максимум інформації
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(
            path=f"reports/error_{timestamp}.png",
            full_page=True,
        )
        context.tracing.stop(path=f"reports/error_trace_{timestamp}.zip")

        # Збір console логів та помилок
        console_logs = []
        page.on("console", lambda msg: console_logs.append({
            "type": msg.type,
            "text": msg.text,
        }))

        # Збір інформації про сторінку
        page_info = {
            "url": page.url,
            "title": page.title(),
            "timestamp": timestamp,
        }
        with open(f"reports/error_info_{timestamp}.json", "w") as f:
            json.dump(page_info, f, indent=2, ensure_ascii=False)

        raise  # Повторно піднімаємо помилку
```

## Корисні посилання

- [Офіційна документація Screenshots](https://playwright.dev/python/docs/screenshots)
- [Запис відео](https://playwright.dev/python/docs/videos)
- [Trace Viewer](https://playwright.dev/python/docs/trace-viewer)
- [Візуальні порівняння](https://playwright.dev/python/docs/test-snapshots)
- [Online Trace Viewer](https://trace.playwright.dev/)
