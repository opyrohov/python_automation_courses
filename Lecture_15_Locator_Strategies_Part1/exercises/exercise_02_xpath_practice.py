"""
Exercise 2: XPath Practice
Practice using XPath selectors

Task: Complete the TODOs below using XPath selectors
"""

from playwright.sync_api import sync_playwright

def xpath_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # TODO 1: Select input using XPath by class attribute
        # Hint: //input[@class='new-todo']
        # TODO: Replace "YOUR_XPATH_HERE"
        page.locator("xpath=YOUR_XPATH_HERE").fill("XPath Task 1")
        page.locator("xpath=YOUR_XPATH_HERE").press("Enter")

        # TODO 2: Select input using XPath by placeholder attribute
        # Hint: Use @placeholder
        # TODO: Replace "YOUR_XPATH_HERE"
        page.locator("xpath=YOUR_XPATH_HERE").fill("XPath Task 2")
        page.locator("xpath=YOUR_XPATH_HERE").press("Enter")

        # TODO 3: Add a specific todo and find it by exact text
        page.locator(".new-todo").fill("Complete XPath Exercise")
        page.locator(".new-todo").press("Enter")

        # TODO: Find the todo with text "Complete XPath Exercise" using XPath
        # Hint: //label[text()='Complete XPath Exercise']
        # TODO: Uncomment and replace "YOUR_XPATH_HERE"
        # found_todo = page.locator("xpath=YOUR_XPATH_HERE")
        # if found_todo.count() > 0:
        #     print("✓ Found todo using XPath text matching!")

        # TODO 4: Find todos containing "XPath" using contains()
        # Hint: //label[contains(text(), 'XPath')]
        # TODO: Uncomment and replace "YOUR_XPATH_HERE"
        # xpath_todos = page.locator("xpath=YOUR_XPATH_HERE").count()
        # print(f"Todos containing 'XPath': {xpath_todos}")

        # TODO 5: Navigate to parent element
        # Find a label and navigate to its parent div
        # Hint: //label/parent::div
        # TODO: Uncomment and replace "YOUR_XPATH_HERE"
        # parents = page.locator("xpath=YOUR_XPATH_HERE").count()
        # print(f"Parent divs: {parents}")

        print("\n✅ Exercise 2 complete!")
        input("Press Enter to close browser...")

        browser.close()

if __name__ == "__main__":
    xpath_practice()
