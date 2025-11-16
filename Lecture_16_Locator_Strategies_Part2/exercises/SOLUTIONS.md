# Exercise Solutions - Lecture 16: Locator Strategies (Part 2)

## Exercise 1: Chaining Practice

### Solutions

```python
from playwright.sync_api import sync_playwright

def chaining_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add test data
        todos = ["Work: Finish report", "Personal: Buy milk", "Work: Team meeting"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Chain to find the input field
        page.locator("section.todoapp").locator("header").locator("input").fill("Chained task")
        page.locator("section.todoapp").locator("header").locator("input").press("Enter")

        # TODO 2: Chain to check the first todo's checkbox
        page.locator("ul.todo-list").locator("li").first.locator("input.toggle").check()

        # TODO 3: Chain to get the text of the second todo
        second_todo = page.locator("section.todoapp").locator("ul.todo-list").locator("li").nth(1).locator("label").text_content()
        print(f"Second todo: {second_todo}")

        # TODO 4: Count todos using chaining
        todo_count = page.locator("section.todoapp").locator("ul.todo-list").locator("li").count()
        print(f"Total todos: {todo_count}")

        print("\n✅ Exercise 1 complete!")
        input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    chaining_practice()
```

### Explanations

1. **TODO 1:** Chain from broad to specific: `section.todoapp` → `header` → `input`
2. **TODO 2:** Chain to structure, select `.first`, then chain to checkbox
3. **TODO 3:** Full chain with `.nth(1)` for second item, then `label` for text
4. **TODO 4:** Chain to list, then li elements, then count

---

## Exercise 2: Filtering Challenge

### Solutions

```python
from playwright.sync_api import sync_playwright

def filtering_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add test data
        todos = ["Buy groceries", "Buy concert tickets", "Walk the dog", "Read a book", "Buy new shoes"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # Mark some as complete
        page.locator("li").first.locator("input.toggle").check()
        page.locator("li").nth(2).locator("input.toggle").check()

        # TODO 1: Filter todos containing "Buy"
        buy_todos = page.locator("li").filter(has_text="Buy")
        print(f"Todos containing 'Buy': {buy_todos.count()}")

        # TODO 2: Filter and find the "Walk the dog" todo
        page.locator("li").filter(has_text="Walk the dog").locator("input.toggle").check()
        print("✓ Marked 'Walk the dog' as complete")

        # TODO 3: Filter for completed todos
        completed = page.locator("li").filter(has=page.locator("input.toggle:checked")).count()
        print(f"Completed todos: {completed}")

        # TODO 4: Filter for active (NOT completed) todos
        active = page.locator("li").filter(has_not=page.locator("input.toggle:checked")).count()
        print(f"Active todos: {active}")

        # TODO 5: Find active "Buy" todos
        active_buy = (
            page.locator("li")
            .filter(has_text="Buy")
            .filter(has_not=page.locator("input.toggle:checked"))
            .count()
        )
        print(f"Active 'Buy' todos: {active_buy}")

        print("\n✅ Exercise 2 complete!")
        input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    filtering_challenge()
```

### Explanations

1. **TODO 1:** `filter(has_text="Buy")` filters for todos containing "Buy"
2. **TODO 2:** Filter by text, then chain to checkbox
3. **TODO 3:** `filter(has=page.locator("input.toggle:checked"))` finds todos with checked checkbox
4. **TODO 4:** `filter(has_not=...)` excludes completed todos
5. **TODO 5:** Chain two filters: by text AND by not checked

---

## Exercise 3: Selection Practice

### Solutions

```python
from playwright.sync_api import sync_playwright

def selection_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add test data
        todos = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Get and print the text of the first todo
        first_text = page.locator("li").first.text_content()
        print(f"First todo: {first_text}")

        # TODO 2: Check the last todo as complete
        page.locator("li").last.locator("input.toggle").check()
        print("✓ Checked last todo")

        # TODO 3: Get the text of the third todo (index 2)
        third_text = page.locator("li").nth(2).text_content()
        print(f"Third todo: {third_text}")

        # TODO 4: Get the second-to-last todo using negative index
        second_last_text = page.locator("li").nth(-2).text_content()
        print(f"Second to last: {second_last_text}")

        # TODO 5: Count total todos
        total = page.locator("li").count()
        print(f"Total todos: {total}")

        # TODO 6: Get all todos and iterate through them
        all_todos = page.locator("li").all()
        print("All todos:")
        for i, todo in enumerate(all_todos):
            print(f"  {i + 1}. {todo.locator('label').text_content()}")

        # TODO 7: Verify a specific element exists
        error_exists = page.locator(".error-message").count() > 0
        print(f"Error message exists: {error_exists}")

        print("\n✅ Exercise 3 complete!")
        input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    selection_practice()
```

### Explanations

1. **TODO 1:** `.first` selects the first matching element
2. **TODO 2:** `.last` selects the last element, then chain to checkbox
3. **TODO 3:** `.nth(2)` selects element at index 2 (third element, 0-indexed)
4. **TODO 4:** `.nth(-2)` uses negative index for second-to-last
5. **TODO 5:** `.count()` returns total number of matches
6. **TODO 6:** `.all()` returns a list to iterate through
7. **TODO 7:** `.count() > 0` checks if element exists

---

## Exercise 4: Combined Mastery

### Solutions

```python
from playwright.sync_api import sync_playwright

def combined_mastery():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        # Add categorized todos
        todos = [
            "Work: Review code",
            "Personal: Call dentist",
            "Work: Write documentation",
            "Personal: Buy birthday gift",
            "Work: Fix bug #123",
            "Personal: Book vacation"
        ]
        for todo in todos:
            page.locator(".new-todo").fill(todo)
            page.locator(".new-todo").press("Enter")

        # TODO 1: Mark the first "Work:" todo as complete
        page.locator("li").filter(has_text="Work:").first.locator("input.toggle").check()
        print("✓ Marked first work todo as complete")

        # TODO 2: Count "Personal:" todos
        personal_count = page.locator("li").filter(has_text="Personal:").count()
        print(f"Personal todos: {personal_count}")

        # TODO 3: Get the text of the second "Work:" todo
        second_work = (
            page.locator("li")
            .filter(has_text="Work:")
            .nth(1)
            .locator("label")
            .text_content()
        )
        print(f"Second work todo: {second_work}")

        # TODO 4: Mark ALL "Personal:" todos as complete
        personal_todos = page.locator("li").filter(has_text="Personal:").all()
        for todo in personal_todos:
            todo.locator("input.toggle").check()
        print(f"✓ Marked all {len(personal_todos)} personal todos as complete")

        # TODO 5: Find active (not completed) "Work:" todos
        active_work = (
            page.locator("li")
            .filter(has_text="Work:")
            .filter(has_not=page.locator("input.toggle:checked"))
            .count()
        )
        print(f"Active work todos: {active_work}")

        # TODO 6: Verify all personal todos are completed
        total_personal = page.locator("li").filter(has_text="Personal:").count()
        completed_personal = (
            page.locator("li")
            .filter(has_text="Personal:")
            .filter(has=page.locator("input.toggle:checked"))
            .count()
        )
        if total_personal == completed_personal:
            print("✓ All personal todos are completed!")
        else:
            print(f"✗ {total_personal - completed_personal} personal todos still pending")

        # TODO 7: Get all work todo texts and print them
        work_todos = page.locator("li").filter(has_text="Work:").all()
        print("Work todos:")
        for todo in work_todos:
            text = todo.locator("label").text_content()
            is_done = todo.locator("input.toggle").is_checked()
            status = "✓" if is_done else "○"
            print(f"  {status} {text}")

        print("\n✅ Exercise 4 complete!")
        input("\nPress Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    combined_mastery()
```

### Explanations

1. **TODO 1:** Filter + First + Chain: `filter(has_text="Work:")` → `.first` → `.locator("input.toggle")`
2. **TODO 2:** Filter + Count: `filter(has_text="Personal:")` → `.count()`
3. **TODO 3:** Filter + nth + Chain: Filter work, get second one (`.nth(1)`), get label text
4. **TODO 4:** Filter + All + Iterate: Get all personal, iterate and check each
5. **TODO 5:** Two Filters: Filter for "Work:" AND not checked
6. **TODO 6:** Compare counts: Total personal vs completed personal
7. **TODO 7:** Filter + All + Extract data: Get all work todos, check status, print

---

## Key Takeaways

### Chaining
- Start broad (container), narrow to specific (element)
- Example: `page.locator(".container").locator(".button")`
- Keep chains 2-3 levels for readability

### Filtering
- **has_text:** `filter(has_text="Buy")` - Contains text
- **has:** `filter(has=page.locator(".badge"))` - Contains element
- **has_not_text:** `filter(has_not_text="Sold")` - Excludes text
- **has_not:** `filter(has_not=page.locator(":checked"))` - Excludes element
- Chain multiple filters for precision

### Selection
- **.first** - First element
- **.last** - Last element
- **.nth(index)** - Element at index (0-based, supports negative)
- **.count()** - Total matches
- **.all()** - List of all elements

### Combining All Three
```python
# Chain → Filter → Select → Chain
page.locator(".container")          # Chain
    .locator("li")                  # Chain
    .filter(has_text="Active")      # Filter
    .first                          # Select
    .locator("button")              # Chain
    .click()                        # Action
```

### Best Practices
1. ✅ Filter by text when possible (more reliable than position)
2. ✅ Use `.count()` to verify before interacting
3. ✅ Chain from broad to specific
4. ✅ Combine techniques for maximum precision
5. ❌ Avoid relying solely on position (.nth)
6. ❌ Don't create overly long chains

Keep practicing these techniques to build muscle memory! 🎯
