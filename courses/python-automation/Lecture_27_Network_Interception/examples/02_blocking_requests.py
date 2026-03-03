"""Example 2: Blocking Requests

Demonstrates how to block specific requests to speed up tests
or simulate unavailable resources.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)

    print("=== Blocking Requests Demo ===\n")

    blocked_count = 0

    # EXAMPLE 1: Load page normally first
    print("--- Example 1: Normal page load ---")
    context1 = browser.new_context()
    page1 = context1.new_page()

    resources_loaded = {"images": 0, "scripts": 0, "stylesheets": 0}

    def count_resources(response):
        req = response.request
        if req.resource_type == "image":
            resources_loaded["images"] += 1
        elif req.resource_type == "script":
            resources_loaded["scripts"] += 1
        elif req.resource_type == "stylesheet":
            resources_loaded["stylesheets"] += 1

    page1.on("response", count_resources)
    page1.goto("https://the-internet.herokuapp.com/")

    print(f"Resources loaded:")
    print(f"  Images: {resources_loaded['images']}")
    print(f"  Scripts: {resources_loaded['scripts']}")
    print(f"  Stylesheets: {resources_loaded['stylesheets']}")

    context1.close()

    # EXAMPLE 2: Block images
    print("\n--- Example 2: Blocking images ---")
    context2 = browser.new_context()
    page2 = context2.new_page()

    def block_images(route):
        global blocked_count
        blocked_count += 1
        print(f"  Blocked image: {route.request.url[:50]}...")
        route.abort()

    # Block common image formats
    page2.route("**/*.{png,jpg,jpeg,gif,svg,ico,webp}", block_images)

    page2.goto("https://the-internet.herokuapp.com/")
    print(f"Total images blocked: {blocked_count}")

    context2.close()

    # EXAMPLE 3: Block by resource type
    print("\n--- Example 3: Block by resource type ---")
    context3 = browser.new_context()
    page3 = context3.new_page()

    blocked_types = {"image": 0, "stylesheet": 0, "font": 0}

    def block_by_type(route):
        resource_type = route.request.resource_type
        if resource_type in ["image", "stylesheet", "font"]:
            blocked_types[resource_type] = blocked_types.get(resource_type, 0) + 1
            route.abort()
        else:
            route.continue_()

    page3.route("**/*", block_by_type)

    page3.goto("https://the-internet.herokuapp.com/")
    print(f"Blocked by type:")
    for rtype, count in blocked_types.items():
        print(f"  {rtype}: {count}")

    context3.close()

    # EXAMPLE 4: Block specific domains
    print("\n--- Example 4: Block specific domains ---")
    context4 = browser.new_context()
    page4 = context4.new_page()

    # Block analytics/tracking (example domains)
    blocked_domains = []

    def block_domains(route):
        url = route.request.url
        blocked_patterns = ["google-analytics", "facebook", "twitter", "ads"]
        for pattern in blocked_patterns:
            if pattern in url.lower():
                blocked_domains.append(url)
                print(f"  Blocked: {url[:60]}...")
                route.abort()
                return
        route.continue_()

    page4.route("**/*", block_domains)

    page4.goto("https://the-internet.herokuapp.com/")
    print(f"Blocked {len(blocked_domains)} tracking requests")

    context4.close()

    # EXAMPLE 5: Simulate network failure
    print("\n--- Example 5: Simulate network failure ---")
    context5 = browser.new_context()
    page5 = context5.new_page()

    def simulate_failure(route):
        if "dynamic_loading" in route.request.url:
            print(f"  Simulating failure for: {route.request.url}")
            route.abort("failed")
        else:
            route.continue_()

    page5.route("**/*", simulate_failure)

    page5.on("requestfailed", lambda req: print(f"  Request failed: {req.url[:50]}"))

    try:
        page5.goto("https://the-internet.herokuapp.com/dynamic_loading/1", timeout=5000)
    except Exception as e:
        print(f"  Expected error: Page failed to load")

    context5.close()

    print("\n=== Demo Complete ===")
    print("\nBlocking benefits:")
    print("  - Faster test execution")
    print("  - Reduced bandwidth usage")
    print("  - Isolated testing (no external dependencies)")
    print("  - Simulate offline/error scenarios")

    browser.close()
