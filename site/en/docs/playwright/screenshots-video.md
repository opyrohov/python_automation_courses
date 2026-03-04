# Screenshots & Video — Test Documentation

Playwright provides powerful tools for visual test documentation: screenshots, video recording, and tracing. These capabilities are critically important for error diagnosis and test behavior analysis. In this section, we will cover all methods of visual documentation.

## Screenshots

### Basic Screenshots

```python
from playwright.sync_api import Page

def test_basic_screenshots(page: Page):
    """Taking page screenshots."""
    page.goto("https://example.com")

    # Screenshot of the visible part of the page
    page.screenshot(path="screenshots/homepage.png")

    # Full page screenshot (with scrolling)
    page.screenshot(path="screenshots/full_page.png", full_page=True)

    # JPEG screenshot with quality
    page.screenshot(path="screenshots/homepage.jpg", type="jpeg", quality=80)

    # Get screenshot as bytes (without saving to file)
    screenshot_bytes = page.screenshot()
    # Can be attached to a report or sent to a server
```

### Element Screenshots

```python
def test_element_screenshots(page: Page):
    """Screenshots of individual page elements."""
    page.goto("https://example.com/dashboard")

    # Screenshot of a specific element
    page.get_by_test_id("stats-chart").screenshot(path="screenshots/chart.png")

    # Table screenshot
    page.get_by_role("table").screenshot(path="screenshots/data_table.png")

    # Form screenshot
    page.locator("form#registration").screenshot(path="screenshots/form.png")

    # Navigation menu screenshot
    page.locator("nav.sidebar").screenshot(path="screenshots/sidebar.png")
```

### Screenshot Options

```python
def test_screenshot_options(page: Page):
    """Additional options for screenshots."""
    page.goto("https://example.com")

    # Hiding certain elements in the screenshot
    page.screenshot(
        path="screenshots/no_ads.png",
        mask=[
            page.locator(".advertisement"),
            page.locator(".cookie-banner"),
        ],
    )

    # Mask color (default is pink)
    page.screenshot(
        path="screenshots/masked.png",
        mask=[page.locator(".dynamic-content")],
        mask_color="#000000",  # Black mask
    )

    # Screenshot with animations stopped
    page.screenshot(
        path="screenshots/no_animation.png",
        animations="disabled",
    )

    # Screenshot with specific scale (for Retina)
    page.screenshot(
        path="screenshots/retina.png",
        scale="css",  # or "device"
    )
```

## Screenshots on Test Failure

### Automatic Screenshots via conftest.py

```python
# conftest.py
import pytest
from datetime import datetime
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page: Page):
    """Automatic screenshot on test failure."""
    yield
    # Runs after each test
    if request.node.rep_call and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        page.screenshot(
            path=f"screenshots/failures/{test_name}_{timestamp}.png",
            full_page=True,
        )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to save test result in request.node."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
```

### Screenshots at Test Steps

```python
def test_checkout_with_screenshots(page: Page):
    """Test documenting each step."""
    page.goto("https://example.com/cart")
    page.screenshot(path="screenshots/steps/01_cart.png")

    # Filling delivery form
    page.get_by_label("Address").fill("123 Main Street")
    page.get_by_label("City").select_option("Kyiv")
    page.screenshot(path="screenshots/steps/02_delivery_form.png")

    # Payment selection
    page.get_by_role("radio", name="Credit card online").check()
    page.screenshot(path="screenshots/steps/03_payment.png")

    # Order confirmation
    page.get_by_role("button", name="Place Order").click()
    page.screenshot(path="screenshots/steps/04_confirmation.png")
```

## Video — Recording

### Video Recording Setup

```python
from playwright.sync_api import sync_playwright

def test_video_recording():
    """Recording test execution video."""
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # Enable video recording via context
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720},
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.get_by_role("link", name="Products").click()
        page.get_by_text("Laptop Pro").click()

        # Video is saved when context is closed
        context.close()
        browser.close()

        # Video path is available via page.video
        # video_path = page.video.path()
```

### Video via pytest-playwright

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Video recording settings for all tests."""
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720},
    }
```

```bash
# Or via command line
pytest --video on                    # Always record video
pytest --video retain-on-failure     # Keep only on failure
```

::: tip Tip
Use `--video retain-on-failure` for CI/CD — this saves video only for failed tests, saving disk space.
:::

## Tracing — Detailed Tracing

Tracing is the most powerful diagnostic tool in Playwright. It records complete information about test execution: screenshots, network requests, console logs, DOM snapshots.

### Recording a Trace

```python
from playwright.sync_api import sync_playwright

def test_with_tracing():
    """Recording detailed test execution trace."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Start trace recording
        context.tracing.start(
            screenshots=True,     # Screenshots at each step
            snapshots=True,       # DOM snapshots
            sources=True,         # Test source code
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.get_by_role("link", name="Catalog").click()
        page.get_by_placeholder("Search").fill("Laptop")
        page.get_by_placeholder("Search").press("Enter")

        # Stop and save trace
        context.tracing.stop(path="traces/test_trace.zip")

        context.close()
        browser.close()
```

### Viewing a Trace

```bash
# Open trace in Trace Viewer
playwright show-trace traces/test_trace.zip

# Or via web interface
# Go to https://trace.playwright.dev and upload the .zip file
```

### Tracing via pytest-playwright

```python
# conftest.py
import pytest
from playwright.sync_api import BrowserContext

@pytest.fixture
def context(context: BrowserContext):
    """Fixture with tracing for each test."""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="traces/trace.zip")
```

```bash
# Or via pytest-playwright command line
pytest --tracing on                   # Always record trace
pytest --tracing retain-on-failure    # Only on failure
```

::: info Information
Trace Viewer shows: action timeline, before/after screenshots for each action, network requests, console logs, and test source code. It is the best debugging tool.
:::

## Group Settings for pytest

```python
# conftest.py — full test documentation configuration
import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page, BrowserContext

# Directories for artifacts
SCREENSHOTS_DIR = Path("test-results/screenshots")
VIDEOS_DIR = Path("test-results/videos")
TRACES_DIR = Path("test-results/traces")

@pytest.fixture(scope="session", autouse=True)
def create_artifact_dirs():
    """Create directories for test artifacts."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    TRACES_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Global context settings with video."""
    return {
        **browser_context_args,
        "record_video_dir": str(VIDEOS_DIR),
        "record_video_size": {"width": 1280, "height": 720},
    }

@pytest.fixture
def context(context: BrowserContext):
    """Context with tracing."""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context

@pytest.fixture(autouse=True)
def test_artifacts(request, page: Page, context: BrowserContext):
    """Save artifacts after each test."""
    yield
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Always save final state screenshot
    page.screenshot(path=str(SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"))

    # Save trace
    trace_path = str(TRACES_DIR / f"{test_name}_{timestamp}.zip")
    context.tracing.stop(path=trace_path)
```

## Visual Testing (Visual Comparison)

```python
from playwright.sync_api import Page, expect

def test_visual_comparison(page: Page):
    """Screenshot comparison to detect visual regressions."""
    page.goto("https://example.com")

    # Compare with reference screenshot
    # On first run, the reference is created
    expect(page).to_have_screenshot("homepage.png")

    # Compare with deviation tolerance
    expect(page).to_have_screenshot(
        "homepage_tolerant.png",
        max_diff_pixels=100,         # Maximum 100 pixels difference
    )

    # Compare with threshold tolerance
    expect(page).to_have_screenshot(
        "homepage_threshold.png",
        threshold=0.2,               # 20% color tolerance
    )

    # Compare specific element
    expect(page.locator("header")).to_have_screenshot("header.png")

    # Masking dynamic elements
    expect(page).to_have_screenshot(
        "static_content.png",
        mask=[
            page.locator(".timestamp"),
            page.locator(".random-banner"),
        ],
    )
```

::: warning Warning
Visual testing is sensitive to environment: different OS, fonts, and resolutions can affect results. It is recommended to run visual tests in Docker for consistency.
:::

## CI/CD Setup

```yaml
# GitHub Actions with test artifacts
name: Playwright Tests
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: |
          pip install pytest-playwright
          playwright install --with-deps chromium
      - name: Run tests with artifacts
        run: |
          pytest tests/ \
            --browser chromium \
            --video retain-on-failure \
            --tracing retain-on-failure \
            --screenshot on
      - name: Upload test artifacts
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-artifacts
          path: |
            test-results/
            screenshots/
            videos/
            traces/
          retention-days: 14
```

## Practical Example: Error Report

```python
from playwright.sync_api import Page, BrowserContext, expect
from datetime import datetime
import json

def test_with_full_reporting(page: Page, context: BrowserContext):
    """Test with full documentation for error analysis."""
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://example.com/checkout")
    page.screenshot(path="reports/step_01_checkout_page.png")

    # Filling the form
    page.get_by_label("Name").fill("Olena Kovalenko")
    page.get_by_label("Email").fill("olena@test.com")
    page.get_by_label("Phone").fill("+380991234567")
    page.screenshot(path="reports/step_02_form_filled.png")

    # Placing the order
    page.get_by_role("button", name="Place Order").click()
    page.screenshot(path="reports/step_03_after_submit.png")

    # Checking the result
    try:
        expect(page.get_by_text("Order accepted")).to_be_visible(timeout=10000)
        page.screenshot(path="reports/step_04_success.png")
    except Exception:
        # On error — collect maximum information
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(
            path=f"reports/error_{timestamp}.png",
            full_page=True,
        )
        context.tracing.stop(path=f"reports/error_trace_{timestamp}.zip")

        # Collect console logs and errors
        console_logs = []
        page.on("console", lambda msg: console_logs.append({
            "type": msg.type,
            "text": msg.text,
        }))

        # Collect page information
        page_info = {
            "url": page.url,
            "title": page.title(),
            "timestamp": timestamp,
        }
        with open(f"reports/error_info_{timestamp}.json", "w") as f:
            json.dump(page_info, f, indent=2, ensure_ascii=False)

        raise  # Re-raise the error
```

## Useful Links

- [Official Screenshots Documentation](https://playwright.dev/python/docs/screenshots)
- [Video recording](https://playwright.dev/python/docs/videos)
- [Trace Viewer](https://playwright.dev/python/docs/trace-viewer)
- [Visual comparisons](https://playwright.dev/python/docs/test-snapshots)
- [Online Trace Viewer](https://trace.playwright.dev/)
