"""
Example 2: Filtering Locators
Demonstrates how to filter locators using has_text, has, and has_not
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_filtering():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Filtering Locators Examples ===\n")

        # Add some test data
        todos = ["Buy groceries", "Walk the dog", "Read a book", "Buy concert tickets", "Buy new shoes"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")
            time.sleep(0.2)

        # Example 1: filter(has_text)
        print("1. Filtering by Text Content")
        # Find todos containing "Buy"
        buy_todos = page.locator("li").filter(has_text="Buy")
        print(f"   Todos containing 'Buy': {buy_todos.count()}")

        # List them
        for todo in buy_todos.all():
            print(f"   - {todo.text_content()}")
        time.sleep(1)

        # Example 2: Filter and Interact
        print("\n2. Filter and Interact")
        # Find the "Walk the dog" todo and mark it complete
        page.locator("li")
            .filter(has_text="Walk the dog")
            .locator("input.toggle")
            .check()
        print("   ✓ Marked 'Walk the dog' as complete")
        time.sleep(1)

        # Example 3: Filter with Exact Text
        print("\n3. Filtering with Partial vs Exact Match")
        # has_text does substring matching
        groceries = page.locator("li").filter(has_text="groceries")
        print(f"   Todos containing 'groceries': {groceries.count()}")

        # Example 4: Multiple Filters
        print("\n4. Combining Multiple Filters")
        # Find todos containing "Buy" that are NOT completed
        active_buy_todos = (
            page.locator("li")
            .filter(has_text="Buy")
            .filter(has_not_text="completed")  # Note: "completed" might be in class, adjust as needed
        )
        print(f"   Active 'Buy' todos: {active_buy_todos.count()}")
        time.sleep(1)

        # Example 5: filter(has=) - Filter by nested element
        print("\n5. Filtering by Nested Element")
        # Find todos that have a checked checkbox
        checked_todos = page.locator("li").filter(
            has=page.locator("input.toggle:checked")
        )
        print(f"   Completed todos: {checked_todos.count()}")
        time.sleep(1)

        # Example 6: filter(has_not=) - Exclude by nested element
        print("\n6. Excluding by Nested Element")
        # Find todos that DON'T have a checked checkbox (active todos)
        active_todos = page.locator("li").filter(
            has_not=page.locator("input.toggle:checked")
        )
        print(f"   Active todos: {active_todos.count()}")
        time.sleep(1)

        # Example 7: Complex Filtering Scenario
        print("\n7. Complex Filtering: Find Specific Todo and Delete")
        # Find "Read a book" and delete it
        # First, let's see total count
        before_count = page.locator("li").count()
        print(f"   Todos before deletion: {before_count}")

        # Find and delete
        read_book_todo = page.locator("li").filter(has_text="Read a book")
        if read_book_todo.count() > 0:
            # Hover to show delete button
            read_book_todo.hover()
            # Find and click delete button within this todo
            read_book_todo.locator("button.destroy").click()
            time.sleep(0.5)

            after_count = page.locator("li").count()
            print(f"   Todos after deletion: {after_count}")
            print("   ✓ Successfully deleted 'Read a book' todo")
        time.sleep(1)

        # Example 8: filter(has_not_text)
        print("\n8. Excluding by Text")
        # Find all todos EXCEPT ones containing "Buy"
        non_buy_todos = page.locator("li").filter(has_not_text="Buy")
        print(f"   Todos NOT containing 'Buy': {non_buy_todos.count()}")
        for todo in non_buy_todos.all():
            print(f"   - {todo.locator("label").text_content()}")
        time.sleep(1)

        # Example 9: Chaining Filters
        print("\n9. Chaining Multiple Filters")
        # Find active todos (not checked) containing "Buy"
        active_buy = (
            page.locator("li")
            .filter(has_text="Buy")
            .filter(has_not=page.locator("input.toggle:checked"))
        )
        print(f"   Active 'Buy' todos (not completed): {active_buy.count()}")

        print("\n=== Filtering Examples Complete ===")
        print("\nKey Takeaways:")
        print("  • filter(has_text) for text content filtering")
        print("  • filter(has=locator) for nested element filtering")
        print("  • filter(has_not_text) to exclude by text")
        print("  • filter(has_not=locator) to exclude by nested element")
        print("  • Filters can be chained for precision")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_filtering()
