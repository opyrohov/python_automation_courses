# Lecture 17: Form Handling

Master form automation with Playwright - fill inputs, check boxes, select options, upload files, and validate submissions.

## Topics Covered
1. **Text Inputs** - fill() vs type()
2. **Checkboxes & Radio Buttons** - check(), uncheck(), set_checked()
3. **Dropdowns** - select_option()
4. **File Uploads** - set_input_files()
5. **Form Submission** - Submit and validate
6. **Best Practices** - Reliable form testing

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

### Form Submission
```python
# Fill and submit
page.get_by_label("Email").fill("user@example.com")
page.get_by_role("button", name="Submit").click()

# Verify success
page.wait_for_selector(".success-message")
assert page.locator(".success-message").is_visible()
```

## Best Practices
- ✅ Use fill() instead of type() (faster)
- ✅ Use get_by_label() for inputs
- ✅ Always verify form submission
- ✅ Test both success and error cases
- ✅ Wait for elements before interacting
- ❌ Don't skip validation checks
- ❌ Don't use brittle selectors
