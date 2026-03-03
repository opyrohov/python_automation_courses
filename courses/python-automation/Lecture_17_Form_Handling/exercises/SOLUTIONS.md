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

## Exercise 3: Dropdowns

```python
from playwright.sync_api import sync_playwright

def dropdown_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/login")

        page.get_by_placeholder("Name").first.fill("Test User")
        page.get_by_placeholder("Email Address").nth(1).fill("dropdown_test@example.com")
        page.get_by_role("button", name="Signup").click()

        # Solution 1: Select day of birth
        page.locator("#days").select_option("15")

        # Solution 2: Select month of birth
        page.locator("#months").select_option("March")

        # Solution 3: Select year of birth
        page.locator("#years").select_option("1995")

        # Solution 4: Select country using label parameter
        page.locator("#country").select_option(label="Canada")

        # Solution 5: Verify country selection
        selected_country = page.locator("#country").input_value()
        assert selected_country == "Canada", f"Expected 'Canada', got '{selected_country}'"

        print("✓ Exercise 3 complete!")
        browser.close()
```

## Exercise 4: File Upload

```python
from playwright.sync_api import sync_playwright
import os

def file_upload_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Create a test file to upload
        test_file_path = os.path.join(os.path.dirname(__file__), "test_upload.txt")
        with open(test_file_path, "w") as f:
            f.write("This is a test file for upload exercise.")

        page.goto("https://www.automationexercise.com/contact_us")

        # Fill out the contact form
        page.get_by_placeholder("Name").fill("Test User")
        page.get_by_placeholder("Email", exact=False).first.fill("test@example.com")
        page.get_by_placeholder("Subject").fill("Test Subject")
        page.locator("#message").fill("This is a test message with file attachment.")

        # Solution 1: Upload the test file
        page.locator("input[name='upload_file']").set_input_files(test_file_path)

        # Handle dialog before clicking submit
        page.on("dialog", lambda dialog: dialog.accept())

        # Solution 2: Click the Submit button
        page.get_by_role("button", name="Submit").click()

        print("✓ Exercise 4 complete!")

        # Cleanup
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

        browser.close()
```

## Key Takeaways

### Text Inputs
- Use **fill()** for text inputs (fast and reliable)
- Use **type()** only for autocomplete or special cases

### Checkboxes & Radio Buttons
- Use **check()/uncheck()** for checkboxes
- Use **is_checked()** to verify checkbox state
- These methods are idempotent (safe to call multiple times)

### Dropdowns
- Use **select_option()** for native `<select>` elements
- Select by value: `select_option("value")`
- Select by label: `select_option(label="Visible Text")`
- Select by index: `select_option(index=0)`
- Use **input_value()** to get selected value

### File Uploads
- Use **set_input_files()** for file upload inputs
- Pass single file: `set_input_files("path/to/file")`
- Pass multiple files: `set_input_files(["file1", "file2"])`
- Clear files: `set_input_files([])`

### Form Validation
- Always **verify** form submission results
- Check for success messages or URL changes
- Test both success and error scenarios
