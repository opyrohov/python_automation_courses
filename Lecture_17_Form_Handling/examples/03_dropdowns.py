"""Example 3: Dropdown Selections"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/login")

    # Navigate to signup
    page.get_by_placeholder("Name").first.fill("Test User")
    page.get_by_placeholder("Email Address").nth(1).fill("test2@example.com")
    page.get_by_role("button", name="Signup").click()
    time.sleep(1)

    # Select date of birth
    print("Selecting date of birth...")
    page.locator("#days").select_option("15")
    page.locator("#months").select_option("March")
    page.locator("#years").select_option("1990")
    time.sleep(1)

    # Select country
    print("Selecting country...")
    page.locator("#country").select_option(label="United States")
    time.sleep(1)

    # Verify selection
    selected_country = page.locator("#country").input_value()
    print(f"Selected country: {selected_country}")
    print("✓ Dropdown examples complete")

    browser.close()
