"""Example 5: Timeout Configuration"""
from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print("=== Timeout Configuration Demo ===\n")

    # Example 1: Default timeout (30 seconds)
    print("1. Default timeout is 30 seconds...")
    print("   (We won't wait that long in demo)")

    # Example 2: Set global timeout
    print("\n2. Setting global timeout to 60 seconds...")
    page.set_default_timeout(60000)  # 60 seconds
    print("   ✓ Global timeout set!")

    # Example 3: Per-action timeout
    print("\n3. Using per-action timeout...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Click with custom timeout
    page.locator("#start button").click(timeout=5000)
    print("   ✓ Clicked with 5-second timeout!")

    # Wait with custom timeout
    page.wait_for_selector("#finish", state="visible", timeout=10000)
    print("   ✓ Waited with 10-second timeout!")

    # Example 4: Navigation timeout
    print("\n4. Setting navigation timeout...")
    page.goto("https://playwright.dev/", timeout=30000)
    print("   ✓ Navigated with 30-second timeout!")

    # Example 5: Assertion timeout
    print("\n5. Using assertion timeout...")
    expect(page.locator("h1")).to_be_visible(timeout=10000)
    print("   ✓ Assertion with 10-second timeout!")

    # Example 6: Demonstrating timeout error
    print("\n6. Demonstrating timeout error (intentional)...")
    try:
        # Try to find non-existent element with short timeout
        page.wait_for_selector("#nonexistent", timeout=2000)
    except Exception as e:
        print(f"   ⚠️  Expected timeout error: {type(e).__name__}")

    # Example 7: Handling slow operations
    print("\n7. Handling slow operations...")
    page.goto("https://the-internet.herokuapp.com/slow")

    # Set longer timeout for slow page
    page.set_default_timeout(45000)  # 45 seconds
    print("   ✓ Increased timeout for slow operations!")

    # Example 8: wait_for_timeout (anti-pattern!)
    print("\n8. wait_for_timeout() - USE SPARINGLY!")
    print("   Waiting 2 seconds (fixed delay - not recommended)...")
    page.wait_for_timeout(2000)
    print("   ✓ Waited 2 seconds")
    print("   ⚠️  This is an ANTI-PATTERN! Use conditional waits instead!")

    # Example 9: Comparison
    print("\n9. Comparing approaches...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    print("\n   ❌ BAD: Fixed timeout")
    page.locator("#start button").click()
    page.wait_for_timeout(3000)  # Hope it's done in 3 seconds
    print("      Waited exactly 3 seconds (might be too long or too short)")

    page.reload()

    print("\n   ✅ GOOD: Conditional wait")
    start = time.time()
    page.locator("#start button").click()
    page.wait_for_selector("#finish", state="visible")
    elapsed = time.time() - start
    print(f"      Waited exactly as long as needed: {elapsed:.2f}s")

    # Example 10: Timeout best practices
    print("\n10. Timeout Best Practices:")
    print("   ✅ Use default timeout for most operations")
    print("   ✅ Increase timeout for legitimately slow operations")
    print("   ✅ Use per-action timeouts for specific slow elements")
    print("   ❌ Don't use very short timeouts (< 1 second)")
    print("   ❌ Don't use wait_for_timeout() unless absolutely necessary")

    print("\n✓ Timeout configuration examples complete!")

    input("\nPress Enter to close...")
    browser.close()
