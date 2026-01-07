"""Example 2: Working with Nested iframes"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Nested iframes Demo ===\n")

    # Example 1: Nested frames on the-internet.herokuapp.com
    print("1. Accessing nested frames on herokuapp...")
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # This page has a complex nested frame structure:
    # - frame-top (contains left, middle, right frames)
    # - frame-bottom

    # Access the top frame
    top_frame = page.frame_locator("frame[name='frame-top']")
    print("   ✓ Accessed top frame")

    # Access middle frame inside top frame (nested!)
    middle_frame = top_frame.frame_locator("frame[name='frame-middle']")
    print("   ✓ Accessed middle frame (nested inside top)")

    # Get content from nested frame
    content = middle_frame.locator("#content")
    if content.count() > 0:
        text = content.text_content()
        print(f"   ✓ Content in middle frame: '{text}'")

    # Access left frame inside top frame
    left_frame = top_frame.frame_locator("frame[name='frame-left']")
    left_content = left_frame.locator("body")
    if left_content.count() > 0:
        print(f"   ✓ Content in left frame: '{left_content.text_content().strip()}'")

    # Access right frame inside top frame
    right_frame = top_frame.frame_locator("frame[name='frame-right']")
    right_content = right_frame.locator("body")
    if right_content.count() > 0:
        print(f"   ✓ Content in right frame: '{right_content.text_content().strip()}'")

    # Access bottom frame (sibling of top, not nested)
    bottom_frame = page.frame_locator("frame[name='frame-bottom']")
    bottom_content = bottom_frame.locator("body")
    if bottom_content.count() > 0:
        print(f"   ✓ Content in bottom frame: '{bottom_content.text_content().strip()}'")

    # Example 2: One-liner for deeply nested access
    print("\n2. One-liner access to nested frame...")

    # Navigate fresh
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # Chain frame_locator calls in one line
    middle_text = (page
        .frame_locator("frame[name='frame-top']")
        .frame_locator("frame[name='frame-middle']")
        .locator("#content"))

    expect(middle_text).to_be_visible()
    print("   ✓ Accessed nested frame with chained frame_locator()")

    # Example 3: Using frame() API for frame properties
    print("\n3. Exploring frame structure with frame() API...")

    # Get all frames
    all_frames = page.frames
    print(f"   Total frames on page: {len(all_frames)}")

    for frame in all_frames:
        name = frame.name if frame.name else "(unnamed)"
        url = frame.url[:50] if frame.url else "(no url)"
        parent = frame.parent_frame
        parent_name = parent.name if parent and parent.name else "(main or unnamed)"
        print(f"   - Frame '{name}' | Parent: '{parent_name}'")

    # Example 4: Verify frame hierarchy
    print("\n4. Verifying frame hierarchy...")

    # Get specific frame by name
    top = page.frame("frame-top")
    if top:
        print(f"   ✓ Top frame URL contains: ...{top.url[-30:]}")

        # Check child frames of top
        children = top.child_frames
        print(f"   ✓ Top frame has {len(children)} child frames")
        for child in children:
            print(f"     - Child frame: {child.name}")

    print("\n=== Demo Complete ===")
    browser.close()
