"""Example 2: Checkboxes and Radio Buttons"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/login")

    # Navigate to signup
    page.get_by_placeholder("Name").first.fill("Test User")
    page.get_by_placeholder("Email Address").nth(1).fill("test@example.com")
    page.get_by_role("button", name="Signup").click()
    time.sleep(1)

    # Radio buttons
    print("Selecting gender...")
    page.locator("#id_gender1").check()  # Male
    time.sleep(0.5)

    # Checkboxes
    print("Checking newsletter...")
    page.locator("#newsletter").check()
    print("Checking special offers...")
    page.locator("#optin").check()
    time.sleep(1)

    # Verify
    assert page.locator("#newsletter").is_checked()
    print("✓ Checkbox and radio examples complete")

    browser.close()
