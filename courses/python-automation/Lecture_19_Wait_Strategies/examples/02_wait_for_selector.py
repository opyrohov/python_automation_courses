"""Example 2: wait_for_selector() Examples"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== wait_for_selector() Demo ===\n")

    # Example 1: Wait for element to appear (visible state)
    print("1. Waiting for element to appear (state='visible')...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.locator("#start button").click()

    # Wait for finish message to be visible
    page.wait_for_selector("#finish", state="visible", timeout=10000)
    print("   ✓ Element appeared!")

    # Example 2: Wait for element to be hidden
    print("\n2. Waiting for loading indicator to hide (state='hidden')...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("#start button").click()

    # Wait for loading div to be hidden
    page.wait_for_selector("#loading", state="hidden")
    print("   ✓ Loading disappeared!")

    # Example 3: Wait for element to be attached (in DOM)
    print("\n3. Waiting for element in DOM (state='attached')...")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.locator("button").click()  # Add element

    # Wait for element to be attached to DOM
    page.wait_for_selector(".added-manually", state="attached")
    print("   ✓ Element attached to DOM!")

    # Example 4: Wait for element to be detached (removed)
    print("\n4. Waiting for element removal (state='detached')...")
    page.locator(".added-manually").click()  # Delete element

    # Wait for element to be removed from DOM
    page.wait_for_selector(".added-manually", state="detached", timeout=5000)
    print("   ✓ Element removed from DOM!")

    # Example 5: Custom timeout
    print("\n5. Using custom timeout...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.locator("#start button").click()

    try:
        # Very short timeout to demonstrate
        page.wait_for_selector("#finish", state="visible", timeout=100)
    except Exception as e:
        print(f"   ⚠️  Timeout as expected (100ms too short)")

    # Now with reasonable timeout
    page.wait_for_selector("#finish", state="visible", timeout=10000)
    print("   ✓ Success with proper timeout!")

    print("\n✓ All wait_for_selector() examples complete!")

    input("\nPress Enter to close...")
    browser.close()
