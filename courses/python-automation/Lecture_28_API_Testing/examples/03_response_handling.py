"""Example 3: Response Handling

Demonstrates how to handle and validate API responses.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("=== Response Handling Demo ===\n")

    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # EXAMPLE 1: Status and OK check
    print("--- Example 1: Status Codes ---")

    response = api.get("/posts/1")
    print(f"GET /posts/1")
    print(f"  status: {response.status}")
    print(f"  status_text: {response.status_text}")
    print(f"  ok: {response.ok}")  # True if 200-299
    print(f"  url: {response.url}")

    # Non-existent resource
    response_404 = api.get("/posts/999999")
    print(f"\nGET /posts/999999")
    print(f"  status: {response_404.status}")
    print(f"  ok: {response_404.ok}")

    # EXAMPLE 2: Response Headers
    print("\n--- Example 2: Response Headers ---")

    response = api.get("/posts/1")
    print("Response headers:")
    for key, value in list(response.headers.items())[:5]:
        print(f"  {key}: {value}")

    # Get specific header
    content_type = response.headers.get("content-type")
    print(f"\nContent-Type: {content_type}")

    # EXAMPLE 3: JSON Response
    print("\n--- Example 3: JSON Response ---")

    response = api.get("/posts/1")
    data = response.json()

    print("JSON data:")
    print(f"  Type: {type(data)}")
    print(f"  Keys: {list(data.keys())}")
    print(f"  id: {data['id']}")
    print(f"  title: {data['title'][:40]}...")

    # JSON array
    response = api.get("/posts", params={"_limit": 3})
    posts = response.json()
    print(f"\nJSON array: {len(posts)} items")

    # EXAMPLE 4: Text Response
    print("\n--- Example 4: Text Response ---")

    response = api.get("/posts/1")
    text = response.text()
    print(f"Raw text (first 100 chars):")
    print(f"  {text[:100]}...")

    # EXAMPLE 5: Binary Response
    print("\n--- Example 5: Binary Response ---")

    response = api.get("/posts/1")
    body = response.body()
    print(f"Binary body:")
    print(f"  Type: {type(body)}")
    print(f"  Size: {len(body)} bytes")

    # EXAMPLE 6: Assertions
    print("\n--- Example 6: Response Assertions ---")

    response = api.get("/posts/1")

    # Status assertions
    assert response.status == 200, f"Expected 200, got {response.status}"
    print("  ✓ Status is 200")

    assert response.ok, "Response not OK"
    print("  ✓ Response is OK")

    # JSON assertions
    data = response.json()

    assert "id" in data, "Missing 'id' field"
    print("  ✓ Has 'id' field")

    assert "title" in data, "Missing 'title' field"
    print("  ✓ Has 'title' field")

    assert data["id"] == 1, f"Expected id=1, got {data['id']}"
    print("  ✓ id equals 1")

    assert isinstance(data["title"], str), "title should be string"
    print("  ✓ title is string")

    # EXAMPLE 7: Error Handling
    print("\n--- Example 7: Error Handling ---")

    response = api.get("/posts/999999")

    if not response.ok:
        print(f"  Request failed with status: {response.status}")
        # Handle error
    else:
        data = response.json()

    # Safe JSON parsing
    try:
        response = api.get("/posts/1")
        data = response.json()
        print(f"  ✓ Successfully parsed JSON")
    except Exception as e:
        print(f"  ✗ Failed to parse: {e}")

    # EXAMPLE 8: Response Validation Helper
    print("\n--- Example 8: Validation Helper ---")

    def validate_post(response):
        """Validate a post response."""
        assert response.ok, f"Request failed: {response.status}"

        data = response.json()
        required_fields = ["id", "title", "body", "userId"]

        for field in required_fields:
            assert field in data, f"Missing field: {field}"

        assert isinstance(data["id"], int), "id must be integer"
        assert isinstance(data["title"], str), "title must be string"
        assert len(data["title"]) > 0, "title must not be empty"

        return data

    response = api.get("/posts/1")
    post = validate_post(response)
    print(f"  ✓ Post validated: {post['title'][:30]}...")

    api.dispose()

    print("\n=== Demo Complete ===")
    print("\nResponse properties:")
    print("  response.status - HTTP status code")
    print("  response.status_text - Status text ('OK', etc)")
    print("  response.ok - True if 200-299")
    print("  response.headers - Dict of headers")
    print("  response.json() - Parsed JSON")
    print("  response.text() - Raw text")
    print("  response.body() - Raw bytes")
