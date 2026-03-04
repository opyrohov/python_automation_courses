# Робота з файлами

Читання, запис та обробка файлів у Python — важлива навичка для QA-автоматизації. Ця сторінка охоплює роботу з текстовими файлами, CSV, JSON та шляхами до файлів.

## Відкриття файлів: open()

Функція `open()` — основний спосіб роботи з файлами в Python.

```python
# Базове відкриття файлу
file = open("data.txt", "r")
content = file.read()
file.close()  # Обов'язково закрити файл!
```

::: warning Завжди закривайте файли!
Якщо не закрити файл, можливі витоки пам'яті та блокування файлу. Використовуйте `with` для автоматичного закриття.
:::

### Контекстний менеджер (with)

Рекомендований спосіб роботи з файлами — оператор `with`. Файл автоматично закривається після виходу з блоку.

```python
# Рекомендований спосіб — файл закриється автоматично
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Після виходу з блоку with файл вже закритий
print(file.closed)  # True
```

::: tip Правило
Завжди використовуйте `with open(...)` замість `open()` + `close()`. Це безпечніше та чистіше.
:::

## Режими відкриття файлів

| Режим | Опис | Файл існує | Файл не існує |
|-------|------|------------|---------------|
| `"r"` | Читання (за замовчуванням) | Читає | `FileNotFoundError` |
| `"w"` | Запис (перезаписує) | Перезаписує | Створює новий |
| `"a"` | Додавання в кінець | Додає | Створює новий |
| `"r+"` | Читання + запис | Читає/пише | `FileNotFoundError` |
| `"x"` | Ексклюзивне створення | `FileExistsError` | Створює новий |
| `"b"` | Бінарний режим (додається до інших) | — | — |

```python
# Комбінації режимів
with open("image.png", "rb") as f:    # Читання бінарного файлу
    data = f.read()

with open("output.bin", "wb") as f:   # Запис бінарного файлу
    f.write(data)
```

## Читання файлів

### read() — весь вміст

```python
with open("test_data.txt", "r", encoding="utf-8") as file:
    content = file.read()       # Весь вміст як один рядок
    print(content)

# Часткове читання
with open("large_file.txt", "r") as file:
    chunk = file.read(100)      # Перші 100 символів
```

### readline() — один рядок

```python
with open("test_data.txt", "r") as file:
    first_line = file.readline()    # Перший рядок
    second_line = file.readline()   # Другий рядок
    print(first_line.strip())       # .strip() видаляє \n
```

### readlines() — список рядків

```python
with open("test_data.txt", "r") as file:
    lines = file.readlines()        # Список усіх рядків
    print(lines)                    # ['рядок 1\n', 'рядок 2\n', ...]

# Видалення символів нового рядка
with open("test_data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    print(lines)                    # ['рядок 1', 'рядок 2', ...]
```

### Ітерація по файлу

```python
# Найефективніший спосіб для великих файлів
with open("server.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
```

::: info Приклад для QA: пошук помилок у логах
```python
def find_errors_in_log(log_path):
    """Знаходить всі рядки з помилками у лог-файлі."""
    errors = []
    with open(log_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            if "ERROR" in line or "CRITICAL" in line:
                errors.append(f"Line {line_num}: {line.strip()}")
    return errors

# Використання
errors = find_errors_in_log("app.log")
for error in errors:
    print(error)
```
:::

## Запис у файли

### write() — запис рядка

```python
# Запис (перезапис файлу)
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Звіт тестування\n")
    file.write("=" * 30 + "\n")
    file.write(f"Дата: 2024-01-15\n")
```

### writelines() — запис списку рядків

```python
lines = ["Тест 1: PASSED\n", "Тест 2: FAILED\n", "Тест 3: PASSED\n"]

with open("results.txt", "w") as file:
    file.writelines(lines)    # Записує всі рядки без додавання \n
```

::: warning writelines() не додає перенос рядка
На відміну від `readlines()`, метод `writelines()` НЕ додає `\n` автоматично. Додавайте його самостійно.
:::

### Додавання в кінець файлу (append)

```python
# Режим "a" — додає в кінець, не перезаписує
with open("test.log", "a", encoding="utf-8") as file:
    file.write("[2024-01-15 10:30:00] Test started\n")
    file.write("[2024-01-15 10:30:05] Test passed\n")
```

::: info Приклад для QA: запис звіту тестування
```python
def write_test_report(results, report_path="test_report.txt"):
    """Створює текстовий звіт з результатами тестів."""
    passed = sum(1 for r in results if r["status"] == "PASSED")
    failed = sum(1 for r in results if r["status"] == "FAILED")
    total = len(results)

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write("        ЗВІТ ТЕСТУВАННЯ\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Всього тестів: {total}\n")
        file.write(f"Пройшло:       {passed}\n")
        file.write(f"Провалено:     {failed}\n")
        file.write(f"Успішність:    {passed/total*100:.1f}%\n\n")

        file.write("-" * 50 + "\n")
        for r in results:
            status = "✓" if r["status"] == "PASSED" else "✗"
            file.write(f"  {status} {r['name']} — {r['status']}\n")

# Використання
results = [
    {"name": "test_login", "status": "PASSED"},
    {"name": "test_logout", "status": "PASSED"},
    {"name": "test_register", "status": "FAILED"},
]
write_test_report(results)
```
:::

## Робота зі шляхами: os.path

Модуль `os.path` — класичний спосіб роботи з файловими шляхами.

```python
import os

# Побудова шляхів (кросплатформно)
path = os.path.join("tests", "data", "users.json")
# Windows: tests\data\users.json
# Linux:   tests/data/users.json

# Корисні функції
print(os.path.exists("config.json"))    # True/False — чи існує файл
print(os.path.isfile("config.json"))    # True/False — чи це файл
print(os.path.isdir("tests"))           # True/False — чи це директорія
print(os.path.basename("/home/user/test.py"))  # "test.py"
print(os.path.dirname("/home/user/test.py"))   # "/home/user"
print(os.path.splitext("report.html"))         # ("report", ".html")
print(os.path.abspath("data.txt"))             # Повний шлях

# Поточна директорія
print(os.getcwd())                      # Поточна робоча директорія
```

## Робота зі шляхами: pathlib.Path

Модуль `pathlib` — сучасний та зручніший спосіб роботи зі шляхами (Python 3.4+).

```python
from pathlib import Path

# Створення шляхів
path = Path("tests") / "data" / "users.json"
print(path)  # tests/data/users.json

# Властивості шляху
print(path.name)       # "users.json"
print(path.stem)       # "users"
print(path.suffix)     # ".json"
print(path.parent)     # tests/data
print(path.exists())   # True/False
print(path.is_file())  # True/False
print(path.is_dir())   # False

# Читання та запис через Path
content = Path("data.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("Hello!", encoding="utf-8")

# Пошук файлів
for py_file in Path("tests").glob("*.py"):
    print(py_file)

# Рекурсивний пошук
for json_file in Path("project").rglob("*.json"):
    print(json_file)
```

::: tip pathlib vs os.path
Рекомендовано використовувати `pathlib.Path` у нових проєктах. Він більш читабельний та підтримує оператор `/` для побудови шляхів.
:::

::: info Приклад для QA: пошук тестових файлів
```python
from pathlib import Path

def find_test_files(test_dir="tests"):
    """Знаходить усі тестові файли у директорії."""
    test_path = Path(test_dir)
    if not test_path.exists():
        print(f"Директорія {test_dir} не знайдена")
        return []

    test_files = list(test_path.rglob("test_*.py"))
    print(f"Знайдено {len(test_files)} тестових файлів:")
    for f in test_files:
        print(f"  - {f}")
    return test_files

find_test_files()
```
:::

## Робота з CSV

Модуль `csv` дозволяє читати та записувати CSV-файли (Comma-Separated Values).

### Читання CSV

```python
import csv

# Читання як список рядків
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)       # Перший рядок — заголовки
    for row in reader:
        print(row)              # ['John', '25', 'admin']

# Читання як словники
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])  # Доступ за іменем колонки
```

### Запис CSV

```python
import csv

# Запис списків
with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["test_name", "status", "duration"])    # Заголовок
    writer.writerow(["test_login", "PASSED", "1.23"])
    writer.writerow(["test_register", "FAILED", "3.45"])

# Запис словників
with open("results.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["test_name", "status", "duration"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"test_name": "test_login", "status": "PASSED", "duration": "1.23"})
```

::: warning Параметр newline=""
При записі CSV на Windows завжди вказуйте `newline=""`, щоб уникнути подвійних порожніх рядків.
:::

::: info Приклад для QA: завантаження тестових даних з CSV
```python
import csv

def load_test_data(csv_path):
    """Завантажує тестові дані з CSV для параметризованих тестів."""
    test_data = []
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(row)
    return test_data

# Файл test_users.csv:
# username,password,expected_result
# admin,Admin123!,success
# user,wrong_pass,failure
# ,empty_pass,failure

test_cases = load_test_data("test_users.csv")
for case in test_cases:
    print(f"Login: {case['username']} | Expected: {case['expected_result']}")

# Використання з pytest parametrize
import pytest

def get_login_data():
    return load_test_data("test_users.csv")

@pytest.mark.parametrize("test_data", get_login_data())
def test_login(test_data):
    username = test_data["username"]
    password = test_data["password"]
    expected = test_data["expected_result"]
    # ... виконання тесту
```
:::

## Робота з JSON

Модуль `json` дозволяє працювати з форматом JSON — найпоширенішим форматом обміну даними в API.

### Читання JSON з файлу

```python
import json

# json.load() — читання з файлу
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
    print(config["base_url"])
    print(config["timeout"])
```

### Запис JSON у файл

```python
import json

data = {
    "base_url": "https://example.com",
    "timeout": 30,
    "users": [
        {"name": "admin", "role": "admin"},
        {"name": "user1", "role": "viewer"}
    ]
}

# json.dump() — запис у файл
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
```

### Робота з JSON-рядками

```python
import json

# json.loads() — парсинг рядка (string → dict/list)
json_string = '{"name": "Test", "passed": true, "score": 95.5}'
data = json.loads(json_string)
print(data["name"])     # "Test"
print(data["passed"])   # True (Python bool)

# json.dumps() — серіалізація (dict/list → string)
result = {"status": "ok", "count": 42}
json_string = json.dumps(result, indent=2)
print(json_string)
```

::: tip load vs loads, dump vs dumps
- `json.load()` / `json.dump()` — працюють з **файлами**
- `json.loads()` / `json.dumps()` — працюють з **рядками** (s = string)
:::

::: info Приклад для QA: завантаження конфігурації з JSON
```python
import json
from pathlib import Path

def load_config(config_path="config.json"):
    """Завантажує конфігурацію тестового середовища."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл конфігурації {config_path} не знайдено")

    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    # Валідація обов'язкових полів
    required_fields = ["base_url", "timeout", "browser"]
    for field in required_fields:
        if field not in config:
            raise KeyError(f"Відсутнє обов'язкове поле: {field}")

    return config

# config.json:
# {
#     "base_url": "https://staging.example.com",
#     "timeout": 30,
#     "browser": "chromium",
#     "headless": true
# }

config = load_config()
print(f"URL: {config['base_url']}")
print(f"Browser: {config['browser']}")
```
:::

::: info Приклад для QA: збереження результатів тестів у JSON
```python
import json
from datetime import datetime

def save_test_results(results, output_path="test_results.json"):
    """Зберігає результати тестів у JSON-файл."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "PASSED"),
        "failed": sum(1 for r in results if r["status"] == "FAILED"),
        "results": results
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"Результати збережено у {output_path}")

# Використання
results = [
    {"name": "test_login", "status": "PASSED", "duration": 1.23},
    {"name": "test_register", "status": "FAILED", "duration": 3.45,
     "error": "Element not found: #submit-btn"},
    {"name": "test_search", "status": "PASSED", "duration": 2.10},
]
save_test_results(results)
```
:::

## Обробка помилок при роботі з файлами

```python
from pathlib import Path

# Перевірка існування файлу
path = Path("config.json")
if not path.exists():
    print("Файл не знайдено!")

# try/except для обробки помилок
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
except PermissionError:
    print("Немає доступу до файлу!")
except UnicodeDecodeError:
    print("Помилка кодування — спробуйте інший encoding")
except Exception as e:
    print(f"Непередбачена помилка: {e}")
```

::: warning Кодування (encoding)
Завжди вказуйте `encoding="utf-8"` при роботі з текстовими файлами. Без цього Python використовує системне кодування, що може призвести до помилок на різних ОС.
```python
# Правильно
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Небезпечно — кодування залежить від системи
with open("data.txt", "r") as f:
    content = f.read()
```
:::

## Корисні посилання

- [Документація Python: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Документація Python: модуль csv](https://docs.python.org/3/library/csv.html)
- [Документація Python: модуль json](https://docs.python.org/3/library/json.html)
- [Документація Python: pathlib](https://docs.python.org/3/library/pathlib.html)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/modules">← Модулі</a>
  <a href="/python_automation_courses/docs/python/decorators">Декоратори →</a>
</div>
