"""
Example 4: Form Interactions
Demonstrates click(), fill(), and type() methods
"""

from playwright.sync_api import sync_playwright
import time


def example_click_methods():
    """Demonstrate different click methods."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("=== Click Methods Example ===\n")

        page.goto("https://playwright.dev")

        # Click by text
        print("1. Clicking 'Get started' link...")
        page.click("text=Get started")
        print(f"   Navigated to: {page.url}\n")
        time.sleep(1)

        # Go back
        page.go_back()
        time.sleep(1)

        # Click with has-text
        print("2. Clicking with :has-text()...")
        page.click("a:has-text('Get started')")
        print(f"   Navigated to: {page.url}\n")

        time.sleep(2)

        browser.close()


def example_fill_vs_type():
    """Compare fill() and type() methods."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        print("\n=== fill() vs type() Example ===\n")

        # Create a simple test page
        page.goto("data:text/html,<html><body><h1>Form Test</h1><input id='input1' placeholder='Use fill()' /><br><br><input id='input2' placeholder='Use type()' /></body></html>")

        # Example 1: fill() - Fast, no keyboard events
        print("1. Using fill() - Fast, instant:")
        start_time = time.time()
        page.fill("#input1", "Hello from fill()")
        fill_time = time.time() - start_time
        print(f"   Time: {fill_time:.3f} seconds\n")
        time.sleep(1)

        # Example 2: type() - Slower, triggers events
        print("2. Using type() - Slower, realistic:")
        start_time = time.time()
        page.type("#input2", "Hello from type()", delay=50)
        type_time = time.time() - start_time
        print(f"   Time: {type_time:.3f} seconds\n")

        print(f"fill() was {type_time/fill_time:.1f}x faster!")

        time.sleep(2)

        browser.close()


def example_fill_form():
    """Fill a complete form using fill()."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== Fill Form Example ===\n")

        # Create test form
        html = """
        <html>
        <body>
            <h1>Registration Form</h1>
            <form>
                <input name="username" placeholder="Username" /><br><br>
                <input name="email" type="email" placeholder="Email" /><br><br>
                <input name="password" type="password" placeholder="Password" /><br><br>
                <input type="checkbox" id="terms" /> Accept Terms<br><br>
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
        """
        page.goto(f"data:text/html,{html}")

        # Fill form fields
        print("Filling form...")
        page.fill("input[name='username']", "john_doe")
        print("  ✓ Username filled")

        page.fill("input[name='email']", "john@example.com")
        print("  ✓ Email filled")

        page.fill("input[name='password']", "SecurePass123")
        print("  ✓ Password filled")

        page.check("#terms")
        print("  ✓ Terms checkbox checked")

        print("\nForm ready to submit!")

        time.sleep(3)

        browser.close()


def example_type_with_autocomplete():
    """Use type() for search/autocomplete scenarios."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        print("\n=== type() for Autocomplete Example ===\n")

        # Go to a real search page
        page.goto("https://playwright.dev")

        # Type in search box (if available)
        print("Typing in search...")
        try:
            # Type slowly to trigger autocomplete
            page.type("input[type='search']", "API", delay=100)
            print("  ✓ Typed 'API' with delay")
            time.sleep(2)

            # Clear and type again
            page.fill("input[type='search']", "")
            page.type("input[type='search']", "Python", delay=100)
            print("  ✓ Typed 'Python' with delay")
        except:
            print("  (Search not available on this page)")

        time.sleep(2)

        browser.close()


def example_click_options():
    """Demonstrate click with different options."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== Click Options Example ===\n")

        # Create test page with button
        html = """
        <html>
        <body style="padding: 50px;">
            <h1>Click Tests</h1>
            <button id="btn" style="padding: 20px; font-size: 18px;">Click Me</button>
            <p id="result"></p>
            <script>
                const btn = document.getElementById('btn');
                const result = document.getElementById('result');

                btn.addEventListener('click', () => {
                    result.textContent = 'Single clicked!';
                });

                btn.addEventListener('dblclick', () => {
                    result.textContent = 'Double clicked!';
                });

                btn.addEventListener('contextmenu', (e) => {
                    e.preventDefault();
                    result.textContent = 'Right clicked!';
                });
            </script>
        </body>
        </html>
        """
        page.goto(f"data:text/html,{html}")

        # Single click
        print("1. Single click:")
        page.click("#btn")
        print(f"   Result: {page.locator('#result').inner_text()}\n")
        time.sleep(1)

        # Double click
        print("2. Double click:")
        page.click("#btn", click_count=2)
        print(f"   Result: {page.locator('#result').inner_text()}\n")
        time.sleep(1)

        # Right click
        print("3. Right click:")
        page.click("#btn", button="right")
        print(f"   Result: {page.locator('#result').inner_text()}\n")

        time.sleep(2)

        browser.close()


def example_interactive_form():
    """Complete interactive form filling example."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== Interactive Form Example ===\n")

        # Create comprehensive form
        html = """
        <html>
        <body style="padding: 30px; font-family: Arial;">
            <h2>Contact Form</h2>
            <form id="contact-form">
                <label>Name:</label><br>
                <input name="name" required /><br><br>

                <label>Email:</label><br>
                <input name="email" type="email" required /><br><br>

                <label>Message:</label><br>
                <textarea name="message" rows="4" cols="50"></textarea><br><br>

                <input type="checkbox" id="subscribe" />
                <label for="subscribe">Subscribe to newsletter</label><br><br>

                <button type="button" onclick="submitForm()">Submit</button>
            </form>
            <div id="result" style="margin-top: 20px; color: green;"></div>

            <script>
                function submitForm() {
                    const name = document.querySelector('[name="name"]').value;
                    const email = document.querySelector('[name="email"]').value;
                    const message = document.querySelector('[name="message"]').value;
                    const subscribe = document.querySelector('#subscribe').checked;

                    document.getElementById('result').innerHTML =
                        `<strong>Form Submitted!</strong><br>
                         Name: ${name}<br>
                         Email: ${email}<br>
                         Message: ${message}<br>
                         Subscribed: ${subscribe}`;
                }
            </script>
        </body>
        </html>
        """
        page.goto(f"data:text/html,{html}")

        print("Step 1: Filling name...")
        page.fill("input[name='name']", "John Doe")
        time.sleep(0.5)

        print("Step 2: Filling email...")
        page.fill("input[name='email']", "john@example.com")
        time.sleep(0.5)

        print("Step 3: Typing message...")
        page.type("textarea[name='message']", "Hello! This is a test message.", delay=30)
        time.sleep(0.5)

        print("Step 4: Checking subscription...")
        page.check("#subscribe")
        time.sleep(0.5)

        print("Step 5: Submitting form...")
        page.click("button")
        time.sleep(1)

        # Verify submission
        result = page.locator("#result").inner_text()
        print(f"\n{result}\n")

        print("✅ Form submitted successfully!")

        time.sleep(3)

        browser.close()


if __name__ == "__main__":
    # Run all examples
    example_click_methods()
    example_fill_vs_type()
    example_fill_form()
    example_type_with_autocomplete()
    example_click_options()
    example_interactive_form()

    print("\n✅ All form interaction examples completed!")
