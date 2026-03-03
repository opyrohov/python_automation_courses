# Лекція 13: Вступ до Playwright та Налаштування

**Курс автоматизації на Python**

---

## Слайд 1: Титульний

# Лекція 13
## Вступ до Playwright та Налаштування

Курс автоматизації на Python

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Що таке Playwright та автоматизація браузера
- Порівняння Playwright та Selenium
- Встановлення Playwright та pytest-playwright
- Налаштування браузерних драйверів (Chromium, Firefox, WebKit)
- Структура проекту для Playwright
- Ваш перший скрипт: відкриття браузера та навігація

**Мета:** Наприкінці лекції у вас буде працюючий Playwright і ваш перший скрипт автоматизації браузера!

---

## Слайд 3: Частина 1 — Що таке Playwright?

# Частина 1
## Що таке Playwright?

Розуміння автоматизації браузера

---

## Слайд 4: Що таке автоматизація браузера?

**Автоматизація браузера** = змусити браузер робити речі автоматично за допомогою коду

**Без автоматизації (вручну):**
- Людина відкриває браузер
- Людина вводить URL
- Людина натискає кнопки
- Людина заповнює форми
- Людина перевіряє результати

**З автоматизацією (Playwright):**
- Код відкриває браузер
- Код переходить за URL
- Код натискає кнопки
- Код заповнює форми
- Код перевіряє результати

---

## Слайд 5: Що таке Playwright?

**Playwright** — це сучасний фреймворк автоматизації браузера, створений Microsoft

**Ключові особливості:**
- **Крос-браузерність**: Chromium, Firefox, WebKit (Safari)
- **Швидкий та надійний**: Автоочікування, без нестабільних тестів
- **Зручний для розробників**: Чудовий API, відмінна документація
- **Підтримка мобільних**: Тестування мобільних веб-переглядів
- **Скріншоти та відео**: Вбудований запис
- **Багато мов**: Python, JavaScript, Java, .NET

**Випущено:** 2020 рік, Microsoft
**Статус:** Активна розробка, готовий до продакшену

---

## Слайд 6: Чому варто використовувати Playwright?

- **Сучасний та швидкий** — побудований з нуля для сучасних веб-додатків
- **Надійний** — автоматично чекає на елементи, зменшує нестабільні тести
- **Потужний** — перехоплення мережі, mock API, геолокація, дозволи
- **Повне рішення для тестування** — скріншоти, відео, trace viewer, інспектор
- **Чудовий для CI/CD** — headless режим, паралелізація, підтримка Docker

---

## Слайд 7: Що можна робити з Playwright?

- **End-to-End тестування** — тестування повних користувацьких сценаріїв
- **Веб-скрейпінг** — витягування даних з веб-сайтів
- **Тестування скріншотів** — візуальне регресійне тестування
- **Автоматизація процесів** — автоматизація повторюваних веб-завдань
- **Тестування продуктивності** — вимірювання часу завантаження сторінок
- **Тестування доступності** — перевірка ARIA, контрасту, клавіатурної навігації

---

## Слайд 8: Частина 2 — Playwright vs Selenium

# Частина 2
## Playwright vs Selenium

Розуміння відмінностей

---

## Слайд 9: Що таке Selenium?

**Selenium** був стандартом автоматизації браузера з 2004 року

**Характеристики:**
- **Зрілий:** 20+ років, перевірений у боях
- **Популярний:** Величезна спільнота, багато ресурсів
- **Протокол WebDriver:** Галузевий стандарт (W3C)
- **Багато прив'язок:** Python, Java, C#, Ruby, JavaScript
- **Крос-браузерність:** Chrome, Firefox, Safari, Edge

**Проблеми:**
- Повільніше виконання
- Нестабільні тести (проблеми з таймінгом)
- Складне налаштування (драйвери, версії)
- Обмежені вбудовані функції

---

## Слайд 10: Playwright vs Selenium: Ключові відмінності

| Функція | Playwright | Selenium |
|---------|------------|----------|
| **Вік** | 2020 (Сучасний) | 2004 (Зрілий) |
| **Швидкість** | Швидший | Повільніший |
| **Автоочікування** | Вбудоване | Вручну |
| **Браузери** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge |
| **Налаштування** | Просте (автовстановлення) | Складне (керування драйверами) |
| **Контроль мережі** | Повний контроль | Обмежений |
| **Скріншоти/Відео** | Вбудовані | Сторонні |

---

## Слайд 11: Коли що використовувати?

**Обирайте Playwright якщо:**
- Починаєте новий проект
- Потрібна швидкість та надійність
- Тестуєте сучасні веб-додатки
- Хочете вбудовані функції (відео, скріншоти, мережа)
- Потрібна емуляція мобільного браузера

**Обирайте Selenium якщо:**
- Великий існуючий набір тестів Selenium
- Команда вже експерти в Selenium
- Організаційні вимоги або політика
- Потрібні специфічні інструменти екосистеми Selenium

**Порада:** Для нових проектів Playwright — сучасний вибір!

---

## Слайд 12: Частина 3 — Встановлення Playwright

# Частина 3
## Встановлення Playwright

Налаштування вашого середовища

---

## Слайд 13: Перевірка передумов

Перед встановленням Playwright переконайтесь, що у вас є:

**Python 3.1x** встановлений
```bash
python --version
# Повинно показати Python 3.10+
```

**Віртуальне середовище** створене та активоване
```bash
# Створення venv
python -m venv venv

# Активація (Windows)
venv\Scripts\activate

# Активація (Mac/Linux)
source venv/bin/activate
```

**Місце на диску:** ~500 МБ для бінарних файлів браузерів

---

## Слайд 14: Встановлення: Крок за кроком

```bash
# Крок 1: Переконайтесь, що venv активовано
(venv) $

# Крок 2: Встановіть пакет Playwright Python
pip install playwright

# Крок 3: Встановіть pytest та pytest-playwright
pip install pytest pytest-playwright

# Крок 4: Встановіть бінарні файли браузерів
playwright install

# Крок 5: Перевірте встановлення
playwright --version
pytest --version
```

**Це все!** Playwright готовий до використання.

---

## Слайд 15: Що встановлюється?

**Пакети Python:**
```
playwright==1.55.0          # Основна бібліотека Playwright
pytest==8.4.2               # Фреймворк тестування
pytest-playwright==0.7.1    # Інтеграція Pytest + Playwright
```

**Бінарні файли браузерів:**
- **Chromium** ~300 МБ (рушій Chrome/Edge)
- **Firefox** ~150 МБ (Mozilla Firefox)
- **WebKit** ~50 МБ (рушій Safari)

**Всього:** ~500 МБ

**Розташування:** Браузери зберігаються в кеші користувача, не в venv

---

## Слайд 16: Частина 4 — Налаштування браузерних драйверів

# Частина 4
## Налаштування браузерних драйверів

Розуміння бінарних файлів браузерів

---

## Слайд 17: Що таке браузерні драйвери?

**Браузерний драйвер** = програма, яка керує браузером

**Як це працює:**

```
Ваш Python код → Playwright → Браузерний драйвер → Браузер
```

**Перевага Playwright:** Автоматично завантажує та керує всіма браузерними драйверами!

---

## Слайд 18: Три браузери Playwright

**1. Chromium** (За замовчуванням)
- Open-source версія Chrome/Edge
- Найпопулярніший браузерний рушій (~65% ринку)
- Використовуйте для: Тестування Chrome, Edge, Brave, Opera

**2. Firefox**
- Браузер Mozilla Firefox
- Інший рушій рендерингу (Gecko)
- Використовуйте для: Firefox-специфічного тестування

**3. WebKit**
- Рушій рендерингу Safari
- Працює на Windows/Linux теж!
- Використовуйте для: Тестування Safari/iOS веб

---

## Слайд 19: Встановлення браузерів

```bash
# Встановити всі браузери (рекомендовано)
playwright install

# Встановити конкретний браузер
playwright install chromium
playwright install firefox
playwright install webkit

# Встановити браузери з залежностями (Linux)
playwright install --with-deps

# Список встановлених браузерів
playwright install --help
```

**Важливо:** Запустіть `playwright install` після встановлення Python пакета!

**Порада:** Для CI/CD встановлюйте тільки chromium для економії місця та часу

---

## Слайд 20: Частина 5 — Налаштування структури проекту

# Частина 5
## Налаштування структури проекту

Організація вашого Playwright проекту

---

## Слайд 21: Структура проекту Playwright

```
my_playwright_project/
│
├── venv/                      # Віртуальне середовище
│
├── tests/                     # Тестові файли
│   ├── __init__.py
│   ├── conftest.py           # Pytest фікстури
│   ├── test_login.py
│   ├── test_search.py
│   └── test_checkout.py
│
├── pages/                     # Page Object Model (пізніше)
│   ├── __init__.py
│   └── base_page.py
│
├── utils/                     # Допоміжні утиліти
│   ├── __init__.py
│   └── config.py
│
├── test_data/                 # Тестові дані
│   └── users.json
│
├── requirements.txt           # Залежності
├── pytest.ini                 # Конфігурація Pytest
└── .env                       # Змінні середовища
```

---

## Слайд 22: Створення структури проекту

```bash
# Створити папку проекту
mkdir my_playwright_project
cd my_playwright_project

# Створити структуру папок
mkdir tests pages utils test_data

# Створити __init__.py файли (Windows)
type nul > tests\__init__.py
type nul > pages\__init__.py
type nul > utils\__init__.py

# Створити __init__.py файли (Mac/Linux)
touch tests/__init__.py pages/__init__.py utils/__init__.py

# Створити віртуальне середовище
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

---

## Слайд 23: Створення requirements.txt

```txt
# requirements.txt для проекту Playwright

playwright==1.55.0
pytest==8.4.2
pytest-playwright==0.7.1
python-dotenv==1.2.1
```

**Встановлення залежностей:**

```bash
# Встановити всі пакети
pip install -r requirements.txt

# Встановити бінарні файли браузерів
playwright install

# Перевірити
pip list | findstr playwright  # Windows
pip list | grep playwright     # Mac/Linux
```

---

## Слайд 24: Налаштування pytest.ini

```ini
# pytest.ini

[pytest]
# Де шукати тести
testpaths = tests

# Маркери тестів
markers =
    smoke: Швидкі smoke тести
    regression: Повний набір регресійних тестів
    login: Тести потоку логіну
    browser: Браузер-специфічні тести

# Параметри командного рядка за замовчуванням
addopts = -v --tb=short --strict-markers

# Playwright-специфічні опції (опціонально)
# --headed: Запуск тестів у headed режимі (бачити браузер)
# --browser chromium: Запуск тестів у конкретному браузері
# --slowmo 1000: Сповільнити операції на 1000мс
```

---

## Слайд 25: Частина 6 — Ваш перший скрипт Playwright

# Частина 6
## Ваш перший скрипт Playwright

Відкриття браузера та навігація

---

## Слайд 26: Метод 1: Sync API (Простий)

```python
# first_script.py - Простий скрипт Playwright

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запустити браузер
    browser = p.chromium.launch(headless=False)

    # Створити нову сторінку
    page = browser.new_page()

    # Перейти за URL
    page.goto("https://playwright.dev")

    # Вивести заголовок сторінки
    print(f"Заголовок сторінки: {page.title()}")

    # Закрити браузер
    browser.close()
```

**Запуск:** `python first_script.py`

---

## Слайд 27: Розбір скрипта

```python
# 1. Імпорт Playwright
from playwright.sync_api import sync_playwright
```

```python
# 2. Створення екземпляра Playwright
with sync_playwright() as p:
    # 'p' - це об'єкт Playwright
    # 'with' забезпечує правильне очищення
```

```python
# 3. Запуск браузера
browser = p.chromium.launch(headless=False)
# headless=False: Бачити вікно браузера
# headless=True: Запуск у фоні (за замовчуванням)
```

```python
# 4. Створення сторінки (вкладки)
page = browser.new_page()
```

```python
# 5. Навігація
page.goto("https://playwright.dev")
```

---

## Слайд 28: Метод 2: Pytest тест (Рекомендований)

```python
# tests/test_first.py

import pytest
from playwright.sync_api import Page, expect


def test_playwright_homepage(page: Page):
    """Тест що домашня сторінка Playwright завантажується коректно."""

    # ARRANGE (Підготовка)
    url = "https://playwright.dev"

    # ACT (Дія)
    page.goto(url)

    # ASSERT (Перевірка)
    expect(page).to_have_title("Playwright")
    expect(page).to_have_url(url)

    print(f"Успішно перейшли до {url}")
```

**Запуск:** `pytest tests/test_first.py`

---

## Слайд 29: Магія фікстури `page`

**pytest-playwright** надає автоматичні фікстури:

```python
def test_example(page: Page):
    # 'page' надається автоматично!
    # Не потрібно запускати браузер чи створювати сторінку вручну
    page.goto("https://example.com")
```

**Що pytest-playwright робить за вас:**
- Запускає браузер перед тестом
- Створює свіжу сторінку для кожного тесту
- Робить скріншот при помилці
- Закриває браузер після тесту
- Обробляє очищення автоматично

**Результат:** Чистіший код тестів, менше шаблонного коду!

---

## Слайд 30: Запуск ваших тестів

```bash
# Базовий запуск (headless режим)
pytest

# Запуск у headed режимі (бачити браузер)
pytest --headed

# Запуск у конкретному браузері
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit

# Запуск у всіх браузерах
pytest --browser chromium --browser firefox --browser webkit

# Сповільнити виконання (корисно для перегляду)
pytest --headed --slowmo 1000

# Запуск конкретного тестового файлу
pytest tests/test_first.py

# Запуск конкретної тестової функції
pytest tests/test_first.py::test_playwright_homepage
```

---

## Слайд 31: Основні команди Playwright

```python
# Навігація
page.goto("https://example.com")
page.go_back()
page.go_forward()
page.reload()

# Отримання інформації
title = page.title()
url = page.url
content = page.content()

# Скріншоти
page.screenshot(path="screenshot.png")

# Очікування завантаження сторінки
page.wait_for_load_state("networkidle")
page.wait_for_load_state("domcontentloaded")

# Закриття
page.close()
```

---

## Слайд 32: Опції запуску браузера

```python
# Headed режим (бачити вікно браузера)
browser = p.chromium.launch(headless=False)

# Headless режим (без UI, швидше)
browser = p.chromium.launch(headless=True)

# Сповільнити операції (для налагодження)
browser = p.chromium.launch(
    headless=False,
    slow_mo=1000  # 1 секунда затримки між діями
)

# Власний розмір вікна
browser = p.chromium.launch(
    headless=False,
    args=['--window-size=1920,1080']
)

# Увімкнути devtools
browser = p.chromium.launch(
    headless=False,
    devtools=True
)
```

---

## Слайд 33: Опції створення сторінки

```python
# Базова сторінка
page = browser.new_page()

# Сторінка з власним viewport
page = browser.new_page(
    viewport={'width': 1920, 'height': 1080}
)

# Емуляція мобільного
page = browser.new_page(
    viewport={'width': 375, 'height': 667},
    user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
)

# Увімкнути запис відео
page = browser.new_page(
    record_video_dir="videos/"
)

# Встановити таймаут за замовчуванням
page.set_default_timeout(30000)  # 30 секунд
```

---

## Слайд 34: Повний робочий приклад

```python
# tests/test_google_search.py

from playwright.sync_api import Page, expect


def test_google_search(page: Page):
    """Тест функціональності пошуку Google."""

    # Перейти до Google
    page.goto("https://www.google.com")

    # Перевірити що сторінка завантажилась
    expect(page).to_have_title("Google")

    # Перевірити що поле пошуку видиме
    search_box = page.locator("textarea[name='q']")
    expect(search_box).to_be_visible()

    # Ввести пошуковий запит
    search_box.fill("Playwright Python")

    # Натиснути Enter
    search_box.press("Enter")

    # Дочекатися результатів
    page.wait_for_load_state("networkidle")

    # Перевірити що сторінка результатів завантажилась
    expect(page).to_have_url("**/search?**")

    print("Тест пошуку Google пройшов!")
```

---

## Слайд 35: Інструменти налагодження Playwright

**1. Headed режим**
```bash
pytest --headed
```
Дивіться як тести виконуються у реальному вікні браузера

**2. Slow Motion**
```bash
pytest --headed --slowmo 1000
```
Сповільнює операції щоб бачити що відбувається

**3. Playwright Inspector**
```python
# Додайте це у ваш код
page.pause()
```
Призупиняє виконання, відкриває інтерактивний відладчик

**4. Скріншоти**
```python
page.screenshot(path="debug.png")
```
Захоплює стан у будь-який момент

---

## Слайд 36: Вирішення поширених проблем

**Проблема:** "playwright: command not found"
**Рішення:** Активуйте віртуальне середовище
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**Проблема:** "No module named 'playwright'"
**Рішення:** Встановіть playwright
```bash
pip install playwright pytest-playwright
```

**Проблема:** "Executable doesn't exist"
**Рішення:** Встановіть бінарні файли браузерів
```bash
playwright install
```

**Проблема:** Тести падають з таймаутом
**Рішення:** Збільште таймаут або перевірте мережу
```python
page.set_default_timeout(60000)  # 60 секунд
```

---

## Слайд 37: Найкращі практики Playwright

- **Використовуйте фікстури pytest-playwright** — чистіший код
- **Використовуйте expect() assertions** — вбудоване автоочікування
- **Запускайте headless у CI/CD** — швидше виконання
- **Використовуйте значущі локатори** — data-testid, text, role
- **Один тест = одна річ** — тримайте тести сфокусованими
- **Використовуйте Page Object Model** — краща організація (ми це вивчимо!)
- **Увімкніть скріншоти/відео при помилці** — легше налагодження

---

## Слайд 38: Що далі?

**Лекція 14:** Playwright Локатори та Взаємодії
- Пошук елементів (CSS, text, role)
- Кліки, введення тексту, вибір
- Робота з формами

**Лекція 15:** Playwright Assertions та Waits
- expect() assertions
- Автоочікування
- Робота з динамічним контентом

**Лекція 16:** Page Object Model
- Організація тестового коду
- Багаторазові класи сторінок
- Найкращі практики

---

## Слайд 39: Практичне завдання

**До наступної лекції:**
1. Встановіть Playwright та всі браузери
2. Створіть структуру проекту
3. Запустіть приклади тестів успішно
4. Напишіть свій тест, який:
   - Переходить на ваш улюблений веб-сайт
   - Перевіряє заголовок сторінки
   - Робить скріншот
5. Поекспериментуйте з різними браузерами (chromium, firefox, webkit)
6. Спробуйте headed vs headless режим

**Перевірте папку exercises для детальних практичних завдань!**

---

## Слайд 40: Шпаргалка

```bash
# Встановлення
pip install playwright
pip install pytest-playwright
playwright install

# Запуск тестів
pytest
pytest --headed
pytest --browser firefox
```

```python
# Навігація
page.goto(url)
page.go_back()
page.reload()

# Інформація
page.title()
page.url
page.content()

# Скріншоти
page.screenshot(path="test.png")

# Налагодження
page.pause()
pytest --headed --slowmo 1000
```

---

## Слайд 41: Підсумок Лекції 13

- **Що таке Playwright** — сучасний фреймворк автоматизації браузера
- **Playwright vs Selenium** — порівняли функції та випадки використання
- **Встановлення** — налаштували Playwright та pytest-playwright
- **Браузерні драйвери** — Chromium, Firefox, WebKit
- **Структура проекту** — організовані проекти Playwright
- **Перший скрипт** — відкриття браузера та навігація

**Тепер ви можете писати базові скрипти автоматизації браузера з Playwright!**

---

## Слайд 42: Фінальний слайд

# Готові автоматизувати!

## До зустрічі на Лекції 14

Питання?
