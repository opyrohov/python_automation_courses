# Exercise Solutions - Lecture 12

Complete solutions and explanations for all exercises.

## Exercise 1: Project Setup

### Solution

**Part 1: Create Project Structure**

```bash
# Windows
mkdir my_test_project
cd my_test_project
mkdir tests pages utils test_data
type nul > tests\__init__.py
type nul > pages\__init__.py
type nul > utils\__init__.py

# Mac/Linux
mkdir my_test_project
cd my_test_project
mkdir tests pages utils test_data
touch tests/__init__.py pages/__init__.py utils/__init__.py
```

**Part 2: Set Up Virtual Environment**

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Verify
where python  # Windows - should show path in venv
which python  # Mac/Linux - should show path in venv
```

**Part 3: Create requirements.txt**

```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
python-dotenv==1.0.0
```

**Part 4: Install Dependencies**

```bash
pip install -r requirements.txt
playwright install
pip list
pytest --version
playwright --version
```

**Part 5: Create .gitignore**

```
# Virtual environment
venv/
env/
ENV/

# Python cache
__pycache__/
*.pyc
*.pyo

# Pytest
.pytest_cache/

# Test artifacts
test-results/
screenshots/
videos/

# Environment variables
.env

# IDE
.vscode/
.idea/
```

**Part 6: Create pytest.ini**

```ini
[pytest]
testpaths = tests

markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    critical: Business-critical tests

addopts = -v --tb=short
```

**Part 7: Create Configuration**

```python
# utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://example.com")
HEADLESS = os.getenv("HEADLESS", "False") == "True"
DEFAULT_TIMEOUT = 30000
```

**Part 8: Create .env Files**

**.env:**
```env
BASE_URL=https://example.com
HEADLESS=False
BROWSER=chromium
```

**.env.example:**
```env
BASE_URL=https://example.com
HEADLESS=False
BROWSER=chromium
```

**Part 9: Write First Test**

```python
# tests/test_example.py
import pytest
from playwright.sync_api import Page, expect


def test_google_homepage(page: Page):
    """Test that Google homepage loads and search box is visible."""
    # ARRANGE
    url = "https://www.google.com"

    # ACT
    page.goto(url)

    # ASSERT
    expect(page).to_have_title("Google")
    assert page.is_visible("textarea[name='q']")
```

**Part 10: Run and Verify**

```bash
# Run tests
pytest

# Run in headed mode
pytest --headed

# Run verbose
pytest -v
```

---

## Exercise 2: Virtual Environment Practice

### Exercise 2.1 Solutions

**Task 1-3: Create, Activate, Install**

```bash
mkdir venv_practice
cd venv_practice
python -m venv venv

# Activate
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install and save
pip install requests
pip list
pip freeze > requirements.txt

# Deactivate
deactivate
```

**Task 3: Verify Isolation**

```bash
# Without venv - FAILS
python -c "import requests"
# ModuleNotFoundError: No module named 'requests'

# With venv - WORKS
venv\Scripts\activate
python -c "import requests"
# Success!
```

**Answer:** It works in venv because the `requests` package is installed only in the venv's isolated environment, not in the system Python.

### Exercise 2.2 Solutions

```bash
# Project A
mkdir project_a
cd project_a
python -m venv venv
venv\Scripts\activate
pip install playwright==1.39.0
pip freeze > requirements.txt
pip show playwright  # Version: 1.39.0

# Project B
cd ..
mkdir project_b
cd project_b
python -m venv venv
venv\Scripts\activate
pip install playwright==1.40.0
pip freeze > requirements.txt
pip show playwright  # Version: 1.40.0
```

**Answer:** Both versions exist because each venv is completely isolated. Each has its own copy of Python and packages.

### Exercise 2.3 Solutions

```bash
mkdir original_project
cd original_project
python -m venv venv
venv\Scripts\activate
pip install playwright pytest python-dotenv
pip freeze > requirements.txt

# Delete and recreate
deactivate
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows

# Recreate
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip list  # Same packages as before!
```

**Answer:** This is useful for:
- Sharing projects with teammates (they recreate the same environment)
- CI/CD pipelines (automated environment setup)
- Troubleshooting (start fresh if venv gets corrupted)

### Exercise 2.5 Solution

```bash
mkdir team_project
cd team_project

# Simulate requirements.txt already exists
echo playwright==1.40.0 > requirements.txt
echo pytest==8.0.0 >> requirements.txt

# Setup steps:
# 1. Create venv
python -m venv venv

# 2. Activate venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install browsers
playwright install

# 5. Run tests
pytest
```

### Challenge Questions Answers

1. **What is a virtual environment?**
   - An isolated Python environment with its own interpreter and packages

2. **Why use virtual environments?**
   - Isolate dependencies per project
   - Prevent version conflicts
   - Reproducible environments
   - Clean uninstall (just delete folder)

3. **Should you commit venv/ to Git?**
   - No! Because:
     - Large size (hundreds of MB)
     - Machine-specific (won't work on different OS)
     - Unnecessary (recreate from requirements.txt)

4. **How do teammates get dependencies?**
   - Clone repository
   - Create their own venv
   - Install from requirements.txt

5. **Command differences:**
   - `pip freeze`: Displays installed packages
   - `pip freeze > requirements.txt`: Saves to file
   - `pip install -r requirements.txt`: Installs from file

6. **True or False:**
   - [F] Same venv for multiple projects - Each project should have its own
   - [T] Each project should have its own venv - Correct!
   - [F] venv folders are small - They're 100-500 MB
   - [F] Deleting venv loses code - Only loses packages, code is safe
   - [T] Activate venv every terminal session - Must activate each time

### Common Issues Solutions

**Scenario 1: pip install fails**
- **Diagnosis:** venv not activated
- **Solution:** Activate venv first

**Scenario 2: ModuleNotFoundError but pip list shows it**
- **Diagnosis:** Using wrong Python (system vs venv)
- **Solution:** Activate venv, ensure using venv Python

**Scenario 3: pytest not found after deactivate**
- **Diagnosis:** pytest only installed in venv
- **Solution:** Activate venv before running pytest

---

## Exercise 3: Requirements.txt Practice

### Exercise 3.1 Solutions

**Answers:**
1. `==` means "exact version" - must be this specific version
2. Specify versions for reproducibility - same versions for everyone
3. `>=` means "this version or newer" - less strict, may get different versions

### Exercise 3.2 Solution

```bash
mkdir install_practice
cd install_practice

# Create requirements.txt
echo pytest==8.0.0 > requirements.txt
echo requests==2.31.0 >> requirements.txt

# Create and activate venv
python -m venv venv
venv\Scripts\activate

# Install
pip install -r requirements.txt

# Verify
pip list
pytest --version
python -c "import pytest, requests; print('Success!')"
```

### Exercise 3.3 Solutions

Test results:

**requirements_exact.txt** (`==`):
- Installs: Exactly 1.40.0 and 8.0.0
- Best for: Production (most stable)

**requirements_minimum.txt** (`>=`):
- Installs: Latest version (could be 1.41.0, 8.1.0, etc.)
- Best for: Development (get new features)

**requirements_compatible.txt** (`~=`):
- Installs: Compatible version (1.40.x, 8.0.x)
- Best for: Balance (bug fixes, no breaking changes)

**When to use:**
- Production: `==` (exact, predictable)
- Development: `>=` (latest features)
- Library: `~=` (compatible updates)

### Exercise 3.5 Answer

**Why split requirements?**
- Development needs tools (linting, formatting, debuggers)
- Production doesn't need dev tools (smaller, faster)
- CI/CD might need different packages
- Clear separation of concerns
- Faster production deployments

### Exercise 3.6 Answers

**Safer strategy:** Update one at a time
- Test after each update
- Easy to identify which update broke something
- Can roll back specific package

**Update all at once:**
- Time-sensitive security updates
- Major version upgrades
- Starting new project
- Must test thoroughly after!

**Testing updates:**
- Run full test suite
- Check for deprecation warnings
- Test critical user flows
- Review changelogs

### Exercise 3.9 Solutions

**Problems identified:**
1. No versions on playwright, pytest, beautifulsoup4, pandas
2. requests==2.25.0 is very outdated (current: 2.31.0)
3. No organization or comments
4. No separation of dependencies

**Improved version:**

```
# ============================================================================
# CORE DEPENDENCIES
# ============================================================================

# Browser automation
playwright==1.40.0

# Testing framework
pytest==8.0.0

# HTTP library
requests==2.31.0


# ============================================================================
# DATA PROCESSING
# ============================================================================

# Web scraping
beautifulsoup4==4.12.2

# Data analysis
pandas==2.1.4
```

### Exercise 3.10 Answers

**Why separate files?**
- CI/CD doesn't need development tools
- Local development wants convenience tools
- Production needs minimal dependencies
- Security: fewer packages = smaller attack surface

**What's `-r requirements-test.txt`?**
- Includes another requirements file
- Inherits all dependencies from that file
- Allows building on top of base requirements

**When to use each:**
- `requirements-test.txt`: CI/CD pipeline
- `requirements-local.txt`: Developer machines

---

## Exercise 4: First Test Solutions

### Test 1 Solution

```python
def test_playwright_homepage(page: Page):
    # ARRANGE
    url = "https://playwright.dev"

    # ACT
    page.goto(url)

    # ASSERT
    expect(page).to_have_title("Playwright")
    assert page.url == url
```

### Test 2 Solution

```python
def test_get_started_button_visible(page: Page):
    # ARRANGE
    url = "https://playwright.dev"
    get_started_selector = "a:has-text('Get started')"

    # ACT
    page.goto(url)

    # ASSERT
    expect(page.locator(get_started_selector)).to_be_visible()
    expect(page.locator(get_started_selector)).to_have_text("Get started")
```

### Test 3 Solution

```python
def test_click_get_started(page: Page):
    # ARRANGE
    page.goto("https://playwright.dev")

    # ACT
    page.click("a:has-text('Get started')")

    # ASSERT
    expect(page).to_have_url("**/docs/intro")
```

### Test 4 Solution

```python
def test_search_docs(page: Page):
    # ARRANGE
    search_term = "selectors"
    page.goto("https://playwright.dev/docs/intro")

    # ACT
    page.click("button[class*='DocSearch']")
    page.fill("input[placeholder='Search docs']", search_term)

    # ASSERT
    expect(page.locator(".DocSearch-Hits")).to_be_visible()
```

### Test 5 Solution

```python
def test_google_search(page: Page):
    # ARRANGE
    search_term = "Playwright Python"
    page.goto("https://www.google.com")

    # ACT
    page.fill("textarea[name='q']", search_term)
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")

    # ASSERT
    expect(page).to_have_url("**/search?**")
    assert page.is_visible("#search")
```

### Test 6 Solution (Challenge)

```python
def test_playwright_python_docs(page: Page):
    # ARRANGE
    page.goto("https://playwright.dev/python")

    # ACT & ASSERT
    # Verify page title
    expect(page).to_have_title("Playwright Python")

    # Verify navigation menu visible
    assert page.is_visible("nav")

    # Verify Installation link exists and is clickable
    installation_link = page.locator("a:has-text('Installation')")
    expect(installation_link).to_be_visible()

    # Click Installation
    installation_link.click()

    # Verify URL changed
    expect(page).to_have_url("**/python/docs/intro")

    # Verify page content contains "pip install"
    expect(page.locator("body")).to_contain_text("pip install")
```

### Test 7 Solution (Smoke Test)

```python
@pytest.mark.smoke
def test_quick_page_load(page: Page):
    # ARRANGE & ACT
    page.goto("https://playwright.dev")

    # ASSERT
    expect(page).to_have_title("Playwright")
```

Run smoke tests only:
```bash
pytest -m smoke
```

### Test 8 Solution (Error Handling)

```python
def test_404_page(page: Page):
    # ARRANGE & ACT
    response = page.goto("https://playwright.dev/this-does-not-exist",
                         wait_until="domcontentloaded")

    # ASSERT
    assert response.status == 404
    expect(page.locator("body")).to_contain_text("Page Not Found")
```

### Bonus Test Example

```python
def test_wikipedia_search(page: Page):
    """Test Wikipedia search functionality."""
    # ARRANGE
    search_term = "Python programming"
    page.goto("https://www.wikipedia.org")

    # ACT
    page.fill("#searchInput", search_term)
    page.press("#searchInput", "Enter")
    page.wait_for_load_state("networkidle")

    # ASSERT
    expect(page).to_have_url("**/Python_(programming_language)")
    expect(page.locator("h1")).to_contain_text("Python")
    assert page.is_visible(".infobox")
```

---

## Common Mistakes and How to Fix Them

### Mistake 1: Not Using AAA Pattern

**Bad:**
```python
def test_messy():
    page.goto("https://example.com")
    assert page.is_visible(".button")
    page.click(".button")
    assert page.url == "https://example.com/next"
```

**Good:**
```python
def test_clear():
    # ARRANGE
    page.goto("https://example.com")

    # ACT
    page.click(".button")

    # ASSERT
    assert page.url == "https://example.com/next"
    assert page.is_visible(".success")
```

### Mistake 2: Fragile Selectors

**Bad:**
```python
page.click("#root > div > div.container > button:nth-child(3)")
```

**Good:**
```python
page.click("button:has-text('Submit')")
# or
page.click("[data-testid='submit-button']")
```

### Mistake 3: Not Waiting for Elements

**Bad:**
```python
page.click(".button")
assert page.is_visible(".result")  # May fail - result not loaded yet
```

**Good:**
```python
page.click(".button")
expect(page.locator(".result")).to_be_visible()  # Automatically waits
```

### Mistake 4: Test Interdependence

**Bad:**
```python
user_id = None

def test_create_user():
    global user_id
    user_id = create_user()

def test_delete_user():
    delete_user(user_id)  # Depends on test_create_user!
```

**Good:**
```python
def test_create_user():
    user_id = create_user()
    # Test creation
    cleanup(user_id)

def test_delete_user():
    user_id = create_user()  # Create its own user
    delete_user(user_id)
    # Test deletion
```

---

## Additional Tips

### Debugging Tests

```bash
# Run single test
pytest tests/test_example.py::test_google_homepage

# Stop on first failure
pytest -x

# Show full traceback
pytest --tb=long

# Run in headed mode
pytest --headed

# Slow down execution
pytest --headed --slowmo=1000

# Keep browser open on failure
pytest --headed --pause-on-failure
```

### Using Fixtures

```python
# conftest.py
import pytest

@pytest.fixture
def authenticated_page(page):
    # Login before test
    page.goto("/login")
    page.fill("#username", "test@example.com")
    page.fill("#password", "password123")
    page.click("button[type='submit']")
    return page

# test_dashboard.py
def test_dashboard(authenticated_page):
    # Already logged in!
    authenticated_page.goto("/dashboard")
    assert authenticated_page.is_visible(".user-profile")
```

### Organizing Tests

```
tests/
├── conftest.py           # Shared fixtures
├── test_authentication/
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_signup.py
├── test_checkout/
│   ├── test_cart.py
│   └── test_payment.py
└── test_search/
    └── test_product_search.py
```

---

## Summary

You've learned:
- Setting up professional project structure
- Managing virtual environments
- Creating and using requirements.txt
- Writing tests with AAA pattern
- Using Playwright for browser automation
- Organizing and running tests with pytest

**Next Steps:**
1. Apply this to your real project
2. Practice writing more tests
3. Learn advanced Playwright features
4. Explore Page Object Model pattern
5. Set up CI/CD for your tests

Keep practicing! 🚀
