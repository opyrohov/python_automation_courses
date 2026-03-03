# Параметризація

Data-driven тестування з `@pytest.mark.parametrize` — запуск одного тесту з різними наборами даних.

## Базова параметризація

```python
import pytest

@pytest.mark.parametrize("input_value,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input_value, expected):
    assert input_value ** 2 == expected
```

## Ідентифікатори тестів (ids)

```python
# Автоматичні ids
@pytest.mark.parametrize("url,status_code", [
    ("https://example.com", 200),
    ("https://example.com/404", 404),
    ("https://example.com/error", 500),
])
def test_status_codes(url, status_code):
    pass
# Згенерує: test_status_codes[url0-200], test_status_codes[url1-404], ...

# Кастомні ids
@pytest.mark.parametrize("url,status_code", [
    ("https://example.com", 200),
    ("https://example.com/404", 404),
    ("https://example.com/error", 500),
], ids=["homepage", "not_found", "server_error"])
def test_status_codes(url, status_code):
    pass
# Згенерує: test_status_codes[homepage], test_status_codes[not_found], ...
```

## pytest.param

```python
@pytest.mark.parametrize("browser", [
    pytest.param("chromium", id="chrome"),
    pytest.param("firefox", id="ff"),
    pytest.param("webkit", id="safari", marks=pytest.mark.slow),
])
def test_cross_browser(browser):
    pass

# Позначити конкретний набір як xfail
@pytest.mark.parametrize("email,password,expected", [
    pytest.param("user@test.com", "Pass123", True, id="valid"),
    pytest.param("", "Pass123", False, id="empty_email"),
    pytest.param(
        "user@test.com", "", False,
        id="empty_password",
        marks=pytest.mark.xfail(reason="Bug #456")
    ),
])
def test_login(email, password, expected):
    pass
```

## Множинна параметризація

```python
# Декартовий добуток — всі комбінації
@pytest.mark.parametrize("browser", ["chromium", "firefox"])
@pytest.mark.parametrize("viewport", ["desktop", "mobile"])
def test_responsive(browser, viewport):
    pass
# Згенерує 4 тести:
# test_responsive[desktop-chromium]
# test_responsive[desktop-firefox]
# test_responsive[mobile-chromium]
# test_responsive[mobile-firefox]
```

## indirect — параметризація фікстур

```python
@pytest.fixture
def user(request):
    """Створює користувача за роллю."""
    role = request.param
    users = {
        "admin": {"name": "Admin", "role": "admin", "permissions": ["all"]},
        "viewer": {"name": "Viewer", "role": "viewer", "permissions": ["read"]},
    }
    return users[role]

@pytest.mark.parametrize("user", ["admin", "viewer"], indirect=True)
def test_user_permissions(user):
    if user["role"] == "admin":
        assert "all" in user["permissions"]
    else:
        assert "read" in user["permissions"]
```

## Дані з зовнішніх джерел

### JSON

```python
import json

def load_test_data(filename: str) -> list:
    with open(f"test_data/{filename}", "r") as f:
        return json.load(f)

@pytest.mark.parametrize(
    "user_data",
    load_test_data("users.json"),
    ids=lambda d: d.get("name", "unknown")
)
def test_create_user(user_data):
    assert "name" in user_data
    assert "email" in user_data
```

### CSV

```python
import csv

def load_csv_data(filename: str) -> list[tuple]:
    with open(f"test_data/{filename}", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Пропустити заголовок
        return [tuple(row) for row in reader]

@pytest.mark.parametrize(
    "email,password,expected_result",
    load_csv_data("login_data.csv")
)
def test_login_from_csv(email, password, expected_result):
    pass
```

::: tip Організація тестових даних
```
test_data/
├── users.json
├── login_data.csv
├── products.json
└── api_payloads/
    ├── create_order.json
    └── update_profile.json
```
:::

## Параметризація класу

```python
@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
class TestCrossBrowser:
    def test_homepage(self, browser_name):
        pass

    def test_login(self, browser_name):
        pass

    def test_search(self, browser_name):
        pass
# Згенерує 9 тестів (3 методи × 3 браузери)
```

## Корисні посилання

- [Документація: Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Документація: pytest.param](https://docs.pytest.org/en/stable/reference/reference.html#pytest-param)
