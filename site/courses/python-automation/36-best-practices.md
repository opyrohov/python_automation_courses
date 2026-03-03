# Лекція 36: Best Practices та фінальний проєкт

Найкращі практики та фінальний проект.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_36_Best_Practices_Final_Project/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_36_Best_Practices_Final_Project/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_36_Best_Practices_Final_Project/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Best practices для тестів
- Структура проекту
- CI/CD інтеграція
- Фінальний проект

## Структура проекту

```
automation_project/
├── pages/                    # Page Objects
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                    # Тести
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   └── test_dashboard.py
├── utils/                    # Утиліти
│   ├── __init__.py
│   ├── api_client.py
│   └── test_data.py
├── data/                     # Тестові дані
│   ├── users.json
│   └── products.json
├── reports/                  # Звіти
├── screenshots/              # Скріншоти
├── pytest.ini
├── requirements.txt
└── README.md
```

## Best Practices: Локатори

```python
# ✅ ДОБРЕ - стабільні локатори
page.get_by_role("button", name="Submit")
page.get_by_test_id("login-button")
page.get_by_label("Email")

# ❌ ПОГАНО - нестабільні локатори
page.locator("div.css-1234 > button:nth-child(2)")
page.locator("//div[@class='container']//button[1]")
```

## Best Practices: Assertions

```python
from playwright.sync_api import expect

# ✅ ДОБРЕ - Playwright assertions (auto-wait)
expect(page.get_by_text("Success")).to_be_visible()
expect(page).to_have_url("**/dashboard")

# ❌ ПОГАНО - Python assertions (no auto-wait)
assert page.is_visible("text=Success")
assert "/dashboard" in page.url
```

## Best Practices: Waits

```python
# ✅ ДОБРЕ - автоматичне очікування
page.get_by_role("button").click()  # чекає автоматично

# ✅ ДОБРЕ - явне очікування коли потрібно
page.wait_for_url("**/dashboard")
expect(page.get_by_text("Loaded")).to_be_visible()

# ❌ ПОГАНО - фіксовані затримки
import time
time.sleep(3)  # НІКОЛИ!
```

## Best Practices: Test Data

```python
# utils/test_data.py
import json
from pathlib import Path

def load_test_data(filename: str) -> dict:
    path = Path(__file__).parent.parent / "data" / filename
    with open(path) as f:
        return json.load(f)

# Використання
users = load_test_data("users.json")

# Або з faker
from faker import Faker
fake = Faker("uk_UA")

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
```

## Best Practices: Page Objects

```python
# pages/login_page.py
class LoginPage:
    """Page Object для сторінки логіну."""

    def __init__(self, page):
        self.page = page
        # Локатори визначаються один раз
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Sign In")
        self.error = page.get_by_role("alert")

    def login(self, email: str, password: str) -> "DashboardPage":
        """Виконує логін та повертає DashboardPage."""
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
        return DashboardPage(self.page)

    def login_and_expect_error(self, email: str, password: str) -> str:
        """Виконує логін та повертає текст помилки."""
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
        expect(self.error).to_be_visible()
        return self.error.text_content()
```

## Best Practices: Fixtures

```python
# conftest.py
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page, base_url):
    """Fixture для LoginPage."""
    page.goto(f"{base_url}/login")
    return LoginPage(page)

@pytest.fixture
def authenticated_user(page, base_url):
    """Fixture з авторизованим користувачем."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("user@test.com", "password")
    yield page
    # cleanup якщо потрібно
```

## CI/CD: GitHub Actions

```yaml
# .github/workflows/tests.yml
name: Playwright Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps

      - name: Run tests
        run: pytest --html=report.html

      - name: Upload report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-report
          path: report.html
```

## Фінальний проект

::: tip Завдання
Створіть автоматизований тест-сьют для e-commerce сайту:

1. **Page Objects:**
   - HomePage
   - ProductPage
   - CartPage
   - CheckoutPage

2. **Тести:**
   - Пошук товару
   - Додавання в кошик
   - Оформлення замовлення

3. **Вимоги:**
   - pytest-playwright
   - Параметризовані тести
   - CI/CD pipeline
   - Звіти (pytest-html)
:::

## Чекліст проекту

- [ ] Структура проекту
- [ ] Base Page Object
- [ ] Мінімум 3 Page Objects
- [ ] Мінімум 5 тестів
- [ ] conftest.py з fixtures
- [ ] pytest.ini конфігурація
- [ ] requirements.txt
- [ ] README.md
- [ ] GitHub Actions workflow

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_36_Best_Practices_Final_Project/examples)
