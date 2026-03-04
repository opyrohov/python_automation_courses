# Playwright Setup

Playwright is a modern browser automation framework from Microsoft. In this section, we will cover the installation, configuration, and basic setup of Playwright for Python.

## Installation

To get started with Playwright, you need to install the package and download browsers.

```python
# Install Playwright via pip
pip install playwright

# Download browsers (Chromium, Firefox, WebKit)
playwright install

# Install only a specific browser
playwright install chromium
playwright install firefox
playwright install webkit
```

::: tip Tip
It is recommended to use a Python virtual environment to isolate project dependencies.
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install playwright
playwright install
```
:::

## Installation with pytest-playwright

For pytest integration, install the additional package:

```python
# Install pytest-playwright for convenient test integration
pip install pytest-playwright

# This will also automatically install playwright
playwright install
```

## Basic Configuration

### Launching the Browser

```python
from playwright.sync_api import sync_playwright

def basic_setup():
    with sync_playwright() as p:
        # Launch Chromium in visible mode
        browser = p.chromium.launch(headless=False)

        # Create a new context with settings
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="uk-UA",
            timezone_id="Europe/Kyiv",
        )

        # Create a new page
        page = context.new_page()
        page.goto("https://example.com")

        # Close resources
        context.close()
        browser.close()
```

### Browser Launch Options

```python
from playwright.sync_api import sync_playwright

def browser_options():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,          # Visible mode
            slow_mo=500,             # Delay between actions (ms)
            args=["--start-maximized"],  # Command line arguments
            devtools=True,           # Open DevTools
        )

        # Context with extended settings
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Custom User Agent",
            locale="uk-UA",
            timezone_id="Europe/Kyiv",
            geolocation={"longitude": 30.5234, "latitude": 50.4501},
            permissions=["geolocation"],
            color_scheme="dark",     # Dark theme
            ignore_https_errors=True,
        )

        page = context.new_page()
        page.goto("https://example.com")

        browser.close()
```

## pytest-playwright Configuration

### conftest.py File

```python
import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Browser context settings for all tests."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "uk-UA",
        "timezone_id": "Europe/Kyiv",
        "ignore_https_errors": True,
    }

@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a new page with basic settings."""
    page = context.new_page()
    # Set default timeout
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)
    yield page
    page.close()

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Fixture for an authenticated page."""
    page.goto("https://example.com/login")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")
    return page
```

### pytest.ini File

```ini
[pytest]
# Settings for pytest-playwright
addopts = --browser chromium --headed --slowmo 100
# Other useful options:
# --browser firefox
# --browser webkit
# --browser-channel chrome
# --headed (visible mode)
# --slowmo 100 (100ms delay)
```

::: warning Warning
The `--headed` parameter enables visible browser mode. For CI/CD, use `headless` mode (default).
:::

## Saving Authentication State

```python
from playwright.sync_api import sync_playwright

def save_auth_state():
    """Save authentication state for reuse."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Perform authentication
        page.goto("https://example.com/login")
        page.get_by_label("Email").fill("user@test.com")
        page.get_by_label("Password").fill("secret123")
        page.get_by_role("button", name="Sign In").click()
        page.wait_for_url("**/dashboard")

        # Save state to file
        context.storage_state(path="auth_state.json")
        browser.close()

def use_saved_auth():
    """Use saved authentication state."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Load saved state
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()

        # Already authenticated — navigate to protected page
        page.goto("https://example.com/dashboard")
        browser.close()
```

## CI/CD Setup

```yaml
# GitHub Actions configuration example
name: Playwright Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: |
          pip install pytest-playwright
          playwright install --with-deps chromium
      - name: Run tests
        run: pytest tests/ --browser chromium
      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: test-results/
```

::: info Information
In CI/CD environments, use `playwright install --with-deps` to automatically install system dependencies.
:::

## Useful Links

- [Official installation documentation](https://playwright.dev/python/docs/intro)
- [pytest-playwright configuration](https://playwright.dev/python/docs/test-runners)
- [Browser launch options](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch)
- [Saving authentication state](https://playwright.dev/python/docs/auth)
