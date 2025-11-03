"""
Lecture 9 - Exercise 3: Page Objects
====================================
Practice creating Page Object Model classes for Playwright.
"""

print("=" * 50)
print("EXERCISE: Page Objects")
print("=" * 50)
print()

# Exercise 3.1: Simple LoginPage
# ==============================
# TODO: Create a 'LoginPage' class with:
# - __init__(page) - stores page
# - Selector attributes: username_input, password_input, submit_button
# - enter_username(username) method
# - enter_password(password) method
# - click_submit() method

# Your code here:


print("-" * 50)


# Exercise 3.2: LoginPage with login() Method
# ===========================================
# TODO: Extend LoginPage with:
# - login(username, password) method that calls:
#   1. enter_username()
#   2. enter_password()
#   3. click_submit()

# Your code here:


# Test (simulated):
# class FakePage:
#     pass
#
# login_page = LoginPage(FakePage())
# login_page.login("testuser", "password123")

print("-" * 50)


# Exercise 3.3: HomePage
# =====================
# TODO: Create a 'HomePage' class with:
# - __init__(page)
# - Selectors: welcome_message, logout_button, profile_link
# - get_welcome_text() method
# - logout() method
# - go_to_profile() method

# Your code here:


print("-" * 50)


# Exercise 3.4: ProductPage
# =========================
# TODO: Create a 'ProductPage' class with:
# - __init__(page)
# - Selectors: product_title, price, add_to_cart_button, quantity_input
# - get_product_name() method
# - get_price() method
# - set_quantity(qty) method
# - add_to_cart() method

# Your code here:


print("-" * 50)


# BONUS: BasePage
# ===============
# TODO: Create a 'BasePage' class with:
# - __init__(page)
# - navigate_to(url) method
# - get_title() method
# - take_screenshot(name) method

# Then make LoginPage inherit from BasePage

# Your code here:


print("-" * 50)

print("=" * 50)
print("Exercise 3 Complete!")
print("You've learned Page Object Model!")
print("=" * 50)
