"""Exercise 1: List Operations"""
from playwright.sync_api import sync_playwright, expect

def list_operations_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # TODO 1: Get all links using all() and print the count
        # Hint: links = page.locator("ul li a").all()
        # links = page.YOUR_CODE_HERE
        # print(f"Total links: {len(links)}")

        # TODO 2: Get the count using count() method
        # Hint: count = page.locator("ul li a").count()
        # count = page.YOUR_CODE_HERE
        # print(f"Count: {count}")

        # TODO 3: Get the first link text
        # Hint: first_link = page.locator("ul li a").first
        # first_link = page.YOUR_CODE_HERE
        # print(f"First link: {first_link.text_content()}")

        # TODO 4: Get the text of all links (first 5) using list comprehension
        # Hint: texts = [link.text_content() for link in page.locator("ul li a").all()[:5]]
        # texts = YOUR_CODE_HERE
        # print(f"First 5 link texts: {texts}")

        # TODO 5: Find and click the "Checkboxes" link using iteration
        # Hint: Iterate through all links, find the one with text "Checkboxes", and click it
        # links = page.locator("ul li a").all()
        # for link in links:
        #     if YOUR_CONDITION_HERE:
        #         YOUR_CODE_HERE
        #         break

        # Verify you're on the checkboxes page
        # expect(page).to_have_url("**/checkboxes")

        print("✓ Exercise 1 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    list_operations_exercise()
