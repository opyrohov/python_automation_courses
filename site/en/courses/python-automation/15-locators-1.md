# Lecture 15: Element Locator Strategies. Part 1

Element locator strategies — recommended locators.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_15_Locator_Strategies_Part1/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/exercises" target="_blank">📝 Вправи</a>
</div>

## Lecture Topics

- What are locators
- Recommended locators
- get_by_role
- get_by_text
- get_by_label

## What are Locators?

A locator is a way to find an element on a page in order to interact with it.

**Locator priority (from best to worst):**
1. `get_by_role` — by element role
2. `get_by_text` — by text
3. `get_by_label` — by form label
4. `get_by_placeholder` — by placeholder
5. `get_by_test_id` — by data-testid
6. CSS/XPath — as a last resort

## get_by_role

```python
# Buttons
page.get_by_role("button", name="Submit")
page.get_by_role("button", name="Sign In")

# Links
page.get_by_role("link", name="Home")
page.get_by_role("link", name="About Us")

# Text fields
page.get_by_role("textbox", name="Email")

# Checkbox
page.get_by_role("checkbox", name="Remember me")

# Headings
page.get_by_role("heading", name="Welcome")
page.get_by_role("heading", level=1)

# List
page.get_by_role("list")
page.get_by_role("listitem")
```

## Element Roles

| HTML Element | Role |
|-------------|------|
| `<button>` | button |
| `<a>` | link |
| `<input type="text">` | textbox |
| `<input type="checkbox">` | checkbox |
| `<input type="radio">` | radio |
| `<select>` | combobox |
| `<h1>-<h6>` | heading |
| `<ul>`, `<ol>` | list |
| `<li>` | listitem |
| `<table>` | table |
| `<tr>` | row |
| `<img>` | img |

## get_by_text

```python
# Exact match
page.get_by_text("Welcome", exact=True)

# Partial match (default)
page.get_by_text("Welcome")  # will find "Welcome to our site"

# Regular expression
import re
page.get_by_text(re.compile(r"Welcome.*"))
```

## get_by_label

```python
# <label for="email">Email</label>
# <input id="email">
page.get_by_label("Email")

# <label>
#   Password
#   <input type="password">
# </label>
page.get_by_label("Password")
```

## get_by_placeholder

```python
# <input placeholder="Enter your email">
page.get_by_placeholder("Enter your email")

# Partial match
page.get_by_placeholder("email")
```

## get_by_alt_text

```python
# <img alt="Company Logo">
page.get_by_alt_text("Company Logo")

# For images
page.get_by_alt_text("Profile picture")
```

## get_by_title

```python
# <button title="Close dialog">×</button>
page.get_by_title("Close dialog")
```

## get_by_test_id

```python
# <button data-testid="submit-btn">Submit</button>
page.get_by_test_id("submit-btn")

# The most stable locator for critical elements
page.get_by_test_id("login-button")
page.get_by_test_id("user-profile")
```

## Combining Locators

```python
# Filtering
page.get_by_role("listitem").filter(has_text="Product A")

# Nested locators
card = page.get_by_test_id("product-card")
card.get_by_role("button", name="Buy")

# Chaining
page.get_by_role("list").get_by_role("listitem").first
```

## Exercises

::: tip Exercise 1
Find all buttons on the page and print their text.
:::

::: tip Exercise 2
Write a test that fills a form using only recommended locators.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_15_Locator_Strategies_Part1/examples)
