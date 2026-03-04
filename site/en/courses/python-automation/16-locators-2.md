# Lecture 16: Element Locator Strategies. Part 2

CSS and XPath selectors.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_16_Locator_Strategies_Part2/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_16_Locator_Strategies_Part2/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_16_Locator_Strategies_Part2/exercises" target="_blank">📝 Вправи</a>
</div>

## CSS Selectors

```python
# By ID
page.locator("#login-btn")

# By class
page.locator(".submit-button")

# By attribute
page.locator("[data-testid='submit']")
page.locator("input[type='email']")

# Combinations
page.locator("form.login input[name='email']")

# Pseudo-selectors
page.locator("li:first-child")
page.locator("li:nth-child(2)")
```

## XPath Selectors

```python
# Basic XPath
page.locator("//button[@type='submit']")

# By text
page.locator("//span[text()='Submit']")
page.locator("//button[contains(text(), 'Sign')]")

# By attribute
page.locator("//input[@placeholder='Email']")

# DOM navigation
page.locator("//div[@class='card']//button")
page.locator("//table//tr[2]/td[1]")
```

## When to Use What

| Situation | Recommendation |
|----------|--------------|
| Has data-testid | `get_by_test_id()` |
| Button/link | `get_by_role()` |
| Form field | `get_by_label()` |
| Complex structure | CSS selector |
| Text inside element | XPath with contains() |
