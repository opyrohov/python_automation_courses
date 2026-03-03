# Lecture 13: Introduction to Playwright & Setup

Welcome to Lecture 13! This is where your browser automation journey begins. You'll learn what Playwright is, how it compares to other tools, and get your first automation scripts running.

## Table of Contents
1. [What is Playwright?](#what-is-playwright)
2. [Playwright vs Selenium](#playwright-vs-selenium)
3. [Installation](#installation)
4. [Browser Drivers Setup](#browser-drivers-setup)
5. [Project Structure](#project-structure)
6. [Your First Script](#your-first-script)
7. [Practice Exercises](#practice-exercises)

## What is Playwright?

**Playwright** is a modern, open-source browser automation framework developed by Microsoft in 2020.

### Key Features:
- **Cross-browser**: Chromium, Firefox, WebKit (Safari engine)
- **Fast & Reliable**: Auto-waiting eliminates flaky tests
- **Modern**: Built for modern web applications
- **Rich API**: Screenshots, videos, network interception, mobile emulation
- **Multiple Languages**: Python, JavaScript, Java, .NET

### What Can You Do?
- ✅ **E2E Testing**: Test complete user workflows
- ✅ **Web Scraping**: Extract data from websites
- ✅ **Process Automation**: Automate repetitive browser tasks
- ✅ **Screenshot Testing**: Visual regression testing
- ✅ **Performance Testing**: Measure page load times
- ✅ **Accessibility Testing**: Check ARIA, keyboard navigation

## Playwright vs Selenium

### Quick Comparison

| Feature | Playwright | Selenium |
|---------|-----------|----------|
| **Released** | 2020 | 2004 |
| **Speed** | ⚡ Faster | 🐢 Slower |
| **Auto-waiting** | ✅ Built-in | ❌ Manual |
| **Setup** | ✅ Simple | ⚠️ Complex |
| **Browsers** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge |
| **Network Control** | ✅ Full | ❌ Limited |
| **Screenshots/Video** | ✅ Built-in | ⚠️ Third-party |
| **Maturity** | New (5 years) | Mature (20 years) |

### When to Choose Playwright?
- ✅ Starting a new automation project
- ✅ Need speed and reliability
- ✅ Testing modern web applications
- ✅ Want built-in features (video, network mocking)
- ✅ Need mobile browser emulation

### When to Choose Selenium?
- ⚠️ Large existing Selenium codebase
- ⚠️ Team expertise in Selenium
- ⚠️ Organizational requirement or policy
- ⚠️ Need specific Selenium ecosystem tools

**For new projects in 2024+, Playwright is the modern choice!**

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Virtual environment (recommended)

### Step-by-Step Installation

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 2. Install Playwright Python package
pip install playwright

# 3. Install pytest and pytest-playwright
pip install pytest pytest-playwright

# 4. Install browser binaries
playwright install

# 5. Verify installation
playwright --version
pytest --version
```

### What Gets Installed?

**Python Packages:**
- `playwright` - Core automation library
- `pytest` - Testing framework
- `pytest-playwright` - Integration between pytest and Playwright

**Browser Binaries (~500 MB):**
- Chromium (~300 MB) - Chrome/Edge engine
- Firefox (~150 MB) - Mozilla Firefox
- WebKit (~50 MB) - Safari engine

## Browser Drivers Setup

### The Three Browsers

**1. Chromium** (Default, Recommended)
- Open-source version of Chrome/Edge
- ~65% browser market share
- Best compatibility with modern web apps

**2. Firefox**
- Mozilla Firefox browser
- Different rendering engine (Gecko)
- Good for cross-browser testing

**3. WebKit**
- Safari's rendering engine
- Works on Windows/Linux too!
- Essential for iOS/Safari testing

### Installing Browsers

```bash
# Install all browsers (recommended for development)
playwright install

# Install specific browser (recommended for CI/CD)
playwright install chromium
playwright install firefox
playwright install webkit

# Install with system dependencies (Linux)
playwright install --with-deps
```

### Browser Storage Location

**Windows:**
```
C:\Users\<username>\AppData\Local\ms-playwright\
```

**Mac:**
```
~/Library/Caches/ms-playwright/
```

**Linux:**
```
~/.cache/ms-playwright/
```

## Project Structure

### Recommended Structure

```
my_playwright_project/
│
├── venv/                      # Virtual environment
│
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures
│   ├── test_login.py
│   ├── test_search.py
│   └── test_checkout.py
│
├── pages/                     # Page Object Model (later)
│   ├── __init__.py
│   └── base_page.py
│
├── utils/                     # Helper utilities
│   ├── __init__.py
│   └── config.py
│
├── test_data/                 # Test data
│   └── users.json
│
├── screenshots/               # Test screenshots
├── videos/                    # Test recordings
│
├── requirements.txt           # Dependencies
├── pytest.ini                 # Pytest configuration
├── .env                       # Environment variables
└── .gitignore                 # Git ignore rules
```

### Creating Project Structure

```bash
# Create project folder
mkdir my_playwright_project
cd my_playwright_project

# Create folders
mkdir tests pages utils test_data screenshots videos

# Create __init__.py files (Windows)
type nul > tests\__init__.py
type nul > pages\__init__.py
type nul > utils\__init__.py

# Create __init__.py files (Mac/Linux)
touch tests/__init__.py pages/__init__.py utils/__init__.py
```

### requirements.txt

```
playwright==1.55.0
pytest==8.4.2
pytest-playwright==0.7.1
python-dotenv==1.2.1
```

### pytest.ini

```ini
[pytest]
testpaths = tests

markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    login: Login flow tests
    browser: Browser-specific tests

addopts = -v --tb=short --strict-markers
```

## Your First Script

### Method 1: Simple Sync Script

```python
# first_script.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create new page
    page = browser.new_page()

    # Navigate to URL
    page.goto("https://playwright.dev")

    # Print page title
    print(f"Page title: {page.title()}")

    # Take screenshot
    page.screenshot(path="screenshot.png")

    # Close browser
    browser.close()
```

**Run it:**
```bash
python first_script.py
```

### Method 2: Pytest Test (Recommended)

```python
# tests/test_first.py
import pytest
from playwright.sync_api import Page, expect


def test_playwright_homepage(page: Page):
    """Test that Playwright homepage loads correctly."""

    # ARRANGE
    url = "https://playwright.dev"

    # ACT
    page.goto(url)

    # ASSERT
    expect(page).to_have_title("Playwright")
    expect(page).to_have_url(url)

    print(f"✅ Successfully navigated to {url}")
```

**Run it:**
```bash
pytest tests/test_first.py
pytest tests/test_first.py --headed
```

### Understanding the Code

**1. Import Playwright:**
```python
from playwright.sync_api import Page, expect
```

**2. Test Function with `page` Fixture:**
```python
def test_example(page: Page):
    # pytest-playwright provides 'page' automatically!
```

**3. Navigate:**
```python
page.goto("https://example.com")
```

**4. Assert:**
```python
expect(page).to_have_title("Expected Title")
```

## Running Tests

### Basic Commands

```bash
# Run all tests (headless mode)
pytest

# Run in headed mode (see browser)
pytest --headed

# Run with specific browser
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit

# Run all browsers
pytest --browser chromium --browser firefox --browser webkit

# Slow down execution (debugging)
pytest --headed --slowmo 1000

# Run specific test file
pytest tests/test_first.py

# Run specific test function
pytest tests/test_first.py::test_playwright_homepage

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

### Useful Options

```bash
# Take screenshots on failure (automatic with pytest-playwright)
pytest

# Record video
pytest --video on

# Set custom timeout
pytest --timeout 60

# Run tests in parallel (requires pytest-xdist)
pip install pytest-xdist
pytest -n 4  # 4 parallel workers
```

## Essential Playwright Commands

### Navigation

```python
# Go to URL
page.goto("https://example.com")

# Navigate back
page.go_back()

# Navigate forward
page.go_forward()

# Reload page
page.reload()
```

### Getting Information

```python
# Get page title
title = page.title()

# Get current URL
current_url = page.url

# Get page content (HTML)
html = page.content()
```

### Screenshots & Videos

```python
# Take screenshot
page.screenshot(path="screenshot.png")

# Full page screenshot
page.screenshot(path="full_page.png", full_page=True)

# Screenshot of specific element
element = page.locator(".header")
element.screenshot(path="header.png")
```

### Waiting

```python
# Wait for page load
page.wait_for_load_state("networkidle")
page.wait_for_load_state("domcontentloaded")

# Wait for specific element
page.wait_for_selector(".content")

# Wait for URL
page.wait_for_url("**/dashboard")
```

## Debugging Tools

### 1. Headed Mode
```bash
pytest --headed
```
Watch tests run in a real browser window.

### 2. Slow Motion
```bash
pytest --headed --slowmo 1000
```
Slow down operations by 1000ms to see what's happening.

### 3. Playwright Inspector
```python
# Add to your test
page.pause()
```
Opens interactive debugger with step-through capability.

### 4. Screenshots
```python
# Take debug screenshot
page.screenshot(path="debug.png")
```

### 5. Video Recording
```bash
pytest --video on
```
Records video of test execution.

### 6. Trace Viewer
```python
# Start tracing
context.tracing.start(screenshots=True, snapshots=True)

# Your test code here

# Stop tracing
context.tracing.stop(path="trace.zip")
```
View trace: `playwright show-trace trace.zip`

## Best Practices

### ✅ DO:
- Use pytest-playwright fixtures for cleaner code
- Use `expect()` assertions (auto-waiting)
- Run headless in CI/CD for speed
- Use meaningful selectors (data-testid, text, role)
- Keep tests independent
- One test = one thing
- Enable screenshots on failure
- Use Page Object Model for organization

### ❌ DON'T:
- Mix Playwright with Selenium
- Use fixed sleeps (`time.sleep()`)
- Hardcode waits unless necessary
- Test implementation details
- Create test interdependencies
- Commit screenshots/videos to Git
- Use complex XPath when CSS works

## Troubleshooting

### Issue: "playwright: command not found"
**Solution:** Activate virtual environment
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### Issue: "No module named 'playwright'"
**Solution:** Install playwright
```bash
pip install playwright pytest-playwright
```

### Issue: "Executable doesn't exist"
**Solution:** Install browser binaries
```bash
playwright install
```

### Issue: Tests timeout
**Solution:** Increase timeout
```python
page.set_default_timeout(60000)  # 60 seconds
```

### Issue: Element not found
**Solution:** Wait for element or check selector
```python
page.wait_for_selector(".element")
# or
expect(page.locator(".element")).to_be_visible()
```

## Practice Exercises

Complete the exercises in the `exercises/` folder:
- `exercise_01_installation.md` - Installation verification
- `exercise_02_first_script.py` - Write your first script
- `exercise_03_navigation.py` - Practice navigation
- `exercise_04_multiple_browsers.py` - Test across browsers

Solutions available in `exercises/SOLUTIONS.md`.

## Quick Reference

### Installation
```bash
pip install playwright pytest pytest-playwright
playwright install
```

### Run Tests
```bash
pytest                    # Headless
pytest --headed          # Headed
pytest --browser firefox # Specific browser
pytest --slowmo 1000     # Slow motion
```

### Basic Commands
```python
page.goto(url)           # Navigate
page.title()             # Get title
page.screenshot(path)    # Screenshot
expect(page).to_have_title()  # Assert
page.pause()             # Debug
```

## Resources

- **Playwright Docs**: https://playwright.dev/python/
- **pytest-playwright**: https://github.com/microsoft/playwright-pytest
- **API Reference**: https://playwright.dev/python/docs/api/class-page
- **Examples**: See `examples/` folder
- **Community**: https://aka.ms/playwright/discord

## Next Steps

After completing this lecture:
1. ✅ Playwright installed and working
2. ✅ First test running successfully
3. ✅ Understand basic navigation
4. ✅ Can run tests in different browsers
5. ✅ Know debugging tools

**Ready for Lecture 14: Playwright Locators & Interactions!** 🚀
