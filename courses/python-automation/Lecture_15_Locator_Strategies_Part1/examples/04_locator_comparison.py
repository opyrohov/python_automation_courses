"""
Example 4: Locator Strategy Comparison
Shows different ways to locate the same element and their pros/cons
"""

from playwright.sync_api import sync_playwright
import time

def compare_locator_strategies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Locator Strategy Comparison ===\n")
        print("Finding the same element (todo input) using different strategies:\n")

        # The element we're targeting:
        # <input class="new-todo" placeholder="What needs to be done?" autofocus="">

        # Strategy 1: CSS Class Selector
        print("1. CSS Class Selector: .new-todo")
        try:
            page.locator(".new-todo").fill("Strategy 1: CSS Class")
            page.locator(".new-todo").press("Enter")
            print("   ✓ Success")
            print("   Pros: Simple, fast")
            print("   Cons: Classes can change, may not be unique")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        # Strategy 2: CSS Attribute Selector
        print("\n2. CSS Attribute Selector: [placeholder='...']")
        try:
            page.locator("[placeholder='What needs to be done?']").fill("Strategy 2: Attribute")
            page.locator("[placeholder='What needs to be done?']").press("Enter")
            print("   ✓ Success")
            print("   Pros: More specific, semantic")
            print("   Cons: Long attribute values can be verbose")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        # Strategy 3: CSS Combined Selector
        print("\n3. CSS Combined: input.new-todo")
        try:
            page.locator("input.new-todo").fill("Strategy 3: Combined CSS")
            page.locator("input.new-todo").press("Enter")
            print("   ✓ Success")
            print("   Pros: More specific than class alone")
            print("   Cons: Still depends on class names")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        # Strategy 4: XPath by class
        print("\n4. XPath by class: xpath=//input[@class='new-todo']")
        try:
            page.locator("xpath=//input[@class='new-todo']").fill("Strategy 4: XPath")
            page.locator("xpath=//input[@class='new-todo']").press("Enter")
            print("   ✓ Success")
            print("   Pros: Powerful for complex queries")
            print("   Cons: Slower, less readable, harder to maintain")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        # Strategy 5: XPath by attribute
        print("\n5. XPath by attribute: xpath=//input[@placeholder='...']")
        try:
            page.locator("xpath=//input[@placeholder='What needs to be done?']").fill("Strategy 5: XPath Attr")
            page.locator("xpath=//input[@placeholder='What needs to be done?']").press("Enter")
            print("   ✓ Success")
            print("   Pros: Flexible")
            print("   Cons: CSS can do this better and faster")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        # Strategy 6: Playwright get_by_placeholder()
        print("\n6. Modern Locator: get_by_placeholder('...')")
        try:
            page.get_by_placeholder("What needs to be done?").fill("Strategy 6: Modern!")
            page.get_by_placeholder("What needs to be done?").press("Enter")
            print("   ✓ Success")
            print("   Pros: User-facing, resilient, readable, RECOMMENDED!")
            print("   Cons: Requires placeholder attribute")
            time.sleep(1)
        except Exception as e:
            print(f"   ✗ Failed: {e}")

        print("\n" + "="*60)
        print("VERDICT: Which strategy to use?")
        print("="*60)
        print("\n🏆 BEST: Modern Locators (get_by_placeholder, get_by_role)")
        print("   → Most resilient, user-facing, accessible")
        print("\n🥈 GOOD: CSS with semantic attributes ([placeholder], #id)")
        print("   → Fast, readable, stable")
        print("\n🥉 OK: CSS classes (when stable)")
        print("   → Simple but can break with styling changes")
        print("\n⚠️  USE SPARINGLY: XPath")
        print("   → Only when CSS can't express the relationship")
        print("\n" + "="*60)

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    compare_locator_strategies()
