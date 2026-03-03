# Lecture 24: Screenshots & Videos

Скріншоти та відео запис.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_24_Screenshots_Videos/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_24_Screenshots_Videos/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_24_Screenshots_Videos/exercises)

</div>

## Screenshots

```python
# Скріншот сторінки
page.screenshot(path="screenshot.png")

# Повна сторінка (з прокруткою)
page.screenshot(path="full.png", full_page=True)

# Конкретний елемент
page.locator(".card").screenshot(path="card.png")

# В буфер (bytes)
screenshot_bytes = page.screenshot()
```

## Опції скріншотів

```python
page.screenshot(
    path="screenshot.png",
    full_page=True,
    type="png",  # або "jpeg"
    quality=80,  # для jpeg
    omit_background=True,  # прозорий фон
    clip={"x": 0, "y": 0, "width": 800, "height": 600}
)
```

## Video Recording

```python
# Запис відео при створенні контексту
context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 1280, "height": 720}
)

page = context.new_page()
page.goto("https://example.com")
# ... дії

# Відео зберігається при закритті контексту
context.close()

# Отримати шлях до відео
video_path = page.video.path()
```

## Tracing

```python
# Детальний trace для debugging
context.tracing.start(screenshots=True, snapshots=True, sources=True)

page.goto("https://example.com")
page.get_by_role("button").click()

# Зберегти trace
context.tracing.stop(path="trace.zip")

# Переглянути: npx playwright show-trace trace.zip
```

## pytest-playwright

```ini
# pytest.ini
[pytest]
screenshot = only-on-failure
video = retain-on-failure
tracing = retain-on-failure
```

```bash
# Командний рядок
pytest --screenshot on
pytest --video on
pytest --tracing on
```
