# Лекція 34: Параметризоване тестування

Параметризовані тести.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_34_Parameterized_Testing/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_34_Parameterized_Testing/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_34_Parameterized_Testing/exercises" target="_blank">📝 Вправи</a>
</div>

## Базова параметризація

```python
import pytest

@pytest.mark.parametrize("email,password,expected", [
    ("valid@test.com", "password123", True),
    ("invalid", "password123", False),
    ("valid@test.com", "wrong", False),
])
def test_login(page, email, password, expected):
    page.goto("/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    if expected:
        expect(page).to_have_url("**/dashboard")
    else:
        expect(page.get_by_text("Error")).to_be_visible()
```

## IDs для параметрів

```python
@pytest.mark.parametrize("browser_name", [
    pytest.param("chromium", id="chrome"),
    pytest.param("firefox", id="ff"),
    pytest.param("webkit", id="safari"),
])
def test_cross_browser(browser_name, playwright):
    browser = getattr(playwright, browser_name).launch()
    # ...
```

## Множинна параметризація

```python
@pytest.mark.parametrize("username", ["user1", "user2"])
@pytest.mark.parametrize("action", ["view", "edit", "delete"])
def test_permissions(page, username, action):
    # Виконується 6 разів: 2 users × 3 actions
    pass
```

## Параметризація з fixtures

```python
@pytest.fixture
def login_data(request):
    data = {
        "valid": ("user@test.com", "pass123"),
        "invalid": ("wrong@test.com", "wrong"),
    }
    return data[request.param]

@pytest.mark.parametrize("login_data", ["valid", "invalid"], indirect=True)
def test_login(page, login_data):
    email, password = login_data
    # ...
```

## Параметризація з файлу

```python
import json

def load_test_cases():
    with open("data/test_cases.json") as f:
        return json.load(f)

@pytest.mark.parametrize("test_case", load_test_cases())
def test_from_file(page, test_case):
    page.goto(test_case["url"])
    expect(page).to_have_title(test_case["expected_title"])
```

## Skip та xfail

```python
@pytest.mark.parametrize("browser", [
    "chromium",
    pytest.param("firefox", marks=pytest.mark.skip(reason="Known bug")),
    pytest.param("webkit", marks=pytest.mark.xfail(reason="Flaky")),
])
def test_browsers(browser):
    pass
```
