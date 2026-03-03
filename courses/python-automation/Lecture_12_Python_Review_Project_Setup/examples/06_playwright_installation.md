# Playwright Installation and Troubleshooting Guide

Complete guide to installing Playwright and resolving common issues.

## Installation Steps

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Install Playwright Package

```bash
# Make sure virtual environment is activated!
(venv) $ pip install playwright

# Or install specific version
pip install playwright==1.40.0

# Verify installation
pip show playwright
```

### Step 2: Install Pytest Integration

```bash
# Install pytest and pytest-playwright
pip install pytest pytest-playwright

# Verify installation
pytest --version
```

### Step 3: Install Browser Drivers

```bash
# Install all browsers (Chromium, Firefox, WebKit)
playwright install

# Or install specific browsers
playwright install chromium
playwright install firefox
playwright install webkit

# Install system dependencies (Linux only)
playwright install-deps
```

### Step 4: Verify Installation

```bash
# Check Playwright version
playwright --version

# List installed browsers
playwright --help
```

## Installation Methods Comparison

### Method 1: Individual Commands (Recommended for Learning)
```bash
pip install playwright
pip install pytest
pip install pytest-playwright
playwright install
```

**Pros**: Understand each component
**Cons**: More commands to type

### Method 2: Requirements File (Recommended for Projects)
```bash
# Create requirements.txt:
# playwright==1.40.0
# pytest==8.0.0
# pytest-playwright==0.4.4

pip install -r requirements.txt
playwright install
```

**Pros**: Reproducible, version-controlled
**Cons**: Need to create file first

### Method 3: All at Once
```bash
pip install playwright pytest pytest-playwright && playwright install
```

**Pros**: Fast
**Cons**: Harder to debug if something fails

## Browser Installation Details

### What Gets Installed?

Playwright installs complete browser binaries:
- **Chromium**: ~300 MB
- **Firefox**: ~150 MB
- **WebKit**: ~50 MB

Total: ~500 MB

### Where Are Browsers Installed?

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

### Custom Browser Location

```bash
# Set custom installation directory
set PLAYWRIGHT_BROWSERS_PATH=C:\my-browsers  # Windows
export PLAYWRIGHT_BROWSERS_PATH=/custom/path  # Mac/Linux

# Then install
playwright install
```

## Common Installation Issues

### Issue 1: "playwright: command not found"

**Symptoms:**
```bash
$ playwright install
playwright: command not found
```

**Causes:**
- Virtual environment not activated
- Playwright not installed
- Wrong PATH

**Solutions:**

```bash
# 1. Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 2. Verify activation (should see 'venv' in prompt)
(venv) $

# 3. Install Playwright
pip install playwright

# 4. Verify installation
playwright --version
```

### Issue 2: "No module named 'playwright'"

**Symptoms:**
```python
ImportError: No module named 'playwright'
```

**Causes:**
- Playwright not installed in current environment
- Using wrong Python/venv

**Solutions:**

```bash
# Check which Python is being used
which python  # Mac/Linux
where python  # Windows

# Should show path inside venv folder
# If not, activate venv and try again

# Install Playwright
pip install playwright

# Verify
python -c "import playwright; print(playwright.__version__)"
```

### Issue 3: "Executable doesn't exist"

**Symptoms:**
```
playwright._impl._api_types.Error: Executable doesn't exist
```

**Cause:**
- Browser drivers not installed

**Solution:**

```bash
# Install browsers
playwright install

# Or install specific browser
playwright install chromium
```

### Issue 4: Permission Denied (Linux/Mac)

**Symptoms:**
```bash
PermissionError: [Errno 13] Permission denied
```

**Solutions:**

```bash
# Don't use sudo! Create venv for current user
python3 -m venv venv
source venv/bin/activate
pip install playwright
playwright install

# If still issues, check folder permissions
chmod -R u+w ~/Library/Caches/ms-playwright/  # Mac
chmod -R u+w ~/.cache/ms-playwright/  # Linux
```

### Issue 5: PowerShell Execution Policy (Windows)

**Symptoms:**
```
cannot be loaded because running scripts is disabled on this system
```

**Solution:**

```powershell
# Run PowerShell as Administrator (one-time fix)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate venv
venv\Scripts\Activate.ps1
```

### Issue 6: SSL Certificate Errors

**Symptoms:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Temporary Solution (Not Recommended for Production):**

```bash
# Set environment variable (temporary)
set PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0  # Windows
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0  # Mac/Linux

# Update certificates (better solution)
pip install --upgrade certifi
```

### Issue 7: Disk Space Issues

**Symptoms:**
```
No space left on device
```

**Check Space:**

```bash
# Windows
dir "C:\Users\<username>\AppData\Local\ms-playwright\"

# Mac/Linux
du -sh ~/Library/Caches/ms-playwright/
```

**Solution:**

```bash
# Uninstall old browsers
playwright uninstall

# Install only what you need
playwright install chromium
```

### Issue 8: Proxy/Firewall Issues

**Symptoms:**
- Download hangs or times out
- Connection refused errors

**Solutions:**

```bash
# Set proxy
set HTTPS_PROXY=http://proxy.company.com:8080  # Windows
export HTTPS_PROXY=http://proxy.company.com:8080  # Mac/Linux

# Then install
playwright install

# Or download browsers manually
# https://playwright.dev/docs/browsers#download-browsers-manually
```

### Issue 9: Wrong Python Version

**Symptoms:**
```
Requires Python 3.8+, but you have Python 3.7
```

**Solution:**

```bash
# Check Python version
python --version

# If too old, install newer Python
# Then create venv with specific version
python3.11 -m venv venv

# Or on Windows with multiple versions
py -3.11 -m venv venv
```

## Verification Commands

### Full Installation Check

```bash
# 1. Check Python version (should be 3.8+)
python --version

# 2. Check virtual environment is activated
# (should see 'venv' in prompt)

# 3. Check pip is working
pip --version

# 4. Check Playwright installed
pip show playwright

# 5. Check pytest installed
pytest --version

# 6. Check playwright CLI works
playwright --version

# 7. List installed packages
pip list | findstr playwright  # Windows
pip list | grep playwright    # Mac/Linux

# 8. Try importing in Python
python -c "from playwright.sync_api import sync_playwright; print('Success!')"
```

### Run Test to Verify Everything Works

Create `test_verify.py`:

```python
from playwright.sync_api import sync_playwright

def test_playwright_working():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev")
        assert "Playwright" in page.title()
        browser.close()
        print("✓ Playwright is working correctly!")

if __name__ == "__main__":
    test_playwright_working()
```

Run it:
```bash
python test_verify.py
```

## Browser-Specific Installation

### Chromium Only (Recommended for CI/CD)

```bash
# Smallest installation for faster CI
playwright install chromium
```

### All Browsers (Recommended for Development)

```bash
# Install everything for cross-browser testing
playwright install
```

### System Dependencies (Linux Only)

```bash
# Install system libraries needed by browsers
sudo playwright install-deps

# Or for specific browser
sudo playwright install-deps chromium
```

## Updating Playwright

### Check for Updates

```bash
# Check current version
pip show playwright

# Check latest version
pip index versions playwright
```

### Update Playwright

```bash
# Update to latest version
pip install --upgrade playwright

# Update browsers to match
playwright install

# Or update to specific version
pip install playwright==1.40.0
playwright install
```

## Uninstalling

### Complete Uninstall

```bash
# 1. Uninstall browsers
playwright uninstall

# 2. Uninstall Python packages
pip uninstall playwright pytest-playwright pytest

# 3. Delete virtual environment
deactivate
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows
```

## Best Practices

✅ **DO:**
- Always use virtual environment
- Pin specific versions in requirements.txt
- Install browsers after installing Python package
- Verify installation before writing tests
- Update regularly for bug fixes

❌ **DON'T:**
- Use sudo/administrator for installation
- Install globally (use venv)
- Forget to install browsers (`playwright install`)
- Mix different Playwright versions in same project

## Quick Start Script

**Windows (setup.bat):**
```batch
@echo off
python -m venv venv
call venv\Scripts\activate
pip install playwright pytest pytest-playwright
playwright install
echo Setup complete!
pytest --version
playwright --version
```

**Mac/Linux (setup.sh):**
```bash
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install playwright pytest pytest-playwright
playwright install
echo "Setup complete!"
pytest --version
playwright --version
```

Run it:
```bash
# Windows
setup.bat

# Mac/Linux
chmod +x setup.sh
./setup.sh
```

## Getting Help

If you're still stuck:

1. **Check Playwright Docs**: https://playwright.dev/python/docs/intro
2. **GitHub Issues**: https://github.com/microsoft/playwright-python/issues
3. **Stack Overflow**: Search "playwright python [your issue]"
4. **Discord**: https://aka.ms/playwright/discord

## Summary

**Installation Checklist:**
- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] playwright installed via pip
- [ ] pytest and pytest-playwright installed
- [ ] Browser drivers installed
- [ ] Installation verified with test

You're ready to start automating! 🚀
