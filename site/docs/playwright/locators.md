# Locators — Стратегії пошуку елементів

Локатори в Playwright — це основний спосіб знаходження елементів на сторінці. Playwright пропонує кілька стратегій пошуку, від рекомендованих семантичних локаторів до класичних CSS та XPath селекторів.

## Рекомендовані локатори

Playwright рекомендує використовувати семантичні локатори, які базуються на ролях та тексті елементів. Вони є найбільш стійкими до змін у верстці.

### get_by_role

```python
from playwright.sync_api import Page, expect

def test_role_locators(page: Page):
    """Пошук елементів за їхньою ARIA-роллю."""
    page.goto("https://example.com")

    # Кнопки
    page.get_by_role("button", name="Зберегти").click()
    page.get_by_role("button", name="Видалити", exact=True).click()

    # Посилання
    page.get_by_role("link", name="Головна").click()

    # Заголовки
    heading = page.get_by_role("heading", name="Ласкаво просимо", level=1)
    expect(heading).to_be_visible()

    # Поля вводу
    page.get_by_role("textbox", name="Пошук").fill("Playwright")

    # Чекбокси та радіокнопки
    page.get_by_role("checkbox", name="Погоджуюсь").check()
    page.get_by_role("radio", name="Варіант А").check()

    # Випадаючий список
    page.get_by_role("combobox", name="Країна").select_option("Ukraine")

    # Рядки таблиці
    row = page.get_by_role("row", name="Іван Петренко")
    expect(row).to_be_visible()
```

::: tip Порада
`get_by_role` — найкращий вибір для більшості ситуацій. Він базується на доступності (accessibility) і працює так, як користувач бачить сторінку.
:::

### get_by_text

```python
def test_text_locators(page: Page):
    """Пошук елементів за текстовим вмістом."""
    page.goto("https://example.com")

    # Пошук за частиною тексту
    page.get_by_text("Ласкаво просимо").click()

    # Точний збіг тексту
    page.get_by_text("Увійти", exact=True).click()

    # Пошук за регулярним виразом
    page.get_by_text(re.compile(r"Замовлення #\d+")).click()
```

### get_by_label

```python
def test_label_locators(page: Page):
    """Пошук полів форми за їхніми мітками (label)."""
    page.goto("https://example.com/register")

    # Заповнення форми реєстрації через мітки
    page.get_by_label("Ім'я").fill("Іван")
    page.get_by_label("Прізвище").fill("Петренко")
    page.get_by_label("Електронна пошта").fill("ivan@example.com")
    page.get_by_label("Пароль").fill("SecurePass123!")
    page.get_by_label("Підтвердіть пароль").fill("SecurePass123!")
```

### get_by_placeholder

```python
def test_placeholder_locators(page: Page):
    """Пошук полів за текстом підказки (placeholder)."""
    page.goto("https://example.com")

    page.get_by_placeholder("Введіть ваш email").fill("user@test.com")
    page.get_by_placeholder("Пошук товарів...").fill("Ноутбук")
```

### get_by_alt_text

```python
def test_alt_text_locators(page: Page):
    """Пошук зображень за альтернативним текстом."""
    page.goto("https://example.com")

    # Пошук зображення за alt текстом
    logo = page.get_by_alt_text("Логотип компанії")
    expect(logo).to_be_visible()

    page.get_by_alt_text("Фото профілю").click()
```

### get_by_title

```python
def test_title_locators(page: Page):
    """Пошук елементів за атрибутом title."""
    page.goto("https://example.com")

    page.get_by_title("Налаштування профілю").click()
    page.get_by_title("Закрити вікно").click()
```

### get_by_test_id

```python
def test_testid_locators(page: Page):
    """Пошук елементів за data-testid атрибутом."""
    page.goto("https://example.com")

    # За замовчуванням шукає атрибут data-testid
    page.get_by_test_id("submit-button").click()
    page.get_by_test_id("user-menu").click()
    page.get_by_test_id("cart-counter").text_content()
```

::: info Інформація
Атрибут для `get_by_test_id` можна змінити в конфігурації:
```python
playwright.selectors.set_test_id_attribute("data-qa")
```
:::

## CSS та XPath селектори

```python
def test_css_xpath_locators(page: Page):
    """Класичні CSS та XPath селектори."""
    page.goto("https://example.com")

    # CSS селектори
    page.locator("css=#login-form").is_visible()
    page.locator(".btn-primary").click()
    page.locator("input[type='email']").fill("user@test.com")
    page.locator("div.card >> span.price").text_content()
    page.locator("[data-qa='submit']").click()

    # XPath селектори
    page.locator("xpath=//button[contains(text(), 'Зберегти')]").click()
    page.locator("xpath=//div[@class='menu']//a[@href='/profile']").click()
    page.locator("xpath=//table//tr[td[text()='Активний']]").count()
```

::: warning Увага
CSS та XPath селектори є більш крихкими — вони залежать від структури HTML. Надавайте перевагу семантичним локаторам (`get_by_role`, `get_by_text` тощо).
:::

## Фільтрація локаторів

```python
def test_locator_filtering(page: Page):
    """Звуження пошуку за допомогою фільтрів."""
    page.goto("https://example.com/products")

    # Фільтрація за текстом
    page.get_by_role("listitem").filter(has_text="Ноутбук").click()

    # Фільтрація за вкладеним локатором
    page.get_by_role("listitem").filter(
        has=page.get_by_role("button", name="Купити")
    ).first.click()

    # Фільтрація за відсутністю тексту
    page.get_by_role("listitem").filter(has_not_text="Розпродано").count()

    # Ланцюжок фільтрів
    products = (
        page.get_by_role("listitem")
        .filter(has_text="Ноутбук")
        .filter(has=page.locator(".in-stock"))
    )
    expect(products).to_have_count(3)
```

## Комбінування та ланцюжки локаторів

```python
def test_chaining_locators(page: Page):
    """Побудова складних локаторів через ланцюжки."""
    page.goto("https://example.com")

    # Пошук всередині контейнера
    sidebar = page.locator(".sidebar")
    sidebar.get_by_role("link", name="Профіль").click()

    # Ланцюжок locator
    page.locator(".product-card").locator(".price").first.text_content()

    # nth — вибір за індексом
    page.get_by_role("listitem").nth(2).click()

    # first / last
    page.get_by_role("button", name="Видалити").first.click()
    page.get_by_role("link").last.click()

    # or_ — об'єднання локаторів
    save_btn = page.get_by_role("button", name="Зберегти").or_(
        page.get_by_role("button", name="Save")
    )
    save_btn.click()

    # and_ — перетин локаторів
    active_btn = page.get_by_role("button").and_(page.locator(".active"))
    active_btn.click()
```

## Робота з Frame та iFrame

```python
def test_frame_locators(page: Page):
    """Пошук елементів всередині фреймів."""
    page.goto("https://example.com/with-iframe")

    # Пошук фрейму та взаємодія з його елементами
    frame = page.frame_locator("iframe#payment-form")
    frame.get_by_label("Номер картки").fill("4111111111111111")
    frame.get_by_label("CVV").fill("123")
    frame.get_by_role("button", name="Оплатити").click()

    # Вкладені фрейми
    nested = page.frame_locator("#outer").frame_locator("#inner")
    nested.get_by_text("Контент").is_visible()
```

## Практичний приклад: тестування форми

```python
import re
from playwright.sync_api import Page, expect

def test_registration_form(page: Page):
    """Комплексний тест форми реєстрації з різними локаторами."""
    page.goto("https://example.com/register")

    # Заповнення полів через семантичні локатори
    page.get_by_label("Ім'я").fill("Олена")
    page.get_by_label("Прізвище").fill("Коваленко")
    page.get_by_label("Email").fill("olena@example.com")
    page.get_by_label("Телефон").fill("+380991234567")
    page.get_by_placeholder("Створіть пароль").fill("MyPass123!")

    # Вибір з випадаючого списку
    page.get_by_role("combobox", name="Місто").select_option("Київ")

    # Чекбокс та радіокнопка
    page.get_by_role("checkbox", name="Погоджуюсь з умовами").check()
    page.get_by_role("radio", name="Жінка").check()

    # Відправка форми
    page.get_by_role("button", name="Зареєструватися").click()

    # Перевірка успішної реєстрації
    expect(page.get_by_role("heading", name="Ласкаво просимо")).to_be_visible()
    expect(page.get_by_text(re.compile(r"Олена"))).to_be_visible()
```

## Корисні посилання

- [Офіційна документація Locators](https://playwright.dev/python/docs/locators)
- [Рекомендації щодо вибору локаторів](https://playwright.dev/python/docs/best-practices#use-locators)
- [ARIA roles довідник](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
- [Playwright Codegen — генерація локаторів](https://playwright.dev/python/docs/codegen)
