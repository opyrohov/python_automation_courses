"""
Lecture 11: *args and **kwargs
This file demonstrates how to use *args and **kwargs for flexible function signatures.
"""

# ============================================
# *ARGS - VARIABLE POSITIONAL ARGUMENTS
# ============================================
print("=" * 60)
print("*ARGS - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 60)

# Basic *args example
def sum_numbers(*args):
    """Accept any number of arguments and return their sum"""
    print(f"Received args: {args}")
    print(f"Type of args: {type(args)}")
    return sum(args)

result1 = sum_numbers(1, 2, 3)
print(f"Sum of 1, 2, 3 = {result1}")

result2 = sum_numbers(10, 20, 30, 40, 50)
print(f"Sum of 10, 20, 30, 40, 50 = {result2}")
print()

# *args with iteration
def print_all(*args):
    """Print each argument on a new line"""
    for i, arg in enumerate(args, 1):
        print(f"  Argument {i}: {arg}")

print("Calling print_all with multiple arguments:")
print_all("apple", "banana", "cherry")
print()

# ============================================
# **KWARGS - VARIABLE KEYWORD ARGUMENTS
# ============================================
print("=" * 60)
print("**KWARGS - VARIABLE KEYWORD ARGUMENTS")
print("=" * 60)

# Basic **kwargs example
def print_user_info(**kwargs):
    """Accept any number of keyword arguments"""
    print(f"Received kwargs: {kwargs}")
    print(f"Type of kwargs: {type(kwargs)}")
    print("\nUser Information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_user_info(name="Alice", age=25, city="NYC", occupation="Developer")
print()

# **kwargs with specific processing
def create_profile(**kwargs):
    """Create a user profile with optional fields"""
    profile = {
        "name": kwargs.get("name", "Unknown"),
        "age": kwargs.get("age", 0),
        "email": kwargs.get("email", "no-email@example.com")
    }
    # Add any extra fields
    for key, value in kwargs.items():
        if key not in profile:
            profile[key] = value
    return profile

profile1 = create_profile(name="Bob", age=30, city="LA")
print(f"Profile 1: {profile1}")

profile2 = create_profile(name="Charlie", email="charlie@example.com", country="USA")
print(f"Profile 2: {profile2}")
print()

# ============================================
# COMBINING REGULAR PARAMETERS WITH *ARGS
# ============================================
print("=" * 60)
print("COMBINING REGULAR PARAMETERS WITH *ARGS")
print("=" * 60)

def greet(greeting, *names):
    """
    First parameter is required greeting,
    rest are variable number of names
    """
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
print()

def calculate(operation, *numbers):
    """Perform operation on multiple numbers"""
    if operation == "sum":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        return None

print(f"Sum: {calculate('sum', 1, 2, 3, 4, 5)}")
print(f"Multiply: {calculate('multiply', 2, 3, 4)}")
print()

# ============================================
# COMBINING REGULAR PARAMETERS WITH **KWARGS
# ============================================
print("=" * 60)
print("COMBINING REGULAR PARAMETERS WITH **KWARGS")
print("=" * 60)

def send_email(recipient, subject, **options):
    """
    Send email with required recipient and subject,
    plus optional settings
    """
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print("Options:")
    for key, value in options.items():
        print(f"  {key}: {value}")

send_email(
    "alice@example.com",
    "Meeting Reminder",
    priority="high",
    cc="bob@example.com",
    send_at="2024-01-15 10:00"
)
print()

# ============================================
# COMBINING *ARGS AND **KWARGS
# ============================================
print("=" * 60)
print("COMBINING *ARGS AND **KWARGS")
print("=" * 60)

# Important: Order must be: regular args, *args, **kwargs
def flexible_function(required, *args, **kwargs):
    """
    Demonstrate all three types of parameters together
    """
    print(f"Required parameter: {required}")
    print(f"Additional positional args: {args}")
    print(f"Keyword arguments: {kwargs}")

flexible_function(
    "must_have",
    "extra1",
    "extra2",
    option1="value1",
    option2="value2"
)
print()

# ============================================
# UNPACKING WITH * AND **
# ============================================
print("=" * 60)
print("UNPACKING WITH * AND **")
print("=" * 60)

# Unpacking a list with *
def add_three_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add_three_numbers(*numbers)  # Unpacks list to individual arguments
print(f"Numbers: {numbers}")
print(f"Sum using unpacking: {result}")

# Unpacking a dictionary with **
def create_user(name, age, city):
    return f"{name}, {age} years old, from {city}"

user_data = {"name": "Alice", "age": 25, "city": "NYC"}
user_string = create_user(**user_data)  # Unpacks dict to keyword arguments
print(f"\nUser data: {user_data}")
print(f"User string: {user_string}")
print()

# ============================================
# FORWARDING ARGUMENTS
# ============================================
print("=" * 60)
print("FORWARDING ARGUMENTS")
print("=" * 60)

def logger(func):
    """Wrapper function that logs before calling another function"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with:")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  result: {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(5, 3)
print()

@logger
def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"

create_greeting("Alice", greeting="Hi")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Configuration builder
def build_config(env, **settings):
    """Build configuration with environment and custom settings"""
    config = {
        "environment": env,
        "debug": settings.get("debug", False),
        "port": settings.get("port", 8080),
        "host": settings.get("host", "localhost")
    }
    # Add any additional settings
    for key, value in settings.items():
        if key not in config:
            config[key] = value
    return config

prod_config = build_config("production", debug=False, port=443, ssl=True)
print(f"Production config: {prod_config}")

dev_config = build_config("development", debug=True, hot_reload=True)
print(f"Development config: {dev_config}")
print()

# Example 2: Database query builder
def query_database(table, *columns, **conditions):
    """
    Build a database query
    table: table name
    *columns: columns to select
    **conditions: WHERE conditions
    """
    # Build SELECT clause
    if columns:
        select_clause = ", ".join(columns)
    else:
        select_clause = "*"

    # Build WHERE clause
    where_parts = [f"{key} = '{value}'" for key, value in conditions.items()]
    where_clause = " AND ".join(where_parts) if where_parts else "1=1"

    query = f"SELECT {select_clause} FROM {table} WHERE {where_clause}"
    return query

query1 = query_database("users", "name", "email", age=25, city="NYC")
print(f"Query 1: {query1}")

query2 = query_database("products", status="active")
print(f"Query 2: {query2}")
print()

# Example 3: Test assertion helper
def assert_all(*conditions, message="Assertion failed"):
    """
    Check multiple conditions and print detailed results
    """
    print(f"Checking {len(conditions)} conditions...")
    all_passed = True
    for i, condition in enumerate(conditions, 1):
        if condition:
            print(f"  ✓ Condition {i}: PASS")
        else:
            print(f"  ✗ Condition {i}: FAIL")
            all_passed = False

    if not all_passed:
        print(f"ERROR: {message}")
    return all_passed

# Test the assertion helper
x = 10
result = assert_all(
    x > 5,
    x < 20,
    x % 2 == 0,
    message="Value validation failed"
)
print(f"All assertions passed: {result}")
print()

# ============================================
# BEST PRACTICES
# ============================================
print("=" * 60)
print("BEST PRACTICES")
print("=" * 60)
print("""
1. Parameter Order:
   def func(required, *args, default=value, **kwargs)

2. Use *args when you need variable positional arguments
   - List of items to process
   - Unknown number of values

3. Use **kwargs when you need variable keyword arguments
   - Optional configuration
   - Forwarding to other functions

4. Don't overuse - explicit parameters are often clearer

5. Document what arguments your function expects

6. Use * and ** for unpacking iterables and dictionaries
""")
