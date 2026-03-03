# Lecture 35: Debugging Techniques

## Overview
Master debugging tools and techniques for Playwright tests. Learn to use Playwright Inspector, debug mode, console logging, tracing, common error patterns, and VS Code debugging setup.

## Topics Covered

### 1. Playwright Inspector
- Launching the inspector (PWDEBUG=1)
- Step-by-step execution
- Picking locators interactively
- Recording actions

### 2. Debug Mode
- PWDEBUG environment variable
- page.pause() for breakpoints
- Browser DevTools integration

### 3. Slow Motion & Headed Mode
- --slowmo flag for visual debugging
- --headed to see the browser
- Combining with pytest flags

### 4. Console Logs & Events
- page.on("console") for browser logs
- page.on("pageerror") for JS errors
- page.on("request") / page.on("response")
- Logging in tests with print and logging module

### 5. Tracing & Trace Viewer
- Recording traces programmatically
- Viewing traces with playwright show-trace
- Analyzing network, DOM, and actions

### 6. Common Errors & Solutions
- TimeoutError and how to fix it
- Strict mode violations
- Element not found patterns
- Debugging flaky tests

### 7. VS Code Debugging
- launch.json for pytest
- Breakpoints in test code
- Playwright Test for VS Code extension

## Examples

1. **01_playwright_inspector.py** - Using PWDEBUG and page.pause()
2. **02_console_and_events.py** - Capturing browser console and events
3. **03_tracing_debug.py** - Recording and viewing traces
4. **04_common_errors.py** - Common errors and solutions
5. **05_debug_strategies.py** - Complete debugging workflow

## Exercises

1. **exercise_01_debug_failing_test.py** - Find and fix bugs in failing tests
2. **exercise_02_trace_and_log.py** - Add tracing and logging to tests

## Key Concepts

### Playwright Inspector
```bash
# Launch with inspector
PWDEBUG=1 pytest test_login.py --headed

# Windows PowerShell
$env:PWDEBUG=1; pytest test_login.py --headed

# Windows CMD
set PWDEBUG=1 && pytest test_login.py --headed
```

### page.pause()
```python
def test_debug(page):
    page.goto("/login")
    page.pause()  # Opens inspector here!
    page.locator("#username").fill("user")
```

### Console Logging
```python
page.on("console", lambda msg: print(f"BROWSER: {msg.text}"))
page.on("pageerror", lambda err: print(f"JS ERROR: {err}"))
```

### Tracing
```bash
# Record trace on failure
pytest --tracing retain-on-failure

# View trace
playwright show-trace test-results/trace.zip
```

## Resources
- [Playwright Debugging](https://playwright.dev/python/docs/debug)
- [Playwright Inspector](https://playwright.dev/python/docs/debug#playwright-inspector)
- [Trace Viewer](https://playwright.dev/python/docs/trace-viewer)

## Next Lecture
Lecture 36: Best Practices & Final Project
