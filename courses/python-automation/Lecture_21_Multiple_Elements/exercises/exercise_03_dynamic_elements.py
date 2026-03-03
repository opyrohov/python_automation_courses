"""Exercise 3: Dynamic Elements Operations"""
from playwright.sync_api import sync_playwright, expect

def dynamic_elements_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # TODO 1: Verify initial state - there should be 0 elements with class "added-manually"
        # Hint: expect(page.locator(".added-manually")).to_have_count(0)
        # expect(YOUR_CODE_HERE)

        # TODO 2: Add 5 elements by clicking the "Add Element" button 5 times
        # Hint: Use a for loop
        # for i in range(5):
        #     page.YOUR_CODE_HERE

        # TODO 3: Verify that 5 elements were added
        # Hint: expect(page.locator(".added-manually")).to_have_count(5)
        # expect(YOUR_CODE_HERE)

        # TODO 4: Get all added elements and verify each is visible
        # Hint: elements = page.locator(".added-manually").all()
        #       for element in elements:
        #           expect(element).to_be_visible()
        # elements = page.YOUR_CODE_HERE
        # for element in elements:
        #     expect(YOUR_CODE_HERE)

        # TODO 5: Remove the first and last elements
        # Hint: page.locator(".added-manually").first.click()
        #       page.locator(".added-manually").last.click()
        # page.YOUR_CODE_HERE  # Remove first
        # page.YOUR_CODE_HERE  # Remove last

        # TODO 6: Verify that 3 elements remain
        # Hint: expect(page.locator(".added-manually")).to_have_count(3)
        # expect(YOUR_CODE_HERE)

        # TODO 7: Remove all remaining elements using a loop
        # Hint: while page.locator(".added-manually").count() > 0:
        #           page.locator(".added-manually").first.click()
        # while YOUR_CONDITION_HERE:
        #     page.YOUR_CODE_HERE

        # TODO 8: Verify no elements remain
        # Hint: expect(page.locator(".added-manually")).to_have_count(0)
        # expect(YOUR_CODE_HERE)

        print("✓ Exercise 3 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    dynamic_elements_exercise()
