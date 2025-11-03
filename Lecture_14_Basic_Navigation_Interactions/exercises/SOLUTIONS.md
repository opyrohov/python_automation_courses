# Exercise Solutions - Lecture 14

Complete solutions for all Lecture 14 exercises.

## Exercise 1: Navigation Solutions

### Exercise 1.1: Basic Navigation

```python
def exercise_1_basic_navigation():
    with sync_playwright() as p:
        # 1. Launch browser in headed mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 2. Navigate to example.com
        page.goto("https://example.com")

        # 3. Print page title
        print(f"Page 1 Title: {page.title()}")

        # 4. Navigate to playwright.dev
        page.goto("https://playwright.dev")

        # 5. Print page title
        print(f"Page 2 Title: {page.title()}")

        # 6. Go back
        page.go_back()

        # 7. Print current URL
        print(f"After go_back: {page.url}")

        # 8. Go forward
        page.go_forward()

        # 9. Print current URL
        print(f"After go_forward: {page.url}")

        # 10. Reload page
        page.reload()

        # 11. Print completion message
        print("Navigation complete!")

        # 12. Close browser
        browser.close()
```

### Exercise 1.2: Navigation with Wait

```python
def exercise_2_navigation_with_wait():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # 2. Navigate with networkidle wait
        response = page.goto("https://playwright.dev", wait_until="networkidle")

        # 3. Print status code
        print(f"Status code: {response.status}")

        # 4. Print whether response is OK
        print(f"OK: {response.ok}")

        # 5. Print page title
        print(f"Title: {page.title()}")

        # 6. Close browser
        browser.close()
```

### Exercise 1.3: Navigation History

```python
def exercise_3_navigation_history():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # 2. Visit URLs
        page.goto("https://example.com")
        print(f"Page 1: {page.title()}")

        page.goto("https://playwright.dev")
        print(f"Page 2: {page.title()}")

        page.goto("https://github.com")
        print(f"Page 3: {page.title()}")

        # 3. Go back twice
        page.go_back()
        page.go_back()

        # 4. Print current URL
        print(f"After 2x back: {page.url}")

        # 5. Go forward once
        page.go_forward()

        # 6. Print current URL
        print(f"After forward: {page.url}")

        # 7. Close browser
        browser.close()
```

### Exercise 1.4: Reload Page

```python
def exercise_4_reload_page():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # 2. Navigate
        page.goto("https://example.com")

        # 3. Get content length
        length_before = len(page.content())
        print(f"Content length before reload: {length_before}")

        # 4. Reload page
        page.reload()

        # 5. Get content length again
        length_after = len(page.content())
        print(f"Content length after reload: {length_after}")

        # 6. Compare
        print(f"Lengths match: {length_before == length_after}")

        # 7. Close browser
        browser.close()
```

### Exercise 1.5: Navigation with Error Handling

```python
def exercise_5_navigation_with_error_handling():
    with sync_playwright() as p:
        # 1. Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # 2. Navigate to valid URL
        try:
            page.goto("https://example.com")
            print("Success!")
        except Exception as e:
            print(f"Error: {e}")

        # 3. Navigate to invalid URL
        try:
            page.goto("https://invalid-url-12345.com", timeout=2000)
        except Exception as e:
            print(f"Error type: {type(e).__name__}")

        # 4. Close browser
        browser.close()
```

### Challenge: Navigation Tracker

```python
def challenge_navigation_tracker():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        urls = [
            "https://example.com",
            "https://playwright.dev",
            "https://python.org",
            "https://github.com",
            "https://npmjs.com"
        ]

        data = []

        for url in urls:
            try:
                response = page.goto(url)
                data.append({
                    'url': page.url,
                    'title': page.title(),
                    'status': response.status,
                    'content_length': len(page.content())
                })
            except Exception as e:
                print(f"Error with {url}: {e}")

        # Print summary table
        print("\n=== NAVIGATION SUMMARY ===\n")
        print(f"{'URL':<30} {'Title':<30} {'Status':<10} {'Size':<10}")
        print("-" * 80)
        for item in data:
            print(f"{item['url']:<30} {item['title'][:28]:<30} {item['status']:<10} {item['content_length']:<10}")

        browser.close()
```

---

## Exercise 2: Form Interaction Solutions

### Exercise 2.1: Simple Click

```python
def exercise_1_simple_click():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate
        page.goto("https://playwright.dev")

        # Click Get started
        page.click("text=Get started")

        # Print results
        print(f"New URL: {page.url}")
        print(f"Page Title: {page.title()}")

        browser.close()
```

### Exercise 2.2: Fill vs Type

```python
def exercise_2_fill_vs_type():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Create HTML page
        html = '<input id="input1" /><br><br><input id="input2" />'
        page.goto(f"data:text/html,{html}")

        # Use fill()
        page.fill("#input1", "Hello from fill()")

        # Use type()
        page.type("#input2", "Hello from type()", delay=50)

        # Take screenshot
        page.screenshot(path="fill_vs_type.png")
        print("Screenshot saved: fill_vs_type.png")

        browser.close()
```

### Exercise 2.3: Complete Form

```python
def exercise_3_complete_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Create form
        html = """
        <form>
            <input name="username" placeholder="Username" /><br><br>
            <input name="email" type="email" placeholder="Email" /><br><br>
            <input name="password" type="password" placeholder="Password" /><br><br>
            <input type="checkbox" id="terms" /> Accept Terms<br><br>
            <button type="submit">Submit</button>
        </form>
        """
        page.goto(f"data:text/html,{html}")

        # Fill form
        page.fill("input[name='username']", "john_doe")
        page.fill("input[name='email']", "john@example.com")
        page.fill("input[name='password']", "SecurePass123")
        page.check("#terms")

        # Submit
        page.click("button[type='submit']")

        print("Form submitted!")

        browser.close()
```

### Exercise 2.4: Click Options

```python
def exercise_4_click_options():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        html = """
        <button id="btn">Click Me</button>
        <p id="result"></p>
        <script>
            const btn = document.getElementById('btn');
            const result = document.getElementById('result');
            btn.addEventListener('click', () => result.textContent = 'Single click!');
            btn.addEventListener('dblclick', () => result.textContent = 'Double click!');
            btn.addEventListener('contextmenu', (e) => {
                e.preventDefault();
                result.textContent = 'Right click!';
            });
        </script>
        """
        page.goto(f"data:text/html,{html}")

        # Single click
        page.click("#btn")
        print(f"Single: {page.locator('#result').inner_text()}")

        # Double click
        page.click("#btn", click_count=2)
        print(f"Double: {page.locator('#result').inner_text()}")

        # Right click
        page.click("#btn", button="right")
        print(f"Right: {page.locator('#result').inner_text()}")

        browser.close()
```

### Exercise 2.5: Type with Delay

```python
def exercise_5_type_with_delay():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        # Create page
        html = '<input id="search" placeholder="Search..." style="padding: 10px; font-size: 18px;" />'
        page.goto(f"data:text/html,{html}")

        # Type with delay
        page.type("#search", "Playwright Automation", delay=100)
        print("Typing complete!")

        import time
        time.sleep(2)

        browser.close()
```

### Challenge: Interactive Form

```python
def challenge_interactive_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        html = """
        <html>
        <body style="padding: 30px;">
            <h2>Contact Form</h2>
            <form>
                <input name="name" placeholder="Name" required /><br><br>
                <input name="email" placeholder="Email" required /><br><br>
                <textarea name="message" rows="4" cols="30" placeholder="Message"></textarea><br><br>
                <input type="checkbox" id="subscribe" /> Subscribe<br><br>
                <button type="button" onclick="submit()">Submit</button>
            </form>
            <div id="result"></div>
            <script>
                function submit() {
                    const name = document.querySelector('[name="name"]').value;
                    const email = document.querySelector('[name="email"]').value;

                    if (!name) {
                        document.getElementById('result').innerHTML = '<p style="color: red;">Name required!</p>';
                        return;
                    }
                    if (!email.includes('@')) {
                        document.getElementById('result').innerHTML = '<p style="color: red;">Invalid email!</p>';
                        return;
                    }

                    document.getElementById('result').innerHTML = '<p style="color: green;">Success! Form submitted.</p>';
                }
            </script>
        </body>
        </html>
        """
        page.goto(f"data:text/html,{html}")

        # Fill form
        page.fill("input[name='name']", "John Doe")
        page.fill("input[name='email']", "john@example.com")
        page.fill("textarea[name='message']", "This is a test message")
        page.check("#subscribe")

        # Submit
        page.click("button")

        # Verify
        result = page.locator("#result").inner_text()
        print(result)

        import time
        time.sleep(2)

        browser.close()
```

---

## Exercise 3: Multiple Pages Solutions

### Exercise 3.1: Create Multiple Pages

```python
def exercise_1_create_multiple_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Create 3 pages
        page1 = context.new_page()
        page1.goto("https://example.com")
        print(f"Page 1: {page1.title()}")

        page2 = context.new_page()
        page2.goto("https://playwright.dev")
        print(f"Page 2: {page2.title()}")

        page3 = context.new_page()
        page3.goto("https://github.com")
        print(f"Page 3: {page3.title()}")

        # Print total
        print(f"\nTotal pages: {len(context.pages)}")

        browser.close()
```

### Exercise 3.2: Switch Between Pages

```python
def exercise_2_switch_between_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()

        # Create pages
        page1 = context.new_page()
        page1.goto("https://example.com")

        page2 = context.new_page()
        page2.goto("https://playwright.dev")

        page3 = context.new_page()
        page3.goto("https://github.com")

        # Switch between pages
        page1.bring_to_front()
        print(f"Switched to: {page1.url}")

        page2.bring_to_front()
        print(f"Switched to: {page2.url}")

        page3.bring_to_front()
        print(f"Switched to: {page3.url}")

        page1.bring_to_front()
        print(f"Switched to: {page1.url}")

        browser.close()
```

### Exercise 3.3: Close Specific Pages

```python
def exercise_3_close_specific_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Create 4 pages
        pages = []
        for i in range(4):
            page = context.new_page()
            page.goto("https://example.com")
            pages.append(page)

        print(f"Total pages: {len(context.pages)}")

        # Close 2nd page
        pages[1].close()
        print(f"After closing 2nd: {len(context.pages)}")

        # Close 4th page (now 3rd)
        pages[3].close()
        print(f"After closing 4th: {len(context.pages)}")

        # Print remaining URLs
        print("\nRemaining pages:")
        for page in context.pages:
            print(f"  {page.url}")

        browser.close()
```

### Exercise 3.4: Multiple Contexts

```python
def exercise_4_multiple_contexts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Context 1
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://example.com")
        page1.evaluate("localStorage.setItem('user', 'Alice')")
        value1 = page1.evaluate("localStorage.getItem('user')")
        print(f"Context 1: {value1}")

        # Context 2
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://example.com")
        value2 = page2.evaluate("localStorage.getItem('user')")
        print(f"Context 2: {value2}")

        print(f"Isolated: {value1 != value2}")

        browser.close()
```

### Exercise 3.5: Iterate Pages

```python
def exercise_5_iterate_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        urls = [
            "https://example.com",
            "https://playwright.dev",
            "https://github.com",
            "https://python.org",
            "https://npmjs.com"
        ]

        # Create pages
        for url in urls:
            page = context.new_page()
            page.goto(url)

        # Iterate and print
        for i, page in enumerate(context.pages, 1):
            print(f"Page {i}:")
            print(f"  URL: {page.url}")
            print(f"  Title: {page.title()}\n")

        browser.close()
```

---

## Exercise 4: Complete Workflow Solutions

### Exercise 4.1: Simple Login Workflow

```python
def exercise_1_simple_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        html = """
        <html>
        <body>
            <h2>Login</h2>
            <form>
                <input name="username" placeholder="Username" /><br><br>
                <input name="password" type="password" placeholder="Password" /><br><br>
                <button type="button" onclick="login()">Submit</button>
            </form>
            <div id="result"></div>
            <script>
                function login() {
                    const user = document.querySelector('[name="username"]').value;
                    const pass = document.querySelector('[name="password"]').value;
                    if (user && pass) {
                        document.getElementById('result').innerHTML = '<p style="color: green;">Success!</p>';
                    }
                }
            </script>
        </body>
        </html>
        """

        page.goto(f"data:text/html,{html}")

        page.fill("input[name='username']", "admin")
        page.fill("input[name='password']", "password123")
        page.click("button")

        result = page.locator("#result").inner_text()
        print(f"Result: {result}")

        browser.close()
```

### Exercise 4.2: Multi-Page Data Extraction

```python
def exercise_2_multi_page_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        urls = [
            "https://example.com",
            "https://playwright.dev",
            "https://python.org"
        ]

        data = []

        for url in urls:
            response = page.goto(url)
            data.append({
                'title': page.title(),
                'url': page.url,
                'status': response.status,
                'length': len(page.content())
            })

        print("\n=== DATA SUMMARY ===\n")
        print(f"{'Title':<30} {'Status':<10} {'Size':<10}")
        print("-" * 50)
        for item in data:
            print(f"{item['title'][:28]:<30} {item['status']:<10} {item['length']:<10}")

        browser.close()
```

---

## Running the Solutions

To run any solution:

```bash
# Save the solution to a file
python exercise_01_navigation.py

# Or run specific exercise
python -c "from exercise_01_navigation import exercise_1_basic_navigation; exercise_1_basic_navigation()"
```

## Tips for Completing Exercises

1. **Start Simple**: Begin with the basic exercises before attempting challenges
2. **Use Headed Mode**: Set `headless=False` to see what's happening
3. **Add slow_mo**: Use `slow_mo=500` to slow down actions for debugging
4. **Print Often**: Add print statements to track progress
5. **Handle Errors**: Use try/except for robust code
6. **Test Incrementally**: Test each step before moving to the next

## Common Mistakes to Avoid

1. ❌ Forgetting to close the browser
2. ❌ Not using context managers (`with` statement)
3. ❌ Using type() instead of fill() for simple forms
4. ❌ Not handling navigation errors
5. ❌ Creating too many contexts (resource intensive)

## Next Steps

After completing these exercises:
- ✅ You understand navigation methods
- ✅ You can interact with forms
- ✅ You can manage multiple pages
- ✅ You can build complete workflows

**Ready for Lecture 15: Locators & Element Selection!** 🚀
