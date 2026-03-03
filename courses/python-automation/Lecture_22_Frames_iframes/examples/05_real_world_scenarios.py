"""Example 5: Real-World iframe Scenarios"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Real-World iframe Scenarios Demo ===\n")

    # Scenario 1: Rich Text Editor (TinyMCE)
    print("1. Scenario: Rich Text Editor (TinyMCE)...")
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Wait for editor to load
    expect(page.locator("#mce_0_ifr")).to_be_visible()
    print("   ✓ TinyMCE editor loaded")

    # Access the editor iframe
    editor_frame = page.frame_locator("#mce_0_ifr")
    editor_body = editor_frame.locator("#tinymce")

    # Clear and type content
    editor_body.clear()
    editor_body.fill("This is a sample document created with Playwright automation.")
    print("   ✓ Typed content into editor")

    # Select all text using keyboard
    editor_body.press("Control+a")
    print("   ✓ Selected all text")

    # Bold button is on the main page toolbar, not in iframe
    bold_button = page.locator("button[aria-label='Bold']")
    if bold_button.count() > 0:
        bold_button.click()
        print("   ✓ Applied bold formatting")

    # Verify content is still there
    expect(editor_body).to_contain_text("sample document")
    print("   ✓ Content verified in editor")

    # Scenario 2: Nested Frames Navigation
    print("\n2. Scenario: Complex Nested Frame Navigation...")
    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # Navigate through nested structure
    top_frame = page.frame_locator("frame[name='frame-top']")

    # Get text from each section
    sections = ["frame-left", "frame-middle", "frame-right"]
    for section_name in sections:
        section_frame = top_frame.frame_locator(f"frame[name='{section_name}']")
        body = section_frame.locator("body")
        if body.count() > 0:
            text = body.text_content().strip()
            print(f"   ✓ {section_name}: '{text}'")

    # Get bottom frame content
    bottom_frame = page.frame_locator("frame[name='frame-bottom']")
    bottom_text = bottom_frame.locator("body").text_content().strip()
    print(f"   ✓ frame-bottom: '{bottom_text}'")

    # Scenario 3: Simulating Payment Form Interaction
    print("\n3. Scenario: Payment Form Pattern (Simulated)...")
    page.goto("https://the-internet.herokuapp.com/iframe")

    # In real payment scenarios, you'd have:
    # payment_frame = page.frame_locator("iframe[name='payment']")
    # payment_frame.locator("#card-number").fill("4111111111111111")
    # payment_frame.locator("#expiry").fill("12/25")
    # payment_frame.locator("#cvv").fill("123")
    # payment_frame.locator("#submit").click()

    # Demo with available iframe
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")

    # Simulate filling a form-like content
    editor.clear()
    editor.fill("""
Order Details:
- Product: Widget Pro
- Quantity: 2
- Total: $99.98
- Card: **** **** **** 4242

[Payment Processed Successfully]
    """.strip())

    expect(editor).to_contain_text("Payment Processed")
    print("   ✓ Simulated payment form filled")
    print("   ✓ Success message verified")

    # Scenario 4: Handling Multiple Content Types
    print("\n4. Scenario: Multiple iframe Types on Page...")
    page.goto("https://www.w3schools.com/html/html_iframe.asp")

    # Find all iframes and categorize
    iframes = page.locator("iframe").all()
    print(f"   Found {len(iframes)} iframes")

    for i, iframe in enumerate(iframes):
        src = iframe.get_attribute("src") or ""
        title = iframe.get_attribute("title") or ""

        # Categorize by src pattern
        if "youtube" in src.lower() or "video" in src.lower():
            category = "Video"
        elif "ad" in src.lower() or "banner" in src.lower():
            category = "Advertisement"
        elif "w3schools" in src.lower():
            category = "W3Schools Content"
        else:
            category = "Other"

        print(f"   - iframe {i}: {category}")

    # Scenario 5: iframe Error Handling
    print("\n5. Scenario: Robust iframe Error Handling...")

    page.goto("https://the-internet.herokuapp.com/iframe")

    def safely_interact_with_iframe(page, iframe_selector, action_callback):
        """Safely interact with an iframe, handling errors gracefully."""
        try:
            # Check if iframe exists
            iframe_element = page.locator(iframe_selector)
            if iframe_element.count() == 0:
                print(f"   ⚠ iframe '{iframe_selector}' not found")
                return False

            # Wait for it to be visible
            expect(iframe_element).to_be_visible(timeout=5000)

            # Get frame locator and execute action
            frame = page.frame_locator(iframe_selector)
            action_callback(frame)
            return True

        except Exception as e:
            print(f"   ⚠ Error with iframe: {str(e)[:50]}")
            return False

    # Use the safe function
    def fill_editor(frame):
        editor = frame.locator("#tinymce")
        expect(editor).to_be_visible()
        editor.clear()
        editor.fill("Safe interaction completed!")
        print("   ✓ Safe iframe interaction successful")

    safely_interact_with_iframe(page, "#mce_0_ifr", fill_editor)

    # Try with non-existent iframe
    def do_nothing(frame):
        pass

    result = safely_interact_with_iframe(page, "#nonexistent-iframe", do_nothing)
    if not result:
        print("   ✓ Handled missing iframe gracefully")

    # Scenario 6: Frame Info Extraction
    print("\n6. Scenario: Extracting iframe Information...")

    page.goto("https://the-internet.herokuapp.com/nested_frames")

    # Get all frames using the frames API
    all_frames = page.frames

    print(f"   Total frames: {len(all_frames)}")
    print("   Frame hierarchy:")

    for frame in all_frames:
        name = frame.name or "(main)"
        parent = frame.parent_frame
        parent_name = parent.name if parent else "(none)"
        depth = 0

        # Calculate depth
        current = frame
        while current.parent_frame:
            depth += 1
            current = current.parent_frame

        indent = "  " * depth
        print(f"   {indent}└─ {name} (parent: {parent_name})")

    print("\n=== Demo Complete ===")
    browser.close()
