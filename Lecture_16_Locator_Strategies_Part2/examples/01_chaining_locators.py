"""
Example 1: Chaining Locators
Demonstrates how to chain locators for precise element targeting
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_chaining():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Chaining Locators Examples ===\n")

        # Example 1: Basic Chaining
        print("1. Basic Chaining")
        # Without chaining - might match wrong element
        # With chaining - precise targeting
        page.locator("input.new-todo").fill("Chaining Example 1")
        page.locator("input.new-todo").press("Enter")
        print("   ✓ Added todo using basic locator")
        time.sleep(1)

        # Example 2: Chaining CSS Selectors
        print("\n2. Chaining CSS Selectors")
        # Navigate from broad to specific
        page.locator("section.todoapp").locator("header").locator("input").fill("Chaining Example 2")
        page.locator("section.todoapp").locator("header").locator("input").press("Enter")
        print("   ✓ Added todo using chained CSS selectors")
        time.sleep(1)

        # Example 3: Chaining with Modern Locators
        print("\n3. Mixing CSS with Modern Locators")
        # Start with CSS container, then use modern locator
        page.locator("header.header").locator("input[placeholder='What needs to be done?']").fill("Modern Chaining")
        page.locator("header.header").locator("input[placeholder='What needs to be done?']").press("Enter")
        print("   ✓ Added todo using mixed locators")
        time.sleep(1)

        # Example 4: Practical Chaining Scenario
        print("\n4. Practical Scenario: Working with Todo Items")
        # Add a few more todos
        todos = ["Buy groceries", "Walk the dog", "Read a book"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")
            time.sleep(0.3)

        # Chain to find checkbox within a specific todo
        # First, find the todo list, then find the first item, then find its checkbox
        todo_list = page.locator("ul.todo-list")
        first_todo = todo_list.locator("li").first
        first_todo_checkbox = first_todo.locator("input.toggle")
        first_todo_checkbox.check()
        print("   ✓ Checked first todo using chained locators")
        time.sleep(1)

        # Example 5: Complex Chaining
        print("\n5. Complex Chaining Example")
        # Navigate through deep structure
        page.locator("section.todoapp")
            .locator("section.main")
            .locator("ul.todo-list")
            .locator("li")
            .nth(1)
            .locator("input.toggle")
            .check()
        print("   ✓ Checked second todo using deep chaining")
        time.sleep(1)

        # Example 6: Chaining for Verification
        print("\n6. Using Chaining for Verification")
        # Count todos in the list
        todo_count = page.locator("section.todoapp").locator("ul.todo-list").locator("li").count()
        print(f"   ✓ Found {todo_count} todos using chained locators")

        # Example 7: Chaining vs No Chaining Comparison
        print("\n7. Comparison: With and Without Chaining")
        print("   Without chaining:")
        all_inputs = page.locator("input").count()
        print(f"   - page.locator('input').count() = {all_inputs} (too broad!)")

        print("   With chaining:")
        todo_inputs = page.locator("section.todoapp").locator("input.new-todo").count()
        print(f"   - page.locator('.todoapp').locator('.new-todo').count() = {todo_inputs} (specific!)")

        print("\n=== Chaining Examples Complete ===")
        print("\nKey Takeaways:")
        print("  • Chain from broad (container) to specific (element)")
        print("  • Keeps locators more maintainable")
        print("  • Reduces ambiguity when multiple elements match")
        print("  • Can mix CSS and modern locators")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_chaining()
