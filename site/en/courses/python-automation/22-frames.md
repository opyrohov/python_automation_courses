# Lecture 22: Frames and iframes

Working with frames and iframes.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_22_Frames_iframes/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/exercises" target="_blank">📝 Вправи</a>
</div>

## Lecture Topics

- What is an iframe
- Finding and interacting with iframes
- Nested frames
- Frame locators

## What is an iframe?

`<iframe>` is an embedded page inside the main page. Each iframe has its own DOM.

```html
<iframe src="https://example.com/widget" name="widget"></iframe>
```

## Accessing an iframe

```python
# By name
frame = page.frame(name="widget")

# By URL
frame = page.frame(url="**/widget")

# By selector
frame = page.frame_locator("iframe.payment").first

# All frames
for frame in page.frames:
    print(frame.url)
```

## Frame Locators (recommended)

```python
# Frame locator - the most convenient way
payment_frame = page.frame_locator("#payment-iframe")

# Interacting with elements inside
payment_frame.get_by_placeholder("Card number").fill("4111111111111111")
payment_frame.get_by_role("button", name="Pay").click()

# Assertions
from playwright.sync_api import expect
expect(payment_frame.get_by_text("Payment successful")).to_be_visible()
```

## Nested Frames

```python
# Accessing a nested frame
outer_frame = page.frame_locator("#outer")
inner_frame = outer_frame.frame_locator("#inner")

# Interaction
inner_frame.get_by_role("button").click()
```

## Example: Payment Widget

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/checkout")

    # Switch to the payment system iframe
    payment = page.frame_locator("iframe[name='payment']")

    # Fill out the payment form
    payment.get_by_placeholder("Card Number").fill("4111111111111111")
    payment.get_by_placeholder("MM/YY").fill("12/25")
    payment.get_by_placeholder("CVV").fill("123")

    # Click the button
    payment.get_by_role("button", name="Pay Now").click()

    # Return to the main page
    expect(page.get_by_text("Thank you")).to_be_visible()

    browser.close()
```

## Legacy API (frame objects)

```python
# Getting a frame object
frame = page.frame(name="widget")

# Navigation within a frame
frame.goto("https://example.com")

# Interaction
frame.click("button")
frame.fill("input", "text")

# Return to parent
parent = frame.parent_frame
```

## Waiting for a Frame

```python
# Wait for a frame to appear
page.wait_for_selector("iframe[name='widget']")

# Then access it
frame = page.frame_locator("iframe[name='widget']")
```

## Exercises

::: tip Exercise 1
Write a test for interacting with a Google reCAPTCHA iframe.
:::

::: tip Exercise 2
Create a test to fill out a payment form inside an iframe.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_22_Frames_iframes/examples)
