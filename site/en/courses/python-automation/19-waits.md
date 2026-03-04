# Lecture 19: Wait Strategies

Wait strategies.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_19_Wait_Strategies/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_19_Wait_Strategies/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_19_Wait_Strategies/exercises" target="_blank">📝 Вправи</a>
</div>

## Auto-waiting

Playwright automatically waits for:
- Element is visible
- Element is stable
- Element is available for interaction
- Element is enabled

```python
# Waits automatically
page.get_by_role("button").click()
```

## Waiting for Elements

```python
# Wait for appearance
page.wait_for_selector("button.loaded")

# Wait for visibility
page.wait_for_selector("button", state="visible")

# Wait for disappearance
page.wait_for_selector(".loading", state="hidden")

# Wait for attachment to DOM
page.wait_for_selector("button", state="attached")
```

## Waiting for Navigation

```python
# Wait for URL
page.wait_for_url("**/dashboard")
page.wait_for_url("https://example.com/success")

# Wait for page load
page.wait_for_load_state("load")
page.wait_for_load_state("domcontentloaded")
page.wait_for_load_state("networkidle")
```

## Waiting for Network

```python
# Wait for response
with page.expect_response("**/api/users") as response_info:
    page.get_by_role("button").click()
response = response_info.value

# Wait for request
with page.expect_request("**/api/submit") as request_info:
    page.get_by_role("button", name="Submit").click()
```

## Timeouts

```python
# Global timeout
page.set_default_timeout(30000)

# Timeout for a specific action
page.get_by_role("button").click(timeout=5000)

# Timeout for navigation
page.goto("https://example.com", timeout=60000)
```

## ❌ What NOT to Do

```python
# NEVER use sleep!
import time
time.sleep(5)  # ❌ BAD!

# Instead use
page.wait_for_selector(".loaded")  # ✅ GOOD
expect(page.get_by_text("Ready")).to_be_visible()  # ✅ GOOD
```
