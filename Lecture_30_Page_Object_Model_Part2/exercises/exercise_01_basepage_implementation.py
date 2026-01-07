"""Exercise 1: Implement BasePage with Common Methods

Your task:
1. Create a BasePage class with common functionality
2. Create two page classes that inherit from BasePage
3. Demonstrate code reuse through inheritance

Requirements for BasePage:
- __init__(self, page) - store the page object
- get_url() - return current URL
- get_title() - return page title
- wait_for_load() - wait for networkidle
- take_screenshot(name) - save screenshot to 'screenshots/name.png'
- scroll_to_top() - scroll to top of page
- scroll_to_bottom() - scroll to bottom of page

Create these pages inheriting from BasePage:
1. DynamicLoadingPage (https://the-internet.herokuapp.com/dynamic_loading/1)
   - start_button locator
   - loading indicator locator
   - result text locator
   - click_start() method
   - wait_for_result() method
   - get_result_text() method

2. InfiniteScrollPage (https://the-internet.herokuapp.com/infinite_scroll)
   - paragraphs locator
   - get_paragraph_count() method
   - scroll_and_load_more() method

Test both pages using inherited BasePage methods.
"""
from playwright.sync_api import sync_playwright
import os


# TODO: Create BasePage class
# class BasePage:
#     def __init__(self, page):
#         self.page = page
#
#     def get_url(self):
#         # TODO
#         pass
#
#     def get_title(self):
#         # TODO
#         pass
#
#     def wait_for_load(self):
#         # TODO
#         pass
#
#     def take_screenshot(self, name):
#         # TODO: Create screenshots folder if needed
#         pass
#
#     def scroll_to_top(self):
#         # TODO
#         pass
#
#     def scroll_to_bottom(self):
#         # TODO
#         pass


# TODO: Create DynamicLoadingPage
# class DynamicLoadingPage(BasePage):
#     URL = "https://the-internet.herokuapp.com/dynamic_loading/1"
#
#     def __init__(self, page):
#         super().__init__(page)
#         # TODO: Define locators
#
#     def navigate(self):
#         # TODO
#         pass
#
#     def click_start(self):
#         # TODO
#         pass
#
#     def wait_for_result(self):
#         # TODO: Wait for loading to finish
#         pass
#
#     def get_result_text(self):
#         # TODO
#         pass


# TODO: Create InfiniteScrollPage
# class InfiniteScrollPage(BasePage):
#     URL = "https://the-internet.herokuapp.com/infinite_scroll"
#
#     def __init__(self, page):
#         super().__init__(page)
#         # TODO: Define locators
#
#     def navigate(self):
#         # TODO
#         pass
#
#     def get_paragraph_count(self):
#         # TODO
#         pass
#
#     def scroll_and_load_more(self):
#         # TODO: Scroll and wait for new content
#         pass


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: BasePage Implementation ===\n")

    # TODO: Test DynamicLoadingPage
    # dynamic = DynamicLoadingPage(page)
    # dynamic.navigate()
    # print(f"1. Title (inherited): {dynamic.get_title()}")
    # print(f"2. URL (inherited): {dynamic.get_url()}")
    #
    # dynamic.click_start()
    # dynamic.wait_for_result()
    # print(f"3. Result: {dynamic.get_result_text()}")
    #
    # dynamic.take_screenshot("dynamic_result")
    # print("4. Screenshot taken (inherited)")

    # TODO: Test InfiniteScrollPage
    # infinite = InfiniteScrollPage(page)
    # infinite.navigate()
    # print(f"\n5. Title (inherited): {infinite.get_title()}")
    #
    # initial_count = infinite.get_paragraph_count()
    # print(f"6. Initial paragraphs: {initial_count}")
    #
    # infinite.scroll_and_load_more()
    # new_count = infinite.get_paragraph_count()
    # print(f"7. After scroll: {new_count}")

    print("\nTODO: Implement the page classes")

    browser.close()
