"""
Exercise 2: *args, **kwargs, and Decorators

Instructions:
1. Complete each task below by implementing the required functions
2. Run the file to check your results
3. Pay attention to function signatures and decorator syntax

Estimated time: 25-30 minutes
"""

import functools
import time

# ============================================
# TASK 1: Function with *args
# ============================================
# Create a function that accepts any number of numbers and returns their average
# YOUR CODE HERE:
def calculate_average(*args):
    # Your implementation here
    pass

# Test your code (don't modify this)
print("=" * 50)
print("TASK 1: Calculate Average")
print("=" * 50)
print(f"Average of 10, 20, 30: {calculate_average(10, 20, 30)}")
print(f"Average of 5, 10, 15, 20, 25: {calculate_average(5, 10, 15, 20, 25)}")
print(f"Expected: 20.0 and 15.0")
print()

# ============================================
# TASK 2: Function with **kwargs
# ============================================
# Create a function that builds a query string from keyword arguments
# Example: build_query(name="Alice", age=25) -> "name=Alice&age=25"
# YOUR CODE HERE:
def build_query(**kwargs):
    # Your implementation here
    pass

# Test your code (don't modify this)
print("=" * 50)
print("TASK 2: Build Query String")
print("=" * 50)
query1 = build_query(name="Alice", age=25, city="NYC")
print(f"Query 1: {query1}")
query2 = build_query(search="python", page=1)
print(f"Query 2: {query2}")
print("Expected: name=Alice&age=25&city=NYC and search=python&page=1")
print()

# ============================================
# TASK 3: Combining Regular Params with *args
# ============================================
# Create a function greet_all(greeting, *names) that greets multiple people
# Example: greet_all("Hello", "Alice", "Bob") -> ["Hello, Alice!", "Hello, Bob!"]
# YOUR CODE HERE:
def greet_all(greeting, *names):
    # Your implementation here
    pass

# Test your code (don't modify this)
print("=" * 50)
print("TASK 3: Greet Multiple People")
print("=" * 50)
greetings = greet_all("Hello", "Alice", "Bob", "Charlie")
print(f"Greetings: {greetings}")
print(f"Expected: ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']")
print()

# ============================================
# TASK 4: Combining *args and **kwargs
# ============================================
# Create a function that formats a message with positional and keyword arguments
# def format_message(template, *args, **kwargs):
#     # Use args for positional placeholders {0}, {1}, etc.
#     # Use kwargs for named placeholders {name}, {age}, etc.
# YOUR CODE HERE:
def format_message(template, *args, **kwargs):
    # Your implementation here
    pass

# Test your code (don't modify this)
print("=" * 50)
print("TASK 4: Format Message")
print("=" * 50)
msg1 = format_message("Hello {0}, you are {1} years old", "Alice", 25)
msg2 = format_message("Hello {name}, you are {age} years old", name="Bob", age=30)
print(f"Message 1: {msg1}")
print(f"Message 2: {msg2}")
print("Expected: 'Hello Alice, you are 25 years old' and 'Hello Bob, you are 30 years old'")
print()

# ============================================
# TASK 5: Simple Decorator
# ============================================
# Create a decorator that prints "START" before and "END" after function execution
# YOUR CODE HERE:
def print_wrapper(func):
    # Your implementation here
    pass

@print_wrapper
def say_hello():
    print("Hello, World!")

# Test your code (don't modify this)
print("=" * 50)
print("TASK 5: Simple Decorator")
print("=" * 50)
print("Calling decorated function:")
say_hello()
print("Expected output: START, then 'Hello, World!', then END")
print()

# ============================================
# TASK 6: Decorator with Arguments
# ============================================
# Create a decorator that handles function arguments properly
# YOUR CODE HERE:
def log_args(func):
    # Your implementation here
    # Remember to use @functools.wraps and *args, **kwargs
    pass

@log_args
def add_numbers(a, b):
    return a + b

# Test your code (don't modify this)
print("=" * 50)
print("TASK 6: Decorator with Arguments")
print("=" * 50)
result = add_numbers(10, 20)
print(f"Result: {result}")
print("Expected: Should print args/kwargs and return 30")
print()

# ============================================
# TASK 7: Timing Decorator
# ============================================
# Create a decorator that measures and prints function execution time
# YOUR CODE HERE:
def timer(func):
    # Your implementation here
    pass

@timer
def slow_function():
    time.sleep(0.5)
    return "Done!"

# Test your code (don't modify this)
print("=" * 50)
print("TASK 7: Timing Decorator")
print("=" * 50)
result = slow_function()
print(f"Result: {result}")
print("Expected: Should print execution time around 0.5 seconds")
print()

# ============================================
# TASK 8: Decorator with Parameters
# ============================================
# Create a decorator factory that repeats function execution N times
# YOUR CODE HERE:
def repeat(times):
    # Your implementation here
    pass

@repeat(times=3)
def print_message(msg):
    print(f"  Message: {msg}")
    return msg

# Test your code (don't modify this)
print("=" * 50)
print("TASK 8: Repeat Decorator")
print("=" * 50)
results = print_message("Hello")
print(f"Returned: {results}")
print("Expected: Message printed 3 times, returns list of results")
print()

# ============================================
# TASK 9: Validation Decorator
# ============================================
# Create a decorator that validates function arguments
# If any argument is negative, raise ValueError
# YOUR CODE HERE:
def validate_positive(func):
    # Your implementation here
    pass

@validate_positive
def calculate_area(length, width):
    return length * width

# Test your code (don't modify this)
print("=" * 50)
print("TASK 9: Validation Decorator")
print("=" * 50)
try:
    area1 = calculate_area(5, 10)
    print(f"Area of 5x10: {area1}")

    area2 = calculate_area(-5, 10)
    print(f"Area of -5x10: {area2}")
except ValueError as e:
    print(f"Caught expected error: {e}")
print("Expected: First calculation succeeds, second raises ValueError")
print()

# ============================================
# BONUS TASK: Cache Decorator
# ============================================
# Create a decorator that caches function results
# If called with same arguments, return cached result
# YOUR CODE HERE:
def cache(func):
    # Your implementation here
    # Hint: Use a dictionary to store results
    pass

@cache
def expensive_calculation(n):
    print(f"  Computing {n}...")
    time.sleep(0.2)  # Simulate expensive operation
    return n * n

# Test your code (don't modify this)
print("=" * 50)
print("BONUS: Cache Decorator")
print("=" * 50)
print("First call:")
result1 = expensive_calculation(5)
print(f"Result: {result1}")
print("\nSecond call (should be cached):")
result2 = expensive_calculation(5)
print(f"Result: {result2}")
print("\nThird call with different arg:")
result3 = expensive_calculation(10)
print(f"Result: {result3}")
print("Expected: First call computes, second is cached, third computes")
print()

print("=" * 50)
print("Congratulations! You completed Exercise 2!")
print("=" * 50)
