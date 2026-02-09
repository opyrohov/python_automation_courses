"""Example 3: Environment Variables and .env Files

Demonstrates how to use environment variables for sensitive data
(passwords, API keys, URLs) and load them from .env files.

Run with: pytest 03_environment_variables.py -v --headed
"""
import os
import pytest
from playwright.sync_api import Page


# ============================================
# BASIC ENVIRONMENT VARIABLES
# ============================================
# Environment variables are set in the OS:
#
# Windows:  set BASE_URL=https://the-internet.herokuapp.com
# Linux:    export BASE_URL=https://the-internet.herokuapp.com
# PowerShell: $env:BASE_URL = "https://the-internet.herokuapp.com"

# Reading environment variables
BASE_URL = os.environ.get("BASE_URL", "https://the-internet.herokuapp.com")
TEST_USERNAME = os.environ.get("TEST_USERNAME", "tomsmith")
TEST_PASSWORD = os.environ.get("TEST_PASSWORD", "SuperSecretPassword!")


# ============================================
# .env FILE
# ============================================
# Create a .env file in project root:
#
# .env:
# BASE_URL=https://the-internet.herokuapp.com
# TEST_USERNAME=tomsmith
# TEST_PASSWORD=SuperSecretPassword!
# HEADLESS=false
# SLOW_MO=500
#
# IMPORTANT: Add .env to .gitignore!

# Create sample .env file for demo
EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(EXAMPLES_DIR, ".env.example")

with open(ENV_FILE, "w") as f:
    f.write("""# Example .env file (copy to .env and fill in values)
# NEVER commit .env to git!

# Application
BASE_URL=https://the-internet.herokuapp.com

# Test Credentials
TEST_USERNAME=tomsmith
TEST_PASSWORD=SuperSecretPassword!

# Browser Settings
HEADLESS=false
SLOW_MO=500

# Environment
ENV=development
""")


# ============================================
# LOADING .env WITH python-dotenv
# ============================================
# pip install python-dotenv

try:
    from dotenv import load_dotenv

    # Load .env file (looks in current directory by default)
    load_dotenv()
    print("  .env file loaded with python-dotenv")
except ImportError:
    print("  python-dotenv not installed, using os.environ only")
    print("  Install: pip install python-dotenv")


# ============================================
# CONFIG CLASS
# ============================================

class Config:
    """Configuration loaded from environment variables."""

    BASE_URL = os.environ.get("BASE_URL", "https://the-internet.herokuapp.com")
    USERNAME = os.environ.get("TEST_USERNAME", "tomsmith")
    PASSWORD = os.environ.get("TEST_PASSWORD", "SuperSecretPassword!")
    HEADLESS = os.environ.get("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.environ.get("SLOW_MO", "0"))
    ENV = os.environ.get("ENV", "development")


# ============================================
# FIXTURES USING CONFIG
# ============================================

@pytest.fixture(scope="session")
def config():
    """Provide configuration to tests."""
    return Config()


@pytest.fixture(scope="session")
def base_url(config):
    """Base URL from config."""
    return config.BASE_URL


# ============================================
# TESTS
# ============================================

def test_homepage(page: Page, config):
    """Test using config object."""
    page.goto(config.BASE_URL)
    assert page.title() == "The Internet"


def test_login_with_env_credentials(page: Page, config):
    """Test login using credentials from environment."""
    page.goto(f"{config.BASE_URL}/login")
    page.locator("#username").fill(config.USERNAME)
    page.locator("#password").fill(config.PASSWORD)
    page.locator("button[type='submit']").click()
    assert "/secure" in page.url


def test_config_values(config):
    """Verify config is loaded correctly."""
    assert config.BASE_URL.startswith("https://")
    assert config.USERNAME  # Not empty
    assert config.PASSWORD  # Not empty
    print(f"\n  BASE_URL: {config.BASE_URL}")
    print(f"  ENV: {config.ENV}")
    print(f"  HEADLESS: {config.HEADLESS}")


# ============================================
# ENVIRONMENT-SPECIFIC CONFIGS
# ============================================

class DevConfig:
    BASE_URL = "https://dev.example.com"
    DB_NAME = "test_db"

class StagingConfig:
    BASE_URL = "https://staging.example.com"
    DB_NAME = "staging_db"

class ProdConfig:
    BASE_URL = "https://example.com"
    DB_NAME = "prod_db"

CONFIGS = {
    "development": DevConfig,
    "staging": StagingConfig,
    "production": ProdConfig,
}


def get_config():
    """Get config based on ENV environment variable."""
    env = os.environ.get("ENV", "development")
    return CONFIGS.get(env, DevConfig)


# ============================================
# KEY POINTS:
#
# 1. os.environ.get("KEY", "default") - safe reading
# 2. os.environ["KEY"] - raises KeyError if missing
# 3. .env file + python-dotenv for local dev
# 4. NEVER commit .env to git (.gitignore!)
# 5. Config class centralizes all settings
# 6. Environment-specific configs (dev/staging/prod)
# 7. Use fixtures to provide config to tests
#
# Run: pytest 03_environment_variables.py -v -s
# ============================================
