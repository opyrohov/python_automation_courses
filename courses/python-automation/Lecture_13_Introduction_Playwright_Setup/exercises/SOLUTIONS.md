# Exercise Solutions - Lecture 13

Complete solutions for all Lecture 13 exercises.

## Exercise 1: Installation Verification

All tasks are verification steps - if they pass, your installation is correct!

**If anything fails:**
- Ensure virtual environment is activated
- Run `pip install playwright pytest pytest-playwright`
- Run `playwright install`

---

## Exercise 2: First Script Solutions

### Exercise 1: Open Browser

```python
def exercise_1_open_browser():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Create new page
        page = browser.new_page()

        # Navigate
        page.goto("https://example.com")

        # Print title
        title = page.title()
        print(f"Page title: {title}")

        # Close
        browser.close()
```

### Exercise 2: Multiple Pages

```python
def exercise_2_multiple_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Page 1
        page1 = browser.new_page()
        page1.goto("https://example.com")
        print(f"Page 1 title: {page1.title()}")

        # Page 2
        page2 = browser.new_page()
        page2.goto("https://playwright.dev")
        print(f"Page 2 title: {page2.title()}")

        # Close
        browser.close()
```

### Exercise 3: Take Screenshot

```python
def exercise_3_take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://playwright.dev")
        page.screenshot(path="my_screenshot.png")

        print("✅ Screenshot saved as my_screenshot.png")

        browser.close()
```

### Exercise 4: Get Page Info

```python
def exercise_4_get_page_info():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://playwright.dev")

        print(f"Title: {page.title()}")
        print(f"URL: {page.url}")
        print(f"Content length: {len(page.content())} characters")

        browser.close()
```

### Exercise 5: Different Browsers

```python
def exercise_5_different_browsers():
    with sync_playwright() as p:
        # Chromium
        browser1 = p.chromium.launch(headless=False)
        page1 = browser1.new_page()
        page1.goto("https://example.com")
        print(f"Chromium title: {page1.title()}")

        # Firefox
        browser2 = p.firefox.launch(headless=False)
        page2 = browser2.new_page()
        page2.goto("https://example.com")
        print(f"Firefox title: {page2.title()}")

        # WebKit
        browser3 = p.webkit.launch(headless=False)
        page3 = browser3.new_page()
        page3.goto("https://example.com")
        print(f"WebKit title: {page3.title()}")

        # Close all
        browser1.close()
        browser2.close()
        browser3.close()
```

### Exercise 6: Navigation

```python
def exercise_6_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to example.com
        page.goto("https://example.com")
        print(f"1. {page.title()}")

        # Navigate to playwright.dev
        page.goto("https://playwright.dev")
        print(f"2. {page.title()}")

        # Go back
        page.go_back()
        print(f"3. Back: {page.title()}")

        # Go forward
        page.go_forward()
        print(f"4. Forward: {page.title()}")

        # Reload
        page.reload()
        print(f"5. Reloaded: {page.title()}")

        browser.close()
```

### Exercise 7: Slow Motion

```python
def exercise_7_slow_motion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://playwright.dev")
        page.click("a:has-text('Get started')")
        page.wait_for_timeout(2000)

        browser.close()
```

### Exercise 8: Your Favorite Website (Example)

```python
def exercise_8_your_favorite_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to GitHub
        page.goto("https://github.com")

        # Print info
        print(f"Title: {page.title()}")
        print(f"URL: {page.url}")

        # Take screenshot
        page.screenshot(path="github.png")
        print("✅ Screenshot saved!")

        # Wait 5 seconds
        page.wait_for_timeout(5000)

        browser.close()
```

---

## Exercise 3: Pytest Tests Solutions

### Test 1: example.com

```python
def test_example_com(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    expect(page).to_have_url("https://example.com/")
```

### Test 2: Playwright Homepage

```python
def test_playwright_homepage(page: Page):
    page.goto("https://playwright.dev")
    expect(page).to_have_title("Playwright")
    expect(page).to_have_url("https://playwright.dev/")
```

### Test 3: Get Started Button

```python
def test_get_started_button_exists(page: Page):
    page.goto("https://playwright.dev")
    get_started = page.locator("a:has-text('Get started')")
    expect(get_started).to_be_visible()
```

### Test 4: Navigation to Docs

```python
def test_navigation_to_docs(page: Page):
    page.goto("https://playwright.dev")
    page.click("a:has-text('Get started')")
    expect(page).to_have_url("**/docs/intro")
```

### Test 5: Take Screenshot

```python
def test_take_screenshot(page: Page):
    page.goto("https://playwright.dev")
    page.screenshot(path="test_screenshot.png")
    expect(page).to_have_title("Playwright")
```

### Test 6: Full Page Screenshot

```python
def test_full_page_screenshot(page: Page):
    page.goto("https://example.com")
    page.screenshot(path="full_page.png", full_page=True)
```

### Test 7: Multiple URLs

```python
@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://playwright.dev",
])
def test_multiple_urls(page: Page, url: str):
    page.goto(url)
    title = page.title()
    print(f"URL: {url}, Title: {title}")
    assert len(title) > 0
```

### Test 8: Smoke Test

```python
@pytest.mark.smoke
def test_smoke_quick_check(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
```

### Test 9: Slow Test

```python
@pytest.mark.slow
def test_slow_operation(page: Page):
    page.goto("https://playwright.dev")
    page.wait_for_timeout(2000)
    expect(page).to_have_title("Playwright")
```

### Test 10: Get Page Info

```python
def test_get_page_info(page: Page):
    page.goto("https://playwright.dev")

    title = page.title()
    url = page.url
    viewport = page.viewport_size

    print(f"Title: {title}")
    print(f"URL: {url}")
    print(f"Viewport: {viewport}")

    expect(page).to_have_title("Playwright")
```

### Test 11: 404 Page

```python
def test_404_page(page: Page):
    response = page.goto("https://playwright.dev/this-page-does-not-exist")

    assert response.status == 404
    expect(page.locator("body")).to_contain_text("Page Not Found")
```

### Test 12: Your Own Website (Example)

```python
def test_your_own_website(page: Page):
    # Example: Testing Python.org
    page.goto("https://www.python.org")

    # Verify title
    expect(page).to_have_title("*Python*")

    # Check search box is visible
    search = page.locator("input[name='q']")
    expect(search).to_be_visible()

    # Take screenshot
    page.screenshot(path="python_org.png")

    print("✅ Python.org test passed!")
```

---

## Running Tests

```bash
# Run all tests
pytest exercise_03_pytest_tests.py

# Run in headed mode
pytest exercise_03_pytest_tests.py --headed

# Run specific test
pytest exercise_03_pytest_tests.py::test_example_com

# Run with verbose output
pytest exercise_03_pytest_tests.py -v

# Run only smoke tests
pytest exercise_03_pytest_tests.py -m smoke

# Run with specific browser
pytest exercise_03_pytest_tests.py --browser firefox

# Run with slow motion (helpful for debugging)
pytest exercise_03_pytest_tests.py --headed --slowmo 1000
```

---

## Common Mistakes and Solutions

### Mistake 1: Forgetting to activate venv
**Error:** `playwright: command not found`

**Solution:**
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### Mistake 2: Browsers not installed
**Error:** `Executable doesn't exist`

**Solution:**
```bash
playwright install
```

### Mistake 3: Wrong selector
**Error:** `Timeout waiting for selector`

**Solution:**
- Use browser DevTools to inspect element
- Try different selector types (CSS, text, role)
- Use `page.pause()` to debug interactively

### Mistake 4: Not using expect()
**Bad:**
```python
assert page.is_visible(".element")  # No auto-waiting!
```

**Good:**
```python
expect(page.locator(".element")).to_be_visible()  # Auto-waits!
```

### Mistake 5: Hardcoded waits
**Bad:**
```python
import time
time.sleep(5)  # Bad practice!
```

**Good:**
```python
page.wait_for_selector(".element")  # Wait for specific condition
# or
expect(page.locator(".element")).to_be_visible()  # Auto-waits
```

---

## Best Practices Demonstrated

1. ✅ **Use `expect()` for assertions** - Auto-waiting built-in
2. ✅ **Use `page` fixture** - Cleaner code with pytest-playwright
3. ✅ **Use meaningful test names** - Describe what's being tested
4. ✅ **One test = one thing** - Keep tests focused
5. ✅ **Use markers** - Organize tests (@pytest.mark.smoke)
6. ✅ **Avoid hardcoded waits** - Use Playwright's smart waiting
7. ✅ **Use headless in CI** - Faster execution
8. ✅ **Use headed for debugging** - See what's happening

---

## Next Steps

After completing these exercises:
1. ✅ You can write basic Playwright scripts
2. ✅ You understand browser automation basics
3. ✅ You can run tests with pytest
4. ✅ You know debugging tools (headed, slow-mo, pause)

**Ready for Lecture 14: Playwright Locators & Interactions!** 🚀

---

## Additional Practice Ideas

1. **Test your own website** - Automate logging into a site you use
2. **Cross-browser testing** - Run same test on all three browsers
3. **Screenshot comparison** - Take screenshots of same page in different browsers
4. **Form automation** - Practice filling out forms
5. **Navigation testing** - Test multi-page workflows

Keep practicing! The more you code, the better you'll get! 💪
