# Лекція 31: Інтеграція з Pytest

**Курс автоматизації на Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 31
## Інтеграція з Pytest

Курс автоматизації на Python + Playwright

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Писати тестові функції pytest з Playwright
- Використовувати вбудовані фікстури (page, context, browser)
- Створювати параметризовані тести
- Організовувати тести за допомогою маркерів
- Запускати тести з командного рядка

---

## Слайд 3: Нагадування — що було раніше

До цього моменту ми запускали Playwright-скрипти вручну:

```python
# Старий підхід — запуск скриптів
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    # перевірки через print...
    browser.close()
```

**Проблема:** немає автоматичного визначення pass/fail, немає звітів, немає паралельного виконання!

---

## Слайд 4: Частина 1 — Чому Pytest?

# Частина 1
## Чому Pytest?

Від скриптів до повноцінних тестів

---

## Слайд 5: Проблеми ручних скриптів

**Ручні скрипти мають суттєві обмеження:**

- Немає автоматичного звіту PASS / FAIL
- Потрібно вручну відкривати та закривати браузер
- Немає ізоляції між тестами
- Неможливо запустити окремий тест
- Немає паралельного виконання
- Немає повторного запуску при падінні

---

## Слайд 6: Що дає Pytest

**З Pytest отримуємо:**

- Автоматичний PASS / FAIL
- Браузер керується автоматично (через фікстури)
- Кожен тест ізольований
- Запуск тестів за назвою, маркером, файлом
- Паралельне виконання
- Повторний запуск, звіти, плагіни

---

## Слайд 7: Встановлення

```bash
# Встановлення pytest та плагіну Playwright
pip install pytest pytest-playwright

# Встановлення браузерів (якщо ще не зроблено)
playwright install
```

Пакет `pytest-playwright` автоматично надає фікстури `page`, `context`, `browser`.

---

## Слайд 8: Частина 2 — Базові тестові функції

# Частина 2
## Базові тестові функції

Написання перших тестів на pytest

---

## Слайд 9: Перший тест на Pytest

```python
# test_example.py
from playwright.sync_api import Page

def test_page_title(page: Page):
    """Test that page has correct title."""
    page.goto("https://the-internet.herokuapp.com")
    assert page.title() == "The Internet"
```

**Ключові правила:**
- Файл починається з `test_`
- Функція починається з `test_`
- Параметр `page` — це автоматична фікстура

---

## Слайд 10: До і після

**Раніше (ручний скрипт):**

```python
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())  # Ручна перевірка
    browser.close()
```

**Тепер (pytest):**

```python
def test_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

Різниця очевидна — код значно коротший та чистіший.

---

## Слайд 11: Декілька тестів в одному файлі

```python
# test_login.py
from playwright.sync_api import Page

def test_login_page_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.locator("h2").text_content() == "Login Page"

def test_successful_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url

def test_failed_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wrong")
    page.locator("#password").fill("wrong")
    page.locator("button[type='submit']").click()
    assert "Your username is invalid!" in page.locator("#flash").text_content()
```

---

## Слайд 12: Правила виявлення тестів

Pytest автоматично знаходить тести, що відповідають таким правилам:

| Правило | Приклад |
|---------|---------|
| Файл починається з `test_` | `test_login.py` |
| Функція починається з `test_` | `def test_title():` |
| Клас починається з `Test` | `class TestLogin:` |
| Метод починається з `test_` | `def test_valid():` |

**Увага:** `login_test.py` або `def check_login()` НЕ будуть знайдені!

---

## Слайд 13: Частина 3 — Фікстури Playwright

# Частина 3
## Фікстури Playwright

Автоматичне керування браузером

---

## Слайд 14: Вбудовані фікстури Playwright

| Фікстура | Що надає | Scope |
|----------|----------|-------|
| `page` | Нова сторінка (вкладка) для кожного тесту | per test |
| `context` | Контекст браузера (як інкогніто) | per test |
| `browser` | Екземпляр браузера | per session |

Кожен тест отримує **свіжу сторінку** — повна ізоляція!

---

## Слайд 15: Фікстура `page`

```python
def test_navigation(page):
    """page = свіжа вкладка браузера, створена автоматично."""
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    # page автоматично закривається після тесту!

def test_another(page):
    """Тут інша page — чистий стан!"""
    page.goto("https://example.com")
    # Немає cookies/даних з попереднього тесту
```

Немає потреби створювати браузер, створювати сторінку чи закривати браузер. Pytest робить це автоматично.

---

## Слайд 16: Власні фікстури (conftest.py)

```python
# conftest.py
import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    """Navigate to login page before test."""
    page.goto("https://the-internet.herokuapp.com/login")
    return page

@pytest.fixture
def logged_in_page(page: Page):
    """Login and return authenticated page."""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    return page
```

Файл `conftest.py` — це спеціальний файл, який pytest автоматично підхоплює. Фікстури, визначені в ньому, доступні всім тестам у цій директорії.

---

## Слайд 17: Використання власних фікстур

```python
# test_secure.py

def test_login_page_has_form(login_page):
    """Фікстура login_page вже перейшла на сторінку."""
    assert login_page.locator("#username").is_visible()
    assert login_page.locator("#password").is_visible()

def test_secure_area(logged_in_page):
    """Фікстура logged_in_page вже виконала вхід."""
    assert "/secure" in logged_in_page.url
    heading = logged_in_page.locator("h2")
    assert heading.text_content() == " Secure Area"
```

Фікстури усувають дублювання коду налаштування!

---

## Слайд 18: Частина 4 — Параметризовані тести

# Частина 4
## Параметризовані тести

Тестування декількох вхідних даних однією функцією

---

## Слайд 19: Проблема — дублювання тестів

**Без параметризації:**

```python
def test_checkbox_1(page):
    page.goto(URL)
    page.locator("#checkbox1").check()
    assert page.locator("#checkbox1").is_checked()

def test_checkbox_2(page):  # Та сама логіка!
    page.goto(URL)
    page.locator("#checkbox2").check()
    assert page.locator("#checkbox2").is_checked()
```

Код повторюється — змінюється лише ідентифікатор елемента.

---

## Слайд 20: Рішення — @pytest.mark.parametrize

```python
import pytest

@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith", "SuperSecretPassword!", "/secure"),
    ("wrong", "wrong", "/login"),
])
def test_login(page, username, password, expected):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    assert expected in page.url
```

Одна функція — декілька тестових випадків! Pytest запускає кожен набір параметрів як окремий тест.

---

## Слайд 21: Синтаксис параметризації

```python
# Один параметр
@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://playwright.dev",
])
def test_page_loads(page, url):
    page.goto(url)
    assert page.title()

# Декілька параметрів
@pytest.mark.parametrize("width,height", [
    (1920, 1080),
    (1366, 768),
    (375, 812),
])
def test_responsive(page, width, height):
    page.set_viewport_size({"width": width, "height": height})
    page.goto("https://example.com")
```

У першому випадку тест запуститься двічі — для кожного URL. У другому — тричі, для кожної роздільної здатності.

---

## Слайд 22: Частина 5 — Маркери та групування

# Частина 5
## Маркери та групування

Організація та фільтрація тестів

---

## Слайд 23: Вбудовані маркери

```python
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature(page):
    pass

@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug(page):
    page.goto("https://example.com/broken")
    assert page.locator("#fixed").is_visible()
```

| Маркер | Призначення |
|--------|-------------|
| `@pytest.mark.skip` | Завжди пропустити цей тест |
| `@pytest.mark.xfail` | Очікуване падіння (відомий баг) |
| `@pytest.mark.skipif` | Пропустити за умовою |

---

## Слайд 24: Власні маркери

```ini
# pytest.ini
[pytest]
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    slow: Tests that take a long time
```

```python
# test_login.py
import pytest

@pytest.mark.smoke
def test_login_page_loads(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.locator("h2").is_visible()

@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(page):
    # ... тест логіну
    pass

@pytest.mark.regression
def test_login_error_messages(page):
    # ... детальний тест
    pass
```

Маркери необхідно зареєструвати в `pytest.ini`, щоб уникнути попереджень.

---

## Слайд 25: Запуск тестів за маркером

```bash
# Запустити тільки smoke тести
pytest -m smoke

# Запустити тільки regression тести
pytest -m regression

# Запустити smoke АБО regression
pytest -m "smoke or regression"

# Запустити smoke, але НЕ slow
pytest -m "smoke and not slow"
```

Маркери дозволяють гнучко обирати, які тести запускати залежно від потреби — наприклад, smoke-набір для швидкої перевірки перед деплоєм.

---

## Слайд 26: Частина 6 — Запуск тестів

# Частина 6
## Запуск тестів

Опції командного рядка

---

## Слайд 27: Базові команди Pytest

```bash
# Запуск усіх тестів у поточній директорії
pytest

# Запуск конкретного файлу
pytest test_login.py

# Запуск конкретної тестової функції
pytest test_login.py::test_successful_login

# Запуск тестів за ключовим словом
pytest -k "login"

# Запуск тестів за виразом ключових слів
pytest -k "login and not error"
```

---

## Слайд 28: Корисні прапорці

| Прапорець | Що робить |
|-----------|-----------|
| `-v` | Розгорнутий вивід (показує назви тестів) |
| `-s` | Показати вивід print() |
| `--headed` | Показати вікно браузера |
| `--slowmo 500` | Сповільнити дії (мс) |
| `--browser chromium` | Обрати браузер |
| `--browser-channel chrome` | Використати встановлений Chrome |
| `-x` | Зупинитися на першому падінні |
| `--lf` | Запустити лише тести, що впали минулого разу |

---

## Слайд 29: Прапорці Playwright

```bash
# Запуск з видимим браузером
pytest --headed

# Сповільнення для налагодження
pytest --headed --slowmo 1000

# Використання Firefox замість Chromium
pytest --browser firefox

# Використання WebKit (рушій Safari)
pytest --browser webkit

# Запуск у декількох браузерах
pytest --browser chromium --browser firefox
```

---

## Слайд 30: Вивід Pytest

```
$ pytest test_login.py -v

======================== test session starts ========================
collected 3 items

test_login.py::test_login_page_loads PASSED      [33%]
test_login.py::test_successful_login PASSED      [66%]
test_login.py::test_failed_login PASSED          [100%]

======================== 3 passed in 5.42s ========================
```

Чіткий результат PASS/FAIL для кожного тесту з вимірюванням часу виконання.

---

## Слайд 31: Підсумок

| Концепція | Призначення |
|-----------|-------------|
| `def test_*(page)` | Тестова функція з автоматичною page |
| `@pytest.fixture` | Повторно використовуване налаштування тесту |
| `@pytest.mark.parametrize` | Декілька наборів тестових даних |
| `@pytest.mark.smoke` | Групування та фільтрація тестів |
| `pytest -v --headed` | Запуск тестів з опціями |
| `conftest.py` | Спільні фікстури |

---

## Слайд 32: Домашнє завдання

**Завдання:**

1. Створити `test_checkboxes.py`:
   - Тести на встановлення / зняття прапорців
   - Використати parametrize для обох чекбоксів

2. Створити `conftest.py`:
   - Фікстура, яка переходить на сторінку
   - Фікстура, яка виконує вхід

3. Додати маркери:
   - Позначити тести як `smoke` або `regression`
   - Запустити лише `smoke` тести

---

## Слайд 33: Наступна лекція

**Лекція 32: Конфігурація та налаштування тестів**

- Конфігурація pytest.ini
- conftest.py поглиблено
- Опції браузера та таймаути
- Скріншоти та трейси при падінні
- Мультибраузерне тестування

**Практика:** Запустіть усі приклади з `pytest -v --headed`

---

## Слайд 34: Фінальний слайд

# Чудово!
## Основи Pytest засвоєно!

Тестові функції, фікстури, parametrize, маркери, CLI
