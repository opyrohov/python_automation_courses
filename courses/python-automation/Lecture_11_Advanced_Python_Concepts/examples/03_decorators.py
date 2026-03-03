"""
Lecture 11: Decorators Basics
This file demonstrates how to create and use decorators in Python.
"""

import time
import functools

# ============================================
# WHAT IS A DECORATOR?
# ============================================
print("=" * 60)
print("WHAT IS A DECORATOR?")
print("=" * 60)
print("""
A decorator is a function that takes another function and extends
its behavior without explicitly modifying it.

Key concepts:
- Functions are first-class objects (can be passed around)
- Decorators wrap functions to add functionality
- Use @decorator_name syntax for clean application
""")
print()

# ============================================
# SIMPLE DECORATOR EXAMPLE
# ============================================
print("=" * 60)
print("SIMPLE DECORATOR EXAMPLE")
print("=" * 60)

def simple_decorator(func):
    """A basic decorator that prints before and after function execution"""
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# Apply decorator manually
def say_hello():
    print("Hello, World!")

print("Without decorator:")
say_hello()
print()

print("With decorator (manual application):")
decorated_hello = simple_decorator(say_hello)
decorated_hello()
print()

# Using @ syntax (cleaner way)
@simple_decorator
def say_goodbye():
    print("Goodbye, World!")

print("With @decorator syntax:")
say_goodbye()
print()

# ============================================
# DECORATOR WITH ARGUMENTS
# ============================================
print("=" * 60)
print("DECORATOR WITH ARGUMENTS")
print("=" * 60)

def decorator_with_args(func):
    """Decorator that works with functions that have arguments"""
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with:")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result1 = add(5, 3)
print(f"Final result: {result1}\n")

result2 = greet("Alice", greeting="Hi")
print(f"Final result: {result2}\n")

# ============================================
# TIMING DECORATOR
# ============================================
print("=" * 60)
print("TIMING DECORATOR")
print("=" * 60)

def timer(func):
    """Decorator to measure function execution time"""
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Simulate a slow operation"""
    time.sleep(1)
    return "Done!"

@timer
def fast_function():
    """A fast operation"""
    return sum(range(1000))

print("Testing timing decorator:")
result = slow_function()
print(f"Result: {result}\n")

result = fast_function()
print(f"Result: {result}\n")

# ============================================
# LOGGING DECORATOR
# ============================================
print("=" * 60)
print("LOGGING DECORATOR")
print("=" * 60)

def log_calls(func):
    """Decorator to log function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} completed successfully")
            return result
        except Exception as e:
            print(f"[LOG] {func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper

@log_calls
def divide(a, b):
    return a / b

print("Testing logging decorator:")
result = divide(10, 2)
print(f"Result: {result}\n")

print("Testing with error:")
try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Error was caught and re-raised\n")

# ============================================
# DECORATOR WITH PARAMETERS
# ============================================
print("=" * 60)
print("DECORATOR WITH PARAMETERS")
print("=" * 60)

def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"Execution {i + 1}/{times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet_user(name):
    return f"Hello, {name}!"

print("Testing repeat decorator:")
results = greet_user("Alice")
print(f"All results: {results}\n")

# ============================================
# RETRY DECORATOR (USEFUL FOR TESTING)
# ============================================
print("=" * 60)
print("RETRY DECORATOR")
print("=" * 60)

def retry(max_attempts=3, delay=0.1):
    """
    Decorator to retry a function if it fails
    Useful for flaky tests or network operations
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    attempts += 1
                    result = func(*args, **kwargs)
                    if attempts > 1:
                        print(f"✓ Succeeded on attempt {attempts}")
                    return result
                except Exception as e:
                    if attempts == max_attempts:
                        print(f"✗ Failed after {max_attempts} attempts")
                        raise
                    print(f"✗ Attempt {attempts} failed: {e}")
                    print(f"  Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Simulate a flaky function
attempt_count = 0

@retry(max_attempts=3, delay=0.1)
def flaky_operation():
    """Simulates an operation that fails first 2 times"""
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError(f"Connection failed (attempt {attempt_count})")
    return "Success!"

print("Testing retry decorator:")
result = flaky_operation()
print(f"Final result: {result}\n")

# ============================================
# CHAINING MULTIPLE DECORATORS
# ============================================
print("=" * 60)
print("CHAINING MULTIPLE DECORATORS")
print("=" * 60)

def uppercase(func):
    """Convert result to uppercase"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def add_exclamation(func):
    """Add exclamation marks to result"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!!!"
    return wrapper

# Decorators are applied bottom to top
@add_exclamation
@uppercase
def generate_message(name):
    return f"hello, {name}"

print("Testing chained decorators:")
message = generate_message("Alice")
print(f"Result: {message}\n")

# ============================================
# PRACTICAL EXAMPLE: CACHE DECORATOR
# ============================================
print("=" * 60)
print("CACHE DECORATOR")
print("=" * 60)

def cache(func):
    """Simple caching decorator"""
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"[CACHE HIT] Returning cached result for {args}")
            return cached_results[args]
        print(f"[CACHE MISS] Computing result for {args}")
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def expensive_calculation(n):
    """Simulate expensive calculation"""
    time.sleep(0.5)  # Simulate slow operation
    return n * n

print("Testing cache decorator:")
print(f"Result: {expensive_calculation(5)}")
print(f"Result: {expensive_calculation(5)}")  # Should be cached
print(f"Result: {expensive_calculation(10)}")
print(f"Result: {expensive_calculation(10)}")  # Should be cached
print()

# ============================================
# BUILT-IN DECORATORS
# ============================================
print("=" * 60)
print("BUILT-IN DECORATORS")
print("=" * 60)

class MyClass:
    """Demonstrating built-in decorators"""

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """Property decorator - access like attribute"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Property setter"""
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value

    @staticmethod
    def static_method():
        """Static method - doesn't need instance"""
        return "I'm a static method"

    @classmethod
    def class_method(cls):
        """Class method - receives class as first argument"""
        return f"I'm a class method of {cls.__name__}"

obj = MyClass(10)
print(f"obj.value: {obj.value}")  # Using property
obj.value = 20  # Using setter
print(f"obj.value after update: {obj.value}")

print(f"\nStatic method: {MyClass.static_method()}")
print(f"Class method: {MyClass.class_method()}")
print()

# ============================================
# KEY TAKEAWAYS
# ============================================
print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Decorators extend function behavior without modifying the function
2. Use @decorator syntax for clean, readable code
3. Always use @functools.wraps to preserve function metadata
4. Common use cases:
   - Logging and debugging
   - Timing and performance monitoring
   - Caching results
   - Input validation
   - Retry logic for flaky operations
   - Authentication and authorization
5. In testing, decorators are great for:
   - Automatic screenshots on failure
   - Retry flaky tests
   - Setup and teardown operations
   - Test data generation
""")
