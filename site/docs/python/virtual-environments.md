# Віртуальні середовища

Віртуальні середовища — це ізольовані простори для Python-проєктів, де кожен проєкт має власний набір залежностей. Це критично важливо для QA-автоматизації, де різні проєкти можуть потребувати різних версій бібліотек.

## Навіщо потрібні віртуальні середовища?

Уявіть ситуацію: ви працюєте над двома проєктами автоматизації тестування одночасно.

```python
# Проєкт A — потребує Selenium 4.10
# pip install selenium==4.10.0

# Проєкт B — потребує Selenium 4.20
# pip install selenium==4.20.0

# Без віртуальних середовищ — конфлікт!
# Можна встановити лише одну версію глобально
```

::: warning Проблеми без ізоляції
- **Конфлікти версій** — різні проєкти потребують різних версій однієї бібліотеки
- **Забруднення глобального Python** — десятки непотрібних пакетів у системі
- **Проблеми відтворюваності** — неможливо гарантувати однакове середовище у CI/CD
- **Складність підтримки** — видалення одного пакета може зламати інший проєкт
:::

::: tip Золоте правило
Завжди створюйте окреме віртуальне середовище для кожного проєкту. Ніколи не встановлюйте пакети глобально для робочих проєктів.
:::

## Створення віртуального середовища

Python має вбудований модуль `venv` для створення віртуальних середовищ.

```bash
# Перейдіть у директорію проєкту
cd my-qa-project

# Створіть віртуальне середовище
python -m venv venv
```

```
my-qa-project/
├── venv/                  # Віртуальне середовище
│   ├── bin/               # (Linux/macOS) або Scripts/ (Windows)
│   ├── include/
│   ├── lib/               # Встановлені пакети
│   └── pyvenv.cfg         # Конфігурація середовища
├── tests/
└── requirements.txt
```

::: info Назва середовища
Найпоширеніші назви: `venv`, `.venv`, `env`. Рекомендовано використовувати `venv` або `.venv` — їх легко впізнати та додати до `.gitignore`.
:::

## Активація та деактивація

### Windows

```bash
# Активація (Command Prompt)
venv\Scripts\activate

# Активація (PowerShell)
venv\Scripts\Activate.ps1

# Активація (Git Bash)
source venv/Scripts/activate
```

### macOS / Linux

```bash
# Активація
source venv/bin/activate
```

### Перевірка та деактивація

```bash
# Після активації в терміналі з'явиться префікс:
(venv) $ python --version
Python 3.12.0

# Перевірте, що Python вказує на venv
(venv) $ which python
/home/user/my-qa-project/venv/bin/python

# Деактивація (однаково для всіх ОС)
(venv) $ deactivate
```

::: warning PowerShell Execution Policy
Якщо у Windows PowerShell з'являється помилка при активації, виконайте:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
:::

## Основи pip

`pip` — менеджер пакетів Python, який встановлює бібліотеки з PyPI (Python Package Index).

### Встановлення пакетів

```bash
# Встановити останню версію
pip install pytest

# Встановити конкретну версію
pip install selenium==4.20.0

# Встановити мінімальну версію
pip install playwright>=1.40.0

# Встановити кілька пакетів одразу
pip install pytest selenium allure-pytest
```

### Оновлення та видалення

```bash
# Оновити пакет до останньої версії
pip install --upgrade pytest

# Оновити pip
pip install --upgrade pip

# Видалити пакет
pip uninstall selenium

# Видалити без підтвердження
pip uninstall -y selenium
```

### Перегляд встановлених пакетів

```bash
# Список усіх встановлених пакетів
pip list

# Список у форматі requirements
pip freeze

# Інформація про конкретний пакет
pip show pytest
```

::: tip pip freeze vs pip list
- `pip list` — показує пакети у зручному табличному форматі
- `pip freeze` — виводить у форматі `пакет==версія`, готовому для `requirements.txt`
:::

## requirements.txt

Файл `requirements.txt` фіксує залежності проєкту для відтворення середовища.

### Створення

```bash
# Зберегти всі залежності у файл
pip freeze > requirements.txt
```

```txt
# requirements.txt
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0
allure-pytest==2.13.5
requests==2.31.0
python-dotenv==1.0.1
```

### Встановлення з файлу

```bash
# Встановити всі залежності з файлу
pip install -r requirements.txt
```

::: info Формати версій
```txt
pytest==8.1.1        # Точна версія (рекомендовано)
selenium>=4.20.0     # Мінімальна версія
requests>=2.28,<3.0  # Діапазон версій
playwright~=1.43.0   # Сумісна версія (>=1.43.0, <1.44.0)
```
:::

### Розділення залежностей

```txt
# requirements.txt — основні залежності
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0

# requirements-dev.txt — для розробки
-r requirements.txt
black==24.3.0
flake8==7.0.0
mypy==1.9.0
pre-commit==3.7.0
```

```bash
# Для розробки — встановлює обидва файли
pip install -r requirements-dev.txt
```

## pyproject.toml

Сучасний стандарт конфігурації Python-проєктів, що замінює `setup.py` та `setup.cfg`.

```toml
[project]
name = "qa-automation-project"
version = "1.0.0"
description = "Проєкт автоматизації тестування"
requires-python = ">=3.10"

dependencies = [
    "pytest>=8.0.0",
    "selenium>=4.20.0",
    "playwright>=1.43.0",
    "allure-pytest>=2.13.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "black>=24.0.0",
    "flake8>=7.0.0",
    "mypy>=1.9.0",
    "pre-commit>=3.7.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "smoke: Smoke тести",
    "regression: Регресійні тести",
    "api: API тести",
    "ui: UI тести",
]
addopts = "-v --tb=short"

[tool.black]
line-length = 120

[tool.mypy]
python_version = "3.12"
strict = true
```

```bash
# Встановлення проєкту з pyproject.toml
pip install .

# Встановлення з dev-залежностями
pip install ".[dev]"

# Встановлення в режимі розробки (editable)
pip install -e ".[dev]"
```

::: tip pyproject.toml vs requirements.txt
- **`pyproject.toml`** — для визначення проєкту та його залежностей (рекомендований підхід)
- **`requirements.txt`** — для фіксації точних версій (lock-файл), зручний для CI/CD
- Можна використовувати обидва: `pyproject.toml` для конфігурації + `requirements.txt` для lock-файлу
:::

## Структура QA-проєкту

Типова структура проєкту автоматизації тестування:

```
qa-automation-project/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI/CD pipeline
├── config/
│   ├── __init__.py
│   ├── settings.py             # Налаштування проєкту
│   └── .env                    # Змінні середовища (НЕ в git!)
├── pages/                      # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Фікстури pytest
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── api/
│       ├── __init__.py
│       └── test_users_api.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── api_client.py
├── .gitignore
├── .env.example                # Шаблон змінних середовища
├── pyproject.toml
├── requirements.txt
└── README.md
```

### .gitignore для Python-проєкту

```gitignore
# Віртуальне середовище
venv/
.venv/
env/

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Середовище
.env

# IDE
.idea/
.vscode/
*.code-workspace

# Тестові артефакти
allure-results/
allure-report/
.pytest_cache/
htmlcov/
*.log
screenshots/
```

## Приклади для QA-автоматизації

### Налаштування нового проєкту

```bash
# 1. Створіть директорію проєкту
mkdir qa-automation && cd qa-automation

# 2. Створіть віртуальне середовище
python -m venv venv

# 3. Активуйте його
source venv/bin/activate  # Linux/macOS
# або
venv\Scripts\activate     # Windows

# 4. Оновіть pip
pip install --upgrade pip

# 5. Встановіть залежності для тестування
pip install pytest selenium playwright allure-pytest requests python-dotenv

# 6. Встановіть Playwright-браузери
playwright install

# 7. Збережіть залежності
pip freeze > requirements.txt

# 8. Створіть структуру проєкту
mkdir -p tests pages config utils
touch tests/__init__.py tests/conftest.py
touch pages/__init__.py pages/base_page.py
touch config/__init__.py config/settings.py
touch utils/__init__.py
```

### Конфігурація тестового проєкту

```python
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Конфігурація тестового середовища."""

    BASE_URL = os.getenv("BASE_URL", "https://staging.example.com")
    API_URL = os.getenv("API_URL", "https://api.staging.example.com")

    # Credentials
    ADMIN_USER = os.getenv("ADMIN_USER", "admin@test.com")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Test123!")

    # Timeouts
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30"))

    # Browser
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

settings = Settings()
```

```bash
# .env.example
BASE_URL=https://staging.example.com
API_URL=https://api.staging.example.com
ADMIN_USER=admin@test.com
ADMIN_PASSWORD=Test123!
DEFAULT_TIMEOUT=30
BROWSER=chromium
HEADLESS=true
```

### Управління залежностями для різних середовищ

```txt
# requirements.txt — базові залежності
pytest==8.1.1
selenium==4.20.0
playwright==1.43.0
allure-pytest==2.13.5
requests==2.31.0
python-dotenv==1.0.1

# requirements-ci.txt — додаткові для CI/CD
-r requirements.txt
pytest-xdist==3.5.0       # Паралельний запуск тестів
pytest-rerunfailures==14.0 # Перезапуск нестабільних тестів
pytest-timeout==2.3.1      # Таймаути для тестів
```

### CI/CD — GitHub Actions

```yaml
# .github/workflows/tests.yml
name: Run Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Create virtual environment
        run: python -m venv venv

      - name: Install dependencies
        run: |
          source venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements-ci.txt

      - name: Install Playwright browsers
        run: |
          source venv/bin/activate
          playwright install --with-deps chromium

      - name: Run tests
        run: |
          source venv/bin/activate
          pytest tests/ -v --alluredir=allure-results
        env:
          BASE_URL: ${{ secrets.BASE_URL }}
          ADMIN_USER: ${{ secrets.ADMIN_USER }}
          ADMIN_PASSWORD: ${{ secrets.ADMIN_PASSWORD }}
          HEADLESS: "true"

      - name: Upload Allure results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: allure-results
          path: allure-results/
```

::: warning Безпека у CI/CD
- **Ніколи** не зберігайте паролі та токени у коді або `requirements.txt`
- Використовуйте **GitHub Secrets** для чутливих даних
- Файл `.env` має бути у `.gitignore`
- Створіть `.env.example` як шаблон без реальних значень
:::

### conftest.py з фікстурами

```python
# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from config.settings import settings


@pytest.fixture(scope="session")
def browser():
    """Запускає браузер на весь тестовий сеанс."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=settings.HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Створює нову сторінку для кожного тесту."""
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(settings.DEFAULT_TIMEOUT * 1000)
    yield page
    context.close()


@pytest.fixture
def authenticated_page(page):
    """Сторінка з авторизованим користувачем."""
    page.goto(f"{settings.BASE_URL}/login")
    page.fill("[data-testid='email']", settings.ADMIN_USER)
    page.fill("[data-testid='password']", settings.ADMIN_PASSWORD)
    page.click("[data-testid='login-button']")
    page.wait_for_url(f"{settings.BASE_URL}/dashboard")
    return page
```

## Корисні посилання

- [Офіційна документація venv](https://docs.python.org/3/library/venv.html)
- [pip — User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [PEP 621 — pyproject.toml](https://peps.python.org/pep-0621/)
- [Python Packaging Guide](https://packaging.python.org/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/api-requests">← Робота з API</a>
  <a href="/python_automation_courses/docs/python/best-practices">Best Practices →</a>
</div>
