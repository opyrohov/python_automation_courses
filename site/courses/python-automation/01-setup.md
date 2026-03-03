# Лекція 1: Встановлення Python та основи

Перша лекція курсу — встановлення Python, налаштування середовища розробки, змінні, типи даних та базові оператори.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_1_Python_Basics_Setup/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Встановлення Python
- Налаштування IDE (VS Code / PyCharm)
- Віртуальне середовище
- Перша програма "Hello World"
- Змінні та типи даних
- Базові оператори
- Функція `print()` та форматування

## Встановлення Python

### Завантаження та інсталяція

1. Завантажте Python з [python.org](https://www.python.org/downloads/) (версія 3.11+)
2. Під час інсталяції обов'язково поставте галочку **"Add Python to PATH"**
3. Перевірте встановлення:

```bash
python --version
# або
python3 --version
```

::: warning Важливо: Add to PATH
Без цієї опції Python не буде доступний з командного рядка. Якщо забули — перевстановіть Python з цією галочкою.
:::

### Вибір IDE

#### VS Code (рекомендовано для початківців)

1. Завантажте з [code.visualstudio.com](https://code.visualstudio.com/)
2. Встановіть розширення Python:
   - Відкрийте VS Code → Extensions (`Ctrl+Shift+X`)
   - Знайдіть "Python" від Microsoft → Install

#### PyCharm

1. Завантажте з [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Community Edition — безкоштовна
3. Підтримка Python вбудована

### Віртуальне середовище

```bash
# Створення віртуального середовища
python -m venv venv

# Активація (Windows)
venv\Scripts\activate

# Активація (macOS/Linux)
source venv/bin/activate

# Деактивація
deactivate
```

::: info Навіщо віртуальне середовище?
Воно ізолює залежності проєкту від системного Python. Кожен проєкт має свої бібліотеки, без конфліктів між ними.
:::

## Hello World

```python
# Перша програма
print("Hello, World!")

# Змінні
name = "Python"
version = 3.12
is_awesome = True

print(f"Welcome to {name} {version}!")
```

### Запуск програми

```bash
# Збережіть код у файл hello.py та запустіть
python hello.py
```

## Змінні та типи даних

Змінні в Python не потребують оголошення типу — інтерпретатор визначає тип автоматично.

```python
# Створення змінних
name = "Alice"          # str — рядок
age = 25                # int — ціле число
height = 5.6            # float — дробове число
is_student = True       # bool — логічне значення

# Множинне присвоєння
x, y, z = 1, 2, 3
```

### Основні типи даних

| Тип | Приклад | Опис |
|-----|---------|------|
| `str` | `"Hello"` | Рядок |
| `int` | `42` | Ціле число |
| `float` | `3.14` | Число з плаваючою точкою |
| `bool` | `True` / `False` | Булеве значення |
| `None` | `None` | Відсутність значення |

### Перевірка та конвертація типів

```python
# Перевірка типу
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>

# Конвертація типів
age_string = "30"
age_number = int(age_string)        # str → int
price_string = "29.99"
price_number = float(price_string)  # str → float
count = 100
count_string = str(count)           # int → str
```

::: tip Іменування змінних
Використовуйте `snake_case` — це стандарт Python (PEP 8):
```python
# Правильно ✓
user_name = "Alice"
total_price = 99.99
is_active = True

# Неправильно ✗
userName = "Alice"    # camelCase — це для JavaScript
TotalPrice = 99.99   # PascalCase — це для класів
```
:::

## Оператори

### Арифметичні оператори

```python
a, b = 10, 3

print(a + b)   # 13  — додавання
print(a - b)   # 7   — віднімання
print(a * b)   # 30  — множення
print(a / b)   # 3.33 — ділення (завжди float)
print(a // b)  # 3   — цілочисельне ділення
print(a % b)   # 1   — залишок від ділення
print(a ** b)  # 1000 — піднесення до степеня
```

### Оператори порівняння

```python
x, y = 5, 10

print(x == y)   # False — дорівнює
print(x != y)   # True  — не дорівнює
print(x > y)    # False — більше
print(x < y)    # True  — менше
print(x >= y)   # False — більше або дорівнює
print(x <= y)   # True  — менше або дорівнює
```

### Логічні оператори

```python
is_adult = True
has_ticket = True

# and — обидві умови True
can_enter = is_adult and has_ticket  # True

# or — хоча б одна умова True
has_cash = False
has_card = True
can_pay = has_cash or has_card  # True

# not — інверсія
is_raining = False
is_sunny = not is_raining  # True
```

### Складені оператори присвоєння

```python
score = 100
score += 10   # score = score + 10 → 110
score -= 5    # score = score - 5  → 105
score *= 2    # score = score * 2  → 210
score /= 3    # score = score / 3  → 70.0
```

## Функція print()

### Базове використання

```python
# Простий вивід
print("Hello, World!")

# Кілька значень (розділяються пробілом)
print("Hello", "Python", "Programming")

# Без переходу на новий рядок
print("Loading", end="")
print("...", end="")
print(" Done!")  # Loading... Done!

# Кастомний розділювач
print("2024", "01", "15", sep="-")  # 2024-01-15
```

### Форматування рядків (f-strings)

```python
name = "Alice"
age = 25

# f-string — рекомендований спосіб
print(f"My name is {name} and I'm {age} years old")

# Вирази всередині f-string
print(f"Next year I'll be {age + 1}")
print(f"Name uppercase: {name.upper()}")

# Форматування чисел
price = 1234.567
print(f"Price: ${price:.2f}")        # Price: $1234.57
print(f"Large: {1234567890:,}")      # Large: 1,234,567,890
print(f"Percent: {0.856:.1%}")       # Percent: 85.6%
```

::: info Інші способи форматування
```python
# .format() — старіший спосіб
print("Hello, {}!".format(name))

# % оператор — застарілий
print("Hello, %s!" % name)

# f-strings — найзручніший, використовуйте його
print(f"Hello, {name}!")
```
:::

### Вирівнювання тексту

```python
# Таблиця з вирівнюванням
print(f"{'Product':<15} {'Price':>10}")
print(f"{'Laptop':<15} {'$999.99':>10}")
print(f"{'Mouse':<15} {'$29.99':>10}")
print(f"{'Keyboard':<15} {'$79.99':>10}")
```

### Дебаг з print

```python
# Python 3.8+ — показує назву змінної
username = "john_doe"
user_age = 30
print(f"{username=}")   # username='john_doe'
print(f"{user_age=}")   # user_age=30
```

## Коментарі

```python
# Однорядковий коментар

"""
Багаторядковий коментар
використовується для документації
"""

# Коментар з поясненням коду
tax_rate = 0.08  # 8% податок
```

## Вправи

::: tip Вправа 1: Змінні та типи даних
Створіть змінні для міста (назва, населення, площа, чи є столицею). Виведіть інформацію за допомогою f-strings.

[📝 Файл вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_01_variables.py)
:::

::: tip Вправа 2: Калькулятор
Напишіть програму-калькулятор рахунку в ресторані: вартість їжі + напої + податок (8%) + чайові (18%).

[📝 Файл вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_02_calculations.py)
:::

::: tip Вправа 3: Персональна картка
Створіть програму, яка виводить красиву візитну картку з вашою інформацією (ім'я, професія, навички, контакти).

[📝 Файл вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_1_Python_Basics_Setup/exercises/exercise_03_personal_info.py)
:::

## Що далі?

Після цієї лекції ви повинні вміти:
- Встановити Python та налаштувати IDE
- Створювати та використовувати змінні
- Працювати з різними типами даних
- Використовувати оператори
- Форматувати вивід за допомогою f-strings

::: info Додаткові матеріали
- [Документація: Основи Python](/docs/python/basics) — детальний довідник
- [Документація: Типи даних](/docs/python/data-types) — повний огляд типів
- [Cheatsheet: Python](/cheatsheets/python) — швидкий довідник
:::

## Корисні посилання

- [Офіційний туторіал Python](https://docs.python.org/3/tutorial/)
- [Python.org — Downloads](https://www.python.org/downloads/)
- [VS Code — Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
