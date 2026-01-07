"""Exercise 2: Refactor Test to Use Page Object Model

Your task:
1. Look at the test below - it's written WITHOUT page objects
2. Create a CheckboxPage class with proper locators and methods
3. Refactor the test to use your page object
4. The test should do the same thing but be much cleaner

Current test (without POM) - refactor this:
"""
from playwright.sync_api import sync_playwright, expect


# ============================================
# ORIGINAL TEST (WITHOUT POM) - REFACTOR THIS
# ============================================
def test_without_pom():
    """This test needs to be refactored to use POM."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("=== Original Test (Without POM) ===\n")

        # Navigate
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        print("1. Navigated to checkboxes page")

        # Get checkboxes
        checkbox1 = page.locator("input[type='checkbox']").nth(0)
        checkbox2 = page.locator("input[type='checkbox']").nth(1)

        # Check initial state
        is_checked1 = checkbox1.is_checked()
        is_checked2 = checkbox2.is_checked()
        print(f"2. Initial state: CB1={is_checked1}, CB2={is_checked2}")

        # Toggle checkbox 1 (check it)
        if not checkbox1.is_checked():
            checkbox1.check()
        print("3. Checked checkbox 1")

        # Toggle checkbox 2 (uncheck it)
        if checkbox2.is_checked():
            checkbox2.uncheck()
        print("4. Unchecked checkbox 2")

        # Verify
        assert checkbox1.is_checked()
        assert not checkbox2.is_checked()
        print("5. Verified checkbox states")

        # Toggle both
        checkbox1.click()
        checkbox2.click()
        print("6. Toggled both checkboxes")

        # Final state
        final1 = checkbox1.is_checked()
        final2 = checkbox2.is_checked()
        print(f"7. Final state: CB1={final1}, CB2={final2}")

        browser.close()
        print("\n✓ Test completed")


# ============================================
# TODO: CREATE PAGE OBJECT
# ============================================
# class CheckboxPage:
#     URL = "https://the-internet.herokuapp.com/checkboxes"
#
#     def __init__(self, page):
#         self.page = page
#         # TODO: Define locators for checkboxes
#
#     def navigate(self):
#         # TODO
#         pass
#
#     def is_checkbox_checked(self, index):
#         # TODO: Return True/False for checkbox at index
#         pass
#
#     def check_checkbox(self, index):
#         # TODO: Check the checkbox at index
#         pass
#
#     def uncheck_checkbox(self, index):
#         # TODO: Uncheck the checkbox at index
#         pass
#
#     def toggle_checkbox(self, index):
#         # TODO: Toggle checkbox at index
#         pass
#
#     def get_checkbox_count(self):
#         # TODO: Return total number of checkboxes
#         pass


# ============================================
# TODO: REFACTORED TEST (WITH POM)
# ============================================
def test_with_pom():
    """Refactored test using Page Object Model."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("=== Refactored Test (With POM) ===\n")

        # TODO: Use CheckboxPage instead of raw locators
        # checkbox_page = CheckboxPage(page)
        # checkbox_page.navigate()
        # ...

        print("TODO: Implement refactored test")

        browser.close()


# Run the original test
if __name__ == "__main__":
    print("Running original test (without POM)...")
    test_without_pom()

    print("\n" + "=" * 50)
    print("Now refactor to use Page Object Model!")
    print("=" * 50)
