"""
Exercise 2: Filtering Challenge
Practice using filter(has_text), filter(has), and filter(has_not)

Task: Complete the TODOs using appropriate filtering methods
"""

from playwright.sync_api import sync_playwright

def filtering_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add test data
        todos = ["Buy groceries", "Buy concert tickets", "Walk the dog", "Read a book", "Buy new shoes"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # Mark some as complete
        page.locator("li").first.locator("input.toggle").check()
        page.locator("li").nth(2).locator("input.toggle").check()

        # TODO 1: Filter todos containing "Buy"
        # Use filter(has_text="...")
        # Replace YOUR_FILTER_HERE
        # buy_todos = page.locator("li").YOUR_FILTER_HERE
        # print(f"Todos containing 'Buy': {buy_todos.count()}")

        # TODO 2: Filter and find the "Walk the dog" todo, then mark it complete
        # Use filter to find it, then chain to checkbox
        # Replace YOUR_FILTER_HERE
        # page.locator("li").YOUR_FILTER_HERE.locator("input.toggle").check()
        # print("✓ Marked 'Walk the dog' as complete")

        # TODO 3: Filter for completed todos
        # Use filter(has=...) with a locator for checked checkboxes
        # Hint: input.toggle:checked
        # Uncomment and replace YOUR_FILTER_HERE
        # completed = page.locator("li").YOUR_FILTER_HERE.count()
        # print(f"Completed todos: {completed}")

        # TODO 4: Filter for active (NOT completed) todos
        # Use filter(has_not=...)
        # Uncomment and replace YOUR_FILTER_HERE
        # active = page.locator("li").YOUR_FILTER_HERE.count()
        # print(f"Active todos: {active}")

        # TODO 5: Find active "Buy" todos (combine two filters!)
        # Filter for "Buy" AND not completed
        # Uncomment and replace YOUR_FILTERS_HERE
        # active_buy = page.locator("li").YOUR_FILTERS_HERE.count()
        # print(f"Active 'Buy' todos: {active_buy}")

        print("\n✅ Exercise 2 complete!")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    filtering_challenge()
