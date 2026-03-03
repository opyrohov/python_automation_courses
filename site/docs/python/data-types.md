# Типи даних

Детальний огляд основних типів даних у Python — рядки, числа, списки, словники, кортежі та множини.

## Рядки (str)

```python
# Створення рядків
single = 'Hello'
double = "World"
multiline = """Багаторядковий
текст для тестів"""

# Екранування
path = "C:\\Users\\test"
raw = r"C:\Users\test"  # raw рядок — без екранування

# Основні операції
name = "Playwright"
print(len(name))          # 10 — довжина
print(name[0])            # P — перший символ
print(name[-1])           # t — останній символ
print(name[0:4])          # Play — зріз
print(name.upper())       # PLAYWRIGHT
print(name.lower())       # playwright
```

### Методи рядків

```python
text = "  Hello, QA World!  "

text.strip()              # "Hello, QA World!" — видалити пробіли
text.lstrip()             # "Hello, QA World!  "
text.rstrip()             # "  Hello, QA World!"
text.split(", ")          # ["  Hello", "QA World!  "]
text.replace("QA", "Dev") # "  Hello, Dev World!  "
text.find("QA")           # 9 — індекс підрядка
text.count("l")           # 2 — кількість входжень
text.startswith("  H")    # True
text.endswith("!  ")      # True

# Перевірки
"hello123".isalnum()      # True — літери та цифри
"hello".isalpha()         # True — тільки літери
"12345".isdigit()         # True — тільки цифри
```

::: tip F-strings для тестів
```python
test_name = "login_test"
status = "passed"
duration = 1.234

# Зручне форматування результатів
log = f"Test [{test_name}] {status} in {duration:.2f}s"
# "Test [login_test] passed in 1.23s"
```
:::

## Числа

```python
# Цілі числа (int)
count = 42
big = 1_000_000  # розділювач для читабельності
binary = 0b1010  # 10 у двійковій
hex_num = 0xFF   # 255 у шістнадцятковій

# Дробові (float)
price = 19.99
scientific = 1.5e3  # 1500.0

# Математичні операції
import math

math.ceil(4.2)    # 5 — округлення вгору
math.floor(4.8)   # 4 — округлення вниз
round(4.567, 2)   # 4.57 — округлення до 2 знаків
abs(-10)          # 10 — абсолютне значення
max(1, 5, 3)      # 5
min(1, 5, 3)      # 1
```

## Списки (list)

Списки — змінювана впорядкована колекція елементів.

```python
# Створення
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
empty = []

# Доступ
fruits[0]     # "apple"
fruits[-1]    # "cherry"
fruits[1:3]   # ["banana", "cherry"]

# Модифікація
fruits.append("orange")       # додати в кінець
fruits.insert(0, "mango")     # вставити за індексом
fruits.extend(["kiwi", "grape"])  # додати кілька
fruits.remove("banana")       # видалити за значенням
fruits.pop()                  # видалити останній
fruits.pop(0)                 # видалити за індексом

# Сортування
numbers = [3, 1, 4, 1, 5]
numbers.sort()                # [1, 1, 3, 4, 5] — на місці
numbers.sort(reverse=True)    # [5, 4, 3, 1, 1]
sorted_nums = sorted(numbers) # нова копія

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

::: info Приклад для QA
```python
# Фільтрація результатів тестів
test_results = [
    {"name": "test_login", "status": "passed", "duration": 1.2},
    {"name": "test_signup", "status": "failed", "duration": 3.5},
    {"name": "test_logout", "status": "passed", "duration": 0.8},
    {"name": "test_profile", "status": "failed", "duration": 2.1},
]

# Знайти всі провалені тести
failed = [t["name"] for t in test_results if t["status"] == "failed"]
# ["test_signup", "test_profile"]

# Загальний час виконання
total_time = sum(t["duration"] for t in test_results)
# 7.6
```
:::

## Словники (dict)

Словники — невпорядкована колекція пар ключ-значення.

```python
# Створення
user = {
    "name": "John",
    "age": 30,
    "role": "QA Engineer"
}

# Доступ
user["name"]              # "John"
user.get("email", "N/A")  # "N/A" — з default значенням

# Модифікація
user["email"] = "john@test.com"  # додати/оновити
del user["age"]                   # видалити
user.pop("role")                  # видалити з поверненням

# Перебір
for key in user:
    print(key)

for key, value in user.items():
    print(f"{key}: {value}")

# Корисні методи
user.keys()     # dict_keys(["name", "email"])
user.values()   # dict_values(["John", "john@test.com"])
user.items()    # dict_items([("name", "John"), ...])
user.update({"age": 31, "city": "Kyiv"})

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Кортежі (tuple)

Кортежі — незмінна впорядкована колекція.

```python
# Створення
point = (10, 20)
single = (42,)  # одноелементний кортеж (потрібна кома)
rgb = (255, 128, 0)

# Розпакування
x, y = point
r, g, b = rgb

# Використання як ключ словника (бо незмінний)
coordinates = {
    (0, 0): "origin",
    (1, 1): "diagonal"
}
```

## Множини (set)

Множини — невпорядкована колекція унікальних елементів.

```python
# Створення
unique = {1, 2, 3, 3, 2}  # {1, 2, 3}
from_list = set([1, 1, 2, 3])

# Операції
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # {1, 2, 3, 4, 5, 6} — об'єднання
a & b   # {3, 4} — перетин
a - b   # {1, 2} — різниця
a ^ b   # {1, 2, 5, 6} — симетрична різниця

# Перевірка
3 in a  # True
7 in a  # False
```

::: tip Множини для порівняння
```python
# Порівняння очікуваних та фактичних елементів
expected_items = {"Login", "Profile", "Settings", "Logout"}
actual_items = {"Login", "Profile", "Logout"}

missing = expected_items - actual_items  # {"Settings"}
extra = actual_items - expected_items    # set()
```
:::

## Корисні посилання

- [Документація: Вбудовані типи](https://docs.python.org/3/library/stdtypes.html)
- [Документація: Структури даних](https://docs.python.org/3/tutorial/datastructures.html)
