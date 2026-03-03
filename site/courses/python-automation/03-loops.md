# Лекція 3: Цикли

Цикли в Python — for та while.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_3_Loops/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Цикл `for`
- Цикл `while`
- `break` та `continue`
- `range()` функція
- Вкладені цикли

## Цикл for

```python
# Ітерація по списку
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Ітерація по рядку
for char in "Hello":
    print(char)

# З enumerate (індекс + значення)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## range() функція

```python
# range(stop)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(2, 5):  # 2, 3, 4
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Зворотній порядок
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(i)
```

## Цикл while

```python
count = 0
while count < 5:
    print(count)
    count += 1

# while з умовою виходу
while True:
    answer = input("Continue? (y/n): ")
    if answer == "n":
        break
```

## break та continue

```python
# break - вихід з циклу
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - пропуск ітерації
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

## else в циклах

```python
# else виконується якщо цикл завершився без break
for i in range(5):
    if i == 10:  # ніколи не True
        break
else:
    print("Цикл завершився нормально")
```

## Вкладені цикли

```python
# Таблиця множення
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
```

## List Comprehension

```python
# Звичайний цикл
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]

# З умовою
evens = [x for x in range(10) if x % 2 == 0]

# Вкладений
matrix = [[i * j for j in range(3)] for i in range(3)]
```

## Вправи

::: tip Вправа 1
Напишіть програму для виведення таблиці множення від 1 до 10.
:::

::: tip Вправа 2
Знайдіть суму всіх чисел від 1 до 100, які діляться на 3 або 5.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/examples)
