"""
Test helper functions for automation.
This is an example of organizing test utilities in a module.
"""

from datetime import datetime

def log_message(message, level="INFO"):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def format_test_name(test_name):
    """Format test name for display."""
    return f"🧪 TEST: {test_name}"

def create_test_data(username, email, password):
    """Create a test user data dictionary."""
    return {
        "username": username,
        "email": email,
        "password": password,
        "created_at": datetime.now().isoformat()
    }

def calculate_test_duration(start_time, end_time):
    """Calculate test duration in seconds."""
    duration = end_time - start_time
    return duration.total_seconds()

def generate_test_report(passed, failed, skipped=0):
    """Generate a simple test report."""
    total = passed + failed + skipped
    success_rate = (passed / total * 100) if total > 0 else 0

    report = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "success_rate": round(success_rate, 2)
    }
    return report

# Module configuration
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

if __name__ == "__main__":
    # Test the module
    print(format_test_name("Login Test"))
    log_message("Test started", "INFO")
    log_message("Test failed", "ERROR")

    test_data = create_test_data("testuser", "test@example.com", "password123")
    print(f"Test data: {test_data}")

    report = generate_test_report(45, 5, 2)
    print(f"Test report: {report}")
