# Lecture 35: Debugging Techniques

Debugging techniques.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_35_Debugging_Techniques/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_35_Debugging_Techniques/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_35_Debugging_Techniques/exercises" target="_blank">📝 Вправи</a>
</div>

## Playwright Inspector

```python
# Opens Inspector for debugging
PWDEBUG=1 pytest tests/test_login.py

# Or in code
page.pause()  # Pauses execution
```

## Headed mode

```python
# pytest.ini
[pytest]
headed = true
slowmo = 500

# Or in code
browser = p.chromium.launch(
    headless=False,
    slow_mo=500
)
```

## Screenshots on Failure

```python
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page

    # Screenshot on test failure
    if hasattr(page, "_test_failed") and page._test_failed:
        page.screenshot(path=f"screenshots/failure.png")
    context.close()

def test_example(page):
    try:
        # test code
        pass
    except Exception:
        page._test_failed = True
        raise
```

## Tracing

```python
context.tracing.start(
    screenshots=True,
    snapshots=True,
    sources=True
)

# ... test

context.tracing.stop(path="trace.zip")

# View
# npx playwright show-trace trace.zip
```

## Console Logs

```python
# Log all console.log from the browser
page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

# Filtering
page.on("console", lambda msg:
    print(f"ERROR: {msg.text}") if msg.type == "error" else None
)
```

## Network Logs

```python
page.on("request", lambda req:
    print(f">> {req.method} {req.url}")
)

page.on("response", lambda res:
    print(f"<< {res.status} {res.url}")
)

page.on("requestfailed", lambda req:
    print(f"FAILED: {req.url} - {req.failure}")
)
```

## Breakpoints in IDE

```python
def test_login(page):
    page.goto("/login")
    breakpoint()  # Stops here
    page.get_by_label("Email").fill("test@example.com")
```

## Verbose pytest output

```bash
# Maximum verbose output
pytest -vvv --tb=long

# Show print statements
pytest -s

# Show local variables on failure
pytest -l
```
