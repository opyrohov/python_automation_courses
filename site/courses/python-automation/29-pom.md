# Lecture 29: Page Object Model Part 1

Патерн Page Object Model для організації тестів.

<div class="lecture-resources">

<a href="/presentations/Lecture_29_Page_Object_Model_Part1/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_29_Page_Object_Model_Part1/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_29_Page_Object_Model_Part1/exercises)

</div>

## Теми лекції

- Що таке POM
- Переваги патерну
- Структура Page Object
- Базовий клас

## Що таке Page Object Model?

**Page Object Model (POM)** — патерн проектування, де кожна сторінка представлена окремим класом, який інкапсулює:
- Локатори елементів
- Методи взаємодії зі сторінкою

## Чому POM?

**Без POM:**
```python
def test_login():
    page.fill("#email", "user@test.com")
    page.fill("#password", "password123")
    page.click("button[type='submit']")
    assert page.is_visible(".dashboard")

def test_login_error():
    page.fill("#email", "wrong@test.com")
    page.fill("#password", "wrong")
    page.click("button[type='submit']")
    assert page.is_visible(".error-message")
```

**Проблеми:**
- Дублювання локаторів
- При зміні UI треба правити всі тести
- Важко підтримувати

## З POM:

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Sign In")
        self.error_message = page.get_by_role("alert")

    def goto(self):
        self.page.goto("/login")
        return self

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        return self

    def get_error(self) -> str:
        return self.error_message.text_content()
```

```python
# tests/test_login.py
def test_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("user@test.com", "password123")
    expect(page).to_have_url("/dashboard")

def test_login_error(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wrong@test.com", "wrong")
    expect(login_page.error_message).to_be_visible()
```

## Структура проекту

```
tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── profile_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_dashboard.py
└── pytest.ini
```

## Базовий клас

```python
# pages/base_page.py
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str = ""):
        self.page.goto(f"/{path}")
        return self

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")
        return self

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
```

## Наслідування

```python
# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "/login"

    def __init__(self, page):
        super().__init__(page)
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Sign In")

    def goto(self):
        super().goto(self.URL)
        return self

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()
        return DashboardPage(self.page)
```

## Fluent Interface

```python
# Ланцюжок методів
login_page = LoginPage(page)
dashboard = (
    login_page
    .goto()
    .login("user@test.com", "password")
    .wait_for_load()
)
```

## Вправи

::: tip Вправа 1
Створіть Page Object для сторінки реєстрації.
:::

::: tip Вправа 2
Реалізуйте BasePage з загальними методами.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_29_Page_Object_Model_Part1/examples)
