# Lecture 27: Network Request Interception

Network request interception.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_27_Network_Interception/presentation.html" target="_blank">🎬 Презентація</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_27_Network_Interception/examples" target="_blank">💻 Приклади</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_27_Network_Interception/exercises" target="_blank">📝 Вправи</a>
</div>

## Monitoring Requests

```python
# Logging requests
page.on("request", lambda req: print(f">> {req.method} {req.url}"))
page.on("response", lambda res: print(f"<< {res.status} {res.url}"))

page.goto("https://example.com")
```

## Waiting for Requests

```python
# Waiting for response
with page.expect_response("**/api/users") as response_info:
    page.get_by_role("button", name="Load Users").click()

response = response_info.value
print(response.status)
print(response.json())
```

## Mocking Responses

```python
# Return a fake response
page.route("**/api/users", lambda route: route.fulfill(
    status=200,
    content_type="application/json",
    body='[{"id": 1, "name": "Mock User"}]'
))

page.goto("https://example.com")
```

## Blocking Requests

```python
# Block images
page.route("**/*.{png,jpg,jpeg,gif}", lambda route: route.abort())

# Block analytics
page.route("**/analytics/**", lambda route: route.abort())
page.route("**google-analytics**", lambda route: route.abort())
```

## Modifying Requests

```python
def modify_request(route):
    headers = route.request.headers
    headers["X-Custom-Header"] = "custom-value"
    route.continue_(headers=headers)

page.route("**/api/**", modify_request)
```

## Modifying Responses

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

## Simulating Network Conditions

```python
# Offline mode
context = browser.new_context(offline=True)

# Or dynamically
context.set_offline(True)
# ... test offline functionality
context.set_offline(False)
```
