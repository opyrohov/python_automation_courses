# Lecture 36: Solutions

## Exercise 1: Refactor Messy Tests

### Summary of Issues

| Test | Issues |
|------|--------|
| test_1 | Tests 2 things (login + logout), brittle CSS selectors, magic strings |
| test_2 | Duplicate setup, brittle selectors, poor name |
| test_3 | Duplicate setup, brittle selectors, poor name |
| test_4 | No fixture, poor name, generic selector |
| test_5 | No fixture, poor name, generic selector |
| test_6 | Tests 2 things in one test, poor name |

### Refactored conftest.py

```python
# conftest.py
import pytest
from playwright.sync_api import Page

BASE_URL = "https://the-internet.herokuapp.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def login_page(page: Page, base_url):
    """Navigate to login page."""
    page.goto(f"{base_url}/login")
    return page


@pytest.fixture
def authenticated_page(page: Page, base_url):
    """Login and return authenticated page."""
    page.goto(f"{base_url}/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    return page


@pytest.fixture
def checkboxes_page(page: Page, base_url):
    """Navigate to checkboxes page."""
    page.goto(f"{base_url}/checkboxes")
    return page


@pytest.fixture
def dropdown_page(page: Page, base_url):
    """Navigate to dropdown page."""
    page.goto(f"{base_url}/dropdown")
    return page
```

### Refactored Tests

```python
# test_login.py
import pytest
from playwright.sync_api import Page

VALID_USER = "tomsmith"
VALID_PASS = "SuperSecretPassword!"


@pytest.mark.smoke
def test_successful_login_redirects_to_secure_area(login_page: Page):
    """Verify valid credentials redirect to /secure."""
    # Arrange: login_page fixture navigated to /login
    # Act
    login_page.locator("#username").fill(VALID_USER)
    login_page.locator("#password").fill(VALID_PASS)
    login_page.locator("button[type='submit']").click()
    # Assert
    assert "/secure" in login_page.url


@pytest.mark.regression
def test_logout_redirects_to_login_page(authenticated_page: Page):
    """Verify logout returns to login page."""
    # Arrange: authenticated_page fixture already logged in
    # Act
    authenticated_page.locator('a[href="/logout"]').click()
    # Assert
    assert "/login" in authenticated_page.url


@pytest.mark.regression
@pytest.mark.parametrize("username,password,error_text", [
    ("wrong", "wrong", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
], ids=["invalid_username", "invalid_password"])
def test_failed_login_shows_error(login_page: Page, username, password, error_text):
    """Verify invalid credentials show correct error message."""
    # Act
    login_page.locator("#username").fill(username)
    login_page.locator("#password").fill(password)
    login_page.locator("button[type='submit']").click()
    # Assert
    assert error_text in login_page.locator("#flash").text_content()
```

```python
# test_checkboxes.py
import pytest
from playwright.sync_api import Page


@pytest.mark.smoke
def test_first_checkbox_can_be_checked(checkboxes_page: Page):
    """Verify first checkbox can be checked."""
    checkbox = checkboxes_page.locator("input[type='checkbox']").first
    checkbox.check()
    assert checkbox.is_checked()


@pytest.mark.smoke
def test_second_checkbox_can_be_unchecked(checkboxes_page: Page):
    """Verify second checkbox can be unchecked."""
    checkbox = checkboxes_page.locator("input[type='checkbox']").nth(1)
    checkbox.uncheck()
    assert not checkbox.is_checked()
```

```python
# test_dropdown.py
import pytest
from playwright.sync_api import Page


@pytest.mark.regression
@pytest.mark.parametrize("value", ["1", "2"], ids=["option_1", "option_2"])
def test_dropdown_option_can_be_selected(dropdown_page: Page, value):
    """Verify dropdown option can be selected."""
    dropdown = dropdown_page.locator("#dropdown")
    dropdown.select_option(value)
    assert dropdown.input_value() == value
```

### What Changed

1. **Constants** instead of magic strings
2. **Descriptive names**: `test_1` → `test_successful_login_redirects_to_secure_area`
3. **Stable selectors**: `div:nth-child(1) > div > ...` → `#username`
4. **Fixtures**: `login_page`, `authenticated_page`, `checkboxes_page`, `dropdown_page`
5. **Parametrize**: Combined test_2 + test_3 into one parametrized test
6. **One test = one thing**: Split test_1 into login test + logout test
7. **Markers**: `@pytest.mark.smoke` and `@pytest.mark.regression`
8. **AAA pattern**: Clear Arrange-Act-Assert sections

---

## Exercise 2: Final Project

### Page Objects

```python
# pages/login_page.py
from playwright.sync_api import Page


class LoginPage:
    URL = "/login"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    def navigate(self):
        self.page.goto(f"{self.base_url}{self.URL}")
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        return self

    def get_flash_message(self) -> str:
        return self.flash_message.text_content()

    @property
    def is_logged_in(self) -> bool:
        return "/secure" in self.page.url
```

```python
# pages/checkboxes_page.py
from playwright.sync_api import Page


class CheckboxesPage:
    URL = "/checkboxes"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self._checkboxes = page.locator("input[type='checkbox']")

    def navigate(self):
        self.page.goto(f"{self.base_url}{self.URL}")
        return self

    def check(self, index: int):
        self._checkboxes.nth(index).check()

    def uncheck(self, index: int):
        self._checkboxes.nth(index).uncheck()

    def is_checked(self, index: int) -> bool:
        return self._checkboxes.nth(index).is_checked()

    @property
    def count(self) -> int:
        return self._checkboxes.count()
```

### Complete conftest.py

```python
# conftest.py
import pytest
from pathlib import Path
from playwright.sync_api import Page, BrowserContext
from pages.login_page import LoginPage
from pages.checkboxes_page import CheckboxesPage

BASE_URL = "https://the-internet.herokuapp.com"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def login_page(page: Page, base_url):
    return LoginPage(page, base_url).navigate()


@pytest.fixture
def checkboxes_page(page: Page, base_url):
    return CheckboxesPage(page, base_url).navigate()


@pytest.fixture
def authenticated_page(page: Page, base_url):
    lp = LoginPage(page, base_url).navigate()
    lp.login("tomsmith", "SuperSecretPassword!")
    return page


@pytest.fixture
def screenshot_on_failure(page: Page, request):
    yield page
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        Path("screenshots").mkdir(exist_ok=True)
        page.screenshot(path=f"screenshots/FAIL_{request.node.name}.png")
```

### Additional Tests

```python
# test_alerts.py
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


@pytest.mark.regression
def test_js_alert(page: Page):
    """Test JavaScript alert handling."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    assert "You successfully clicked an alert" in page.locator("#result").text_content()


@pytest.mark.regression
def test_js_confirm_accept(page: Page):
    """Test accepting a JS confirm dialog."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    assert "You clicked: Ok" in page.locator("#result").text_content()


@pytest.mark.regression
def test_js_confirm_dismiss(page: Page):
    """Test dismissing a JS confirm dialog."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    assert "You clicked: Cancel" in page.locator("#result").text_content()


@pytest.mark.regression
def test_js_prompt(page: Page):
    """Test JS prompt with custom text."""
    page.goto(f"{BASE_URL}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    assert "You entered: Hello Playwright" in page.locator("#result").text_content()
```

```python
# test_hovers.py
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://the-internet.herokuapp.com"


@pytest.mark.regression
@pytest.mark.parametrize("index,expected_name", [
    (0, "name: user1"),
    (1, "name: user2"),
    (2, "name: user3"),
], ids=["user1", "user2", "user3"])
def test_hover_reveals_user_info(page: Page, index, expected_name):
    """Test that hovering over avatar reveals user info."""
    page.goto(f"{BASE_URL}/hovers")
    figure = page.locator(".figure").nth(index)
    figure.hover()
    info = figure.locator(".figcaption")
    expect(info).to_be_visible()
    assert expected_name in info.text_content()
```

### GitHub Actions Workflow

```yaml
# .github/workflows/tests.yml
name: Playwright Tests

on:
  push:
    branches: [main]
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
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps chromium

      - name: Run smoke tests
        run: pytest -m smoke -v --tracing retain-on-failure --output test-results/

      - name: Run full regression
        run: pytest -v --tracing retain-on-failure --output test-results/

      - name: Upload test artifacts
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: test-results/
```
