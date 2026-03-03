# Lecture 6: Modules & Imports

Модулі та імпорти в Python.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_6_Modules_Imports/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/exercises)

</div>

## Теми лекції

- Імпорт модулів
- Створення власних модулів
- Пакети
- Віртуальні середовища
- pip та requirements.txt

## Імпорт модулів

```python
# Імпорт всього модуля
import math
result = math.sqrt(16)  # 4.0

# Імпорт з псевдонімом
import numpy as np
arr = np.array([1, 2, 3])

# Імпорт конкретних функцій
from math import sqrt, pi
result = sqrt(16)

# Імпорт всього (не рекомендується)
from math import *
```

## Стандартні модулі

```python
# os - робота з ОС
import os
current_dir = os.getcwd()
os.makedirs("new_folder", exist_ok=True)
files = os.listdir(".")

# datetime - дати та час
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)

# json - робота з JSON
import json
data = json.loads('{"name": "John"}')
text = json.dumps(data, indent=2)

# random - випадкові числа
import random
random.randint(1, 10)
random.choice(["a", "b", "c"])
random.shuffle(my_list)

# re - регулярні вирази
import re
pattern = r"\d+"
matches = re.findall(pattern, "abc123def456")
```

## Створення модуля

```python
# my_module.py
"""Мій власний модуль."""

PI = 3.14159

def greet(name: str) -> str:
    """Привітання."""
    return f"Hello, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b

# Використання
# main.py
from my_module import greet, Calculator

print(greet("World"))
calc = Calculator()
```

## Пакети

```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# __init__.py
from .module1 import function1
from .module2 import function2

# Використання
from my_package import function1
from my_package.subpackage import module3
```

## Віртуальні середовища

```bash
# Створення
python -m venv venv

# Активація (Windows)
venv\Scripts\activate

# Активація (Linux/Mac)
source venv/bin/activate

# Деактивація
deactivate
```

## pip та requirements.txt

```bash
# Встановлення пакету
pip install requests

# Встановлення конкретної версії
pip install requests==2.28.0

# Список встановлених
pip list
pip freeze

# Збереження залежностей
pip freeze > requirements.txt

# Встановлення з файлу
pip install -r requirements.txt
```

## requirements.txt

```txt
requests==2.28.0
playwright>=1.40.0
pytest>=7.0.0
python-dotenv~=1.0.0
```

## if __name__ == "__main__"

```python
# my_module.py
def main():
    print("Running as main script")

def helper():
    print("Helper function")

# Виконується тільки при прямому запуску
if __name__ == "__main__":
    main()
```

## Вправи

::: tip Вправа 1
Створіть модуль з функціями для роботи з рядками.
:::

::: tip Вправа 2
Організуйте код в пакет з підмодулями.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/examples)
