# Лекція 5: Функції

Функції в Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_5_Functions/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Визначення функцій
- Параметри та аргументи
- Повернення значень
- Область видимості
- Lambda функції

## Визначення функції

```python
# Базова функція
def greet():
    print("Hello!")

greet()  # виклик

# Функція з параметрами
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Параметри та аргументи

```python
# Позиційні параметри
def add(a, b):
    return a + b

result = add(2, 3)  # 5

# Default параметри
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # "Hello, Alice!"
greet("Bob", "Hi")          # "Hi, Bob!"

# Keyword аргументи
greet(greeting="Hey", name="Charlie")

# *args (довільна кількість позиційних)
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs (довільна кількість keyword)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")
```

## Повернення значень

```python
# Одне значення
def square(x):
    return x ** 2

# Кілька значень (tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

# Без return повертає None
def greet(name):
    print(f"Hello, {name}!")  # None
```

## Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

## Область видимості (Scope)

```python
# Global vs Local
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)   # можна читати
    print(local_var)

my_function()
# print(local_var)  # NameError!

# Модифікація global
counter = 0

def increment():
    global counter
    counter += 1
```

## Lambda функції

```python
# Анонімні функції
square = lambda x: x ** 2
add = lambda a, b: a + b

# З sorted/map/filter
numbers = [3, 1, 4, 1, 5]

# Сортування
sorted(numbers, key=lambda x: -x)  # [5, 4, 3, 1, 1]

# Map
squares = list(map(lambda x: x ** 2, numbers))

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## Docstrings

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area of the rectangle

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width
```

## Вправи

::: tip Вправа 1
Напишіть функцію для перевірки чи є число простим.
:::

::: tip Вправа 2
Створіть функцію-калькулятор, що приймає два числа та операцію.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_5_Functions/examples)
