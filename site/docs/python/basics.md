# Основи Python

Базовий синтаксис мови Python — змінні, оператори, введення/виведення даних. Ця сторінка охоплює все, що потрібно для початку роботи з Python у QA-автоматизації.

## Коментарі

Коментарі допомагають пояснити код іншим розробникам (і вам через місяць).

```python
# Однорядковий коментар — починається з #

# Декілька однорядкових коментарів поспіль
# описують складну логіку
# крок за кроком

"""
Багаторядковий коментар (docstring).
Використовується для документації модулів,
класів та функцій.
"""

def login(username, password):
    """Авторизує користувача в системі.

    Args:
        username: Ім'я користувача
        password: Пароль

    Returns:
        True якщо авторизація успішна
    """
    pass
```

::: tip Коли коментувати?
- Пояснюйте **чому**, а не **що** — код вже показує що відбувається
- Документуйте функції через docstrings
- Не коментуйте очевидний код: `x = x + 1  # збільшуємо x на 1` — зайве
:::

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

::: info Приклад для QA: тестові дані у змінних
```python
# Зберігання тестових даних
base_url = "https://example.com"
api_endpoint = f"{base_url}/api/v1/users"
admin_login = "admin@test.com"
admin_password = "Test123!"
timeout_seconds = 30
max_retries = 3

# Очікувані значення для assertions
expected_status = 200
expected_title = "Dashboard"
```
:::

## Типи даних

| Тип | Приклад | Опис | Mutable |
|-----|---------|------|---------|
| `str` | `"Hello"` | Текстовий рядок | Ні |
| `int` | `42` | Ціле число | Ні |
| `float` | `3.14` | Дробове число | Ні |
| `bool` | `True` / `False` | Логічний тип | Ні |
| `NoneType` | `None` | Відсутність значення | Ні |
| `list` | `[1, 2, 3]` | Список (впорядкований) | **Так** |
| `tuple` | `(1, 2, 3)` | Кортеж (впорядкований) | Ні |
| `set` | `{1, 2, 3}` | Множина (унікальні) | **Так** |
| `dict` | `{"key": "val"}` | Словник (ключ-значення) | **Так** |

```python
# Перевірка типу
name = "Test"
print(type(name))  # <class 'str'>
```

::: warning Mutable vs Immutable
**Mutable** (змінювані) об'єкти можна змінити "на місці". **Immutable** — ні, при зміні створюється новий об'єкт.
```python
# Mutable — list змінюється на місці
items = [1, 2, 3]
items.append(4)      # items = [1, 2, 3, 4] — той самий об'єкт

# Immutable — str створює новий об'єкт
name = "Hello"
name_upper = name.upper()  # "HELLO" — новий рядок, name не змінився
```
:::

## Оператори

### Арифметичні оператори

| Оператор | Опис | Приклад | Результат |
|----------|------|---------|-----------|
| `+` | Додавання | `10 + 3` | `13` |
| `-` | Віднімання | `10 - 3` | `7` |
| `*` | Множення | `10 * 3` | `30` |
| `/` | Ділення (float) | `10 / 3` | `3.33...` |
| `//` | Цілочисельне ділення | `10 // 3` | `3` |
| `%` | Залишок від ділення | `10 % 3` | `1` |
| `**` | Піднесення до степеня | `10 ** 3` | `1000` |

### Оператори порівняння

| Оператор | Опис | Приклад | Результат |
|----------|------|---------|-----------|
| `==` | Дорівнює | `5 == 10` | `False` |
| `!=` | Не дорівнює | `5 != 10` | `True` |
| `>` | Більше | `5 > 10` | `False` |
| `<` | Менше | `5 < 10` | `True` |
| `>=` | Більше або дорівнює | `5 >= 10` | `False` |
| `<=` | Менше або дорівнює | `5 <= 10` | `True` |

### Логічні оператори

| Оператор | Опис | Приклад | Результат |
|----------|------|---------|-----------|
| `and` | Логічне І — обидва True | `True and False` | `False` |
| `or` | Логічне АБО — хоча б один True | `True or False` | `True` |
| `not` | Логічне НЕ — інвертує | `not True` | `False` |

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

::: details Що перетворюється в False?
Ці значення вважаються "хибними" (falsy) при перетворенні в `bool`:
```python
bool(0)        # False — нуль
bool(0.0)      # False — нуль float
bool("")       # False — порожній рядок
bool([])       # False — порожній список
bool({})       # False — порожній словник
bool(None)     # False — None

# Все інше — True
bool(1)        # True
bool("text")   # True
bool([1, 2])   # True
```
:::

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

::: info Приклад для QA: генерація повідомлень
```python
# Логування у тестах
test_name = "test_login_valid_user"
status = "PASSED"
duration = 2.347
print(f"[{status}] {test_name} — {duration:.2f}s")
# [PASSED] test_login_valid_user — 2.35s

# Генерація тестових даних
for i in range(3):
    email = f"user_{i}@test.com"
    print(f"Created test user: {email}")
```
:::

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

::: info Приклад для QA: перевірка відповідей API
```python
# Валідація status code
status_code = 201
assert 200 <= status_code < 300, f"Expected 2xx, got {status_code}"

# Перевірка вмісту відповіді
response_body = {"id": 1, "name": "Test User"}

if "id" in response_body:
    print(f"User created with ID: {response_body['id']}")
else:
    print("ERROR: 'id' not found in response")

# Перевірка декількох умов
is_success = status_code == 200
has_data = response_body is not None
is_valid = is_success and has_data
```
:::

::: warning Відступи
Python використовує відступи (4 пробіли) замість фігурних дужок. Неправильні відступи призведуть до `IndentationError`.
:::

## Часті помилки початківців

### `=` vs `==`

```python
# = це присвоєння
x = 10

# == це порівняння
if x == 10:    # Правильно
    print("yes")

if x = 10:     # SyntaxError!
    print("yes")
```

### Відступи (IndentationError)

```python
# Неправильно — змішані відступи
if True:
    print("ok")
      print("error")  # IndentationError!

# Правильно — однакові відступи (4 пробіли)
if True:
    print("ok")
    print("also ok")
```

### Зміна типу змінної

```python
# Python дозволяє, але це небезпечно
count = 10
count = "ten"   # Тепер це рядок — легко отримати помилку пізніше

# Краще: використовуйте різні імена
count = 10
count_text = "ten"
```

### `is None` vs `== None`

```python
result = None

# Правильно — is перевіряє ідентичність
if result is None:
    print("No result")

if result is not None:
    print(f"Got: {result}")

# Неправильно — == перевіряє рівність (може бути перевизначено)
if result == None:  # Працює, але не рекомендовано
    print("No result")
```

::: tip Правило
Завжди використовуйте `is None` та `is not None` для перевірки на `None`. Оператор `is` порівнює ідентичність об'єкта, а не його значення.
:::

<script setup>
const quizQuestions = [
  {
    question: 'Що повертає type(42)?',
    options: ['str', 'int', 'float', 'number'],
    correct: 1,
    explanation: 'type(42) повертає <class int>, бо 42 — це ціле число (integer).'
  },
  {
    question: 'Який символ починає однорядковий коментар у Python?',
    options: ['//', '#', '--', '/*'],
    correct: 1,
    explanation: 'У Python однорядковий коментар починається з символу #. Символи // використовуються в JavaScript/C++.'
  },
  {
    question: 'Який з цих типів даних є mutable (змінюваний)?',
    options: ['str', 'tuple', 'int', 'dict'],
    correct: 3,
    explanation: 'dict (словник) є mutable — можна додавати, змінювати та видаляти ключі. str, tuple та int — immutable.'
  },
  {
    question: 'Що поверне вираз 10 // 3?',
    options: ['3.33', '3', '1', '3.0'],
    correct: 1,
    explanation: 'Оператор // — це цілочисельне ділення. 10 // 3 = 3 (відкидає дробову частину).'
  },
  {
    question: 'Що поверне вираз 10 % 3?',
    options: ['3', '0', '1', '10'],
    correct: 2,
    explanation: 'Оператор % повертає залишок від ділення. 10 % 3 = 1, бо 10 = 3 * 3 + 1.'
  },
  {
    question: 'Який стиль іменування змінних рекомендує PEP 8?',
    options: ['camelCase', 'PascalCase', 'snake_case', 'UPPER_CASE'],
    correct: 2,
    explanation: 'PEP 8 рекомендує snake_case для змінних та функцій: user_name, max_retry_count.'
  },
  {
    question: 'Що поверне bool("")?',
    options: ['True', 'False', 'None', 'Error'],
    correct: 1,
    explanation: 'Порожній рядок є falsy значенням — bool("") повертає False. Непорожні рядки повертають True.'
  },
  {
    question: 'Як правильно перевірити змінну на None?',
    options: ['if x == None', 'if x is None', 'if x = None', 'if x.isNone()'],
    correct: 1,
    explanation: 'Використовуйте is None — оператор is перевіряє ідентичність об\'єкта. == може бути перевизначений.'
  },
  {
    question: 'Яка різниця між = та ==?',
    options: ['Немає різниці', '= порівнює, == присвоює', '= присвоює значення, == порівнює', '== працює тільки з числами'],
    correct: 2,
    explanation: '= — оператор присвоєння (x = 10). == — оператор порівняння (if x == 10). Плутанина між ними — часта помилка.'
  },
  {
    question: 'Що поверне вираз True and False?',
    options: ['True', 'False', 'None', 'Error'],
    correct: 1,
    explanation: 'Оператор and повертає True лише коли обидва операнди True. True and False = False.'
  },
  {
    question: 'Який рекомендований спосіб форматування рядків у сучасному Python?',
    options: ['% оператор', '.format()', 'f-string', 'concat (+)'],
    correct: 2,
    explanation: 'f-string — рекомендований спосіб з Python 3.6+. Він найчитабельніший та найшвидший.'
  },
  {
    question: 'Що станеться при виконанні: x, y, z = 1, 2, 3?',
    options: ['SyntaxError', 'x=1, y=2, z=3', 'Всі стануть [1,2,3]', 'x=3, y=2, z=1'],
    correct: 1,
    explanation: 'Це множинне присвоєння — кожна змінна отримує відповідне значення: x=1, y=2, z=3.'
  },
  {
    question: 'Що використовується для документування функцій у Python?',
    options: ['// коментар', '# коментар', 'docstring (потрійні лапки)', '/* ... */'],
    correct: 2,
    explanation: 'Docstring — рядок у потрійних лапках одразу після визначення функції. Він доступний через func.__doc__.'
  },
  {
    question: 'Яку помилку викличуть неправильні відступи в Python?',
    options: ['SyntaxError', 'IndentationError', 'TypeError', 'ValueError'],
    correct: 1,
    explanation: 'Python використовує відступи для визначення блоків коду. Неправильні відступи викликають IndentationError.'
  },
  {
    question: 'Що поверне isinstance(True, bool)?',
    options: ['True', 'False', 'None', 'TypeError'],
    correct: 0,
    explanation: 'isinstance перевіряє, чи є об\'єкт екземпляром вказаного типу. True — це значення типу bool, тому результат True.'
  }
]
</script>

## Перевір себе

<Quiz :questions="quizQuestions" />

## Корисні посилання

- [Офіційний туторіал Python](https://docs.python.org/3/tutorial/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Python для початківців](https://www.learnpython.org/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/">← Вступ</a>
  <a href="/python_automation_courses/docs/python/data-types">Типи даних →</a>
</div>
