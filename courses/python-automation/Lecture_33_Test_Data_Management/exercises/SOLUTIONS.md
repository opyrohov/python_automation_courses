# Solutions - Lecture 33: Test Data Management

## Exercise 1: Data-Driven Tests from JSON and CSV

```python
"""Exercise 1 Solution: Data-Driven Tests"""
import json
import csv
import os
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"
EXERCISE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(EXERCISE_DIR, "test_data")


# ============================================
# CREATE DATA FILES
# ============================================

os.makedirs(DATA_DIR, exist_ok=True)

# login_scenarios.json
login_data = {
    "valid": {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    },
    "invalid": [
        {
            "username": "wrong",
            "password": "wrong",
            "error": "Your username is invalid!"
        },
        {
            "username": "tomsmith",
            "password": "bad",
            "error": "Your password is invalid!"
        }
    ]
}

with open(os.path.join(DATA_DIR, "login_scenarios.json"), "w") as f:
    json.dump(login_data, f, indent=2)

# dropdown_options.csv
with open(os.path.join(DATA_DIR, "dropdown_options.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["value", "expected_text"])
    writer.writerow(["1", "Option 1"])
    writer.writerow(["2", "Option 2"])


# ============================================
# HELPER FUNCTIONS
# ============================================

def load_json(filename):
    """Load JSON from test_data/ directory."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_csv(filename):
    """Load CSV from test_data/ directory as list of dicts."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ============================================
# LOAD DATA
# ============================================

LOGIN_DATA = load_json("login_scenarios.json")
DROPDOWN_DATA = load_csv("dropdown_options.csv")


# ============================================
# TESTS
# ============================================

def test_valid_login(page: Page):
    """Login with valid credentials from JSON."""
    user = LOGIN_DATA["valid"]
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


@pytest.mark.parametrize("user", LOGIN_DATA["invalid"],
                         ids=lambda u: u["username"] or "empty")
def test_invalid_login(page: Page, user):
    """Parametrized invalid login from JSON."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("button[type='submit']").click()
    assert user["error"] in page.locator("#flash").text_content()


@pytest.mark.parametrize("row", DROPDOWN_DATA,
                         ids=lambda r: f"option-{r['value']}")
def test_dropdown_selection(page: Page, row):
    """Parametrized dropdown test from CSV."""
    page.goto(f"{BASE_URL}/dropdown")
    page.locator("#dropdown").select_option(value=row["value"])
    selected = page.locator("#dropdown option:checked")
    assert row["expected_text"] in selected.text_content()
```

### Key Points:
- JSON loaded once at module level (not in each test)
- `ids=` for readable test names in output
- CSV data loaded as list of dicts with DictReader
- Data files created programmatically for the exercise

---

## Exercise 2: Configuration with .env and Faker

### .env.example
```
# Copy this file to .env and fill in values
BASE_URL=https://the-internet.herokuapp.com
TEST_USERNAME=tomsmith
TEST_PASSWORD=SuperSecretPassword!
HEADLESS=true
```

### Solution
```python
"""Exercise 2 Solution: Config and Faker"""
import os
import pytest
from playwright.sync_api import Page

# Load .env if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ============================================
# CONFIG CLASS
# ============================================

class Config:
    """Configuration from environment variables."""
    BASE_URL = os.environ.get("BASE_URL", "https://the-internet.herokuapp.com")
    TEST_USERNAME = os.environ.get("TEST_USERNAME", "tomsmith")
    TEST_PASSWORD = os.environ.get("TEST_PASSWORD", "SuperSecretPassword!")
    HEADLESS = os.environ.get("HEADLESS", "true").lower() == "true"


# ============================================
# FIXTURES
# ============================================

@pytest.fixture(scope="session")
def config():
    """Provide Config to tests."""
    return Config()


@pytest.fixture
def fake():
    """Provide Faker instance."""
    try:
        from faker import Faker
        return Faker()
    except ImportError:
        pytest.skip("Faker not installed")


@pytest.fixture
def user_factory():
    """Factory that generates user data on demand."""
    try:
        from faker import Faker
        fake = Faker()
    except ImportError:
        pytest.skip("Faker not installed")

    def create_user():
        return {
            "name": fake.name(),
            "email": fake.email(),
            "username": fake.user_name(),
            "password": fake.password(length=12),
        }

    return create_user


# ============================================
# TESTS
# ============================================

def test_config_loaded(config):
    """Verify config values are set."""
    assert config.BASE_URL
    assert config.TEST_USERNAME
    assert config.TEST_PASSWORD
    assert isinstance(config.HEADLESS, bool)
    print(f"\n  URL: {config.BASE_URL}")
    print(f"  User: {config.TEST_USERNAME}")
    print(f"  Headless: {config.HEADLESS}")


def test_login_with_config(page: Page, config):
    """Login using Config credentials."""
    page.goto(f"{config.BASE_URL}/login")
    page.locator("#username").fill(config.TEST_USERNAME)
    page.locator("#password").fill(config.TEST_PASSWORD)
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


def test_invalid_login_with_faker(page: Page, config, fake):
    """Use Faker for random invalid credentials."""
    page.goto(f"{config.BASE_URL}/login")
    username = fake.user_name()
    password = fake.password()
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()
    assert "/login" in page.url
    print(f"\n  Tried: {username} / {password}")


def test_user_factory(user_factory):
    """Generate multiple users and verify uniqueness."""
    user1 = user_factory()
    user2 = user_factory()
    user3 = user_factory()
    print(f"\n  User 1: {user1['name']} ({user1['email']})")
    print(f"  User 2: {user2['name']} ({user2['email']})")
    print(f"  User 3: {user3['name']} ({user3['email']})")
    # All emails should be different
    emails = {user1["email"], user2["email"], user3["email"]}
    assert len(emails) == 3
```

### Key Points:
- Config class centralizes all environment settings
- `os.environ.get("KEY", "default")` with safe defaults
- Faker fixture with graceful skip if not installed
- Factory fixture returns a function (not data directly)
- Each `user_factory()` call generates fresh data

---

## Summary: Data Management Patterns

```python
# Pattern 1: JSON for complex data
data = load_json("test_data/users.json")
@pytest.mark.parametrize("user", data["invalid"])
def test_invalid(page, user): ...

# Pattern 2: CSV for tabular data
rows = load_csv("test_data/products.csv")
@pytest.mark.parametrize("row", rows)
def test_products(page, row): ...

# Pattern 3: .env for secrets
from dotenv import load_dotenv
load_dotenv()
URL = os.environ.get("BASE_URL")

# Pattern 4: Faker for dynamic data
@pytest.fixture
def fake():
    return Faker()

# Pattern 5: Factory for on-demand generation
@pytest.fixture
def user_factory():
    fake = Faker()
    def create():
        return {"name": fake.name(), "email": fake.email()}
    return create

# Pattern 6: Data class with caching
class TestData:
    _cache = {}
    @classmethod
    def load(cls, file):
        if file not in cls._cache:
            cls._cache[file] = json.load(open(file))
        return cls._cache[file]
```

---

## Common Mistakes to Avoid

### Mistake 1: Loading data in each test
```python
# WRONG - reads file for every test
def test_login(page):
    data = json.load(open("users.json"))  # Slow!

# CORRECT - load once
DATA = json.load(open("users.json"))
def test_login(page):
    user = DATA["valid"]
```

### Mistake 2: Committing .env to git
```
# .gitignore
.env          # NEVER commit!
.env.local
```

### Mistake 3: CSV types
```python
# WRONG - CSV value is string "true"
if row["active"]:  # Always truthy (non-empty string)!

# CORRECT - convert explicitly
if row["active"].lower() == "true":
```
