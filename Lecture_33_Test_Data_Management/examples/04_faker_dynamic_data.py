"""Example 4: Faker - Dynamic Test Data Generation

Demonstrates how to use the Faker library to generate
realistic test data dynamically.

Install: pip install faker
Run with: pytest 04_faker_dynamic_data.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page

try:
    from faker import Faker
    FAKER_AVAILABLE = True
except ImportError:
    FAKER_AVAILABLE = False
    print("Faker not installed. Run: pip install faker")


# ============================================
# BASIC FAKER USAGE
# ============================================

if FAKER_AVAILABLE:
    # English (default)
    fake = Faker()

    # Ukrainian locale
    fake_ua = Faker("uk_UA")

    # Multiple locales
    fake_multi = Faker(["en_US", "uk_UA"])


# ============================================
# FAKER FIXTURE
# ============================================

@pytest.fixture
def fake_data():
    """Provide Faker instance for tests."""
    if not FAKER_AVAILABLE:
        pytest.skip("Faker not installed")
    return Faker()


@pytest.fixture
def fake_ua_data():
    """Provide Ukrainian Faker instance."""
    if not FAKER_AVAILABLE:
        pytest.skip("Faker not installed")
    return Faker("uk_UA")


# ============================================
# COMMON FAKER METHODS (DEMO)
# ============================================

@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_faker_basics():
    """Demonstrate common Faker methods."""
    fake = Faker()

    # Personal data
    name = fake.name()
    first = fake.first_name()
    last = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()

    print(f"\n  Name: {name}")
    print(f"  First: {first}")
    print(f"  Last: {last}")
    print(f"  Email: {email}")
    print(f"  Phone: {phone}")

    # Address
    address = fake.address()
    city = fake.city()
    country = fake.country()

    print(f"\n  Address: {address}")
    print(f"  City: {city}")
    print(f"  Country: {country}")

    # Internet
    username = fake.user_name()
    password = fake.password(length=12)
    url = fake.url()

    print(f"\n  Username: {username}")
    print(f"  Password: {password}")
    print(f"  URL: {url}")

    # Text
    sentence = fake.sentence()
    paragraph = fake.paragraph()

    print(f"\n  Sentence: {sentence}")
    print(f"  Paragraph: {paragraph[:80]}...")

    assert name  # All should be non-empty
    assert email
    assert "@" in email


# ============================================
# UKRAINIAN LOCALE
# ============================================

@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_faker_ukrainian():
    """Generate Ukrainian test data."""
    fake = Faker("uk_UA")

    name = fake.name()
    address = fake.address()
    phone = fake.phone_number()

    print(f"\n  Ім'я: {name}")
    print(f"  Адреса: {address}")
    print(f"  Телефон: {phone}")

    assert name


# ============================================
# REPRODUCIBLE DATA WITH SEED
# ============================================

@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_faker_with_seed():
    """Seed makes data reproducible (same every run)."""
    Faker.seed(12345)
    fake = Faker()

    name1 = fake.name()
    email1 = fake.email()

    # Reset seed - get same data again
    Faker.seed(12345)
    fake2 = Faker()

    name2 = fake2.name()
    email2 = fake2.email()

    print(f"\n  Run 1: {name1}, {email1}")
    print(f"  Run 2: {name2}, {email2}")

    assert name1 == name2
    assert email1 == email2


# ============================================
# FAKER IN PLAYWRIGHT TESTS
# ============================================

BASE_URL = "https://the-internet.herokuapp.com"


@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_login_with_fake_data(page: Page):
    """Use Faker for invalid login credentials."""
    fake = Faker()

    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(fake.user_name())
    page.locator("#password").fill(fake.password())
    page.locator("button[type='submit']").click()

    # Random credentials should fail
    assert "/login" in page.url
    assert "invalid" in page.locator("#flash").text_content().lower()


@pytest.mark.skipif(not FAKER_AVAILABLE, reason="Faker not installed")
def test_input_with_fake_numbers(page: Page):
    """Use Faker for number input."""
    fake = Faker()
    number = str(fake.random_int(min=1, max=1000))

    page.goto(f"{BASE_URL}/inputs")
    input_field = page.locator("input[type='number']")
    input_field.fill(number)
    assert input_field.input_value() == number
    print(f"\n  Entered: {number}")


# ============================================
# FAKER DATA FACTORY FIXTURE
# ============================================

@pytest.fixture
def user_factory():
    """Factory fixture - generate user data on demand."""
    if not FAKER_AVAILABLE:
        pytest.skip("Faker not installed")

    fake = Faker()

    def create_user(locale=None):
        f = Faker(locale) if locale else fake
        return {
            "first_name": f.first_name(),
            "last_name": f.last_name(),
            "email": f.email(),
            "username": f.user_name(),
            "password": f.password(length=12),
            "phone": f.phone_number(),
            "address": f.address(),
        }

    return create_user


def test_with_user_factory(user_factory):
    """Test using factory fixture."""
    user = user_factory()
    print(f"\n  Generated user: {user['first_name']} {user['last_name']}")
    print(f"  Email: {user['email']}")

    ua_user = user_factory(locale="uk_UA")
    print(f"  UA user: {ua_user['first_name']} {ua_user['last_name']}")

    assert user["email"] != ua_user["email"]


# ============================================
# KEY POINTS:
#
# 1. pip install faker
# 2. Faker() - English, Faker("uk_UA") - Ukrainian
# 3. .name(), .email(), .address(), etc.
# 4. Faker.seed(N) for reproducible data
# 5. Factory fixtures for on-demand generation
# 6. Great for invalid/random test data
# 7. Use seeds in CI for reproducibility
#
# Run: pytest 04_faker_dynamic_data.py -v -s --headed
# ============================================
