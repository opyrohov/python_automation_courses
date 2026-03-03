"""Exercise 1: Basic API Operations

Your task:
1. Create an API request context for https://jsonplaceholder.typicode.com
2. GET all posts and print the count
3. GET a single post (id=1) and print its title
4. POST a new post with title "My Test Post" and body "Test content"
5. Verify the POST response status is 201
6. PUT update the post with id=1 (change title to "Updated Title")
7. DELETE the post with id=1
8. Verify all operations completed successfully

Bonus:
- Add error handling for failed requests
- Create a helper function for common assertions
- Test with query parameters (get posts by userId)

Hints:
- Use p.request.new_context(base_url="...") to create context
- api.get(), api.post(), api.put(), api.delete() for operations
- response.status, response.ok, response.json() for responses
- Don't forget api.dispose() at the end
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("=== Exercise 1: API Basics ===\n")

    # TODO: Create API context
    # api = p.request.new_context(base_url="https://jsonplaceholder.typicode.com")

    # TODO: GET all posts
    # response = api.get("/posts")
    # posts = response.json()
    # print(f"Total posts: {len(posts)}")

    # TODO: GET single post
    # response = api.get("/posts/1")
    # post = response.json()
    # print(f"Post title: {post['title']}")

    # TODO: POST new post
    # response = api.post("/posts", data={
    #     "title": "My Test Post",
    #     "body": "Test content",
    #     "userId": 1
    # })
    # assert response.status == 201
    # print(f"Created post: {response.json()}")

    # TODO: PUT update post
    # response = api.put("/posts/1", data={
    #     "id": 1,
    #     "title": "Updated Title",
    #     "body": "Updated body",
    #     "userId": 1
    # })
    # print(f"Updated: {response.json()}")

    # TODO: DELETE post
    # response = api.delete("/posts/1")
    # print(f"Delete status: {response.status}")

    # TODO: Dispose context
    # api.dispose()

    print("Exercise completed!")
