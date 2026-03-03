"""Exercise 2: Multi-Page Flow with Page Transitions

Your task:
1. Create a complete login flow with multiple page objects
2. Implement page transitions (methods returning different page objects)
3. Handle both success and failure scenarios

Pages to create:

1. BasePage
   - Common methods

2. LoginPage (https://the-internet.herokuapp.com/login)
   - navigate()
   - enter_username(username)
   - enter_password(password)
   - click_login()
   - login(username, password) -> returns SecurePage on success, self on failure
   - login_expecting_error(username, password) -> always returns self
   - get_error_message()
   - has_error()

3. SecurePage (after successful login)
   - get_heading()
   - get_welcome_message()
   - is_logged_in()
   - logout() -> returns LoginPage

Test scenarios:
1. Successful login flow (LoginPage -> SecurePage)
2. Logout flow (SecurePage -> LoginPage)
3. Failed login (stay on LoginPage)
4. Full user journey (login -> verify -> logout -> verify)
"""
from playwright.sync_api import sync_playwright


# TODO: Create BasePage
# class BasePage:
#     def __init__(self, page):
#         self.page = page
#
#     def get_url(self):
#         return self.page.url
#
#     def get_title(self):
#         return self.page.title()


# TODO: Create LoginPage with transitions
# class LoginPage(BasePage):
#     URL = "https://the-internet.herokuapp.com/login"
#
#     def __init__(self, page):
#         super().__init__(page)
#         # TODO: Define locators
#
#     def navigate(self):
#         # TODO
#         pass
#
#     def enter_username(self, username):
#         # TODO: Return self for chaining
#         pass
#
#     def enter_password(self, password):
#         # TODO: Return self for chaining
#         pass
#
#     def click_login(self):
#         # TODO: Return SecurePage if successful, self if not
#         pass
#
#     def login(self, username, password):
#         # TODO: Complete login, return appropriate page
#         pass
#
#     def login_expecting_error(self, username, password):
#         # TODO: Login expecting failure, return self
#         pass
#
#     def get_error_message(self):
#         # TODO
#         pass
#
#     def has_error(self):
#         # TODO
#         pass


# TODO: Create SecurePage with transition back
# class SecurePage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)
#         # TODO: Define locators
#
#     def get_heading(self):
#         # TODO
#         pass
#
#     def get_welcome_message(self):
#         # TODO
#         pass
#
#     def is_logged_in(self):
#         # TODO
#         pass
#
#     def logout(self):
#         # TODO: Return LoginPage
#         pass


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Exercise 2: Multi-Page Flow ===\n")

    # TODO: Test Scenario 1 - Successful Login
    # print("--- Scenario 1: Successful Login ---")
    # login_page = LoginPage(page)
    # login_page.navigate()
    # print(f"1. On LoginPage: {login_page.__class__.__name__}")
    #
    # secure_page = login_page.login("tomsmith", "SuperSecretPassword!")
    # print(f"2. After login: {secure_page.__class__.__name__}")
    # print(f"   Is logged in: {secure_page.is_logged_in()}")

    # TODO: Test Scenario 2 - Logout
    # print("\n--- Scenario 2: Logout ---")
    # login_page = secure_page.logout()
    # print(f"3. After logout: {login_page.__class__.__name__}")

    # TODO: Test Scenario 3 - Failed Login
    # print("\n--- Scenario 3: Failed Login ---")
    # login_page.navigate()
    # result = login_page.login("wrong", "wrong")
    # print(f"4. After bad login: {result.__class__.__name__}")
    # print(f"   Has error: {result.has_error()}")

    # TODO: Test Scenario 4 - Full Journey
    # print("\n--- Scenario 4: Full User Journey ---")
    # Steps: Navigate -> Try bad login -> Good login -> Use secure area -> Logout

    print("\nTODO: Implement the page classes and test scenarios")

    browser.close()
