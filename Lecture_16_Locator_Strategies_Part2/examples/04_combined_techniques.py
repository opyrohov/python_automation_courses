"""
Example 4: Combined Techniques
Demonstrates using chaining, filtering, and selection together
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_combined_techniques():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Combined Techniques Examples ===\n")

        # Add categorized todos
        todos = [
            "Work: Complete project proposal",
            "Work: Review pull requests",
            "Personal: Buy groceries",
            "Personal: Call mom",
            "Work: Team meeting at 3pm",
            "Personal: Exercise for 30 minutes"
        ]

        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")
            time.sleep(0.2)

        print("Added 6 categorized todos (Work and Personal)\n")
        time.sleep(1)

        # Example 1: Chain + Filter
        print("1. Chaining + Filtering")
        # Find work-related todos
        work_todos = (
            page.locator("ul.todo-list")
            .locator("li")
            .filter(has_text="Work:")
        )
        print(f"   Work todos: {work_todos.count()}")
        time.sleep(1)

        # Example 2: Chain + Filter + Select
        print("\n2. Chaining + Filtering + Selection")
        # Get the first work todo
        first_work = (
            page.locator("ul.todo-list")
            .locator("li")
            .filter(has_text="Work:")
            .first
        )
        first_work_text = first_work.text_content()
        print(f"   First work todo: {first_work_text}")

        # Mark it as complete
        first_work.locator("input.toggle").check()
        print("   ✓ Marked first work todo as complete")
        time.sleep(1)

        # Example 3: Complex Combination
        print("\n3. Complex Combination: Find and Complete All Personal Tasks")
        # Find all personal tasks and mark them complete
        personal_todos = (
            page.locator("section.todoapp")
            .locator("ul.todo-list")
            .locator("li")
            .filter(has_text="Personal:")
        )

        personal_count = personal_todos.count()
        print(f"   Found {personal_count} personal todos")

        # Mark all as complete using .all()
        for todo in personal_todos.all():
            todo.locator("input.toggle").check()
            time.sleep(0.3)

        print("   ✓ Marked all personal todos as complete")
        time.sleep(1)

        # Example 4: Filter + Count for Verification
        print("\n4. Using Filter + Count for Verification")
        # Count completed todos
        completed = (
            page.locator("li")
            .filter(has=page.locator("input.toggle:checked"))
            .count()
        )
        print(f"   Completed todos: {completed}")

        # Count active (not completed) todos
        active = (
            page.locator("li")
            .filter(has_not=page.locator("input.toggle:checked"))
            .count()
        )
        print(f"   Active todos: {active}")
        print(f"   Total: {completed + active}")
        time.sleep(1)

        # Example 5: Nested Filtering
        print("\n5. Nested Filtering")
        # Find active work todos (not completed)
        active_work = (
            page.locator("li")
            .filter(has_text="Work:")
            .filter(has_not=page.locator("input.toggle:checked"))
        )
        print(f"   Active work todos: {active_work.count()}")

        # List them
        for todo in active_work.all():
            print(f"   - {todo.locator('label').text_content()}")
        time.sleep(1)

        # Example 6: Chain → Filter → Select → Chain Again
        print("\n6. Multi-Level Chaining and Filtering")
        # Find the second personal todo and get its text
        second_personal = (
            page.locator("section.todoapp")
            .locator("ul.todo-list")
            .locator("li")
            .filter(has_text="Personal:")
            .nth(1)  # Second one (0-indexed)
            .locator("label")
        )
        print(f"   Second personal todo: {second_personal.text_content()}")
        time.sleep(1)

        # Example 7: Real-World Pattern: Delete Specific Item
        print("\n7. Real-World Pattern: Find and Delete Specific Item")
        # Find "Call mom" todo and delete it
        call_mom_todo = page.locator("li").filter(has_text="Call mom")

        if call_mom_todo.count() > 0:
            before = page.locator("li").count()
            print(f"   Todos before deletion: {before}")

            # Hover to reveal delete button
            call_mom_todo.hover()
            # Click delete button within this specific todo
            call_mom_todo.locator("button.destroy").click()
            time.sleep(0.5)

            after = page.locator("li").count()
            print(f"   Todos after deletion: {after}")
            print("   ✓ Successfully deleted 'Call mom' todo")
        time.sleep(1)

        # Example 8: Get All Uncompleted Work Tasks
        print("\n8. Complex Query: Get All Uncompleted Work Tasks")
        uncompleted_work = (
            page.locator("li")
            .filter(has_text="Work:")
            .filter(has_not=page.locator("input.toggle:checked"))
            .all()
        )

        print(f"   Uncompleted work tasks ({len(uncompleted_work)}):")
        for todo in uncompleted_work:
            print(f"   - {todo.locator('label').text_content()}")
        time.sleep(1)

        # Example 9: Verification Pattern
        print("\n9. Verification Pattern")
        # Verify all personal todos are completed
        personal_all = page.locator("li").filter(has_text="Personal:")
        personal_completed = personal_all.filter(
            has=page.locator("input.toggle:checked")
        )

        if personal_all.count() == personal_completed.count():
            print("   ✓ All personal todos are completed!")
        else:
            incomplete = personal_all.count() - personal_completed.count()
            print(f"   ✗ {incomplete} personal todo(s) still incomplete")
        time.sleep(1)

        # Example 10: Performance Optimization
        print("\n10. Performance Tip")
        print("   ❌ Inefficient: Multiple separate queries")
        print("      - page.locator('li').count()")
        print("      - page.locator('li').filter(...).count()")
        print("      - page.locator('li').filter(...).all()")
        print("\n   ✅ Efficient: Reuse locator")
        all_items = page.locator("li")
        total = all_items.count()
        work_items = all_items.filter(has_text="Work:")
        work_count = work_items.count()
        print(f"      Total: {total}, Work: {work_count}")

        print("\n=== Combined Techniques Examples Complete ===")
        print("\nKey Takeaways:")
        print("  • Chain locators for structure navigation")
        print("  • Filter to narrow down matches")
        print("  • Select specific elements with .first, .last, .nth()")
        print("  • Combine all three for maximum precision")
        print("  • Reuse locators for better performance")
        print("  • Always verify counts before interacting")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    demonstrate_combined_techniques()
