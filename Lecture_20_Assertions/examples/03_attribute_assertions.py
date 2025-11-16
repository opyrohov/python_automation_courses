"""Example 3: Attribute Assertions"""
from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Attribute Assertions Demo ===\n")

    # Example 1: to_have_attribute() - Check attribute value
    print("1. Testing to_have_attribute()...")
    page.goto("https://the-internet.herokuapp.com/")

    # Check first link's href attribute
    first_link = page.locator("ul li a").first
    expect(first_link).to_have_attribute("href", "/abtest")
    print("   ✓ First link has href='/abtest'")

    # Example 2: to_have_attribute() with regex
    print("\n2. Testing attribute with regex pattern...")
    page.goto("https://playwright.dev/")

    # Find an image and check src ends with specific extension
    img = page.locator("img").first
    expect(img).to_have_attribute("src", re.compile(r".*\.(png|jpg|svg)$"))
    print("   ✓ Image src has valid extension")

    # Example 3: to_have_class()
    print("\n3. Testing to_have_class()...")
    page.goto("https://the-internet.herokuapp.com/challenging_dom")

    # Check button classes
    button = page.locator(".button").first
    expect(button).to_have_class(re.compile(r".*button.*"))
    print("   ✓ Button has 'button' class")

    # Example 4: to_have_id()
    print("\n4. Testing to_have_id()...")
    page.goto("https://the-internet.herokuapp.com/login")

    # Check element ID
    expect(page.locator("input[type='text']")).to_have_id("username")
    print("   ✓ Input has id='username'")

    expect(page.locator("input[type='password']")).to_have_id("password")
    print("   ✓ Password input has id='password'")

    # Example 5: Multiple attributes
    print("\n5. Testing multiple attributes on same element...")
    page.goto("https://the-internet.herokuapp.com/login")

    username_input = page.locator("#username")
    expect(username_input).to_have_attribute("type", "text")
    expect(username_input).to_have_attribute("name", "username")
    expect(username_input).to_have_id("username")
    print("   ✓ Input has multiple correct attributes")

    # Example 6: Checking for attribute existence
    print("\n6. Testing attribute existence...")
    page.goto("https://the-internet.herokuapp.com/inputs")

    # Input should have type attribute
    input_field = page.locator("input[type='number']")
    expect(input_field).to_have_attribute("type", "number")
    print("   ✓ Input has type attribute")

    # Example 7: Negative attribute assertions
    print("\n7. Testing negative attribute assertions...")
    page.goto("https://the-internet.herokuapp.com/")

    # First link should NOT have target="_blank"
    first_link = page.locator("ul li a").first
    expect(first_link).not_to_have_attribute("target", "_blank")
    print("   ✓ Link does NOT have target='_blank'")

    # Example 8: Dynamic attribute changes
    print("\n8. Testing dynamic attribute changes...")
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    input_field = page.locator("input[type='text']")

    # Initially disabled
    expect(input_field).to_have_attribute("disabled", "")
    print("   ✓ Input has disabled attribute")

    # Enable it
    page.locator("button").filter(has_text="Enable").click()
    expect(page.locator("input[type='text']")).not_to_have_attribute("disabled")
    print("   ✓ Input no longer has disabled attribute")

    print("\n✓ All attribute assertion examples complete!")

    input("\nPress Enter to close...")
    browser.close()
