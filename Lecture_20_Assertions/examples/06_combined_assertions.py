"""Example 6: Combined Assertions - Complete Test Scenarios"""
from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Combined Assertions Demo ===\n")

    # Scenario 1: Login Form Validation
    print("Scenario 1: Login Form Validation")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/login")

    # Verify initial state
    expect(page).to_have_url("**/login")
    expect(page).to_have_title("The Internet")
    expect(page.locator("h2")).to_have_text("Login Page")
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_enabled()
    print("✓ Login page loaded correctly")

    # Fill and submit form
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    # Verify input values
    expect(page.locator("#username")).to_have_value("tomsmith")
    expect(page.locator("#password")).to_have_value("SuperSecretPassword!")
    print("✓ Form filled correctly")

    # Submit
    page.locator("button[type='submit']").click()

    # Verify success
    expect(page).to_have_url("**/secure")
    expect(page.locator(".flash")).to_be_visible()
    expect(page.locator(".flash")).to_contain_text("You logged into a secure area!")
    expect(page.locator("a")).filter(has_text="Logout").to_be_visible()
    print("✓ Login successful - all validations passed\n")

    # Scenario 2: Dynamic Content Verification
    print("Scenario 2: Dynamic Content Loading")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Initial state
    expect(page.locator("#start button")).to_be_visible()
    expect(page.locator("#start button")).to_be_enabled()
    expect(page.locator("#finish")).to_be_hidden()
    print("✓ Initial state verified")

    # Trigger loading
    page.locator("#start button").click()

    # Verify loading state
    expect(page.locator("#loading")).to_be_visible()
    print("✓ Loading indicator visible")

    # Verify completion
    expect(page.locator("#loading")).to_be_hidden()
    expect(page.locator("#finish")).to_be_visible()
    expect(page.locator("#finish h4")).to_have_text("Hello World!")
    print("✓ Content loaded successfully\n")

    # Scenario 3: Form Element States
    print("Scenario 3: Dynamic Form Controls")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Checkbox section
    checkbox = page.locator("#checkbox input")
    remove_btn = page.locator("button").filter(has_text="Remove")

    # Initial state
    expect(checkbox).to_be_visible()
    expect(checkbox).to_be_attached()
    expect(remove_btn).to_be_enabled()
    print("✓ Checkbox visible initially")

    # Remove checkbox
    remove_btn.click()
    expect(checkbox).not_to_be_attached()
    expect(page.locator("#message")).to_contain_text("It's gone!")
    print("✓ Checkbox removed successfully")

    # Add it back
    page.locator("button").filter(has_text="Add").click()
    expect(checkbox).to_be_attached()
    expect(checkbox).to_be_visible()
    print("✓ Checkbox added back successfully")

    # Input section
    input_field = page.locator("input[type='text']")
    enable_btn = page.locator("button").filter(has_text="Enable")

    # Initial state
    expect(input_field).to_be_disabled()
    expect(input_field).not_to_be_editable()
    print("✓ Input disabled initially")

    # Enable input
    enable_btn.click()
    expect(input_field).to_be_enabled()
    expect(input_field).to_be_editable()
    print("✓ Input enabled successfully\n")

    # Scenario 4: Table Data Verification
    print("Scenario 4: Table Data Verification")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/tables")

    # Verify table structure
    table = page.locator("#table1")
    expect(table).to_be_visible()

    # Count rows and columns
    rows = table.locator("tbody tr")
    expect(rows).to_have_count(4)
    print(f"✓ Table has 4 data rows")

    # Verify headers exist
    headers = table.locator("thead th")
    expect(headers).to_have_count(6)
    print(f"✓ Table has 6 columns")

    # Verify first row data
    first_row = rows.first
    expect(first_row.locator("td").nth(0)).to_contain_text("Smith")
    expect(first_row.locator("td").nth(1)).to_contain_text("John")
    print("✓ First row data verified\n")

    # Scenario 5: Multi-Element List Verification
    print("Scenario 5: List Operations")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Initial state
    elements = page.locator(".added-manually")
    expect(elements).to_have_count(0)
    print("✓ Initially no elements")

    # Add 5 elements
    add_btn = page.locator("button").first
    for i in range(5):
        add_btn.click()

    # Verify count
    expect(elements).to_have_count(5)
    print("✓ Added 5 elements")

    # Verify each element
    for i in range(5):
        element = elements.nth(i)
        expect(element).to_be_visible()
        expect(element).to_be_enabled()
        expect(element).to_have_text("Delete")

    print("✓ All elements verified")

    # Remove some elements
    elements.first.click()
    elements.first.click()

    # Verify new count
    expect(elements).to_have_count(3)
    print("✓ Removed 2 elements, 3 remaining\n")

    # Scenario 6: Complete User Flow
    print("Scenario 6: Complete User Flow")
    print("-" * 40)
    page.goto("https://the-internet.herokuapp.com/")

    # Homepage verification
    expect(page).to_have_title("The Internet")
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h2")).to_contain_text("Available Examples")
    print("✓ Homepage loaded")

    # Navigate to checkboxes
    page.locator("a").filter(has_text="Checkboxes").click()
    expect(page).to_have_url("**/checkboxes")
    print("✓ Navigated to Checkboxes page")

    # Interact with checkboxes
    checkbox1 = page.locator("input[type='checkbox']").first
    checkbox2 = page.locator("input[type='checkbox']").last

    checkbox1.check()
    expect(checkbox1).to_be_checked()

    checkbox2.uncheck()
    expect(checkbox2).not_to_be_checked()
    print("✓ Checkbox interactions verified")

    # Go back
    page.go_back()
    expect(page).to_have_url("https://the-internet.herokuapp.com/")
    expect(page.locator("h1")).to_be_visible()
    print("✓ Navigated back to homepage\n")

    print("=" * 40)
    print("✓ All combined assertion scenarios complete!")
    print("=" * 40)

    input("\nPress Enter to close...")
    browser.close()
