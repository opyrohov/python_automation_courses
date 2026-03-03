# Exercise 1: Installation Verification

Verify that your Playwright installation is complete and working correctly.

## Objective
Ensure all components of Playwright are installed and configured properly.

## Tasks

### Task 1: Verify Python and pip

```bash
# Check Python version (should be 3.10+)
python --version

# Check pip version
pip --version
```

**Expected:** Python 3.10 or higher

### Task 2: Verify Virtual Environment

```bash
# Check if venv is activated (you should see 'venv' in prompt)
# Windows:
where python

# Mac/Linux:
which python
```

**Expected:** Python path should be inside your venv folder

### Task 3: Verify Playwright Installation

```bash
# Check playwright version
playwright --version

# Check pytest version
pytest --version

# List installed packages
pip list | findstr playwright  # Windows
pip list | grep playwright     # Mac/Linux
```

**Expected Output:**
```
playwright           1.55.0
pytest-playwright    0.7.1
```

### Task 4: Verify Browser Binaries

```bash
# This should list installed browsers
playwright install --help
```

Create a simple test file to verify browsers:

```python
# test_browsers.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Test Chromium
    print("Testing Chromium...")
    browser = p.chromium.launch()
    browser.close()
    print("✅ Chromium OK")

    # Test Firefox
    print("Testing Firefox...")
    browser = p.firefox.launch()
    browser.close()
    print("✅ Firefox OK")

    # Test WebKit
    print("Testing WebKit...")
    browser = p.webkit.launch()
    browser.close()
    print("✅ WebKit OK")

print("\n✅ All browsers are installed correctly!")
```

Run it:
```bash
python test_browsers.py
```

### Task 5: Run Sample Test

Create this test file:

```python
# test_installation.py
import pytest
from playwright.sync_api import Page, expect


def test_playwright_works(page: Page):
    """Verify Playwright is working."""
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    print("✅ Playwright test passed!")
```

Run it:
```bash
pytest test_installation.py -v
pytest test_installation.py --headed  # See browser
```

**Expected:** Test should pass ✓

## Verification Checklist

- [ ] Python 3.10+ installed
- [ ] Virtual environment activated
- [ ] playwright package installed
- [ ] pytest and pytest-playwright installed
- [ ] All three browsers (Chromium, Firefox, WebKit) installed
- [ ] Can run simple Playwright script
- [ ] Can run pytest test with Playwright

## If Something Fails

### Python not found
```bash
# Install Python from python.org
# Or use package manager
```

### Playwright not found
```bash
# Activate venv first!
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Then install
pip install playwright pytest-playwright
```

### Browsers not installed
```bash
# Install browsers
playwright install
```

### Tests failing
```bash
# Check error message
# Increase timeout if needed
pytest --timeout=60
```

## Success Criteria

When you see:
```
✅ Python 3.10+ installed
✅ Virtual environment activated
✅ Playwright installed
✅ pytest-playwright installed
✅ All browsers installed
✅ Test passed
```

You're ready to move to Exercise 2! 🎉
