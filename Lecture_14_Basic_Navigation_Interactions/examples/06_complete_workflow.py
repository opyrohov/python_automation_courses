"""
Example 6: Complete Workflow
Demonstrates a complete automation workflow combining all concepts
"""

from playwright.sync_api import sync_playwright
import time


def example_complete_login_workflow():
    """Complete login workflow with all best practices."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720}
        )
        page = context.new_page()

        print("=== Complete Login Workflow Example ===\n")

        try:
            # Step 1: Navigate
            print("Step 1: Navigating to login page...")
            response = page.goto("data:text/html," + """
            <html>
            <body style="padding: 50px; font-family: Arial;">
                <h2>Login Page</h2>
                <form id="login-form">
                    <input name="username" placeholder="Username" required /><br><br>
                    <input name="password" type="password" placeholder="Password" required /><br><br>
                    <button type="button" onclick="login()">Login</button>
                </form>
                <div id="message" style="margin-top: 20px;"></div>
                <script>
                    function login() {
                        const username = document.querySelector('[name="username"]').value;
                        const password = document.querySelector('[name="password"]').value;

                        if (username === 'admin' && password === 'password123') {
                            document.body.innerHTML = '<h1>Dashboard</h1><p>Welcome, ' + username + '!</p><a href="#" onclick="logout()">Logout</a>';
                        } else {
                            document.getElementById('message').innerHTML = '<span style="color: red;">Invalid credentials!</span>';
                        }
                    }
                    function logout() {
                        location.reload();
                    }
                </script>
            </body>
            </html>
            """)
            print(f"   Page loaded: {page.title()}")
            print(f"   Status: {response.status}\n")
            time.sleep(1)

            # Step 2: Fill form
            print("Step 2: Filling login form...")
            page.fill("input[name='username']", "admin")
            print("   ✓ Username entered")
            time.sleep(0.5)

            page.fill("input[name='password']", "password123")
            print("   ✓ Password entered\n")
            time.sleep(0.5)

            # Step 3: Submit
            print("Step 3: Submitting form...")
            page.click("button")
            time.sleep(1)

            # Step 4: Verify
            print("Step 4: Verifying login...")
            if "Dashboard" in page.content():
                print("   ✅ Login successful!")
                print(f"   Current page: {page.locator('h1').inner_text()}\n")
            else:
                print("   ❌ Login failed!\n")

            time.sleep(2)

            print("Workflow completed successfully!")

        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            browser.close()


def example_multi_page_data_collection():
    """Collect data from multiple pages."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        print("\n=== Multi-Page Data Collection Example ===\n")

        data_collected = []

        urls = [
            "https://example.com",
            "https://playwright.dev"
        ]

        for i, url in enumerate(urls, 1):
            print(f"Collecting data from page {i}...")

            try:
                response = page.goto(url)

                # Collect page data
                page_data = {
                    'url': page.url,
                    'title': page.title(),
                    'status': response.status,
                    'content_length': len(page.content())
                }

                data_collected.append(page_data)
                print(f"   ✓ Collected: {page_data['title']}\n")

                time.sleep(1)

            except Exception as e:
                print(f"   ✗ Error: {e}\n")

        # Display results
        print("=== DATA COLLECTION SUMMARY ===\n")
        for i, data in enumerate(data_collected, 1):
            print(f"Page {i}:")
            print(f"  Title: {data['title']}")
            print(f"  URL: {data['url']}")
            print(f"  Status: {data['status']}")
            print(f"  Size: {data['content_length']} chars\n")

        browser.close()


def example_e2e_shopping_flow():
    """End-to-end shopping workflow simulation."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("\n=== E-Commerce Shopping Flow Example ===\n")

        # Create shopping site
        html = """
        <html>
        <body style="padding: 30px; font-family: Arial;">
            <h1 id="page-title">Product Page</h1>
            <div id="content">
                <h3>Awesome Product</h3>
                <p>Price: $99.99</p>
                <button onclick="addToCart()">Add to Cart</button>
            </div>
            <div id="cart" style="margin-top: 30px; display:none;">
                <h2>Shopping Cart</h2>
                <p>Items: 1</p>
                <button onclick="checkout()">Checkout</button>
            </div>
            <div id="checkout" style="display:none;">
                <h2>Checkout</h2>
                <form>
                    <input name="name" placeholder="Full Name" /><br><br>
                    <input name="address" placeholder="Address" /><br><br>
                    <button type="button" onclick="placeOrder()">Place Order</button>
                </form>
            </div>
            <div id="confirmation" style="display:none; color: green;">
                <h2>Order Confirmed!</h2>
                <p>Thank you for your purchase!</p>
            </div>
            <script>
                function addToCart() {
                    document.getElementById('content').style.display = 'none';
                    document.getElementById('cart').style.display = 'block';
                    document.getElementById('page-title').textContent = 'Shopping Cart';
                }
                function checkout() {
                    document.getElementById('cart').style.display = 'none';
                    document.getElementById('checkout').style.display = 'block';
                    document.getElementById('page-title').textContent = 'Checkout';
                }
                function placeOrder() {
                    document.getElementById('checkout').style.display = 'none';
                    document.getElementById('confirmation').style.display = 'block';
                    document.getElementById('page-title').textContent = 'Order Confirmation';
                }
            </script>
        </body>
        </html>
        """

        page.goto(f"data:text/html,{html}")

        # Step 1: Product page
        print("Step 1: On product page")
        print(f"   Page: {page.locator('#page-title').inner_text()}")
        time.sleep(1)

        print("   Clicking 'Add to Cart'...")
        page.click("text=Add to Cart")
        time.sleep(1)

        # Step 2: Shopping cart
        print("\nStep 2: In shopping cart")
        print(f"   Page: {page.locator('#page-title').inner_text()}")
        time.sleep(1)

        print("   Clicking 'Checkout'...")
        page.click("text=Checkout")
        time.sleep(1)

        # Step 3: Checkout
        print("\nStep 3: At checkout")
        print(f"   Page: {page.locator('#page-title').inner_text()}")
        time.sleep(1)

        print("   Filling checkout form...")
        page.fill("input[name='name']", "John Doe")
        page.fill("input[name='address']", "123 Main Street")
        time.sleep(1)

        print("   Placing order...")
        page.click("text=Place Order")
        time.sleep(1)

        # Step 4: Confirmation
        print("\nStep 4: Order confirmation")
        print(f"   Page: {page.locator('#page-title').inner_text()}")
        confirmation_text = page.locator("#confirmation").inner_text()
        print(f"   {confirmation_text}")

        print("\n✅ E-commerce flow completed successfully!")

        time.sleep(2)

        browser.close()


def example_multi_tab_workflow():
    """Work with multiple tabs in a workflow."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()

        print("\n=== Multi-Tab Workflow Example ===\n")

        # Open multiple tabs
        print("Opening 3 tabs...")

        tab1 = context.new_page()
        tab1.goto("https://example.com")
        print(f"Tab 1: {tab1.title()}")

        tab2 = context.new_page()
        tab2.goto("https://playwright.dev")
        print(f"Tab 2: {tab2.title()}")

        tab3 = context.new_page()
        tab3.goto("https://github.com")
        print(f"Tab 3: {tab3.title()}\n")

        # Work with each tab
        print("Working with tabs...")

        print("  Switching to Tab 1...")
        tab1.bring_to_front()
        print(f"  Current: {tab1.url}")
        time.sleep(1)

        print("  Switching to Tab 2...")
        tab2.bring_to_front()
        print(f"  Current: {tab2.url}")
        time.sleep(1)

        print("  Switching to Tab 3...")
        tab3.bring_to_front()
        print(f"  Current: {tab3.url}")
        time.sleep(1)

        # Close tabs
        print("\nClosing tabs...")
        tab1.close()
        print(f"  Closed Tab 1. Remaining: {len(context.pages)}")
        time.sleep(0.5)

        tab2.close()
        print(f"  Closed Tab 2. Remaining: {len(context.pages)}")
        time.sleep(0.5)

        tab3.close()
        print(f"  Closed Tab 3. Remaining: {len(context.pages)}")

        print("\n✅ Multi-tab workflow completed!")

        browser.close()


def example_error_handling_workflow():
    """Complete workflow with comprehensive error handling."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("\n=== Error Handling Workflow Example ===\n")

        try:
            # Step 1: Navigation with error handling
            print("Step 1: Navigating...")
            try:
                response = page.goto("https://example.com", timeout=10000)
                print(f"   ✓ Navigation successful: {response.status}\n")
            except Exception as e:
                print(f"   ✗ Navigation failed: {e}\n")
                raise

            # Step 2: Interaction with error handling
            print("Step 2: Looking for element...")
            try:
                # Try to find element (will timeout on example.com)
                page.click("button.non-existent", timeout=2000)
                print("   ✓ Element found and clicked\n")
            except Exception as e:
                print(f"   ✗ Element not found (expected): {type(e).__name__}\n")

            # Step 3: Get page info
            print("Step 3: Getting page info...")
            print(f"   Title: {page.title()}")
            print(f"   URL: {page.url}")
            print(f"   Content: {len(page.content())} chars\n")

            print("✅ Workflow completed with error handling!")

        except Exception as e:
            print(f"\n❌ Workflow failed: {e}")
            # Take screenshot on error
            page.screenshot(path="error_screenshot.png")
            print("   Screenshot saved: error_screenshot.png")

        finally:
            print("\nCleaning up...")
            browser.close()
            print("   Browser closed")


if __name__ == "__main__":
    # Run all examples
    example_complete_login_workflow()
    example_multi_page_data_collection()
    example_e2e_shopping_flow()
    example_multi_tab_workflow()
    example_error_handling_workflow()

    print("\n✅ All complete workflow examples finished!")
