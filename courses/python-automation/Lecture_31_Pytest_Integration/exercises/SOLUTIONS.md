# Solutions - Lecture 31: Pytest Integration

## Exercise 1: Write Basic Pytest Tests

```python
"""Exercise 1 Solution: Basic Pytest Tests"""
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# CHECKBOX TESTS
# ============================================

def test_checkboxes_page_loads(page: Page):
    """Verify checkboxes page loads with correct heading."""
    page.goto(f"{BASE_URL}/checkboxes")
    heading = page.locator("h3")
    assert heading.text_content() == "Checkboxes"


def test_two_checkboxes_present(page: Page):
    """Verify exactly 2 checkboxes exist."""
    page.goto(f"{BASE_URL}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2


def test_check_first_checkbox(page: Page):
    """Check first checkbox and verify."""
    page.goto(f"{BASE_URL}/checkboxes")
    first_checkbox = page.locator("input[type='checkbox']").first
    first_checkbox.check()
    assert first_checkbox.is_checked()


def test_uncheck_second_checkbox(page: Page):
    """Uncheck second checkbox and verify."""
    page.goto(f"{BASE_URL}/checkboxes")
    second_checkbox = page.locator("input[type='checkbox']").nth(1)
    second_checkbox.uncheck()
    assert not second_checkbox.is_checked()


# ============================================
# DROPDOWN TESTS
# ============================================

def test_dropdown_page_loads(page: Page):
    """Verify dropdown page loads."""
    page.goto(f"{BASE_URL}/dropdown")
    heading = page.locator("h3")
    assert heading.text_content() == "Dropdown List"


def test_select_option_1(page: Page):
    """Select Option 1 and verify."""
    page.goto(f"{BASE_URL}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(value="1")

    selected = dropdown.locator("option:checked")
    assert selected.text_content().strip() == "Option 1"


def test_select_option_2(page: Page):
    """Select Option 2 and verify."""
    page.goto(f"{BASE_URL}/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(value="2")

    selected = dropdown.locator("option:checked")
    assert selected.text_content().strip() == "Option 2"
```

### Key Points:
- Each test function starts with `test_`
- `page` fixture is provided automatically by pytest-playwright
- Use `assert` for all verifications
- Each test is independent (navigates on its own)

---

## Exercise 2: Fixtures and Parametrize

```python
"""Exercise 2 Solution: Fixtures and Parametrize"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# FIXTURES
# ============================================

@pytest.fixture
def checkbox_page(page: Page):
    """Navigate to checkboxes page."""
    page.goto(f"{BASE_URL}/checkboxes")
    return page


@pytest.fixture
def dropdown_page(page: Page):
    """Navigate to dropdown page."""
    page.goto(f"{BASE_URL}/dropdown")
    return page


@pytest.fixture
def input_page(page: Page):
    """Navigate to inputs page."""
    page.goto(f"{BASE_URL}/inputs")
    return page


# ============================================
# TESTS USING FIXTURES
# ============================================

@pytest.mark.smoke
def test_checkboxes_visible(checkbox_page):
    """Verify checkboxes are visible."""
    checkboxes = checkbox_page.locator("input[type='checkbox']")
    assert checkboxes.count() == 2
    assert checkboxes.first.is_visible()


@pytest.mark.smoke
def test_dropdown_visible(dropdown_page):
    """Verify dropdown is visible."""
    dropdown = dropdown_page.locator("#dropdown")
    assert dropdown.is_visible()


@pytest.mark.regression
def test_input_accepts_numbers(input_page):
    """Verify input field accepts numbers."""
    input_field = input_page.locator("input[type='number']")
    input_field.fill("42")
    assert input_field.input_value() == "42"


# ============================================
# PARAMETERIZED TESTS
# ============================================

@pytest.mark.regression
@pytest.mark.parametrize("value,expected_text", [
    ("1", "Option 1"),
    ("2", "Option 2"),
])
def test_dropdown_options(dropdown_page, value, expected_text):
    """Test selecting different dropdown options."""
    dropdown = dropdown_page.locator("#dropdown")
    dropdown.select_option(value=value)

    selected = dropdown.locator("option:checked")
    assert selected.text_content().strip() == expected_text


@pytest.mark.parametrize("username,password,should_succeed", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("wrong", "wrong", False),
    ("tomsmith", "bad_password", False),
])
def test_login_credentials(page: Page, username, password, should_succeed):
    """Test different login credentials."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    if should_succeed:
        assert "/secure" in page.url
    else:
        assert "/login" in page.url


# ============================================
# BONUS: FIXTURE WITH YIELD
# ============================================

@pytest.fixture
def add_remove_page(page: Page):
    """Fixture with setup and teardown."""
    # SETUP
    page.goto(f"{BASE_URL}/add_remove_elements/")

    yield page

    # TEARDOWN
    count = page.locator(".added-manually").count()
    print(f"\n[Teardown] {count} elements remaining")


@pytest.mark.regression
def test_add_elements(add_remove_page):
    """Test adding elements."""
    add_button = add_remove_page.locator("button", has_text="Add Element")

    # Click 3 times
    add_button.click()
    add_button.click()
    add_button.click()

    # Verify 3 delete buttons appear
    delete_buttons = add_remove_page.locator(".added-manually")
    assert delete_buttons.count() == 3
```

### Key Points:
- Fixtures eliminate duplicate `page.goto()` calls
- `@pytest.mark.parametrize` generates separate test cases
- Combine fixtures with parametrize (dropdown_page + values)
- `yield` in fixtures enables teardown code
- Markers categorize tests for selective execution

---

## Summary: Pytest Integration Patterns

```python
# Pattern 1: Basic test function
def test_something(page):
    page.goto("https://example.com")
    assert page.title() == "Expected"

# Pattern 2: Custom fixture
@pytest.fixture
def my_page(page):
    page.goto("https://example.com")
    return page

def test_with_fixture(my_page):
    assert my_page.title() == "Expected"

# Pattern 3: Parametrize
@pytest.mark.parametrize("input,expected", [
    ("value1", "result1"),
    ("value2", "result2"),
])
def test_with_data(page, input, expected):
    # Test with each data set
    pass

# Pattern 4: Markers
@pytest.mark.smoke
def test_critical(page):
    pass  # Run with: pytest -m smoke

# Pattern 5: Fixture with yield
@pytest.fixture
def setup_page(page):
    # Setup
    page.goto("https://example.com")
    yield page
    # Teardown
    print("Done!")
```

---

## Common Mistakes to Avoid

### Mistake 1: Wrong file/function naming
```python
# WRONG - won't be discovered
# File: login_test.py
def check_login(page):  # Doesn't start with test_
    pass

# CORRECT
# File: test_login.py
def test_login(page):  # Starts with test_
    pass
```

### Mistake 2: Forgetting the page parameter
```python
# WRONG - no page fixture
def test_something():
    page.goto("...")  # NameError!

# CORRECT - page as parameter
def test_something(page):
    page.goto("...")
```

### Mistake 3: Not using assert
```python
# WRONG - no assertion, always passes
def test_title(page):
    page.goto("https://example.com")
    page.title()  # Returns value but doesn't check it

# CORRECT - assert checks the value
def test_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

### Mistake 4: Tests depending on each other
```python
# WRONG - test_b depends on test_a running first
def test_a_login(page):
    page.goto("/login")
    page.locator("#user").fill("admin")
    # Stores state...

def test_b_check_profile(page):
    # Assumes we're logged in from test_a
    # But page is FRESH! This will fail.
    pass

# CORRECT - each test is independent
def test_check_profile(page):
    # Login in this test
    page.goto("/login")
    page.locator("#user").fill("admin")
    # ... then check profile
```
