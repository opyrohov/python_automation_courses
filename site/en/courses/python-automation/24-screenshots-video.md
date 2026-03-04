# Lecture 24: Screenshots and Video

Screenshots and video recording.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_24_Screenshots_Videos/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_24_Screenshots_Videos/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_24_Screenshots_Videos/exercises" target="_blank">📝 Вправи</a>
</div>

## Screenshots

```python
# Page screenshot
page.screenshot(path="screenshot.png")

# Full page (with scrolling)
page.screenshot(path="full.png", full_page=True)

# Specific element
page.locator(".card").screenshot(path="card.png")

# To buffer (bytes)
screenshot_bytes = page.screenshot()
```

## Screenshot Options

```python
page.screenshot(
    path="screenshot.png",
    full_page=True,
    type="png",  # or "jpeg"
    quality=80,  # for jpeg
    omit_background=True,  # transparent background
    clip={"x": 0, "y": 0, "width": 800, "height": 600}
)
```

## Video Recording

```python
# Record video when creating a context
context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 1280, "height": 720}
)

page = context.new_page()
page.goto("https://example.com")
# ... actions

# Video is saved when the context is closed
context.close()

# Get the video path
video_path = page.video.path()
```

## Tracing

```python
# Detailed trace for debugging
context.tracing.start(screenshots=True, snapshots=True, sources=True)

page.goto("https://example.com")
page.get_by_role("button").click()

# Save trace
context.tracing.stop(path="trace.zip")

# View: npx playwright show-trace trace.zip
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
# Command line
pytest --screenshot on
pytest --video on
pytest --tracing on
```
