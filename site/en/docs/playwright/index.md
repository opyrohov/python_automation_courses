# Playwright

Documentation on Playwright for Python — a powerful tool for E2E testing of web applications.

## Sections

- [Setup](/en/docs/playwright/setup) - Installation and configuration
- [Locators](/en/docs/playwright/locators) - Element finding strategies
- [Actions](/en/docs/playwright/actions) - Interacting with elements
- [Assertions](/en/docs/playwright/assertions) - Checks and expectations
- [Waits](/en/docs/playwright/waits) - Waiting strategies
- [Page Object Model](/en/docs/playwright/page-object) - Test organization pattern
- [API Testing](/en/docs/playwright/api-testing) - API testing
- [Screenshots & Video](/en/docs/playwright/screenshots-video) - Test documentation

## Quick Start

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigation
    page.goto("https://example.com")

    # Locators
    page.get_by_role("button", name="Sign In").click()
    page.get_by_placeholder("Email").fill("user@test.com")

    # Assertions
    expect(page.get_by_text("Welcome")).to_be_visible()

    browser.close()
```

## Useful Links

- [Official Playwright Documentation](https://playwright.dev/python/)
- [Playwright GitHub](https://github.com/microsoft/playwright-python)
