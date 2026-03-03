"""
Lecture 9 - Example 5: Practical Class Examples
===============================================
Real-world examples of classes for test automation.
"""

print("=" * 60)
print("EXAMPLE 5: PRACTICAL EXAMPLES")
print("=" * 60)
print()


# 1. Test User Class
# ==================
print("1. Test User Class")
print("-" * 40)

class TestUser:
    """Represents a test user with credentials."""

    def __init__(self, username, password, email, role="user"):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.is_logged_in = False

    def login(self):
        """Simulate user login."""
        self.is_logged_in = True
        print(f"✅ {self.username} logged in")

    def logout(self):
        """Simulate user logout."""
        self.is_logged_in = False
        print(f"👋 {self.username} logged out")

    def has_permission(self, permission):
        """Check if user has permission."""
        permissions = {
            "admin": ["read", "write", "delete"],
            "user": ["read"],
            "moderator": ["read", "write"]
        }
        return permission in permissions.get(self.role, [])

# Create test users
admin = TestUser("admin", "admin123", "admin@example.com", "admin")
regular_user = TestUser("user1", "pass123", "user1@example.com")

admin.login()
print(f"Admin can delete: {admin.has_permission('delete')}")
print(f"Regular user can delete: {regular_user.has_permission('delete')}")
print()


# 2. Browser Class
# ================
print("2. Browser Class")
print("-" * 40)

class Browser:
    """Represents a browser for testing."""

    def __init__(self, browser_type="chromium", headless=False):
        self.browser_type = browser_type
        self.headless = headless
        self.is_open = False
        self.current_url = None

    def open(self):
        """Open the browser."""
        self.is_open = True
        print(f"🌐 Opening {self.browser_type} browser (headless={self.headless})")

    def navigate(self, url):
        """Navigate to a URL."""
        if not self.is_open:
            print("❌ Browser is not open")
            return
        self.current_url = url
        print(f"📍 Navigated to: {url}")

    def close(self):
        """Close the browser."""
        if self.is_open:
            self.is_open = False
            print("🚪 Browser closed")

browser = Browser("chromium", headless=True)
browser.open()
browser.navigate("https://example.com")
browser.close()
print()


# 3. Test Case Class
# ==================
print("3. Test Case Class")
print("-" * 40)

from datetime import datetime

class TestCase:
    """Represents a single test case."""

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.status = "Not Run"
        self.start_time = None
        self.end_time = None
        self.error_message = None

    def start(self):
        """Mark test as started."""
        self.status = "Running"
        self.start_time = datetime.now()
        print(f"▶️  Starting: {self.name}")

    def pass_test(self):
        """Mark test as passed."""
        self.status = "Passed"
        self.end_time = datetime.now()
        print(f"✅ PASSED: {self.name}")

    def fail_test(self, error):
        """Mark test as failed."""
        self.status = "Failed"
        self.end_time = datetime.now()
        self.error_message = error
        print(f"❌ FAILED: {self.name}")
        print(f"   Error: {error}")

    def get_duration(self):
        """Get test duration in seconds."""
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds()
            return round(duration, 2)
        return 0

test = TestCase("test_login", "Verify user can login")
test.start()
# Simulate test execution
import time
time.sleep(0.1)  # Simulate test running
test.pass_test()
print(f"Duration: {test.get_duration()}s")
print()


# 4. API Client Class
# ===================
print("4. API Client Class")
print("-" * 40)

class APIClient:
    """Client for making API requests."""

    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    def get(self, endpoint):
        """Simulate GET request."""
        url = f"{self.base_url}/{endpoint}"
        print(f"GET {url}")
        print(f"Headers: {self.headers}")
        return {"status": 200, "data": "Simulated response"}

    def post(self, endpoint, data):
        """Simulate POST request."""
        url = f"{self.base_url}/{endpoint}"
        print(f"POST {url}")
        print(f"Data: {data}")
        return {"status": 201, "data": "Created"}

api = APIClient("https://api.example.com", "secret-key-123")
api.get("users")
api.post("users", {"name": "Alice", "email": "alice@example.com"})
print()


# 5. Test Data Generator Class
# ============================
print("5. Test Data Generator Class")
print("-" * 40)

import random
import string

class TestDataGenerator:
    """Generate test data for automation."""

    def __init__(self, prefix="test"):
        self.prefix = prefix
        self.counter = 0

    def get_unique_email(self):
        """Generate unique email."""
        self.counter += 1
        return f"{self.prefix}_user{self.counter}@example.com"

    def get_random_username(self, length=8):
        """Generate random username."""
        letters = string.ascii_lowercase
        return self.prefix + '_' + ''.join(random.choice(letters) for _ in range(length))

    def get_random_password(self, length=12):
        """Generate random password."""
        chars = string.ascii_letters + string.digits + "!@#$"
        return ''.join(random.choice(chars) for _ in range(length))

generator = TestDataGenerator("auto")
print(f"Email 1: {generator.get_unique_email()}")
print(f"Email 2: {generator.get_unique_email()}")
print(f"Username: {generator.get_random_username()}")
print(f"Password: {generator.get_random_password()}")
print()


# 6. Screenshot Manager Class
# ===========================
print("6. Screenshot Manager Class")
print("-" * 40)

from pathlib import Path

class ScreenshotManager:
    """Manage test screenshots."""

    def __init__(self, output_dir="screenshots"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.screenshot_count = 0

    def save_screenshot(self, page, test_name):
        """Save a screenshot."""
        self.screenshot_count += 1
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = self.output_dir / filename

        print(f"📸 Saving screenshot: {filepath}")
        # In real code: page.screenshot(path=str(filepath))

        return str(filepath)

    def get_screenshot_count(self):
        """Get total screenshots taken."""
        return self.screenshot_count

screenshot_mgr = ScreenshotManager("test_screenshots")
screenshot_mgr.save_screenshot(None, "test_login")
screenshot_mgr.save_screenshot(None, "test_checkout")
print(f"Total screenshots: {screenshot_mgr.get_screenshot_count()}")
print()


# 7. Configuration Manager Class
# ==============================
print("7. Configuration Manager Class")
print("-" * 40)

class ConfigManager:
    """Manage test configuration."""

    def __init__(self, environment="staging"):
        self.environment = environment
        self.configs = {
            "dev": {"url": "https://dev.example.com", "timeout": 30},
            "staging": {"url": "https://staging.example.com", "timeout": 60},
            "production": {"url": "https://example.com", "timeout": 90}
        }

    def get_url(self):
        """Get URL for current environment."""
        return self.configs[self.environment]["url"]

    def get_timeout(self):
        """Get timeout for current environment."""
        return self.configs[self.environment]["timeout"]

    def switch_environment(self, env):
        """Switch to different environment."""
        if env in self.configs:
            self.environment = env
            print(f"Switched to {env} environment")
        else:
            print(f"Unknown environment: {env}")

config = ConfigManager("staging")
print(f"URL: {config.get_url()}")
print(f"Timeout: {config.get_timeout()}s")
config.switch_environment("production")
print(f"New URL: {config.get_url()}")
print()


# 8. Test Report Class
# ====================
print("8. Test Report Class")
print("-" * 40)

class TestReport:
    """Generate test execution report."""

    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.test_results = []
        self.start_time = datetime.now()

    def add_result(self, test_name, status, duration):
        """Add a test result."""
        self.test_results.append({
            "name": test_name,
            "status": status,
            "duration": duration
        })

    def get_summary(self):
        """Get test summary."""
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r["status"] == "Passed")
        failed = total - passed
        total_duration = sum(r["duration"] for r in self.test_results)

        return {
            "suite": self.suite_name,
            "total": total,
            "passed": passed,
            "failed": failed,
            "duration": total_duration
        }

    def print_report(self):
        """Print formatted report."""
        summary = self.get_summary()
        print(f"\n{'=' * 50}")
        print(f"TEST REPORT: {summary['suite']}")
        print(f"{'=' * 50}")
        for result in self.test_results:
            status_icon = "✅" if result["status"] == "Passed" else "❌"
            print(f"{status_icon} {result['name']}: {result['duration']}s")
        print(f"{'=' * 50}")
        print(f"Total: {summary['total']} | Passed: {summary['passed']} | Failed: {summary['failed']}")
        print(f"Duration: {summary['duration']:.2f}s")
        print(f"{'=' * 50}")

report = TestReport("Regression Tests")
report.add_result("test_login", "Passed", 2.3)
report.add_result("test_signup", "Passed", 3.1)
report.add_result("test_checkout", "Failed", 1.5)
report.print_report()
print()


print("=" * 60)
print("Key Takeaways:")
print("- Classes organize related functionality")
print("- Real-world examples: Users, Browsers, Test Cases")
print("- Classes make code reusable and maintainable")
print("- Perfect for automation utilities")
print("- Combine multiple classes for complex systems")
print("=" * 60)
