"""Exercise 2: Configuration with .env and Faker

Your task:
1. Create a Config class that reads from environment variables
2. Create a .env.example file with required variables
3. Use Faker to generate dynamic test data
4. Create a factory fixture for user generation

Requirements:

Config class:
- BASE_URL (default: https://the-internet.herokuapp.com)
- TEST_USERNAME (default: tomsmith)
- TEST_PASSWORD (default: SuperSecretPassword!)
- HEADLESS (default: true, convert to bool)

Fixtures:
- config: Returns Config instance (session scope)
- fake: Returns Faker instance
- user_factory: Returns function that creates user dicts

Tests:
- test_config_loaded: Verify config has all values
- test_login_with_config: Login using Config credentials
- test_invalid_login_with_faker: Use Faker for random invalid credentials
- test_user_factory: Generate multiple users and verify they're different

Run with: pytest exercise_02_config_and_faker.py -v --headed -s
"""
import os
import pytest
from playwright.sync_api import Page


# ============================================
# TODO: Create .env.example file
# ============================================
# Write a .env.example file with:
# BASE_URL=https://the-internet.herokuapp.com
# TEST_USERNAME=tomsmith
# TEST_PASSWORD=SuperSecretPassword!
# HEADLESS=true


# ============================================
# TODO: Config class
# ============================================

# class Config:
#     """Configuration from environment variables."""
#     BASE_URL = os.environ.get("BASE_URL", "https://the-internet.herokuapp.com")
#     # TODO: Add TEST_USERNAME, TEST_PASSWORD, HEADLESS


# ============================================
# TODO: Fixtures
# ============================================

# @pytest.fixture(scope="session")
# def config():
#     """Provide Config to tests."""
#     return Config()


# @pytest.fixture
# def fake():
#     """Provide Faker instance."""
#     try:
#         from faker import Faker
#         return Faker()
#     except ImportError:
#         pytest.skip("Faker not installed")


# @pytest.fixture
# def user_factory():
#     """Factory that generates user data."""
#     try:
#         from faker import Faker
#         fake = Faker()
#     except ImportError:
#         pytest.skip("Faker not installed")
#
#     def create_user():
#         return {
#             "name": fake.name(),
#             "email": fake.email(),
#             "username": fake.user_name(),
#             "password": fake.password(length=12),
#         }
#
#     return create_user


# ============================================
# TODO: Tests
# ============================================

# def test_config_loaded(config):
#     """Verify config values are set."""
#     assert config.BASE_URL
#     assert config.TEST_USERNAME
#     assert config.TEST_PASSWORD
#     print(f"\n  URL: {config.BASE_URL}")
#     print(f"  User: {config.TEST_USERNAME}")


# def test_login_with_config(page: Page, config):
#     """Login using Config credentials."""
#     page.goto(f"{config.BASE_URL}/login")
#     page.locator("#username").fill(config.TEST_USERNAME)
#     page.locator("#password").fill(config.TEST_PASSWORD)
#     page.locator("button[type='submit']").click()
#     assert "/secure" in page.url


# def test_invalid_login_with_faker(page: Page, config, fake):
#     """Use Faker for random invalid credentials."""
#     page.goto(f"{config.BASE_URL}/login")
#     page.locator("#username").fill(fake.user_name())
#     page.locator("#password").fill(fake.password())
#     page.locator("button[type='submit']").click()
#     assert "/login" in page.url


# def test_user_factory(user_factory):
#     """Generate multiple users and verify uniqueness."""
#     user1 = user_factory()
#     user2 = user_factory()
#     print(f"\n  User 1: {user1['name']} ({user1['email']})")
#     print(f"  User 2: {user2['name']} ({user2['email']})")
#     assert user1["email"] != user2["email"]
