"""
Exercise 4: Combined Mastery
Combine chaining, filtering, and selection in realistic scenarios

Task: Solve real-world problems using all techniques together
"""

from playwright.sync_api import sync_playwright

def combined_mastery():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add categorized todos
        todos = [
            "Work: Review code",
            "Personal: Call dentist",
            "Work: Write documentation",
            "Personal: Buy birthday gift",
            "Work: Fix bug #123",
            "Personal: Book vacation"
        ]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Find and mark the first "Work:" todo as complete
        # Hint: Filter for "Work:" then use .first, then chain to checkbox
        # Uncomment and complete
        # page.locator("li").filter(YOUR_FILTER).first.locator("input.toggle").check()
        # print("✓ Marked first work todo as complete")

        # TODO 2: Count how many "Personal:" todos there are
        # Hint: Filter for "Personal:" then count
        # Uncomment and complete
        # personal_count = page.locator("li").filter(YOUR_FILTER).count()
        # print(f"Personal todos: {personal_count}")

        # TODO 3: Get the text of the second "Work:" todo
        # Hint: Filter for "Work:", use .nth(1), get text
        # Uncomment and complete
        # second_work = page.locator("li").filter(YOUR_FILTER).nth(1).locator("label").text_content()
        # print(f"Second work todo: {second_work}")

        # TODO 4: Mark ALL "Personal:" todos as complete
        # Hint: Filter for "Personal:", use .all(), iterate and check each
        # Uncomment and complete
        # personal_todos = page.locator("li").filter(YOUR_FILTER).all()
        # for todo in personal_todos:
        #     todo.locator("input.toggle").check()
        # print(f"✓ Marked all {len(personal_todos)} personal todos as complete")

        # TODO 5: Find active (not completed) "Work:" todos
        # Hint: Filter for "Work:" AND filter for NOT checked
        # Use filter(has_not=...)
        # Uncomment and complete
        # active_work = page.locator("li").filter(YOUR_FILTER_1).filter(YOUR_FILTER_2).count()
        # print(f"Active work todos: {active_work}")

        # TODO 6: Verify all personal todos are completed
        # Hint: Count personal todos, count completed personal todos, compare
        # Uncomment and complete
        # total_personal = page.locator("li").filter(YOUR_FILTER).count()
        # completed_personal = page.locator("li").filter(YOUR_FILTER_1).filter(YOUR_FILTER_2).count()
        # if total_personal == completed_personal:
        #     print("✓ All personal todos are completed!")
        # else:
        #     print(f"✗ {total_personal - completed_personal} personal todos still pending")

        # TODO 7: Get all work todo texts and print them
        # Hint: Filter for "Work:", use .all(), extract label text
        # Uncomment and complete
        # work_todos = page.locator("li").filter(YOUR_FILTER).all()
        # print("Work todos:")
        # for todo in work_todos:
        #     text = todo.locator("label").text_content()
        #     is_done = todo.locator("input.toggle").is_checked()
        #     status = "✓" if is_done else "○"
        #     print(f"  {status} {text}")

        print("\n✅ Exercise 4 complete!")
        print("This exercise tested your ability to combine:")
        print("  • Chaining (container → element)")
        print("  • Filtering (by text and by nested elements)")
        print("  • Selection (.first, .nth(), .all())")
        input("\nPress Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    combined_mastery()
