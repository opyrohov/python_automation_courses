# Плагіни

Розширення функціональності pytest за допомогою плагінів — від звітів до паралельного запуску.

## pytest-playwright

Інтеграція Playwright з pytest для E2E тестування.

```bash
pip install pytest-playwright
playwright install
```

```python
# conftest.py автоматично надає фікстури: page, browser, context
import pytest

def test_homepage(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"

# Конфігурація через CLI
# pytest --browser chromium --headed --slowmo 500
```

```ini
# pytest.ini
[pytest]
# Базові налаштування playwright
base_url = https://staging.example.com
```

## pytest-html

HTML звіти з результатами тестів.

```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

```python
# conftest.py — додавання скріншотів до звіту
import pytest
import base64

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            b64 = base64.b64encode(screenshot).decode()
            report.extras = [
                pytest.html.extras.image(b64, mime_type="image/png")
            ]
```

## pytest-xdist

Паралельний запуск тестів.

```bash
pip install pytest-xdist

# Запуск
pytest -n auto           # Автовизначення процесів
pytest -n 4              # 4 процеси
pytest -n auto --dist loadgroup  # Групування
```

```python
# Групування тестів для послідовного виконання
@pytest.mark.xdist_group("database")
class TestDatabase:
    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_delete(self):
        pass
```

::: warning Паралельні тести
Тести мають бути ізольованими один від одного. Уникайте спільного стану між тестами при паралельному запуску.
:::

## Allure

Детальні інтерактивні звіти.

```bash
pip install allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

```python
import allure

@allure.feature("Авторизація")
@allure.story("Логін")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(page):
    with allure.step("Відкрити сторінку логіну"):
        page.goto("/login")

    with allure.step("Ввести дані"):
        page.fill("#email", "user@test.com")
        page.fill("#password", "pass123")

    with allure.step("Натиснути кнопку входу"):
        page.click("#submit")

    with allure.step("Перевірити результат"):
        assert page.url.endswith("/dashboard")

    # Прикріпити скріншот
    allure.attach(
        page.screenshot(),
        name="dashboard",
        attachment_type=allure.attachment_type.PNG
    )
```

## pytest-rerunfailures

Повторний запуск провалених тестів.

```bash
pip install pytest-rerunfailures

# Перезапуск провалених до 3 разів
pytest --reruns 3

# З затримкою між спробами
pytest --reruns 3 --reruns-delay 2
```

```python
# Маркер для конкретного тесту
@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_unstable_api():
    response = api_client.get("/data")
    assert response.status_code == 200
```

## pytest-timeout

Обмеження часу виконання тестів.

```bash
pip install pytest-timeout

# Глобальний таймаут
pytest --timeout=60
```

```python
# Таймаут для конкретного тесту
@pytest.mark.timeout(30)
def test_slow_operation():
    pass

# Через фікстуру
@pytest.fixture(autouse=True)
def default_timeout():
    return pytest.importorskip("pytest_timeout")
```

## pytest-mock

Мокування об'єктів.

```bash
pip install pytest-mock
```

```python
def test_api_call(mocker):
    # Замокати HTTP запит
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Test"}

    mocker.patch("requests.get", return_value=mock_response)

    # Тест використовує замоканий requests.get
    import requests
    response = requests.get("https://api.example.com/users/1")
    assert response.json()["name"] == "Test"
```

## Створення власного плагіна

```python
# conftest.py або окремий пакет
import pytest
import time

class TimingPlugin:
    """Плагін для вимірювання часу тестів."""

    def __init__(self):
        self.results = []

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_call(self, item):
        start = time.time()
        yield
        duration = time.time() - start
        self.results.append((item.name, duration))

    def pytest_terminal_summary(self, terminalreporter):
        terminalreporter.write_sep("=", "Найповільніші тести")
        sorted_results = sorted(self.results, key=lambda x: x[1], reverse=True)
        for name, duration in sorted_results[:5]:
            terminalreporter.write_line(f"  {name}: {duration:.2f}s")

def pytest_configure(config):
    config.pluginmanager.register(TimingPlugin(), "timing-plugin")
```

## Корисні посилання

- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
- [pytest-html](https://pytest-html.readthedocs.io/)
- [pytest-xdist](https://pytest-xdist.readthedocs.io/)
- [Allure pytest](https://allurereport.org/docs/pytest/)
- [Список плагінів pytest](https://docs.pytest.org/en/stable/reference/plugin_list.html)
