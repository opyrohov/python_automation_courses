"""Example 4: Complete CRUD Operations

Demonstrates a complete Create, Read, Update, Delete workflow.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("=== CRUD Operations Demo ===\n")

    api = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # Note: jsonplaceholder.typicode.com is a fake API
    # It accepts requests but doesn't actually persist data

    print("Using JSONPlaceholder API (fake REST API for testing)")
    print("=" * 50)

    # CREATE - POST
    print("\n1. CREATE (POST)")
    print("-" * 30)

    new_post = {
        "title": "My Test Post",
        "body": "This is the content of my test post created via API.",
        "userId": 1
    }

    response = api.post("/posts", data=new_post)

    print(f"POST /posts")
    print(f"Request body: {new_post}")
    print(f"Status: {response.status} {response.status_text}")

    created_post = response.json()
    post_id = created_post.get("id", 101)  # JSONPlaceholder returns 101 for new posts

    print(f"Response: {created_post}")
    print(f"✓ Created post with ID: {post_id}")

    # READ - GET
    print("\n2. READ (GET)")
    print("-" * 30)

    # Read single item
    response = api.get(f"/posts/{post_id}")
    print(f"GET /posts/{post_id}")
    print(f"Status: {response.status}")

    # Since JSONPlaceholder doesn't persist, we'll read an existing post
    response = api.get("/posts/1")
    post = response.json()
    print(f"\nActual data from /posts/1:")
    print(f"  ID: {post['id']}")
    print(f"  Title: {post['title'][:40]}...")
    print(f"  User ID: {post['userId']}")

    # Read with filters
    print(f"\nGET /posts?userId=1&_limit=3")
    response = api.get("/posts", params={"userId": 1, "_limit": 3})
    posts = response.json()
    print(f"Found {len(posts)} posts by user 1")
    for p_item in posts:
        print(f"  - [{p_item['id']}] {p_item['title'][:30]}...")

    # UPDATE - PUT (full update)
    print("\n3. UPDATE - PUT (Full Replace)")
    print("-" * 30)

    updated_post = {
        "id": 1,
        "title": "Completely Updated Title",
        "body": "This body has been completely replaced.",
        "userId": 1
    }

    response = api.put("/posts/1", data=updated_post)
    print(f"PUT /posts/1")
    print(f"Request body: {updated_post}")
    print(f"Status: {response.status}")

    result = response.json()
    print(f"Response: {result}")
    print(f"✓ Post fully updated")

    # UPDATE - PATCH (partial update)
    print("\n4. UPDATE - PATCH (Partial Update)")
    print("-" * 30)

    partial_update = {
        "title": "Only Title Changed"
    }

    response = api.patch("/posts/1", data=partial_update)
    print(f"PATCH /posts/1")
    print(f"Request body: {partial_update}")
    print(f"Status: {response.status}")

    result = response.json()
    print(f"Response: {result}")
    print(f"✓ Post partially updated (only title)")

    # DELETE
    print("\n5. DELETE")
    print("-" * 30)

    response = api.delete("/posts/1")
    print(f"DELETE /posts/1")
    print(f"Status: {response.status}")
    print(f"OK: {response.ok}")
    print(f"✓ Post deleted")

    # Verify deletion (in real API, this would return 404)
    print("\nVerifying deletion...")
    response = api.get("/posts/1")
    print(f"GET /posts/1 after delete: Status {response.status}")
    print("(JSONPlaceholder still returns 200 as it's a fake API)")

    # BONUS: Batch operations
    print("\n6. BONUS: Multiple Operations")
    print("-" * 30)

    # Get all posts, count, and get specific ones
    response = api.get("/posts")
    all_posts = response.json()
    print(f"Total posts: {len(all_posts)}")

    # Get comments for a post
    response = api.get("/posts/1/comments")
    comments = response.json()
    print(f"Comments on post 1: {len(comments)}")

    # Get user's posts
    response = api.get("/users/1/posts")
    user_posts = response.json()
    print(f"Posts by user 1: {len(user_posts)}")

    api.dispose()

    print("\n" + "=" * 50)
    print("=== CRUD Demo Complete ===")
    print("\nHTTP Methods:")
    print("  CREATE -> POST   /resource")
    print("  READ   -> GET    /resource or /resource/{id}")
    print("  UPDATE -> PUT    /resource/{id} (full)")
    print("  UPDATE -> PATCH  /resource/{id} (partial)")
    print("  DELETE -> DELETE /resource/{id}")
