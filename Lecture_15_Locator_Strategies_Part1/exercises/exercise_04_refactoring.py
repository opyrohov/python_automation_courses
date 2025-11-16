"""
Exercise 4: Locator Refactoring Challenge
Refactor bad locators into good ones

Task: The code below uses BAD locator practices.
      Your job is to refactor them into BETTER locators.
"""

from playwright.sync_api import sync_playwright

def refactoring_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Locator Refactoring Challenge ===\n")

        # BAD PRACTICE 1: Using absolute XPath
        print("1. Refactor absolute XPath to modern locator")
        print("   BAD: page.locator('xpath=/html/body/section/div/header/input')")
        # TODO: Refactor to use get_by_placeholder() or a better selector
        # Current (bad):
        # page.locator("xpath=/html/body/section/div/header/input").fill("Task 1")

        # TODO: Replace with better locator
        # page.REFACTOR_THIS_LOCATOR.fill("Task 1 - Refactored")
        # page.REFACTOR_THIS_LOCATOR.press("Enter")

        # BAD PRACTICE 2: Position-based selector
        print("\n2. Refactor position-based selector")
        print("   BAD: page.locator('li:nth-child(1)')")

        # Add some todos first
        page.locator(".new-todo").fill("First item")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").fill("Second item")
        page.locator(".new-todo").press("Enter")

        # Current (bad):
        # first_todo = page.locator("li:nth-child(1)").text_content()

        # TODO: Refactor to find by text using get_by_text()
        # first_todo = page.REFACTOR_THIS_LOCATOR.text_content()
        # print(f"   Found: {first_todo}")

        # BAD PRACTICE 3: Overly specific selector
        print("\n3. Refactor overly specific selector")
        print("   BAD: page.locator('section.todoapp > div.main > ul.todo-list > li > div > label')")

        # Current (bad):
        # label = page.locator("section.todoapp > div.main > ul.todo-list > li > div > label").first

        # TODO: Refactor to simpler, more maintainable selector
        # Hint: Just ".todo-list label" would work!
        # label = page.locator("REFACTOR_THIS_LOCATOR").first
        # print(f"   Found label: {label.text_content()}")

        # BAD PRACTICE 4: Generic selector that matches many elements
        print("\n4. Refactor generic selector")
        print("   BAD: page.locator('input')")

        # Current (bad) - matches multiple inputs!
        # bad_count = page.locator("input").count()
        # print(f"   Generic 'input' matches {bad_count} elements!")

        # TODO: Refactor to be specific - target the .new-todo input
        # Hint: Use class, placeholder, or combination
        # good_locator = page.locator("REFACTOR_THIS_LOCATOR")
        # good_locator.fill("Specific input")
        # print("   ✓ Filled the correct input")

        # BAD PRACTICE 5: Using generated/dynamic classes
        print("\n5. Refactor away from generated classes")
        print("   BAD: page.locator('.css-xyz123-generated')")
        print("   (This is simulated - the todo app doesn't have generated classes)")

        # TODO: Imagine the input had a generated class like "css-xyz123"
        # How would you select it instead?
        # Answer: Use semantic attributes like placeholder, name, or add a test ID
        # Example:
        # Instead of: page.locator(".css-xyz123").fill("text")
        # Use: page.get_by_placeholder("What needs to be done?").fill("text")

        print("\n=== End of Refactoring Challenge ===")
        print("\nKey Learnings:")
        print("  • Avoid absolute paths → Use relative selectors")
        print("  • Avoid positions → Use text, labels, or roles")
        print("  • Avoid overly specific → Keep it simple")
        print("  • Avoid generic → Be specific but not brittle")
        print("  • Avoid generated classes → Use semantic attributes")

        input("\nPress Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    refactoring_challenge()
