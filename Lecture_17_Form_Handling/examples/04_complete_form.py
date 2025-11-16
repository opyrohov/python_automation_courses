"""Example 4: Complete Form Submission"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/login")

    print("=== Complete Registration Form ===")

    # Step 1: Initial signup
    print("Step 1: Enter name and email...")
    page.get_by_placeholder("Name").first.fill("John Doe")
    page.get_by_placeholder("Email Address").nth(1).fill("john.doe@example.com")
    page.get_by_role("button", name="Signup").click()
    time.sleep(1)

    # Step 2: Fill account information
    print("Step 2: Fill account details...")
    page.locator("#id_gender1").check()  # Gender
    page.get_by_label("Password").fill("SecurePass123")

    # Date of birth
    page.locator("#days").select_option("15")
    page.locator("#months").select_option("June")
    page.locator("#years").select_option("1990")

    # Checkboxes
    page.locator("#newsletter").check()
    page.locator("#optin").check()

    # Step 3: Fill address information
    print("Step 3: Fill address...")
    page.locator("#first_name").fill("John")
    page.locator("#last_name").fill("Doe")
    page.locator("#company").fill("Test Company")
    page.locator("#address1").fill("123 Main St")
    page.locator("#country").select_option(label="United States")
    page.locator("#state").fill("California")
    page.locator("#city").fill("Los Angeles")
    page.locator("#zipcode").fill("90001")
    page.locator("#mobile_number").fill("5551234567")

    # Step 4: Submit
    print("Step 4: Submitting form...")
    page.get_by_role("button", name="Create Account").click()
    time.sleep(2)

    # Step 5: Verify success
    print("Step 5: Verifying registration...")
    success_msg = page.locator("h2[data-qa='account-created']")
    if success_msg.is_visible():
        print("✓ Registration successful!")
    else:
        print("✗ Registration may have failed")

    print("\n✓ Complete form example finished")
    time.sleep(2)
    browser.close()
