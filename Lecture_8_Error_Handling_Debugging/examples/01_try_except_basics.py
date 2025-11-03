"""
Lecture 8 - Example 1: Try/Except Basics
=========================================
Learn the fundamentals of exception handling in Python.
"""

print("=" * 60)
print("EXAMPLE 1: TRY/EXCEPT BASICS")
print("=" * 60)
print()


# 1. Basic Try/Except
# ===================
print("1. Basic Try/Except")
print("-" * 40)

# Without error handling - This would crash!
# result = 10 / 0  # ZeroDivisionError

# With error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")
    result = None

print(f"Result: {result}")
print()


# 2. Catching Any Exception
# =========================
print("2. Catching Any Exception")
print("-" * 40)

try:
    # This will cause an error
    number = int("not a number")
except Exception as e:
    print(f"❌ An error occurred: {e}")
    print(f"   Error type: {type(e).__name__}")
print()


# 3. Multiple Except Blocks
# =========================
print("3. Multiple Except Blocks")
print("-" * 40)

def safe_divide(a, b):
    """Divide two numbers with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
        return None
    except TypeError:
        print("❌ Please provide numbers only")
        return None

# Test different scenarios
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")
print()


# 4. Try/Except/Else
# ==================
print("4. Try/Except/Else")
print("-" * 40)

def process_number(num_str):
    """Convert string to number and process it."""
    try:
        number = int(num_str)
    except ValueError:
        print(f"❌ '{num_str}' is not a valid number")
    else:
        # Runs only if no exception occurred
        print(f"✅ Successfully converted: {number}")
        print(f"   Doubled: {number * 2}")

process_number("42")
process_number("abc")
print()


# 5. Try/Except/Finally
# =====================
print("5. Try/Except/Finally")
print("-" * 40)

def read_file_safe(filename):
    """Read file with proper cleanup."""
    file = None
    try:
        print(f"📖 Opening file: {filename}")
        file = open(filename, 'r')
        content = file.read()
        print(f"✅ File read successfully")
        return content
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return None
    finally:
        # Always runs, even if error occurred
        if file:
            file.close()
            print("📕 File closed")
        print("🏁 Cleanup complete")

# Test with non-existent file
result = read_file_safe("nonexistent.txt")
print()


# 6. Getting Error Details
# ========================
print("6. Getting Error Details")
print("-" * 40)

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except Exception as error:
    print(f"❌ Error occurred!")
    print(f"   Type: {type(error).__name__}")
    print(f"   Message: {str(error)}")
    print(f"   Args: {error.args}")
print()


# 7. Nested Try/Except
# ====================
print("7. Nested Try/Except")
print("-" * 40)

def process_user_data(data):
    """Process user data with multiple error checks."""
    try:
        # First, try to access the data
        user = data['user']
        print(f"✅ Found user: {user}")

        try:
            # Then try to convert age
            age = int(data['age'])
            print(f"✅ Age: {age}")

            if age < 0:
                raise ValueError("Age cannot be negative")

        except ValueError as e:
            print(f"❌ Invalid age: {e}")

    except KeyError as e:
        print(f"❌ Missing required field: {e}")

# Test different scenarios
print("Test 1: Valid data")
process_user_data({'user': 'Alice', 'age': '25'})
print()

print("Test 2: Invalid age")
process_user_data({'user': 'Bob', 'age': 'twenty'})
print()

print("Test 3: Missing field")
process_user_data({'user': 'Charlie'})
print()


# 8. Automation Example: Safe Element Access
# ==========================================
print("8. Automation Example: Safe Element Access")
print("-" * 40)

def get_element_text(elements, index):
    """Safely get text from element list."""
    try:
        element = elements[index]
        # Simulate getting text
        text = element['text']
        print(f"✅ Element {index}: {text}")
        return text
    except IndexError:
        print(f"❌ No element at index {index}")
        return None
    except KeyError:
        print(f"❌ Element has no 'text' property")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Simulate page elements
page_elements = [
    {'text': 'Home'},
    {'text': 'About'},
    {'text': 'Contact'}
]

get_element_text(page_elements, 0)  # Valid
get_element_text(page_elements, 10)  # Index error
get_element_text([{'name': 'Test'}], 0)  # Key error
print()


# 9. Re-raising Exceptions
# ========================
print("9. Re-raising Exceptions")
print("-" * 40)

def validate_and_process(value):
    """Validate input and process it."""
    try:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        if value < 0:
            raise ValueError("Value must be positive")

        print(f"✅ Processing value: {value}")
        return value * 2

    except (TypeError, ValueError) as e:
        print(f"❌ Validation failed: {e}")
        # Re-raise the exception for caller to handle
        raise

try:
    validate_and_process(10)
    validate_and_process(-5)
except ValueError as e:
    print(f"💡 Caught re-raised exception: {e}")
print()


# 10. Best Practices Summary
# ==========================
print("10. Best Practices Summary")
print("-" * 40)
print("""
✅ DO:
- Catch specific exceptions when possible
- Use finally for cleanup code
- Log or print error details for debugging
- Re-raise exceptions if you can't handle them
- Use else block for code that runs on success

❌ DON'T:
- Use bare 'except:' without specifying exception type
- Catch exceptions you can't handle properly
- Hide errors silently
- Ignore error messages
- Use exceptions for control flow
""")


print("=" * 60)
print("Key Takeaways:")
print("- try/except prevents crashes from errors")
print("- Catch specific exceptions for better control")
print("- Use finally for cleanup (closing files, etc.)")
print("- Always handle errors meaningfully")
print("=" * 60)
