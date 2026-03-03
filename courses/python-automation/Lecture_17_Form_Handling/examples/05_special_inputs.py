"""Example 5: Special Inputs - Date Pickers, Range Sliders, Color Pickers"""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    # Demo page with various input types
    page.set_content("""
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; padding: 40px; background: #f5f5f5; }
                .form-group { margin: 20px 0; padding: 15px; background: white; border-radius: 8px; }
                label { display: block; margin-bottom: 8px; font-weight: bold; color: #333; }
                input { padding: 8px; font-size: 16px; }
                input[type="range"] { width: 300px; }
                .value-display { margin-left: 10px; color: #667eea; font-weight: bold; }
                h1 { color: #667eea; }
            </style>
        </head>
        <body>
            <h1>Special Input Types Demo</h1>

            <div class="form-group">
                <label for="birthday">Date Picker:</label>
                <input type="date" id="birthday" name="birthday">
            </div>

            <div class="form-group">
                <label for="meeting-time">DateTime Local:</label>
                <input type="datetime-local" id="meeting-time" name="meeting-time">
            </div>

            <div class="form-group">
                <label for="volume">Range Slider (Volume):</label>
                <input type="range" id="volume" name="volume" min="0" max="100" value="50">
                <span class="value-display" id="volume-value">50</span>
            </div>

            <div class="form-group">
                <label for="price">Range Slider (Price):</label>
                <input type="range" id="price" name="price" min="0" max="1000" step="50" value="500">
                <span class="value-display" id="price-value">$500</span>
            </div>

            <div class="form-group">
                <label for="color">Color Picker:</label>
                <input type="color" id="color" name="color" value="#667eea">
            </div>

            <div class="form-group">
                <label for="week">Week Picker:</label>
                <input type="week" id="week" name="week">
            </div>

            <div class="form-group">
                <label for="month">Month Picker:</label>
                <input type="month" id="month" name="month">
            </div>

            <script>
                document.getElementById('volume').addEventListener('input', function() {
                    document.getElementById('volume-value').textContent = this.value;
                });
                document.getElementById('price').addEventListener('input', function() {
                    document.getElementById('price-value').textContent = '$' + this.value;
                });
            </script>
        </body>
        </html>
    """)
    time.sleep(1)

    # === DATE PICKER ===
    print("=== Date Picker ===")
    # Method 1: Using fill() with date string (YYYY-MM-DD format)
    page.locator("#birthday").fill("1990-06-15")
    print(f"Birthday set to: {page.locator('#birthday').input_value()}")
    time.sleep(0.5)

    # === DATETIME-LOCAL ===
    print("\n=== DateTime Local ===")
    # Format: YYYY-MM-DDTHH:MM
    page.locator("#meeting-time").fill("2024-12-25T14:30")
    print(f"Meeting time set to: {page.locator('#meeting-time').input_value()}")
    time.sleep(0.5)

    # === RANGE SLIDER ===
    print("\n=== Range Slider ===")
    # Method 1: Using fill() - sets value directly
    page.locator("#volume").fill("75")
    print(f"Volume set to: {page.locator('#volume').input_value()}")
    time.sleep(0.5)

    # Method 2: Using evaluate() for more control
    page.locator("#price").evaluate("""element => {
        element.value = 750;
        element.dispatchEvent(new Event('input', { bubbles: true }));
    }""")
    print(f"Price set to: {page.locator('#price').input_value()}")
    time.sleep(0.5)

    # === COLOR PICKER ===
    print("\n=== Color Picker ===")
    # Using fill() with hex color
    page.locator("#color").fill("#ff5733")
    print(f"Color set to: {page.locator('#color').input_value()}")
    time.sleep(0.5)

    # === WEEK PICKER ===
    print("\n=== Week Picker ===")
    # Format: YYYY-Www (e.g., 2024-W52)
    page.locator("#week").fill("2024-W51")
    print(f"Week set to: {page.locator('#week').input_value()}")
    time.sleep(0.5)

    # === MONTH PICKER ===
    print("\n=== Month Picker ===")
    # Format: YYYY-MM
    page.locator("#month").fill("2024-12")
    print(f"Month set to: {page.locator('#month').input_value()}")
    time.sleep(1)

    print("\n✓ All special input examples complete!")
    input("Press Enter to close...")
    browser.close()
