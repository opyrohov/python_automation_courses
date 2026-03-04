# Plugins

Extending pytest functionality with plugins — from reports to parallel execution.

## pytest-playwright

Playwright integration with pytest for E2E testing.

```bash
pip install pytest-playwright
playwright install
```

```python
# conftest.py automatically provides fixtures: page, browser, context
import pytest

def test_homepage(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"

# Configuration via CLI
# pytest --browser chromium --headed --slowmo 500
```

```ini
# pytest.ini
[pytest]
# Basic playwright settings
base_url = https://staging.example.com
```

## pytest-html

HTML reports with test results.

```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

```python
# conftest.py — adding screenshots to the report
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

Parallel test execution.

```bash
pip install pytest-xdist

# Execution
pytest -n auto           # Auto-detect processes
pytest -n 4              # 4 processes
pytest -n auto --dist loadgroup  # Grouping
```

```python
# Grouping tests for sequential execution
@pytest.mark.xdist_group("database")
class TestDatabase:
    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_delete(self):
        pass
```

::: warning Parallel Tests
Tests must be isolated from each other. Avoid shared state between tests during parallel execution.
:::

## Allure

Detailed interactive reports.

```bash
pip install allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

```python
import allure

@allure.feature("Authentication")
@allure.story("Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(page):
    with allure.step("Open the login page"):
        page.goto("/login")

    with allure.step("Enter credentials"):
        page.fill("#email", "user@test.com")
        page.fill("#password", "pass123")

    with allure.step("Click the login button"):
        page.click("#submit")

    with allure.step("Verify the result"):
        assert page.url.endswith("/dashboard")

    # Attach screenshot
    allure.attach(
        page.screenshot(),
        name="dashboard",
        attachment_type=allure.attachment_type.PNG
    )
```

## pytest-rerunfailures

Re-running failed tests.

```bash
pip install pytest-rerunfailures

# Re-run failed tests up to 3 times
pytest --reruns 3

# With delay between attempts
pytest --reruns 3 --reruns-delay 2
```

```python
# Marker for a specific test
@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_unstable_api():
    response = api_client.get("/data")
    assert response.status_code == 200
```

## pytest-timeout

Limiting test execution time.

```bash
pip install pytest-timeout

# Global timeout
pytest --timeout=60
```

```python
# Timeout for a specific test
@pytest.mark.timeout(30)
def test_slow_operation():
    pass

# Via fixture
@pytest.fixture(autouse=True)
def default_timeout():
    return pytest.importorskip("pytest_timeout")
```

## pytest-mock

Object mocking.

```bash
pip install pytest-mock
```

```python
def test_api_call(mocker):
    # Mock HTTP request
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Test"}

    mocker.patch("requests.get", return_value=mock_response)

    # Test uses the mocked requests.get
    import requests
    response = requests.get("https://api.example.com/users/1")
    assert response.json()["name"] == "Test"
```

## Creating Your Own Plugin

```python
# conftest.py or separate package
import pytest
import time

class TimingPlugin:
    """Plugin for measuring test time."""

    def __init__(self):
        self.results = []

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_call(self, item):
        start = time.time()
        yield
        duration = time.time() - start
        self.results.append((item.name, duration))

    def pytest_terminal_summary(self, terminalreporter):
        terminalreporter.write_sep("=", "Slowest Tests")
        sorted_results = sorted(self.results, key=lambda x: x[1], reverse=True)
        for name, duration in sorted_results[:5]:
            terminalreporter.write_line(f"  {name}: {duration:.2f}s")

def pytest_configure(config):
    config.pluginmanager.register(TimingPlugin(), "timing-plugin")
```

## Useful Links

- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
- [pytest-html](https://pytest-html.readthedocs.io/)
- [pytest-xdist](https://pytest-xdist.readthedocs.io/)
- [Allure pytest](https://allurereport.org/docs/pytest/)
- [pytest plugin list](https://docs.pytest.org/en/stable/reference/plugin_list.html)
