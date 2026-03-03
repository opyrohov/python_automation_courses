"""
Exercise 1: Chaining Practice
Practice chaining locators for precise targeting

Task: Complete the TODOs by chaining locators appropriately
"""

from playwright.sync_api import sync_playwright

def chaining_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add some test data
        todos = ["Work: Finish report", "Personal: Buy milk", "Work: Team meeting"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Chain to find the input field
        # Start from section.todoapp, then find header, then find the input
        # Replace YOUR_CHAIN_HERE
        # page.locator("section.todoapp").YOUR_CHAIN_HERE.fill("Chained task")
        # page.locator("section.todoapp").YOUR_CHAIN_HERE.press("Enter")

        # TODO 2: Chain to check the first todo's checkbox
        # Start from ul.todo-list, find first li, then find the checkbox input
        # Replace YOUR_CHAIN_HERE
        # page.locator("ul.todo-list").YOUR_CHAIN_HERE.check()

        # TODO 3: Chain to get the text of the second todo
        # Start from section.todoapp, find ul.todo-list, get second li, get label
        # Uncomment and replace YOUR_CHAIN_HERE
        # second_todo = page.locator("section.todoapp").YOUR_CHAIN_HERE.text_content()
        # print(f"Second todo: {second_todo}")

        # TODO 4: Count todos using chaining
        # Chain from section.todoapp to ul.todo-list to li elements
        # Uncomment and replace YOUR_CHAIN_HERE
        # todo_count = page.locator("section.todoapp").YOUR_CHAIN_HERE.count()
        # print(f"Total todos: {todo_count}")

        print("\n✅ Exercise 1 complete! Check the browser to verify.")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    chaining_practice()
