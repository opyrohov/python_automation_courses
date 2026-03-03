# Python Cheatsheet

Швидкий довідник по Python.

## Змінні та типи даних

```python
# Рядки
name = "Hello"
multiline = """
Багаторядковий
текст
"""

# Числа
integer = 42
floating = 3.14
complex_num = 1 + 2j

# Boolean
is_active = True
is_disabled = False

# None
result = None
```

## Колекції

```python
# Список (list) - змінюваний
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[0]  # "apple"

# Кортеж (tuple) - незмінний
point = (10, 20)
x, y = point  # unpacking

# Словник (dict)
user = {
    "name": "John",
    "age": 30,
    "active": True
}
user["name"]  # "John"
user.get("email", "N/A")  # з default

# Множина (set)
unique = {1, 2, 3, 3}  # {1, 2, 3}
```

## Умовні оператори

```python
# if/elif/else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Тернарний оператор
status = "active" if is_active else "inactive"

# Match (Python 3.10+)
match command:
    case "start":
        run()
    case "stop":
        stop()
    case _:
        print("Unknown")
```

## Цикли

```python
# for
for item in items:
    print(item)

for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i, item in enumerate(items):
    print(f"{i}: {item}")

# while
while condition:
    do_something()

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Dict comprehension
squared = {x: x**2 for x in range(5)}
```

## Функції

```python
# Базова функція
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Default параметри
def greet(name: str = "World") -> str:
    return f"Hello, {name}!"

# *args та **kwargs
def func(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict

# Lambda
square = lambda x: x ** 2
```

## Класи

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"

    @property
    def is_adult(self) -> bool:
        return self.age >= 18

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(data["name"], data["age"])

    @staticmethod
    def validate_age(age: int) -> bool:
        return 0 <= age <= 150
```

## Обробка помилок

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success!")
finally:
    cleanup()

# Власний виняток
class CustomError(Exception):
    pass

raise CustomError("Something went wrong")
```

## Робота з файлами

```python
# Читання
with open("file.txt", "r") as f:
    content = f.read()

# Запис
with open("file.txt", "w") as f:
    f.write("Hello")

# JSON
import json

with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

## Корисні методи рядків

```python
s = "  Hello World  "

s.strip()       # "Hello World"
s.lower()       # "  hello world  "
s.upper()       # "  HELLO WORLD  "
s.split()       # ["Hello", "World"]
s.replace("o", "0")  # "  Hell0 W0rld  "
s.startswith("  H")  # True
s.endswith("  ")     # True
"x" in s        # False
```

## Корисні методи списків

```python
lst = [3, 1, 4, 1, 5]

lst.append(9)      # [3, 1, 4, 1, 5, 9]
lst.extend([2, 6]) # [3, 1, 4, 1, 5, 9, 2, 6]
lst.pop()          # 6, lst = [3, 1, 4, 1, 5, 9, 2]
lst.remove(1)      # [3, 4, 1, 5, 9, 2]
lst.sort()         # [1, 2, 3, 4, 5, 9]
lst.reverse()      # [9, 5, 4, 3, 2, 1]
len(lst)           # 6
sum(lst)           # 24
min(lst), max(lst) # 1, 9
```
