"""Example 1: Playwright Inspector & page.pause()

Demonstrates how to use Playwright Inspector for interactive debugging
and page.pause() to set breakpoints in your tests.

Run with:
    PWDEBUG=1 pytest 01_playwright_inspector.py -v --headed -s
    (Windows CMD): set PWDEBUG=1 && pytest 01_playwright_inspector.py -v --headed -s
    (PowerShell):  $env:PWDEBUG=1; pytest 01_playwright_inspector.py -v --headed -s
"""
import pytest
from playwright.sync_api import Page


BASE_URL = "https://the-internet.herokuapp.com"


# ============================================
# page.pause() - INTERACTIVE BREAKPOINT
# ============================================

def test_pause_before_login(page: Page):
    """Pause before login to inspect the page.

    page.pause() opens the Playwright Inspector where you can:
    - Step through actions one by one
    - Pick locators with the selector picker
    - See the page state at each step
    - Resume execution
    """
    page.goto(f"{BASE_URL}/login")

    # PAUSE HERE - Inspector opens!
    # You can inspect elements, try locators, etc.
    page.pause()

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    assert "/secure" in page.url


def test_pause_at_multiple_points(page: Page):
    """Multiple pause points for step-by-step debugging."""
    page.goto(f"{BASE_URL}/login")
    page.pause()  # Pause 1: Before filling form

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.pause()  # Pause 2: After filling, before submit

    page.locator("button[type='submit']").click()
    page.pause()  # Pause 3: After login, see result

    assert "/secure" in page.url


# ============================================
# CONDITIONAL PAUSE (for debugging specific cases)
# ============================================

@pytest.mark.parametrize("username,password", [
    ("tomsmith", "SuperSecretPassword!"),
    ("wrong", "wrong"),
])
def test_pause_on_failure(page: Page, username, password):
    """Pause only when something unexpected happens."""
    page.goto(f"{BASE_URL}/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']").click()

    # Pause if we're NOT where expected
    if "/secure" not in page.url and username == "tomsmith":
        print(f"\n  UNEXPECTED: Login failed for {username}")
        page.pause()  # Debug this case!


# ============================================
# USING PWDEBUG ENVIRONMENT VARIABLE
# ============================================
#
# PWDEBUG=1 automatically:
# - Opens Playwright Inspector for every action
# - Sets headless=False
# - Disables timeouts (infinite wait)
# - Steps through each action
#
# How to launch:
#
# Linux/Mac:
#   PWDEBUG=1 pytest test_file.py -s
#
# Windows CMD:
#   set PWDEBUG=1 && pytest test_file.py -s
#
# Windows PowerShell:
#   $env:PWDEBUG=1; pytest test_file.py -s
#
# To disable:
#   unset PWDEBUG       (Linux/Mac)
#   set PWDEBUG=        (Windows CMD)
#   $env:PWDEBUG=""     (PowerShell)


# ============================================
# INSPECTOR FEATURES
# ============================================
#
# When the inspector is open:
#
# 1. LOCATOR PICKER (crosshair icon)
#    - Click elements on page to get selectors
#    - Shows multiple selector strategies
#    - Tests selector uniqueness
#
# 2. STEP OVER (→ button)
#    - Execute one action at a time
#    - See page state after each step
#
# 3. RESUME (▶ button)
#    - Continue running until next pause
#
# 4. ACTION LOG
#    - See all Playwright actions
#    - Copy generated code
#


def test_simple_for_inspector(page: Page):
    """Simple test to demonstrate inspector features.

    Run with PWDEBUG=1 to see each action in inspector.
    """
    page.goto(f"{BASE_URL}/checkboxes")

    checkboxes = page.locator("input[type='checkbox']")
    first = checkboxes.first
    second = checkboxes.nth(1)

    first.check()
    assert first.is_checked()

    second.uncheck()
    assert not second.is_checked()


# ============================================
# KEY POINTS:
#
# 1. page.pause() = interactive breakpoint
# 2. PWDEBUG=1 = auto-open inspector for all actions
# 3. Inspector: pick locators, step through, resume
# 4. Conditional pause for specific failures
# 5. PWDEBUG disables timeouts automatically
# 6. Use -s flag to see print output
# 7. Remove page.pause() before committing!
#
# Run: PWDEBUG=1 pytest 01_playwright_inspector.py -v -s --headed
# ============================================
