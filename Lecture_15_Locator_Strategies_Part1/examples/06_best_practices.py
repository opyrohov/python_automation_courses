"""
Example 6: Locator Best Practices
Demonstrates good vs bad locator practices
"""

from playwright.sync_api import sync_playwright
import time

def demonstrate_best_practices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Navigate to a demo website
        page.goto("https://demo.playwright.dev/todomvc/")

        print("=== Locator Best Practices ===\n")

        # Add some test data
        page.locator(".new-todo").fill("Buy groceries")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").fill("Walk the dog")
        page.locator(".new-todo").press("Enter")
        page.locator(".new-todo").fill("Read a book")
        page.locator(".new-todo").press("Enter")
        time.sleep(1)

        print("BAD PRACTICES (What to AVOID):\n")

        # Bad Practice 1: Position-based selectors
        print("❌ 1. Position-Based Selectors")
        print("   Code: page.locator('li:nth-child(2)')")
        print("   Why bad: Breaks if order changes")
        print("   Example: Adding item at top breaks the test")

        # Bad Practice 2: Generated class names
        print("\n❌ 2. Generated/Dynamic Class Names")
        print("   Code: page.locator('.css-1dbjc4n-xyz')")
        print("   Why bad: Changes on every build")
        print("   Impact: All tests break after deployment")

        # Bad Practice 3: Overly specific selectors
        print("\n❌ 3. Overly Specific Selectors")
        print("   Code: page.locator('section > div > div > ul > li:nth-child(1) > div > label')")
        print("   Why bad: Too fragile, breaks with any structure change")
        print("   Impact: High maintenance cost")

        # Bad Practice 4: Using only generic classes
        print("\n❌ 4. Generic Classes")
        todo_label = page.locator("label").first
        print(f"   Code: page.locator('label')")
        print(f"   Why bad: Finds {page.locator('label').count()} elements!")
        print("   Impact: Ambiguous, may click wrong element")

        print("\n" + "="*60)
        print("\nGOOD PRACTICES (What to DO):\n")

        # Good Practice 1: User-facing attributes
        print("✅ 1. Use User-Facing Attributes")
        page.locator("[placeholder='What needs to be done?']").fill("Good practice example")
        page.locator("[placeholder='What needs to be done?']").press("Enter")
        time.sleep(0.5)
        print("   Code: page.get_by_placeholder('What needs to be done?')")
        print("   Why good: Matches how users interact")
        print("   Benefit: Resilient to implementation changes")

        # Good Practice 2: Semantic locators
        print("\n✅ 2. Use Semantic, Meaningful Selectors")
        print("   Code: page.locator('.new-todo')  # Semantic class")
        print("   Why good: Class name describes purpose")
        print("   Benefit: Self-documenting, likely to be stable")

        # Good Practice 3: Keep it simple
        print("\n✅ 3. Keep Selectors Simple")
        simple = page.locator(".new-todo")
        print("   Code: page.locator('.new-todo')")
        print(f"   vs: page.locator('section > div > input.new-todo')")
        print("   Why good: Easier to read and maintain")
        print("   Benefit: Less likely to break")

        # Good Practice 4: Combine when needed
        print("\n✅ 4. Combine Selectors for Specificity")
        page.locator("input.new-todo[placeholder='What needs to be done?']").fill("Specific selector")
        page.locator("input.new-todo[placeholder='What needs to be done?']").press("Enter")
        time.sleep(0.5)
        print("   Code: page.locator('input.new-todo')")
        print("   Why good: Specific enough without being brittle")
        print("   Benefit: Balance between precision and maintainability")

        # Good Practice 5: Use modern locators
        print("\n✅ 5. Prefer Modern Locators (When Possible)")
        page.get_by_placeholder("What needs to be done?").fill("Modern locator FTW!")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        time.sleep(0.5)
        print("   Code: page.get_by_placeholder('What needs to be done?')")
        print("   Why good: Playwright's recommended approach")
        print("   Benefit: Most resilient, best practices built-in")

        print("\n" + "="*60)
        print("\nDECISION TREE: Choosing the Right Locator\n")
        print("1. Can you use get_by_role()?")
        print("   → YES: Use it! (BEST option)")
        print("   → NO: Go to step 2")
        print("\n2. Is there a label or placeholder?")
        print("   → YES: Use get_by_label() or get_by_placeholder()")
        print("   → NO: Go to step 3")
        print("\n3. Can you use visible text?")
        print("   → YES: Use get_by_text()")
        print("   → NO: Go to step 4")
        print("\n4. Is there a test ID?")
        print("   → YES: Use get_by_test_id()")
        print("   → NO: Go to step 5")
        print("\n5. Is there a stable attribute (id, name, data-*)?")
        print("   → YES: Use CSS selector (#id, [name='...'])")
        print("   → NO: Go to step 6")
        print("\n6. Do you need parent navigation or complex text?")
        print("   → YES: Use XPath (sparingly!)")
        print("   → NO: Consider adding a test ID!")

        print("\n" + "="*60)
        print("\nKEY PRINCIPLES:")
        print("  1. User-facing > Implementation details")
        print("  2. Simple > Complex")
        print("  3. Stable > Dynamic")
        print("  4. Semantic > Generic")
        print("  5. Modern locators > CSS/XPath (when possible)")
        print("="*60)

        time.sleep(3)
        browser.close()

if __name__ == "__main__":
    demonstrate_best_practices()
