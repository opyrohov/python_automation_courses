# Робота з API

Бібліотека `requests` — найпопулярніший інструмент для роботи з HTTP-запитами в Python. Ця сторінка охоплює все необхідне для тестування REST API: від базових запитів до просунутих патернів автоматизації.

## Встановлення

```python
pip install requests
```

```python
import requests
```

::: tip Перевірка встановлення
```python
import requests
print(requests.__version__)  # Наприклад: 2.31.0
```
:::

## HTTP-методи

### GET — отримання даних

```python
import requests

response = requests.get("https://api.example.com/users")
print(response.status_code)  # 200
print(response.json())       # [{"id": 1, "name": "John"}, ...]
```

### POST — створення ресурсу

```python
payload = {"name": "Test User", "email": "test@example.com"}

response = requests.post(
    "https://api.example.com/users",
    json=payload
)
print(response.status_code)  # 201
print(response.json())       # {"id": 42, "name": "Test User", ...}
```

### PUT — повна заміна ресурсу

```python
updated_data = {"name": "Updated User", "email": "updated@example.com"}

response = requests.put(
    "https://api.example.com/users/42",
    json=updated_data
)
print(response.status_code)  # 200
```

### PATCH — часткове оновлення

```python
partial_data = {"email": "new_email@example.com"}

response = requests.patch(
    "https://api.example.com/users/42",
    json=partial_data
)
print(response.status_code)  # 200
```

### DELETE — видалення ресурсу

```python
response = requests.delete("https://api.example.com/users/42")
print(response.status_code)  # 204
```

::: info Приклад для QA: CRUD-тестування
```python
# Повний цикл CRUD-тестування
base_url = "https://api.example.com/users"

# Create
new_user = {"name": "QA Test", "email": "qa@test.com"}
create_resp = requests.post(base_url, json=new_user)
assert create_resp.status_code == 201
user_id = create_resp.json()["id"]

# Read
get_resp = requests.get(f"{base_url}/{user_id}")
assert get_resp.status_code == 200
assert get_resp.json()["name"] == "QA Test"

# Update
update_resp = requests.put(f"{base_url}/{user_id}", json={"name": "Updated", "email": "qa@test.com"})
assert update_resp.status_code == 200

# Delete
delete_resp = requests.delete(f"{base_url}/{user_id}")
assert delete_resp.status_code == 204
```
:::

## Параметри запиту

### Query-параметри (params)

```python
# Параметри додаються до URL автоматично
params = {"page": 1, "per_page": 10, "sort": "name"}

response = requests.get(
    "https://api.example.com/users",
    params=params
)
# URL стане: https://api.example.com/users?page=1&per_page=10&sort=name
```

### Заголовки (headers)

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Custom-Header": "test-value"
}

response = requests.get(
    "https://api.example.com/users",
    headers=headers
)
```

### Тіло запиту (json vs data)

```python
# json= автоматично серіалізує dict і встановлює Content-Type
response = requests.post(
    "https://api.example.com/users",
    json={"name": "Test", "age": 25}
)

# data= відправляє form-encoded дані
response = requests.post(
    "https://api.example.com/login",
    data={"username": "admin", "password": "secret"}
)

# data= з рядком — відправляє як є
import json
response = requests.post(
    "https://api.example.com/users",
    data=json.dumps({"name": "Test"}),
    headers={"Content-Type": "application/json"}
)
```

### Таймаут (timeout)

```python
# Таймаут у секундах
response = requests.get(
    "https://api.example.com/users",
    timeout=5  # 5 секунд
)

# Окремі таймаути для підключення та читання
response = requests.get(
    "https://api.example.com/users",
    timeout=(3, 10)  # 3 сек на підключення, 10 сек на читання
)
```

::: warning Завжди встановлюйте timeout
Без таймауту запит може зависнути назавжди. У тестах завжди вказуйте `timeout`.
```python
# Погано — може зависнути
response = requests.get("https://api.example.com/users")

# Добре — є обмеження часу
response = requests.get("https://api.example.com/users", timeout=30)
```
:::

## Об'єкт Response

```python
response = requests.get("https://api.example.com/users/1")

# Код статусу
print(response.status_code)     # 200

# Тіло відповіді
print(response.json())          # dict або list (парсить JSON)
print(response.text)            # Рядок (сирий текст відповіді)
print(response.content)         # bytes (бінарний вміст)

# Заголовки відповіді
print(response.headers)                    # Всі заголовки
print(response.headers["Content-Type"])    # 'application/json'

# Cookies
print(response.cookies)                    # RequestsCookieJar
print(response.cookies.get("session_id"))  # Конкретний cookie

# Інші атрибути
print(response.url)             # Фінальний URL (після редиректів)
print(response.elapsed)         # Час виконання запиту
print(response.encoding)        # Кодування відповіді
print(response.ok)              # True якщо status_code < 400
```

::: info Приклад для QA: перевірка відповіді API
```python
response = requests.get("https://api.example.com/users/1", timeout=10)

# Перевірка статус коду
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# Перевірка заголовків
assert response.headers["Content-Type"] == "application/json"

# Перевірка тіла відповіді
data = response.json()
assert "id" in data, "Response missing 'id' field"
assert data["id"] == 1
assert isinstance(data["name"], str), "Name should be a string"

# Перевірка часу відповіді
assert response.elapsed.total_seconds() < 2, "Response too slow"
```
:::

## Автентифікація

### Basic Auth

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/profile",
    auth=HTTPBasicAuth("username", "password"),
    timeout=10
)

# Скорочений варіант
response = requests.get(
    "https://api.example.com/profile",
    auth=("username", "password"),
    timeout=10
)
```

### Bearer Token

```python
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://api.example.com/profile",
    headers=headers,
    timeout=10
)
```

### API Key

```python
# API ключ у заголовку
headers = {"X-API-Key": "your-api-key-here"}
response = requests.get(
    "https://api.example.com/data",
    headers=headers,
    timeout=10
)

# API ключ у query-параметрах
params = {"api_key": "your-api-key-here"}
response = requests.get(
    "https://api.example.com/data",
    params=params,
    timeout=10
)
```

::: tip Зберігання секретів
Ніколи не зберігайте токени та паролі в коді. Використовуйте змінні оточення:
```python
import os

API_TOKEN = os.environ.get("API_TOKEN")
API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.example.com")

headers = {"Authorization": f"Bearer {API_TOKEN}"}
```
:::

## Управління сесіями

`requests.Session()` зберігає cookies, заголовки та інші параметри між запитами.

```python
session = requests.Session()

# Встановлюємо базові заголовки для всіх запитів
session.headers.update({
    "Authorization": "Bearer my-token",
    "Content-Type": "application/json"
})

# Встановлюємо базовий таймаут через хук (не вбудований параметр)
# Всі запити через session будуть використовувати ці заголовки
response1 = session.get("https://api.example.com/users", timeout=10)
response2 = session.get("https://api.example.com/posts", timeout=10)

# Cookies зберігаються автоматично між запитами
session.post(
    "https://api.example.com/login",
    json={"username": "admin", "password": "secret"},
    timeout=10
)
# Наступні запити вже автентифіковані через cookies
profile = session.get("https://api.example.com/profile", timeout=10)

# Закриття сесії
session.close()
```

::: info Приклад для QA: базовий клас API-тестів
```python
import requests

class APIClient:
    """Базовий клієнт для API-тестування."""

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=30,
            **kwargs
        )

    def post(self, endpoint, data=None, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=30,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=30,
            **kwargs
        )

    def close(self):
        self.session.close()


# Використання
client = APIClient("https://api.example.com", token="my-token")
response = client.get("/users")
assert response.status_code == 200
client.close()
```
:::

## Обробка помилок

### raise_for_status()

```python
response = requests.get("https://api.example.com/users/999", timeout=10)

# Піднімає HTTPError якщо status_code >= 400
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP помилка: {e}")
    print(f"Статус: {response.status_code}")
    print(f"Тіло: {response.text}")
```

### Обробка таймаутів

```python
try:
    response = requests.get(
        "https://api.example.com/slow-endpoint",
        timeout=5
    )
except requests.exceptions.ConnectTimeout:
    print("Не вдалося підключитися до сервера")
except requests.exceptions.ReadTimeout:
    print("Сервер не відповів вчасно")
except requests.exceptions.Timeout:
    print("Загальний таймаут")
```

### Повторні спроби (retries)

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Налаштування стратегії повторних спроб
retry_strategy = Retry(
    total=3,                    # Максимум 3 спроби
    backoff_factor=1,           # Затримка між спробами: 1, 2, 4 секунди
    status_forcelist=[500, 502, 503, 504],  # Повторювати при цих кодах
    allowed_methods=["GET", "POST"]         # Для яких методів повторювати
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

# Тепер запити автоматично повторюються при помилках
response = session.get("https://api.example.com/users", timeout=10)
```

### Комплексна обробка помилок

```python
import requests

def safe_api_call(method, url, **kwargs):
    """Безпечний виклик API з повною обробкою помилок."""
    kwargs.setdefault("timeout", 30)

    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print(f"Помилка підключення до {url}")
    except requests.exceptions.Timeout:
        print(f"Таймаут при запиті до {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP помилка {response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Невідома помилка: {e}")

    return None
```

::: warning Ієрархія винятків requests
```
RequestException
├── ConnectionError
│   └── ProxyError
│       └── SSLError
├── HTTPError
├── URLRequired
├── TooManyRedirects
├── Timeout
│   ├── ConnectTimeout
│   └── ReadTimeout
└── ContentDecodingError
```
Ловіть конкретні винятки перед загальними.
:::

## Приклади для QA-автоматизації

### Тестування REST API ендпоінтів

```python
import requests
import pytest

BASE_URL = "https://api.example.com"

class TestUsersAPI:
    """Тести для ендпоінту /users."""

    def test_get_all_users(self):
        response = requests.get(f"{BASE_URL}/users", timeout=10)
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0

    def test_get_user_by_id(self):
        response = requests.get(f"{BASE_URL}/users/1", timeout=10)
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "name" in user
        assert "email" in user

    def test_create_user(self):
        new_user = {
            "name": "Test User",
            "email": "test@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=new_user,
            timeout=10
        )
        assert response.status_code == 201
        created = response.json()
        assert created["name"] == new_user["name"]
        assert "id" in created

    def test_get_nonexistent_user(self):
        response = requests.get(f"{BASE_URL}/users/99999", timeout=10)
        assert response.status_code == 404

    def test_create_user_without_required_fields(self):
        response = requests.post(
            f"{BASE_URL}/users",
            json={},
            timeout=10
        )
        assert response.status_code == 400
```

### Валідація схеми відповіді

```python
def validate_user_schema(user_data):
    """Перевіряє, що відповідь відповідає очікуваній схемі."""
    required_fields = {
        "id": int,
        "name": str,
        "email": str,
        "created_at": str
    }

    for field, expected_type in required_fields.items():
        assert field in user_data, f"Відсутнє поле: {field}"
        assert isinstance(user_data[field], expected_type), (
            f"Поле '{field}' має тип {type(user_data[field])}, "
            f"очікувався {expected_type}"
        )

# Використання в тесті
def test_user_response_schema():
    response = requests.get("https://api.example.com/users/1", timeout=10)
    assert response.status_code == 200
    validate_user_schema(response.json())
```

::: tip Валідація схеми з jsonschema
Для складніших схем використовуйте бібліотеку `jsonschema`:
```python
pip install jsonschema
```
```python
from jsonschema import validate

user_schema = {
    "type": "object",
    "required": ["id", "name", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
        "is_active": {"type": "boolean"}
    },
    "additionalProperties": False
}

def test_user_json_schema():
    response = requests.get("https://api.example.com/users/1", timeout=10)
    validate(instance=response.json(), schema=user_schema)
```
:::

### Патерни автоматизованого API-тестування

```python
import requests
import pytest

class TestAPIPatterns:
    """Просунуті патерни API-тестування."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Створює сесію та тестові дані перед кожним тестом."""
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": "Bearer test-token"
        })
        self.base_url = "https://api.example.com"
        yield
        self.session.close()

    def test_pagination(self):
        """Перевірка пагінації."""
        page1 = self.session.get(
            f"{self.base_url}/users",
            params={"page": 1, "per_page": 5},
            timeout=10
        )
        assert page1.status_code == 200
        data1 = page1.json()
        assert len(data1) <= 5

        page2 = self.session.get(
            f"{self.base_url}/users",
            params={"page": 2, "per_page": 5},
            timeout=10
        )
        assert page2.status_code == 200
        data2 = page2.json()

        # ID на сторінках не повинні перетинатися
        ids_page1 = {u["id"] for u in data1}
        ids_page2 = {u["id"] for u in data2}
        assert ids_page1.isdisjoint(ids_page2), "Дублювання між сторінками"

    def test_response_time(self):
        """Перевірка часу відповіді (performance)."""
        response = self.session.get(
            f"{self.base_url}/users",
            timeout=10
        )
        assert response.elapsed.total_seconds() < 2, (
            f"Відповідь занадто повільна: {response.elapsed.total_seconds()}s"
        )

    def test_unauthorized_access(self):
        """Перевірка доступу без автентифікації."""
        no_auth_session = requests.Session()
        response = no_auth_session.get(
            f"{self.base_url}/admin/users",
            timeout=10
        )
        assert response.status_code in [401, 403]
        no_auth_session.close()

    def test_idempotent_put(self):
        """Перевірка ідемпотентності PUT."""
        user_data = {"name": "Test", "email": "test@example.com"}
        url = f"{self.base_url}/users/1"

        resp1 = self.session.put(url, json=user_data, timeout=10)
        resp2 = self.session.put(url, json=user_data, timeout=10)

        assert resp1.status_code == resp2.status_code
        assert resp1.json() == resp2.json()
```

## Корисні посилання

- [Документація requests](https://docs.python-requests.org/)
- [HTTP статус-коди (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [REST API Best Practices](https://restfulapi.net/)
- [jsonschema документація](https://python-jsonschema.readthedocs.io/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/docs/python/regex">← Регулярні вирази</a>
  <a href="/python_automation_courses/docs/python/virtual-environments">Віртуальні середовища →</a>
</div>
