"""
Example 5: Debugging Locators
Techniques to debug and troubleshoot locators
"""

from playwright.sync_api import sync_playwright
import time

def debug_locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Debugging Locator Techniques ===\n")

        # Add some todos first
        page.locator(".new-todo").fill("First task")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").fill("Second task")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").fill("Third task")
        page.locator(".new-todo").press("Enter")
        time.sleep(1)

        # Technique 1: Count elements
        print("1. Counting Elements")
        button_count = page.locator("button").count()
        print(f"   Total buttons on page: {button_count}")

        li_count = page.locator("li").count()
        print(f"   Total list items on page: {li_count}")

        todo_count = page.locator(".todo-list li").count()
        print(f"   Todo items in list: {todo_count}")

        # Technique 2: Check if element exists
        print("\n2. Checking Element Existence")
        exists = page.locator(".new-todo").count() > 0
        print(f"   Does .new-todo exist? {exists}")

        not_exists = page.locator(".does-not-exist").count() > 0
        print(f"   Does .does-not-exist exist? {not_exists}")

        # Technique 3: Get all text contents
        print("\n3. Getting All Text Contents")
        todo_texts = page.locator(".todo-list li label").all_text_contents()
        print(f"   All todo texts: {todo_texts}")

        # Technique 4: Get element attributes
        print("\n4. Getting Element Attributes")
        input_placeholder = page.locator(".new-todo").get_attribute("placeholder")
        print(f"   Input placeholder: '{input_placeholder}'")

        input_class = page.locator(".new-todo").get_attribute("class")
        print(f"   Input class: '{input_class}'")

        # Technique 5: Check visibility
        print("\n5. Checking Visibility")
        is_visible = page.locator(".new-todo").is_visible()
        print(f"   Is input visible? {is_visible}")

        hidden_element = page.locator(".hidden-element-xyz").is_visible()
        print(f"   Is .hidden-element-xyz visible? {hidden_element}")

        # Technique 6: Filter elements
        print("\n6. Filtering Elements")
        # Get all todos
        all_todos = page.locator(".todo-list li")
        print(f"   Total todos: {all_todos.count()}")

        # Filter todos containing specific text
        first_task_todos = all_todos.filter(has_text="First")
        print(f"   Todos containing 'First': {first_task_todos.count()}")

        # Technique 7: Get first, last, nth element
        print("\n7. Accessing Specific Elements")
        first_todo = page.locator(".todo-list li").first.text_content()
        print(f"   First todo: {first_todo}")

        last_todo = page.locator(".todo-list li").last.text_content()
        print(f"   Last todo: {last_todo}")

        second_todo = page.locator(".todo-list li").nth(1).text_content()
        print(f"   Second todo (nth(1)): {second_todo}")

        # Technique 8: Highlight element (visual debugging)
        print("\n8. Highlighting Elements (Visual Debugging)")
        print("   Highlighting the input field...")
        page.locator(".new-todo").highlight()
        time.sleep(2)

        print("   Highlighting first todo item...")
        page.locator(".todo-list li").first.highlight()
        time.sleep(2)

        # Technique 9: Take screenshot of element
        print("\n9. Taking Element Screenshots")
        print("   Taking screenshot of input field...")
        page.locator(".new-todo").screenshot(path="input_screenshot.png")
        print("   ✓ Saved to input_screenshot.png")

        print("   Taking screenshot of todo list...")
        page.locator(".todo-list").screenshot(path="todolist_screenshot.png")
        print("   ✓ Saved to todolist_screenshot.png")

        # Technique 10: Print locator info
        print("\n10. Debugging Locator Strings")
        locator = page.locator(".todo-list li")
        print(f"   Locator: {locator}")
        print(f"   Count: {locator.count()}")

        # Technique 11: Try-Except for locator errors
        print("\n11. Handling Locator Errors")
        try:
            # This will timeout if element doesn't exist
            page.locator(".element-that-does-not-exist").click(timeout=2000)
        except Exception as e:
            print(f"   ✓ Caught error: {type(e).__name__}")
            print(f"   Message: Element not found (expected)")

        # Technique 12: Wait for element
        print("\n12. Waiting for Elements")
        print("   Waiting for input field to be visible...")
        page.locator(".new-todo").wait_for(state="visible", timeout=5000)
        print("   ✓ Input field is visible")

        print("\n=== Debugging Techniques Complete ===")
        print("\nPro Tips:")
        print("  • Use count() > 0 to check existence")
        print("  • Use all_text_contents() to see all matching elements")
        print("  • Use highlight() to visually debug")
        print("  • Use screenshot() to capture element state")
        print("  • Use PWDEBUG=1 for interactive debugging")
        print("  • Use browser DevTools to test selectors: ")
        print("    - document.querySelector('.selector')")
        print("    - $x('//xpath/expression')")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    debug_locators()
