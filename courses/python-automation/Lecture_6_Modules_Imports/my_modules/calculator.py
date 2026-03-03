"""
Calculator module for basic math operations.
Demonstrates creating utility modules.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculate_percentage(value, total):
    """Calculate percentage."""
    if total == 0:
        return 0
    return (value / total) * 100

# Module constant
PI = 3.14159

# Code that runs only when module is run directly
if __name__ == "__main__":
    print("Calculator Module Test")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"50% of 200 = {calculate_percentage(50, 100) * 200 / 100}")
