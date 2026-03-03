# Лекція 33: Управління тестовими даними

**Курс автоматизації на Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 33
## Управління тестовими даними (Test Data Management)

Курс автоматизації на Python + Playwright

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Читати тестові дані з JSON-файлів
- Читати тестові дані з CSV-файлів
- Використовувати змінні середовища для секретів
- Генерувати динамічні дані за допомогою Faker
- Створювати повторно використовувані фікстури для даних

---

## Слайд 3: Навіщо керувати тестовими даними?

**❌ Захардкоджені дані:**

```python
page.locator("#user").fill("tomsmith")       # Захардкоджено!
page.locator("#pass").fill("SuperSecret!")  # В кожному тесті!
```

**✅ Зовнішні дані:**

```python
user = test_data["valid_user"]                # З файлу
page.locator("#user").fill(user["username"])
page.locator("#pass").fill(user["password"])
```

Коли дані зашиті прямо в тестах — це погана практика. Якщо пароль зміниться, потрібно буде правити десятки файлів. Якщо хтось побачить код — побачить і секрети. Тому тестові дані мають зберігатися окремо від тестової логіки. Це покращує підтримуваність, повторне використання та захист чутливих даних.

---

## Слайд 4: Частина 1 — JSON тестові дані

# Частина 1
## JSON тестові дані

Структуровані дані з файлів

---

## Слайд 5: JSON-файл з даними

```json
// test_data/login_data.json
{
  "valid_user": {
    "username": "tomsmith",
    "password": "SuperSecretPassword!"
  },
  "invalid_users": [
    {"username": "wrong", "password": "wrong"},
    {"username": "", "password": ""}
  ]
}
```

JSON — це найпоширеніший формат для зберігання тестових даних. Він підтримує вкладені структури, різні типи даних (рядки, числа, булеві значення, null) і добре читається як людиною, так і програмою. Створюємо окремий файл у директорії `test_data/` і зберігаємо там усі необхідні дані для тестів.

---

## Слайд 6: Завантаження JSON у Python

```python
import json

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

data = load_json("test_data/login_data.json")
user = data["valid_user"]
print(user["username"])  # tomsmith
```

Модуль `json` вбудований у Python — нічого додатково встановлювати не потрібно. Функція `json.load()` приймає файловий об'єкт і повертає Python-словник або список. Після завантаження працюємо з даними як зі звичайними Python-об'єктами — через ключі словника або індекси списку.

---

## Слайд 7: JSON + Parametrize

```python
data = load_json("test_data/login_data.json")

@pytest.mark.parametrize("user", data["invalid_users"])
def test_invalid_login(page, user):
    page.goto("/login")
    page.locator("#username").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("button").click()
    assert "/login" in page.url
```

Кожен елемент масиву = окремий тестовий випадок!

Ось де JSON по-справжньому розкривається. Ми завантажуємо дані один раз на рівні модуля, а потім передаємо масив `invalid_users` у `@pytest.mark.parametrize`. Pytest автоматично створить окремий тест для кожного словника в масиві. Також можна додати параметр `ids=` для зрозуміліших назв тестів у виводі.

---

## Слайд 8: Частина 2 — CSV тестові дані

# Частина 2
## CSV тестові дані

Табличні дані зі спредшитів

---

## Слайд 9: CSV-файл з даними

```
# test_data/login_data.csv
username,password,should_succeed
tomsmith,SuperSecretPassword!,true
wrong,wrong,false
tomsmith,bad_password,false
```

CSV легко редагувати в Excel або Google Sheets!

CSV — це простий табличний формат. Перший рядок — заголовки стовпців, кожен наступний рядок — набір даних. Цей формат ідеальний, коли потрібно, щоб нетехнічні спеціалісти (наприклад, QA-менеджери) могли редагувати тестові дані в Excel або Google Sheets.

---

## Слайд 10: Завантаження CSV у Python

```python
import csv

def load_csv(file_path):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

rows = load_csv("test_data/login_data.csv")
# [{"username": "tomsmith", "password": "...", ...}]
```

⚠️ Значення в CSV — це завжди **рядки**! Конвертуйте вручну: `"true" → True`

Модуль `csv` також вбудований у Python. `csv.DictReader` читає CSV і повертає список словників, де ключі — це заголовки стовпців. Це дуже зручно, бо далі працюємо так само, як із JSON. Головне пам'ятати: CSV не має типів даних — усі значення будуть рядками, тому `"true"` потрібно перетворювати в `True` вручну.

---

## Слайд 11: CSV vs JSON

| | CSV | JSON |
|---|---|---|
| **Редагування в Excel** | ✅ Легко | ❌ Складно |
| **Типи даних** | ❌ Тільки рядки | ✅ int, bool, null |
| **Вкладені дані** | ❌ Ні | ✅ Так |
| **Великі набори** | ✅ Ефективно | ❌ Громіздко |
| **Найкраще для** | Прості таблиці | Складні дані |

Яке правило вибору? Якщо дані плоскі й табличні — CSV. Якщо потрібна вкладена структура, різні типи або дані складні — JSON. На практиці в проектах часто використовують обидва формати для різних цілей.

---

## Слайд 12: Частина 3 — Змінні середовища

# Частина 3
## Змінні середовища

Захист чутливих даних

---

## Слайд 13: Навіщо змінні середовища?

**❌ НІКОЛИ не комітьте секрети:**

```python
# НЕ РОБІТЬ ТАК!
PASSWORD = "SuperSecretPassword!"  # В коді!
API_KEY = "sk-abc123..."           # В git!
```

**✅ Використовуйте змінні середовища:**

```python
import os
PASSWORD = os.environ.get("TEST_PASSWORD")
API_KEY = os.environ.get("API_KEY")
```

Це критично важливий момент. Паролі, API-ключі, URL-адреси до баз даних — все це чутлива інформація, яка НІКОЛИ не повинна потрапити в git-репозиторій. Якщо хтось випадково запушить пароль у публічний репозиторій — це серйозна проблема безпеки. Змінні середовища дозволяють зберігати секрети за межами коду.

---

## Слайд 14: .env файл + python-dotenv

```ini
# .env (додайте до .gitignore!)
BASE_URL=https://the-internet.herokuapp.com
TEST_USERNAME=tomsmith
TEST_PASSWORD=SuperSecretPassword!
HEADLESS=true
```

```python
# conftest.py
from dotenv import load_dotenv
load_dotenv()  # Завантажує .env у os.environ

BASE_URL = os.environ.get("BASE_URL")
```

```bash
pip install python-dotenv
```

Файл `.env` — це простий текстовий файл з парами ключ=значення. Бібліотека `python-dotenv` зчитує цей файл і завантажує змінні в `os.environ`. Головне правило: файл `.env` має бути в `.gitignore`! Натомість створіть `.env.example` з порожніми значеннями як шаблон для інших розробників.

---

## Слайд 15: Config Class (патерн конфігурації)

```python
class Config:
    """Усі налаштування в одному місці."""
    BASE_URL = os.environ.get("BASE_URL", "https://default.com")
    USERNAME = os.environ.get("TEST_USERNAME", "user")
    PASSWORD = os.environ.get("TEST_PASSWORD", "pass")
    HEADLESS = os.environ.get("HEADLESS", "true") == "true"

# Використання в тестах:
def test_login(page, config):
    page.goto(config.BASE_URL)
    page.locator("#user").fill(config.USERNAME)
```

Патерн Config class — це рекомендований підхід. Усі налаштування зібрані в одному класі з дефолтними значеннями. Другий аргумент `os.environ.get()` — це значення за замовчуванням, яке використовується, коли змінна середовища не задана. Зверніть увагу на конвертацію `HEADLESS`: оскільки змінні середовища завжди рядки, ми порівнюємо з `"true"` щоб отримати булеве значення.

---

## Слайд 16: Частина 4 — Бібліотека Faker

# Частина 4
## Бібліотека Faker

Динамічна генерація тестових даних

---

## Слайд 17: Що таке Faker?

```bash
pip install faker
```

```python
from faker import Faker

fake = Faker()
print(fake.name())        # John Smith
print(fake.email())       # john@example.com
print(fake.address())     # 123 Main St...
print(fake.phone_number()) # +1-555-0123
```

Генерує реалістичні дані кожного разу!

Faker — це потужна бібліотека для генерації випадкових, але реалістичних тестових даних. Вона може створювати імена, email-адреси, телефонні номери, адреси, текст та ще сотні інших типів даних. Кожного разу при виклику генеруються нові випадкові дані, що робить тести більш надійними — вони перевіряють поведінку системи з різними вхідними даними.

---

## Слайд 18: Faker: українська локаль

```python
from faker import Faker

fake_ua = Faker("uk_UA")

print(fake_ua.name())
# Олександр Петренко

print(fake_ua.address())
# вул. Хрещатик, 1, Київ

print(fake_ua.phone_number())
# +380 44 123 4567
```

Faker підтримує десятки локалей, включаючи українську `uk_UA`. Це особливо корисно, коли ви тестуєте інтерфейс з кириличними символами — перевіряєте, що форми правильно приймають українські імена, адреси, телефонні номери. Можна навіть створити `Faker` з кількома локалями одночасно: `Faker(["en_US", "uk_UA"])`.

---

## Слайд 19: Популярні методи Faker

| Метод | Приклад результату |
|-------|-------------------|
| `fake.name()` | John Smith |
| `fake.email()` | john@example.com |
| `fake.user_name()` | jsmith42 |
| `fake.password()` | xK9#mP2!qR |
| `fake.address()` | 123 Main St, NY |
| `fake.phone_number()` | +1-555-0123 |
| `fake.random_int(1, 100)` | 42 |
| `fake.sentence()` | The quick brown fox... |

Це лише мала частина можливостей Faker. Бібліотека має сотні методів для генерації різних типів даних: дати, кредитні картки, кольори, компанії, IP-адреси, URL та багато іншого. Повний перелік можна знайти в офіційній документації.

---

## Слайд 20: Відтворювані дані з seed

```python
from faker import Faker

# Встановити seed для відтворюваних даних
Faker.seed(12345)
fake = Faker()

print(fake.name())   # Завжди одне й те саме ім'я!
print(fake.email())  # Завжди той самий email!
```

Використовуйте seed у CI/CD для **стабільних** тестових даних між запусками.

Іноді потрібно, щоб "випадкові" дані були однаковими при кожному запуску. Наприклад, у CI/CD пайплайні хочеться, щоб тести були детерміністичними. Метод `Faker.seed()` встановлює початкове значення генератора випадкових чисел. Після цього послідовність згенерованих даних буде завжди однаковою. Це дуже корисно для дебагу — можна точно відтворити проблему.

---

## Слайд 21: Faker у тестах Playwright

```python
@pytest.fixture
def fake():
    return Faker()

def test_invalid_login(page, fake):
    """Випадкові дані завжди мають провалити логін."""
    page.goto("/login")
    page.locator("#username").fill(fake.user_name())
    page.locator("#password").fill(fake.password())
    page.locator("button").click()
    assert "/login" in page.url
```

Faker ідеально підходить для негативного тестування. Якщо ми заповнюємо форму входу випадковими логіном і паролем — система повинна відхилити спробу. Якщо ні — це баг. Кожен запуск тесту перевіряє з новими даними, що значно збільшує покриття тестування.

---

## Слайд 22: Частина 5 — Фікстури для даних

# Частина 5
## Фікстури для даних

Об'єднуємо все разом

---

## Слайд 23: Патерн фікстури для даних

```python
# conftest.py
import json, pytest

@pytest.fixture(scope="session")
def test_data():
    with open("test_data/users.json") as f:
        return json.load(f)

@pytest.fixture
def valid_user(test_data):
    return test_data["valid_user"]

@pytest.fixture
def logged_in_page(page, valid_user):
    page.goto("/login")
    page.locator("#user").fill(valid_user["username"])
    page.locator("#pass").fill(valid_user["password"])
    page.locator("button").click()
    return page
```

Ось як виглядає повноцінний підхід. Фікстура `test_data` завантажує JSON один раз на всю сесію тестування (завдяки `scope="session"`). Фікстура `valid_user` витягує конкретного користувача. А `logged_in_page` використовує ці дані для виконання входу і повертає вже авторизовану сторінку. Кожен наступний рівень будується на попередньому — це принцип композиції фікстур.

---

## Слайд 24: Фабрична фікстура

```python
@pytest.fixture
def user_factory():
    """Генерує дані користувача на вимогу."""
    fake = Faker()

    def create_user():
        return {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password(),
        }

    return create_user

def test_registration(page, user_factory):
    user = user_factory()  # Новий користувач при кожному виклику
    print(user["name"])
```

Фабрична фікстура (Factory Fixture) — це просунутий патерн. Замість того, щоб повертати одні й ті ж дані, фікстура повертає функцію, яка створює нові дані при кожному виклику. Це особливо корисно, коли тесту потрібно кілька різних користувачів, або коли кожен виклик має генерувати унікальні дані.

---

## Слайд 25: Рекомендована структура проекту

```
project/
├── .env                 # Секрети (в gitignore!)
├── .env.example         # Шаблон
├── .gitignore           # .env, screenshots/
├── pytest.ini
├── conftest.py          # Фікстури
├── test_data/
│   ├── users.json       # Дані користувачів
│   ├── pages.csv        # Дані сторінок
│   └── products.json
├── pages/               # Page Objects
├── utils/
│   └── data_loader.py   # Клас TestData
└── tests/
```

Це рекомендована структура проекту, яка об'єднує все, про що ми говорили. Тестові дані лежать в окремій директорії `test_data/`. Секрети — у `.env` (яка є в `.gitignore`). Утиліти для завантаження даних — в `utils/`. Фікстури — в `conftest.py`. Така структура масштабується і легко підтримується.

---

## Слайд 26: Підсумок

| Джерело | Найкраще для |
|---------|-------------|
| `JSON` | Складні, вкладені тестові дані |
| `CSV` | Прості табличні дані, редагування в Excel |
| `.env` | Секрети, URL, конфіг для різних середовищ |
| `Faker` | Динамічні, випадкові, реалістичні дані |
| `Fixtures` | Об'єднання джерел, повторне налаштування |

Підсумуємо. JSON — для складних структурованих даних. CSV — для простих таблиць, які зручно редагувати. Файл `.env` — виключно для секретів та конфігурації середовища. Faker — для динамічної генерації реалістичних даних. І нарешті, фікстури pytest — це клей, який з'єднує всі ці джерела та надає їх тестам у зручному вигляді.

---

## Слайд 27: Домашнє завдання

**Завдання:**

1. Створити JSON тестові дані:
   - Дані для логіну (валідні + невалідні)
   - Використати з `parametrize`

2. Створити .env файл:
   - BASE_URL, логін, пароль
   - Завантажити через `python-dotenv`

3. Використати Faker:
   - Згенерувати випадкові тестові дані
   - Створити фабричну фікстуру

---

## Слайд 28: Наступна лекція

**Лекція 34: Параметризоване тестування**

- @pytest.mark.parametrize поглиблено
- Data-driven тестові випадки
- Інтеграція з Excel/CSV
- Динамічна генерація тестів
- Найкращі практики

**Практика:** `pip install faker python-dotenv`

---

## Слайд 29: Фінальний слайд

# Чудово!
## Ви опанували управління тестовими даними!

JSON, CSV, .env, Faker, фікстури для даних
