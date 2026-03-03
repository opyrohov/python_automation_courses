# API Testing — Тестування API за допомогою Playwright

Playwright дозволяє тестувати API без запуску браузера, використовуючи `APIRequestContext`. Це корисно для тестування бекенду, підготовки тестових даних або комбінування API та UI тестів. У цьому розділі розглянемо всі аспекти API тестування.

## Основи APIRequestContext

```python
from playwright.sync_api import sync_playwright, APIRequestContext

def test_basic_api_request():
    """Базовий API запит без браузера."""
    with sync_playwright() as p:
        # Створення контексту API запитів
        api_context = p.request.new_context(
            base_url="https://api.example.com",
            extra_http_headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        # GET запит
        response = api_context.get("/users")
        assert response.ok  # Перевірка статусу 2xx
        assert response.status == 200

        # Отримання даних
        users = response.json()
        assert len(users) > 0

        # Закриття контексту
        api_context.dispose()
```

## HTTP методи

### GET запити

```python
def test_get_requests(api_context: APIRequestContext):
    """Різні варіанти GET запитів."""

    # Простий GET запит
    response = api_context.get("/api/users")
    assert response.status == 200
    users = response.json()

    # GET з параметрами запиту
    response = api_context.get("/api/users", params={
        "page": 1,
        "limit": 10,
        "sort": "name",
        "order": "asc",
    })
    data = response.json()
    assert len(data["items"]) <= 10

    # GET конкретного ресурсу
    response = api_context.get("/api/users/42")
    assert response.status == 200
    user = response.json()
    assert user["id"] == 42
```

### POST запити

```python
def test_post_requests(api_context: APIRequestContext):
    """Створення ресурсів через POST."""

    # POST з JSON тілом
    response = api_context.post("/api/users", data={
        "name": "Іван Петренко",
        "email": "ivan@example.com",
        "role": "tester",
    })
    assert response.status == 201
    created_user = response.json()
    assert created_user["name"] == "Іван Петренко"
    assert "id" in created_user

    # POST з form-data
    response = api_context.post("/api/feedback", form={
        "name": "Олена",
        "message": "Чудовий сервіс!",
        "rating": "5",
    })
    assert response.status == 201

    # POST з multipart (завантаження файлу)
    response = api_context.post("/api/upload", multipart={
        "file": {
            "name": "report.pdf",
            "mimeType": "application/pdf",
            "buffer": open("tests/data/report.pdf", "rb").read(),
        },
        "description": "Щомісячний звіт",
    })
    assert response.status == 200
```

### PUT та PATCH запити

```python
def test_put_patch_requests(api_context: APIRequestContext):
    """Оновлення ресурсів через PUT та PATCH."""

    # PUT — повне оновлення ресурсу
    response = api_context.put("/api/users/42", data={
        "name": "Іван Бондаренко",
        "email": "ivan.b@example.com",
        "role": "senior_tester",
    })
    assert response.status == 200
    updated = response.json()
    assert updated["name"] == "Іван Бондаренко"

    # PATCH — часткове оновлення ресурсу
    response = api_context.patch("/api/users/42", data={
        "role": "lead_tester",
    })
    assert response.status == 200
    patched = response.json()
    assert patched["role"] == "lead_tester"
```

### DELETE запити

```python
def test_delete_requests(api_context: APIRequestContext):
    """Видалення ресурсів через DELETE."""

    # Видалення ресурсу
    response = api_context.delete("/api/users/42")
    assert response.status == 204  # No Content

    # Перевірка, що ресурс видалено
    response = api_context.get("/api/users/42")
    assert response.status == 404
```

## Налаштування через фікстури pytest

```python
# conftest.py
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    """Фікстура для API контексту з базовими налаштуваннями."""
    context = playwright.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    yield context
    context.dispose()

@pytest.fixture(scope="session")
def auth_api_context(playwright: Playwright) -> APIRequestContext:
    """Фікстура для авторизованого API контексту."""
    # Отримання токена
    context = playwright.request.new_context(
        base_url="https://api.example.com",
    )
    response = context.post("/auth/login", data={
        "email": "admin@example.com",
        "password": "admin123",
    })
    token = response.json()["access_token"]
    context.dispose()

    # Створення авторизованого контексту
    auth_context = playwright.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        },
    )
    yield auth_context
    auth_context.dispose()
```

## Перевірка відповідей

```python
import re

def test_response_validation(api_context: APIRequestContext):
    """Детальна перевірка API відповідей."""
    response = api_context.get("/api/users/1")

    # Перевірка статус-коду
    assert response.status == 200
    assert response.ok  # True для статусів 200-299

    # Перевірка статус-тексту
    assert response.status_text == "OK"

    # Перевірка заголовків відповіді
    headers = response.headers
    assert headers["content-type"] == "application/json; charset=utf-8"
    assert "x-request-id" in headers

    # Перевірка тіла відповіді
    user = response.json()
    assert user["id"] == 1
    assert isinstance(user["name"], str)
    assert len(user["name"]) > 0
    assert re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", user["email"])
    assert user["role"] in ["admin", "user", "tester"]

    # Перевірка вкладених об'єктів
    assert "address" in user
    assert user["address"]["city"] is not None

    # Перевірка масивів
    assert isinstance(user["permissions"], list)
    assert len(user["permissions"]) > 0
```

::: tip Порада
Для складної валідації JSON-схем можна використовувати бібліотеки `jsonschema` або `pydantic` разом з Playwright.
:::

## Тестування CRUD операцій

```python
def test_full_crud_cycle(api_context: APIRequestContext):
    """Повний цикл CRUD операцій для ресурсу."""

    # CREATE — створення нового користувача
    create_response = api_context.post("/api/users", data={
        "name": "Тестовий Користувач",
        "email": "test_crud@example.com",
        "role": "tester",
    })
    assert create_response.status == 201
    user_id = create_response.json()["id"]

    # READ — читання створеного користувача
    read_response = api_context.get(f"/api/users/{user_id}")
    assert read_response.status == 200
    user = read_response.json()
    assert user["name"] == "Тестовий Користувач"

    # UPDATE — оновлення користувача
    update_response = api_context.put(f"/api/users/{user_id}", data={
        "name": "Оновлений Користувач",
        "email": "test_crud@example.com",
        "role": "senior_tester",
    })
    assert update_response.status == 200
    assert update_response.json()["name"] == "Оновлений Користувач"

    # DELETE — видалення користувача
    delete_response = api_context.delete(f"/api/users/{user_id}")
    assert delete_response.status == 204

    # Перевірка видалення
    verify_response = api_context.get(f"/api/users/{user_id}")
    assert verify_response.status == 404
```

## Комбінування API та UI тестів

```python
from playwright.sync_api import Page, expect

def test_api_prepare_ui_verify(page: Page):
    """Підготовка даних через API, перевірка через UI."""

    # Створення тестових даних через API
    api = page.context.request
    response = api.post("https://api.example.com/products", data={
        "name": "Тестовий товар для UI",
        "price": 999.99,
        "category": "electronics",
    })
    product_id = response.json()["id"]

    # Перевірка через UI
    page.goto(f"https://example.com/products/{product_id}")
    expect(page.get_by_role("heading", level=1)).to_have_text("Тестовий товар для UI")
    expect(page.get_by_test_id("price")).to_contain_text("999.99")

    # Очищення через API
    api.delete(f"https://api.example.com/products/{product_id}")


def test_ui_action_api_verify(page: Page):
    """Дія через UI, перевірка через API."""

    # Створення замовлення через UI
    page.goto("https://example.com/products/1")
    page.get_by_role("button", name="Додати до кошика").click()
    page.get_by_role("link", name="Оформити замовлення").click()
    page.get_by_label("Адреса").fill("вул. Хрещатик, 1")
    page.get_by_role("button", name="Підтвердити").click()

    # Отримання ID замовлення з UI
    order_text = page.get_by_test_id("order-number").text_content()
    order_id = order_text.split("#")[1]

    # Перевірка через API
    api = page.context.request
    response = api.get(f"https://api.example.com/orders/{order_id}")
    order = response.json()
    assert order["status"] == "pending"
    assert order["address"] == "вул. Хрещатик, 1"
```

::: info Інформація
Комбінування API та UI тестів — потужна стратегія. API запити швидші для підготовки та очищення тестових даних, а UI тести перевіряють те, що бачить користувач.
:::

## Тестування помилок API

```python
def test_api_error_handling(api_context: APIRequestContext):
    """Перевірка обробки помилок API."""

    # 400 Bad Request — невалідні дані
    response = api_context.post("/api/users", data={
        "email": "not-an-email",
    })
    assert response.status == 400
    error = response.json()
    assert "validation" in error["error"].lower()

    # 401 Unauthorized — без автентифікації
    response = api_context.get("/api/admin/settings")
    assert response.status == 401

    # 404 Not Found — неіснуючий ресурс
    response = api_context.get("/api/users/999999")
    assert response.status == 404

    # 409 Conflict — дублікат
    api_context.post("/api/users", data={
        "name": "Дублікат",
        "email": "duplicate@example.com",
    })
    response = api_context.post("/api/users", data={
        "name": "Дублікат 2",
        "email": "duplicate@example.com",
    })
    assert response.status == 409

    # 422 Unprocessable Entity — семантична помилка
    response = api_context.post("/api/orders", data={
        "product_id": 1,
        "quantity": -5,  # Від'ємна кількість
    })
    assert response.status == 422
```

## Перехоплення мережевих запитів

```python
def test_intercept_api_requests(page: Page):
    """Перехоплення та модифікація API запитів у браузері."""

    # Мокування API відповіді
    page.route("**/api/users", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='[{"id": 1, "name": "Мок-користувач"}]',
    ))
    page.goto("https://example.com/users")
    expect(page.get_by_text("Мок-користувач")).to_be_visible()

    # Перехоплення та модифікація відповіді
    def modify_response(route):
        response = route.fetch()  # Виконати реальний запит
        body = response.json()
        # Модифікуємо дані
        for user in body:
            user["name"] = user["name"].upper()
        route.fulfill(response=response, json=body)

    page.route("**/api/users", modify_response)

    # Блокування запитів (наприклад, аналітика)
    page.route("**/analytics/**", lambda route: route.abort())
```

::: warning Увага
Мокування API відповідей корисне для ізоляції тестів, але не замінює повноцінне інтеграційне тестування з реальним бекендом.
:::

## Корисні посилання

- [Офіційна документація API Testing](https://playwright.dev/python/docs/api-testing)
- [APIRequestContext API](https://playwright.dev/python/docs/api/class-apirequestcontext)
- [Мережеве перехоплення](https://playwright.dev/python/docs/network)
- [Мокування запитів](https://playwright.dev/python/docs/mock)
