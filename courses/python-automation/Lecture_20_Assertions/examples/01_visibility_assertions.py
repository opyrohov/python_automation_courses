"""Example 1: Visibility Assertions"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Visibility Assertions Demo ===\n")

    # Example 1: to_be_visible()
    print("1. Testing to_be_visible()...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Start button should be visible
    expect(page.locator("#start button")).to_be_visible()
    print("   ✓ Start button is visible")

    page.locator("#start button").click()

    # Finish message should become visible
    expect(page.locator("#finish")).to_be_visible()
    print("   ✓ Finish message is now visible")

    # Example 2: to_be_hidden()
    print("\n2. Testing to_be_hidden()...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Finish element should be hidden initially
    expect(page.locator("#finish")).to_be_hidden()
    print("   ✓ Finish message is hidden initially")

    page.locator("#start button").click()

    # Loading should eventually be hidden
    expect(page.locator("#loading")).to_be_hidden()
    print("   ✓ Loading indicator is now hidden")

    # Example 3: to_be_enabled() / to_be_disabled()
    print("\n3. Testing enabled/disabled state...")
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Input should be disabled initially
    expect(page.locator("input[type='text']")).to_be_disabled()
    print("   ✓ Input is disabled initially")

    # Enable it
    page.locator("button").filter(has_text="Enable").click()

    # Input should now be enabled
    expect(page.locator("input[type='text']")).to_be_enabled()
    print("   ✓ Input is now enabled")

    # Example 4: to_be_checked()
    print("\n4. Testing checkbox state...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # First checkbox is unchecked
    checkbox1 = page.locator("input[type='checkbox']").first

    # Check it
    checkbox1.check()
    expect(checkbox1).to_be_checked()
    print("   ✓ Checkbox is checked")

    # Uncheck it
    checkbox1.uncheck()
    expect(checkbox1).not_to_be_checked()
    print("   ✓ Checkbox is unchecked")

    # Example 5: to_be_editable()
    print("\n5. Testing editable state...")
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Enable input first
    page.locator("button").filter(has_text="Enable").click()
    expect(page.locator("input[type='text']")).to_be_enabled()

    # Should be editable
    expect(page.locator("input[type='text']")).to_be_editable()
    print("   ✓ Input is editable")

    # Example 6: to_be_attached()
    print("\n6. Testing element attachment to DOM...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Add an element
    page.locator("button").click()

    # Element should be attached to DOM
    expect(page.locator(".added-manually")).to_be_attached()
    print("   ✓ Element is attached to DOM")

    # Remove it
    page.locator(".added-manually").click()

    # Element should no longer be attached
    expect(page.locator(".added-manually")).not_to_be_attached()
    print("   ✓ Element is no longer attached")

    # Example 7: Negative assertions
    print("\n7. Testing negative assertions (not_)...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Finish should NOT be visible initially
    expect(page.locator("#finish")).not_to_be_visible()
    print("   ✓ Element is NOT visible (as expected)")

    print("\n✓ All visibility assertion examples complete!")

    input("\nPress Enter to close...")
    browser.close()
