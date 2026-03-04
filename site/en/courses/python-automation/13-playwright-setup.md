# Lecture 13: Playwright Setup

Introduction to Playwright and environment setup.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_13_Introduction_Playwright_Setup/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/exercises" target="_blank">📝 Вправи</a>
</div>

## Lecture Topics

- What is Playwright
- Installation
- First script
- Browsers and contexts

## What is Playwright?

Playwright is a browser automation library from Microsoft.

**Advantages:**
- Support for Chromium, Firefox, WebKit
- Automatic element waiting
- Mobile emulation
- Video recording and screenshots
- Network interception

## Installation

```bash
# Install the library
pip install playwright

# Install browsers
playwright install
```

## First Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create a page
    page = browser.new_page()

    # Navigation
    page.goto("https://example.com")

    # Get the title
    print(page.title())

    # Close the browser
    browser.close()
```

## Browser Launch Options

```python
browser = p.chromium.launch(
    headless=False,      # Show browser window
    slow_mo=500,         # Delay between actions (ms)
    devtools=True,       # Open DevTools
)

# Different browsers
browser = p.chromium.launch()
browser = p.firefox.launch()
browser = p.webkit.launch()
```

## Browser Context

```python
# Context = isolated session (like incognito)
context = browser.new_context(
    viewport={"width": 1920, "height": 1080},
    locale="uk-UA",
    timezone_id="Europe/Kiev",
)

page = context.new_page()

# Multiple pages in one context
page1 = context.new_page()
page2 = context.new_page()
```

## Navigation

```python
# Go to a page
page.goto("https://example.com")
page.goto("https://example.com", wait_until="networkidle")

# Browser navigation
page.go_back()
page.go_forward()
page.reload()

# URL and title
current_url = page.url
current_title = page.title()
```

## Async Version

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()

asyncio.run(main())
```

## Exercises

::: tip Exercise 1
Write a script that opens Google, performs a search, and prints the result URLs.
:::

::: tip Exercise 2
Create a script to open a website in three different browsers simultaneously.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_13_Introduction_Playwright_Setup/examples)
