"""
Lecture 10 - Exercise 2: Building Reusable Page Objects
=======================================================
Practice creating a complete page object hierarchy.
"""

print("=" * 50)
print("EXERCISE: Building Page Objects")
print("=" * 50)
print()

# Exercise 2.1: Create BasePage
# =============================
# TODO: Create a comprehensive BasePage class with:
# - __init__(page)
# - navigate_to(url) method
# - click(selector) method
# - fill(selector, text) method
# - get_text(selector) method
# - is_visible(selector) method
# - wait_for_element(selector) method
# - take_screenshot(name) method

# Your code here:


print("-" * 50)


# Exercise 2.2: Create LoginPage from BasePage
# ============================================
# TODO: Create LoginPage that inherits from BasePage:
# - __init__(page)
# - Selectors: username_input, password_input, submit_button, error_message
# - login(username, password) method using parent methods
# - get_error_message() method
# - is_error_visible() method

# Your code here:


# Test (simulated):
# class FakePage:
#     pass
#
# login_page = LoginPage(FakePage())
# login_page.login("user@test.com", "password123")

print("-" * 50)


# Exercise 2.3: Create HomePage from BasePage
# ===========================================
# TODO: Create HomePage that inherits from BasePage:
# - __init__(page)
# - Selectors: welcome_message, user_menu, logout_button, search_box
# - get_welcome_text() method
# - search(query) method
# - logout() method
# - get_current_user() method (returns text from user_menu)

# Your code here:


print("-" * 50)


# Exercise 2.4: Create ProductPage from BasePage
# ==============================================
# TODO: Create ProductPage that inherits from BasePage:
# - __init__(page)
# - Selectors: product_title, price, add_to_cart_btn, quantity_input
# - get_product_name() method
# - get_product_price() method
# - set_quantity(qty) method
# - add_to_cart() method
# - is_in_stock() method (returns True if stock message visible)

# Your code here:


print("-" * 50)


# Exercise 2.5: Create Enhanced BasePage
# ======================================
# TODO: Create an EnhancedBasePage with additional methods:
# - __init__(page, url=None)
# - open() method (navigates to self.url)
# - refresh() method
# - go_back() method
# - get_current_url() method
# - get_page_title() method
# - wait_for_page_load() method
# - is_element_enabled(selector) method
# - get_element_count(selector) method

# Your code here:


print("-" * 50)


# Exercise 2.6: Create CheckoutPage from EnhancedBasePage
# =======================================================
# TODO: Create CheckoutPage using EnhancedBasePage:
# - __init__(page)
# - Set url to "https://example.com/checkout"
# - Selectors for: billing info, payment info, shipping info, submit button
# - fill_billing_info(billing_data) method
# - fill_payment_info(payment_data) method
# - fill_shipping_info(shipping_data) method
# - complete_checkout() method that:
#   1. Calls all fill methods
#   2. Clicks submit
#   3. Takes screenshot
#   4. Waits for page load

# Your code here:


# Test:
# checkout = CheckoutPage(FakePage())
# checkout.open()
# checkout.complete_checkout(billing_data, payment_data, shipping_data)

print("-" * 50)


# BONUS Exercise 2.7: Create AuthBasePage
# =======================================
# TODO: Create AuthBasePage (inherits from EnhancedBasePage)
# This is for pages that require authentication:
# - __init__(page, url=None)
# - verify_logged_in() method
# - get_logged_in_user() method
# - logout() method
#
# Then create DashboardPage (inherits from AuthBasePage):
# - __init__(page)
# - Selectors: stats_widget, notifications, user_profile
# - get_statistics() method
# - get_notifications_count() method
# - open_user_profile() method

# Your code here:


# Test:
# dashboard = DashboardPage(FakePage())
# dashboard.verify_logged_in()
# stats = dashboard.get_statistics()

print("-" * 50)


# BONUS Exercise 2.8: Complete Test Flow
# ======================================
# TODO: Create a complete test flow using all page objects:
#
# Create a test_complete_purchase_flow() function that:
# 1. Creates instances of LoginPage, HomePage, ProductPage, CheckoutPage
# 2. Logs in with test credentials
# 3. Searches for a product
# 4. Adds product to cart
# 5. Completes checkout
# 6. Verifies success
#
# Use print statements to simulate each step

# Your code here:


# def test_complete_purchase_flow():
#     """Test complete purchase flow."""
#     page = FakePage()
#
#     # Your implementation here
#     pass
#
# test_complete_purchase_flow()

print("-" * 50)

print("=" * 50)
print("Exercise 2 Complete!")
print("You've built a complete page object hierarchy!")
print("Check SOLUTIONS.md to verify your implementation")
print("=" * 50)
