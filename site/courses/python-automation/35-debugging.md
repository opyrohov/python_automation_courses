# Lecture 35: Debugging Techniques

Техніки налагодження.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_35_Debugging_Techniques/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_35_Debugging_Techniques/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_35_Debugging_Techniques/exercises)

</div>

## Playwright Inspector

```python
# Відкриває Inspector для debugging
PWDEBUG=1 pytest tests/test_login.py

# Або в коді
page.pause()  # Зупиняє виконання
```

## Headed mode

```python
# pytest.ini
[pytest]
headed = true
slowmo = 500

# Або в коді
browser = p.chromium.launch(
    headless=False,
    slow_mo=500
)
```

## Скріншоти при помилках

```python
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page

    # Скріншот при падінні тесту
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

# ... тест

context.tracing.stop(path="trace.zip")

# Переглянути
# npx playwright show-trace trace.zip
```

## Console logs

```python
# Логування всіх console.log з браузера
page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

# Фільтрація
page.on("console", lambda msg:
    print(f"ERROR: {msg.text}") if msg.type == "error" else None
)
```

## Network logs

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

## Breakpoints в IDE

```python
def test_login(page):
    page.goto("/login")
    breakpoint()  # Зупинка тут
    page.get_by_label("Email").fill("test@example.com")
```

## Verbose pytest output

```bash
# Максимально детальний вивід
pytest -vvv --tb=long

# Показати print statements
pytest -s

# Показати локальні змінні при помилці
pytest -l
```
