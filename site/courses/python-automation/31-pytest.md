# Lecture 31: Pytest Integration

Інтеграція Playwright з pytest.

<div class="lecture-resources">

<a href="/presentations/Lecture_31_Pytest_Integration/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_31_Pytest_Integration/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_31_Pytest_Integration/exercises)

</div>

## Теми лекції

- pytest-playwright
- Fixtures для Playwright
- Конфігурація
- Запуск тестів

## Встановлення

```bash
pip install pytest-playwright
playwright install
```

## Базовий тест

```python
# test_example.py
from playwright.sync_api import Page, expect

def test_homepage(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")

def test_navigation(page: Page):
    page.goto("https://example.com")
    page.get_by_role("link", name="More information").click()
    expect(page).to_have_url("https://www.iana.org/help/example-domains")
```

## Вбудовані fixtures

```python
# page - нова сторінка для кожного тесту
def test_example(page: Page):
    pass

# context - browser context
def test_with_context(context):
    page1 = context.new_page()
    page2 = context.new_page()

# browser - browser instance
def test_with_browser(browser):
    context = browser.new_context()
    page = context.new_page()
```

## conftest.py

```python
# conftest.py
import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="session")
def base_url():
    return "https://staging.example.com"

@pytest.fixture
def authenticated_page(page: Page, base_url):
    """Сторінка з авторизованим користувачем."""
    page.goto(f"{base_url}/login")
    page.get_by_label("Email").fill("user@test.com")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")
    return page
```

## pytest.ini

```ini
[pytest]
# Базовий URL
base_url = https://example.com

# Браузер
browser = chromium

# Headless режим
headed = true

# Slowmo
slowmo = 100

# Screenshots
screenshot = only-on-failure

# Video
video = retain-on-failure

# Trace
tracing = retain-on-failure
```

## Командний рядок

```bash
# Запуск з різними браузерами
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
pytest --browser chromium --browser firefox  # всі

# Headless/Headed
pytest --headed
pytest --headless

# Slowmo
pytest --slowmo 500

# Base URL
pytest --base-url https://staging.example.com

# Screenshots
pytest --screenshot on
pytest --screenshot only-on-failure

# Video
pytest --video on
pytest --video retain-on-failure

# Tracing
pytest --tracing on
pytest --tracing retain-on-failure
```

## Markers

```python
import pytest

@pytest.mark.skip_browser("firefox")
def test_chromium_only(page):
    pass

@pytest.mark.only_browser("webkit")
def test_webkit_only(page):
    pass
```

## Browser Context Options

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "uk-UA",
        "timezone_id": "Europe/Kiev",
        "permissions": ["geolocation"],
    }
```

## Паралельний запуск

```bash
# Встановлення
pip install pytest-xdist

# Запуск
pytest -n auto           # авто кількість workers
pytest -n 4              # 4 workers
pytest -n auto --dist loadgroup  # групування
```

## Приклад тесту

```python
# tests/test_login.py
import pytest
from playwright.sync_api import Page, expect

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, base_url: str):
        self.page = page
        page.goto(f"{base_url}/login")

    def test_valid_login(self):
        self.page.get_by_label("Email").fill("user@test.com")
        self.page.get_by_label("Password").fill("password123")
        self.page.get_by_role("button", name="Sign In").click()

        expect(self.page).to_have_url("**/dashboard")
        expect(self.page.get_by_text("Welcome")).to_be_visible()

    def test_invalid_password(self):
        self.page.get_by_label("Email").fill("user@test.com")
        self.page.get_by_label("Password").fill("wrong")
        self.page.get_by_role("button", name="Sign In").click()

        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()
```

## Вправи

::: tip Вправа 1
Налаштуйте pytest-playwright для вашого проекту.
:::

::: tip Вправа 2
Створіть тести з різними fixtures для authenticated/anonymous користувачів.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_31_Pytest_Integration/examples)
