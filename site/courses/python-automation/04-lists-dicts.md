# Лекція 4: Списки та словники

Колекції даних в Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_4_Lists_Dictionaries/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Списки (lists)
- Методи списків
- Словники (dictionaries)
- Методи словників
- Кортежі та множини

## Списки (Lists)

```python
# Створення
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []

# Доступ за індексом
first = fruits[0]    # "apple"
last = fruits[-1]    # "cherry"

# Slice
subset = fruits[0:2]  # ["apple", "banana"]
```

## Методи списків

```python
fruits = ["apple", "banana"]

# Додавання
fruits.append("cherry")        # ["apple", "banana", "cherry"]
fruits.insert(1, "orange")     # ["apple", "orange", "banana", "cherry"]
fruits.extend(["grape", "kiwi"])

# Видалення
fruits.remove("banana")        # видаляє перше входження
popped = fruits.pop()          # видаляє і повертає останній
del fruits[0]                  # видаляє за індексом
fruits.clear()                 # очищує список

# Пошук
index = fruits.index("apple")  # індекс елемента
count = fruits.count("apple")  # кількість входжень
exists = "apple" in fruits     # True/False

# Сортування
numbers.sort()                 # сортує на місці
numbers.sort(reverse=True)     # зворотній порядок
sorted_list = sorted(numbers)  # повертає новий список

# Інші
numbers.reverse()              # розвертає список
length = len(numbers)          # довжина
```

## Словники (Dictionaries)

```python
# Створення
user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Доступ
name = user["name"]           # KeyError якщо немає
name = user.get("name")       # None якщо немає
name = user.get("name", "N/A") # default значення

# Зміна/Додавання
user["age"] = 31
user["phone"] = "123-456"

# Видалення
del user["phone"]
age = user.pop("age")
```

## Методи словників

```python
user = {"name": "John", "age": 30}

# Ключі, значення, пари
keys = user.keys()       # dict_keys(['name', 'age'])
values = user.values()   # dict_values(['John', 30])
items = user.items()     # dict_items([('name', 'John'), ('age', 30)])

# Ітерація
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key}: {value}")

# Перевірка
"name" in user           # True
"email" in user          # False

# Оновлення
user.update({"age": 31, "city": "NYC"})

# Копіювання
user_copy = user.copy()
```

## Кортежі (Tuples)

```python
# Незмінювана послідовність
point = (10, 20)
single = (42,)  # кома обов'язкова для одного елемента

# Unpacking
x, y = point

# Як ключі словника (бо незмінні)
locations = {
    (0, 0): "origin",
    (1, 0): "right"
}
```

## Множини (Sets)

```python
# Унікальні елементи
numbers = {1, 2, 3, 3, 2, 1}  # {1, 2, 3}

# Операції
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # union: {1, 2, 3, 4}
a & b  # intersection: {2, 3}
a - b  # difference: {1}
a ^ b  # symmetric difference: {1, 4}
```

## Вправи

::: tip Вправа 1
Створіть словник з інформацією про 3 книги (назва, автор, рік).
:::

::: tip Вправа 2
Напишіть функцію для підрахунку частоти слів у тексті.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/examples)
