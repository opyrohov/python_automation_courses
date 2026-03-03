"""
Example 5: Playwright Inspector Demo
Demonstrates how to use Playwright Inspector for debugging
"""

from playwright.sync_api import sync_playwright
import time

def inspector_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Playwright Inspector Demo ===\n")
        print("This example demonstrates using Playwright Inspector for debugging\n")

        # Add some test data
        todos = ["Task 1", "Task 2", "Task 3"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")
            time.sleep(0.2)

        print("To use Playwright Inspector, you have two options:\n")
        print("Option 1: Run with PWDEBUG=1")
        print("  Windows (CMD):       set PWDEBUG=1 && python 05_inspector_demo.py")
        print("  Windows (PowerShell): $env:PWDEBUG=1; python 05_inspector_demo.py")
        print("  Mac/Linux:           PWDEBUG=1 python 05_inspector_demo.py\n")

        print("Option 2: Use page.pause() (we'll do this now)\n")

        print("=" * 60)
        print("PAUSING FOR INSPECTOR")
        print("=" * 60)
        print("\nThe Inspector window should open now!")
        print("\nTry these actions in the Inspector:")
        print("  1. Click 'Explore' button to pick elements from the page")
        print("  2. Use the locator playground to test different selectors")
        print("  3. Try these locators:")
        print("     - page.locator('.new-todo')")
        print("     - page.locator('li')")
        print("     - page.locator('li').filter(has_text='Task 1')")
        print("     - page.locator('li').first")
        print("  4. See how many elements each locator matches")
        print("  5. Click 'Resume' or press F8 to continue\n")

        # Pause here - Inspector opens
        page.pause()

        print("\n✓ Inspector session completed!\n")

        # Continue with some actions to demonstrate stepping
        print("Now we'll perform some actions you can step through:")
        print("  (If still in Inspector, use Step Over to see each action)\n")

        # Action 1
        print("Action 1: Marking first todo as complete...")
        page.locator("li").first.locator("input.toggle").check()
        time.sleep(0.5)

        # Action 2
        print("Action 2: Adding a new todo...")
        page.locator(".new-todo").fill("Inspector Demo Task")
        page.locator(".new-todo").press("Enter")
        time.sleep(0.5)

        # Action 3
        print("Action 3: Counting todos...")
        count = page.locator("li").count()
        print(f"   Total todos: {count}")
        time.sleep(0.5)

        # Action 4
        print("Action 4: Filtering todos...")
        task_todos = page.locator("li").filter(has_text="Task")
        print(f"   Todos containing 'Task': {task_todos.count()}")
        time.sleep(0.5)

        print("\n=== Inspector Demo Tips ===")
        print("\n1. Use Explorer to Pick Elements:")
        print("   - Click the 'Pick locator' button")
        print("   - Click any element on the page")
        print("   - Inspector suggests multiple locator strategies")
        print("   - Choose the most reliable one for your needs")

        print("\n2. Use Locator Playground:")
        print("   - Type locators in the text box")
        print("   - See real-time highlighting of matched elements")
        print("   - Shows count of matches")
        print("   - Test different strategies before coding")

        print("\n3. Step Through Code:")
        print("   - Use Step Over (F10) to execute line by line")
        print("   - See exactly what each locator matches")
        print("   - Verify actions have desired effect")
        print("   - Debug failing tests interactively")

        print("\n4. Common Debugging Workflow:")
        print("   a. Add page.pause() before failing locator")
        print("   b. Run test")
        print("   c. Use Explorer to pick the element")
        print("   d. Try suggested locators in playground")
        print("   e. Verify the locator matches correctly")
        print("   f. Copy working locator to your code")
        print("   g. Resume and verify test passes")

        print("\n5. Inspector Keyboard Shortcuts:")
        print("   - F8: Resume execution")
        print("   - F10: Step over")
        print("   - F11: Step into")
        print("   - Shift+F11: Step out")

        print("\n=== Inspector Demo Complete ===")
        print("\nRemember:")
        print("  • Inspector is your best friend for debugging locators")
        print("  • Always test locators before committing code")
        print("  • Use it to learn what locators work best")
        print("  • Great for understanding page structure")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    inspector_demo()
