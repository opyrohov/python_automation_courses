"""Exercise 1: Create Your First Page Object

Your task:
1. Create a page object class for the "Add/Remove Elements" page
   URL: https://the-internet.herokuapp.com/add_remove_elements/
2. Define locators for:
   - "Add Element" button
   - "Delete" buttons (there can be multiple)
3. Create methods:
   - navigate() - go to the page
   - click_add_element() - click add button
   - get_delete_button_count() - return number of delete buttons
   - click_delete_button(index) - click specific delete button
   - delete_all() - click all delete buttons
4. Test your page object with a simple test

Bonus:
- Add method chaining (return self)
- Add is_loaded() validation method
- Add click_add_multiple(count) method

Hints:
- Use page.locator() to define locators
- Use locator.count() to count elements
- Use locator.nth(index) to get specific element
"""
from playwright.sync_api import sync_playwright


# TODO: Create AddRemoveElementsPage class
# class AddRemoveElementsPage:
#     URL = "https://the-internet.herokuapp.com/add_remove_elements/"
#
#     def __init__(self, page):
#         self.page = page
#         # TODO: Define locators
#         # self.add_button = page.locator(...)
#         # self.delete_buttons = page.locator(...)
#
#     def navigate(self):
#         # TODO: Navigate to page
#         pass
#
#     def click_add_element(self):
#         # TODO: Click add button
#         pass
#
#     def get_delete_button_count(self):
#         # TODO: Return count of delete buttons
#         pass
#
#     def click_delete_button(self, index=0):
#         # TODO: Click delete button at index
#         pass
#
#     def delete_all(self):
#         # TODO: Delete all buttons
#         pass


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 1: Create Page Object ===\n")

    # TODO: Create page object instance
    # add_remove_page = AddRemoveElementsPage(page)

    # TODO: Test the page object
    # add_remove_page.navigate()
    # print(f"Initial delete buttons: {add_remove_page.get_delete_button_count()}")

    # add_remove_page.click_add_element()
    # add_remove_page.click_add_element()
    # add_remove_page.click_add_element()
    # print(f"After adding 3: {add_remove_page.get_delete_button_count()}")

    # add_remove_page.click_delete_button(0)
    # print(f"After deleting 1: {add_remove_page.get_delete_button_count()}")

    # add_remove_page.delete_all()
    # print(f"After delete all: {add_remove_page.get_delete_button_count()}")

    print("Exercise completed!")
    browser.close()
