"""
Lecture 8 - Example 5: Logging for Debugging
============================================
Learn to use Python's logging module for better debugging.
"""

import logging
from pathlib import Path
from datetime import datetime

print("=" * 60)
print("EXAMPLE 5: LOGGING FOR DEBUGGING")
print("=" * 60)
print()


# 1. Basic Logging Setup
# ======================
print("1. Basic Logging")
print("-" * 40)

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
print()


# 2. Logging Levels
# =================
print("2. Logging Levels")
print("-" * 40)
print("""
Logging Levels (from lowest to highest):
- DEBUG (10): Detailed information for diagnosing problems
- INFO (20): General informational messages
- WARNING (30): Warning messages (something unexpected)
- ERROR (40): Error messages (something failed)
- CRITICAL (50): Critical messages (serious error)

Only messages at or above the configured level are shown.
""")


# 3. Logging to File
# ==================
print("3. Logging to File")
print("-" * 40)

# Create logs directory
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Configure file logging
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.DEBUG)

# Create file handler
log_file = log_dir / "test_execution.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)

# Add handler to logger
file_logger.addHandler(file_handler)

# Log messages
file_logger.info("Test suite started")
file_logger.debug("Loading test configuration")
file_logger.warning("Test data file not found, using defaults")
file_logger.error("Test failed: Element not found")
file_logger.info("Test suite completed")

print(f"✅ Log file created: {log_file}")
print()


# 4. Logging in Functions
# =======================
print("4. Logging in Functions")
print("-" * 40)

# Create a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

def login_user(username, password):
    """Login user with logging."""
    logger.info(f"Attempting login for user: {username}")
    logger.debug(f"Username length: {len(username)}")

    if not username:
        logger.error("Login failed: Username is empty")
        return False

    if not password:
        logger.error("Login failed: Password is empty")
        return False

    if len(password) < 6:
        logger.warning(f"Weak password for user: {username}")

    logger.info(f"Login successful for user: {username}")
    return True

login_user("testuser", "password123")
login_user("", "password")
login_user("user", "pass")
print()


# 5. Logging Exceptions
# =====================
print("5. Logging Exceptions")
print("-" * 40)

def divide_with_logging(a, b):
    """Divide numbers with exception logging."""
    try:
        logger.info(f"Dividing {a} by {b}")
        result = a / b
        logger.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero: {a} / {b}")
        logger.exception("Full exception details:")  # Logs with traceback
        return None
    except Exception as e:
        logger.critical(f"Unexpected error: {type(e).__name__}: {e}")
        logger.exception("Full traceback:")
        raise

divide_with_logging(10, 2)
divide_with_logging(10, 0)
print()


# 6. Custom Log Levels
# ====================
print("6. Custom Log Levels")
print("-" * 40)

# Create custom logger for tests
test_logger = logging.getLogger('TestLogger')
test_logger.setLevel(logging.DEBUG)

# Add handler
test_handler = logging.StreamHandler()
test_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
test_logger.addHandler(test_handler)

def run_test(test_name):
    """Run a test with detailed logging."""
    test_logger.info(f"=" * 50)
    test_logger.info(f"Running test: {test_name}")
    test_logger.debug(f"Test started at: {datetime.now()}")

    try:
        # Simulate test steps
        test_logger.debug("Step 1: Opening browser")
        test_logger.debug("Step 2: Navigating to login page")
        test_logger.debug("Step 3: Entering credentials")
        test_logger.info("Test passed!")

    except Exception as e:
        test_logger.error(f"Test failed: {e}")
        test_logger.exception("Error details:")

    test_logger.debug(f"Test finished at: {datetime.now()}")
    test_logger.info(f"=" * 50)

run_test("test_login")
print()


# 7. Structured Logging for Automation
# ====================================
print("7. Structured Logging for Automation")
print("-" * 40)

class TestLogger:
    """Custom logger for test automation."""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # File handler
        log_file = log_dir / f"{name}.log"
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)

        # Console handler (less verbose)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatters
        file_format = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_format = logging.Formatter('%(levelname)s: %(message)s')

        file_handler.setFormatter(file_format)
        console_handler.setFormatter(console_format)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def test_start(self, test_name):
        """Log test start."""
        self.logger.info(f"🚀 TEST START: {test_name}")

    def test_step(self, step_description):
        """Log test step."""
        self.logger.info(f"  ▸ {step_description}")

    def test_pass(self, test_name):
        """Log test pass."""
        self.logger.info(f"✅ TEST PASSED: {test_name}")

    def test_fail(self, test_name, error):
        """Log test failure."""
        self.logger.error(f"❌ TEST FAILED: {test_name}")
        self.logger.error(f"   Error: {error}")

    def debug(self, message):
        """Log debug message."""
        self.logger.debug(message)

# Use the custom logger
test_log = TestLogger("login_tests")

test_log.test_start("test_valid_login")
test_log.test_step("Open login page")
test_log.debug("Page URL: https://example.com/login")
test_log.test_step("Enter username: testuser")
test_log.test_step("Enter password")
test_log.test_step("Click login button")
test_log.debug("Waiting for redirect...")
test_log.test_pass("test_valid_login")

print()

test_log.test_start("test_invalid_login")
test_log.test_step("Open login page")
test_log.test_step("Enter invalid credentials")
test_log.test_step("Click login button")
test_log.test_fail("test_invalid_login", "Expected error message not shown")
print()


# 8. Conditional Logging
# ======================
print("8. Conditional Logging")
print("-" * 40)

DEBUG_MODE = True  # Toggle this in your tests

def conditional_log(message, level="info"):
    """Log only if DEBUG_MODE is enabled."""
    if DEBUG_MODE:
        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)

conditional_log("This will be logged", "info")
conditional_log("Debug information: variable value = 42", "debug")

DEBUG_MODE = False
conditional_log("This will not be logged", "info")
print()


# 9. Performance Logging
# ======================
print("9. Performance Logging")
print("-" * 40)

import time

def log_execution_time(func):
    """Decorator to log function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Starting {func.__name__}")

        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"Completed {func.__name__} in {execution_time:.2f}s")
            return result

        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(
                f"Failed {func.__name__} after {execution_time:.2f}s: {e}"
            )
            raise

    return wrapper

@log_execution_time
def load_test_data():
    """Simulate loading test data."""
    time.sleep(0.5)  # Simulate slow operation
    return {"users": 100, "products": 500}

@log_execution_time
def run_slow_test():
    """Simulate a slow test."""
    time.sleep(1)
    return "Test completed"

load_test_data()
run_slow_test()
print()


# 10. Best Practices
# ==================
print("10. Logging Best Practices")
print("-" * 40)
print("""
✅ DO:
1. Use appropriate log levels:
   - DEBUG: Detailed diagnostic info
   - INFO: General progress messages
   - WARNING: Something unexpected but not an error
   - ERROR: Something failed
   - CRITICAL: Serious failure

2. Include context in log messages:
   - What operation was being performed
   - What data was being processed
   - What the expected vs actual result was

3. Use structured logging:
   - Timestamp
   - Log level
   - Message
   - Additional context (user, test, etc.)

4. Log to both file and console:
   - Console: High-level info for immediate feedback
   - File: Detailed debug info for later analysis

5. Use logger names to organize logs:
   - __name__ for module-level loggers
   - Custom names for specific components

❌ DON'T:
1. Log sensitive information (passwords, tokens)
2. Log too much (noise makes debugging harder)
3. Use print() instead of logging in production
4. Forget to configure log rotation for long-running tests
5. Log without context (just "Error occurred")

💡 For Test Automation:
- Log test start/end
- Log each major test step
- Log failures with full context
- Log performance metrics
- Keep separate log files per test suite
""")


print("=" * 60)
print("Key Takeaways:")
print("- Use logging instead of print for production code")
print("- Choose appropriate log levels")
print("- Include context in log messages")
print("- Log to both file and console")
print("- Review logs when debugging test failures")
print("=" * 60)
