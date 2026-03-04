# Колекції

Колекції в Python — це структури даних для зберігання та організації множини елементів. Вони є основою будь-якого автоматизованого тестування: від зберігання тестових даних до управління конфігураціями.

## Списки (list)

Список — впорядкована змінювана (mutable) колекція елементів. Найчастіше використовувана структура даних у Python.

### Створення списків

```python
# Порожній список
empty = []
empty2 = list()

# Список з елементами
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", True, 3.14, None]

# Список зі списку (копія)
original = [1, 2, 3]
copy = list(original)

# Список з range
numbers = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Індексація та зрізи (slicing)

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Індексація (починається з 0)
fruits[0]      # "apple"
fruits[2]      # "cherry"
fruits[-1]     # "elderberry" — останній елемент
fruits[-2]     # "date" — передостанній

# Зрізи [start:stop:step]
fruits[1:3]    # ["banana", "cherry"] — з 1 до 3 (не включаючи 3)
fruits[:3]     # ["apple", "banana", "cherry"] — перші 3
fruits[2:]     # ["cherry", "date", "elderberry"] — з 2 до кінця
fruits[::2]    # ["apple", "cherry", "elderberry"] — кожен другий
fruits[::-1]   # ["elderberry", "date", "cherry", "banana", "apple"] — реверс
```

::: tip Запам'ятайте
Індексація починається з `0`. Негативні індекси рахують з кінця: `-1` — останній, `-2` — передостанній.
:::

### Методи списків

```python
# Додавання елементів
items = [1, 2, 3]
items.append(4)          # [1, 2, 3, 4] — додає в кінець
items.insert(0, 0)       # [0, 1, 2, 3, 4] — вставляє на позицію
items.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6] — додає кілька елементів

# Видалення елементів
items.remove(0)          # [1, 2, 3, 4, 5, 6] — видаляє перше входження
last = items.pop()       # last = 6, items = [1, 2, 3, 4, 5]
second = items.pop(1)    # second = 2, items = [1, 3, 4, 5]
del items[0]             # items = [3, 4, 5]

# Сортування
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()           # [1, 1, 2, 3, 4, 5, 6, 9] — на місці
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1] — у зворотному порядку
sorted_nums = sorted(numbers)  # Повертає новий список, не змінює оригінал

# Реверс
numbers.reverse()        # Розвертає список на місці

# Пошук та підрахунок
numbers = [1, 2, 3, 2, 1]
numbers.index(2)         # 1 — індекс першого входження
numbers.count(2)         # 2 — кількість входжень
3 in numbers             # True — перевірка наявності
len(numbers)             # 5 — довжина списку
```

::: warning Зверніть увагу
`sort()` змінює список на місці та повертає `None`. `sorted()` повертає новий відсортований список. Не пишіть `items = items.sort()` — це присвоїть `None`!
:::

### Списки-вирази (list comprehensions)

```python
# Базовий синтаксис: [вираз for елемент in ітерабельний]
squares = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# З умовою (фільтрація)
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# З перетворенням
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]  # ["ALICE", "BOB", "CHARLIE"]

# З умовним виразом
labels = ["pass" if x >= 50 else "fail" for x in [80, 30, 65, 45, 90]]
# ["pass", "fail", "pass", "fail", "pass"]
```

::: info Приклад для QA: фільтрація результатів тестів
```python
# Результати тестів
test_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

# Тільки провалені тести
failed = [t["name"] for t in test_results if t["status"] == "failed"]
# ["test_signup", "test_profile"]

# Повільні тести (> 2 секунди)
slow_tests = [t for t in test_results if t["duration"] > 2.0]
```
:::

## Кортежі (tuple)

Кортеж — впорядкована **незмінна** (immutable) колекція. Після створення елементи не можна додавати, видаляти чи змінювати.

### Створення кортежів

```python
# Створення кортежу
coordinates = (10, 20)
single = (42,)           # Кортеж з одним елементом — кома обов'язкова!
not_tuple = (42)          # Це просто число в дужках, не кортеж!
from_list = tuple([1, 2, 3])

# Без дужок (пакування)
point = 10, 20, 30        # Теж кортеж: (10, 20, 30)
```

### Розпакування кортежів

```python
# Базове розпакування
x, y = (10, 20)
print(x)  # 10
print(y)  # 20

# Розпакування з * (зірочкою)
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

head, *middle, tail = (1, 2, 3, 4, 5)
# head = 1, middle = [2, 3, 4], tail = 5

# Обмін значень змінних
a, b = 1, 2
a, b = b, a  # a = 2, b = 1
```

### Коли використовувати кортежі замість списків?

| Кортеж (tuple) | Список (list) |
|----------------|---------------|
| Дані не змінюватимуться | Дані можуть змінюватися |
| Координати, RGB-кольори | Колекція тестів, результати |
| Ключі словника | Буфер, черга, стек |
| Повернення кількох значень з функції | Набір даних для обробки |
| Трохи швидше та менше пам'яті | Більше методів |

::: info Приклад для QA: повернення кількох значень
```python
def run_test(test_name):
    """Запускає тест і повертає результат."""
    # ... логіка виконання тесту ...
    status = "passed"
    duration = 2.35
    error_message = None
    return status, duration, error_message  # Повертає кортеж

# Розпакування результату
status, duration, error = run_test("test_login")
print(f"[{status}] {duration:.2f}s")
```
:::

## Словники (dict)

Словник — колекція пар "ключ: значення". Ключі повинні бути незмінними (str, int, tuple) та унікальними.

### Створення словників

```python
# Порожній словник
empty = {}
empty2 = dict()

# Словник з даними
user = {
    "name": "John",
    "age": 30,
    "is_active": True
}

# Створення з пар
pairs = dict([("a", 1), ("b", 2)])  # {"a": 1, "b": 2}

# Створення з ключових аргументів
config = dict(timeout=30, retries=3, base_url="https://example.com")
```

### Доступ до елементів

```python
user = {"name": "Alice", "age": 25, "role": "QA"}

# Доступ за ключем
user["name"]         # "Alice"
# user["email"]      # KeyError! — ключа не існує

# Безпечний доступ з get()
user.get("name")           # "Alice"
user.get("email")          # None — ключа немає, помилки немає
user.get("email", "N/A")   # "N/A" — значення за замовчуванням

# Перевірка наявності ключа
"name" in user       # True
"email" in user      # False
```

::: tip Рекомендація
Завжди використовуйте `.get()` коли не впевнені, що ключ існує. Це запобігає `KeyError` у тестах.
:::

### Методи словників

```python
user = {"name": "Alice", "age": 25}

# Отримання ключів, значень, пар
user.keys()      # dict_keys(["name", "age"])
user.values()    # dict_values(["Alice", 25])
user.items()     # dict_items([("name", "Alice"), ("age", 25)])

# Додавання та оновлення
user["email"] = "alice@test.com"    # Додає нову пару
user["age"] = 26                    # Оновлює існуюче значення
user.update({"role": "QA", "age": 27})  # Оновлює кілька пар

# Видалення
email = user.pop("email")           # Видаляє та повертає значення
user.pop("phone", None)             # Безпечне видалення (не буде KeyError)
del user["role"]                     # Видаляє пару

# Ітерація
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key}: {value}")
```

### Словники-вирази (dict comprehensions)

```python
# Базовий синтаксис: {ключ: значення for елемент in ітерабельний}
squares = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# З умовою
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Інверсія словника
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

::: info Приклад для QA: конфігурація тестового середовища
```python
# Конфігурація як словник
config = {
    "base_url": "https://staging.example.com",
    "timeout": 30,
    "browser": "chromium",
    "headless": True,
    "retries": 3,
}

# Доступ до конфігурації
base_url = config.get("base_url")
timeout = config.get("timeout", 10)  # 10 як значення за замовчуванням

# Оновлення конфігурації для різних середовищ
production_overrides = {"base_url": "https://example.com", "headless": False}
config.update(production_overrides)

# Перетворення HTTP-заголовків
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
    "X-Request-ID": "test-001",
}
```
:::

## Множини (set)

Множина — невпорядкована колекція **унікальних** елементів. Множини не підтримують індексацію.

### Створення множин

```python
# Створення множини
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 2, 1}    # {1, 2, 3} — дублікати видаляються
empty_set = set()              # Порожня множина (не {}!)
from_list = set([1, 2, 2, 3]) # {1, 2, 3}
```

::: warning Увага
`{}` створює порожній **словник**, а не множину! Для порожньої множини використовуйте `set()`.
:::

### Методи множин

```python
colors = {"red", "green", "blue"}

# Додавання
colors.add("yellow")        # {"red", "green", "blue", "yellow"}
colors.add("red")           # Без змін — елемент вже є

# Видалення
colors.remove("yellow")     # Видаляє елемент (KeyError якщо немає)
colors.discard("purple")    # Видаляє елемент (без помилки якщо немає)
removed = colors.pop()      # Видаляє та повертає довільний елемент
```

### Операції над множинами

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Об'єднання (union) — всі елементи з обох множин
a | b              # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)         # те саме

# Перетин (intersection) — спільні елементи
a & b              # {4, 5}
a.intersection(b)  # те саме

# Різниця (difference) — елементи в a, яких немає в b
a - b              # {1, 2, 3}
a.difference(b)    # те саме

# Симетрична різниця — елементи, що є тільки в одній з множин
a ^ b              # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)  # те саме

# Підмножина та надмножина
{1, 2}.issubset({1, 2, 3})      # True — {1,2} є підмножиною
{1, 2, 3}.issuperset({1, 2})    # True — {1,2,3} є надмножиною
```

::: info Приклад для QA: порівняння тестових покриттів
```python
# Тести, що покривають різні модулі
smoke_tests = {"test_login", "test_home", "test_search"}
regression_tests = {"test_login", "test_home", "test_search", "test_cart", "test_checkout"}
flaky_tests = {"test_search", "test_cart"}

# Які тести є в regression, але не в smoke?
new_in_regression = regression_tests - smoke_tests
# {"test_cart", "test_checkout"}

# Стабільні regression тести (без flaky)
stable_tests = regression_tests - flaky_tests
# {"test_login", "test_home", "test_checkout"}

# Унікальні тест-кейси (без дублікатів)
all_test_ids = [1, 2, 3, 2, 4, 3, 5]
unique_ids = list(set(all_test_ids))  # [1, 2, 3, 4, 5]
```
:::

## Вкладені колекції

Колекції можна вкладати одна в одну для створення складних структур даних.

```python
# Список словників
users = [
    {"name": "Alice", "role": "QA"},
    {"name": "Bob", "role": "Dev"},
    {"name": "Charlie", "role": "QA"},
]

# Доступ до вкладених даних
users[0]["name"]  # "Alice"

# Словник зі списками
test_suite = {
    "smoke": ["test_login", "test_home"],
    "regression": ["test_login", "test_home", "test_cart", "test_checkout"],
    "performance": ["test_load", "test_stress"],
}

# Словник словників
environments = {
    "dev": {"url": "https://dev.example.com", "db": "dev_db"},
    "staging": {"url": "https://staging.example.com", "db": "staging_db"},
    "prod": {"url": "https://example.com", "db": "prod_db"},
}

# Доступ
staging_url = environments["staging"]["url"]
# "https://staging.example.com"
```

::: info Приклад для QA: зберігання та аналіз результатів тестів
```python
# Повна структура тестового звіту
test_report = {
    "suite": "Regression",
    "total": 4,
    "results": [
        {
            "name": "test_login_valid",
            "status": "passed",
            "duration": 1.2,
            "tags": ["smoke", "auth"],
        },
        {
            "name": "test_login_invalid",
            "status": "passed",
            "duration": 0.9,
            "tags": ["auth"],
        },
        {
            "name": "test_add_to_cart",
            "status": "failed",
            "duration": 3.1,
            "tags": ["cart", "regression"],
            "error": "Element not found: #add-btn",
        },
        {
            "name": "test_checkout",
            "status": "skipped",
            "duration": 0,
            "tags": ["cart", "checkout"],
        },
    ],
}

# Аналіз результатів
results = test_report["results"]

passed = [r["name"] for r in results if r["status"] == "passed"]
failed = [r["name"] for r in results if r["status"] == "failed"]

total_duration = sum(r["duration"] for r in results)
pass_rate = len(passed) / test_report["total"] * 100

print(f"Pass rate: {pass_rate:.1f}%")          # Pass rate: 50.0%
print(f"Total duration: {total_duration:.1f}s") # Total duration: 5.2s
print(f"Failed: {failed}")                      # Failed: ["test_add_to_cart"]

# Знайти всі унікальні теги
all_tags = set()
for r in results:
    all_tags.update(r["tags"])
# {"smoke", "auth", "cart", "regression", "checkout"}
```
:::

## Корисні функції для колекцій

```python
numbers = [5, 2, 8, 1, 9, 3]

len(numbers)      # 6 — кількість елементів
min(numbers)      # 1 — мінімальне значення
max(numbers)      # 9 — максимальне значення
sum(numbers)      # 28 — сума елементів
sorted(numbers)   # [1, 2, 3, 5, 8, 9] — новий відсортований список

# enumerate — ітерація з індексом
for i, num in enumerate(numbers):
    print(f"{i}: {num}")

# zip — об'єднання кількох ітерованих об'єктів
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# any / all — перевірка умов
numbers = [2, 4, 6, 8]
all(x % 2 == 0 for x in numbers)  # True — всі парні
any(x > 5 for x in numbers)       # True — хоча б один > 5
```

## Корисні посилання

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Collections Module](https://docs.python.org/3/library/collections.html)
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/strings">← Рядки</a>
  <a href="/python_automation_courses/docs/python/loops">Цикли →</a>
</div>
