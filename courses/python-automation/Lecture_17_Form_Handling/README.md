# Lecture 17: Form Handling

Master form automation with Playwright - fill inputs, check boxes, select options, upload files, and validate submissions.

## Topics Covered
1. **Text Inputs** - fill() vs type()
2. **Checkboxes & Radio Buttons** - check(), uncheck(), set_checked()
3. **Dropdowns** - select_option()
4. **File Uploads** - set_input_files()
5. **Special Inputs** - Date pickers, range sliders, color pickers
6. **Form Submission** - Submit and validate
7. **Best Practices** - Reliable form testing

## Quick Reference

### Text Inputs
```python
# fill() - Fast (recommended)
page.locator("#email").fill("user@example.com")
page.get_by_label("Password").fill("SecurePass123")

# type() - Slow, character-by-character
page.locator("#search").type("query", delay=50)
```

### Checkboxes
```python
page.locator("#terms").check()           # Check
page.locator("#newsletter").uncheck()    # Uncheck
page.locator("#remember").set_checked(True)  # Set to specific state
is_checked = page.locator("#terms").is_checked()  # Verify
```

### Radio Buttons
```python
page.get_by_label("Credit Card").check()
page.locator("input[name='payment'][value='paypal']").check()
```

### Dropdowns
```python
# Select by label (recommended)
page.locator("#country").select_option(label="United States")

# Select by value
page.locator("#country").select_option("us")

# Select multiple (multi-select)
page.locator("#skills").select_option(["python", "javascript"])
```

### File Uploads
```python
page.locator("input[type='file']").set_input_files("document.pdf")
page.locator("#upload").set_input_files(["file1.jpg", "file2.pdf"])
```

### Special Inputs
```python
# Date picker (YYYY-MM-DD)
page.locator("#birthday").fill("1990-06-15")

# DateTime local (YYYY-MM-DDTHH:MM)
page.locator("#meeting").fill("2024-12-25T14:30")

# Range slider
page.locator("#volume").fill("75")

# Color picker (hex)
page.locator("#color").fill("#ff5733")

# Week picker (YYYY-Www)
page.locator("#week").fill("2024-W51")

# Month picker (YYYY-MM)
page.locator("#month").fill("2024-12")
```

### Form Submission
```python
# Fill and submit
page.get_by_label("Email").fill("user@example.com")
page.get_by_role("button", name="Submit").click()

# Verify success
page.wait_for_selector(".success-message")
assert page.locator(".success-message").is_visible()
```

## Examples

| File | Description |
|------|-------------|
| `01_text_inputs.py` | fill() vs type() demonstration |
| `02_checkboxes_radios.py` | Working with checkboxes and radio buttons |
| `03_dropdowns.py` | Dropdown selection methods |
| `04_complete_form.py` | Complete registration form example |
| `05_special_inputs.py` | Date pickers, range sliders, color pickers |

## Exercises

| Exercise | Topic | Difficulty |
|----------|-------|------------|
| `exercise_01_login_form.py` | Text inputs & buttons | Easy |
| `exercise_02_checkboxes.py` | Checkboxes | Easy |
| `exercise_03_dropdowns.py` | Dropdown selection | Medium |
| `exercise_04_file_upload.py` | File uploads | Medium |

Solutions are available in `exercises/SOLUTIONS.md`.

## Best Practices
- ✅ Use fill() instead of type() (faster)
- ✅ Use get_by_label() for inputs
- ✅ Always verify form submission
- ✅ Test both success and error cases
- ✅ Wait for elements before interacting
- ✅ Use absolute paths for file uploads
- ❌ Don't skip validation checks
- ❌ Don't use brittle selectors
- ❌ Don't hardcode file paths

## Resources

- [Playwright Input Documentation](https://playwright.dev/python/docs/input)
- [Playwright Locators](https://playwright.dev/python/docs/locators)
- [Ukrainian Transcript](transcript_ua.md)
