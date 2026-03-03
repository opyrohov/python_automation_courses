"""
Exercise 1: CSS Selector Challenge
Practice using different CSS selector strategies

Task: Complete the TODOs below by filling in the correct CSS selectors
"""

from playwright.sync_api import sync_playwright

def css_selector_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # TODO 1: Select the input field using its class
        # Hint: The class is "new-todo"
        # TODO: Replace "YOUR_SELECTOR_HERE" with the correct CSS selector
        page.locator("YOUR_SELECTOR_HERE").fill("Task 1: CSS Class")
        page.locator("YOUR_SELECTOR_HERE").press("Enter")

        # TODO 2: Select the input field using its placeholder attribute
        # Hint: placeholder="What needs to be done?"
        # TODO: Replace "YOUR_SELECTOR_HERE" with the correct attribute selector
        page.locator("YOUR_SELECTOR_HERE").fill("Task 2: Attribute Selector")
        page.locator("YOUR_SELECTOR_HERE").press("Enter")

        # TODO 3: Select the input field using tag + class
        # Hint: It's an <input> with class "new-todo"
        # TODO: Replace "YOUR_SELECTOR_HERE" with the combined selector
        page.locator("YOUR_SELECTOR_HERE").fill("Task 3: Combined Selector")
        page.locator("YOUR_SELECTOR_HERE").press("Enter")

        # TODO 4: Count how many <li> elements are on the page
        # TODO: Replace "YOUR_SELECTOR_HERE" and uncomment the line
        # todo_count = page.locator("YOUR_SELECTOR_HERE").count()
        # print(f"Total todos: {todo_count}")

        # TODO 5: Select the first <li> element using CSS pseudo-class
        # Hint: Use :first-child
        # TODO: Uncomment and replace "YOUR_SELECTOR_HERE"
        # first_todo_text = page.locator("YOUR_SELECTOR_HERE").text_content()
        # print(f"First todo: {first_todo_text}")

        print("\n✅ Exercise 1 complete! Check the browser to verify.")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    css_selector_challenge()
