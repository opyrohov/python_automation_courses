# Page Object Model — Патерн організації тестів

Page Object Model (POM) — це патерн проєктування, який створює об'єктну модель для кожної сторінки або компонента веб-додатку. Він відокремлює логіку тестів від деталей реалізації UI, що робить тести зрозумілішими та легшими в підтримці.

## Навіщо потрібен POM

Без POM тести стають крихкими та складними в підтримці. Зміна одного селектора може вимагати змін у десятках тестів. POM вирішує цю проблему, інкапсулюючи взаємодію з елементами в одному місці.

::: tip Порада
Основний принцип POM: **тести описують ЩО перевіряти**, а Page Object описує **ЯК взаємодіяти** зі сторінкою.
:::

## Базова структура Page Object

### Структура проєкту

```
tests/
├── conftest.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── products_page.py
├── test_login.py
├── test_dashboard.py
└── test_products.py
```

### Базовий Page Object

```python
# tests/pages/base_page.py
from playwright.sync_api import Page, expect

class BasePage:
    """Базовий клас для всіх Page Object."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        """Перехід на сторінку за відносним шляхом."""
        self.page.goto(f"https://example.com{path}")

    def get_title(self) -> str:
        """Отримання заголовку сторінки."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Отримання поточного URL."""
        return self.page.url

    def wait_for_page_loaded(self):
        """Очікування повного завантаження сторінки."""
        self.page.wait_for_load_state("domcontentloaded")
```

## Приклад: Сторінка авторизації

```python
# tests/pages/login_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object для сторінки авторизації."""

    # URL сторінки
    URL = "/login"

    def __init__(self, page: Page):
        super().__init__(page)
        # Визначення локаторів
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Пароль")
        self.login_button = page.get_by_role("button", name="Увійти")
        self.error_message = page.get_by_test_id("error-message")
        self.remember_checkbox = page.get_by_role("checkbox", name="Запам'ятати мене")
        self.forgot_password_link = page.get_by_role("link", name="Забули пароль?")

    def open(self):
        """Відкриття сторінки авторизації."""
        self.navigate(self.URL)
        return self

    def login(self, email: str, password: str):
        """Авторизація з вказаними обліковими даними."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def login_with_remember(self, email: str, password: str):
        """Авторизація з опцією 'Запам'ятати мене'."""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.remember_checkbox.check()
        self.login_button.click()

    def get_error_text(self) -> str:
        """Отримання тексту помилки."""
        return self.error_message.text_content()

    def expect_error_visible(self, message: str):
        """Перевірка відображення помилки."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(message)

    def expect_login_button_disabled(self):
        """Перевірка, що кнопка входу неактивна."""
        expect(self.login_button).to_be_disabled()
```

## Приклад: Сторінка панелі керування

```python
# tests/pages/dashboard_page.py
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    """Page Object для панелі керування."""

    URL = "/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = page.get_by_test_id("welcome-msg")
        self.user_menu = page.get_by_test_id("user-menu")
        self.logout_button = page.get_by_role("menuitem", name="Вийти")
        self.sidebar_links = page.locator("nav.sidebar").get_by_role("link")
        self.notification_badge = page.get_by_test_id("notification-count")
        self.stats_cards = page.locator(".stats-card")

    def open(self):
        """Відкриття панелі керування."""
        self.navigate(self.URL)
        return self

    def get_welcome_text(self) -> str:
        """Отримання тексту вітання."""
        return self.welcome_message.text_content()

    def logout(self):
        """Вихід з облікового запису."""
        self.user_menu.click()
        self.logout_button.click()

    def navigate_to_section(self, section_name: str):
        """Перехід до розділу через бокове меню."""
        self.sidebar_links.filter(has_text=section_name).click()

    def get_notification_count(self) -> int:
        """Отримання кількості сповіщень."""
        text = self.notification_badge.text_content()
        return int(text) if text else 0

    def expect_page_loaded(self):
        """Перевірка, що панель керування завантажилась."""
        expect(self.page).to_have_url(re.compile(r".*/dashboard"))
        expect(self.welcome_message).to_be_visible()
        expect(self.sidebar_links.first).to_be_visible()
```

## Приклад: Сторінка товарів

```python
# tests/pages/products_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Page Object для сторінки каталогу товарів."""

    URL = "/products"

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.get_by_placeholder("Пошук товарів...")
        self.category_filter = page.get_by_role("combobox", name="Категорія")
        self.sort_select = page.get_by_role("combobox", name="Сортування")
        self.product_cards = page.locator(".product-card")
        self.cart_badge = page.get_by_test_id("cart-count")
        self.loading_spinner = page.locator(".loading-spinner")

    def open(self):
        """Відкриття каталогу товарів."""
        self.navigate(self.URL)
        self.loading_spinner.wait_for(state="hidden")
        return self

    def search(self, query: str):
        """Пошук товарів."""
        self.search_input.fill(query)
        self.search_input.press("Enter")
        self.loading_spinner.wait_for(state="hidden")

    def filter_by_category(self, category: str):
        """Фільтрація за категорією."""
        self.category_filter.select_option(label=category)
        self.loading_spinner.wait_for(state="hidden")

    def sort_by(self, option: str):
        """Сортування товарів."""
        self.sort_select.select_option(label=option)
        self.loading_spinner.wait_for(state="hidden")

    def add_to_cart(self, product_name: str):
        """Додавання товару до кошика."""
        card = self.product_cards.filter(has_text=product_name)
        card.get_by_role("button", name="Купити").click()

    def get_product_count(self) -> int:
        """Отримання кількості відображених товарів."""
        return self.product_cards.count()

    def get_product_price(self, product_name: str) -> str:
        """Отримання ціни конкретного товару."""
        card = self.product_cards.filter(has_text=product_name)
        return card.locator(".price").text_content()

    def expect_products_loaded(self, count: int):
        """Перевірка завантаження товарів."""
        expect(self.product_cards).to_have_count(count)

    def expect_empty_results(self):
        """Перевірка відсутності результатів."""
        expect(self.page.get_by_text("Нічого не знайдено")).to_be_visible()
        expect(self.product_cards).to_have_count(0)
```

## Написання тестів з POM

### conftest.py з фікстурами

```python
# tests/conftest.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.products_page import ProductsPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Фікстура для сторінки авторизації."""
    return LoginPage(page).open()

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """Фікстура для панелі керування (з авторизацією)."""
    login = LoginPage(page).open()
    login.login("admin@example.com", "admin123")
    dashboard = DashboardPage(page)
    dashboard.expect_page_loaded()
    return dashboard

@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """Фікстура для каталогу товарів."""
    return ProductsPage(page).open()
```

### Тести авторизації

```python
# tests/test_login.py
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestLogin:
    """Тести сторінки авторизації."""

    def test_successful_login(self, login_page: LoginPage, page):
        """Перевірка успішної авторизації."""
        login_page.login("user@example.com", "password123")
        dashboard = DashboardPage(page)
        dashboard.expect_page_loaded()

    def test_invalid_password(self, login_page: LoginPage):
        """Перевірка помилки при невірному паролі."""
        login_page.login("user@example.com", "wrong_password")
        login_page.expect_error_visible("Невірний email або пароль")

    def test_empty_fields(self, login_page: LoginPage):
        """Перевірка валідації порожніх полів."""
        login_page.login("", "")
        login_page.expect_login_button_disabled()
```

### Тести каталогу товарів

```python
# tests/test_products.py
from pages.products_page import ProductsPage

class TestProducts:
    """Тести каталогу товарів."""

    def test_search_products(self, products_page: ProductsPage):
        """Перевірка пошуку товарів."""
        products_page.search("Ноутбук")
        products_page.expect_products_loaded(5)

    def test_filter_by_category(self, products_page: ProductsPage):
        """Перевірка фільтрації за категорією."""
        products_page.filter_by_category("Електроніка")
        products_page.expect_products_loaded(8)

    def test_add_to_cart(self, products_page: ProductsPage):
        """Перевірка додавання товару до кошика."""
        products_page.add_to_cart("Бездротові навушники")
        assert products_page.cart_badge.text_content() == "1"

    def test_empty_search_results(self, products_page: ProductsPage):
        """Перевірка пошуку без результатів."""
        products_page.search("неіснуючий_товар_xyz")
        products_page.expect_empty_results()
```

## Компонентний Page Object

Для повторюваних компонентів UI (навігація, хедер, модальні вікна) створюйте окремі компоненти:

```python
# tests/pages/components/header.py
from playwright.sync_api import Page, expect

class Header:
    """Компонент хедера (використовується на всіх сторінках)."""

    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator("header .logo")
        self.search = page.get_by_placeholder("Пошук...")
        self.cart_icon = page.get_by_test_id("cart-icon")
        self.user_avatar = page.get_by_test_id("user-avatar")

    def search_for(self, query: str):
        """Глобальний пошук через хедер."""
        self.search.fill(query)
        self.search.press("Enter")

    def open_cart(self):
        """Відкриття кошика."""
        self.cart_icon.click()

    def open_profile_menu(self):
        """Відкриття меню профілю."""
        self.user_avatar.click()
```

```python
# tests/pages/dashboard_page.py (оновлений)
from pages.base_page import BasePage
from pages.components.header import Header

class DashboardPage(BasePage):
    """Page Object з використанням компонентів."""

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)  # Компонент хедера
        # ... інші локатори
```

::: info Інформація
Компонентний підхід зменшує дублювання коду. Якщо хедер змінюється, потрібно оновити лише один клас `Header`, а не кожен Page Object.
:::

## Корисні посилання

- [Playwright рекомендації щодо POM](https://playwright.dev/python/docs/pom)
- [Martin Fowler — PageObject Pattern](https://martinfowler.com/bliki/PageObject.html)
- [Найкращі практики тестування](https://playwright.dev/python/docs/best-practices)
