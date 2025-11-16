"""
Example 1: CSS Selectors
Demonstrates various CSS selector strategies in Playwright
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_css_selectors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== CSS Selector Examples ===\n")

        # Example 1: ID Selector (#id)
        print("1. Using ID Selector (#id)")
        # Note: This is just for demonstration
        # The todo site doesn't use IDs in this particular structure

        # Example 2: Class Selector (.class)
        print("2. Using Class Selector (.class)")
        # Select the input field by class
        page.locator(".new-todo").fill("Learn CSS Selectors")
        page.locator(".new-todo").press("Enter")
        print("   ✓ Added todo using class selector")
        time.sleep(1)

        # Example 3: Attribute Selector ([attribute])
        print("\n3. Using Attribute Selector ([attribute='value'])")
        page.locator("[placeholder='What needs to be done?']").fill("Learn Attribute Selectors")
        page.locator("[placeholder='What needs to be done?']").press("Enter")
        print("   ✓ Added todo using attribute selector")
        time.sleep(1)

        # Example 4: Tag Selector
        print("\n4. Using Tag Selector")
        # Count all list items
        count = page.locator("li").count()
        print(f"   ✓ Found {count} list items using tag selector")

        # Example 5: Combining Selectors
        print("\n5. Combining Selectors (tag + class)")
        page.locator("input.new-todo").fill("Learn Combined Selectors")
        page.locator("input.new-todo").press("Enter")
        print("   ✓ Added todo using combined selector (input.new-todo)")
        time.sleep(1)

        # Example 6: Attribute with partial match
        print("\n6. Using Attribute Partial Match ([attr*='value'])")
        # Find elements where class contains 'todo'
        todos = page.locator("[class*='todo']").count()
        print(f"   ✓ Found {todos} elements with 'todo' in class")

        # Example 7: Child Combinator (>)
        print("\n7. Using Child Combinator (parent > child)")
        # This selects direct children only
        list_items = page.locator("ul.todo-list > li").count()
        print(f"   ✓ Found {list_items} direct <li> children of <ul class='todo-list'>")

        # Example 8: Descendant Combinator (space)
        print("\n8. Using Descendant Combinator (ancestor descendant)")
        # This selects all descendants at any level
        descendants = page.locator("section label").count()
        print(f"   ✓ Found {descendants} <label> elements inside <section>")

        print("\n=== CSS Selector Examples Complete ===")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_css_selectors()
