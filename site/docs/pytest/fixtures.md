# Fixtures

Фікстури в pytest — механізм підготовки та очищення тестового оточення.

## Базова фікстура

```python
import pytest

@pytest.fixture
def user_data():
    """Повертає тестові дані користувача."""
    return {
        "name": "John Doe",
        "email": "john@test.com",
        "password": "SecurePass123"
    }

def test_login(user_data):
    assert user_data["email"] == "john@test.com"
    assert len(user_data["password"]) >= 8
```

## Scope фікстур

```python
# function — для кожного тесту (за замовчуванням)
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# class — один раз на клас
@pytest.fixture(scope="class")
def api_client():
    client = APIClient(base_url="https://api.example.com")
    yield client
    client.close()

# module — один раз на файл
@pytest.fixture(scope="module")
def database():
    db = Database.connect("test_db")
    yield db
    db.disconnect()

# session — один раз на весь запуск
@pytest.fixture(scope="session")
def browser():
    browser = playwright.chromium.launch()
    yield browser
    browser.close()
```

::: warning Порядок scope
`session` > `module` > `class` > `function`

Фікстура з вужчим scope не може залежати від фікстури з ширшим scope у зворотному напрямку.
:::

## yield — Setup та Teardown

```python
@pytest.fixture
def authenticated_page(page):
    # SETUP — виконується перед тестом
    page.goto("/login")
    page.fill("#email", "user@test.com")
    page.fill("#password", "password123")
    page.click("#submit")
    page.wait_for_url("**/dashboard")

    yield page  # Передаємо в тест

    # TEARDOWN — виконується після тесту
    page.goto("/logout")
    page.wait_for_url("**/login")
```

## conftest.py

Файл `conftest.py` — автоматично доступний для всіх тестів у директорії.

```python
# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def base_url():
    return "https://staging.example.com"
```

## Фабричні фікстури

```python
@pytest.fixture
def create_user():
    """Фабрика для створення користувачів."""
    created_users = []

    def _create_user(name: str = "Test User", role: str = "tester"):
        user = {"name": name, "role": role, "id": len(created_users) + 1}
        created_users.append(user)
        return user

    yield _create_user

    # Очищення всіх створених користувачів
    for user in created_users:
        print(f"Видалення користувача: {user['name']}")

def test_multiple_users(create_user):
    admin = create_user("Admin", "admin")
    tester = create_user("Tester", "tester")
    assert admin["role"] == "admin"
    assert tester["role"] == "tester"
```

## autouse

```python
@pytest.fixture(autouse=True)
def log_test_name(request):
    """Автоматично логує назву кожного тесту."""
    print(f"\n▶ Запуск: {request.node.name}")
    yield
    print(f"✓ Завершено: {request.node.name}")

# Автоматичне очищення cookies
@pytest.fixture(autouse=True)
def clear_cookies(page):
    yield
    page.context.clear_cookies()
```

## Вбудовані фікстури

```python
# tmp_path — тимчасова директорія
def test_save_report(tmp_path):
    report_file = tmp_path / "report.json"
    report_file.write_text('{"status": "passed"}')
    assert report_file.exists()

# request — інформація про тест
@pytest.fixture
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")

# capsys — перехоплення stdout/stderr
def test_output(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

# monkeypatch — підміна значень
def test_env_variable(monkeypatch):
    monkeypatch.setenv("BASE_URL", "https://test.example.com")
    import os
    assert os.getenv("BASE_URL") == "https://test.example.com"
```

## Корисні посилання

- [Документація: Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Документація: conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html)
