# Рядки

Рядки (strings) — один з найважливіших типів даних у Python. У QA-автоматизації рядки зустрічаються всюди: URL-адреси, тестові дані, логи, повідомлення про помилки, відповіді API. Ця сторінка охоплює все, що потрібно знати про роботу з рядками.

## Створення рядків

Python підтримує кілька способів створення рядків.

```python
# Одинарні лапки
name = 'QA Engineer'

# Подвійні лапки
title = "Автоматизація тестування"

# Одинарні та подвійні — еквівалентні
print('Hello' == "Hello")  # True

# Лапки всередині рядка
message = "It's a test"          # подвійні зовні, одинарна всередині
html = '<div class="header">'    # одинарні зовні, подвійні всередині

# Потрійні лапки — багаторядковий рядок
description = """
Це багаторядковий рядок.
Він зберігає всі переноси рядків
та відступи.
"""

# Потрійні одинарні лапки теж працюють
sql_query = '''
    SELECT * FROM users
    WHERE status = 'active'
    ORDER BY created_at DESC
'''
```

::: tip Яку конвенцію обрати?
У Python обидва варіанти (одинарні та подвійні лапки) рівноцінні. Головне — дотримуватись одного стилю в проєкті. PEP 8 не диктує конкретний стиль, але більшість QA-проєктів використовують подвійні лапки.
:::

## Індексація та зрізи

Рядок — це послідовність символів. Кожен символ має індекс, починаючи з `0`.

```python
text = "Python"
#       P y t h o n
#       0 1 2 3 4 5
#      -6-5-4-3-2-1

# Індексація
print(text[0])    # P — перший символ
print(text[5])    # n — останній символ
print(text[-1])   # n — останній (від'ємний індекс)
print(text[-2])   # o — передостанній

# Зрізи (slicing): [start:stop:step]
print(text[0:3])   # Pyt — символи з 0 по 2 (stop не включається)
print(text[2:])    # thon — від індексу 2 до кінця
print(text[:3])    # Pyt — від початку до індексу 2
print(text[::2])   # Pto — кожен другий символ
print(text[::-1])  # nohtyP — реверс рядка

# Довжина рядка
print(len(text))   # 6
```

::: warning IndexError
Спроба звернутися до неіснуючого індексу викличе помилку:
```python
text = "Python"
print(text[10])  # IndexError: string index out of range
```
Але зрізи не викликають помилку — вони просто повертають те, що є:
```python
print(text[2:100])  # thon — без помилки
```
:::

::: info Приклад для QA: аналіз відповідей
```python
# Перевірка коду відповіді у тексті логу
log_line = "2024-01-15 10:30:45 INFO Response: 200 OK"

# Отримати час
timestamp = log_line[:19]  # "2024-01-15 10:30:45"

# Отримати статус код
status = log_line[-6:-3]   # "200"
```
:::

## Методи рядків

### Зміна регістру

```python
text = "Hello, QA World!"

print(text.upper())       # HELLO, QA WORLD!
print(text.lower())       # hello, qa world!
print(text.title())       # Hello, Qa World!
print(text.capitalize())  # Hello, qa world!
print(text.swapcase())    # hELLO, qa wORLD!
```

### Очищення пробілів — strip()

```python
raw_input = "   test@example.com   "

print(raw_input.strip())   # "test@example.com" — обидва боки
print(raw_input.lstrip())  # "test@example.com   " — тільки зліва
print(raw_input.rstrip())  # "   test@example.com" — тільки справа

# Видалення конкретних символів
url = "///api/users///"
print(url.strip("/"))  # "api/users"
```

::: tip Порада для QA
Завжди використовуйте `.strip()` при обробці введених даних у тестах — зайві пробіли часто спричиняють "фейли" тестів.
:::

### Розділення та з'єднання — split(), join()

```python
# split() — розбиває рядок на список
csv_line = "John,Doe,QA,Senior"
parts = csv_line.split(",")
print(parts)  # ['John', 'Doe', 'QA', 'Senior']

# Розбиття за пробілами (за замовчуванням)
sentence = "Python is awesome"
words = sentence.split()
print(words)  # ['Python', 'is', 'awesome']

# Обмеження кількості розбиттів
log = "ERROR: Connection failed: timeout"
parts = log.split(": ", 1)
print(parts)  # ['ERROR', 'Connection failed: timeout']

# join() — з'єднує список у рядок
words = ['Python', 'for', 'QA']
result = " ".join(words)
print(result)  # "Python for QA"

# Створення шляху
path = "/".join(["api", "v1", "users", "123"])
print(path)  # "api/v1/users/123"

# CSV рядок
csv = ",".join(["name", "email", "role"])
print(csv)  # "name,email,role"
```

### Заміна — replace()

```python
text = "Hello World"
print(text.replace("World", "QA"))  # "Hello QA"

# Заміна декількох входжень
url = "http://old-api.com/v1/users"
new_url = url.replace("old-api", "new-api")
print(new_url)  # "http://new-api.com/v1/users"

# Обмеження кількості замін
text = "a-b-c-d"
print(text.replace("-", " ", 2))  # "a b c-d"
```

### Пошук — find(), count()

```python
text = "Hello, World! Hello, Python!"

# find() — повертає індекс першого входження (-1 якщо не знайдено)
print(text.find("Hello"))    # 0
print(text.find("Python"))   # 21
print(text.find("Java"))     # -1

# rfind() — пошук з кінця
print(text.rfind("Hello"))   # 14

# index() — як find(), але викликає ValueError якщо не знайдено
# print(text.index("Java"))  # ValueError!

# count() — кількість входжень
print(text.count("Hello"))   # 2
print(text.count("l"))       # 4
```

### Перевірка початку та кінця — startswith(), endswith()

```python
filename = "test_report_2024.pdf"

print(filename.startswith("test"))   # True
print(filename.endswith(".pdf"))     # True
print(filename.endswith(".csv"))     # False

# Перевірка декількох варіантів (кортеж)
print(filename.endswith((".pdf", ".csv", ".xlsx")))  # True

url = "https://api.example.com/users"
print(url.startswith("https://"))  # True
print(url.startswith("http://"))   # False
```

::: info Приклад для QA: фільтрація файлів
```python
# Знайти всі скріншоти серед файлів
files = ["report.pdf", "screenshot_01.png", "data.csv", "error.jpg", "log.txt"]

images = [f for f in files if f.endswith((".png", ".jpg", ".jpeg"))]
print(images)  # ['screenshot_01.png', 'error.jpg']

# Знайти всі тестові файли
test_files = [f for f in files if f.startswith("test")]
```
:::

## Форматування рядків

### f-strings (рекомендовано)

```python
name = "QA Engineer"
experience = 3
salary = 45000.50

# Базове форматування
print(f"Я {name} з досвідом {experience} роки")

# Вирази всередині f-string
print(f"Досвід у місяцях: {experience * 12}")
print(f"Ім'я великими: {name.upper()}")

# Форматування чисел
print(f"Зарплата: ${salary:,.2f}")    # Зарплата: $45,000.50
print(f"Відсоток: {0.856:.1%}")       # Відсоток: 85.6%
print(f"ID: {42:05d}")                # ID: 00042

# Вирівнювання тексту
print(f"{'Тест':<20} — PASSED")   # ліворуч
print(f"{'Тест':>20} — PASSED")   # праворуч
print(f"{'Тест':^20} — PASSED")   # по центру
```

### Метод .format()

```python
# Позиційні аргументи
print("Я {} з досвідом {} роки".format("QA", 3))

# Іменовані аргументи
print("URL: {protocol}://{host}:{port}".format(
    protocol="https",
    host="api.example.com",
    port=8080
))

# Індекси
print("{0} vs {1}: {0} wins!".format("Python", "Java"))
# Python vs Java: Python wins!
```

::: info Приклад для QA: генерація тестових даних
```python
# Генерація тестових URL
base_url = "https://api.example.com"
endpoints = ["users", "orders", "products"]

for endpoint in endpoints:
    url = f"{base_url}/api/v1/{endpoint}"
    print(f"Testing: {url}")

# Генерація тестових email
for i in range(1, 4):
    email = f"test_user_{i:03d}@qa-team.com"
    print(email)
# test_user_001@qa-team.com
# test_user_002@qa-team.com
# test_user_003@qa-team.com
```
:::

## Екрановані символи

```python
# Основні escape-послідовності
print("Рядок 1\nРядок 2")       # \n — новий рядок
print("Колонка1\tКолонка2")     # \t — табуляція
print("Шлях: C:\\Users\\test")   # \\ — зворотний слеш
print("Він сказав: \"Привіт\"") # \" — подвійна лапка
print('It\'s a test')            # \' — одинарна лапка

# Raw-рядки — ігнорують escape-послідовності
path = r"C:\Users\test\new_folder"
print(path)  # C:\Users\test\new_folder

# Корисно для регулярних виразів
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # SSN pattern
```

::: tip Raw-рядки в QA
Використовуйте raw-рядки (`r"..."`) для Windows-шляхів та регулярних виразів — це позбавить від проблем з екрануванням.
:::

## Незмінність рядків (Immutability)

Рядки в Python — **незмінні** (immutable). Це означає, що після створення рядок не можна змінити.

```python
text = "Hello"

# Не можна змінити окремий символ
# text[0] = "h"  # TypeError: 'str' object does not support item assignment

# Потрібно створити новий рядок
text = "h" + text[1:]
print(text)  # "hello"

# Усі методи рядків повертають НОВИЙ рядок
original = "Hello World"
upper = original.upper()
print(original)  # "Hello World" — оригінал не змінився!
print(upper)     # "HELLO WORLD" — новий рядок
```

::: warning Часта помилка
```python
name = "  John  "
name.strip()     # Повертає "John", але name НЕ ЗМІНЮЄТЬСЯ!
print(name)      # "  John  " — все ще з пробілами

# Правильно — зберегти результат
name = name.strip()
print(name)      # "John"
```
:::

## Перевірка вмісту рядка

```python
# Перевірка типу символів
print("12345".isdigit())     # True — тільки цифри
print("12.34".isdigit())     # False — крапка це не цифра
print("Hello".isalpha())     # True — тільки букви
print("Hello1".isalpha())    # False — є цифра
print("Hello1".isalnum())    # True — букви та/або цифри
print("hello".islower())     # True — всі маленькі
print("HELLO".isupper())     # True — всі великі
print("   ".isspace())       # True — тільки пробіли
```

::: info Приклад для QA: валідація введених даних
```python
def validate_username(username):
    """Перевіряє, чи валідне ім'я користувача."""
    if not username:
        return False, "Ім'я не може бути порожнім"
    if not username.isalnum():
        return False, "Тільки букви та цифри дозволені"
    if len(username) < 3 or len(username) > 20:
        return False, "Довжина має бути від 3 до 20 символів"
    return True, "OK"

# Тестування
test_cases = ["admin", "user_1", "ab", "a" * 21, "", "validUser123"]
for tc in test_cases:
    is_valid, message = validate_username(tc)
    print(f"'{tc}' -> {is_valid}: {message}")
```
:::

## Приклади для QA-автоматизації

### Парсинг URL

```python
url = "https://api.example.com:8080/api/v1/users?status=active&page=2"

# Розбір URL вручну (для розуміння)
protocol = url.split("://")[0]                    # "https"
domain_and_path = url.split("://")[1]             # "api.example.com:8080/api/v1/users?..."
domain = domain_and_path.split("/")[0]            # "api.example.com:8080"
path = "/" + "/".join(domain_and_path.split("/")[1:]).split("?")[0]  # "/api/v1/users"

print(f"Протокол: {protocol}")
print(f"Домен: {domain}")
print(f"Шлях: {path}")

# Парсинг query параметрів
query_string = url.split("?")[1]              # "status=active&page=2"
params = dict(p.split("=") for p in query_string.split("&"))
print(params)  # {'status': 'active', 'page': '2'}
```

::: tip У реальних проєктах
Для парсингу URL у реальних проєктах використовуйте модуль `urllib.parse`:
```python
from urllib.parse import urlparse, parse_qs

url = "https://api.example.com/users?status=active&page=2"
parsed = urlparse(url)
params = parse_qs(parsed.query)
print(params)  # {'status': ['active'], 'page': ['2']}
```
:::

### Валідація email (спрощена)

```python
def validate_email_simple(email):
    """Спрощена перевірка формату email."""
    email = email.strip()

    # Базові перевірки
    if "@" not in email:
        return False, "Відсутній символ @"
    if email.count("@") > 1:
        return False, "Занадто багато символів @"

    local, domain = email.rsplit("@", 1)

    if not local:
        return False, "Порожня локальна частина"
    if not domain:
        return False, "Порожній домен"
    if "." not in domain:
        return False, "Домен без крапки"
    if domain.startswith(".") or domain.endswith("."):
        return False, "Некоректний домен"

    return True, "Валідний"

# Тестування
test_emails = [
    "user@example.com",
    "invalid-email",
    "@no-local.com",
    "user@",
    "user@@double.com",
    "user@.bad.com",
]

for email in test_emails:
    is_valid, msg = validate_email_simple(email)
    status = "PASS" if is_valid else "FAIL"
    print(f"[{status}] {email:<25} — {msg}")
```

### Обробка лог-файлів

```python
# Парсинг рядків логу
log_lines = [
    "2024-01-15 10:30:45 INFO  Login successful for user: admin",
    "2024-01-15 10:30:46 ERROR Connection timeout after 30s",
    "2024-01-15 10:30:47 WARN  Retry attempt 2/3 for /api/users",
    "2024-01-15 10:30:48 INFO  Response: 200 OK (150ms)",
    "2024-01-15 10:30:49 ERROR AssertionError: Expected 200, got 500",
]

# Фільтрація помилок
errors = [line for line in log_lines if " ERROR " in line]
print(f"Знайдено {len(errors)} помилок:")
for error in errors:
    print(f"  {error}")

# Витягування часових міток
timestamps = [line[:19] for line in log_lines]
print(f"\nЧасові мітки: {timestamps}")

# Пошук конкретного патерну
for line in log_lines:
    if "timeout" in line.lower():
        # Витягнути час очікування
        parts = line.split()
        for part in parts:
            if part.endswith("s") and part[:-1].isdigit():
                print(f"\nTimeout: {part}")
```

### Побудова тестових даних

```python
# Генерація тестових даних для API
def build_test_user(user_id, role="user"):
    """Створює тестові дані користувача."""
    return {
        "username": f"test_{role}_{user_id:04d}",
        "email": f"test_{role}_{user_id}@qa-automation.com",
        "password": f"Test_{role.capitalize()}_{user_id}!",
        "display_name": f"Test {role.title()} {user_id}",
    }

# Генерація набору тестових користувачів
for i in range(1, 4):
    user = build_test_user(i, "admin")
    print(f"Username: {user['username']}")
    print(f"Email:    {user['email']}")
    print(f"Password: {user['password']}")
    print("---")

# Побудова SQL-запитів для тестових даних
table = "users"
fields = ["name", "email", "status"]
values = ["'John Doe'", "'john@test.com'", "'active'"]

sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(values)});"
print(f"\n{sql}")
```

::: warning Безпека
Ніколи не будуйте SQL-запити через конкатенацію рядків у реальних проєктах — це вразливість SQL Injection. Використовуйте параметризовані запити.
:::

## Корисні прийоми

```python
# Перевірка, чи рядок порожній
text = ""
if not text:
    print("Рядок порожній")

# Множення рядків
separator = "-" * 40
print(separator)  # ----------------------------------------

# Перевірка входження (in)
if "error" in "Connection error occurred".lower():
    print("Знайдено помилку!")

# Видалення конкретних символів
phone = "+38 (050) 123-45-67"
digits_only = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "").replace("+", "")
print(digits_only)  # 380501234567

# Розбиття на рядки
multiline = "line1\nline2\nline3"
lines = multiline.splitlines()
print(lines)  # ['line1', 'line2', 'line3']

# Вирівнювання (padding)
for item in ["PASSED", "FAILED", "SKIPPED"]:
    print(f"| {item:^10} |")
# |  PASSED   |
# |  FAILED   |
# |  SKIPPED  |
```

## Корисні посилання

- [Документація Python: str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Документація Python: string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 498 — f-strings](https://peps.python.org/pep-0498/)
- [Форматування рядків — pyformat.info](https://pyformat.info/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/data-types">← Типи даних</a>
  <a href="/python_automation_courses/docs/python/collections">Колекції →</a>
</div>
