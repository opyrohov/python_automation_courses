# Регулярні вирази

Регулярні вирази (regex) — потужний інструмент для пошуку, валідації та обробки текстових даних. У QA-автоматизації регулярні вирази використовуються для валідації форм, парсингу логів, перевірки API-відповідей та багато іншого.

## Модуль `re`

Python має вбудований модуль `re` для роботи з регулярними виразами.

```python
import re

# Простий пошук
result = re.search(r"test", "This is a test string")
if result:
    print(result.group())  # test
```

::: tip Сирі рядки (raw strings)
Завжди використовуйте префікс `r` перед шаблоном регулярного виразу. Це запобігає подвійній інтерпретації зворотних слешів.
```python
# Правильно — сирий рядок
pattern = r"\d+"

# Неправильно — без r потрібно подвійний слеш
pattern = "\\d+"
```
:::

## Базові шаблони

### Літеральні символи

Літеральні символи збігаються самі з собою.

```python
import re

text = "QA Engineer працює з automation testing"

# Пошук конкретного слова
result = re.search(r"automation", text)
print(result.group())  # automation
```

### Метасимволи

| Метасимвол | Опис | Приклад |
|:---:|---|---|
| `.` | Будь-який символ (крім `\n`) | `a.c` → `abc`, `a1c` |
| `^` | Початок рядка | `^Hello` |
| `$` | Кінець рядка | `world$` |
| `*` | 0 або більше повторень | `ab*c` → `ac`, `abc`, `abbc` |
| `+` | 1 або більше повторень | `ab+c` → `abc`, `abbc` |
| `?` | 0 або 1 повторення | `colou?r` → `color`, `colour` |
| `\|` | Логічне АБО | `cat\|dog` |
| `()` | Групування | `(ab)+` → `ab`, `abab` |
| `[]` | Набір символів | `[aeiou]` — голосні |
| `{}` | Кількість повторень | `a{2,4}` → `aa`, `aaa`, `aaaa` |
| `\` | Екранування | `\.` — буквальна крапка |

```python
import re

# Метасимвол . — будь-який символ
print(re.findall(r"t.st", "test tast tost t1st"))  # ['test', 'tast', 'tost', 't1st']

# ^ і $ — початок і кінець рядка
print(re.search(r"^Error", "Error: file not found"))   # Match
print(re.search(r"^Error", "No Error here"))            # None

# | — логічне АБО
print(re.findall(r"pass|fail", "test pass, test fail"))  # ['pass', 'fail']
```

## Класи символів

### Вбудовані класи

| Клас | Опис | Еквівалент |
|:---:|---|---|
| `\d` | Цифра | `[0-9]` |
| `\D` | Не цифра | `[^0-9]` |
| `\w` | Буква, цифра або `_` | `[a-zA-Z0-9_]` |
| `\W` | Не буква, не цифра, не `_` | `[^a-zA-Z0-9_]` |
| `\s` | Пробільний символ | `[ \t\n\r\f\v]` |
| `\S` | Не пробільний символ | `[^ \t\n\r\f\v]` |
| `\b` | Межа слова | — |
| `\B` | Не межа слова | — |

```python
import re

text = "Order #12345 created on 2024-01-15 at 14:30"

# \d — цифри
print(re.findall(r"\d+", text))  # ['12345', '2024', '01', '15', '14', '30']

# \w — слова та числа
print(re.findall(r"\w+", text))  # ['Order', '12345', 'created', 'on', '2024', '01', '15', 'at', '14', '30']

# \s — пробільні символи
parts = re.split(r"\s+", "test   data   here")
print(parts)  # ['test', 'data', 'here']

# \b — межа слова
text = "testing test tested"
print(re.findall(r"\btest\b", text))  # ['test'] — тільки точне слово
```

### Власні класи символів

```python
import re

# [abc] — один з символів a, b або c
print(re.findall(r"[aeiou]", "hello world"))  # ['e', 'o', 'o']

# [a-z] — діапазон
print(re.findall(r"[a-zA-Z]+", "test123data"))  # ['test', 'data']

# [^abc] — будь-який символ КРІМ a, b, c
print(re.findall(r"[^0-9]+", "abc123def456"))  # ['abc', 'def']
```

## Функції модуля `re`

### `re.search()` — пошук першого збігу

```python
import re

text = "Error 404: Page not found"

match = re.search(r"\d+", text)
if match:
    print(match.group())   # 404
    print(match.start())   # 6
    print(match.end())     # 9
    print(match.span())    # (6, 9)
```

### `re.match()` — пошук на початку рядка

```python
import re

# match() перевіряє тільки початок рядка
print(re.match(r"\d+", "123abc"))   # Match — починається з цифр
print(re.match(r"\d+", "abc123"))   # None — не починається з цифр
```

::: warning search() vs match()
`re.match()` шукає збіг тільки на **початку** рядка. Для пошуку в будь-якому місці використовуйте `re.search()`.
```python
text = "Status: 200 OK"
re.match(r"\d+", text)    # None — рядок починається з "Status"
re.search(r"\d+", text)   # Match — знаходить "200"
```
:::

### `re.findall()` — знайти всі збіги

```python
import re

text = "Prices: $10.99, $25.50, $7.00"

# Знайти всі ціни
prices = re.findall(r"\$[\d.]+", text)
print(prices)  # ['$10.99', '$25.50', '$7.00']

# З групами — повертає вміст груп
prices = re.findall(r"\$([\d.]+)", text)
print(prices)  # ['10.99', '25.50', '7.00']
```

### `re.finditer()` — ітератор збігів

```python
import re

text = "Error at line 10, Error at line 25, Error at line 42"

for match in re.finditer(r"line (\d+)", text):
    print(f"Знайдено на позиції {match.start()}: рядок {match.group(1)}")
# Знайдено на позиції 9: рядок 10
# Знайдено на позиції 25: рядок 25
# Знайдено на позиції 41: рядок 42
```

### `re.sub()` — заміна

```python
import re

# Проста заміна
text = "Phone: 123-456-7890"
cleaned = re.sub(r"-", "", text)
print(cleaned)  # Phone: 1234567890

# Заміна з функцією
def censor_email(match):
    email = match.group()
    name, domain = email.split("@")
    return f"{name[0]}***@{domain}"

text = "Contacts: john@example.com, admin@test.com"
result = re.sub(r"[\w.]+@[\w.]+", censor_email, text)
print(result)  # Contacts: j***@example.com, a***@test.com
```

### `re.split()` — розбиття рядка

```python
import re

# Розбити за кількома роздільниками
text = "apple;banana,cherry orange|grape"
fruits = re.split(r"[;,\s|]+", text)
print(fruits)  # ['apple', 'banana', 'cherry', 'orange', 'grape']

# Обмежити кількість розбиттів
text = "one:two:three:four:five"
print(re.split(r":", text, maxsplit=2))  # ['one', 'two', 'three:four:five']
```

### `re.compile()` — компіляція шаблону

```python
import re

# Компіляція для багаторазового використання
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")

texts = [
    "Contact: user@example.com",
    "No email here",
    "Send to admin@test.org please",
]

for text in texts:
    match = email_pattern.search(text)
    if match:
        print(f"Знайдено: {match.group()}")
```

::: tip Коли використовувати compile()?
Використовуйте `re.compile()`, коли один шаблон використовується багато разів (наприклад, у циклі). Це покращує продуктивність, оскільки шаблон компілюється лише один раз.
:::

## Групи та захоплення

### Прості групи `()`

```python
import re

text = "2024-01-15"

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    print(match.group())    # 2024-01-15 — весь збіг
    print(match.group(1))   # 2024 — перша група
    print(match.group(2))   # 01 — друга група
    print(match.group(3))   # 15 — третя група
    print(match.groups())   # ('2024', '01', '15')
```

### Іменовані групи `(?P<name>...)`

```python
import re

text = "User: John Doe, Age: 30, Email: john@example.com"

pattern = r"User: (?P<name>[\w ]+), Age: (?P<age>\d+), Email: (?P<email>[\w.]+@[\w.]+)"
match = re.search(pattern, text)

if match:
    print(match.group("name"))    # John Doe
    print(match.group("age"))     # 30
    print(match.group("email"))   # john@example.com
    print(match.groupdict())      # {'name': 'John Doe', 'age': '30', 'email': 'john@example.com'}
```

### Групи без захоплення `(?:...)`

```python
import re

# Група без захоплення — для групування без збереження
text = "http://example.com https://example.org"

# (?:...) — не потрапить у results
urls = re.findall(r"(?:https?://)(\S+)", text)
print(urls)  # ['example.com', 'example.org']
```

## Квантифікатори

| Квантифікатор | Опис |
|:---:|---|
| `*` | 0 або більше (жадібний) |
| `+` | 1 або більше (жадібний) |
| `?` | 0 або 1 |
| `{n}` | Рівно n разів |
| `{n,}` | n або більше разів |
| `{n,m}` | Від n до m разів |
| `*?` | 0 або більше (лінивий) |
| `+?` | 1 або більше (лінивий) |

```python
import re

# Жадібний vs лінивий
html = "<b>bold</b> and <i>italic</i>"

# Жадібний — захоплює максимум
print(re.findall(r"<.*>", html))    # ['<b>bold</b> and <i>italic</i>']

# Лінивий — захоплює мінімум
print(re.findall(r"<.*?>", html))   # ['<b>', '</b>', '<i>', '</i>']
```

::: warning Жадібний vs Лінивий
За замовчуванням квантифікатори `*`, `+`, `?` є **жадібними** — вони захоплюють максимально можливу кількість символів. Додайте `?` після квантифікатора, щоб зробити його **лінивим**.
:::

```python
import re

# {n} — рівно n разів
print(re.findall(r"\d{3}", "12 123 1234 12345"))  # ['123', '123', '123']

# {n,m} — від n до m
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))  # ['12', '123', '1234', '1234']
```

## Прапорці (Flags)

### `re.IGNORECASE` (re.I)

```python
import re

text = "Error: CONNECTION REFUSED, error: timeout, ERROR: denied"

# Без прапорця — чутливий до регістру
print(re.findall(r"error", text))               # ['error']

# З re.IGNORECASE — нечутливий до регістру
print(re.findall(r"error", text, re.IGNORECASE)) # ['Error', 'error', 'ERROR']
```

### `re.MULTILINE` (re.M)

```python
import re

log = """ERROR: Connection failed
INFO: Retry attempt 1
ERROR: Timeout exceeded
INFO: Retry attempt 2"""

# Без MULTILINE — ^ відповідає тільки початку всього тексту
print(re.findall(r"^ERROR.*", log))               # ['ERROR: Connection failed']

# З MULTILINE — ^ відповідає початку кожного рядка
print(re.findall(r"^ERROR.*", log, re.MULTILINE))  # ['ERROR: Connection failed', 'ERROR: Timeout exceeded']
```

### `re.DOTALL` (re.S)

```python
import re

html = """<div>
  <p>Hello World</p>
</div>"""

# Без DOTALL — . не збігається з \n
print(re.search(r"<div>.*</div>", html))             # None

# З DOTALL — . збігається з \n
print(re.search(r"<div>.*</div>", html, re.DOTALL))  # Match
```

### Комбінування прапорців

```python
import re

text = """name: John
Name: Jane
NAME: Admin"""

# Комбінування через |
matches = re.findall(r"^name: \w+", text, re.IGNORECASE | re.MULTILINE)
print(matches)  # ['name: John', 'Name: Jane', 'NAME: Admin']
```

## Поширені шаблони

### Email

```python
import re

email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

emails = [
    "user@example.com",       # Valid
    "admin+tag@test.org",     # Valid
    "invalid@",               # Invalid
    "no-at-sign.com",         # Invalid
    "first.last@company.co",  # Valid
]

for email in emails:
    if email_pattern.fullmatch(email):
        print(f"  Valid: {email}")
    else:
        print(f"  Invalid: {email}")
```

### URL

```python
import re

url_pattern = re.compile(
    r"https?://"
    r"(?:[\w-]+\.)+[\w-]+"
    r"(?:/[\w./?%&=~#-]*)?"
)

text = "Visit https://example.com/page?id=1 or http://test.org"
urls = url_pattern.findall(text)
print(urls)  # ['https://example.com/page?id=1', 'http://test.org']
```

### Номер телефону

```python
import re

phone_pattern = re.compile(
    r"(?:\+?\d{1,3}[-.\s]?)?"   # Код країни
    r"(?:\(?\d{2,3}\)?[-.\s]?)" # Код міста
    r"\d{3}[-.\s]?\d{2}[-.\s]?\d{2}"
)

phones = [
    "+380-67-123-45-67",
    "(067) 123 45 67",
    "+38(067)1234567",
    "067-123-45-67",
]

for phone in phones:
    match = phone_pattern.search(phone)
    if match:
        print(f"Знайдено: {match.group()}")
```

### IP-адреса

```python
import re

ip_pattern = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}"
    r"(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
)

text = "Server 192.168.1.1 responded, but 10.0.0.255 is unreachable. Invalid: 999.999.999.999"
ips = ip_pattern.findall(text)
print(ips)  # ['192.168.1.1', '10.0.0.255']
```

## Приклади для QA

### Валідація даних форми

```python
import re

def validate_registration_form(data: dict) -> dict:
    """Валідація даних реєстраційної форми."""
    errors = {}

    # Валідація email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data.get("email", "")):
        errors["email"] = "Невалідний формат email"

    # Валідація пароля: мінімум 8 символів, великі/малі букви, цифри
    password = data.get("password", "")
    if len(password) < 8:
        errors["password"] = "Пароль повинен містити мінімум 8 символів"
    elif not re.search(r"[A-Z]", password):
        errors["password"] = "Пароль повинен містити великі літери"
    elif not re.search(r"[a-z]", password):
        errors["password"] = "Пароль повинен містити малі літери"
    elif not re.search(r"\d", password):
        errors["password"] = "Пароль повинен містити цифри"

    # Валідація телефону
    phone = data.get("phone", "")
    if not re.match(r"^\+?\d{10,15}$", re.sub(r"[-.\s()\u2013]", "", phone)):
        errors["phone"] = "Невалідний формат телефону"

    return errors

# Тест
form_data = {
    "email": "user@example.com",
    "password": "SecurePass123",
    "phone": "+380-67-123-45-67",
}

errors = validate_registration_form(form_data)
if not errors:
    print("Форма валідна!")
else:
    print(f"Помилки: {errors}")
```

### Парсинг лог-файлів

```python
import re
from collections import Counter

log_text = """
2024-01-15 10:23:45 [ERROR] Connection timeout to database server db-01
2024-01-15 10:23:46 [INFO] Retrying connection (attempt 1/3)
2024-01-15 10:23:50 [ERROR] Authentication failed for user admin
2024-01-15 10:24:01 [WARNING] High memory usage: 85%
2024-01-15 10:24:15 [INFO] Connection established to db-02
2024-01-15 10:24:20 [ERROR] Query timeout after 30s: SELECT * FROM users
"""

# Шаблон для парсингу рядків логу
log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"\[(?P<level>\w+)\]\s+"
    r"(?P<message>.+)"
)

# Парсинг кожного рядка
entries = []
for match in log_pattern.finditer(log_text):
    entries.append(match.groupdict())

# Підрахунок за рівнем логування
levels = Counter(entry["level"] for entry in entries)
print(f"Рівні логування: {dict(levels)}")
# Рівні логування: {'ERROR': 3, 'INFO': 2, 'WARNING': 1}

# Фільтрація тільки помилок
errors = [e for e in entries if e["level"] == "ERROR"]
for error in errors:
    print(f"[{error['time']}] {error['message']}")
```

### Витягування даних з API-відповідей

```python
import re

# Парсинг HTML-відповіді для витягування даних
html_response = """
<table id="users">
    <tr><td>John Doe</td><td>john@example.com</td><td>Admin</td></tr>
    <tr><td>Jane Smith</td><td>jane@test.org</td><td>User</td></tr>
    <tr><td>Bob Wilson</td><td>bob@company.com</td><td>Moderator</td></tr>
</table>
"""

# Витягнення рядків таблиці
row_pattern = re.compile(r"<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td></tr>")
users = row_pattern.findall(html_response)

for name, email, role in users:
    print(f"Name: {name}, Email: {email}, Role: {role}")
# Name: John Doe, Email: john@example.com, Role: Admin
# Name: Jane Smith, Email: jane@test.org, Role: User
# Name: Bob Wilson, Email: bob@company.com, Role: Moderator
```

::: info Приклад для QA: перевірка відповіді API
```python
import re
import json

def validate_api_response(response_text: str) -> dict:
    """Валідація структури JSON-відповіді API."""
    results = {"valid": True, "errors": []}

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        results["valid"] = False
        results["errors"].append("Невалідний JSON")
        return results

    # Перевірка формату ID (UUID v4)
    uuid_pattern = re.compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        re.IGNORECASE,
    )

    if "id" in data and not uuid_pattern.match(str(data["id"])):
        results["valid"] = False
        results["errors"].append(f"Невалідний UUID: {data['id']}")

    # Перевірка формату дати ISO 8601
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
    for field in ["created_at", "updated_at"]:
        if field in data and not date_pattern.match(str(data[field])):
            results["valid"] = False
            results["errors"].append(f"Невалідний формат дати в {field}")

    return results
```
:::

### Валідація тестових даних у Pytest

```python
import re
import pytest

class TestDataValidation:
    """Тести валідації даних за допомогою регулярних виразів."""

    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("admin+tag@test.org", True),
        ("first.last@company.co.uk", True),
        ("invalid@", False),
        ("@example.com", False),
        ("no-at-sign", False),
        ("spaces in@email.com", False),
    ])
    def test_email_validation(self, email, expected):
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        assert bool(pattern.match(email)) == expected, f"Email '{email}' validation failed"

    @pytest.mark.parametrize("password,is_strong", [
        ("SecurePass1", True),
        ("weakpass", False),      # Немає великих літер і цифр
        ("ALLCAPS123", False),    # Немає малих літер
        ("Short1A", False),       # Менше 8 символів
        ("GoodPassword99", True),
    ])
    def test_password_strength(self, password, is_strong):
        checks = [
            len(password) >= 8,
            bool(re.search(r"[A-Z]", password)),
            bool(re.search(r"[a-z]", password)),
            bool(re.search(r"\d", password)),
        ]
        assert all(checks) == is_strong
```

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/error-handling">← Обробка помилок</a>
  <a href="/python_automation_courses/docs/python/api-requests">Робота з API →</a>
</div>
