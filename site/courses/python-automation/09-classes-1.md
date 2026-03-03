# Lecture 9: Classes & Objects Part 1

Основи об'єктно-орієнтованого програмування.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_9_Classes_Objects_Part1/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_9_Classes_Objects_Part1/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_9_Classes_Objects_Part1/exercises)

</div>

## Теми лекції

- Класи та об'єкти
- Атрибути та методи
- Конструктор `__init__`
- self

## Базовий клас

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, I'm {self.name}"

# Створення об'єкта
user = User("Alice", "alice@example.com")
print(user.greet())
```

## Атрибути класу vs екземпляра

```python
class Counter:
    count = 0  # Атрибут класу

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # Атрибут екземпляра

c1 = Counter()  # count = 1
c2 = Counter()  # count = 2
print(Counter.count)  # 2
```

## Методи

```python
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self  # Для chaining

    def multiply(self, x):
        self.value *= x
        return self

calc = Calculator(10)
calc.add(5).multiply(2)  # 30
```
