# Lecture 33: Test Data Management

Test data management.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_33_Test_Data_Management/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_33_Test_Data_Management/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_33_Test_Data_Management/exercises" target="_blank">📝 Вправи</a>
</div>

## JSON Files

```python
# data/users.json
{
    "valid_user": {
        "email": "test@example.com",
        "password": "password123"
    },
    "invalid_user": {
        "email": "invalid",
        "password": "short"
    }
}

# tests/conftest.py
import json

@pytest.fixture
def test_data():
    with open("data/users.json") as f:
        return json.load(f)

def test_login(page, test_data):
    user = test_data["valid_user"]
    # ...
```

## Faker

```python
from faker import Faker

fake = Faker("uk_UA")

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address()
    }

@pytest.fixture
def random_user():
    return generate_user()

def test_registration(page, random_user):
    page.get_by_label("Name").fill(random_user["name"])
    page.get_by_label("Email").fill(random_user["email"])
```

## Factory Pattern

```python
from dataclasses import dataclass, field
from faker import Faker

fake = Faker()

@dataclass
class User:
    email: str = field(default_factory=fake.email)
    password: str = "Password123!"
    name: str = field(default_factory=fake.name)

# Usage
user = User()  # All fields generated
user = User(email="specific@test.com")  # Specific email
```

## Fixtures with Parameters

```python
@pytest.fixture
def user(request):
    user_type = getattr(request, "param", "valid")
    users = {
        "valid": {"email": "valid@test.com", "password": "pass123"},
        "invalid": {"email": "invalid", "password": "x"},
        "admin": {"email": "admin@test.com", "password": "admin123"}
    }
    return users[user_type]

@pytest.mark.parametrize("user", ["valid", "admin"], indirect=True)
def test_login(page, user):
    # user will be valid or admin
    pass
```

## Cleanup Test Data

```python
@pytest.fixture
def created_user(api):
    # Setup: create user
    response = api.post("/users", data={"name": "Test"})
    user_id = response.json()["id"]

    yield user_id

    # Teardown: delete user
    api.delete(f"/users/{user_id}")
```
