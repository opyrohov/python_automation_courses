# Lecture 19: Wait Strategies

Стратегії очікування.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_19_Wait_Strategies/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_19_Wait_Strategies/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_19_Wait_Strategies/exercises)

</div>

## Auto-waiting

Playwright автоматично чекає на:
- Елемент видимий
- Елемент стабільний
- Елемент доступний для взаємодії
- Елемент enabled

```python
# Автоматично чекає
page.get_by_role("button").click()
```

## Очікування елементів

```python
# Очікування появи
page.wait_for_selector("button.loaded")

# Очікування видимості
page.wait_for_selector("button", state="visible")

# Очікування зникнення
page.wait_for_selector(".loading", state="hidden")

# Очікування прикріплення до DOM
page.wait_for_selector("button", state="attached")
```

## Очікування навігації

```python
# Очікування URL
page.wait_for_url("**/dashboard")
page.wait_for_url("https://example.com/success")

# Очікування завантаження
page.wait_for_load_state("load")
page.wait_for_load_state("domcontentloaded")
page.wait_for_load_state("networkidle")
```

## Очікування мережі

```python
# Очікування response
with page.expect_response("**/api/users") as response_info:
    page.get_by_role("button").click()
response = response_info.value

# Очікування request
with page.expect_request("**/api/submit") as request_info:
    page.get_by_role("button", name="Submit").click()
```

## Таймаути

```python
# Глобальний таймаут
page.set_default_timeout(30000)

# Таймаут для конкретної дії
page.get_by_role("button").click(timeout=5000)

# Таймаут для навігації
page.goto("https://example.com", timeout=60000)
```

## ❌ Що НЕ робити

```python
# НІКОЛИ не використовуйте sleep!
import time
time.sleep(5)  # ❌ BAD!

# Замість цього
page.wait_for_selector(".loaded")  # ✅ GOOD
expect(page.get_by_text("Ready")).to_be_visible()  # ✅ GOOD
```
