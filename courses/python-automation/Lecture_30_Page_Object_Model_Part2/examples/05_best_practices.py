"""Example 5: Page Object Model Best Practices

Demonstrates correct patterns (DO) and anti-patterns (DON'T)
for implementing Page Object Model.
"""
from playwright.sync_api import sync_playwright, expect


# ============================================
# BEST PRACTICE 1: Locators in __init__
# ============================================

# DON'T - Locators scattered in methods
class BadLoginPage_ScatteredLocators:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        # BAD: Locator defined here
        self.page.locator("#username").fill(username)

    def enter_password(self, password):
        # BAD: Same pattern repeated
        self.page.locator("#password").fill(password)


# DO - Locators centralized in __init__
class GoodLoginPage_CentralizedLocators:
    def __init__(self, page):
        self.page = page
        # GOOD: All locators in one place
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)


# ============================================
# BEST PRACTICE 2: No Assertions in Page Objects
# ============================================

# DON'T - Assertions inside page object
class BadLoginPage_WithAssertions:
    def __init__(self, page):
        self.page = page
        self.flash = page.locator("#flash")

    def login_and_verify(self, username, password):
        self.page.locator("#username").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("button").click()
        # BAD: Assertion in page object
        assert "success" in self.flash.text_content()


# DO - Return data, assert in test
class GoodLoginPage_NoAssertions:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    # GOOD: Provide data, don't assert
    def get_message(self):
        return self.flash.text_content()

    def has_success(self):
        return "success" in (self.flash.get_attribute("class") or "")


# Test does the assertion:
# page.login("user", "pass")
# assert page.has_success()  # Assertion HERE, not in page object


# ============================================
# BEST PRACTICE 3: Return self for Chaining
# ============================================

# DON'T - No return value
class BadPage_NoChaining:
    def __init__(self, page):
        self.page = page
        self.input = page.locator("#input")
        self.button = page.locator("#button")

    def fill_input(self, text):
        self.input.fill(text)
        # BAD: Nothing returned

    def click_button(self):
        self.button.click()
        # BAD: Nothing returned


# DO - Return self for fluent interface
class GoodPage_WithChaining:
    def __init__(self, page):
        self.page = page
        self.input = page.locator("#input")
        self.button = page.locator("#button")

    def fill_input(self, text):
        self.input.fill(text)
        return self  # GOOD: Return self

    def click_button(self):
        self.button.click()
        return self  # GOOD: Return self


# Enables: page.fill_input("text").click_button()


# ============================================
# BEST PRACTICE 4: Descriptive Method Names
# ============================================

# DON'T - Generic method names
class BadPage_GenericNames:
    def click1(self):
        pass

    def fill1(self, text):
        pass

    def check(self):
        pass


# DO - Descriptive, action-based names
class GoodPage_DescriptiveNames:
    def click_login_button(self):
        pass

    def fill_username(self, username):
        pass

    def check_remember_me(self):
        pass

    def is_logged_in(self):
        pass

    def get_error_message(self):
        pass


# ============================================
# BEST PRACTICE 5: Single Responsibility
# ============================================

# DON'T - Page object doing too much
class BadPage_TooMuchResponsibility:
    def login_and_navigate_to_settings_and_change_password(self):
        # BAD: Too many responsibilities
        pass


# DO - Single responsibility per method
class GoodPage_SingleResponsibility:
    def login(self, user, password):
        # Just login
        pass

    def navigate_to_settings(self):
        # Just navigate
        pass

    def change_password(self, old_pwd, new_pwd):
        # Just change password
        pass


# ============================================
# BEST PRACTICE 6: Use Semantic Locators
# ============================================

# DON'T - Brittle locators
class BadPage_BrittleLocators:
    def __init__(self, page):
        # BAD: Fragile selectors
        self.button = page.locator("body > div > div > button")
        self.input = page.locator("div:nth-child(3) > input")


# DO - Semantic, stable locators
class GoodPage_SemanticLocators:
    def __init__(self, page):
        # GOOD: Meaningful selectors
        self.login_button = page.locator("button[data-testid='login']")
        self.username = page.locator("#username")
        self.submit = page.get_by_role("button", name="Submit")


# ============================================
# DEMO
# ============================================

class LoginPageDemo:
    """Example of a well-designed page object."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        # Centralized locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")

    # Navigation
    def navigate(self):
        self.page.goto(self.URL)
        return self

    # Actions with chaining
    def enter_username(self, username):
        self.username_input.fill(username)
        return self

    def enter_password(self, password):
        self.password_input.fill(password)
        return self

    def click_login(self):
        self.login_button.click()
        return self

    # Convenience method
    def login(self, username, password):
        return (self
                .enter_username(username)
                .enter_password(password)
                .click_login())

    # Getters - no assertions
    def get_flash_message(self):
        return self.flash.text_content().strip()

    def has_error(self):
        return "error" in (self.flash.get_attribute("class") or "")

    def has_success(self):
        return "success" in (self.flash.get_attribute("class") or "")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=" * 60)
    print("BEST PRACTICES DEMO")
    print("=" * 60)

    login = LoginPageDemo(page)
    login.navigate()

    # Method chaining
    print("\n1. Method chaining:")
    login.enter_username("tomsmith").enter_password("SuperSecretPassword!")
    print("   login.enter_username('...').enter_password('...')")

    # Get data, assert in test
    login.click_login()
    print("\n2. Assertions in test (not page object):")
    print(f"   has_success(): {login.has_success()}")
    print(f"   Message: {login.get_flash_message()[:40]}...")

    # Assertions would be:
    # assert login.has_success()
    # assert "logged in" in login.get_flash_message()

    browser.close()

    print("\n" + "=" * 60)
    print("""
BEST PRACTICES SUMMARY:

1. LOCATORS IN __init__
   - All locators defined once
   - Easy to find and update

2. NO ASSERTIONS IN PAGE OBJECTS
   - Return data/state
   - Tests do assertions

3. RETURN SELF FOR CHAINING
   - Fluent interface
   - Readable test code

4. DESCRIPTIVE METHOD NAMES
   - click_login_button() not click1()
   - get_error_message() not get()

5. SINGLE RESPONSIBILITY
   - One action per method
   - Compose in tests

6. SEMANTIC LOCATORS
   - Use IDs, data-testid, roles
   - Avoid fragile CSS paths
""")
