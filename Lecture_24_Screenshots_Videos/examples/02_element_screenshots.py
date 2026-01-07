"""Example 2: Element Screenshots"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Element Screenshots Demo ===\n")

    # Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    print("1. Navigated to login page")

    # Screenshot of the entire form
    form = page.locator("#login")
    form.screenshot(path="element_form.png")
    print("2. Form screenshot saved: element_form.png")

    # Screenshot of specific input field
    username_field = page.locator("#username")
    username_field.screenshot(path="element_username.png")
    print("3. Username field screenshot saved: element_username.png")

    # Screenshot of the button
    button = page.locator("button[type='submit']")
    button.screenshot(path="element_button.png")
    print("4. Button screenshot saved: element_button.png")

    # Navigate to tables page for more examples
    page.goto("https://the-internet.herokuapp.com/tables")
    print("5. Navigated to tables page")

    # Screenshot of table
    table = page.locator("#table1")
    table.screenshot(path="element_table.png")
    print("6. Table screenshot saved: element_table.png")

    # Screenshot of table header row
    header = page.locator("#table1 thead")
    header.screenshot(path="element_table_header.png")
    print("7. Table header screenshot saved: element_table_header.png")

    # Navigate to page with more elements
    page.goto("https://the-internet.herokuapp.com/challenging_dom")
    print("8. Navigated to challenging DOM page")

    # Screenshot of first button
    first_button = page.locator("a.button").first
    first_button.screenshot(path="element_first_button.png")
    print("9. First button screenshot saved: element_first_button.png")

    print("\n=== Demo Complete ===")
    browser.close()
