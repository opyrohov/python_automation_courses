# Solutions - Lecture 34: Parameterized Testing

## Exercise 1: Comprehensive Login Test Suite

```python
"""Exercise 1 Solution: Data-Driven Login Tests"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# TUPLE PARAMS WITH CUSTOM IDs
# ============================================

@pytest.mark.parametrize("username,password,expected_url", [
    ("tomsmith", "SuperSecretPassword!", "/secure"),
    ("wrong", "wrong", "/login"),
    ("tomsmith", "bad_password", "/login"),
    ("", "", "/login"),
], ids=["valid", "bad_user", "bad_pass", "empty"])
def test_login_scenarios(page: Page, username, password, expected_url):
    """Login with various credentials."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    assert expected_url in page.url


# ============================================
# DICT PARAMS
# ============================================

ERROR_CASES = [
    {"username": "wrong", "password": "SuperSecretPassword!", "error": "Your username is invalid!"},
    {"username": "tomsmith", "password": "wrong", "error": "Your password is invalid!"},
]

@pytest.mark.parametrize("case", ERROR_CASES, ids=lambda c: c["username"])
def test_login_error_messages(page: Page, case):
    """Check error messages for invalid logins."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(case["username"])
    page.locator("#password").fill(case["password"])
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash").text_content()
    assert case["error"] in flash


# ============================================
# pytest.param WITH MARKS
# ============================================

@pytest.mark.parametrize("username,password,succeeds", [
    pytest.param("tomsmith", "SuperSecretPassword!", True, id="valid"),
    pytest.param("wrong", "wrong", False, id="invalid"),
    pytest.param("admin", "admin", True, id="admin_guess",
                 marks=pytest.mark.xfail(reason="admin is not a valid user")),
])
def test_login_with_marks(page: Page, username, password, succeeds):
    """Login tests with per-case marks."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if succeeds:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# TABLE PATTERN
# ============================================

TEST_TABLE = [
    # username      password                   success  error_fragment
    ("tomsmith",    "SuperSecretPassword!",     True,    None),
    ("wrong",       "SuperSecretPassword!",     False,   "username is invalid"),
    ("tomsmith",    "wrong",                    False,   "password is invalid"),
]

@pytest.mark.parametrize("username,password,success,error", TEST_TABLE,
                         ids=["valid", "bad_user", "bad_pass"])
def test_login_table(page: Page, username, password, success, error):
    """Table-style parametrize."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if success:
        assert "/secure" in page.url
    else:
        flash = page.locator("#flash").text_content()
        assert error in flash


# ============================================
# CLASS-LEVEL PARAMETRIZE
# ============================================

@pytest.mark.parametrize("username,password", [
    ("tomsmith", "SuperSecretPassword!"),
])
class TestLoginFlow:
    def test_can_login(self, page: Page, username, password):
        page.goto(f"{BASE_URL}/login")
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("button[type='submit']").click()
        assert "/secure" in page.url

    def test_sees_secure_area(self, page: Page, username, password):
        page.goto(f"{BASE_URL}/login")
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("button[type='submit']").click()
        assert page.locator("h2").text_content().strip() == "Secure Area"
```

---

## Exercise 2: Matrix Testing

```python
"""Exercise 2 Solution: Matrix Testing"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# STACKED: RESPONSIVE PAGES
# ============================================

@pytest.mark.parametrize("path", ["/login", "/checkboxes", "/dropdown"])
@pytest.mark.parametrize("width,height", [
    (1920, 1080),
    (768, 1024),
    (375, 812),
], ids=["desktop", "tablet", "mobile"])
def test_responsive_pages(page: Page, width, height, path):
    """3 pages x 3 viewports = 9 tests."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{BASE_URL}{path}")
    assert page.title() == "The Internet"
    print(f"\n  {path} @ {width}x{height}")


# ============================================
# INDIRECT: VIEWPORT FIXTURE
# ============================================

@pytest.fixture
def viewport_page(request, page: Page):
    """Fixture: set viewport and navigate from parameter."""
    config = request.param
    page.set_viewport_size({"width": config["width"], "height": config["height"]})
    page.goto(f"{BASE_URL}{config['path']}")
    return page


@pytest.mark.parametrize("viewport_page", [
    {"width": 1920, "height": 1080, "path": "/login"},
    {"width": 375, "height": 812, "path": "/login"},
    {"width": 1920, "height": 1080, "path": "/checkboxes"},
    {"width": 375, "height": 812, "path": "/checkboxes"},
], indirect=True, ids=["desktop_login", "mobile_login", "desktop_cb", "mobile_cb"])
def test_viewport_heading(viewport_page):
    """Indirect parametrize with viewport fixture."""
    heading = viewport_page.locator("h3, h2").first
    assert heading.is_visible()


# ============================================
# STACKED: CHECKBOX ACTIONS
# ============================================

@pytest.mark.parametrize("action", ["check", "uncheck"])
@pytest.mark.parametrize("index", [0, 1], ids=["first", "second"])
def test_checkbox_actions(page: Page, index, action):
    """2 checkboxes x 2 actions = 4 tests."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkbox = page.locator("input[type='checkbox']").nth(index)

    if action == "check":
        checkbox.check()
        assert checkbox.is_checked()
    else:
        checkbox.uncheck()
        assert not checkbox.is_checked()

    print(f"\n  Checkbox {index}: {action}")


# ============================================
# STACKED: DROPDOWN x VIEWPORT
# ============================================

@pytest.mark.parametrize("option", ["1", "2"])
@pytest.mark.parametrize("width,height", [
    (1280, 720),
    (375, 812),
], ids=["desktop", "mobile"])
def test_dropdown_viewport(page: Page, width, height, option):
    """2 options x 2 viewports = 4 tests."""
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{BASE_URL}/dropdown")
    page.locator("#dropdown").select_option(value=option)
    selected = page.locator("#dropdown option:checked")
    assert f"Option {option}" in selected.text_content()
```

### Key Points:
- Stacking creates all combinations automatically
- indirect=True parametrizes the fixture, not the test
- Count your combinations: N x M can grow fast
- Use meaningful IDs for readability

---

## Summary: When to Use Each Pattern

| Pattern | Use When |
|---------|----------|
| Basic `parametrize` | Simple input/output variations |
| Custom IDs | Complex parameters need readable names |
| `pytest.param(marks=)` | Some cases should xfail/skip |
| Dict parameters | 4+ fields per test case |
| Table pattern | Many similar cases, scannable |
| Stacking | All combinations needed (matrix) |
| `indirect=True` | Parametrize fixture setup |
| `fixture(params=)` | Every test using fixture gets all params |
| `pytest_generate_tests` | Dynamic data from files/DB/API |
| Generator function | Computed/calculated parameters |
