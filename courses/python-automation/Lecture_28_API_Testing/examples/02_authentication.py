"""Example 2: API Authentication

Demonstrates different authentication methods for API requests.
"""
from playwright.sync_api import sync_playwright
import base64

with sync_playwright() as p:
    print("=== API Authentication Demo ===\n")

    # EXAMPLE 1: Bearer Token Authentication
    print("--- Example 1: Bearer Token ---")

    # In real scenario, you'd get this from login or environment
    fake_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fake"

    api_bearer = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Authorization": f"Bearer {fake_token}"
        }
    )
    print(f"  Created context with Bearer token")
    print(f"  Token: {fake_token[:30]}...")

    # All requests will include Authorization header
    response = api_bearer.get("/posts/1")
    print(f"  GET /posts/1 - Status: {response.status}")

    api_bearer.dispose()

    # EXAMPLE 2: Basic Authentication
    print("\n--- Example 2: Basic Auth ---")

    username = "testuser"
    password = "testpass"
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

    api_basic = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Authorization": f"Basic {credentials}"
        }
    )
    print(f"  Username: {username}")
    print(f"  Encoded: Basic {credentials[:20]}...")

    response = api_basic.get("/posts/1")
    print(f"  GET /posts/1 - Status: {response.status}")

    api_basic.dispose()

    # EXAMPLE 3: API Key Authentication
    print("\n--- Example 3: API Key ---")

    api_key = "sk-test-12345abcdef"

    # API Key in header
    api_header = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "X-API-Key": api_key
        }
    )
    print(f"  API Key in header: X-API-Key: {api_key}")

    response = api_header.get("/posts/1")
    print(f"  GET /posts/1 - Status: {response.status}")

    api_header.dispose()

    # API Key in query parameter
    api_query = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    print(f"\n  API Key in query: ?api_key={api_key}")

    response = api_query.get("/posts/1", params={"api_key": api_key})
    print(f"  GET /posts/1?api_key=... - Status: {response.status}")

    api_query.dispose()

    # EXAMPLE 4: Custom Headers
    print("\n--- Example 4: Custom Headers ---")

    api_custom = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "X-Custom-Header": "CustomValue",
            "X-Request-ID": "test-123",
            "Accept": "application/json",
            "User-Agent": "PlaywrightAPITest/1.0"
        }
    )
    print("  Custom headers:")
    print("    X-Custom-Header: CustomValue")
    print("    X-Request-ID: test-123")
    print("    Accept: application/json")
    print("    User-Agent: PlaywrightAPITest/1.0")

    response = api_custom.get("/posts/1")
    print(f"  GET /posts/1 - Status: {response.status}")

    api_custom.dispose()

    # EXAMPLE 5: Per-Request Headers
    print("\n--- Example 5: Per-Request Headers ---")

    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # Override headers for specific request
    response = api.get("/posts/1", headers={
        "Authorization": "Bearer specific-request-token",
        "X-Request-ID": "req-456"
    })
    print("  Added headers for specific request only")
    print(f"  GET /posts/1 - Status: {response.status}")

    api.dispose()

    # EXAMPLE 6: Login to Get Token (conceptual)
    print("\n--- Example 6: Login Flow (Conceptual) ---")

    print("""
    # Real-world pattern:

    # 1. Create unauthenticated context
    api = p.request.new_context(base_url="https://api.example.com")

    # 2. Login to get token
    response = api.post("/auth/login", data={
        "email": "user@example.com",
        "password": "secret"
    })
    token = response.json()["access_token"]

    # 3. Create authenticated context
    auth_api = p.request.new_context(
        base_url="https://api.example.com",
        extra_http_headers={
            "Authorization": f"Bearer {token}"
        }
    )

    # 4. Make authenticated requests
    response = auth_api.get("/users/me")
    """)

    print("\n=== Demo Complete ===")
    print("\nAuthentication methods:")
    print("  - Bearer Token: Authorization: Bearer <token>")
    print("  - Basic Auth: Authorization: Basic <base64>")
    print("  - API Key: X-API-Key: <key> or ?api_key=<key>")
    print("  - Custom: Any header via extra_http_headers")
