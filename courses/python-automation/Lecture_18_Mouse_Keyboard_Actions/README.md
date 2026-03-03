# Lecture 18: Mouse & Keyboard Actions

Master advanced interactions with Playwright - hover, click variations, drag and drop, keyboard shortcuts, and scrolling.

## Topics Covered
1. **Hover Actions** - hover() for tooltips and menus
2. **Click Variations** - dblclick(), right click, click with modifiers
3. **Drag and Drop** - drag_to() for dragging elements
4. **Keyboard Actions** - press(), press_sequentially(), keyboard shortcuts
5. **Scroll Actions** - Scroll to elements and positions

## Quick Reference

### Hover Actions
```python
# Hover over element
page.locator("#menu-item").hover()

# Hover to reveal submenu
page.locator(".dropdown").hover()
page.locator(".submenu-item").click()
```

### Click Variations
```python
# Double click
page.locator("#element").dblclick()

# Right click
page.locator("#element").click(button="right")

# Click with modifier keys
page.locator("#element").click(modifiers=["Shift"])
page.locator("#element").click(modifiers=["Control"])
```

### Drag and Drop
```python
# Drag to target
source = page.locator("#draggable")
target = page.locator("#droppable")
source.drag_to(target)

# Manual drag and drop
page.locator("#draggable").hover()
page.mouse.down()
page.locator("#droppable").hover()
page.mouse.up()
```

### Keyboard Actions
```python
# Press single key
page.keyboard.press("Enter")
page.keyboard.press("Escape")

# Type text character by character
page.keyboard.press_sequentially("Hello World")

# Keyboard shortcuts
page.keyboard.press("Control+A")  # Select all
page.keyboard.press("Control+C")  # Copy
page.keyboard.press("Control+V")  # Paste

# Press key in element
page.locator("#input").press("Enter")
```

### Scroll Actions
```python
# Scroll element into view
page.locator("#bottom-element").scroll_into_view_if_needed()

# Scroll to position
page.evaluate("window.scrollTo(0, 500)")

# Scroll by amount
page.mouse.wheel(0, 500)  # Scroll down 500px
```

## Best Practices
- ✅ Use hover() before interacting with hidden elements
- ✅ Wait for animations to complete after hover
- ✅ Use drag_to() for simple drag and drop
- ✅ Test keyboard shortcuts across browsers
- ✅ Scroll elements into view before interaction
- ❌ Don't assume elements are visible without hovering
- ❌ Don't forget to wait after scroll actions
