"""Example 3: Load States"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print("=== Load States Demo ===\n")

    # Example 1: Default load state
    print("1. Waiting for 'load' state (default)...")
    start = time.time()
    page.goto("https://playwright.dev/")
    page.wait_for_load_state("load")
    elapsed = time.time() - start
    print(f"   ✓ Page loaded in {elapsed:.2f}s")

    # Example 2: domcontentloaded - faster
    print("\n2. Waiting for 'domcontentloaded' state (faster)...")
    start = time.time()
    page.goto("https://playwright.dev/")
    page.wait_for_load_state("domcontentloaded")
    elapsed = time.time() - start
    print(f"   ✓ DOM ready in {elapsed:.2f}s")

    # Example 3: networkidle - good for SPAs
    print("\n3. Waiting for 'networkidle' state (for SPAs)...")
    start = time.time()
    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle")
    elapsed = time.time() - start
    print(f"   ✓ Network idle in {elapsed:.2f}s")

    # Example 4: After navigation
    print("\n4. Using load state after clicking link...")
    page.goto("https://playwright.dev/")

    # Click a link and wait for new page to load
    page.locator("text=Docs").first.click()
    page.wait_for_load_state("networkidle")
    print("   ✓ New page loaded!")
    print(f"   Current URL: {page.url}")

    # Example 5: Comparing load states
    print("\n5. Comparing all three load states...")

    states = ["domcontentloaded", "load", "networkidle"]
    timings = {}

    for state in states:
        start = time.time()
        page.goto("https://playwright.dev/")
        page.wait_for_load_state(state)
        timings[state] = time.time() - start
        print(f"   {state:20s}: {timings[state]:.2f}s")

    print("\n   Analysis:")
    print(f"   - domcontentloaded is typically fastest (DOM ready)")
    print(f"   - load waits for resources (images, CSS)")
    print(f"   - networkidle waits for no network activity")

    print("\n✓ Load state examples complete!")

    input("\nPress Enter to close...")
    browser.close()
