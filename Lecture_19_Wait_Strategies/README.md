# Lecture 19: Wait Strategies

## Overview
Master Playwright's waiting mechanisms to create reliable, non-flaky tests that handle dynamic content properly.

## Quick Reference

### Auto-Waiting
```python
# Playwright automatically waits for elements to be actionable
page.locator("#button").click()  # Auto-waits for visible, enabled, stable
page.locator("#input").fill("text")  # Auto-waits for enabled
expect(page.locator("#msg")).to_be_visible()  # Auto-waits and retries
```

### wait_for_selector()
```python
# Wait for element to appear
page.wait_for_selector("#element")

# Wait states
page.wait_for_selector("#element", state="visible")    # Default
page.wait_for_selector("#loading", state="hidden")     # Wait to disappear
page.wait_for_selector("#element", state="attached")   # In DOM
page.wait_for_selector("#element", state="detached")   # Removed from DOM

# With timeout
page.wait_for_selector("#element", timeout=10000)  # 10 seconds
```

### wait_for_load_state()
```python
# Wait for page load
page.wait_for_load_state()  # Default: "load"
page.wait_for_load_state("domcontentloaded")  # DOM ready
page.wait_for_load_state("networkidle")  # No network activity
```

### Custom Wait Conditions
```python
# Wait for JavaScript condition
page.wait_for_function("() => document.readyState === 'complete'")

# Wait for element count
page.wait_for_function("() => document.querySelectorAll('.item').length > 5")

# Wait with arguments
page.wait_for_function(
    "text => document.body.textContent.includes(text)",
    arg="Success"
)
```

### Timeout Configuration
```python
# Global timeout
page.set_default_timeout(60000)

# Per-action timeout
page.locator("#button").click(timeout=5000)

# Navigation timeout
page.goto(url, timeout=30000)
```

## What Auto-Waiting Checks

Before performing an action, Playwright waits for element to be:
1. **Attached** - Present in DOM
2. **Visible** - Not hidden (display, visibility, opacity)
3. **Stable** - Not animating
4. **Receives Events** - Not covered by other elements
5. **Enabled** - Not disabled (for inputs)

## Load State Types

| State | When Complete | Best For |
|-------|---------------|----------|
| `load` | `window.load` event fired | Regular pages |
| `domcontentloaded` | DOM ready | Fast tests, simple pages |
| `networkidle` | No network for 500ms | SPAs, AJAX pages |

## Decision Tree

1. **Interacting with element?** → Trust auto-waiting
2. **Asserting element state?** → Use `expect()`
3. **Waiting for appearance/disappearance?** → Use `wait_for_selector()`
4. **Waiting for page load?** → Use `wait_for_load_state()`
5. **Complex custom condition?** → Use `wait_for_function()`
6. **Need fixed delay?** → Avoid `wait_for_timeout()`

## Common Patterns

### Pattern 1: Wait for Loading Spinner
```python
# Click action that triggers loading
page.locator("#submit").click()

# Wait for spinner to disappear
page.wait_for_selector(".loading-spinner", state="hidden")

# Proceed with next action
expect(page.locator(".success-message")).to_be_visible()
```

### Pattern 2: SPA Navigation
```python
# Navigate in Single Page App
page.locator("#dashboard-link").click()

# Wait for network to settle
page.wait_for_load_state("networkidle")

# Verify content loaded
expect(page.locator("h1")).to_have_text("Dashboard")
```

### Pattern 3: Dynamic Content
```python
# Trigger dynamic content load
page.locator("#load-more").click()

# Wait for new items to appear
page.wait_for_function(
    "count => document.querySelectorAll('.item').length > count",
    arg=initial_count
)
```

### Pattern 4: Form Submission
```python
# Submit form
page.locator("#submit").click()

# Wait for redirect
page.wait_for_load_state("networkidle")

# Or wait for success element
page.wait_for_selector(".success-message", state="visible")
```

## Best Practices

### ✅ DO
- Trust auto-waiting for standard actions
- Use `expect()` for assertions
- Wait for specific conditions, not arbitrary times
- Use appropriate load states for your app type
- Set reasonable global timeouts
- Handle timeout errors gracefully

### ❌ DON'T
- Use `wait_for_timeout()` by default (anti-pattern!)
- Add waits before every action (unnecessary)
- Use very short timeouts (< 1 second)
- Ignore timeout errors without investigating
- Mix up sync and async methods
- Wait when auto-wait already handles it

## Common Issues

### TimeoutError
```python
# Problem: Element never appears
page.wait_for_selector("#nonexistent")  # ❌ Timeout!

# Solutions:
1. Verify selector is correct
2. Check if element actually appears
3. Increase timeout if legitimately slow
4. Use correct wait state
```

### Element Not Clickable
```python
# Problem: Element obscured or not ready
page.locator("#button").click()  # ❌ Error!

# Solutions:
page.wait_for_selector("#button", state="visible")
page.locator("#button").scroll_into_view_if_needed()
page.locator("#overlay").wait_for(state="hidden")
```

## Examples Included
1. `01_auto_waiting.py` - Demonstrations of auto-waiting
2. `02_wait_for_selector.py` - Element waiting examples
3. `03_load_states.py` - Page load state examples
4. `04_custom_waits.py` - Custom wait conditions
5. `05_timeout_config.py` - Timeout configuration

## Resources
- [Playwright Auto-waiting](https://playwright.dev/python/docs/actionability)
- [Wait for Selector](https://playwright.dev/python/docs/api/class-page#page-wait-for-selector)
- [Load States](https://playwright.dev/python/docs/api/class-page#page-wait-for-load-state)
