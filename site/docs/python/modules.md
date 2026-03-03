# Модулі

Модулі та пакети в Python — організація коду, імпорти та віртуальні середовища.

## Імпорт модулів

```python
# Імпорт цілого модуля
import os
import json

# Імпорт конкретних об'єктів
from pathlib import Path
from typing import Optional, List

# Імпорт з псевдонімом
import datetime as dt
from collections import defaultdict as dd

# Імпорт всього (не рекомендовано)
from os.path import *
```

::: warning Уникайте import *
`from module import *` імпортує все з модуля, що може призвести до конфліктів імен. Завжди імпортуйте конкретні об'єкти.
:::

## Створення модулів

```python
# utils/helpers.py
"""Допоміжні функції для тестів."""

def generate_email(name: str) -> str:
    """Генерує тестовий email."""
    return f"{name.lower()}@test.com"

def generate_password(length: int = 12) -> str:
    """Генерує випадковий пароль."""
    import string
    import random
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choices(chars, k=length))

# Константи
DEFAULT_TIMEOUT = 30000
BASE_URL = "https://example.com"
```

```python
# Використання в іншому файлі
from utils.helpers import generate_email, generate_password, DEFAULT_TIMEOUT

email = generate_email("john")  # john@test.com
password = generate_password()  # випадковий пароль
```

## Пакети

Пакет — це директорія з файлом `__init__.py`.

```
project/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   └── test_signup.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_generator.py
│   └── constants.py
└── conftest.py
```

```python
# pages/__init__.py — експорт основних класів
from .base_page import BasePage
from .login_page import LoginPage
from .dashboard_page import DashboardPage

__all__ = ["BasePage", "LoginPage", "DashboardPage"]
```

```python
# Тепер можна імпортувати напряму з пакету
from pages import LoginPage, DashboardPage
```

## Стандартна бібліотека

### os та pathlib

```python
import os
from pathlib import Path

# Робота з шляхами (рекомендовано pathlib)
project_root = Path(__file__).parent.parent
config_path = project_root / "config" / "settings.json"
screenshots_dir = project_root / "screenshots"

# Створення директорії
screenshots_dir.mkdir(parents=True, exist_ok=True)

# Перевірка існування
if config_path.exists():
    print("Конфіг знайдено")

# Змінні оточення
base_url = os.getenv("BASE_URL", "https://localhost:3000")
api_key = os.environ.get("API_KEY")
```

### json

```python
import json

# Читання JSON
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Запис JSON
data = {"users": [{"name": "John", "role": "QA"}]}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Робота з рядками
json_str = json.dumps(data, indent=2)
parsed = json.loads(json_str)
```

### datetime

```python
from datetime import datetime, timedelta

# Поточний час
now = datetime.now()
utc_now = datetime.utcnow()

# Форматування
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
# "2024-01-15_14-30-45"

# Парсинг
date = datetime.strptime("2024-01-15", "%Y-%m-%d")

# Арифметика
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
```

### logging

```python
import logging

# Налаштування логера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("test_run.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("tests")

# Використання
logger.info("Тест запущено")
logger.warning("Елемент не знайдено, повторна спроба")
logger.error("Тест провалено: %s", error_message)
```

## Віртуальні середовища

```bash
# Створення віртуального середовища
python -m venv venv

# Активація
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Встановлення залежностей
pip install playwright pytest

# Збереження залежностей
pip freeze > requirements.txt

# Встановлення з файлу
pip install -r requirements.txt

# Деактивація
deactivate
```

::: tip requirements.txt для QA проєкту
```txt
playwright==1.40.0
pytest==7.4.3
pytest-playwright==0.4.3
pytest-html==4.1.1
pytest-xdist==3.5.0
allure-pytest==2.13.2
python-dotenv==1.0.0
```
:::

## Корисні посилання

- [Документація: Модулі](https://docs.python.org/3/tutorial/modules.html)
- [Документація: venv](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
