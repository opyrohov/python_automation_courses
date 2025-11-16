"""Exercise 4: Filtering and Searching Elements"""
from playwright.sync_api import sync_playwright

def filtering_search_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # TODO 1: Get all links and count them
        # Hint: all_links = page.locator("ul li a").all()
        # all_links = page.YOUR_CODE_HERE
        # print(f"Total links: {len(all_links)}")

        # TODO 2: Find all links containing the word "Dynamic" using filter()
        # Hint: dynamic_links = page.locator("ul li a").filter(has_text="Dynamic")
        # dynamic_links = page.YOUR_CODE_HERE
        # print(f"Links with 'Dynamic': {dynamic_links.count()}")

        # TODO 3: Extract text from all "Dynamic" links
        # Hint: texts = [link.text_content() for link in dynamic_links.all()]
        # texts = YOUR_CODE_HERE
        # print(f"Dynamic link texts: {texts}")

        # TODO 4: Find links that start with letter "A" using iteration
        # Hint: a_links = [link for link in all_links if link.text_content().startswith('A')]
        # a_links = YOUR_CODE_HERE
        # print(f"Links starting with 'A': {len(a_links)}")
        # for link in a_links:
        #     print(f"  - {link.text_content()}")

        # TODO 5: Find and click the link with exact text "Form Authentication"
        # Hint: Iterate through all links, find the one with matching text, and click it
        # for link in all_links:
        #     if YOUR_CONDITION_HERE:
        #         YOUR_CODE_HERE
        #         break

        # TODO 6: Verify you're on the form authentication page
        # Hint: Check that URL contains "/login"
        # print(f"Current URL: {page.url}")
        # assert "/login" in page.url

        print("✓ Exercise 4 complete!")
        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    filtering_search_exercise()
