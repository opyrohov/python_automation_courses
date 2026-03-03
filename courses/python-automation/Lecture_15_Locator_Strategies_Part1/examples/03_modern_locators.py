"""
Example 3: Playwright Modern Locators
Demonstrates Playwright's recommended modern locator strategies
"""

from playwright.sync_api import sync_playwright, expect
import time

def demonstrate_modern_locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website with better semantic HTML
        page.goto("https://playwright.dev/")

        print("=== Playwright Modern Locator Examples ===\n")

        # Example 1: get_by_role() - The best locator!
        print("1. Using get_by_role() - THE RECOMMENDED WAY")

        # Find and interact with links by role
        docs_link = page.get_by_role("link", name="Docs")
        if docs_link.is_visible():
            print("   ✓ Found 'Docs' link using get_by_role()")

        # Find navigation by role
        nav = page.get_by_role("navigation")
        if nav.count() > 0:
            print(f"   ✓ Found {nav.count()} navigation element(s)")

        # Example 2: get_by_text()
        print("\n2. Using get_by_text()")

        # Exact text match
        heading = page.get_by_text("Playwright", exact=False)
        if heading.count() > 0:
            print(f"   ✓ Found {heading.count()} element(s) containing 'Playwright'")

        # Example 3: Chaining locators
        print("\n3. Chaining Modern Locators")

        # Find a link within navigation
        nav_link = page.get_by_role("navigation").get_by_role("link").first
        if nav_link.is_visible():
            print("   ✓ Found first link inside navigation using chained locators")

        # Navigate to a form page for more examples
        print("\n4. Navigating to form demo...")
        page.goto("https://www.automationexercise.com/login")
        time.sleep(1)

        # Example 4: get_by_placeholder()
        print("\n5. Using get_by_placeholder()")

        # Find input by placeholder
        email_input = page.get_by_placeholder("Email Address")
        if email_input.count() > 0:
            email_input.first.fill("test@example.com")
            print("   ✓ Filled email using get_by_placeholder()")

        # Example 5: get_by_label() - Great for forms!
        print("\n6. Using get_by_label()")

        # Try to find inputs by label
        name_input = page.get_by_placeholder("Name")
        if name_input.count() > 0:
            name_input.first.fill("John Doe")
            print("   ✓ Filled name field")

        # Example 6: Combining with CSS
        print("\n7. Combining Modern Locators with CSS")

        # Use CSS to narrow down, then modern locator
        form_button = page.locator("form").get_by_role("button").first
        if form_button.count() > 0:
            print("   ✓ Found button inside form using combined approach")

        print("\n=== Modern Locator Examples Complete ===")
        print("\nKey Takeaway: Modern locators are:")
        print("  • More resilient to changes")
        print("  • User-facing (better accessibility)")
        print("  • Self-documenting")
        print("  • Playwright's recommended approach!")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_modern_locators()
