# Lecture 2: Strings & Control Flow

Робота з рядками та керування потоком виконання.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_2_Strings_Control_Flow/presentation.html" target="_blank">🎬 Презентація</a> |
[📺 Відео](https://www.loom.com/share/...) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/exercises)

</div>

## Теми лекції

- Рядки та їх методи
- Форматування рядків (f-strings)
- Умовні оператори (if/elif/else)
- Порівняння та логічні оператори

## Рядки

```python
# Створення рядків
single = 'Hello'
double = "World"
multiline = """
Багаторядковий
текст
"""

# Конкатенація
full = single + " " + double  # "Hello World"

# Повторення
repeat = "Ha" * 3  # "HaHaHa"
```

## Методи рядків

```python
text = "  Hello World  "

text.strip()       # "Hello World"
text.lower()       # "  hello world  "
text.upper()       # "  HELLO WORLD  "
text.replace("o", "0")  # "  Hell0 W0rld  "
text.split()       # ["Hello", "World"]

# Перевірки
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True
"Hello".isalpha()         # True
"123".isdigit()           # True
```

## F-strings (форматування)

```python
name = "Alice"
age = 25

# F-string
message = f"My name is {name} and I'm {age} years old"

# З виразами
result = f"Next year I'll be {age + 1}"

# Форматування чисел
price = 19.99
formatted = f"Price: ${price:.2f}"  # "Price: $19.99"
```

## Умовні оператори

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade: {grade}")
```

## Логічні оператори

```python
age = 25
has_license = True

# and - обидві умови True
can_drive = age >= 18 and has_license

# or - хоча б одна умова True
is_minor_or_senior = age < 18 or age > 65

# not - інверсія
is_adult = not (age < 18)
```

## Тернарний оператор

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

## Вправи

::: tip Вправа 1
Напишіть програму, яка перевіряє чи є число парним або непарним.
:::

::: tip Вправа 2
Створіть програму для визначення найбільшого з трьох чисел.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_2_Strings_Control_Flow/examples)
