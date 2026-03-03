# Lecture 26: Cookies & Local Storage

Cookies та локальне сховище.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_26_Cookies_Local_Storage/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_26_Cookies_Local_Storage/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_26_Cookies_Local_Storage/exercises)

</div>

## Cookies

```python
# Отримати всі cookies
cookies = context.cookies()
for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")

# Отримати cookies для URL
cookies = context.cookies(["https://example.com"])

# Додати cookie
context.add_cookies([{
    "name": "session_id",
    "value": "abc123",
    "domain": "example.com",
    "path": "/"
}])

# Очистити cookies
context.clear_cookies()
```

## Local Storage

```python
# Отримати значення
value = page.evaluate("() => localStorage.getItem('key')")

# Встановити значення
page.evaluate("() => localStorage.setItem('key', 'value')")

# Видалити
page.evaluate("() => localStorage.removeItem('key')")

# Очистити все
page.evaluate("() => localStorage.clear()")

# Отримати всі ключі
keys = page.evaluate("""() => {
    const keys = [];
    for (let i = 0; i < localStorage.length; i++) {
        keys.push(localStorage.key(i));
    }
    return keys;
}""")
```

## Session Storage

```python
# Аналогічно до localStorage
value = page.evaluate("() => sessionStorage.getItem('key')")
page.evaluate("() => sessionStorage.setItem('key', 'value')")
```

## Storage State

```python
# Зберегти весь стан (cookies + localStorage)
storage = context.storage_state()

# Зберегти у файл
context.storage_state(path="state.json")

# Завантажити стан
context = browser.new_context(storage_state="state.json")
```

## Приклад: Пропуск cookie banner

```python
# Встановити cookie що користувач прийняв cookies
context.add_cookies([{
    "name": "cookie_consent",
    "value": "accepted",
    "domain": "example.com",
    "path": "/"
}])

page.goto("https://example.com")
# Cookie banner не з'явиться
```
