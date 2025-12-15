"""Exercise 4: File Upload - Practice uploading files"""
from playwright.sync_api import sync_playwright
import os

def file_upload_exercise():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Create a test file to upload
        test_file_path = os.path.join(os.path.dirname(__file__), "test_upload.txt")
        with open(test_file_path, "w") as f:
            f.write("This is a test file for upload exercise.\nCreated by Playwright automation.")

        # Navigate to contact form with file upload
        page.goto("https://www.automationexercise.com/contact_us")

        # Fill out the contact form first
        page.get_by_placeholder("Name").fill("Test User")
        page.get_by_placeholder("Email", exact=False).first.fill("test@example.com")
        page.get_by_placeholder("Subject").fill("Test Subject")
        page.locator("#message").fill("This is a test message with file attachment.")

        # TODO 1: Upload the test file
        # Hint: Use locator("input[name='upload_file']").set_input_files(test_file_path)
        # page.YOUR_CODE_HERE

        # TODO 2: Click the Submit button
        # Hint: Use get_by_role("button", name="Submit")
        # page.YOUR_CODE_HERE

        # TODO 3: Handle the confirmation dialog (accept it)
        # Note: This site shows a JavaScript alert, you may need to handle it
        # page.on("dialog", lambda dialog: dialog.accept())
        # Or just click OK if there's a button

        print("✓ Exercise 4 complete!")

        # Cleanup: remove test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)
            print("✓ Test file cleaned up")

        input("Press Enter to close...")
        browser.close()

if __name__ == "__main__":
    file_upload_exercise()
