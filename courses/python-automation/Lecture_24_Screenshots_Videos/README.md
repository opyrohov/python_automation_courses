# Lecture 24: Screenshots & Videos

## Overview
Learn how to capture screenshots and record videos during test execution in Playwright. These features are essential for debugging, visual testing, and creating test artifacts.

## Topics Covered

### 1. Taking Screenshots
- Basic screenshot capture
- `page.screenshot()` method
- Saving to file vs returning bytes
- Screenshot options and formats

### 2. Full Page vs Element Screenshots
- Full page screenshots (`full_page=True`)
- Element-specific screenshots (`locator.screenshot()`)
- Viewport-only screenshots
- Clipping specific regions

### 3. Screen Recording (Video)
- Enabling video recording in context
- Video size and quality options
- Saving videos on test completion
- Video file management

### 4. Screenshot Comparison Basics
- Comparing screenshots
- Pixel-by-pixel comparison concepts
- Tolerance thresholds
- Visual regression testing introduction

### 5. Best Practices
- When to capture screenshots
- Naming conventions for artifacts
- Organizing screenshots and videos
- CI/CD integration considerations

### 6. Saving Artifacts
- Creating artifact directories
- Timestamped file names
- Cleanup strategies
- Integrating with test frameworks

## Quick Reference

### Basic Screenshot
```python
# Save screenshot to file
page.screenshot(path="screenshot.png")

# Full page screenshot
page.screenshot(path="full_page.png", full_page=True)

# Get screenshot as bytes
screenshot_bytes = page.screenshot()
```

### Element Screenshot
```python
# Screenshot of specific element
element = page.locator("#my-element")
element.screenshot(path="element.png")
```

### Video Recording
```python
# Enable video recording when creating context
context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 1280, "height": 720}
)
page = context.new_page()

# ... perform actions ...

# Close context to save video
context.close()

# Get video path
video_path = page.video.path()
```

### Screenshot Options
```python
page.screenshot(
    path="screenshot.png",
    full_page=True,              # Capture full scrollable page
    type="png",                  # "png" or "jpeg"
    quality=80,                  # JPEG quality (0-100)
    omit_background=True,        # Transparent background
    timeout=30000,               # Timeout in ms
    animations="disabled",       # Disable CSS animations
    scale="css"                  # "css" or "device"
)
```

### Clipping Region
```python
page.screenshot(
    path="clipped.png",
    clip={
        "x": 0,
        "y": 0,
        "width": 500,
        "height": 300
    }
)
```

## Examples

| File | Description |
|------|-------------|
| `01_basic_screenshots.py` | Basic screenshot capture techniques |
| `02_element_screenshots.py` | Element-specific screenshots |
| `03_video_recording.py` | Recording test execution videos |
| `04_screenshot_options.py` | Advanced screenshot options |
| `05_artifacts_management.py` | Organizing and managing artifacts |

## Exercises

| File | Description |
|------|-------------|
| `exercise_01_capture_flow.py` | Capture screenshots during user flow |
| `exercise_02_video_test.py` | Record video of complete test scenario |

## Key Concepts

1. **Screenshot Types**
   - Viewport: Only visible area
   - Full Page: Entire scrollable content
   - Element: Specific DOM element
   - Clipped: Custom region

2. **Video Recording**
   - Configured at context level
   - Video saved when context closes
   - Useful for debugging failed tests
   - Can slow down test execution

3. **Artifact Organization**
   - Use descriptive file names
   - Include timestamps for uniqueness
   - Organize by test/feature
   - Clean up old artifacts regularly

## Common Issues

| Issue | Solution |
|-------|----------|
| Screenshot is blank | Wait for page to load (`wait_for_load_state()`) |
| Video not saved | Ensure `context.close()` is called |
| Element screenshot fails | Element must be visible and in viewport |
| Full page too large | Use `clip` to capture specific region |
| Animations cause flaky screenshots | Use `animations="disabled"` option |

## Best Practices

1. **Screenshots**
   - Capture on test failure automatically
   - Use meaningful file names
   - Disable animations for consistency
   - Consider viewport size standardization

2. **Videos**
   - Enable only when debugging
   - Configure appropriate video size
   - Clean up videos after successful runs
   - Store with test results in CI/CD

3. **Visual Testing**
   - Establish baseline images
   - Use tolerance for minor differences
   - Test across different browsers
   - Review visual changes carefully

## Resources

- [Playwright Screenshots Documentation](https://playwright.dev/python/docs/screenshots)
- [Playwright Video Recording](https://playwright.dev/python/docs/videos)
- [Visual Comparisons](https://playwright.dev/python/docs/test-snapshots)
