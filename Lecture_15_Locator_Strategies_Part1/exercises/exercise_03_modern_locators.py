"""
Exercise 3: Playwright Modern Locators
Practice using Playwright's recommended modern locators

Task: Complete the TODOs using modern locator methods
"""

from playwright.sync_api import sync_playwright, expect

def modern_locators_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://playwright.dev/")

        # TODO 1: Find and click the "Docs" link using get_by_role()
        # Hint: It's a link with name "Docs"
        # TODO: Uncomment and complete
        # page.get_by_role("YOUR_ROLE_HERE", name="YOUR_NAME_HERE").click()
        # print("✓ Clicked Docs link")

        # TODO 2: Find the navigation element using get_by_role()
        # Hint: The role is "navigation"
        # TODO: Uncomment and complete
        # nav = page.get_by_role("YOUR_ROLE_HERE")
        # print(f"✓ Found {nav.count()} navigation element(s)")

        # TODO 3: Find text containing "Playwright" using get_by_text()
        # Hint: Use exact=False for partial match
        # TODO: Uncomment and complete
        # elements = page.get_by_text("YOUR_TEXT_HERE", exact=False).count()
        # print(f"✓ Found {elements} element(s) containing 'Playwright'")

        # Navigate to form page
        page.goto("https://www.automationexercise.com/login")

        # TODO 4: Fill the email field using get_by_placeholder()
        # Hint: Look for placeholder "Email Address"
        # TODO: Uncomment and complete
        # page.get_by_placeholder("YOUR_PLACEHOLDER_HERE").first.fill("test@example.com")
        # print("✓ Filled email using placeholder")

        # TODO 5: Fill the name field using get_by_placeholder()
        # Hint: Look for placeholder "Name"
        # TODO: Uncomment and complete
        # page.get_by_placeholder("YOUR_PLACEHOLDER_HERE").first.fill("John Doe")
        # print("✓ Filled name field")

        # TODO 6: Chain locators - find a button inside a form
        # Hint: page.locator("form").get_by_role("button")
        # TODO: Uncomment and complete
        # button = page.locator("YOUR_CONTAINER_HERE").get_by_role("YOUR_ROLE_HERE").first
        # print(f"✓ Found button inside form")

        print("\n✅ Exercise 3 complete!")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    modern_locators_practice()
