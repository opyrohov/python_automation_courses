"""Example 1: Basic API Requests

Demonstrates GET, POST, PUT, PATCH, DELETE requests using Playwright's
request context - no browser needed!
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("=== Basic API Requests Demo ===\n")

    # Create API request context
    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    print("1. Created API context for jsonplaceholder.typicode.com\n")

    # GET request - fetch all posts
    print("--- GET Request ---")
    response = api.get("/posts")
    print(f"GET /posts")
    print(f"  Status: {response.status}")
    print(f"  OK: {response.ok}")
    posts = response.json()
    print(f"  Total posts: {len(posts)}")
    print(f"  First post: {posts[0]['title'][:50]}...")

    # GET with query parameters
    print("\n--- GET with Parameters ---")
    response = api.get("/posts", params={"userId": 1})
    print(f"GET /posts?userId=1")
    print(f"  Status: {response.status}")
    user_posts = response.json()
    print(f"  Posts by user 1: {len(user_posts)}")

    # GET single item
    print("\n--- GET Single Item ---")
    response = api.get("/posts/1")
    print(f"GET /posts/1")
    print(f"  Status: {response.status}")
    post = response.json()
    print(f"  Title: {post['title'][:50]}...")
    print(f"  Body: {post['body'][:50]}...")

    # POST request - create new item
    print("\n--- POST Request ---")
    new_post = {
        "title": "My New Post",
        "body": "This is the content of my new post.",
        "userId": 1
    }
    response = api.post("/posts", data=new_post)
    print(f"POST /posts")
    print(f"  Status: {response.status}")
    print(f"  Status Text: {response.status_text}")
    created = response.json()
    print(f"  Created ID: {created.get('id')}")
    print(f"  Title: {created.get('title')}")

    # PUT request - full update
    print("\n--- PUT Request ---")
    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "Completely updated body content.",
        "userId": 1
    }
    response = api.put("/posts/1", data=updated_post)
    print(f"PUT /posts/1")
    print(f"  Status: {response.status}")
    result = response.json()
    print(f"  Updated title: {result.get('title')}")

    # PATCH request - partial update
    print("\n--- PATCH Request ---")
    partial_update = {"title": "Patched Title Only"}
    response = api.patch("/posts/1", data=partial_update)
    print(f"PATCH /posts/1")
    print(f"  Status: {response.status}")
    result = response.json()
    print(f"  Patched title: {result.get('title')}")

    # DELETE request
    print("\n--- DELETE Request ---")
    response = api.delete("/posts/1")
    print(f"DELETE /posts/1")
    print(f"  Status: {response.status}")
    print(f"  OK: {response.ok}")

    # Cleanup
    api.dispose()
    print("\n2. API context disposed")

    print("\n=== Demo Complete ===")
    print("\nKey methods:")
    print("  api.get(url, params={}, headers={})")
    print("  api.post(url, data={})")
    print("  api.put(url, data={})")
    print("  api.patch(url, data={})")
    print("  api.delete(url)")
