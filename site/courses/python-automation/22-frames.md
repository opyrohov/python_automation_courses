# Лекція 22: Frames та iframes

Робота з фреймами та iframe.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_22_Frames_iframes/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/exercises" target="_blank">📝 Вправи</a>
</div>

## Теми лекції

- Що таке iframe
- Пошук та взаємодія з iframe
- Вкладені фрейми
- Frame locators

## Що таке iframe?

`<iframe>` — це вбудована сторінка всередині основної сторінки. Кожен iframe має свій DOM.

```html
<iframe src="https://example.com/widget" name="widget"></iframe>
```

## Доступ до iframe

```python
# По імені
frame = page.frame(name="widget")

# По URL
frame = page.frame(url="**/widget")

# По селектору
frame = page.frame_locator("iframe.payment").first

# Всі фрейми
for frame in page.frames:
    print(frame.url)
```

## Frame Locators (рекомендовано)

```python
# Frame locator - найзручніший спосіб
payment_frame = page.frame_locator("#payment-iframe")

# Взаємодія з елементами всередині
payment_frame.get_by_placeholder("Card number").fill("4111111111111111")
payment_frame.get_by_role("button", name="Pay").click()

# Assertions
from playwright.sync_api import expect
expect(payment_frame.get_by_text("Payment successful")).to_be_visible()
```

## Вкладені фрейми

```python
# Доступ до вкладеного фрейму
outer_frame = page.frame_locator("#outer")
inner_frame = outer_frame.frame_locator("#inner")

# Взаємодія
inner_frame.get_by_role("button").click()
```

## Приклад: Payment Widget

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/checkout")

    # Перемикаємось на iframe платіжної системи
    payment = page.frame_locator("iframe[name='payment']")

    # Заповнюємо форму оплати
    payment.get_by_placeholder("Card Number").fill("4111111111111111")
    payment.get_by_placeholder("MM/YY").fill("12/25")
    payment.get_by_placeholder("CVV").fill("123")

    # Натискаємо кнопку
    payment.get_by_role("button", name="Pay Now").click()

    # Повертаємось до основної сторінки
    expect(page.get_by_text("Thank you")).to_be_visible()

    browser.close()
```

## Старий API (frame objects)

```python
# Отримання frame object
frame = page.frame(name="widget")

# Навігація у фреймі
frame.goto("https://example.com")

# Взаємодія
frame.click("button")
frame.fill("input", "text")

# Повернення до parent
parent = frame.parent_frame
```

## Очікування фрейму

```python
# Очікування появи фрейму
page.wait_for_selector("iframe[name='widget']")

# Потім доступ
frame = page.frame_locator("iframe[name='widget']")
```

## Вправи

::: tip Вправа 1
Напишіть тест для взаємодії з Google reCAPTCHA iframe.
:::

::: tip Вправа 2
Створіть тест для заповнення платіжної форми в iframe.
:::

[Приклади коду на GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/examples)
