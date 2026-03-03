"""Exercise 2: Count and URL Assertions"""
from playwright.sync_api import sync_playwright, expect

def count_url_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        # TODO 1: Assert that the URL matches the pattern "**/add_remove_elements/"
        # Hint: expect(page).to_have_url("**/add_remove_elements/")
        # expect(YOUR_CODE_HERE)

        # TODO 2: Assert that initially there are 0 elements with class "added-manually"
        # Hint: expect(page.locator(".added-manually")).to_have_count(0)
        # expect(YOUR_CODE_HERE)

        # Add 3 elements
        for i in range(3):
            page.locator("button").first.click()

        # TODO 3: Assert that there are now 3 elements
        # Hint: expect(page.locator(".added-manually")).to_have_count(3)
        # expect(YOUR_CODE_HERE)

        # TODO 4: Assert that each added element is visible
        # Hint: Use a loop and expect(page.locator(".added-manually").nth(i)).to_be_visible()
        # for i in range(3):
        #     expect(YOUR_CODE_HERE)

        # Remove one element
        page.locator(".added-manually").first.click()

        # TODO 5: Assert that there are now 2 elements
        # Hint: expect(page.locator(".added-manually")).to_have_count(2)
        # expect(YOUR_CODE_HERE)

        print("✓ Exercise 2 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    count_url_exercise()
