# Exercise Solutions - Lecture 17: Form Handling

## Exercise 1: Login Form

```python
from playwright.sync_api import sync_playwright

def login_form_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        # Solution 1: Fill email
        page.locator("[data-qa='login-email']").fill("test@example.com")

        # Solution 2: Fill password
        page.locator("[data-qa='login-password']").fill("password123")

        # Solution 3: Click login
        page.get_by_role("button", name="Login").click()

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()
```

## Exercise 2: Checkboxes

```python
from playwright.sync_api import sync_playwright

def checkbox_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        page.get_by_placeholder("Name").first.fill("Test User")
        page.get_by_placeholder("Email Address").nth(1).fill("test@example.com")
        page.get_by_role("button", name="Signup").click()

        # Solution 1: Check newsletter
        page.locator("#newsletter").check()

        # Solution 2: Check special offers
        page.locator("#optin").check()

        # Solution 3: Verify both checked
        assert page.locator("#newsletter").is_checked()
        assert page.locator("#optin").is_checked()

        print("✓ Exercise 2 complete!")
        browser.close()
```

## Key Takeaways
- Use **fill()** for text inputs (fast and reliable)
- Use **check()/uncheck()** for checkboxes
- Use **is_checked()** to verify checkbox state
- Use **select_option()** for dropdowns
- Always **verify** form submission results
