# Exercise Solutions - Lecture 15: Locator Strategies

## Exercise 1: CSS Selector Challenge

### Solution Code

```python
from playwright.sync_api import sync_playwright

def css_selector_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # TODO 1: Select using class
        page.locator(".new-todo").fill("Task 1: CSS Class")
        page.locator(".new-todo").press("Enter")

        # TODO 2: Select using placeholder attribute
        page.locator("[placeholder='What needs to be done?']").fill("Task 2: Attribute Selector")
        page.locator("[placeholder='What needs to be done?']").press("Enter")

        # TODO 3: Select using tag + class
        page.locator("input.new-todo").fill("Task 3: Combined Selector")
        page.locator("input.new-todo").press("Enter")

        # TODO 4: Count <li> elements
        todo_count = page.locator("li").count()
        print(f"Total todos: {todo_count}")

        # TODO 5: Select first <li> using pseudo-class
        first_todo_text = page.locator("li:first-child").text_content()
        print(f"First todo: {first_todo_text}")

        print("\n✅ Exercise 1 complete!")
        input("Press Enter to close browser...")
        browser.close()
```

### Explanations

1. **`.new-todo`** - Class selector with dot prefix
2. **`[placeholder='What needs to be done?']`** - Attribute selector with exact match
3. **`input.new-todo`** - Combined tag and class selector
4. **`li`** - Simple tag selector to match all list items
5. **`li:first-child`** - Pseudo-class to select first child

---

## Exercise 2: XPath Practice

### Solution Code

```python
from playwright.sync_api import sync_playwright

def xpath_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # TODO 1: XPath by class
        page.locator("xpath=//input[@class='new-todo']").fill("XPath Task 1")
        page.locator("xpath=//input[@class='new-todo']").press("Enter")

        # TODO 2: XPath by placeholder
        page.locator("xpath=//input[@placeholder='What needs to be done?']").fill("XPath Task 2")
        page.locator("xpath=//input[@placeholder='What needs to be done?']").press("Enter")

        # TODO 3: XPath exact text match
        page.locator(".new-todo").fill("Complete XPath Exercise")
        page.locator(".new-todo").press("Enter")

        found_todo = page.locator("xpath=//label[text()='Complete XPath Exercise']")
        if found_todo.count() > 0:
            print("✓ Found todo using XPath text matching!")

        # TODO 4: XPath contains
        xpath_todos = page.locator("xpath=//label[contains(text(), 'XPath')]").count()
        print(f"Todos containing 'XPath': {xpath_todos}")

        # TODO 5: Parent navigation
        parents = page.locator("xpath=//label/parent::div").count()
        print(f"Parent divs: {parents}")

        print("\n✅ Exercise 2 complete!")
        input("Press Enter to close browser...")
        browser.close()
```

### Explanations

1. **`xpath=//input[@class='new-todo']`** - Select input by class attribute
2. **`xpath=//input[@placeholder='...']`** - Select by placeholder attribute
3. **`xpath=//label[text()='Complete XPath Exercise']`** - Exact text match
4. **`xpath=//label[contains(text(), 'XPath')]`** - Substring text match
5. **`xpath=//label/parent::div`** - Navigate to parent element

---

## Exercise 3: Modern Locators Practice

### Solution Code

```python
from playwright.sync_api import sync_playwright, expect

def modern_locators_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://playwright.dev/")

        # TODO 1: get_by_role() for link
        page.get_by_role("link", name="Docs").click()
        print("✓ Clicked Docs link")

        # TODO 2: get_by_role() for navigation
        nav = page.get_by_role("navigation")
        print(f"✓ Found {nav.count()} navigation element(s)")

        # TODO 3: get_by_text() with partial match
        elements = page.get_by_text("Playwright", exact=False).count()
        print(f"✓ Found {elements} element(s) containing 'Playwright'")

        # Navigate to form page
        page.goto("https://www.automationexercise.com/login")

        # TODO 4: get_by_placeholder() for email
        page.get_by_placeholder("Email Address").first.fill("test@example.com")
        print("✓ Filled email using placeholder")

        # TODO 5: get_by_placeholder() for name
        page.get_by_placeholder("Name").first.fill("John Doe")
        print("✓ Filled name field")

        # TODO 6: Chaining locators
        button = page.locator("form").get_by_role("button").first
        print(f"✓ Found button inside form")

        print("\n✅ Exercise 3 complete!")
        input("Press Enter to close browser...")
        browser.close()
```

### Explanations

1. **`get_by_role("link", name="Docs")`** - Find link by ARIA role and accessible name
2. **`get_by_role("navigation")`** - Find navigation landmark
3. **`get_by_text("Playwright", exact=False)`** - Partial text match
4. **`get_by_placeholder("Email Address")`** - Find input by placeholder
5. **`get_by_placeholder("Name")`** - Find input by placeholder
6. **`locator("form").get_by_role("button")`** - Chain CSS with modern locator

---

## Exercise 4: Locator Refactoring Challenge

### Solutions

#### 1. Refactor Absolute XPath

**Bad:**
```python
page.locator("xpath=/html/body/section/div/header/input").fill("Task 1")
```

**Good Options:**
```python
# Option 1: Modern locator (BEST)
page.get_by_placeholder("What needs to be done?").fill("Task 1")

# Option 2: CSS class
page.locator(".new-todo").fill("Task 1")

# Option 3: CSS attribute
page.locator("[placeholder='What needs to be done?']").fill("Task 1")
```

**Why:** Absolute XPath breaks with any DOM structure change. Modern locators and stable attributes are resilient.

---

#### 2. Refactor Position-Based Selector

**Bad:**
```python
first_todo = page.locator("li:nth-child(1)").text_content()
```

**Good:**
```python
# Find by text content
first_todo = page.get_by_text("First item").text_content()

# Or if you genuinely need the first item regardless of content:
first_todo = page.locator(".todo-list li").first.text_content()
```

**Why:** Position-based selectors break when order changes. Finding by text is more meaningful and stable.

---

#### 3. Refactor Overly Specific Selector

**Bad:**
```python
label = page.locator("section.todoapp > div.main > ul.todo-list > li > div > label").first
```

**Good:**
```python
# Much simpler!
label = page.locator(".todo-list label").first

# Or even better with modern locator:
label = page.get_by_text("First item")  # If you know the text
```

**Why:** Long selector chains are brittle and hard to read. Keep it simple - select the element directly with minimal context.

---

#### 4. Refactor Generic Selector

**Bad:**
```python
page.locator("input")  # Matches ALL inputs!
```

**Good:**
```python
# Option 1: Use class
page.locator("input.new-todo")

# Option 2: Use placeholder (modern)
page.get_by_placeholder("What needs to be done?")

# Option 3: Use attribute
page.locator("[placeholder='What needs to be done?']")
```

**Why:** Generic selectors are ambiguous and may match the wrong element. Be specific!

---

#### 5. Refactor Generated Classes

**Bad (Hypothetical):**
```python
page.locator(".css-xyz123-generated").fill("text")
```

**Good:**
```python
# Use semantic attribute
page.get_by_placeholder("What needs to be done?").fill("text")

# Or add a test ID
page.get_by_test_id("todo-input").fill("text")

# Or use name attribute
page.locator("[name='todo']").fill("text")
```

**Why:** Generated class names change on every build. Use stable, semantic attributes instead.

---

## Key Takeaways

### Locator Priority (Best to Worst)

1. ✅ **Modern Locators** (`get_by_role`, `get_by_label`, `get_by_placeholder`, `get_by_text`)
   - Most resilient
   - User-facing
   - Best practices

2. ✅ **CSS with Semantic Attributes** (`#id`, `[name='...']`, `.semantic-class`)
   - Fast
   - Stable
   - Readable

3. ⚠️ **XPath** (use sparingly)
   - Only when CSS can't express the relationship
   - Parent navigation
   - Complex text matching

### What to Avoid

- ❌ Absolute paths
- ❌ Position-based selectors
- ❌ Generated class names
- ❌ Overly specific chains
- ❌ Generic selectors

### Best Practices

- ✅ Prefer user-facing attributes
- ✅ Keep selectors simple
- ✅ Use semantic, meaningful names
- ✅ Add test IDs when needed
- ✅ Think about maintainability

---

## Additional Practice

Try these challenges to further improve your skills:

1. **Challenge 1:** Visit your favorite website and identify 5 different ways to locate the search input. Which is best?

2. **Challenge 2:** Find an element using CSS, then refactor it to use a modern locator.

3. **Challenge 3:** Create a test that breaks intentionally with bad locators, then fix it with good ones.

4. **Challenge 4:** Practice XPath parent navigation on a complex page structure.

5. **Challenge 5:** Build a Page Object that uses only modern locators.

Keep practicing! The more you work with locators, the better your intuition will become. 🎯
