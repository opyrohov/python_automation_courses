# Lecture 7: File Handling & JSON

Робота з файлами та JSON в Python.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_7_File_Handling_JSON/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_7_File_Handling_JSON/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_7_File_Handling_JSON/exercises)

</div>

## Теми лекції

- Читання та запис файлів
- Context manager (with)
- Робота з JSON
- Робота з CSV

## Читання файлів

```python
# Читання всього файлу
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Читання рядок за рядком
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Читання всіх рядків у список
with open("file.txt", "r") as f:
    lines = f.readlines()
```

## Запис файлів

```python
# Запис (перезаписує файл)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# Додавання до файлу
with open("output.txt", "a") as f:
    f.write("New line\n")

# Запис списку рядків
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

## JSON

```python
import json

# Читання JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Запис JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# JSON рядок
json_str = json.dumps({"name": "John"})
data = json.loads('{"name": "John"}')
```

## Path (pathlib)

```python
from pathlib import Path

# Створення шляху
path = Path("data/users.json")

# Перевірки
path.exists()
path.is_file()
path.is_dir()

# Читання/запис
content = path.read_text()
path.write_text("content")

# Створення директорій
Path("data/reports").mkdir(parents=True, exist_ok=True)
```
