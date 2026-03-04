# Working with API

The `requests` library is the most popular tool for making HTTP requests in Python. This page covers everything you need for REST API testing: from basic requests to advanced automation patterns.

## Installation

```python
pip install requests
```

```python
import requests
```

::: tip Verify installation
```python
import requests
print(requests.__version__)  # e.g., 2.31.0
```
:::

## HTTP Methods

### GET — retrieve data

```python
import requests

response = requests.get("https://api.example.com/users")
print(response.status_code)  # 200
print(response.json())       # [{"id": 1, "name": "John"}, ...]
```

### POST — create a resource

```python
payload = {"name": "Test User", "email": "test@example.com"}

response = requests.post(
    "https://api.example.com/users",
    json=payload
)
print(response.status_code)  # 201
print(response.json())       # {"id": 42, "name": "Test User", ...}
```

### PUT — full resource replacement

```python
updated_data = {"name": "Updated User", "email": "updated@example.com"}

response = requests.put(
    "https://api.example.com/users/42",
    json=updated_data
)
print(response.status_code)  # 200
```

### PATCH — partial update

```python
partial_data = {"email": "new_email@example.com"}

response = requests.patch(
    "https://api.example.com/users/42",
    json=partial_data
)
print(response.status_code)  # 200
```

### DELETE — remove a resource

```python
response = requests.delete("https://api.example.com/users/42")
print(response.status_code)  # 204
```

::: info QA Example: CRUD testing
```python
# Full CRUD testing cycle
base_url = "https://api.example.com/users"

# Create
new_user = {"name": "QA Test", "email": "qa@test.com"}
create_resp = requests.post(base_url, json=new_user)
assert create_resp.status_code == 201
user_id = create_resp.json()["id"]

# Read
get_resp = requests.get(f"{base_url}/{user_id}")
assert get_resp.status_code == 200
assert get_resp.json()["name"] == "QA Test"

# Update
update_resp = requests.put(f"{base_url}/{user_id}", json={"name": "Updated", "email": "qa@test.com"})
assert update_resp.status_code == 200

# Delete
delete_resp = requests.delete(f"{base_url}/{user_id}")
assert delete_resp.status_code == 204
```
:::

## Request Parameters

### Query parameters (params)

```python
# Parameters are appended to the URL automatically
params = {"page": 1, "per_page": 10, "sort": "name"}

response = requests.get(
    "https://api.example.com/users",
    params=params
)
# URL becomes: https://api.example.com/users?page=1&per_page=10&sort=name
```

### Headers

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Custom-Header": "test-value"
}

response = requests.get(
    "https://api.example.com/users",
    headers=headers
)
```

### Request body (json vs data)

```python
# json= automatically serializes dict and sets Content-Type
response = requests.post(
    "https://api.example.com/users",
    json={"name": "Test", "age": 25}
)

# data= sends form-encoded data
response = requests.post(
    "https://api.example.com/login",
    data={"username": "admin", "password": "secret"}
)

# data= with a string — sends as-is
import json
response = requests.post(
    "https://api.example.com/users",
    data=json.dumps({"name": "Test"}),
    headers={"Content-Type": "application/json"}
)
```

### Timeout

```python
# Timeout in seconds
response = requests.get(
    "https://api.example.com/users",
    timeout=5  # 5 seconds
)

# Separate timeouts for connection and reading
response = requests.get(
    "https://api.example.com/users",
    timeout=(3, 10)  # 3 sec for connection, 10 sec for reading
)
```

::: warning Always set a timeout
Without a timeout, a request can hang forever. Always specify `timeout` in your tests.
```python
# Bad — can hang indefinitely
response = requests.get("https://api.example.com/users")

# Good — has a time limit
response = requests.get("https://api.example.com/users", timeout=30)
```
:::

## The Response Object

```python
response = requests.get("https://api.example.com/users/1")

# Status code
print(response.status_code)     # 200

# Response body
print(response.json())          # dict or list (parses JSON)
print(response.text)            # String (raw response text)
print(response.content)         # bytes (binary content)

# Response headers
print(response.headers)                    # All headers
print(response.headers["Content-Type"])    # 'application/json'

# Cookies
print(response.cookies)                    # RequestsCookieJar
print(response.cookies.get("session_id"))  # Specific cookie

# Other attributes
print(response.url)             # Final URL (after redirects)
print(response.elapsed)         # Request execution time
print(response.encoding)        # Response encoding
print(response.ok)              # True if status_code < 400
```

::: info QA Example: validating an API response
```python
response = requests.get("https://api.example.com/users/1", timeout=10)

# Status code check
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# Headers check
assert response.headers["Content-Type"] == "application/json"

# Body check
data = response.json()
assert "id" in data, "Response missing 'id' field"
assert data["id"] == 1
assert isinstance(data["name"], str), "Name should be a string"

# Response time check
assert response.elapsed.total_seconds() < 2, "Response too slow"
```
:::

## Authentication

### Basic Auth

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/profile",
    auth=HTTPBasicAuth("username", "password"),
    timeout=10
)

# Shorthand
response = requests.get(
    "https://api.example.com/profile",
    auth=("username", "password"),
    timeout=10
)
```

### Bearer Token

```python
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://api.example.com/profile",
    headers=headers,
    timeout=10
)
```

### API Key

```python
# API key in header
headers = {"X-API-Key": "your-api-key-here"}
response = requests.get(
    "https://api.example.com/data",
    headers=headers,
    timeout=10
)

# API key in query parameters
params = {"api_key": "your-api-key-here"}
response = requests.get(
    "https://api.example.com/data",
    params=params,
    timeout=10
)
```

::: tip Storing secrets
Never hardcode tokens or passwords in your code. Use environment variables:
```python
import os

API_TOKEN = os.environ.get("API_TOKEN")
API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.example.com")

headers = {"Authorization": f"Bearer {API_TOKEN}"}
```
:::

## Session Management

`requests.Session()` persists cookies, headers, and other parameters across requests.

```python
session = requests.Session()

# Set base headers for all requests
session.headers.update({
    "Authorization": "Bearer my-token",
    "Content-Type": "application/json"
})

# All requests through session will use these headers
response1 = session.get("https://api.example.com/users", timeout=10)
response2 = session.get("https://api.example.com/posts", timeout=10)

# Cookies are preserved automatically between requests
session.post(
    "https://api.example.com/login",
    json={"username": "admin", "password": "secret"},
    timeout=10
)
# Subsequent requests are already authenticated via cookies
profile = session.get("https://api.example.com/profile", timeout=10)

# Close the session
session.close()
```

::: info QA Example: base API test client
```python
import requests

class APIClient:
    """Base client for API testing."""

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=30,
            **kwargs
        )

    def post(self, endpoint, data=None, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=30,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=30,
            **kwargs
        )

    def close(self):
        self.session.close()


# Usage
client = APIClient("https://api.example.com", token="my-token")
response = client.get("/users")
assert response.status_code == 200
client.close()
```
:::

## Error Handling

### raise_for_status()

```python
response = requests.get("https://api.example.com/users/999", timeout=10)

# Raises HTTPError if status_code >= 400
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")
```

### Handling timeouts

```python
try:
    response = requests.get(
        "https://api.example.com/slow-endpoint",
        timeout=5
    )
except requests.exceptions.ConnectTimeout:
    print("Could not connect to the server")
except requests.exceptions.ReadTimeout:
    print("Server did not respond in time")
except requests.exceptions.Timeout:
    print("General timeout")
```

### Retries

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure retry strategy
retry_strategy = Retry(
    total=3,                    # Maximum 3 attempts
    backoff_factor=1,           # Delay between attempts: 1, 2, 4 seconds
    status_forcelist=[500, 502, 503, 504],  # Retry on these status codes
    allowed_methods=["GET", "POST"]         # Which methods to retry
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

# Requests now automatically retry on errors
response = session.get("https://api.example.com/users", timeout=10)
```

### Comprehensive error handling

```python
import requests

def safe_api_call(method, url, **kwargs):
    """Safe API call with full error handling."""
    kwargs.setdefault("timeout", 30)

    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print(f"Connection error to {url}")
    except requests.exceptions.Timeout:
        print(f"Timeout requesting {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Unknown error: {e}")

    return None
```

::: warning requests exception hierarchy
```
RequestException
├── ConnectionError
│   └── ProxyError
│       └── SSLError
├── HTTPError
├── URLRequired
├── TooManyRedirects
├── Timeout
│   ├── ConnectTimeout
│   └── ReadTimeout
└── ContentDecodingError
```
Catch specific exceptions before general ones.
:::

## QA Automation Examples

### Testing REST API endpoints

```python
import requests
import pytest

BASE_URL = "https://api.example.com"

class TestUsersAPI:
    """Tests for the /users endpoint."""

    def test_get_all_users(self):
        response = requests.get(f"{BASE_URL}/users", timeout=10)
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0

    def test_get_user_by_id(self):
        response = requests.get(f"{BASE_URL}/users/1", timeout=10)
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "name" in user
        assert "email" in user

    def test_create_user(self):
        new_user = {
            "name": "Test User",
            "email": "test@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=new_user,
            timeout=10
        )
        assert response.status_code == 201
        created = response.json()
        assert created["name"] == new_user["name"]
        assert "id" in created

    def test_get_nonexistent_user(self):
        response = requests.get(f"{BASE_URL}/users/99999", timeout=10)
        assert response.status_code == 404

    def test_create_user_without_required_fields(self):
        response = requests.post(
            f"{BASE_URL}/users",
            json={},
            timeout=10
        )
        assert response.status_code == 400
```

### Validating response schemas

```python
def validate_user_schema(user_data):
    """Verify the response matches the expected schema."""
    required_fields = {
        "id": int,
        "name": str,
        "email": str,
        "created_at": str
    }

    for field, expected_type in required_fields.items():
        assert field in user_data, f"Missing field: {field}"
        assert isinstance(user_data[field], expected_type), (
            f"Field '{field}' has type {type(user_data[field])}, "
            f"expected {expected_type}"
        )

# Usage in a test
def test_user_response_schema():
    response = requests.get("https://api.example.com/users/1", timeout=10)
    assert response.status_code == 200
    validate_user_schema(response.json())
```

::: tip Schema validation with jsonschema
For more complex schemas, use the `jsonschema` library:
```python
pip install jsonschema
```
```python
from jsonschema import validate

user_schema = {
    "type": "object",
    "required": ["id", "name", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
        "is_active": {"type": "boolean"}
    },
    "additionalProperties": False
}

def test_user_json_schema():
    response = requests.get("https://api.example.com/users/1", timeout=10)
    validate(instance=response.json(), schema=user_schema)
```
:::

### Automated API testing patterns

```python
import requests
import pytest

class TestAPIPatterns:
    """Advanced API testing patterns."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Create session and test data before each test."""
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": "Bearer test-token"
        })
        self.base_url = "https://api.example.com"
        yield
        self.session.close()

    def test_pagination(self):
        """Verify pagination works correctly."""
        page1 = self.session.get(
            f"{self.base_url}/users",
            params={"page": 1, "per_page": 5},
            timeout=10
        )
        assert page1.status_code == 200
        data1 = page1.json()
        assert len(data1) <= 5

        page2 = self.session.get(
            f"{self.base_url}/users",
            params={"page": 2, "per_page": 5},
            timeout=10
        )
        assert page2.status_code == 200
        data2 = page2.json()

        # IDs across pages should not overlap
        ids_page1 = {u["id"] for u in data1}
        ids_page2 = {u["id"] for u in data2}
        assert ids_page1.isdisjoint(ids_page2), "Duplicate entries across pages"

    def test_response_time(self):
        """Check response time (performance)."""
        response = self.session.get(
            f"{self.base_url}/users",
            timeout=10
        )
        assert response.elapsed.total_seconds() < 2, (
            f"Response too slow: {response.elapsed.total_seconds()}s"
        )

    def test_unauthorized_access(self):
        """Verify access without authentication is denied."""
        no_auth_session = requests.Session()
        response = no_auth_session.get(
            f"{self.base_url}/admin/users",
            timeout=10
        )
        assert response.status_code in [401, 403]
        no_auth_session.close()

    def test_idempotent_put(self):
        """Verify PUT idempotency."""
        user_data = {"name": "Test", "email": "test@example.com"}
        url = f"{self.base_url}/users/1"

        resp1 = self.session.put(url, json=user_data, timeout=10)
        resp2 = self.session.put(url, json=user_data, timeout=10)

        assert resp1.status_code == resp2.status_code
        assert resp1.json() == resp2.json()
```

## Useful Links

- [requests documentation](https://docs.python-requests.org/)
- [HTTP status codes (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [REST API Best Practices](https://restfulapi.net/)
- [jsonschema documentation](https://python-jsonschema.readthedocs.io/)

---

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="/python_automation_courses/en/docs/python/regex">← Regular Expressions</a>
  <a href="/python_automation_courses/en/docs/python/virtual-environments">Virtual Environments →</a>
</div>
