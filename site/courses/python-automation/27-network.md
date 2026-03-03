# Lecture 27: Network Interception

Перехоплення мережевих запитів.

<div class="lecture-resources">

<a href="/python_automation_courses/presentations/Lecture_27_Network_Interception/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_27_Network_Interception/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_27_Network_Interception/exercises)

</div>

## Моніторинг запитів

```python
# Логування запитів
page.on("request", lambda req: print(f">> {req.method} {req.url}"))
page.on("response", lambda res: print(f"<< {res.status} {res.url}"))

page.goto("https://example.com")
```

## Очікування запитів

```python
# Очікування response
with page.expect_response("**/api/users") as response_info:
    page.get_by_role("button", name="Load Users").click()

response = response_info.value
print(response.status)
print(response.json())
```

## Мокування відповідей

```python
# Повернути фейкову відповідь
page.route("**/api/users", lambda route: route.fulfill(
    status=200,
    content_type="application/json",
    body='[{"id": 1, "name": "Mock User"}]'
))

page.goto("https://example.com")
```

## Блокування запитів

```python
# Блокувати зображення
page.route("**/*.{png,jpg,jpeg,gif}", lambda route: route.abort())

# Блокувати аналітику
page.route("**/analytics/**", lambda route: route.abort())
page.route("**google-analytics**", lambda route: route.abort())
```

## Модифікація запитів

```python
def modify_request(route):
    headers = route.request.headers
    headers["X-Custom-Header"] = "custom-value"
    route.continue_(headers=headers)

page.route("**/api/**", modify_request)
```

## Модифікація відповідей

```python
def modify_response(route):
    response = route.fetch()
    body = response.json()
    body["modified"] = True
    route.fulfill(
        response=response,
        body=json.dumps(body)
    )

page.route("**/api/data", modify_response)
```

## Симуляція мережевих умов

```python
# Офлайн режим
context = browser.new_context(offline=True)

# Або динамічно
context.set_offline(True)
# ... тест офлайн функціональності
context.set_offline(False)
```
