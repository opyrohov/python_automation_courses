"""Example 4: Custom Wait Conditions"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Custom Wait Conditions Demo ===\n")

    # Example 1: Wait for element count
    print("1. Waiting for specific number of elements...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Add 5 elements
    for i in range(5):
        page.locator("button").first.click()

    # Wait for exactly 5 elements
    page.wait_for_function(
        "() => document.querySelectorAll('.added-manually').length === 5"
    )
    print("   ✓ 5 elements present!")

    # Example 2: Wait for text content
    print("\n2. Waiting for specific text in element...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("#start button").click()

    # Wait for specific text to appear
    page.wait_for_function(
        """() => {
            const el = document.querySelector('#finish h4');
            return el && el.textContent.includes('Hello World');
        }"""
    )
    print("   ✓ Text 'Hello World' appeared!")

    # Example 3: Wait for document ready state
    print("\n3. Waiting for document ready state...")
    page.goto("https://playwright.dev/")

    page.wait_for_function("() => document.readyState === 'complete'")
    print("   ✓ Document is complete!")

    # Example 4: Wait for custom JavaScript variable
    print("\n4. Waiting for JavaScript variable to be defined...")
    page.goto("https://www.google.com")

    # Wait for Google's search object
    page.wait_for_function("() => typeof google !== 'undefined'")
    print("   ✓ Google object is defined!")

    # Example 5: Wait with arguments
    print("\n5. Waiting with custom arguments...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("#start button").click()

    # Wait for element to contain specific text (passed as argument)
    page.wait_for_function(
        """(selector) => {
            const el = document.querySelector(selector);
            return el && el.textContent.trim().length > 0;
        }""",
        arg="#finish h4"
    )
    print("   ✓ Element has content!")

    # Example 6: Wait for element attribute
    print("\n6. Waiting for element attribute value...")
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Click to enable input
    page.locator("button").filter(has_text="Enable").click()

    # Wait for disabled attribute to be removed
    page.wait_for_function(
        """() => {
            const input = document.querySelector('input[type="text"]');
            return input && !input.disabled;
        }"""
    )
    print("   ✓ Input is enabled!")

    # Example 7: Wait for CSS property
    print("\n7. Waiting for CSS style change...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("#start button").click()

    # Wait for element to become visible (opacity/display change)
    page.wait_for_function(
        """() => {
            const el = document.querySelector('#finish');
            const style = window.getComputedStyle(el);
            return style.display !== 'none';
        }"""
    )
    print("   ✓ Element became visible!")

    print("\n✓ All custom wait examples complete!")

    input("\nPress Enter to close...")
    browser.close()
