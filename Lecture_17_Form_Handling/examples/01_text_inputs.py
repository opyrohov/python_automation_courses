"""Example 1: Text Inputs - fill() vs type()"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/login")

    # fill() - Fast
    print("Using fill() - Fast")
    page.get_by_placeholder("Name").first.fill("John Doe")
    page.get_by_placeholder("Email Address").nth(1).fill("john@example.com")
    time.sleep(1)

    # type() - Slow (for demonstration)
    print("Using type() - Character by character")
    page.get_by_placeholder("Password").fill("")  # Clear first
    page.get_by_placeholder("Password").type("SecurePass123", delay=100)
    time.sleep(1)

    print("✓ Text input examples complete")
    browser.close()
