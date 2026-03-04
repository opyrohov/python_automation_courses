# Цикли в Python

Цикли дозволяють виконувати блок коду багаторазово — це одна з найважливіших конструкцій у програмуванні та QA-автоматизації. Ця сторінка охоплює всі типи циклів, корисні функції та практичні приклади для тестувальників.

## Цикл for

Цикл `for` ітерує по елементах будь-якого ітерабельного об'єкта — списку, рядку, словнику, діапазону тощо.

### Ітерація по списку

```python
# Перебір списку браузерів для тестування
browsers = ["chrome", "firefox", "safari", "edge"]

for browser in browsers:
    print(f"Запуск тестів у {browser}")
```

### Функція range()

```python
# range(stop) — від 0 до stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) — від start до stop-1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) — з кроком
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Зворотний відлік
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

::: info Приклад для QA: генерація тестових даних
```python
# Створення тестових користувачів
test_users = []
for i in range(1, 6):
    user = {
        "username": f"test_user_{i}",
        "email": f"user{i}@test.com",
        "password": f"Pass{i}!secure"
    }
    test_users.append(user)
    print(f"Створено користувача: {user['username']}")
```
:::

### Ітерація по рядку

```python
# Кожен символ — окрема ітерація
url = "https"
for char in url:
    print(char)  # h, t, t, p, s

# Підрахунок символів
text = "Hello, World!"
count = 0
for char in text:
    if char.isupper():
        count += 1
print(f"Великих літер: {count}")  # 2
```

### Ітерація по словнику

```python
# Ітерація по ключах (за замовчуванням)
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
    "Accept": "text/html"
}

for key in headers:
    print(key)

# Ітерація по значеннях
for value in headers.values():
    print(value)

# Ітерація по парах ключ-значення
for key, value in headers.items():
    print(f"{key}: {value}")
```

::: info Приклад для QA: валідація заголовків відповіді
```python
response_headers = {
    "Content-Type": "application/json",
    "X-Request-Id": "abc-123",
    "Cache-Control": "no-cache"
}

required_headers = ["Content-Type", "X-Request-Id"]

for header in required_headers:
    assert header in response_headers, f"Відсутній заголовок: {header}"
    print(f"✓ {header}: {response_headers[header]}")
```
:::

## Цикл while

Цикл `while` виконується, поки умова залишається істинною (`True`).

```python
# Базовий while
count = 0
while count < 5:
    print(f"Ітерація {count}")
    count += 1  # Не забудьте інкремент!
```

::: warning Нескінченний цикл
Завжди переконайтеся, що умова циклу `while` рано чи пізно стане `False`. Інакше отримаєте нескінченний цикл.
```python
# НЕБЕЗПЕЧНО — нескінченний цикл!
# while True:
#     print("Це ніколи не зупиниться")

# БЕЗПЕЧНО — з умовою виходу
attempts = 0
max_attempts = 10
while attempts < max_attempts:
    attempts += 1
    # виконуємо дії
```
:::

::: info Приклад для QA: retry-механізм для нестабільних тестів
```python
import time

def wait_for_element(locator, timeout=10):
    """Чекає на появу елемента з повторними спробами."""
    elapsed = 0
    interval = 0.5

    while elapsed < timeout:
        element = find_element(locator)  # умовна функція
        if element is not None:
            print(f"Елемент знайдено за {elapsed:.1f}с")
            return element
        time.sleep(interval)
        elapsed += interval

    raise TimeoutError(f"Елемент '{locator}' не знайдено за {timeout}с")
```
:::

::: info Приклад для QA: очікування відповіді API
```python
import time

def poll_task_status(task_id, max_wait=60):
    """Опитує API до завершення задачі."""
    start_time = time.time()

    while time.time() - start_time < max_wait:
        response = get_task_status(task_id)  # умовна функція
        status = response.get("status")

        if status == "completed":
            print(f"Задача {task_id} завершена!")
            return response
        elif status == "failed":
            raise Exception(f"Задача {task_id} провалилась: {response.get('error')}")

        print(f"Статус: {status}, чекаємо...")
        time.sleep(2)

    raise TimeoutError(f"Задача {task_id} не завершилась за {max_wait}с")
```
:::

## break, continue, else

### break — вихід з циклу

```python
# Зупинити цикл при першому знаходженні
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"Перше парне число: {num}")
        break
# Перше парне число: 8
```

### continue — пропуск ітерації

```python
# Пропустити непотрібні елементи
test_results = ["PASSED", "FAILED", "SKIPPED", "PASSED", "FAILED"]

for result in test_results:
    if result == "SKIPPED":
        continue  # пропускаємо пропущені тести
    print(f"Аналізуємо: {result}")
```

### else в циклах

Блок `else` виконується, якщо цикл завершився **без** `break`.

```python
# else виконається, бо break не спрацював
numbers = [1, 3, 5, 7]

for num in numbers:
    if num % 2 == 0:
        print(f"Знайдено парне: {num}")
        break
else:
    print("Парних чисел не знайдено")
# Парних чисел не знайдено
```

::: info Приклад для QA: пошук критичного бага
```python
test_results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_checkout", "status": "passed"},
    {"name": "test_payment", "status": "passed"},
]

for test in test_results:
    if test["status"] == "failed":
        print(f"КРИТИЧНО: {test['name']} впав!")
        break
else:
    print("Всі тести пройшли успішно!")
# Всі тести пройшли успішно!
```
:::

::: tip Коли використовувати break/continue?
- `break` — коли знайшли потрібне значення і далі шукати немає сенсу
- `continue` — коли потрібно пропустити певні елементи, але продовжити цикл
- `else` — коли потрібно виконати код тільки якщо цикл завершився нормально (без `break`)
:::

## enumerate() — індекс + елемент

Функція `enumerate()` повертає пари (індекс, елемент) під час ітерації.

```python
# Без enumerate — потрібна додаткова змінна
browsers = ["chrome", "firefox", "safari"]
index = 0
for browser in browsers:
    print(f"{index}: {browser}")
    index += 1

# З enumerate — чисто та зручно
for index, browser in enumerate(browsers):
    print(f"{index}: {browser}")
# 0: chrome
# 1: firefox
# 2: safari

# Початок індексу з 1
for num, browser in enumerate(browsers, start=1):
    print(f"Браузер #{num}: {browser}")
# Браузер #1: chrome
# Браузер #2: firefox
# Браузер #3: safari
```

::: info Приклад для QA: нумерація тестових кроків
```python
test_steps = [
    "Відкрити сторінку логіну",
    "Ввести email",
    "Ввести пароль",
    "Натиснути кнопку 'Увійти'",
    "Перевірити URL dashboard"
]

print("=== Тестовий сценарій: Логін ===")
for step_num, step in enumerate(test_steps, start=1):
    print(f"Крок {step_num}: {step}")
```
:::

## zip() — паралельна ітерація

Функція `zip()` об'єднує кілька ітерабельних об'єктів у пари.

```python
# Об'єднання двох списків
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score} балів")
# Alice: 95 балів
# Bob: 87 балів
# Charlie: 92 балів

# Три списки одночасно
cities = ["Київ", "Львів", "Одеса"]
temperatures = [25, 22, 28]
conditions = ["сонячно", "хмарно", "дощ"]

for city, temp, cond in zip(cities, temperatures, conditions):
    print(f"{city}: {temp}°C, {cond}")
```

::: warning zip() зупиняється на найкоротшому
Якщо списки різної довжини, `zip()` зупиниться на найкоротшому.
```python
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

result = list(zip(a, b))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')] — 4 і 5 втрачені!

# Використовуйте itertools.zip_longest для збереження всіх
from itertools import zip_longest
result = list(zip_longest(a, b, fillvalue=None))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]
```
:::

::: info Приклад для QA: порівняння очікуваних і фактичних результатів
```python
expected = [200, 201, 204, 404]
actual = [200, 201, 500, 404]
endpoints = ["/users", "/users/new", "/users/1", "/unknown"]

for endpoint, exp, act in zip(endpoints, expected, actual):
    status = "PASS" if exp == act else "FAIL"
    print(f"[{status}] {endpoint}: очікувано {exp}, отримано {act}")
# [PASS] /users: очікувано 200, отримано 200
# [PASS] /users/new: очікувано 201, отримано 201
# [FAIL] /users/1: очікувано 204, отримано 500
# [PASS] /unknown: очікувано 404, отримано 404
```
:::

## List Comprehensions

List comprehension — компактний спосіб створення списків у одному рядку.

```python
# Звичайний цикл
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension — те саме, але в один рядок
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# З умовою (фільтрація)
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# З умовою if/else (трансформація)
labels = ["парне" if x % 2 == 0 else "непарне" for x in range(5)]
print(labels)  # ['парне', 'непарне', 'парне', 'непарне', 'парне']
```

::: info Приклад для QA: обробка тестових даних
```python
# Фільтрація провалених тестів
all_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

failed_tests = [t["name"] for t in all_results if t["status"] == "failed"]
print(failed_tests)  # ['test_signup', 'test_profile']

# Витяг тривалості всіх тестів
durations = [t["duration"] for t in all_results]
print(f"Середня тривалість: {sum(durations) / len(durations):.2f}с")

# Генерація URL-ів для тестування
base_url = "https://example.com/api"
endpoints = ["/users", "/products", "/orders"]
urls = [f"{base_url}{ep}" for ep in endpoints]
print(urls)
# ['https://example.com/api/users', 'https://example.com/api/products', 'https://example.com/api/orders']
```
:::

::: tip Коли використовувати list comprehension?
- **Використовуйте** для простих трансформацій та фільтрацій
- **Не використовуйте** якщо логіка складна — краще звичайний цикл для читабельності
- Якщо comprehension не вміщається в один рядок (~80 символів), краще використати цикл
:::

## Dict Comprehensions

Аналогічно до list comprehensions, але створює словники.

```python
# Створення словника з двох списків
keys = ["name", "age", "role"]
values = ["Alice", 30, "QA"]
user = {k: v for k, v in zip(keys, values)}
print(user)  # {'name': 'Alice', 'age': 30, 'role': 'QA'}

# Трансформація словника
prices = {"apple": 25, "banana": 15, "cherry": 40}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)  # {'apple': 22.5, 'banana': 13.5, 'cherry': 36.0}

# Фільтрація словника
expensive = {item: price for item, price in prices.items() if price > 20}
print(expensive)  # {'apple': 25, 'cherry': 40}
```

::: info Приклад для QA: обробка відповідей API
```python
# Перетворення списку об'єктів у словник для швидкого пошуку
users_list = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "user"},
]

users_by_id = {user["id"]: user for user in users_list}
print(users_by_id[2])  # {'id': 2, 'name': 'Bob', 'role': 'user'}

# Підрахунок статусів відповідей
status_codes = [200, 200, 404, 200, 500, 404, 200]
status_counts = {code: status_codes.count(code) for code in set(status_codes)}
print(status_counts)  # {200: 4, 404: 2, 500: 1}
```
:::

## Set Comprehensions

```python
# Унікальні значення з трансформацією
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Унікальні домени з email-ів
emails = ["user@gmail.com", "admin@test.com", "qa@gmail.com", "dev@test.com"]
domains = {email.split("@")[1] for email in emails}
print(domains)  # {'gmail.com', 'test.com'}
```

## Вкладені цикли

Вкладені цикли корисні для роботи з матрицями, комбінаціями та складними структурами.

```python
# Таблиця множення
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  ")
    print()  # новий рядок

# Вкладений list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

::: info Приклад для QA: крос-браузерне тестування
```python
# Генерація тестових комбінацій
browsers = ["chrome", "firefox", "safari"]
resolutions = ["1920x1080", "1366x768", "375x667"]
os_list = ["Windows", "macOS"]

test_matrix = []
for browser in browsers:
    for resolution in resolutions:
        for os_name in os_list:
            test_matrix.append({
                "browser": browser,
                "resolution": resolution,
                "os": os_name
            })

print(f"Загалом тестових комбінацій: {len(test_matrix)}")
# Загалом тестових комбінацій: 18

# Те саме через list comprehension
test_matrix = [
    {"browser": b, "resolution": r, "os": o}
    for b in browsers
    for r in resolutions
    for o in os_list
]
```
:::

::: info Приклад для QA: перевірка всіх полів у відповіді API
```python
# Валідація структури вкладених даних
api_response = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@test.com"},
        {"id": 2, "name": "Bob", "email": "bob@test.com"},
        {"id": 3, "name": "Charlie", "email": None},  # проблема!
    ]
}

required_fields = ["id", "name", "email"]

for user in api_response["users"]:
    for field in required_fields:
        assert field in user, f"Поле '{field}' відсутнє у user {user.get('id')}"
        if user[field] is None:
            print(f"УВАГА: поле '{field}' = None у user {user['id']}")
```
:::

::: warning Складність вкладених циклів
Вкладені цикли збільшують складність алгоритму. Два рівні — O(n^2), три — O(n^3). Для великих обсягів даних шукайте альтернативні рішення.
```python
# O(n^2) — повільно для великих списків
for i in range(1000):
    for j in range(1000):
        pass  # 1 000 000 ітерацій

# Краще — використовувати множини для пошуку
big_list = list(range(10000))
big_set = set(big_list)  # пошук у set — O(1)
```
:::

## Корисні патерни

### Ітерація з розпакуванням

```python
# Список кортежів
coordinates = [(0, 0), (1, 2), (3, 4)]
for x, y in coordinates:
    print(f"x={x}, y={y}")

# Список словників
test_data = [
    ("admin@test.com", "Admin123!", 200),
    ("user@test.com", "User456!", 200),
    ("invalid@test.com", "wrong", 401),
]

for email, password, expected_status in test_data:
    print(f"Логін {email} → очікуємо {expected_status}")
```

### Walrus operator (:=) у циклах (Python 3.8+)

```python
# Читання даних до кінця
import random

# Без walrus
while True:
    value = random.randint(1, 10)
    if value == 7:
        break
    print(f"Отримано: {value}")

# З walrus operator
while (value := random.randint(1, 10)) != 7:
    print(f"Отримано: {value}")
print(f"Знайдено 7!")
```

### Retry з exponential backoff

::: info Приклад для QA: retry нестабільних запитів
```python
import time

def retry_request(url, max_retries=5):
    """Повторює запит з експоненційною затримкою."""
    for attempt in range(max_retries):
        try:
            response = make_request(url)  # умовна функція
            if response.status_code == 200:
                return response
        except ConnectionError as e:
            wait_time = 2 ** attempt  # 1, 2, 4, 8, 16 секунд
            print(f"Спроба {attempt + 1}/{max_retries} невдала. "
                  f"Чекаємо {wait_time}с...")
            time.sleep(wait_time)

    raise Exception(f"Всі {max_retries} спроб невдалі для {url}")
```
:::

## Часті помилки

### Зміна списку під час ітерації

```python
# НЕПРАВИЛЬНО — зміна списку під час перебору
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Непередбачувана поведінка!

# ПРАВИЛЬНО — створити новий список
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)  # [1, 3, 5]

# АБО — ітерація по копії
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # [:] створює копію
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3, 5]
```

### Забутий інкремент у while

```python
# НЕПРАВИЛЬНО — нескінченний цикл
# i = 0
# while i < 5:
#     print(i)  # i ніколи не змінюється!

# ПРАВИЛЬНО
i = 0
while i < 5:
    print(i)
    i += 1
```

### Невикористання enumerate

```python
# НЕПРАВИЛЬНО — ручний лічильник
items = ["a", "b", "c"]
i = 0
for item in items:
    print(f"{i}: {item}")
    i += 1

# ПРАВИЛЬНО — enumerate
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

::: tip Правило
Якщо вам потрібен індекс елемента під час ітерації, завжди використовуйте `enumerate()` замість ручного лічильника.
:::

## Корисні посилання

- [Офіційна документація: for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Офіційна документація: range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Офіційна документація: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 274 — Dict Comprehensions](https://peps.python.org/pep-0274/)
- [Real Python — Python for Loops](https://realpython.com/python-for-loop/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/collections">← Колекції</a>
  <a href="/python_automation_courses/docs/python/functions">Функції →</a>
</div>
