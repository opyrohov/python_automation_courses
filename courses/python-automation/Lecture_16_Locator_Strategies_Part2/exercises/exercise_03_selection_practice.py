"""
Exercise 3: Selection Practice
Practice using .first, .last, .nth(), .count(), and .all()

Task: Complete the TODOs using appropriate selection methods
"""

from playwright.sync_api import sync_playwright

def selection_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add test data
        todos = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Get and print the text of the first todo
        # Use .first
        # Uncomment and replace YOUR_SELECTOR_HERE
        # first_text = page.locator("li").YOUR_SELECTOR_HERE.text_content()
        # print(f"First todo: {first_text}")

        # TODO 2: Check the last todo as complete
        # Use .last and chain to the checkbox
        # Uncomment and replace YOUR_SELECTOR_HERE
        # page.locator("li").YOUR_SELECTOR_HERE.locator("input.toggle").check()
        # print("✓ Checked last todo")

        # TODO 3: Get the text of the third todo (index 2)
        # Use .nth(2)
        # Uncomment and replace YOUR_SELECTOR_HERE
        # third_text = page.locator("li").YOUR_SELECTOR_HERE.text_content()
        # print(f"Third todo: {third_text}")

        # TODO 4: Get the second-to-last todo using negative index
        # Use .nth(-2)
        # Uncomment and replace YOUR_SELECTOR_HERE
        # second_last_text = page.locator("li").YOUR_SELECTOR_HERE.text_content()
        # print(f"Second to last: {second_last_text}")

        # TODO 5: Count total todos
        # Use .count()
        # Uncomment and replace YOUR_METHOD_HERE
        # total = page.locator("li").YOUR_METHOD_HERE
        # print(f"Total todos: {total}")

        # TODO 6: Get all todos and iterate through them
        # Use .all()
        # Uncomment and replace YOUR_METHOD_HERE
        # all_todos = page.locator("li").YOUR_METHOD_HERE
        # print("All todos:")
        # for i, todo in enumerate(all_todos):
        #     print(f"  {i + 1}. {todo.locator('label').text_content()}")

        # TODO 7: Verify a specific element exists
        # Check if there are more than 0 elements matching
        # Uncomment and complete
        # error_exists = page.locator(".error-message").YOUR_METHOD_HERE > 0
        # print(f"Error message exists: {error_exists}")

        print("\n✅ Exercise 3 complete!")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    selection_practice()
