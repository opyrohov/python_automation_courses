"""
Example 3: Selection Methods
Demonstrates .first, .last, .nth(), .count(), and .all()
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_selection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Selection Methods Examples ===\n")

        # Add test data
        todos = ["First task", "Second task", "Third task", "Fourth task", "Fifth task"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")
            time.sleep(0.2)

        # Example 1: .count()
        print("1. Counting Elements with .count()")
        total_todos = page.locator("li").count()
        print(f"   Total todos: {total_todos}")
        time.sleep(1)

        # Example 2: .first
        print("\n2. Selecting First Element with .first")
        first_todo_text = page.locator("li").first.text_content()
        print(f"   First todo: {first_todo_text}")

        # Check the first todo
        page.locator("li").first.locator("input.toggle").check()
        print("   ✓ Checked first todo")
        time.sleep(1)

        # Example 3: .last
        print("\n3. Selecting Last Element with .last")
        last_todo_text = page.locator("li").last.text_content()
        print(f"   Last todo: {last_todo_text}")

        # Check the last todo
        page.locator("li").last.locator("input.toggle").check()
        print("   ✓ Checked last todo")
        time.sleep(1)

        # Example 4: .nth(index)
        print("\n4. Selecting by Index with .nth()")
        # Remember: 0-based indexing!
        second_todo = page.locator("li").nth(1)  # index 1 = second item
        second_todo_text = second_todo.text_content()
        print(f"   Second todo (nth(1)): {second_todo_text}")

        third_todo = page.locator("li").nth(2)  # index 2 = third item
        third_todo_text = third_todo.text_content()
        print(f"   Third todo (nth(2)): {third_todo_text}")

        # Check the third todo
        third_todo.locator("input.toggle").check()
        print("   ✓ Checked third todo")
        time.sleep(1)

        # Example 5: Negative Indices
        print("\n5. Using Negative Indices")
        # -1 means last element
        last_with_negative = page.locator("li").nth(-1).text_content()
        print(f"   Last todo (nth(-1)): {last_with_negative}")

        # -2 means second to last
        second_to_last = page.locator("li").nth(-2).text_content()
        print(f"   Second to last (nth(-2)): {second_to_last}")
        time.sleep(1)

        # Example 6: .all() - Get All Elements
        print("\n6. Getting All Elements with .all()")
        all_todos = page.locator("li").all()
        print(f"   Total elements retrieved: {len(all_todos)}")

        print("   All todos:")
        for i, todo in enumerate(all_todos):
            todo_text = todo.locator("label").text_content()
            is_checked = todo.locator("input.toggle").is_checked()
            status = "✓" if is_checked else "○"
            print(f"   {status} {i + 1}. {todo_text}")
        time.sleep(1)

        # Example 7: Iterating with .all()
        print("\n7. Iterating Through Elements")
        unchecked_count = 0
        for todo in all_todos:
            if not todo.locator("input.toggle").is_checked():
                unchecked_count += 1

        print(f"   Unchecked todos: {unchecked_count}")
        print(f"   Checked todos: {len(all_todos) - unchecked_count}")
        time.sleep(1)

        # Example 8: Combining Selection with Filtering
        print("\n8. Combining Selection with Filtering")
        # Get first "task" todo
        first_task = page.locator("li").filter(has_text="task").first.text_content()
        print(f"   First todo containing 'task': {first_task}")

        # Get last "task" todo
        last_task = page.locator("li").filter(has_text="task").last.text_content()
        print(f"   Last todo containing 'task': {last_task}")
        time.sleep(1)

        # Example 9: Practical Use Case - Get All Text Contents
        print("\n9. Extracting All Text Contents")
        # Get all todo texts at once
        all_todo_texts = page.locator("li label").all_text_contents()
        print("   All todo texts:")
        for text in all_todo_texts:
            print(f"   - {text}")
        time.sleep(1)

        # Example 10: Verification with count()
        print("\n10. Using count() for Verification")
        # Verify expected number of elements
        expected_count = 5
        actual_count = page.locator("li").count()

        if actual_count == expected_count:
            print(f"   ✓ Verification passed: {actual_count} todos as expected")
        else:
            print(f"   ✗ Verification failed: Expected {expected_count}, found {actual_count}")

        # Check if specific element exists
        error_message_exists = page.locator(".error-message").count() > 0
        print(f"   Error message present: {error_message_exists}")
        time.sleep(1)

        # Example 11: Performance Note
        print("\n11. Performance Consideration")
        print("   .count() is fast - just counts matches")
        print("   .all() loads all elements - use when you need to interact with each")

        print("\n=== Selection Examples Complete ===")
        print("\nKey Takeaways:")
        print("  • .count() - Get total number of matches")
        print("  • .first - Get first element")
        print("  • .last - Get last element")
        print("  • .nth(index) - Get element at specific position (0-based)")
        print("  • .nth(-1) - Negative indices work (last element)")
        print("  • .all() - Get list of all matching elements")
        print("  • Prefer filtering over position when possible")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_selection()
