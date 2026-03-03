"""
Example 2: XPath Locators
Demonstrates XPath selector strategies in Playwright
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_xpath():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== XPath Locator Examples ===\n")

        # Example 1: Basic XPath by tag
        print("1. Basic XPath - Select by tag")
        page.locator("xpath=//input[@class='new-todo']").fill("Learn XPath Basics")
        page.locator("xpath=//input[@class='new-todo']").press("Enter")
        print("   ✓ Added todo using XPath tag selector")
        time.sleep(1)

        # Example 2: XPath by attribute
        print("\n2. XPath - Select by attribute")
        page.locator("xpath=//input[@placeholder='What needs to be done?']").fill("Learn XPath Attributes")
        page.locator("xpath=//input[@placeholder='What needs to be done?']").press("Enter")
        print("   ✓ Added todo using XPath attribute selector")
        time.sleep(1)

        # Example 3: XPath with contains()
        print("\n3. XPath - Using contains() function")
        # Find elements where class contains 'todo'
        count = page.locator("xpath=//*[contains(@class, 'todo')]").count()
        print(f"   ✓ Found {count} elements with 'todo' in class using contains()")

        # Example 4: XPath text matching
        print("\n4. XPath - Text matching")
        # Add a specific todo first
        page.locator("xpath=//input[@class='new-todo']").fill("Buy groceries")
        page.locator("xpath=//input[@class='new-todo']").press("Enter")
        time.sleep(0.5)

        # Find by exact text
        grocery_todo = page.locator("xpath=//label[text()='Buy groceries']")
        if grocery_todo.count() > 0:
            print("   ✓ Found todo with exact text 'Buy groceries'")

        # Example 5: XPath with contains(text())
        print("\n5. XPath - Using contains(text())")
        # Find todos containing 'XPath'
        xpath_todos = page.locator("xpath=//label[contains(text(), 'XPath')]").count()
        print(f"   ✓ Found {xpath_todos} todos containing 'XPath'")

        # Example 6: XPath parent navigation
        print("\n6. XPath - Navigate to parent")
        # Find a label and go to its parent
        # This is something CSS can't do easily!
        parent_count = page.locator("xpath=//label/parent::div").count()
        print(f"   ✓ Found {parent_count} parent <div> elements of <label>")

        # Example 7: XPath following-sibling
        print("\n7. XPath - Following sibling")
        # Find siblings that come after an element
        siblings = page.locator("xpath=//input[@class='new-todo']/following-sibling::*").count()
        print(f"   ✓ Found {siblings} elements after the input field")

        # Example 8: XPath with multiple conditions
        print("\n8. XPath - Multiple conditions (AND)")
        # Find input with specific type AND class
        multi_cond = page.locator("xpath=//input[@class='new-todo' and @placeholder='What needs to be done?']")
        if multi_cond.count() > 0:
            print("   ✓ Found input matching multiple conditions")

        # Example 9: XPath starts-with()
        print("\n9. XPath - Using starts-with()")
        page.locator("xpath=//input[@class='new-todo']").fill("Complete this task")
        page.locator("xpath=//input[@class='new-todo']").press("Enter")
        time.sleep(0.5)

        # Find todos starting with 'Complete'
        starts_with_count = page.locator("xpath=//label[starts-with(text(), 'Complete')]").count()
        print(f"   ✓ Found {starts_with_count} todos starting with 'Complete'")

        print("\n=== XPath Examples Complete ===")
        print("\nNote: XPath is powerful but use it sparingly!")
        print("Prefer CSS or Playwright's modern locators when possible.")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_xpath()
