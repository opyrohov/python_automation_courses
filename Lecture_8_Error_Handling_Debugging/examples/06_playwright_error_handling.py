"""
Lecture 8 - Example 6: Playwright Error Handling
================================================
Learn to handle Playwright-specific errors and make tests more robust.
"""

print("=" * 60)
print("EXAMPLE 6: PLAYWRIGHT ERROR HANDLING")
print("=" * 60)
print()

print("""
NOTE: This file shows error handling patterns for Playwright.
To run actual Playwright code, you need to:
1. Install playwright: pip install playwright
2. Install browsers: playwright install
3. Uncomment and run the examples at the bottom
""")
print()


# 1. Common Playwright Errors
# ===========================
print("1. Common Playwright Errors")
print("-" * 40)
print("""
Common Playwright Errors:

1. TimeoutError
   - Element not found within timeout
   - Page didn't load in time
   - Navigation timeout

2. Error: Element is not visible/enabled
   - Trying to click hidden element
   - Element is disabled

3. Error: Multiple elements found
   - Selector matches more than one element

4. Error: Browser disconnected
   - Browser crashed
   - Network issues

5. Error: Selector does not match any element
   - Element doesn't exist
   - Wrong selector
""")
print()


# 2. Handling TimeoutError
# ========================
print("2. Handling TimeoutError")
print("-" * 40)

# Simulated Playwright error handling patterns
def safe_click(page, selector, timeout=5000):
    """
    Safely click an element with timeout handling.

    Args:
        page: Playwright page object
        selector: CSS selector
        timeout: Timeout in milliseconds
    """
    try:
        # page.click(selector, timeout=timeout)
        print(f"✅ Clicked element: {selector}")
        return True

    except Exception as e:  # Would be TimeoutError
        print(f"❌ TimeoutError: Could not click {selector}")
        print(f"   Waited {timeout}ms but element not found")

        # Take screenshot for debugging
        # page.screenshot(path=f"error_{selector.replace('#', '')}.png")
        print(f"   Screenshot saved for debugging")

        return False

# Usage
print("Example: Safe click with timeout handling")
safe_click(None, "#submit-button", timeout=5000)
safe_click(None, "#missing-element", timeout=3000)
print()


# 3. Retry Logic for Flaky Elements
# =================================
print("3. Retry Logic for Flaky Elements")
print("-" * 40)

import time

def click_with_retry(page, selector, max_retries=3, delay=1):
    """
    Click element with retry logic for flaky elements.

    Args:
        page: Playwright page object
        selector: CSS selector
        max_retries: Maximum number of retry attempts
        delay: Delay between retries in seconds
    """
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}/{max_retries}: Clicking {selector}")
            # page.click(selector, timeout=5000)
            # Simulate success on 3rd attempt
            if attempt >= 3:
                print(f"✅ Successfully clicked {selector}")
                return True
            else:
                raise Exception("TimeoutError")

        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")

            if attempt < max_retries:
                print(f"   Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"   Max retries reached. Element not clickable.")
                return False

click_with_retry(None, "#flaky-button", max_retries=3, delay=0.5)
print()


# 4. Multiple Elements Error
# ==========================
print("4. Handling Multiple Elements")
print("-" * 40)

def safe_get_element(page, selector):
    """
    Safely get element, handling multiple matches.

    Args:
        page: Playwright page object
        selector: CSS selector

    Returns:
        Locator for the element or None
    """
    try:
        # count = page.locator(selector).count()
        count = 2  # Simulate multiple matches

        if count == 0:
            print(f"❌ No elements found for selector: {selector}")
            return None

        elif count > 1:
            print(f"⚠️  Warning: {count} elements match '{selector}'")
            print(f"   Consider using a more specific selector")
            # Could also use .first or .nth(0)
            return f"{selector} (using first match)"

        else:
            print(f"✅ Found exactly one element: {selector}")
            return selector

    except Exception as e:
        print(f"❌ Error getting element: {e}")
        return None

safe_get_element(None, ".button")  # Multiple matches
safe_get_element(None, "#unique-button")  # Single match
print()


# 5. Page Navigation Errors
# =========================
print("5. Page Navigation Errors")
print("-" * 40)

def safe_navigate(page, url, timeout=30000):
    """
    Safely navigate to a URL with error handling.

    Args:
        page: Playwright page object
        url: URL to navigate to
        timeout: Navigation timeout in milliseconds
    """
    try:
        print(f"🌐 Navigating to: {url}")
        # response = page.goto(url, timeout=timeout, wait_until="domcontentloaded")

        # Simulate successful navigation
        response_status = 200

        if response_status >= 400:
            print(f"❌ Navigation failed with status: {response_status}")
            return False

        print(f"✅ Successfully navigated to {url}")
        return True

    except Exception as e:  # Would be TimeoutError
        print(f"❌ Navigation timeout: {url}")
        print(f"   Page did not load within {timeout}ms")

        # Try to get current URL for debugging
        # current_url = page.url
        # print(f"   Current URL: {current_url}")

        return False

safe_navigate(None, "https://example.com", timeout=30000)
safe_navigate(None, "https://slow-site.com", timeout=5000)
print()


# 6. Element State Checks
# =======================
print("6. Element State Checks")
print("-" * 40)

def safe_interact(page, selector, action="click"):
    """
    Safely interact with element after checking state.

    Args:
        page: Playwright page object
        selector: CSS selector
        action: Action to perform (click, fill, etc.)
    """
    try:
        # Check if element exists
        # if not page.locator(selector).is_visible():
        #     print(f"❌ Element not visible: {selector}")
        #     return False

        # Check if element is enabled
        # if not page.locator(selector).is_enabled():
        #     print(f"❌ Element is disabled: {selector}")
        #     return False

        # Perform action
        if action == "click":
            # page.click(selector)
            print(f"✅ Clicked: {selector}")
        elif action == "fill":
            # page.fill(selector, value)
            print(f"✅ Filled: {selector}")

        return True

    except Exception as e:
        print(f"❌ Error interacting with {selector}: {e}")
        return False

safe_interact(None, "#enabled-button", "click")
safe_interact(None, "#disabled-button", "click")
print()


# 7. Screenshot on Error
# ======================
print("7. Screenshot on Error")
print("-" * 40)

from pathlib import Path
from datetime import datetime

def execute_with_screenshot(page, test_name, func):
    """
    Execute function and take screenshot on error.

    Args:
        page: Playwright page object
        test_name: Name of the test
        func: Function to execute
    """
    try:
        print(f"🚀 Executing: {test_name}")
        func()
        print(f"✅ {test_name} completed successfully")

    except Exception as e:
        print(f"❌ {test_name} failed: {e}")

        # Create screenshots directory
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = screenshots_dir / filename

        # Take screenshot
        # page.screenshot(path=str(filepath), full_page=True)
        print(f"📸 Screenshot saved: {filepath}")

        raise

# Simulate test execution
def test_function():
    # Simulate test that might fail
    pass

execute_with_screenshot(None, "test_login", test_function)
print()


# 8. Context Manager for Browser Errors
# =====================================
print("8. Context Manager for Browser Errors")
print("-" * 40)

class PlaywrightTestContext:
    """Context manager for Playwright tests."""

    def __init__(self, test_name):
        self.test_name = test_name
        self.page = None
        self.browser = None

    def __enter__(self):
        print(f"🚀 Starting test: {self.test_name}")
        try:
            # Simulate browser setup
            # self.browser = playwright.chromium.launch()
            # self.page = self.browser.new_page()
            print("   Browser launched")
            return self

        except Exception as e:
            print(f"❌ Failed to start browser: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is not None:
                print(f"❌ Test failed: {self.test_name}")
                print(f"   Error: {exc_type.__name__}: {exc_val}")

                # Take screenshot on failure
                # if self.page:
                #     self.page.screenshot(path=f"{self.test_name}_error.png")
                print(f"   Screenshot saved")

            else:
                print(f"✅ Test passed: {self.test_name}")

        finally:
            # Clean up resources
            # if self.page:
            #     self.page.close()
            # if self.browser:
            #     self.browser.close()
            print(f"   Browser closed")

        return False  # Don't suppress exceptions

# Usage
with PlaywrightTestContext("test_example"):
    print("   Executing test steps...")
    # Your test code here
    pass
print()


# 9. Comprehensive Error Handler
# ==============================
print("9. Comprehensive Error Handler")
print("-" * 40)

class PlaywrightErrorHandler:
    """Comprehensive error handler for Playwright tests."""

    @staticmethod
    def handle_error(e, page=None, context=None):
        """
        Handle Playwright errors with appropriate actions.

        Args:
            e: The exception
            page: Playwright page object (optional)
            context: Additional context information
        """
        error_type = type(e).__name__
        print(f"❌ {error_type}: {str(e)}")

        if context:
            print(f"   Context: {context}")

        # Timeout errors
        if "Timeout" in error_type:
            print("   💡 Suggestion: Increase timeout or check if element exists")
            print("   💡 Check network conditions")

            if page:
                # print(f"   Current URL: {page.url}")
                # page.screenshot(path="timeout_error.png")
                print("   Screenshot saved: timeout_error.png")

        # Selector errors
        elif "Selector" in str(e) or "locator" in str(e).lower():
            print("   💡 Suggestion: Verify your selector is correct")
            print("   💡 Check if element has loaded")
            print("   💡 Try waiting for the element first")

        # Navigation errors
        elif "navigation" in str(e).lower() or "goto" in str(e).lower():
            print("   💡 Suggestion: Check URL is accessible")
            print("   💡 Check network connectivity")
            print("   💡 Verify page loads correctly in browser")

        # Browser errors
        elif "browser" in str(e).lower() or "context" in str(e).lower():
            print("   💡 Suggestion: Browser may have crashed")
            print("   💡 Try restarting the browser")
            print("   💡 Check system resources")

        # Generic errors
        else:
            print("   💡 Suggestion: Review the error message carefully")
            print("   💡 Check Playwright documentation")

            if page:
                # Take screenshot for debugging
                # page.screenshot(path="generic_error.png")
                print("   Screenshot saved: generic_error.png")

# Example usage
try:
    raise Exception("Timeout 30000ms exceeded")
except Exception as e:
    PlaywrightErrorHandler.handle_error(
        e,
        page=None,
        context="Waiting for #submit-button"
    )
print()


# 10. Best Practices Summary
# ==========================
print("10. Playwright Error Handling Best Practices")
print("-" * 40)
print("""
✅ Best Practices:

1. TIMEOUTS
   - Use reasonable timeouts (not too short, not too long)
   - Increase timeouts for slow-loading elements
   - Use explicit waits instead of sleep()

2. SELECTORS
   - Use specific, stable selectors
   - Prefer data-testid attributes
   - Avoid brittle selectors (nth-child, complex CSS)
   - Check selector matches exactly one element

3. ERROR HANDLING
   - Wrap Playwright calls in try/except
   - Take screenshots on failure
   - Log current state (URL, page title)
   - Provide meaningful error messages

4. RETRIES
   - Implement retry logic for flaky operations
   - Use exponential backoff
   - Limit maximum retry attempts

5. STATE CHECKS
   - Verify element is visible before interacting
   - Check element is enabled
   - Wait for proper page state

6. CLEANUP
   - Always close browser/page in finally block
   - Use context managers for automatic cleanup
   - Handle browser crashes gracefully

7. DEBUGGING
   - Enable slow-mo for visual debugging
   - Use headless=False during development
   - Save page content on error
   - Record videos of test execution

💡 Example Template:

try:
    # Wait for element
    page.wait_for_selector("#element", state="visible", timeout=10000)

    # Check element state
    if page.locator("#element").is_enabled():
        page.click("#element")
    else:
        raise Exception("Element is disabled")

except TimeoutError:
    page.screenshot(path="error.png")
    raise AssertionError(f"Element not found: #element")

except Exception as e:
    page.screenshot(path="error.png")
    raise

finally:
    # Cleanup
    page.close()
""")


print("=" * 60)
print("Key Takeaways:")
print("- Always handle TimeoutError in Playwright")
print("- Take screenshots on errors for debugging")
print("- Use specific selectors and verify element state")
print("- Implement retry logic for flaky operations")
print("- Clean up resources properly")
print("=" * 60)


# Actual Playwright Example (Commented Out)
# =========================================
print("\n" + "=" * 60)
print("ACTUAL PLAYWRIGHT EXAMPLE (Uncomment to run)")
print("=" * 60)
print("""
# Uncomment and run this example if you have Playwright installed

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def test_with_error_handling():
    with sync_playwright() as p:
        browser = None
        try:
            # Launch browser
            browser = p.chromium.launch(headless=False, slow_mo=100)
            page = browser.new_page()

            # Navigate with error handling
            try:
                page.goto("https://example.com", timeout=30000)
                print("✅ Page loaded")
            except PlaywrightTimeoutError:
                print("❌ Page load timeout")
                page.screenshot(path="navigation_error.png")
                raise

            # Click with error handling
            try:
                page.click("text=More information", timeout=5000)
                print("✅ Link clicked")
            except PlaywrightTimeoutError:
                print("❌ Element not found")
                page.screenshot(path="click_error.png")
                raise

            # Wait for navigation
            page.wait_for_load_state("networkidle")
            print(f"✅ Navigated to: {page.url}")

        except Exception as e:
            print(f"❌ Test failed: {e}")
            raise

        finally:
            if browser:
                browser.close()
                print("🏁 Browser closed")

# Uncomment to run:
# test_with_error_handling()
""")
