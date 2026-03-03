# Основи Python

Базовий синтаксис мови Python — змінні, оператори, введення/виведення даних.

## Змінні

Змінні в Python не потребують оголошення типу — інтерпретатор визначає тип автоматично.

```python
# Створення змінних
name = "QA Engineer"
age = 25
salary = 5500.50
is_active = True

# Множинне присвоєння
x, y, z = 1, 2, 3
a = b = c = 0
```

::: tip Іменування змінних
Використовуйте `snake_case` для змінних та функцій — це стандарт PEP 8.
```python
# Правильно
user_name = "John"
max_retry_count = 3

# Неправильно
userName = "John"
MaxRetryCount = 3
```
:::

## Типи даних

```python
# Перевірка типу
name = "Test"
print(type(name))  # <class 'str'>

# Основні типи
text = "Hello"          # str
number = 42             # int
decimal = 3.14          # float
flag = True             # bool
nothing = None          # NoneType
items = [1, 2, 3]      # list
pair = (1, 2)           # tuple
unique = {1, 2, 3}      # set
data = {"key": "value"} # dict
```

## Оператори

### Арифметичні оператори

```python
a, b = 10, 3

print(a + b)   # 13  — додавання
print(a - b)   # 7   — віднімання
print(a * b)   # 30  — множення
print(a / b)   # 3.33 — ділення (float)
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
a, b = True, False

print(a and b)  # False — логічне І
print(a or b)   # True  — логічне АБО
print(not a)    # False — логічне НЕ
```

::: info Практичний приклад для QA
```python
# Перевірка умов у тестах
is_visible = True
is_enabled = True
has_text = False

# Елемент готовий до кліку?
can_click = is_visible and is_enabled  # True

# Є хоча б одна проблема?
has_issue = not is_visible or not is_enabled or not has_text  # True
```
:::

## Введення та виведення

```python
# Виведення
print("Hello, World!")
print("Name:", "QA", "Engineer")  # Name: QA Engineer
print(f"Вік: {age}")              # f-string форматування

# Введення
name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))  # конвертація в число
```

## Перетворення типів

```python
# Конвертація типів
num_str = "42"
num_int = int(num_str)      # str → int
num_float = float(num_str)  # str → float
back_str = str(num_int)     # int → str
is_true = bool(1)           # int → bool (True)
is_false = bool(0)          # int → bool (False)

# Перевірка типу
isinstance(42, int)         # True
isinstance("hello", str)    # True
isinstance(True, bool)      # True
```

## Форматування рядків

```python
name = "QA Engineer"
experience = 3

# f-string (рекомендовано)
print(f"Я {name} з досвідом {experience} роки")

# format()
print("Я {} з досвідом {} роки".format(name, experience))

# % оператор (застарілий)
print("Я %s з досвідом %d роки" % (name, experience))

# Форматування чисел
price = 1234.5678
print(f"Ціна: {price:.2f}")     # Ціна: 1234.57
print(f"Відсоток: {0.856:.1%}") # Відсоток: 85.6%
print(f"Число: {42:05d}")       # Число: 00042
```

## Умовні конструкції

```python
# if / elif / else
status_code = 200

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code >= 500:
    print("Server Error")
else:
    print(f"Інший код: {status_code}")

# Тернарний оператор
result = "Pass" if status_code == 200 else "Fail"
```

::: warning Відступи
Python використовує відступи (4 пробіли) замість фігурних дужок. Неправильні відступи призведуть до `IndentationError`.
:::

## Корисні посилання

- [Офіційний туторіал Python](https://docs.python.org/3/tutorial/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Python для початківців](https://www.learnpython.org/)
